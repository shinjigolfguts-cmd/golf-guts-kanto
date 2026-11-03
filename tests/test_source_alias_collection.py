"""Offline coverage regression for the three published non-image sources aliases.

No network request or fact/date update belongs to URL collection.
"""
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
from urllib.parse import urldefrag, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_sources import collect_urls


def legacy_collect_urls(value, urls):
    """Frozen pre-change collector: preserve its exact existing set."""
    if isinstance(value, dict):
        for key, item in value.items():
            if key in ('url', 'officialUrl') and isinstance(item, str):
                url = urldefrag(item.strip())[0]
                if urlsplit(url).scheme in ('http', 'https'):
                    urls.add(url)
            if key == 'supportingUrls' and isinstance(item, list):
                for link in item:
                    if isinstance(link, str) and urlsplit(link.strip()).scheme in ('http', 'https'):
                        urls.add(urldefrag(link.strip())[0])
            legacy_collect_urls(item, urls)
    elif isinstance(value, list):
        for item in value:
            legacy_collect_urls(item, urls)


class SourceAliasCollectionTests(unittest.TestCase):
    def urls(self, value):
        result = set()
        with patch('check_sources.urlopen', side_effect=AssertionError('No source requests in collection')), patch('socket.socket', side_effect=AssertionError('No network in offline tests')):
            collect_urls(value, result)
        return result

    def test_nested_sources_list_is_collected(self):
        self.assertEqual(self.urls({'courses': [{'comparison': {'stay': {'sources': ['https://example.test/faq/']}}}]}), {'https://example.test/faq/'})

    def test_alias_defragmentation_and_dedup_preserve_query(self):
        value = 'https://example.test/?cc_id=52&news_id=60309&p=guide.news_detail'
        self.assertEqual(self.urls({'url': value, 'sources': [value + '#one', value + '#two']}), {value})

    def test_non_https_relative_and_script_aliases_rejected(self):
        self.assertEqual(self.urls({'sources': ['http://example.test/', '//example.test/', '/local', 'javascript:alert(1)', 'data:text/plain,x', '']}), set())

    def test_invalid_auth_control_backslash_and_port_rejected(self):
        values = ['https://user:pass@example.test/', 'https://example.test/a\nb', 'https://example.test/a b', 'https://example.test/\\x', 'https://example.test:99999/', 'https://[invalid/']
        self.assertEqual(self.urls({'sources': values}), set())

    def test_alias_bad_types_not_coerced_to_urls(self):
        for value in [None, 3, True, 'https://example.test/', ['https://example.test/'], {'text': 'https://example.test/'}]:
            # An actual list is handled separately; scalar or nested list data
            # must not become an invented string URL.
            item = [value] if isinstance(value, list) else value
            with self.subTest(value=value):
                self.assertEqual(self.urls({'sources': item}), set())

    def test_menu_images_and_scalar_alias_not_expanded(self):
        self.assertEqual(self.urls({'menuImageUrl': 'https://example.test/menu.jpg', 'supportingUrl': 'https://example.test/guide', 'text': 'https://example.test/text'}), set())

    def test_legacy_canonical_collection_kept_exact(self):
        value = {'url': ' http://legacy.test/price#x ', 'officialUrl': 'https://legacy.test/home#x', 'supportingUrls': ['http://legacy.test/supplement#x', 'https://legacy.test/b#z'], 'nested': [{'url': 'https://legacy.test/nested'}], 'sources': [{'url': 'https://legacy.test/already-recursed'}]}
        old = set()
        legacy_collect_urls(value, old)
        self.assertEqual(self.urls(value), old)

    def test_collection_does_not_mutate_values_or_dates(self):
        value = {'sources': ['https://example.test/faq/#x'], 'checked': '2026-10-25', 'text': '未確認', 'conditions': '旧条件'}
        before = copy.deepcopy(value)
        self.urls(value)
        self.assertEqual(value, before)

    def test_current_snapshot_adds_only_the_three_approved_aliases(self):
        path = Path(__file__).resolve().parents[1] / 'data.js'
        before_bytes = path.read_bytes()
        data = json.loads(before_bytes.decode('utf-8-sig').split('=', 1)[1].strip().rstrip(';'))
        expected = {
            91: 'https://booking.pacificgolf.co.jp/sp/?cc_id=52&news_id=60309&p=guide.news_detail',
            109: 'https://www.minamitsukubagolf.com/faq/',
            110: 'https://kogalinks.com/sisetuannai',
        }
        for course_id, url in expected.items():
            course = next(c for c in data['courses'] if c['id'] == course_id)
            self.assertEqual(course['comparison']['stay']['sources'], [url])
        old = set()
        legacy_collect_urls(data, old)
        new = self.urls(data)
        self.assertEqual(old - new, set())
        self.assertEqual(new - old, set(expected.values()))
        self.assertEqual(len(new), len(old) + 3)
        self.assertEqual(path.read_bytes(), before_bytes)

    def test_takasaki_already_in_canonical_set_not_added_again(self):
        value = {'scenery': {'url': 'https://www.taiheiyoclub.co.jp/course/takasaki/guide.html'}, 'stay': {'supportingUrl': 'https://www.taiheiyoclub.co.jp/course/takasaki/guide.html'}}
        self.assertEqual(self.urls(value), {'https://www.taiheiyoclub.co.jp/course/takasaki/guide.html'})


if __name__ == '__main__':
    unittest.main()

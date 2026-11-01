import html
import json
from html.parser import HTMLParser
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from source_links import supplementary_sources


class SectionLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        if tag == 'section':
            self.current = []
            self.sections.append(self.current)
        elif tag == 'a' and self.current is not None:
            self.current.append(dict(attrs).get('href'))

    def handle_endtag(self, tag):
        if tag == 'section':
            self.current = None


class SupplementarySources(unittest.TestCase):
    def test_alias_order_and_deduplication(self):
        a, b, c = ('https://example.test/' + value for value in ('a', 'b', 'c'))
        self.assertEqual(supplementary_sources({'supportingUrls': [a], 'sources': [a, b], 'supportingUrl': c}), [a, b, c])
        self.assertEqual(supplementary_sources({'supportingUrls': [a, a], 'sources': [a], 'supportingUrl': a}), [a])

    def test_existing_primary_as_supplement_is_not_silently_removed(self):
        url = 'https://example.test/existing'
        self.assertEqual(supplementary_sources({'url': url, 'supportingUrls': [url]}), [url])

    def test_menu_image_is_not_part_of_this_change(self):
        self.assertEqual(supplementary_sources({'menuImageUrl': 'https://example.test/menu.jpg'}), [])

    def test_non_https_and_relative_links_are_rejected(self):
        for value in ['javascript:alert(1)', 'data:text/html,test', 'http://example.test/', '//example.test/', '/local', '']:
            with self.subTest(value=value):
                self.assertEqual(supplementary_sources({'sources': [value]}), [])

    def test_credentials_control_backslash_and_invalid_port_rejected(self):
        for value in ['https://user:password@example.test/', 'https://example.test/a\nb', 'https://example.test/a b', 'https://example.test/\\x', 'https://example.test:99999/', 'https://[invalid/']:
            with self.subTest(value=value):
                self.assertEqual(supplementary_sources({'supportingUrl': value}), [])

    def test_bad_metadata_types_are_not_interpreted_as_links(self):
        for fact in [{'sources': 'https://example.test/'}, {'sources': [{'url': 'https://example.test/'}]}, {'sources': [None, 4]}, {'supportingUrls': None}, {'supportingUrl': ['https://example.test/']}]:
            with self.subTest(fact=fact):
                self.assertEqual(supplementary_sources(fact), [])

    def test_query_ampersand_remains_exact_after_html_escape(self):
        value = 'https://example.test/?cc_id=52&news_id=60309&p=guide.news_detail'
        self.assertEqual(supplementary_sources({'sources': [value]}), [value])
        self.assertEqual(html.unescape(html.escape(value, quote=True)), value)


    def test_stored_aliases_rendered_in_their_own_sections(self):
        root = Path(__file__).resolve().parents[1]
        data = json.loads((root / 'data.js').read_text().split('=', 1)[1].strip().rstrip(';'))
        order = ('play', 'car', 'rail', 'dining', 'stay', 'budget', 'scenery')
        checked = []
        for course in data['courses']:
            parser = SectionLinks()
            parser.feed((root / f'courses/{course["id"]}.html').read_text())
            facts = [(key, course['comparison'].get(key)) for key in order if course['comparison'].get(key)]
            self.assertEqual(len(parser.sections), len(facts))
            for (key, fact), urls in zip(facts, parser.sections):
                expected = list(fact.get('sources') or [])
                if fact.get('supportingUrl'):
                    expected.append(fact['supportingUrl'])
                for value in expected:
                    self.assertEqual(urls.count(value), 1, f'{course["id"]}:{key}:{value}')
                    checked.append((course['id'], key))
        self.assertEqual(checked, [(91, 'stay'), (109, 'stay'), (110, 'stay'), (480, 'stay')])


if __name__ == '__main__':
    unittest.main()

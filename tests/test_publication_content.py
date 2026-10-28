import html
import json
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://shinjigolfguts-cmd.github.io/golf-guts-kanto/'


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value:
                self.urls.append(value)


class PublicationContent(unittest.TestCase):
    def test_internal_pages_and_assets_exist(self):
        for path in [*ROOT.glob('*.html'), *ROOT.glob('courses/*.html')]:
            parser = Links()
            parser.feed(path.read_text())
            base = ORIGIN + path.relative_to(ROOT).as_posix()
            for value in parser.urls:
                absolute = urljoin(base, value)
                if not absolute.startswith(ORIGIN):
                    continue
                relative = unquote(urlsplit(absolute).path.removeprefix('/golf-guts-kanto/'))
                target = ROOT / (relative or 'index.html')
                self.assertTrue(target.is_file(), f'{path.name}: {value}')

    def test_course_pages_preserve_conditions_dates_and_supporting_sources(self):
        data = json.loads((ROOT / 'data.js').read_text().split('=', 1)[1].strip().rstrip(';'))
        for course in data['courses']:
            page = (ROOT / f'courses/{course["id"]}.html').read_text()
            fields = course['comparison'].values()
            if any(value is None for value in fields):
                self.assertIn('設備やサービスがないという意味ではありません', page)
            self.assertIn(html.escape(course.get('officialUrl') or course['url'], quote=True), page)
            for fact in fields:
                if not fact:
                    continue
                for value in [fact['text'], fact.get('checked'), fact.get('conditions'), *fact.get('supportingUrls', [])]:
                    if value:
                        self.assertIn(html.escape(value, quote=True), page)


if __name__ == '__main__':
    unittest.main()

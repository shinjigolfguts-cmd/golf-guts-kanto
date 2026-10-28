import json,xml.etree.ElementTree as ET
from pathlib import Path
r=Path(__file__).resolve().parents[1];d=json.loads((r/'data.js').read_text().split('=',1)[1].strip().rstrip(';'));urls=[x.text for x in ET.parse(r/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')];assert len(urls)==503 and len(set(urls))==503
for c in d['courses']:
 p=f'courses/{c["id"]}.html';s=(r/p).read_text();assert '<h1>' in s and 'rel="canonical"' in s and p in (r/'all-courses.html').read_text()
assert len(list((r/'courses').glob('*.html')))==500
print('500 course pages, crawlable directory, 503 unique sitemap URLs passed')

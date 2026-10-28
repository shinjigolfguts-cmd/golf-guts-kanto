"""Render crawlable course pages from the current verified data; no invented facts."""
import json,html
from pathlib import Path
R=Path(__file__).resolve().parents[1]; origin='https://shinjigolfguts-cmd.github.io/golf-guts-kanto/'
d=json.loads((R/'data.js').read_text().split('=',1)[1].strip().rstrip(';'));esc=lambda v:html.escape(str(v),quote=True)
labels={'play':'プレーの特徴','car':'車でのアクセス','rail':'電車でのアクセス','dining':'食事','stay':'宿泊・お風呂','budget':'予算の目安','scenery':'景色'}
style='body{margin:0;background:#E8DFD3;color:#3F3A36;font:16px/1.9 sans-serif}main{max-width:880px;margin:auto;padding:28px 20px}a{color:#4F6B57}section{background:#f4efe7;padding:20px;margin:20px 0;border-top:3px solid #4F6B57}h1{font-family:serif}small{display:block;color:#716b62}li{margin:12px 0}'
def page(title,desc,path,body):
 return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} | GOLF GUTS</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{origin+path}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{origin+path}"><meta property="og:image" content="{origin}assets/golf-lake-sunset.png"><style>{style}</style></head><body><main><a href="{origin}">GOLF GUTS — DESIGN YOUR GOLF LIFE</a>{body}<p><a href="{origin}find.html">４つの質問でコースを探す</a> ｜ <a href="{origin}all-courses.html">関東500コース一覧</a></p></main></body></html>'
(R/'courses').mkdir(exist_ok=True);links=[];urls=[origin,origin+'find.html',origin+'all-courses.html']
for c in d['courses']:
 path=f'courses/{c["id"]}.html';urls.append(origin+path)
 body=f'<h1>{esc(c["name"])}</h1><p>{esc(c["area"])}</p><p>{esc(c.get("feature",""))}</p>'
 missing=[label for key,label in labels.items() if not c.get('comparison',{}).get(key)]
 if missing:
  body+=f'<p>掲載情報が未確認の項目：{esc("・".join(missing))}。設備やサービスがないという意味ではありません。</p>'
 for key,label in labels.items():
  f=c.get('comparison',{}).get(key)
  if not f:continue
  body+=f'<section><h2>{label}</h2><p>{esc(f["text"])}</p>'
  if f.get('conditions'):body+=f'<p>{esc(f["conditions"])}</p>'
  body+=f'<a href="{esc(f["url"])}" rel="noopener noreferrer">出典を確認する</a>'
  for source in f.get('supportingUrls',[]):
   body+=f' <a href="{esc(source)}" rel="noopener noreferrer">補足の出典</a>'
  body+=f'<small>情報確認：{esc(f.get("checked","未確認"))}</small></section>'
 body+=f'<p><a href="{esc(c.get("officialUrl") or c["url"])}" rel="noopener noreferrer">公式案内・予約条件を確認する</a></p>'
 body+='<p>料金・施設の利用条件は日程やプランによって変わります。予約前に公式情報をご確認ください。</p>'
 (R/path).write_text(page(c['name'],c['area']+'のゴルフコース。アクセス・食事・料金などの掲載情報と出典を確認できます。',path,body))
 links.append(f'<li><a href="{path}">{esc(c["name"])}</a> — {esc(c["area"])}</li>')
(R/'all-courses.html').write_text(page('関東500コース一覧','関東1都6県の500コースを掲載。各施設の情報と出典をご覧いただけます。','all-courses.html','<h1>関東500コース一覧</h1><ul>'+''.join(links)+'</ul>'))
(R/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+esc(u)+'</loc></url>' for u in urls)+'</urlset>')
print('Generated 500 course pages, index and 503 sitemap URLs')

index=R/"index.html"
t=index.read_text()
if "href=\"all-courses.html\"" not in t:
    index.write_text(t.replace("</footer>","<p><a href=\"all-courses.html\">関東500コースを一覧で見る</a></p></footer>"))

"""Inventory missing fields; presence is not a claim of factual verification."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = {'play': 'プレー', 'car': '車のアクセス', 'rail': '電車のアクセス',
          'dining': '食事', 'stay': '宿泊・お風呂', 'budget': '料金', 'scenery': '景色'}


# Keep the same text-only rule used in the 2026-10-31 review notes.
# This is a review queue, not a completeness or truth classifier.
UNRESOLVED = re.compile(
    r'未確認|確認でき(?:てい(?:ません|ない)|ません|ない|ず|なかった)'
    r'|取得でき(?:てい(?:ません|ない)|ません|ない|ず|なかった)|不明'
)


def unresolved_inventory(data):
    rows = []
    for course in data['courses']:
        for key in LABELS:
            fact = course.get('comparison', {}).get(key)
            if not isinstance(fact, dict):
                continue
            text = fact.get('text', '')
            if UNRESOLVED.search(text):
                rows.append({'id': course['id'], 'name': course['name'],
                             'field': key, 'text': text,
                             'url': fact.get('url', ''),
                             'checked': fact.get('checked')})
    return rows


def inventory(data):
    missing = []
    for course in data['courses']:
        fields = [key for key in LABELS
                  if not (course.get('comparison', {}).get(key) or {}).get('text', '').strip()]
        if fields:
            missing.append({'id': course['id'], 'name': course['name'], 'fields': fields,
                            'officialUrl': course.get('officialUrl') or course['url']})
    return missing


def main():
    raw = (ROOT / 'data.js').read_bytes()
    data = json.loads(raw.decode().split('=', 1)[1].strip().rstrip(';'))
    rows = inventory(data)
    counts = {key: sum(key in row['fields'] for row in rows) for key in LABELS}
    text = '# 掲載情報の残作業一覧\n\n'
    text += 'data.js SHA256: `' + hashlib.sha256(raw).hexdigest() + '`\n\n'
    text += ('この一覧は空欄の所在を示すもので、完成率ではありません。'
             '情報がある項目も、全件の再検証が済んだという意味ではありません。'
             '未確認と「設備・サービスなし」を区別し、根拠のない補完はしません。\n\n')
    text += '| 項目 | 空欄数 |\n|---|---:|\n'
    text += ''.join(f'| {LABELS[key]} | {count} |\n' for key, count in counts.items())
    text += f'\n空欄を含む施設：{len(rows)} / {len(data["courses"])}。項目数には同じ施設の重複があります。\n\n'
    text += '## 空欄のある項目\n\n'
    text += ('公式本文・料金条件・送迎予約条件を確認し、施設IDと出典を照合して差分更新します。'
             'これは調査作業であり、利用者のパソコン操作待ちではありません。\n\n')
    text += '| ID | 施設 | 未確認の項目 |\n|---:|---|---|\n'
    for row in rows:
        name = row['name'].replace('|', '\\|')
        text += f'| {row["id"]} | [{name}]({row["officialUrl"]}) | {"・".join(LABELS[k] for k in row["fields"])} |\n'
    unresolved = unresolved_inventory(data)
    unresolved_counts = {key: sum(row['field'] == key for row in unresolved) for key in LABELS}
    text += '\n## 本文に未確認表現が残る項目\n\n'
    text += ('空欄とは別集計です。一部の条件だけ未確認の欄も含みます。'
             '表現の機械抽出であり、全事実の未確認件数や完成率ではありません。'
             '該当表現がない項目も、確認済みと認定しません。\n\n')
    text += '| 項目 | 未確認表現を含む欄数 |\n|---|---:|\n'
    text += ''.join(f'| {LABELS[key]} | {count} |\n' for key, count in unresolved_counts.items())
    text += (f'\n合計：{len(unresolved)}欄 / '
             f'{len({row["id"] for row in unresolved})}施設。'
             'IDと項目の組み合わせで重複を除外。\n\n')
    text += ('抽出規則：`' + UNRESOLVED.pattern + '`（comparison.textのみ）。'
             '2026-10-31のレビュー記録と同じ規則を維持します。\n\n')
    text += '| ID | 施設 | 項目 | 掲載本文（確認待ちの理由を含む） |\n|---:|---|---|---|\n'
    for row in unresolved:
        cells = [str(row['id']), row['name'], LABELS[row['field']], row['text']]
        text += '| ' + ' | '.join(c.replace('|', '\\|').replace('\n', ' ') for c in cells) + ' |\n'
    (ROOT / 'docs/maintenance/unresolved-status.json').write_text(json.dumps({
        'dataSha256': hashlib.sha256(raw).hexdigest(),
        'scope': 'comparison.text marker inventory; not factual completeness',
        'pattern': UNRESOLVED.pattern, 'counts': unresolved_counts,
        'fieldCount': len(unresolved),
        'courseCount': len({row['id'] for row in unresolved}),
        'entries': unresolved,
    }, ensure_ascii=False, indent=2) + '\n')
    (ROOT / 'docs/maintenance/content-status.md').write_text(text)
    print(json.dumps({'missing': counts, 'courses_with_missing_fields': len(rows)}, ensure_ascii=False))


if __name__ == '__main__':
    main()

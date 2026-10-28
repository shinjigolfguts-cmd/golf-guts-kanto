"""Inventory missing fields; presence is not a claim of factual verification."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = {'play': 'プレー', 'car': '車のアクセス', 'rail': '電車のアクセス',
          'dining': '食事', 'stay': '宿泊・お風呂', 'budget': '料金', 'scenery': '景色'}


def inventory(data):
    missing = []
    for course in data['courses']:
        fields = [key for key in LABELS if not course.get('comparison', {}).get(key)]
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
    text += '## 次に調べる項目\n\n'
    text += ('公式本文・料金条件・送迎予約条件を確認し、施設IDと出典を照合して差分更新します。'
             'これは調査作業であり、利用者のパソコン操作待ちではありません。\n\n')
    text += '| ID | 施設 | 未確認の項目 |\n|---:|---|---|\n'
    for row in rows:
        name = row['name'].replace('|', '\\|')
        text += f'| {row["id"]} | [{name}]({row["officialUrl"]}) | {"・".join(LABELS[k] for k in row["fields"])} |\n'
    (ROOT / 'docs/maintenance/content-status.md').write_text(text)
    print(json.dumps({'missing': counts, 'courses_with_missing_fields': len(rows)}, ensure_ascii=False))


if __name__ == '__main__':
    main()

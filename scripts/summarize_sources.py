"""Create human-readable reports without changing course facts or verdicts."""
import csv
import json
import os
from collections import Counter
from pathlib import Path


def classify(row):
    code = row.get('http_status')
    error = row.get('error', '').lower()
    if row.get('status') == 'reachable':
        return '接続成功'
    if code in (404, 410):
        return 'ページなし（要確認）'
    if code in (401, 403, 429):
        return '認証・アクセス制限'
    if isinstance(code, int) and code >= 500:
        return '接続先サーバーエラー'
    if 'timed out' in error or 'timeout' in error:
        return 'タイムアウト'
    if 'ssl' in error or 'certificate' in error:
        return '証明書・TLS'
    return 'その他・要確認'


def csv_cell(value):
    value = str(value if value is not None else '')
    return "'" + value if value.startswith(('=', '+', '-', '@', '\t', '\r', '\n')) else value


def write_summary(report, folder):
    rows = report['results']
    complete = (report.get('complete') is True and report.get('pending') == 0
                and len(rows) == report['total'])
    counts = Counter(classify(row) for row in rows)
    lines = ['## 関東版・参照URL確認',
             f"確認対象: {report['total']}件 / 確認済み: {len(rows)}件",
             f"接続成功: {counts['接続成功']}件 / 要確認: {len(rows) - counts['接続成功']}件",
             '完了' if complete else '未完了：途中までの結果です。', '',
             '| 判定 | 件数 |', '| --- | ---: |']
    lines.extend(f'| {label} | {count} |' for label, count in sorted(counts.items()))
    lines += ['', 'URLの接続確認のみです。掲載内容の正確性は未検証です。',
              '通信失敗だけでは閉鎖・リンク切れとは断定できません。',
              '掲載データと内容確認日は変更していません。',
              'Artifacts の kanto-source-check に全件CSV・要確認CSV・JSONを保存します。']
    text = '\n'.join(lines) + '\n'
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'source-check-summary.md').write_text(text, encoding='utf-8')
    for name, selected in [('source-check.csv', rows), ('needs-review.csv', [r for r in rows if r.get('status') != 'reachable'])]:
        with (folder / name).open('w', encoding='utf-8-sig', newline='') as handle:
            writer = csv.writer(handle)
            writer.writerow(['判定', 'URL', 'HTTP', '転送先', '接続確認時刻', '詳細'])
            for row in selected:
                writer.writerow(map(csv_cell, [classify(row), row['url'], row.get('http_status'), row.get('final_url'), row.get('checked_at'), row.get('error')]))
    return text, complete


def main():
    folder = Path(__file__).resolve().parents[1] / 'reports'
    report = json.loads((folder / 'source-check.json').read_text(encoding='utf-8'))
    text, complete = write_summary(report, folder)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as handle:
            handle.write(text)
    print(text)
    if not complete:
        raise SystemExit('確認未完了：途中結果を保存しました。')
    if any(row.get('status') != 'reachable' for row in report['results']):
        print('::error::要確認URLがあります。needs-review.csvを確認してください。')
        raise SystemExit(1)


if __name__ == '__main__':
    main()

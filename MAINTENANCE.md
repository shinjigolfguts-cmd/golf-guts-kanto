# 関東版の更新
対象 shinjigolfguts-cmd/golf-guts-kanto のみ。500施設と現在のデザイン・保存キーを維持。

- 毎週のsource-check.ymlは通信を確認し、全件CSVと要確認CSVを保存する。404/410と未完了は失敗、その他通信問題は警告。警告は未解決であり正常判定ではない。
- 掲載事実の更新は公式本文で裏付け、施設ID/名称、旧値、出典URL、確認日、根拠、料金条件をJSON台帳へ保存する。HTTP成功だけで確認日を進めない。
- scripts/apply_verified_updates.py はbaseSha256、reviewed=true、reviewer、updatesを持つJSONを検証する。updatesの要素はid/name/field/before/after/evidenceNote。afterにはtext/url/checked/sourceType=official、料金にはconditionsを含める。
- ドライラン後--applyで適用し、検索と単体テストを通す。古いバッチを再適用しない。
- updates/*.json追加で「確認済み情報の更新案」が自動実行し、適用結果data.jsを成果物に保存。これは自動公開ではない。公式根拠のレビューとmainへの反映は担当者/接続したエージェントが行う。main反映後は既存Pages公開処理を確認する。
- SEO: index.html/find.htmlのcanonical、OGP、sitemap.xmlを維持。Search Console所有権確認とインデックス登録は別作業。GitHub Pagesサブパス内robots.txtはルートrobots設定にならない。
- 全件内容確認は未完了。2026-10-28時点の空欄: budget298/stay237/rail41（重複あり）。検索の正常動作とは区別する。

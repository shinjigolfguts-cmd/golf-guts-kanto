# 関東版の更新
対象 shinjigolfguts-cmd/golf-guts-kanto のみ。500施設と現在のデザイン・保存キーを維持。

- 毎週のsource-check.ymlは通信を確認し、全件CSVと要確認CSVを保存する。404/410と未完了は失敗、その他通信問題は警告。警告は未解決であり正常判定ではない。
- 掲載事実の更新は公式本文で裏付け、施設ID/名称、旧値、出典URL、確認日、根拠、料金条件をJSON台帳へ保存する。HTTP成功だけで確認日を進めない。
- scripts/apply_verified_updates.py はbaseSha256、reviewed=true、reviewer、updatesを持つJSONを検証する。updatesの要素はid/name/field/before/after/evidenceNote。afterにはtext/url/checked/sourceType=official、料金にはconditionsを含める。
- ドライラン後--applyで適用し、検索と単体テストを通す。古いバッチを再適用しない。
- SEO: index.html/find.htmlのcanonical、OGP、sitemap.xmlを維持。Search Console所有権確認とインデックス登録は別作業。GitHub Pagesサブパス内robots.txtはルートrobots設定にならない。
- 全件内容確認は未完了。2026-10-28時点の空欄: budget298/stay237/rail41（重複あり）。検索の正常動作とは区別する。

## 2026-10-28 自動反映
updates/*.jsonの確認済みバッチ追加で、検証→反映→500施設の検索用ページ生成→main保存→既存Pages公開→公開data.jsのSHA256照合まで自動実行する。失敗はActionsで赤く表示され、同時変更のpushは拒否される。処理済みバッチはapplied_updatesへ移動する。公式本文の収集・解釈・reviewed承認は担当エージェントが行い、HTTP成功で事実を作らない。Search ConsoleのGoogle所有権確認は未実施。
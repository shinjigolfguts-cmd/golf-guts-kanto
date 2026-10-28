# 関東版の更新
対象 shinjigolfguts-cmd/golf-guts-kanto のみ。500施設と現在のデザイン・保存キーを維持。

## 旧ZIPの利用中止と差分更新
- `kanto-maintenance-20261028.zip` をアップロードする案内は撤回。現行mainより古いデータ・サイト構成を含むため、使用しない。
- 修正はGitHubの最新mainを取得して開始し、追加済みの掲載情報、`applied_updates/` の更新台帳、500施設の個別ページ、自動反映処理を保持する。
- 適用前にmainのコミットを再確認する。同時更新があれば最新mainへ差分を載せ直し、データ保持とテストを再確認する。古いZIPや古いdata.jsで一括上書きしない。
- 参照URL確認は一時的なタイムアウト・接続リセット・HTTP500/502/503/504に限り3秒後に1回再試行する。再試行前の結果を保存し、証明書検証や認証を回避しない。検査時間は従来より長くなる場合がある。

- 毎週のsource-check.ymlは通信を確認し、全件CSVと要確認CSVを保存する。404/410と未完了は失敗、その他通信問題は警告。警告は未解決であり正常判定ではない。
- 掲載事実の更新は公式本文で裏付け、施設ID/名称、旧値、出典URL、確認日、根拠、料金条件をJSON台帳へ保存する。HTTP成功だけで確認日を進めない。
- scripts/apply_verified_updates.py はbaseSha256、reviewed=true、reviewer、updatesを持つJSONを検証する。updatesの要素はid/name/field/before/after/evidenceNote。afterにはtext/url/checked/sourceType=official、料金にはconditionsを含める。
- ドライラン後--applyで適用し、検索と単体テストを通す。古いバッチを再適用しない。
- SEO: index.html/find.htmlのcanonical、OGP、sitemap.xmlを維持。Search Console所有権確認とインデックス登録は別作業。GitHub Pagesサブパス内robots.txtはルートrobots設定にならない。
- 全件内容確認は未完了。最新の空欄数と施設別内訳は docs/maintenance/content-status.md を参照（更新時に自動生成、重複あり）。検索の正常動作とは区別する。

## 2026-10-28 自動反映
updates/*.jsonの確認済みバッチ追加で、検証→反映→500施設の検索用ページ生成→main保存→既存Pages公開→公開data.jsのSHA256照合まで自動実行する。失敗はActionsで赤く表示され、同時変更のpushは拒否される。処理済みバッチはapplied_updatesへ移動する。公式本文の収集・解釈・reviewed承認は担当エージェントが行い、HTTP成功で事実を作らない。Search ConsoleのGoogle所有権確認は未実施。

## 完成条件と残作業
[完成までの確認事項](docs/maintenance/completion-checklist-20261028.md) と [施設別の空欄一覧](docs/maintenance/content-status.md) を参照。公開済み・動作検証済み・内容確認済みは別々に報告する。本人認証待ちと調査未完了を、PCがないための待機と混同しない。

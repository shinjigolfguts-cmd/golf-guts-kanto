# 追加調査 bt・bs公開証跡（2026-10-30）

基準main: 6fa0f362c57499d9e870359c45b9cefce8c163cc。最新mainをfetchし別worktreeで確認。MAINTENANCE.md、facilities-followup-20261029.md、followup-20261030bs.mdを再読。

## 公開検証
bsの3施設3料金項目は適用・公開完了。
- Actions run: https://github.com/shinjigolfguts-cmd/golf-guts-kanto/actions/runs/41018858967
- job123941314379: 公式根拠付き更新、公開前検証、保存、Pages公開と反映確認すべてsuccess。
- ログ2026-10-30T07:15:48Z: Published and verified 6fa0f362c57499d9e870359c45b9cefce8c163cc
- Pages run41018877076もsuccess。
- mainのdata.js SHA256: 742d3e9518de186882bb191a18497a352766ae3fca14c60008423da3d59834d3。ローカル検証済みbsと一致。
- 最新mainを再集計しnull77項目。brとbs合計8施設8項目を公開済み。
- null77は未解決の総件数ではない。過去に未確認説明を入力した項目・部分未確認も残っている。0件完了と報告しない。

## 新たな調査・不採用理由
|ID|調査先|実際の確認結果・残課題|
|---|---|---|
|157|https://www.hillsgolf.jp/shishido/ → https://wst1.asts.jp/golfnet/cc/0308CC/plan/ → plan_view.asp?p_no=1087 および index.asp?D=20261104&P=1087&m=e|一覧・プラン詳細は東セルフWeb優待17,200円、3B660円2B1,980円。一方11/4日付詳細は0円を返し、アイコンもセルフに対してキャディ付と矛盾。0円を無料とせず、日付料金と食事条件の不整合が解決するまで未採用。|
|399|https://www.belle-co.com/belleselva/|タイムアウト後、1回再試行で502。食事本文取得不能。検索で出た宇都宮のBistro BelleSelvaは別施設であり流用しない。|
|426|https://www.kasumigasekicc.or.jp/information/index.html|予約は会員経由、平日は同伴または紹介、土日祝は同伴という条件を本文確認。プレー価格は当該公開本文に見つからず。条件だけで価格の空欄を解消しない。|
|425|https://www.olympicnational.co.jp/west/fee.html → reservation.html → https://www.jgo-os.com/11117/003/reserve/|公式料金本文はカート割増等で基本料金は予約カレンダー参照。WEST専用ビジター予約リンクを辿ったが「ゴルフ場情報の取得に失敗しました」。EASTの料金や第三者価格を転用しない。|
|139|https://booking.pacificgolf.co.jp/guide/178.html → ?cc_id=178&p=guide.access_map および ?cc_id=178&p=guide.gallery|公式ゴルフ場情報本文は交通・レンタル等。ギャラリーにレストラン見出しはあるが料理や営業時間の本文を取得できず。検索結果のPGM南市原、市原GC市原コースは別施設なので不採用。|

今回は新規の確定データ差分なし。上記調査は同じ方法で反復せず、予約表示不整合・取得制限・画像内容の別途確認が必要。情報不存在とは断定しない。未確認を施設なしに変換しない。Search Consoleと既存通知は変更していない。

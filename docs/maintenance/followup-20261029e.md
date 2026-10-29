# 2026-10-29 追加調査 e

基準main: `af505d1f78573c7e9e3362b75ece466d432579dc`。MAINTENANCE.md、facilities-followup-20261029.md、最新引継ぎ followup-20261029d.md を読んで開始。旧ZIPは不使用。

## 確認済み差分

6コース9項目（新規5・既存補足4）。前後値・出典・確認日・根拠・条件は `verified-followup-20261029e.json`（適用後は `applied_updates/`）に保存。

|ID|コース|内容|
|---|---|---|
|5|江戸川ライン|アイアンのみ、予約不要、回り放題、レンタル・更衣室制限、悪天候休場|
|6|アジア取手|男女浴室。宿泊・プラン別浴室条件は未確認と明記|
|21|ムーンレイク茂原|通年ナイト、カート乗り入れ料金・除外条件。クラブバスなしを追加し既存の駅から車13分を保持|
|40|本千葉|公式本文で昼食3品を確認|
|62|藤岡|公式画像で昼食3品を目視確認、ランチのみ営業|
|73|うぐいすの森馬頭|昼食3品と昼食付き条件。ホテル客室・禁煙・温泉。10〜11月の料金表表示額と2B割増条件|

料金表の税の内外表記が明確でないため、馬頭の税込支払総額は推測していない。`priceVerified=false` とし価格絞り込みの確定総額には使わない。12月・年末年始に10〜11月料金を流用しない。

## 主出典

- https://edogawaline.or.jp/ショートコース/
- https://www.asia-toride.com/facility.html
- https://booking.pacificgolf.co.jp/?cc_id=65&p=guide.access_map
- https://honchiba-cc.co.jp/menu_item/
- https://reserve.accordiagolf.com/golfCourse/gunma/fujioka/restaurant
- https://reserve.accordiagolf.com/images/restaurantMenus/126_2_20260930165355.jpg.webp
- https://umgc.jp/bato/施設案内/
- https://umgc.jp/bato/wp-content/uploads/2026/07/lunchmenu20260708.jpg
- https://umgc.jp/bato/price/
- https://umgc.jp/bato/wp-content/uploads/2026/10/202610-202612_list-price-1024x1447.jpg

料理・料金画像は目視確認に使用し、サイトへ転載していない。HTTP成功だけで内容確認済みにはしていない。

## 未確認・採用しなかった調査

確認日はいずれも2026-10-29。同じ失敗先を無条件に繰り返さず、次回は未調査群を優先する。

|ID|調査先|結果・残件|
|---|---|---|
|5|https://edogawaline.or.jp/ショートコース/|食事・浴場・宿泊の明示なし。ロッカー・更衣室なしから宿泊や浴場なしとは推論しない|
|6|https://www.asia-toride.com/ と facility.html|施設案内はバイキング、トップの感染症対応案内はワンプレート＋一部バイキング。現行の料理名・運用を確定できず dining は空欄維持|
|18|https://www.pacificgolf.co.jp/tokyobayside/index.asp|本文抽出はiframeのみ。https://booking.pacificgolf.co.jp/guide/159.html の現行本文は取得できたが具体的料理・料金は未掲載。女性向け施設リンク https://angel.pacificgolf.co.jp/recommend/ はタイムアウト|
|21|https://booking.pacificgolf.co.jp/?cc_id=65&p=guide.gallery|本文とHTMLの公開画像一覧から具体的料理メニューを確認できず。食事・浴場・プレー総額は未確認|
|40|https://honchiba-cc.co.jp/price/|料金本文なし。HTMLの公開画像・iframeにも料金表を確認できず。budget空欄維持|
|62|https://reserve.accordiagolf.com/golfCourse/gunma/fujioka/|本文サイズ上限エラー。別の公式detailとrestaurantは取得できた。予約総額は未確認、既存浴室情報は重複更新しない|
|73|https://umgc.jp/bato/price/ と 各種利用料金/|一般料金表の「利用税600円・消費税」は内外税が明示されない。ジュニア料金の税込注記を一般料金へ転用しない。総額確認が残る|
|84|https://dynamic-golf.jp/chiba/|かぼちゃハウスの施設名・営業時間を確認。リンク先 https://www.mars.dti.ne.jp/~rasta/chiba/restauran.htm は初回タイムアウト、再試行でも取得できず。具体的料理は未確認|

## 検証と残件

ドライラン・適用成功。500 IDを保持し、9項目以外の全データが不変であることを構造比較で確認。分類、デザイン、お気に入りコードは変更していない。
384検索条件、Python 11テスト、data.js/finder.js構文、500ページ・503URL SEO検査、git diff --check が成功。

未入力は669→664（食事116、宿泊177、料金286、景色42、電車35、車8）。空欄を含むコースは383。部分記載の精査は別途残る。空欄減少を完成率として扱わない。
この実行のd/e合計は13コース23項目、新規13・既存補足10。全件完遂ではない。
次回は最新mainと本記録を読み、未調査群（例：ID58・63・81・83・87・89・92の食事・宿泊・料金）を優先する。先に各IDの最新値と過去記録を照合する。
Google Search Console非公開状態は確認していない。既存の10月30日通知は変更していない。

## 公開結果

投入コミット `ea9a4e083dee921f090daedd0b8d61ee8e8c3d55`、適用コミット `d16a964ec5c1f51f419036d2f5741d32f79cc76f`。
verified-update 実行 `40814813835` は成功。実サイトの data.js と対象6コースのHTMLを `?revision=d16a964ec5c1f51f419036d2f5741d32f79cc76f` 付きURLで取得し、ローカルでテストした生成物と全件バイト一致を確認。
data.js SHA256: `fe95ef5ae9d057a9dcfe0ee58c27c21e18c75e908122ef3c5a4210867b43be89`。
公開直前に開始したクエリなしURLの取得では旧d版が返ったため、反映検証では公開リビジョンを明示した。閲覧キャッシュの反映と公開元の一致を区別する。
その後、通常のクエリなし data.js も再取得し、上記の最新SHA256との一致を確認した。

# 2026-10-29 追加調査 h

基準main: 332ba44faae65d998dafddc0427e36c727a342f4。MAINTENANCE.md、facilities-followup-20261029.md、最新引継ぎfollowup-20261029g.mdを確認。旧ZIPは不使用。

## 確認済み差分

7コース9項目（新規8、既存補足1）。台帳 verified-followup-20261029h.json は適用後 applied_updates/ に保存。全項目に旧値・出典・確認日2026-10-29・根拠を記録。

- ID134 チェックメイト：実際の昼食料理とセルフデーの食事・営業時間条件。
- ID139 PGM市原：既存18Hを保持し、起伏・丘陵・セルフ/キャディ選択制を補足。
- ID166 日光：現行昼食料理、ロッヂ部屋数・浴場時間・利用期間、2026通常期ビジター4B料金と税・人数・追加手当・会員紹介条件。
- ID172 小幡郷：昼食と朝食の料理。プラス表示は追加額として扱い、単品総額にはしない。
- ID173 甘楽：具体的な昼食料理、通常営業時間と12月土日祝の例外。
- ID176 妙義：具体的な昼食料理、早期閉店の可能性と外来事前問合せ。
- ID177 南総：実際の昼食料理と食事付きプランの上限。台風復旧中の既存プレー運用は保持。

未入力654→646。食事101、宿泊・お風呂175、料金285、景色42、電車35、車8、プレー0。空欄あり378コース。空欄がない項目にも部分未確認があり、全件内容確認完了ではない。

## 調査先と未確認理由

|ID|調査先|今回の確認と残件|
|---|---|---|
|134|https://checkmate-cc.com/restaurantmenu.html 、 https://checkmate-cc.com/availability.html 、 https://checkmate-cc.com/faci.html|昼食画像20261003gmenu_page-0001.jpgを目視。宿泊・浴場条件は確認できず空欄維持。料金ページに会員料金はあるがゲスト料金のカレンダー部分を確認できずbudget未入力。会員料金をゲスト料金に転用しない|
|139|https://booking.pacificgolf.co.jp/guide/178.html 、 https://booking.pacificgolf.co.jp/?cc_id=178&p=guide.access_map 、 https://booking.pacificgolf.co.jp/?cc_id=178&p=guide.gallery|現行運営会社の本文を確認。ギャラリーはレストラン等の見出しのみで料理や施設利用条件を確認できない。dining/stay/budgetは未入力のまま。存在しないとは判断しない|
|163|https://www.president-cc.jp/|取得タイムアウト、3秒以上経過後に1回再試行したが再度タイムアウト。今回は変更なし。dining/budget未入力。次回同じ失敗先を無条件反復しない|
|166|https://www.nikkocc.or.jp/guide/ 、 https://www.nikkocc.or.jp/guide/facilities/ 、同サイトの guide/images/20251201.pdf と guide/facilities/images/3-lanch20261007.pdf|本文とPDFを取得。料金表全体・メニュー1頁目を画像でも確認。終了済み2025/12〜2026/2の冬料金は現在料金にしない。浴場22時は宿泊者向け条件。料金は4B概算、12月手当や人数による増額を条件に記録|
|172|https://www.obatago-golf.com/restaurant/ 、 https://www.obatago-golf.com/pdf/menu.pdf 、 https://www.obatago-golf.com/detail/|wwwなしトップは取得ツールでアクセス不可。既存データのwww付き公式に進んで本文・現行PDF画像を確認。昼食プラス額と料理総額を区別。プレー料金budgetは未解消|
|173|https://reserve.accordiagolf.com/golfCourse/gunma/kanra/restaurant|現行ランチ画像118_24_20261004165048.jpg.webpを目視。料理価格や昼食差額は確認できないため追加しない。プレー料金budgetは未解消|
|176|https://reserve.accordiagolf.com/golfCourse/gunma/myogi/restaurant|現行ランチ画像073_8_20261001073315.jpg.webpを目視。料理価格や昼食差額は確認できないため追加しない。プレー料金budgetは未解消|
|177|https://nanso-cc.com/restaurant/|現行2026/10/lunch01.jpgを目視。食事付きプランは1,650円までという条件を確認。すべてのプレーに食事が付くとは記載しない。営業時間は今回未確認|

公式画像・PDF自体は転載していない。出典画像URLは台帳にも保存。HTTP成功だけで内容確認とは扱っていない。過去の403/429等の取得不能先は再試行していない。

## ローカル検証

ドライラン→適用→ページ/残件生成を実施。384検索条件、Python11テスト、data.js/finder.js構文、500ページ/503URLのSEO検査、git diff --check通過。独立構造比較で500 ID、分類、9項目以外の全データを保持。デザイン・お気に入り機能のコード変更なし。

公開・公開実物照合はこの文書の公開結果欄で追記する。全件未完了のため継続対象。Search Console非公開ステータス未閲覧、10月30日の通知は未変更。

## 公開結果

入力コミット660b106b8493c3653082fcad20c8c60ee1cb936b、反映コミット20a28721b0b50a493a13384ecf26d77bc0ae0e05。verified-update実行40824557112は2026-10-29 05:39:30 UTCに成功。公開data.jsと7個別ページ（134/139/166/172/173/176/177）の計8ファイルをローカル検証済み生成物とバイト照合し全一致。data.js SHA256:722c02a2b978680802f113825663f41f2291078db9fbe9e7191eee87694a1b22。7コース9項目を公開・反映検証済み。

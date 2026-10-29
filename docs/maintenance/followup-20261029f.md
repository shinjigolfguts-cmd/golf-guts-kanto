# 2026-10-29 追加調査 f

基準main: 87e717e49a99e5b4fe4b7a158fd09c135e5447a8。MAINTENANCE.md、facilities-followup-20261029.md、最新followup-20261029e.mdを読んで開始。旧ZIPは不使用。

## 差分と検証

6コース8項目（新規3・既存補足5）。前後値・出典・条件は verified-followup-20261029f.json（処理後applied_updates）に保存。
- ID58 イーグルレイク：食事営業時間・朝食なし、カート条件。
- ID63 東京相武：食事営業時間・予約条件。料理画像は未確認。
- ID81 鶴舞：ホテル夕食の事前予約期限・営業時間。客室浴室・禁煙・入退室時間・2026年9月改定後の宿泊料金。ゴルフ料金と混同しない。
- ID83 市原：通年ナイト・GPSセルフ。既存LED情報を保持。
- ID87 川崎リバーサイド：1名受付と4名組プレー、平日と休日の予約方法、練習場条件。
- ID92 岡部美里：岡部駅からクラブバス約12分を追加。既存の車10分、岡部で受付・美里へ移動という区別を保持。

未入力664→661（食事113、宿泊177、料金286、景色42、電車35、車8）。空欄あり383コース。新規食事項目はいずれも部分補完で、昼食の具体的料理名は未確認。未入力の減少は調査完了数ではない。

500 IDと8項目以外のデータが不変であることを構造比較。384検索条件、Python11テスト、JS構文、500ページ・503URL SEO検査、diff検査を通過。デザイン・分類・お気に入りコードを変更していない。

## 調査済み・未確認の記録

確認日2026-10-29。以下の不明点を「施設なし」や料金の推測で埋めない。

|ID|調査先|結果と残件|
|---|---|---|
|58|https://booking.pacificgolf.co.jp/?cc_id=59&p=guide.access_map と https://booking.pacificgolf.co.jp/guide/59.html|営業時間本文は確認。料理・浴室・宿泊・プレー料金は本文で確認できず|
|63|https://reserve.accordiagolf.com/golfCourse/tokyo/sobu/restaurant|営業時間本文取得。掲載ランチ画像 https://reserve.accordiagolf.com/images/restaurantMenus/149_43_20260806085227.jpg.webp は403。迂回・再試行せず料理未確認|
|81|https://www.pacificgolf.co.jp/moonlake_t/stay/ と https://booking.pacificgolf.co.jp/guide/143.html|詳細ページの追加取得がタイムアウト、3秒後に1回再試行し本文取得成功。夕食・宿泊条件を確認。昼食の具体的料理、ゴルフを含む総額は未確認|
|83|https://booking.pacificgolf.co.jp/?cc_id=141&p=guide.access_map|ラウンド条件確認。食事・宿泊・料金の不足は未解消|
|87|https://www.kasen-kikou.or.jp/tamagawa/golf.html と https://www.kasen-kikou.or.jp/tamagawa/center.html|交流センターの休憩・更衣室・ロッカー・飲料自販機を確認。浴場・宿泊・料理は明示なし。stay/diningは空欄維持|
|89|https://reserve.accordiagolf.com/golfCourse/kanagawa/daiatsugi_sakura/restaurant|403。迂回・再試行せず未確認を維持|
|92|https://booking.pacificgolf.co.jp/?cc_id=72&p=guide.access_map|バス時間確認。料理・浴室・宿泊・プレー料金は未確認|

次回はこの失敗群の反復を避け、最新mainの未調査コース群から進める。全件未完了のため継続タスクは停止しない。Search Console非公開状態は未閲覧、10月30日通知は未変更。
公開結果は実行完了・ライブ照合後に追記する。

# 追加調査 br（2026-10-30）
基準 main: 4cb1f13f111b6d247932f2a8e5b7e9d1c6e30734
MAINTENANCE.md、facilities-followup-20261029.md、最新bq引継ぎと公開証跡を確認。旧ZIP不使用。

## 採用差分
5コース5項目。246 rail、381 rail、256 budget、366 budget、179 budget。
各出典・確認日・人数・料金条件・旧値は verified-followup-20261030br.json に記録。
料金は公式サイトからリンクした公式予約の対象日詳細を読んで採用。空き枠保証ではない。
246はバスターミナルからの送迎時間。FAQとコンセプトで出発時刻が食い違うため時刻を非掲載。
381は「送迎バスなし」という明記だけを採用。駅からの時間は未確認。

## 件数の注意
空欄85→80予定（車3、鉄道13、食事11、宿泊12、料金36、景観5、プレー0）。
空欄数は未解決事実数ではない。既存bp/bq等には「未確認」と記載して非空欄になった項目もある。これらを内容確認完了として扱わない。今回も381の駅からの経路は未解決。確認不能を「なし」に変えない。全件完了ではない。

## 調査済み・今回未採用（同じ失敗の反復を避ける）
下記は2026-10-30確認。記載なしは施設なしや公式情報が存在しないとの断定ではない。
|ID|調査先|結果・次に必要な確認|
|---|---|---|
|335|https://www.suginosato.co.jp/restaurant.html|502後タイムアウト。メニュー画像の実内容未検証。取得可能になってから画像確認。|
|80|https://www.hatsuhocc.co.jp/|502再試行でも502。食事・料金未確認。|
|19|https://www.belle-co.com/ichihara/|502後タイムアウト。食事・料金未確認。|
|241|https://www.katoricc.com/|502後タイムアウト。残項目継続。|
|243|https://www.shinchiba-cc.co.jp/|502。再試行未実施。|
|427|https://www.kodama-cc.jp/|502。再試行未実施。kodama-gc.comは別施設につき流用不可。|
|352|https://www.ashikagajo.jp/price/|2026年9～11月PDF導線あり。jimcontent PDF取得不可、画像取得403。認証・アクセス制限を回避していない。実画像未読につき料金未採用。|
|357|https://www.touricc.com/clubhouse.html ; https://www.touricc.com/playguide.html|クラブハウス・会員紹介条件を確認。宿泊・現行総額は確認できず。|
|495|https://www.shonanseaside.com/|本文に宿泊条件見つからず。宿泊なしとは扱わない。|
|492|https://www.riverside-park.co.jp/facilities/|テラスとカフェ時間の表現のみ。実際の料理提供・メニューを確認できず。|
|394|https://www.linehill2026.com/ ; https://www.linehill2026.com/sitemap/|新公式サイトの名称・住所・電話確認。ICからの時間は見つからず。|
|348|https://www.g7cc.co.jp/access.html|車の案内のみ確認。駅からの所要時間未確認。|
|365|https://yaita-cc.com/access|車の案内のみ確認。駅からの時間は推測しない。|
|259|https://www.kanasago.com/access/|車の案内のみ確認。駅からの時間未確認。|
|339|https://www.mashikohills.com/accesse.html|公式は車案内。県観光サイトの駅情報は今回コース一次資料として採用せず。|
|314|https://www.mgcc.jp/access/|住所・地図のみ。駅からの経路未確認。|
|453|https://www.takanashiclub.jp/access.html|地図中心。駅からの経路未確認。|
|246|https://www.brickandwood.jp/official/access/|地図PDFは実画像未読。車時間・料金は未採用。|
|356|https://thomson-cc.com/fee.html|料金は動的カレンダー。本文で昼食・人数等は確認できるが総額未確認。|
|450|https://www.kiryucc.com/reservation.html|ログイン予約。レンタル・練習料金はプレー総額ではないため代用しない。|
|449|https://www.shimonitacc.com/reservation.html|同上。プレー総額未確認。|
|478|https://rfgr.jp/silk/|料金リンク404。公式予約562-489.jpのカレンダーは動的表示で金額未確認。|
|496|https://chigasaki.golfdigest.co.jp/guide ; https://reserve.golfdigest.co.jp/golf-course/373203/calendar/|GDO運営公式。同行非プレーヤー料金をゴルファー料金へ転用しない。対象日プラン未取得。|
|248|https://www.unimat-golf.jp/choshi/price/|公式予約カレンダーの日付リンク応答は本文なし。ホテル料金をプレー料金に代用しない。|
|260|https://sevenlakes.jp/fee.html|セルフ開放日条件・キャンセル規定は掲載。基本総額は動的表示で未確認。|
|366|https://firstee.jp/lakelandcc/lakelandcc/iframe|一覧に価格があっても11/5・11/6詳細は金額非表示。11/2詳細のみ採用。|
|158|https://www.higashi-tsukuba.co.jp/reservation/reservation/ ; https://www.higashi-tsukuba.co.jp/reserve/|予約導線確認まで。対象日料金詳細への追跡が残る。|
|465,455,12|前回の引継ぎに記載された公式URL|403・タイムアウト・メンテナンス転送の同一失敗を繰り返していない。改善済みとは判断しない。|

## 検証
ドライラン、適用、384通りの選択、11単体テスト、JS構文、500ページ・503URL、diff check合格。
公開前に5項目だけの差分であることを全データ比較。既存ID・情報・分類・お気に入り・デザイン保持。
公開は既存verified-update経由。公開後のrunとハッシュは別証跡に記録。
Search Consoleの非公開状態・既存通知は操作していない。

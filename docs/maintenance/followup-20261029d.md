# 2026-10-29 追加調査 d

基準main: c9fce101e74a5d1fe267d2716697f13a7d0e4b16。MAINTENANCE.md、facilities-followup-20261029.md、followup-20261029c.mdを読んで着手。旧ZIPは不使用。

## 確認済み差分

7コース14項目（新規8・既存補足6）。前後値・公式出典・確認日・条件は `verified-followup-20261029d.json`（適用後 `applied_updates/`）に記録。

|ID|コース|更新内容|
|---|---|---|
|22|烏山城|夕食の粋虎・とちぎ和牛・営業時間。昼食は未確認と明示|
|71|城里|公式メニュー画像を目視しカレー2品、昼食付き条件。ホテル客室浴室・入退室時間|
|72|那須陽光|予約制夕食3品と人数条件。男女大浴場・ドライサウナ|
|75|静ヒルズ|2026年秋の静和食膳。大浴場・女性用化粧ブース|
|132|鎌倉|食事3品。10月15日以降の18H/PAR71、仮設グリーン・ティと日曜例外|
|137|姉ヶ崎|食事3品。男女浴室・場内宿泊なし。送迎バス時間・予約条件・セルフデー運休|
|242|ミルフィーユ|通行止めに伴う迂回案内。10月1日からサブバッグ使用禁止|

主出典は以下。料理写真は転載せず料理名のみ採用。
- https://www.karasuyamajo.com/suiko.html
- https://shirosato-gc.com/restaurant.html （2026-01.jpg・2026-02.jpgを目視）
- https://shirosato-gc.com/hotel.html
- https://golf.nasusunlight.jp/restaurant
- https://golf.nasusunlight.jp/facilities
- https://www.hillsgolf.jp/shizu/news/260915-1/
- https://www.hillsgolf.jp/shizu/facility/
- https://kamakura-cc.com/menu-category/grand/
- https://kamakura-cc.com/ （10月14日告知本文の完全URLはJSON）
- https://heiwanosan.co.jp/anegasaki/facilities/restaurant/
- https://heiwanosan.co.jp/anegasaki/qanda/
- https://heiwanosan.co.jp/anegasaki/facilities/
- https://www.milgolf.co.jp/

## 未確定・今回更新しない調査

確認日はいずれも2026-10-29。失敗は施設なし・閉鎖の根拠にしない。同じ失敗先の反復を避け、次回は別の未調査群を優先する。

|ID|調査先|結果・残件|
|---|---|---|
|19|https://www.belle-co.com/ichihara/|トップが再試行でもタイムアウト。食事本文未確認。restaurant.htmlも502|
|80|https://www.hatsuhocc.co.jp/|502の後、再試行タイムアウト。食事未確認|
|334|https://www.taka-golf.co.jp/|トップタイムアウト。食事未確認|
|335|https://www.suginosato.co.jp/|トップ502。食事未確認|
|77|https://nasukasumigajo.com/ja|取得本文はLoadingと連絡先のみ。食事未確認|
|78|https://www.mannacc.com/restaurant/manna-grill/|公式コースページのリンクから進んだが429。制限を迂回せず食事未確認|
|495|https://www.shonanseaside.com/|料金・食事付きプランはあるが料理内容未確認。既存料金は重複更新しない|
|242|https://www.milgolf.co.jp/|パーティーパックの品数のみで具体的料理未確認。IC時間も未確認|
|22|https://www.karasuyamajo.com/restaurant.html|ランチ料理の本文が抽出されず。夕食のみ部分補完。粋虎の12月開始メニューは現時点の料理に採用しない|
|71|https://shirosato-gc.com/fee.html|秋冬の日別料金は抽出本文に金額なし。4〜9月限定の早朝・薄暮料金を現在料金に転用しない|
|72|https://golf.nasusunlight.jp/restaurant|昼食は画像のため今回未検証。夕食のみ部分補完。トップは初回タイムアウト後の再試行で取得できた|
|132|https://kamakura-cc.com/facility/|浴室・宿泊の明示を本文で確認できず。stayは空欄維持|

## 検証と残件

ドライラン・適用成功。500 IDと14項目以外の全データが不変であることを構造比較。既存61追加項目を含む値、分類、デザイン、お気に入りコードは変更しない。
384検索条件、Python 11テスト、data.js/finder.js構文、500ページ・503URL SEO検査、git diff --checkが成功。

未入力は677→669（食事119、宿泊178、料金287、景色42、電車35、車8）。対象500コースのうち空欄を含むコースは384。部分記載の精査は別途残る。空欄減少は完成率ではない。
次回はこの記録と最新mainを読み、未調査の食事群（例: ID5・6・18・21・40等）または料金・宿泊の未調査群へ進む。失敗群の無条件再試行はしない。今回も全件完遂ではない。
Google Search Console非公開状態は確認していない。別途の10月30日通知は変更していない。

公開完了：投入コミット `07c5aa3f28447e8c85ec5211ea62a0886db6b150`、適用コミット `af505d1f78573c7e9e3362b75ece466d432579dc`。verified-update 実行 `40813506802` は成功。
実サイトの data.js と対象7コースのHTMLを生成物とバイト単位で照合し、一致を確認。data.js SHA256: `76abea2504a0cd9e4c363dde5d239a997d881c4376e4c75d80a2652217f87a1d`。

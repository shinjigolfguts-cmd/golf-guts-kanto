# 2026-10-29 追加調査 i

基準main:20a28721b0b50a493a13384ecf26d77bc0ae0e05。MAINTENANCE.md、facilities-followup-20261029.md、followup-20261029h.mdを確認。古いZIPは不使用。

## 確認済み差分

5コース10項目（新規7、既存補足3）。verified-followup-20261029i.jsonに旧値、出典、確認日2026-10-29、条件と根拠を保存。適用後はapplied_updatesへ移動。

- ID190 ザ ナショナル千葉：現行昼食PDFの実際の料理、食事付き差額。通常の交通目安を保持し、10月15日発表の通行止め・迂回案内を日付付きで補足。解除や迂回時間は推測しない。
- ID209 カントリークラブ・ジャパン：現行昼食、浴室・迎賓館客室、バックナインの地形、指定来場経路。宿泊利用資格等は未確認と明示。
- ID224 千葉バーディ：公式経路図から八街駅タクシー15分と山田IC10分7km。既存佐倉IC15分12kmを保持。タクシー料金改定日不明のため金額不採用。
- ID225 グレンオークス：朝食の具体的内容とレストラン営業時間。朝食終日提供とはしない。昼食料理は未確認と明示。
- ID228 習志野：朝昼営業時間、パーティーの料理構成と2組6名以上・1週間前予約。通常昼食料理名は未確認と明示。

未入力646→639。プレー0、車8、電車34、食事97、宿泊・風呂174、料金285、景色41。空欄あり377コース。空欄なしでも部分未確認あり、全件完了ではない。

## 調査先・未確認理由

|ID|調査先|残件・注意|
|---|---|---|
|190|https://national-cc.jp/chiba/facility/ 、 https://national-cc.jp/chiba1/wp-content/uploads/2026/10/chiba.menu_lunch-.pdf 、公式accessと10月15日news|14頁PDFの1〜3頁を画像目視。プレー料金budget未入力。交通規制は過去日付の公式発表と明示し、解除は未確認|
|209|https://www.ccjapan.jp/cn7/pg937030.html 、 https://www.ccjapan.jp/cn6/facility.html 、 https://www.ccjapan.jp/course/ 、 https://www.ccjapan.jp/access.html 、 https://www.ccjapan.jp/pg1442011.html|夏限定料理は現在提供と断定せず不採用。迎賓館利用資格・予約・料金・浴室時間は記載を確認できず。10月8日交通案内はクラブ指定経路だけの説明。通常料金表season-fee.htmlは既存記載と整合し変更なし|
|224|https://www.c-birdie.com/access/ 、 https://www.c-birdie.com/assets/img/access/route.jpg 、 https://www.c-birdie.com/facility/|経路画像を目視。施設紹介にレストランあり、実際の料理を確認できずdining未入力を保持。浴室既存情報を保持|
|225|https://reserve.accordiagolf.com/golfCourse/chiba/glenoaks/restaurant|現行朝食画像902_27_20250930191004.jpg.webp目視。通常昼食の料理は掲載内容から確認できず部分未確認として残す。営業時間はレストラン全体|
|228|https://reserve.accordiagolf.com/golfCourse/chiba/narashino/restaurant|現行パーティー画像012_23_20250903141109.jpg.webp目視。パーティー条件を通常昼食へ流用しない。通常昼食料理は部分未確認|

公式画像は転載せずURLを台帳に保存。過去の取得不能先を無条件反復していない。未調査候補は200/220/221/222/235/236/243/249/250/255/262など（今回調査済みとは扱わない）。

## ローカル検証

ドライラン、適用、ページ・残件生成完了。384検索条件、Python11テスト、500ページ/503URL SEO、data.js/finder.js構文、git diff --check通過。独立構造比較で500 ID/順序と承認済み10項目以外の全項目・メタデータ保持を確認。デザイン・分類・お気に入りのコード変更なし。data.js SHA256:a83d4ba2fab36ad02bed2a8e464935dae0ce706c688f61be4cf3737ab7838821。

公開実物の照合結果は後続で追記。全件未完了のため継続。Search Console非公開ステータス未閲覧、10月30日通知未変更。

## 公開結果

入力コミットf5aff47a8e181cce5d519fb7277d46e2de57dcbd、反映コミットbb477508eea1a500132b56b64a61fbf5f452391a。verified-update実行40825668790成功。公開data.jsと5個別ページ（190/209/224/225/228）を検証済みローカル生成物とバイト照合して全一致。5コース10項目を公開・反映検証済み。

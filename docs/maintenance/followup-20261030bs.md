# 追加調査 bs（2026-10-30）
基準main: ba84e0ec57fcfc4a9948f88437feccfe77ca430e。最新mainをfetchして別worktreeで適用。MAINTENANCE、facilities-followup-20261029、brの調査記録を継承。

brの5項目はrun41018073524/job123938822718で全テストと公開照合に成功。ログ2026-10-30T07:07:39Z: Published and verified ba84e0ec57fcfc4a9948f88437feccfe77ca430e。data.js SHA256:6956025c3fcacd367b2fea771f3ede9a62095fd3e0b1dee330d19871f044deb7。

## bs採用
178加茂、383足利多幸、316龍ヶ崎の料金3項目。公式サイトから実際の予約・料金本文まで辿り、税込額・対象日・人数・食事・会員条件・別料金を確認。検証JSONに出典・確認日・条件・before保存。多幸の7,085円はロッカー浴槽550円別。加茂の古い2020～2021料金は採用しない。

空欄80→77予定（車3、鉄道13、食事11、宿泊12、料金33、景観5）。空欄数と未解決事実数は異なる。brに記載した過去の「未確認」埋め戻しも全件確認完了とは扱わない。

## 追加調査・未採用（2026-10-30）
|ID|出典|結果・残作業|
|---|---|---|
|140|https://www.kanozan.co.jp/|タイムアウト後502。料金本文未取得。|
|163|https://www.president-cc.jp/|タイムアウト、再試行もタイムアウト。|
|397|https://www.tsugacc.co.jp/|502、再試行も502。|
|158|https://www.higashi-tsukuba.co.jp/reserve/|ゲストWeb会員案内は読めるが予約ボタンの遷移先を抽出できず。金額未確認。|
|354|https://tochigicc.com/reservation.html → https://www.valuegolf.co.jp/rental/rental_top.cfm?page_flg=V&rent_cid=090007301|新公式予約は動的表示「取得中」。金額未確認。|
|435|https://www.yc21.co.jp/heisei/fee.html ; https://www.yc21.co.jp/heisei/online.html|画像料金とvaluegolf一人予約は読み込み中。総額未確認。|
|424|https://www.olympicnational.co.jp/east/fee.html ; https://www.olympicnational.co.jp/east/reservation.html → https://www.jgo-os.com/11109/003/reserve/|追加カート等のみ本文確認。予約は「ゴルフ場情報の取得に失敗」。基本料金未採用。WESTへ転用不可。|
|476|https://tcgv.jp/ ; https://tcgv.jp/pr ; https://prtimes.jp/main/html/rd/p/000000008.000078010.html|完全会員制とメンバー同伴ゲストの条件。2024年運営会社発表にもプレー金額なし。会員ログインを回避しない。|
|390|https://www.livemax-golfclub.com/access/|車経路17kmは記載。駅からの時間未確認。|
|134|https://checkmate-cc.com/availability.html → https://docs.google.com/spreadsheets/d/e/2PACX-1vTU0w2WGiZzI5CLTvgAQpxC9Uox-jxXmLSLx7lJxJJNWs7I0ahNKlCTGLl6RA5LjCPK8kkJAx82BMY0/pubhtml|本文は会員料金のみ。ゲスト用公開カレンダーはタイトルのみ取得。会員価格を一般料金に転用しない。|
|486|https://sagamino-cc.jp/club-house.html|画像主体。宿泊・浴室実内容未確認。画像リンク取得だけで確認済みにしない。|
|300|https://www.daiyagreen.com/|502後タイムアウト。残る交通・食事・宿泊の本文未取得。|
|367|https://www.royalcc.co.jp/|画像主体のトップまで。景観本文未確認。第三者ゴルフラボを一次資料の代用にしない。|
|249|https://tokyo-classic.jp/members_login/|会員専用ログイン。公開トップに料金なし。認証迂回せず。|
|254|https://www.eaglepoint.co.jp/?page_id=39|会員紹介・同伴条件、会員限定Web予約。公開ページに総額未確認。|
|432|https://www.tokyogolfclub.jp/guide/|予約は会員から・会員同伴が原則。公開本文に料理・料金未確認。|
|234|https://reserve.accordiagolf.com/golfCourse/chiba/fujiichihara/detail|送迎の本文記載を見つけられず。送迎なしとは扱わない。|
|384|https://www.ashikaga-cc.com/|公式WEB予約導線は多幸に遷移。飛駒の選択先詳細追跡が残る。多幸料金を流用しない。|

## 検証
ドライラン・適用、384選択、11単体テスト、JS構文、500ページ503URL、diff check成功。
全データ比較で3項目以外は不変。ID・分類・お気に入り・デザイン保持。公開結果は別証跡。
未調査・未確認は残り、全件完了ではない。Search Console・通知は変更しない。

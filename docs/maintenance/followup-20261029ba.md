# 追加調査 ba

基準main bc72d39e08c925bf114d6b26222f98a74073b9a9。MAINTENANCE.md、facilities-followup-20261029.md、az引継ぎに従い、最新mainを再取得。確認日2026-10-30（日本時間）。

霞ヶ関公式サイトは2026年10月26日付で一部再開を告知。食堂メニューと倶楽部の一日を実読し、dining/stayの2項目を採用。料理の限定数と提供時間を保持。浴場の存在以外の設備を推測しない。利用案内・ゲスト案内にはプレー料金の具体額なし。

調査先と非採用理由:
- https://www.kasumigasekicc.or.jp/information/index.html 、 https://www.kasumigasekicc.or.jp/information/01.html ：予約・同伴条件はあるが料金額なし。
- https://www.tokyogolfclub.jp/guide/ ：会員同伴原則、予約は会員から問い合わせ。公開本文に料金額なし。会員ログインは行わない。
- https://www.ota-futaba-cc.co.jp/ ：HTTP403。回避せず保留。
- https://www.camelliahills.com/ ：メンテナンス・交通告知のみで料金本文なし。
- https://www.katoricc.com/ 、 https://www.shinchiba-cc.co.jp/ ：規定再試行後もHTTP503。料金なしとは扱わない。
- https://www.brickandwood.jp/official/facilities/ ：施設本文は確認できるがプレー料金なし。ネット予約リンクはログイン宛。料金推測なし。
- https://www.brickandwood.jp/wp1/wp-content/uploads/2020/08/bwcmap.pdf ：公式accessからリンクされた地図を画像で確認。木更津東IC・市原鶴舞ICと周辺道路は示すが、IC・駅からの所要時間はないため時間欄は未補完。
- http://www.daiyagreen.com/facilities/index6.html ：公式HTTP本文で料理例を確認したが、HTTPS版は503。更新処理が要求するHTTPS出典を満たさず保留。価格の現在の適用日は未確認。
- http://www.daiyagreen.com/access/index2.html ：旧列車名「フレッシュひたち」「スーパーひたち」・古い運賃表記を含む。記載の送迎条件が現在も有効か確認できず採用しない。HTTPS版も503。トップの佐原香取IC3分という文言と詳細アクセスの記載が整合しないため、トップ文言の転用もしない。

公開前検証: 500ID・既存情報の保持、2項目以外に変更がないこと、単体・選択・DOM・JS構文・SEO検証。予定空欄217→215（車8、電車24、食事25、宿泊60、料金90、景観8）。未確認項目は残っており全件完了ではない。Search Consoleと別途通知は変更しない。

追加の交通調査: https://kasama-club.com/access の本文は予約制クラブバス発時刻のみでICからの所要時間なし。https://www.linehill2026.com/ のトップ本文はコース・レストラン・予約案内でICからの時間なし。この2件も車アクセスの推測補完をしていない。

公開完了: input dfa1e6912e0395a9ca04cbd8978b341d35f687c9、生成main d5a90ecf26223caccb5b621e36392809933c68f0。verified-update 40974504746成功、Pages 40974523361成功。公開data.jsとcourses/426.htmlのSHA256一致。空欄215。

(()=>{
 const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const parts=text=>{const sentences=String(text||'公式アクセス案内をご覧ください。').match(/[^。]+。?/g)||[];return sentences.map(t=>`<p${/記載がありません|記載なし|未確認|確認できていません/.test(t)?' class="finder-note"':''}>${esc(t)}</p>`).join('')};
 const url=s=>/^https?:\/\//.test(s||'')?esc(s):'#';
 window.gutsAccessHtml=course=>{
  const rows=[['car','車で · ICから'],['rail','電車で · 駅から']].map(([key,label])=>{
   const f=course.comparison?.[key];
   return `<div class="course-access-row"><p class="course-access-label">${label}</p>${parts(f?.text)}<a class="finder-source" href="${url(f?.url||course.officialUrl)}" target="_blank" rel="noopener noreferrer">公式アクセスを見る ↗</a>${(f?.supportingUrls||[]).slice(0,1).map(u=>` <a class="finder-source" href="${url(u)}" target="_blank" rel="noopener noreferrer">補足の公式案内 ↗</a>`).join('')}</div>`;
  }).join('');
  return `<div class="course-access">${rows}<p class="course-access-footnote">ゴルフ場・運営会社の公表資料（公式サイト・採用情報等）を参照。所要時間は目安です。</p></div>`;
 };
})();

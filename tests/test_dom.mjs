// Run from repository root after npm install --no-save happy-dom@21.0.4
import {Window} from 'happy-dom';
import fs from 'node:fs';import assert from 'node:assert/strict';
let w=new Window({url:'https://example.test',settings:{disableJavaScriptFileLoading:true,disableJavaScriptEvaluation:true}});
const html=fs.readFileSync('index.html','utf8');w.document.write(html);w.matchMedia=()=>({matches:false});w.HTMLElement.prototype.scrollIntoView=function(){};
w.eval(fs.readFileSync('data.js','utf8')+';window.DATA=DATA;');
w.eval(fs.readFileSync('access.js','utf8'));
w.localStorage.setItem('guts-course-saved',JSON.stringify([422]));
for(const s of w.document.querySelectorAll('script:not([src])'))w.eval(s.textContent);
assert.equal(w.document.querySelectorAll('.entry').length,20);
// Header favorites must include a saved course outside the active category and clear prior filters.
w.document.querySelector('#pref').value='東京都';w.document.querySelector('#search').value='見つからない';w.document.querySelector('#headerSaved').click();assert.equal(w.document.querySelectorAll('.entry').length,1);assert.equal(w.document.querySelector('.entry').dataset.courseId,'422');w.document.querySelector('.save').click();assert.equal(w.document.querySelectorAll('.entry').length,0);
for(const b of w.document.querySelectorAll('.cat')){b.click();assert.equal(w.document.querySelectorAll('.entry').length,20);}
await w.happyDOM.close();
w=new Window({url:'https://example.test/find.html',settings:{disableJavaScriptFileLoading:true,disableJavaScriptEvaluation:true}});
w.document.write(fs.readFileSync('find.html','utf8'));w.HTMLElement.prototype.scrollIntoView=function(){};
const inline=[...w.document.querySelectorAll('script:not([src])')].map(x=>x.textContent).join('\n');
w.eval(fs.readFileSync('data.js','utf8')+';window.DATA=DATA;');w.eval(fs.readFileSync('access.js','utf8'));w.eval(inline+'\n'+fs.readFileSync('finder.js','utf8'));
for(const area of ['', '東京都','神奈川県','千葉県','埼玉県','茨城県','栃木県','群馬県']){
 const start=w.document.querySelector('[data-start]');start.click();
 const auto=w.document.querySelector('#auto-advance');if(auto)auto.checked=false;
 for(const [i,value] of [area,'car','beginner','food'].entries()){
  const panel=w.document.querySelector(`[data-question="${i}"]`);assert.equal(panel.hidden,false);panel.querySelector(`[data-answer="${value}"]`).click();panel.querySelector('[data-next]').click();
 }
 assert.equal(w.document.querySelector('.finder-results').hidden,false);
}
console.log('PASS DOM: favorites across categories, remove favorite, 10 categories, 8 finder area flows');await w.happyDOM.close();

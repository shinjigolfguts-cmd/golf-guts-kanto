const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const root=path.join(__dirname,'..');const source=fs.readFileSync(path.join(root,'finder.js'),'utf8');const ctx=vm.createContext({});
vm.runInContext(fs.readFileSync(path.join(root,'data.js'),'utf8')+';globalThis.data=DATA;',ctx);
vm.runInContext(source.slice(source.indexOf('const memberships='),source.indexOf('const answers='))+source.slice(source.indexOf('function selectCourses('),source.indexOf('// Keep question controls'))+';globalThis.select=selectCourses;',ctx);
assert.equal(ctx.data.courses.length,500);const ids=new Set(ctx.data.courses.map(x=>x.id));assert.equal(ids.size,500);
for(const c of ctx.data.categories){assert.equal(c.ids.length,c.reasons.length);for(const id of c.ids)assert(ids.has(id));}
let count=0;
for(const area of ['', '東京都','神奈川県','千葉県','埼玉県','茨城県','栃木県','群馬県'])for(const travel of ['car','train','either'])for(const style of ['beginner','casual','relax','challenge'])for(const priority of ['scenery','food','budget','access']){
 const r=ctx.select({area,travel,style,priority});assert.equal(r.length,4);assert.equal(new Set(r.map(x=>x.course.id)).size,4);for(const x of r){assert(x.course.area.startsWith(area));assert(Number.isFinite(x.score));}count++;
}
console.log(`PASS ${count} selection combinations, 500 courses, category references`);

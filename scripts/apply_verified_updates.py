"""Apply an explicitly reviewed batch. No scraping or inferred facts."""
import argparse, copy, hashlib, json
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

def apply(raw, patch):
    if hashlib.sha256(raw).hexdigest()!=patch['baseSha256']:
        raise ValueError('Source changed; review against latest data')
    if patch.get('reviewed') is not True or not patch.get('reviewer'):
        raise ValueError('Reviewed evidence required')
    data=json.loads(raw.decode().split('=',1)[1].strip().rstrip(';'))
    by={c['id']:c for c in data['courses']}; seen=set()
    for u in patch['updates']:
        c=by[u['id']]; key=u['field']; fact=u['after']
        if c['name']!=u['name'] or key not in c['comparison'] or c['comparison'][key]!=u['before']:
            raise ValueError('Identity or prior value mismatch')
        if (c['id'],key) in seen: raise ValueError('Duplicate update')
        seen.add((c['id'],key))
        if not fact.get('text') or not fact.get('url','').startswith('https://') or fact.get('sourceType')!='official' or not u.get('evidenceNote'):
            raise ValueError('Official evidence required')
        checked=datetime.strptime(fact['checked'],'%Y-%m-%d').date()
        if checked>datetime.now(ZoneInfo('Asia/Tokyo')).date(): raise ValueError('Future date')
        if key=='budget' and not fact.get('conditions'): raise ValueError('Price conditions required')
        c['comparison'][key]=copy.deepcopy(fact)
    return ('const DATA='+json.dumps(data,ensure_ascii=False,indent=2)+';\n').encode()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('patch');p.add_argument('--apply',action='store_true');a=p.parse_args()
    target=Path(__file__).resolve().parents[1]/'data.js';raw=target.read_bytes();result=apply(raw,json.loads(Path(a.patch).read_text()))
    if a.apply:
        if target.read_bytes()!=raw:raise ValueError('Concurrent data change')
        target.write_bytes(result)
    print('Validated reviewed update batch'+(' and applied' if a.apply else ' (dry run)'))

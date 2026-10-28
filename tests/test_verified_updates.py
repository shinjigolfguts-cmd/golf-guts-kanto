import hashlib,json,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from apply_verified_updates import apply
class Updates(unittest.TestCase):
 def test_guarded_update(self):
  raw=b'const DATA={"courses":[{"id":1,"name":"Example","comparison":{"stay":null,"budget":null}}]};'
  p={'baseSha256':hashlib.sha256(raw).hexdigest(),'reviewed':True,'reviewer':'test','updates':[{'id':1,'name':'Example','field':'stay','before':None,'after':{'text':'Bath','url':'https://example.com/facility','sourceType':'official','checked':'2026-10-28'},'evidenceNote':'Official body states bath'}]}
  self.assertIn(b'Bath',apply(raw,p))
  with self.assertRaises(ValueError):apply(raw+b' ',p)
  p['updates'][0]['name']='Wrong'
  with self.assertRaises(ValueError):apply(raw,p)
  p['updates'][0]['name']='Example';p['updates'][0]['field']='budget'
  with self.assertRaises(ValueError):apply(raw,p)
  p['reviewed']=False
  with self.assertRaises(ValueError):apply(raw,p)

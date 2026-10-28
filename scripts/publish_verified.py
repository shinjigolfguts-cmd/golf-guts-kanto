"""Publish through the existing branch-based Pages configuration, then verify it."""
import os,json,time,subprocess,urllib.request,hashlib
repo=os.environ['GITHUB_REPOSITORY'];token=os.environ['GH_TOKEN'];base='https://api.github.com/repos/'+repo
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
def api(path,method='GET'):
 req=urllib.request.Request(base+path,method=method,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
 with urllib.request.urlopen(req,timeout=30) as r:return json.load(r)
api('/pages/builds','POST')
for _ in range(60):
 b=api('/pages/builds/latest')
 if b.get('commit')==head and b.get('status')=='built':break
 if b.get('commit')==head and b.get('status')=='errored':raise SystemExit('Pages build failed')
 time.sleep(10)
else:raise SystemExit('Pages build verification timed out')
url='https://'+repo.split('/')[0]+'.github.io/'+repo.split('/')[1]+'/'
expected=hashlib.sha256(open('data.js','rb').read()).hexdigest()
for _ in range(30):
 with urllib.request.urlopen(url+'data.js?revision='+head,timeout=30) as r:actual=hashlib.sha256(r.read()).hexdigest()
 if actual==expected:break
 time.sleep(10)
else:raise SystemExit('Published data differs from tested data')
print('Published and verified '+head+' '+url)

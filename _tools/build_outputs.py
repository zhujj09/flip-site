import re, json, html
from collections import OrderedDict
root='/workspace/flip-site/content/zh/'
items=[]
seen=set()
def key(t): return re.sub(r'[^a-z0-9]','',t.lower())[:60]
for f in ['research-wellbore','research-esp','research-plunger','research-jetpump','research-mfl','research-bigdata']:
    s=open(root+f+'/index.md').read()
    s=s[s.find('代表性论文'):]
    for li in re.findall(r'<li>(.*?)</li>',s,re.S):
        if 'manuscript submitted' in li: continue
        m=re.search(r'<a [^>]*>(.*?)</a>',li); t=m.group(1) if m else re.split(r'\. ',re.sub(r'^.*?</b>[^.]*\. ','',li))[0]
        y=int(re.search(r'(\d{4})\.$',li.strip()).group(1))
        k=key(re.sub('<.*?>','',t))
        if k in seen: continue
        seen.add(k); items.append((y,li.strip()))
pubs=json.load(open('/workspace/rs/pubs.json'))
doi_fix={'Transformer-based forecasting':'10.1016/j.egyai.2025.100535',
 'Numerical study on electrical-submersible-pump':'10.2118/170727-pa'}
skip=['Transient Plunger-Lift Model Improves','Efficiency and critical velocity']
def fmt_auth(a):
    return ', '.join('<b>%s</b>'%x if x.strip() in ('J Zhu','JJ Zhu') else x for x in a.split(', '))
for v in pubs.values():
    for p in v:
        t=p['sch']['title']; k=key(t)
        if k in seen or any(s in t for s in skip): continue
        doi=p.get('doi')
        if doi and ('ssrn' in doi or 'review' in doi): doi=None
        for kk,dd in doi_fix.items():
            if t.startswith(kk): doi=dd
        venue=re.sub(r',\s*\d{4}$','',p['sch']['venue']).rstrip(' …')
        tt=html.escape(t)
        title='<a href="https://doi.org/%s" target="_blank" rel="noopener">%s</a>'%(doi,tt) if doi else tt
        y=int(p['sch']['year'])
        items.append((y,'%s. %s. <i>%s</i>, %d.'%(fmt_auth(p['sch']['authors']),title,html.escape(venue),y)))
        seen.add(k)
by=OrderedDict()
for y,li in sorted(items,key=lambda x:-x[0]): by.setdefault(y,[]).append(li)
out=[]
for y,lis in by.items():
    out.append('<h3 class="flip-out-year">%d</h3>\n<ol class="flip-out-pubs">'%y)
    out+=['  <li>%s</li>'%l for l in lis]
    out.append('</ol>')
open('/tmp/pubs_html.txt','w').write('\n'.join(out))
print(len(items), {y:len(l) for y,l in by.items()})

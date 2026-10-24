import json,sys,collections
A=json.load(open('taxonomy_A.json'));B=json.load(open('taxonomy_B.json'))
now=json.load(open('concepts_now.json'))
known={c['id'] for c in now}
R={'distributions@functional':'schwartz-distributions'}
def fix(p): return 'schwartz-distributions' if p=='distributions' else p
T={};dups=[]
for src,d in (('A',A),('B',B)):
  for t in d['proposed']:
    t=dict(t); t['prerequisites']=[fix(p) for p in t['prerequisites']]
    if t['id'] in T:
      o=T[t['id']]; dups.append(t['id'])
      o['tier']=min(o['tier'],t['tier']); o['prerequisites']=sorted(set(o['prerequisites'])|set(t['prerequisites']))
      o['categories']=sorted(set(o.get('categories',[]))|set(t.get('categories',[])))
      o['evidence']=list(dict.fromkeys(o['evidence']+t['evidence']))
    else: t['from']=src; T[t['id']]=t
clash=[i for i in T if i in known and i!='distributions']
allids=known|set(T)|{'schwartz-distributions'}
missing=sorted({(i,p) for i,t in T.items() for p in t['prerequisites'] if p not in allids})
# cycle check + topological order
indeg={i:0 for i in T};g=collections.defaultdict(list)
for i,t in T.items():
  for p in t['prerequisites']:
    if p in T: g[p].append(i); indeg[i]+=1
q=[i for i in T if indeg[i]==0];order=[]
while q:
  x=q.pop(0);order.append(x)
  for y in g[x]:
    indeg[y]-=1
    if indeg[y]==0:q.append(y)
cyc=len(order)!=len(T)
# tier monotone: raise
raised=[]
for i in order:
  m=max([T[p]['tier'] for p in T[i]['prerequisites'] if p in T]+[0])
  if T[i]['tier']<m: raised.append((i,T[i]['tier'],m)); T[i]['tier']=m
print('dups',len(dups),dups);print('clash with existing',clash);print('missing prereqs',missing);print('cycle',cyc);print('raised',raised)
tiers=collections.Counter(t['tier'] for t in T.values());print('total',len(T),dict(sorted(tiers.items())))
areas=collections.Counter(t['area'] for t in T.values());print(dict(areas.most_common()))
out=dict(note="Merged arXiv/MSC taxonomy (parts A and B). Tier 1 = needed to read most papers in the field; 2 = needed for a large share; 3 = frontier specialities. Order = dependency order. MSC codes beyond 00-19 partly from memory; verify before publishing.",
 rename={"distributions (functional analysis, planned round 5)":"schwartz-distributions"},
 proposed=[T[i] for i in order], splits=A['splits']+B['splits'], new_areas=A['new_areas']+B['new_areas'],
 categories=A['categories']+B['categories'], notes=A['notes']+B['notes'])
json.dump(out,open('/home/claude/frontier_atlas/pipeline/round5/research/taxonomy.json','w'),indent=1,ensure_ascii=False)

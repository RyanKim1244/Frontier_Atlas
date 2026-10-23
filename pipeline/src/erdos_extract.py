import re, os, yaml, json
FC = 'formal-conjectures/FormalConjectures/ErdosProblems'
Y = {p['number']: p for p in yaml.safe_load(open('erdosproblems/data/problems.yaml'))}
DOC = r'/--((?:(?!-/).)*?)-/'
decl = re.compile(DOC + r'\s*(?:@\[((?:(?!\]\s*\n).)*?)\]\s*)?(theorem|lemma|def|abbrev|noncomputable def|noncomputable abbrev)\s+([\w.\']+)', re.S)
AI = re.compile(r'OpenAI|DeepMind|AlphaProof|AlphaEvolve|GPT|Gemini|Aristotle|\bClaude\b|machine-checked|\bAI\b|Kimi|Astra|Harmonic|AxiomProver|Seed-Prover|large language model|LLM', re.I)
def paras(t): return [p.strip() for p in re.split(r'\n\s*\n', t.strip()) if p.strip()]
def split(doc):
    ps = paras(doc)
    k = None
    for i, p in enumerate(ps[:4]):
        if re.search(r'\?\s*$', p) or re.search(r'\?\s*\$\$\s*$', p): k = i; break
    if k is None: k = 0
    st = ps[:k+1]
    while len(st) > 1 and re.match(r'(Yes|No)\b', st[-1]): st.pop()
    return '\n\n'.join(st), '\n\n'.join(ps[k+1:])
res = {}
for f in os.listdir(FC):
    if not f.endswith('.lean'): continue
    n = f[:-5]
    if n not in Y: continue
    s = open(f'{FC}/{n}.lean').read()
    head = re.search(r'/-!(.*?)-/', s, re.S); head = head.group(1) if head else ''
    defs, thms = [], []
    for m in decl.finditer(s):
        doc, attr, kind, name = m.group(1).strip(), m.group(2) or '', m.group(3), m.group(4)
        if 'test' in attr.split(',')[0] if attr else False: continue
        if 'def' in kind or 'abbrev' in kind:
            if not thms and '$' in doc and '`' not in doc and re.match(r"(Let|Define|We say|We call|For |Given|An? [^.]{0,80}\b(is|are) (said|called))", doc): defs.append(doc)
            continue
        if not name.startswith(f'erdos_{n}') or '.variants' in name: continue
        if name == f'erdos_{n}' or '.parts' in name: thms.append(dict(name=name, doc=doc, attr=attr))
    if not thms: continue
    main = [t for t in thms if t['name'] == f'erdos_{n}'] or thms
    if len(main) == 1: q, notes = split(main[0]['doc'])
    else:
        qs, ns, seen = [], [], set()
        for t in main:
            a, b = split(t['doc'])
            if a not in seen: seen.add(a); qs.append(a)
            if b: ns.append(b)
        q = '\n\n'.join(qs) if len(qs) == 1 else '\n\n'.join(f'({chr(97+i)}) ' + x for i, x in enumerate(qs))
        notes = '\n\n'.join(dict.fromkeys(ns))
    if defs: q = '\n\n'.join(defs) + '\n\n' + q
    refs = re.findall(r'^- (.*?)(?=^- |\Z)', head.split('*References:*')[-1], re.S | re.M) if '*References:*' in head else []
    refs = [re.sub(r'\s+', ' ', r).strip() for r in refs]
    attr = main[0]['attr']
    cat = re.search(r'category research (\w+)', attr)
    ams = re.findall(r'AMS ([\d ]+)', attr)
    lean = re.search(r'formal_proof using lean4 at\s*"([^"]+)"', attr)
    y = Y[n]
    res[n] = dict(q=q, notes=notes, refs=refs, fc=cat.group(1) if cat else None, ams=(ams[0].split() if ams else []), lean=lean.group(1) if lean else None,
                  status=y['status']['state'], updated=y['status'].get('last_update'), prize=y.get('prize'), tags=y.get('tags', []), oeis=y.get('oeis', []),
                  ai=bool(AI.search(notes + ' ' + ' '.join(refs))))
json.dump(res, open('erdos_all.json', 'w'), ensure_ascii=False, indent=0)
import collections
print(len(res), 'ai', sum(v['ai'] for v in res.values()), 'with ?', sum('?' in v['q'] for v in res.values()))
print(collections.Counter((v['status'], v['fc']) for v in res.values()).most_common(20))
lens = sorted(len(v['q']) for v in res.values()); print('len q median/max', lens[len(lens)//2], lens[-5:])

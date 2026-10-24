import json, os, re, sys, shutil, glob
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import catalog_src as cat
import catalog_ext   # noqa: F401
import catalog_ext2  # noqa: F401
import catalog_r2    # noqa: F401
import problems_src as pr
from imo_src import IMO
from research_hand import CLAY

SRC = os.path.join(HERE, "..", "src")
OUT = os.environ.get("ATLAS_OUT", os.path.join(HERE, "..", "..", "site"))
PD = os.path.join(OUT, "data", "problems")
shutil.rmtree(PD, ignore_errors=True); os.makedirs(PD)

ids = [c["id"] for c in cat.C]
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]
IDS = set(ids)
FIDS = {f["id"] for f in cat.FIELDS}
for c in cat.C:
    for p in c["pre"]: assert p in IDS, (c["id"], p)
    for f in c["fields"]: assert f in FIDS, (c["id"], f)
    for l in c["links"]: assert l["field"] in FIDS, (c["id"], l)
for e in cat.EVENTS:
    for n in e["nodes"]: assert n in IDS, (e["id"], n)
CF = {c["id"]: c["fields"] for c in cat.C}
def fields_of(concepts, extra=()):
    out = list(extra)
    for c in concepts: out += CF[c]
    return list(dict.fromkeys(out))

# ---------- examples: one of our own per concept ----------
def ans_tex(p):
    if p["t"] == "choice": return p["opts"][p["a"]]
    if p.get("exact"):
        a, b = p["exact"]; return f"${a}$" if b == 1 else f"$\\dfrac{{{a}}}{{{b}}}$"
    if p.get("a") is not None:
        v = p["a"]; return f"${v:.6g}$" if isinstance(v, float) and not float(v).is_integer() else f"${int(v)}$"
    return ""
examples = []  # our own examples were removed from the problem bank (2026-10-23); worked examples live inside lessons
for cid, ps in ({}).items():
    cand = [p for p in ps if p["t"] != "proof"]
    cand.sort(key=lambda p: (not p.get("ex"), p["src"] != "original", abs(p["d"] - 2)))
    if not cand: continue
    p = cand[0]
    examples.append(dict(id=f"EX-{cid}", kind="example", coll="Atlas", title="Example", q=p["q"], concepts=[cid], fields=CF[cid],
                         ans=ans_tex(p), sol=p.get("ex", ""), hint=p.get("hint") or "", opts=p.get("opts") if p["t"] == "choice" else None))

# ---------- olympiad: hand-curated IMO number theory + converted compfiles batches ----------
def aops(src, y, n):
    if src == "IMO": return {"label": "AoPS wiki", "url": f"https://artofproblemsolving.com/wiki/index.php/{y}_IMO_Problems/Problem_{n}"}
    if src == "USAMO" and y: return {"label": "AoPS wiki", "url": f"https://artofproblemsolving.com/wiki/index.php/{y}_USAMO_Problems/Problem_{n}"}
    return None
olympiad, seen = [], set()
for x in IMO:
    y, n = x["year"], x["pos"]
    pid = f"IMO-{y}-P{n}"; seen.add(f"Imo{y}P{n}")
    olympiad.append(dict(id=pid, kind="olympiad", coll="IMO", title=f"IMO {y} · Problem {n}", year=y, q=x["q"], concepts=x["concepts"], fields=fields_of(x["concepts"]),
                         links=[aops("IMO", y, n), {"label": "Lean statement", "url": f"https://github.com/dwrensha/compfiles/blob/main/Compfiles/Imo{y}P{n}.lean"}]))
flagged = []
for f in sorted(glob.glob(os.path.join(SRC, "batches", "out_*.json"))):
    for x in json.load(open(f)):
        if x["file"] in seen or x["source"] == "Classic" or x["file"] in ("Poland1998P4", "Russia1998P42"): continue
        seen.add(x["file"])
        cs = [c for c in x["concepts"] if c in IDS]
        assert cs, x["file"]
        src, y, num = x["source"], x.get("year"), str(x.get("num") or "")
        if x.get("check", "ok") != "ok": flagged.append((x["file"], x["check"]))
        slug = re.sub(r"[^A-Za-z0-9]+", "-", f"{src}-{y or ''}-P{num}").strip("-")
        title = f"{src} {y} · Problem {num}" if y else (f"{src} · {num}" if num else src)
        links = [l for l in [aops(src, y, num), {"label": "Lean statement", "url": f"https://github.com/dwrensha/compfiles/blob/main/Compfiles/{x['file']}.lean"}] if l]
        olympiad.append(dict(id=slug, kind="olympiad", coll=src, title=title, year=y, q=x["q"].strip(), concepts=cs[:3], fields=fields_of(cs[:3]), links=links,
                             note="Statement reconstructed from the formal version." if "reconstruct" in x.get("check", "").lower() or "empty" in x.get("check", "").lower() else None))
ids_o = [p["id"] for p in olympiad]
dups = {i for i in ids_o if ids_o.count(i) > 1}
for p in olympiad:
    if p["id"] in dups: p["id"] += "-" + re.sub(r"\W", "", p["links"][-1]["url"].rsplit("/", 1)[-1][:-5])
def okey(p):
    m = re.search(r"(\d+)\D*$", p["title"]); return (p["year"] or 0, p["coll"], int(m.group(1)) if m else 0)
olympiad.sort(key=okey)

# Putnam (PutnamBench informal statements, published with permission of the MAA). Answers are not included.
def detex_text(t):
    """Turn text-mode LaTeX (enumerate/itemize/emph/center/tabular-free) into the site's plain-text conventions, leaving math alone."""
    parts = re.split(r"(\$\$.*?\$\$|\$[^$]*\$)", t, flags=re.S)
    out = []
    for i, x in enumerate(parts):
        if i % 2: out.append(x); continue
        x = re.sub(r"\\(?:emph|textit|textbf|text)\{([^{}]*)\}", r"\1", x)
        x = re.sub(r"\{\\em\s+([^{}]*)\}", r"\1", x)
        x = re.sub(r"\\(?:begin|end)\{center\}", "", x)
        x = re.sub(r"\\noindent\s*", "", x)
        out.append(x)
    t = "".join(out)
    def lst(m, ordered):
        items = [it.strip() for it in re.split(r"\\item\s*", m.group(1)) if it.strip()]
        lab = re.match(r"\[([^\]]*)\]", items[0]) if items else None
        lines = []
        for k, it in enumerate(items, 1):
            mm = re.match(r"\[([^\]]*)\]\s*", it)
            if mm: lines.append(f"{k}. ({mm.group(1).strip('()')}) " + it[mm.end():].replace("\n", " ") if False else f"{k}. " + it[mm.end():].replace("\n", " "))
            else: lines.append((f"{k}. " if ordered else "- ") + it.replace("\n", " "))
        return "\n\n" + "\n".join(lines) + "\n\n"
    t = re.sub(r"\\begin\{enumerate\}(?:\[[^\]]*\])?(.*?)\\end\{enumerate\}", lambda m: lst(m, True), t, flags=re.S)
    t = re.sub(r"\\begin\{itemize\}(.*?)\\end\{itemize\}", lambda m: lst(m, False), t, flags=re.S)
    t = re.sub(r"(?<![\\$a-zA-Z])lim(?=_| ?\\)", r"\\lim", t) if False else t
    t = "".join(x if i % 2 else x.replace("``", "“").replace("''", "”") for i, x in enumerate(re.split(r"(\$\$.*?\$\$|\$[^$]*\$)", t, flags=re.S))).replace("factorails", "factorials")
    return re.sub(r"\n{3,}", "\n\n", t).strip()
PT = {}
PEX = set(json.load(open(os.path.join(HERE, "..", "round2", "putnam", "exclude.json")))) if os.path.exists(os.path.join(HERE, "..", "round2", "putnam", "exclude.json")) else set()
for f in sorted(glob.glob(os.path.join(HERE, "..", "round2", "putnam", "out_*.json"))):
    for x in json.load(open(f)): PT[x["name"]] = x
LEAN_PUTNAM = set(open(os.path.join(SRC, "PutnamBench", "lean_names.txt")).read().split())
for p in json.load(open(os.path.join(SRC, "PutnamBench", "informal", "putnam.json"))):
    t = PT.get(p["problem_name"])
    if not t or p["problem_name"] in PEX: continue
    if re.search(r"\\(begin\{(tabular|center)|item\b|emph)", detex_text(p["informal_statement"])): continue
    cs = [c for c in t["concepts"] if c in IDS][:3]
    if not cs: continue
    m = re.match(r"putnam_(\d{4})_([ab]\d)", p["problem_name"]); y, n = int(m.group(1)), m.group(2).upper()
    olympiad.append(dict(id=f"PUTNAM-{y}-{n}", kind="olympiad", coll="Putnam", title=f"Putnam {y} · {n}", year=y, q=detex_text(p["informal_statement"]), concepts=cs, fields=fields_of(cs),
                         links=[{"label": "Lean statement (PutnamBench)", "url": f"https://github.com/trishullab/PutnamBench/blob/main/lean4/src/{p['problem_name']}.lean"}] if p["problem_name"] in LEAN_PUTNAM else []))
olympiad.sort(key=okey)

# ---------- research ----------
TAG = {"primes": "prime-patterns", "divisors": "arithmetic-functions", "unit fractions": "unit-fractions", "sidon sets": "sidon-sets",
       "additive basis": "additive-bases", "complete sequences": "additive-bases", "arithmetic progressions": "arithmetic-progressions",
       "additive combinatorics": "additive-combinatorics", "covering systems": "covering-systems", "binomial coefficients": "binomial-factorial",
       "factorials": "binomial-factorial", "powerful": "smooth-powerful", "squares": "smooth-powerful", "powers": "smooth-powerful",
       "irrationality": "diophantine-approx", "irrational": "diophantine-approx", "diophantine approximation": "diophantine-approx",
       "primitive sets": "primitive-sets", "discrepancy": "discrepancy", "base representations": "digits-bases", "iterated functions": "arithmetic-functions",
       "chromatic number": "graph-coloring", "hypergraphs": "hypergraphs", "turan number": "extremal-graphs", "cycles": "cycles-matchings",
       "distances": "discrete-geometry", "geometry": "discrete-geometry", "convex": "discrete-geometry", "intersecting family": "set-systems",
       "set theory": "infinite-combinatorics", "planar graphs": "graph-coloring", "group theory": "groups"}
def erdos_concepts(tags):
    nt = "number theory" in tags
    cs = [TAG[t] for t in tags if t in TAG]
    if "ramsey theory" in tags or "ramsey" in tags: cs.append("ramsey-arithmetic" if nt else "ramsey")
    if "polynomials" in tags: cs.append("integer-polynomials" if nt else "polynomials-roots")
    if "probability" in tags or "distribution" in tags: cs.append("probabilistic-nt" if nt else "probabilistic-method")
    if "analysis" in tags and not cs: cs.append("sequences")
    if "graph theory" in tags and not cs: cs.append("graph-basics")
    if not cs: cs.append("combinatorial-nt" if nt else ("set-systems" if "combinatorics" in tags else "graph-basics"))
    return list(dict.fromkeys(cs))
TFIELD = {"number theory": "number-theory", "graph theory": "combinatorics", "ramsey theory": "combinatorics", "hypergraphs": "combinatorics", "chromatic number": "combinatorics",
          "combinatorics": "combinatorics", "additive combinatorics": "combinatorics", "geometry": "geometry", "distances": "geometry", "convex": "geometry",
          "analysis": "real-analysis", "probability": "probability", "set theory": "logic", "group theory": "algebra", "algebra": "algebra", "topology": "topology"}
AMS = {"5": "combinatorics", "11": "number-theory", "52": "geometry", "51": "geometry", "3": "logic", "26": "real-analysis", "28": "real-analysis",
       "40": "real-analysis", "41": "real-analysis", "42": "harmonic-analysis", "60": "probability", "20": "algebra", "12": "algebra", "68": "computer-science", "14": "algebraic-geometry", "54": "topology", "57": "topology"}
OPENAI_OCT = {3, 90, 120, 138, 148, 172, 181, 184, 293, 304, 371, 416, 431, 508, 551, 604, 802, 821, 952, 968, 970, 1083, 1150}
AI = re.compile(r"OpenAI|DeepMind|AlphaProof|AlphaEvolve|GPT|Gemini|Aristotle|\bClaude\b|\bAI\b|Kimi|Astra|Harmonic|AxiomProver|Seed-Prover|language model|\bLLM|Codex")
FIX = [("\\pmd", "\\pm"), ("(\\sp{2n}\\sb{n})", "\\binom{2n}{n}"), ("da\\ss", "daß"), ('\\"U', "Ü"), ('\\"u', "ü"), ('\\"o', "ö"), ('\\"a', "ä"), ('\\"O', "Ö"),
       ("\\'e", "é"), ("\\'a", "á"), ("\\H{o}", "ő"), ("\\'{e}", "é"), ('\\"{o}', "ö"), ('\\"{u}', "ü"), ("\\'{a}", "á"), ("\\mathbf{Z}", "\\mathbb{Z}"), ("\\mathbf{N}", "\\mathbb{N}")]
FIX.append(("\\mamthbb", "\\mathbb"))
def fix(t):
    for a, b in FIX: t = t.replace(a, b)
    t = re.sub(r"^\*\*[^*]{0,80}\*\*:?\s*", "", t)
    t = re.sub(r"(?<=[\s(])\$(\d\d+(?:,\d{3})*)(?=\s+(?:is|for|was|prize|reward|to anyone)\b|\)|\.\s)", r"\\$\1", t)
    return t
def status_of(raw, fc, n=None):
    base = raw.replace(" (Lean)", "")
    group = "solved" if base in ("proved", "disproved", "solved") else "open"
    claim = None
    if group == "open" and n is not None and int(n) in OPENAI_OCT: claim = "A solution is claimed in OpenAI's October 2026 release; not yet checked by erdosproblems.com."
    elif group == "open" and fc == "solved": claim = "formal-conjectures records this as solved; erdosproblems.com still lists it as open."
    if n is not None and int(n) == 3: claim = "OpenAI's October 2026 release claims a proof through a 198-page manuscript. According to Thomas Bloom, the accompanying Lean file proves only a weaker bound, and erdosproblems.com still lists the problem as open."
    if claim: group = "claimed"
    label = {"proved": "Proved", "disproved": "Disproved", "solved": "Solved", "open": "Open"}.get(base, base.capitalize())
    return group, label, "(Lean)" in raw, claim
research = []
E = json.load(open(os.path.join(SRC, "erdos_all.json")))
for n, v in E.items():
    q, notes, refs = fix(v["q"]), fix(v["notes"]).strip(), [fix(r) for r in v["refs"]][:12]
    concepts = erdos_concepts(v["tags"])
    fields = list(dict.fromkeys([TFIELD[t] for t in v["tags"] if t in TFIELD] + [AMS[a] for a in v["ams"] if a in AMS])) or fields_of(concepts)
    group, label, lean, claim = status_of(v["status"], v["fc"], n)
    links = [{"label": "erdosproblems.com", "url": f"https://www.erdosproblems.com/{n}"},
             {"label": "Lean statement", "url": f"https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/{n}.lean"}]
    if v["lean"]: links.append({"label": "Formal proof" if group != "claimed" else "Claimed formal proof", "url": v["lean"]})
    for o in v["oeis"][:3]: links.append({"label": f"OEIS {o}", "url": f"https://oeis.org/{o}"})
    prize = v["prize"] if v["prize"] and v["prize"] != "no" else None
    research.append(dict(id=f"ERDOS-{n}", kind="research", coll="Erdős", title=f"Erdős Problem #{n}", num=int(n), q=q, concepts=concepts, fields=fields,
                         status=group, slabel=label, lean=lean, claim=claim, prize=prize, updated=v["updated"], notes=notes, refs=refs,
                         ai=bool(AI.search(notes)) or int(n) in OPENAI_OCT, tags=v["tags"], links=links))
GKEY = [(r"Sidon|B_2|B_h", "sidon-sets"), (r"progression|Szemer|r_3|r_k|Roth", "arithmetic-progressions"), (r"van der Waerden|W\(", "ramsey-arithmetic"),
        (r"sum-free|sumset|A\s*\+\s*A|A \\hat|doubling|Freiman|additive energy", "additive-combinatorics"), (r"Ramsey", "ramsey"), (r"prime", "prime-patterns"),
        (r"graph", "graph-basics"), (r"group|A_n|S_n", "groups"), (r"colou?r", "ramsey-arithmetic"), (r"measure|\[0,\s*1\]|open set", "additive-combinatorics"),
        (r"\\mathbb\{F\}|\\mathbf\{F\}|\\F_|cap set", "additive-combinatorics"), (r"polynomial", "polynomials-roots"), (r"divisor|lcm|gcd", "arithmetic-functions")]
G = json.load(open(os.path.join(SRC, "green.json")))
for n, v in G.items():
    text = v["q"] + " " + v["notes"]
    cs = list(dict.fromkeys(c for pat, c in GKEY if re.search(pat, text)))[:3] or ["additive-combinatorics"]
    fields = list(dict.fromkeys([AMS[a] for a in v["ams"] if a in AMS])) or fields_of(cs)
    st = "solved" if v["status"] == "solved" else "open"
    links = [{"label": "Green, 100 open problems", "url": f"https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.{n}"},
             {"label": "Lean statement", "url": f"https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/GreensOpenProblems/{n}.lean"}]
    if v["lean"]: links.append({"label": "Formal proof", "url": v["lean"]})
    notes = fix(v["notes"]).strip()
    research.append(dict(id=f"GREEN-{n}", kind="research", coll="Green", title=f"Green's Problem {n}", num=int(n), q=fix(v["q"]), concepts=cs, fields=fields,
                         status=st, slabel="Solved" if st == "solved" else "Open", lean=bool(v["lean"]), claim=None, prize=None, notes=notes, refs=[fix(r) for r in v["refs"]][:12],
                         ai=bool(AI.search(notes)), links=links))
for x in CLAY:
    for c in x["concepts"]: assert c in IDS, x
    research.append(dict(id=f"CLAY-{x['key']}", kind="research", coll="Millennium", title=f"Millennium Prize · {x['title']}", num=0, q=x["q"], concepts=x["concepts"], fields=x["fields"],
                         status=x["status"], slabel=x.get("slabel", "Open"), lean=False, claim=None, prize="$1,000,000", notes=x.get("notes", ""), refs=[], ai=False,
                         links=[{"label": "Clay Mathematics Institute", "url": "https://www.claymath.org/millennium-problems/"}]))

# ---------- textbook exercises (openly licensed books; statements only) ----------
LIC = {"Understanding Linear Algebra": ("CC BY 4.0", "https://creativecommons.org/licenses/by/4.0/", "David Austin, Understanding Linear Algebra"),
       "Applied Combinatorics": ("CC BY-SA 4.0", "https://creativecommons.org/licenses/by-sa/4.0/", "Mitchel T. Keller and William T. Trotter, Applied Combinatorics")}
SHORT = {"Understanding Linear Algebra": ("ULA", "Austin, Understanding Linear Algebra"), "Applied Combinatorics": ("AC", "Keller & Trotter, Applied Combinatorics")}
TBEX = set(json.load(open(os.path.join(HERE, "..", "round3", "exclude.json")))) if os.path.exists(os.path.join(HERE, "..", "round3", "exclude.json")) else set()
textbook = []
for x in json.load(open(os.path.join(HERE, "..", "round3", "textbook_raw.json"))):
    cs = [c for c in x["concepts"] if c in IDS]
    if not cs: continue
    code, coll = SHORT[x["book"]]
    sec = x["sec"]
    secno = sec.split(" ")[0] if code == "ULA" else ""
    pid = re.sub(r"[^A-Za-z0-9.]+", "-", f"{code}-{secno or sec}-{x['num']}").strip("-")
    if pid in TBEX: continue
    lic = LIC[x["book"]]
    textbook.append(dict(id=pid, kind="textbook", coll=coll, title=(f"{code} {secno} · Exercise {x['num']}" if secno else f"{code} · {sec} · Exercise {x['num']}"), section=sec,
                         q=x["q"], concepts=cs, fields=fields_of(cs), license=lic[0], license_url=lic[1], credit=lic[2],
                         links=[{"label": "Book", "url": x["link"]}, {"label": lic[0], "url": lic[1]}]))
ids_t = [p["id"] for p in textbook]; assert len(ids_t) == len(set(ids_t)), [i for i in ids_t if ids_t.count(i) > 1][:5]

# ---------- bridge ladders: ordered steps from olympiad/textbook level to research problems (reviewed only) ----------
bridge = []
RIDS = {p["id"] for p in research}
for f in sorted(glob.glob(os.path.join(HERE, "..", "round4", "ladders", "ladder_final_*.json"))):
    for L in json.load(open(f)):
        cid = L["concept"]
        if cid not in IDS: continue
        rungs = L["ladder"]
        for k, r in enumerate(rungs, 1):
            cs = [c for c in r.get("concepts", []) if c in IDS]
            if cid not in cs: cs = [cid] + cs
            bridge.append(dict(id=f"LAD-{cid}-{k}", kind="bridge", coll="Ladder", title=r["title"], year=r.get("year"), q=r["q"], concepts=cs, fields=fields_of(cs),
                               ladder=dict(concept=cid, step=k, of=len(rungs)), rkind=r.get("kind", ""), source=r.get("source", ""), note=r.get("note", ""),
                               bridges_to=[b for b in r.get("bridges_to", []) if b in RIDS]))
ALL = {"textbook": textbook, "olympiad": olympiad, "bridge": bridge, "research": research, "examples": examples}
for k, ps in ALL.items():
    for p in ps:
        for c in p["concepts"]: assert c in IDS, (p["id"], c)
        for f in p["fields"]: assert f in FIDS, (p["id"], f)
    assert len({p["id"] for p in ps}) == len(ps), k
    with open(os.path.join(PD, k + ".json"), "w", encoding="utf8") as f:
        json.dump(ps, f, ensure_ascii=False, separators=(",", ":"))

# ---------- lessons (AI-written, independently reviewed) ----------
LD = os.path.join(OUT, "data", "lessons"); shutil.rmtree(LD, ignore_errors=True); os.makedirs(LD)
LESSONS = {}
for f in sorted(glob.glob(os.path.join(HERE, "..", "lessons", "final_*.json"))):
    for les in json.load(open(f)):
        assert les["id"] in IDS, les["id"]
        LESSONS[les["id"]] = les
        with open(os.path.join(LD, les["id"] + ".json"), "w", encoding="utf8") as g:
            json.dump({"blocks": les["blocks"], "sources": les.get("sources", [])}, g, ensure_ascii=False, separators=(",", ":"))

for cid, les in catalog_r2.LESSONS_R2.items():
    LESSONS[cid] = les
    with open(os.path.join(LD, cid + ".json"), "w", encoding="utf8") as g:
        json.dump({"blocks": les["blocks"], "sources": les.get("sources", [])}, g, ensure_ascii=False, separators=(",", ":"))
REVIEW = {}
for f in glob.glob(os.path.join(HERE, "..", "lessons", "review_*.json")) + glob.glob(os.path.join(HERE, "..", "round2", "review_*.json")):
    for r in json.load(open(f)): REVIEW[r["id"]] = sum(1 for i in r.get("issues", []) if i.get("severity") == "error")

# ---------- reviewed corrections to catalog entries (round 4 reviewers) ----------
FIXKEY = {"summary": "sum", "key_statements": "key", "why": "why"}
CBY = {c["id"]: c for c in cat.C}
for f in sorted(glob.glob(os.path.join(HERE, "..", "round4", "entry_fixes_*.json"))):
    for fx in json.load(open(f)):
        c = CBY.get(fx["id"]); k = FIXKEY.get(fx["field"])
        if c and k and fx.get("corrected") is not None: c[k] = fx["corrected"]

# ---------- catalog ----------
order = {b["id"]: i for i, b in enumerate(cat.BANDS)}
concepts = sorted(cat.C, key=lambda c: order[c["band"]])
for c in concepts:
    for k in ("no", "counts"): c.pop(k, None)
    c["np"] = {k: sum(1 for p in ps if c["id"] in p["concepts"]) for k, ps in ALL.items()}
    c["nprob"] = sum(c["np"].values())
    if c["id"] in LESSONS: c["lesson"] = {"minutes": LESSONS[c["id"]].get("minutes", 15), "checks": len(LESSONS[c["id"]].get("checks", [])), "fixed": REVIEW.get(c["id"], 0)}
colls = {}
for ps in ALL.values():
    for p in ps: colls[p["coll"]] = colls.get(p["coll"], 0) + 1
stats = {"textbook": len(textbook), "olympiad": len(olympiad), "bridge": len(bridge), "research": len(research), "examples": len(examples), "total": sum(len(v) for v in ALL.values()),
         "open": sum(p["status"] == "open" for p in research), "solved": sum(p["status"] == "solved" for p in research), "claimed": sum(p["status"] == "claimed" for p in research), "collections": colls}
catalog = {"bands": cat.BANDS, "fields": cat.FIELDS, "concepts": concepts, "events": cat.EVENTS, "built": "2026-10-23", "stats": stats,
           "credits": ["Textbook exercises: David Austin, Understanding Linear Algebra (CC BY 4.0); Mitchel T. Keller and William T. Trotter, Applied Combinatorics (CC BY-SA 4.0). Statements only, reformatted; exercises from CC BY-SA sources are shared under CC BY-SA 4.0.",
                       "Olympiad statements: IMO, USAMO and national olympiads, cross-checked with the compfiles Lean statements (Apache-2.0).",
                       "Erdős and Green problems: google-deepmind/formal-conjectures (Apache-2.0); Erdős status from teorth/erdosproblems, mirroring erdosproblems.com.",
                       "Millennium Prize Problems: stated in our own words after the Clay Mathematics Institute descriptions."]}
js = json.dumps(catalog, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
tpl = open(os.path.join(HERE, "template.html"), encoding="utf8").read()
html = tpl.replace("/*CATALOG*/", js)
open(os.path.join(OUT, "index.html"), "w", encoding="utf8").write(html)
empty = [c["id"] for c in concepts if c["nprob"] == 0]
print(len(concepts), "concepts;", {k: v for k, v in stats.items() if k != "collections"}, colls, "; no problems:", empty, "; html KB", len(html) // 1024,
      "; files KB", {k: os.path.getsize(os.path.join(PD, k + ".json")) // 1024 for k in ALL})
print("flagged:", len(flagged), "lessons:", len(LESSONS))

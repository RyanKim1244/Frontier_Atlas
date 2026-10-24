# Round 4: topic areas (no level-based areas), new topic concepts from textbook TOC surveys.
# New concepts are published only once their entry and lesson are independently reviewed (round4/concepts/final_*.json).
import os, sys, json, glob
import catalog_src as cat
import catalog_ext   # noqa
import catalog_ext2  # noqa
import catalog_r2    # noqa
from catalog_src import C, FIELDS, BANDS
HERE = os.path.dirname(os.path.abspath(__file__))
R4 = os.path.join(HERE, "..", "round4")
import importlib.util as _u
_s = _u.spec_from_file_location("curriculum_r4", os.path.join(R4, "curriculum.py")); _m = _u.module_from_spec(_s); _s.loader.exec_module(_m)
CUR, AREAS, NEW_FIELDS, MOVE, REWIRE, RENAME_AREAS, DROP_AREAS = _m.C, _m.AREAS, _m.NEW_FIELDS, _m.MOVE, _m.REWIRE, _m.RENAME_AREAS, _m.DROP_AREAS

for f in NEW_FIELDS:
    if not any(x["id"] == f["id"] for x in FIELDS): FIELDS.append(dict(f, built=True))

FINAL = {}
for f in sorted(glob.glob(os.path.join(R4, "concepts", "final_*.json"))):
    for x in json.load(open(f)): FINAL[x["id"]] = x
LESSONS_R4 = {}
present = {c["id"] for c in C}
for (cid, title, short, area, fields, stage, pre) in CUR:
    x = FINAL.get(cid)
    if not x: continue
    e = x["entry"]
    C.append(dict(id=cid, band=area, title=title, short=short, pre=list(pre), sum=e["sum"], key=list(e.get("key", [])), why=e.get("why", ""),
                  msc=list(e.get("msc", [])), links=[l for l in e.get("links", []) if l.get("field") and l["field"] not in fields], refs=list(e.get("refs", [])),
                  status=None, aliases=list(e.get("aliases", [])), fields=list(fields), stage=stage))
    LESSONS_R4[cid] = dict(id=cid, **x["lesson"])

# Round 5: source-composed pages (depth standard, pipeline/round5/DEPTH.md); same publish rule.
R5 = os.path.join(HERE, "..", "round5")
_s5 = _u.spec_from_file_location("curriculum_r5", os.path.join(R5, "curriculum.py")); _m5 = _u.module_from_spec(_s5); _s5.loader.exec_module(_m5)
FINAL5 = {}
for f in sorted(glob.glob(os.path.join(R5, "concepts", "final_*.json"))):
    for x in json.load(open(f)): FINAL5[x["id"]] = x
for a in getattr(_m5, "NEW_AREAS", []):
    if not any(x["id"] == a["id"] for x in AREAS): AREAS.append(dict(a))
for (cid, title, short, area, fields, stage, pre) in _m5.C:
    x = FINAL5.get(cid)
    if not x: continue
    assert not any(c["id"] == cid for c in C), cid
    e = x["entry"]
    C.append(dict(id=cid, band=area, title=title, short=short, pre=list(pre), sum=e["sum"], key=list(e.get("key", [])), why=e.get("why", ""),
                  msc=list(e.get("msc", [])), links=[l for l in e.get("links", []) if l.get("field") and l["field"] not in fields], refs=list(e.get("refs", [])),
                  status=None, aliases=list(e.get("aliases", [])), fields=list(fields), stage=stage))
    LESSONS_R4[cid] = dict(id=cid, **x["lesson"])
present = {c["id"] for c in C}
for c in C:
    c["pre"] = [p for p in c["pre"] if p in present]
    if c["id"] in MOVE: c["band"] = MOVE[c["id"]]
for cid, extra in REWIRE:
    c = next((c for c in C if c["id"] == cid), None)
    if c: c["pre"] += [p for p in extra if p in present and p not in c["pre"]]

# Areas: rename, drop level-based ones, add topic areas (kept only if they hold a concept), order by topic.
for b in BANDS:
    if b["id"] in RENAME_AREAS: b["name"], b["blurb"] = RENAME_AREAS[b["id"]]
    if b["id"] == "foundations": b["name"], b["blurb"] = "Elementary number theory", "Divisibility, congruences, primes and Diophantine equations."
used = {c["band"] for c in C}
for a in AREAS:
    if not any(b["id"] == a["id"] for b in BANDS): BANDS.append(dict(a))
ORDER = ["logic", "functions", "precalc", "calculus", "realanalysis", "complex", "harmonic", "odes", "dynamics", "pde", "functional", "linalg", "abstract", "lie",
         "topology", "diffgeo", "alggeo", "foundations", "analytic", "algebraic", "combinatorial", "discrete", "olyalg", "geometry", "probability", "statistics", "numerics", "computation"]
BANDS[:] = sorted([b for b in BANDS if b["id"] not in DROP_AREAS and b["id"] in used], key=lambda b: ORDER.index(b["id"]) if b["id"] in ORDER else 99)
assert all(c["band"] in {b["id"] for b in BANDS} for c in C), [c["id"] for c in C if c["band"] not in {b["id"] for b in BANDS}]

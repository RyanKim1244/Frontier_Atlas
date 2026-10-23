# Round 2: precalculus, calculus, real analysis, linear algebra, abstract algebra, probability.
# Concept entries and lessons are AI-written and independently reviewed (round2/final_*.json).
import os, sys, json, glob
import catalog_src as cat
import catalog_ext   # noqa
import catalog_ext2  # noqa
from catalog_src import C, FIELDS, BANDS
HERE = os.path.dirname(os.path.abspath(__file__))
R2 = os.path.join(HERE, "..", "round2")
sys.path.insert(0, R2)
from curriculum import C as CUR, AREAS, NEW_FIELDS, REWIRE

FIELDS.extend(NEW_FIELDS)
pos = next(i for i, b in enumerate(BANDS) if b["id"] == "olyalg")
for a in reversed(AREAS): BANDS.insert(pos, a)   # analysis-like areas before the olympiad ones

FINAL = {}
for f in sorted(glob.glob(os.path.join(R2, os.environ.get("ATLAS_R2_GLOB", "final_*.json")))):
    for x in json.load(open(f)): FINAL[x["id"]] = x
LESSONS_R2 = {}
for (cid, title, short, area, fields, stage, pre) in CUR:
    x = FINAL.get(cid)
    if not x: continue            # not reviewed yet: not published
    e = x["entry"]
    C.append(dict(id=cid, band=area, title=title, short=short, pre=list(pre), sum=e["sum"], key=list(e.get("key", [])), why=e.get("why", ""),
                  msc=list(e.get("msc", [])), links=[l for l in e.get("links", []) if l.get("field") and l["field"] not in fields], refs=list(e.get("refs", [])),
                  status=None, aliases=list(e.get("aliases", [])), fields=list(fields), stage=stage))
    LESSONS_R2[cid] = dict(id=cid, **x["lesson"])
present = {c["id"] for c in C}
for c in C:   # drop prerequisites that are not published yet
    c["pre"] = [p for p in c["pre"] if p in present]
for cid, extra, area in REWIRE:
    c = next(c for c in C if c["id"] == cid)
    c["pre"] += [p for p in extra if p in present and p not in c["pre"]]
    if area: c["band"] = area
lin = next(c for c in C if c["id"] == "linear-algebra")
lin["title"], lin["short"] = "Linear algebra methods in combinatorics", "Linear algebra methods"

STAGE = {}
for i in "divisibility bezout fta digits-bases pythagorean counting pigeonhole euclid-basics circles amgm polynomials-roots sequences floor-functions complex-numbers".split(): STAGE[i] = "school"
for i in ("congruences mod-inverse crt fermat-euler wilson order-primroot p-adic-valuation quadratic-residues diophantine vieta-jumping lte-zsigmondy binomial-factorial "
          "integer-polynomials integer-functional-eq invariants comb-games grids-tilings cauchy-schwarz convexity symmetric-ineq real-functional-eq triangle-centres "
          "geo-transformations analytic-geometry geo-inequalities lucas sums-of-squares combinatorial-nt").split(): STAGE[i] = "olympiad"
for i in ("functional-equation nontrivial-zeros explicit-formula zero-free-region class-number-formula siegel-zeros siegel-walfisz sieve-basics selberg-sieve large-sieve "
          "bombieri-vinogradov bounded-gaps exponential-sums circle-method ternary-goldbach waring moments zero-density dedekind-zeta hecke-l additive-combinatorics "
          "arithmetic-progressions sidon-sets additive-bases unit-fractions covering-systems primitive-sets ramsey-arithmetic discrepancy hypergraphs discrete-geometry "
          "infinite-combinatorics smooth-powerful prime-patterns probabilistic-nt diophantine-approx mellin continuation").split(): STAGE[i] = "graduate"
for i in "lindelof pair-correlation rh grh quasi-rh no-siegel twin-primes goldbach bsd p-vs-np navier-stokes yang-mills hodge poincare".split(): STAGE[i] = "research"
for c in C:
    if "stage" not in c: c["stage"] = STAGE.get(c["id"], "undergraduate")

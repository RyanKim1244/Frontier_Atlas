"""Validate round-5 page files: schema, src keys, links, $ balance, figure compile. Usage: validate.py file.json [...]"""
import json, os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
IDS = {c["id"] for c in json.load(open(os.path.join(D, "all_concepts.json")))}
FIELDS = set(json.load(open(os.path.join(D, "field_ids.json"))))
BRIEF = {b["id"]: b for b in json.load(open(os.path.join(D, "brief.json")))}
TYPES = {"intro", "section", "definition", "theorem", "proof", "example", "pitfall", "connection", "exercise", "views", "conventions", "figure", "check", "summary"}
sys.path.insert(0, "/home/claude/frontier_atlas/pipeline/atlas")
errs = []
def E(cid, m): errs.append(f"{cid}: {m}")
def text_ok(cid, where, s):
    if not isinstance(s, str): E(cid, f"{where}: not a string"); return
    t = s.replace("\\$", "")
    if t.count("$$") % 2: E(cid, f"{where}: odd $$")
    if t.replace("$$", "").count("$") % 2: E(cid, f"{where}: odd $")
    for m in re.findall(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", s):
        if m not in IDS: E(cid, f"{where}: bad link [[{m}]]")
    if re.search(r"\*\*|`|<[a-z]+[ >]|^#", s, re.M): E(cid, f"{where}: markdown/HTML")
for f in sys.argv[1:]:
    for x in json.load(open(f)):
        cid = x["id"]; e = x.get("entry", {}); L = x.get("lesson", {})
        if cid not in BRIEF: E(cid, "not in brief")
        for k in ("sum", "key", "why", "msc", "links", "refs", "aliases"):
            if k not in e: E(cid, "entry missing " + k)
        for l in e.get("links", []):
            if l.get("field") not in FIELDS or l.get("field") in BRIEF.get(cid, {}).get("fields", []): E(cid, f"entry link field {l.get('field')}")
        if L.get("v") != 2: E(cid, "lesson.v != 2")
        keys = [s.get("k") for s in L.get("sources", [])]
        if len(keys) != len(set(keys)) or None in keys: E(cid, "source keys missing/duplicate")
        K = set(keys)
        if sum(1 for s in L.get("sources", []) if s.get("kind") == "paper") < 3: E(cid, "fewer than 3 papers in sources")
        for r in L.get("requires", []):
            if r.get("priority") not in ("core", "common", "specialised"): E(cid, f"requires priority {r}")
            text_ok(cid, "requires", r.get("item", "") + " " + r.get("where", ""))
        titles = {b.get("title") for b in L.get("blocks", [])}
        nviews = 0; uncited = 0
        for i, b in enumerate(L.get("blocks", [])):
            t = b.get("type"); w = f"block {i} {t} {b.get('title','')!r}"
            if t not in TYPES: E(cid, w + ": bad type"); continue
            for k in b.get("src", []):
                if k not in K: E(cid, w + f": unknown src {k}")
            if t in ("section", "definition") and not b.get("src"): uncited += 1
            for fld in ("body", "solution", "caption"):
                if fld in b: text_ok(cid, w + "." + fld, b[fld])
            if t == "exercise":
                its = b.get("items")
                if not its: E(cid, w + ": exercise needs items with q/hint/solution")
                for it in its or []:
                    if not (it.get("q") and it.get("hint") and it.get("solution")): E(cid, w + ": exercise item incomplete")
                    for fld in ("q", "hint", "solution"): text_ok(cid, w + "." + fld, it.get(fld, ""))
            if t == "check":
                for it in b.get("items", []):
                    if not (it.get("q") and it.get("a")): E(cid, w + ": check item incomplete")
                    text_ok(cid, w + ".check", it.get("q", "") + " " + it.get("a", ""))
            if t == "views":
                nviews += 1
                if not 2 <= len(b.get("items", [])) <= 5: E(cid, w + ": views needs 2-5 items")
                for it in b.get("items", []):
                    text_ok(cid, w + ".item", it.get("body", ""))
                    if not it.get("src"): E(cid, w + f": view {it.get('label')} without src")
                    for k in it.get("src", []):
                        if k not in K: E(cid, w + f": unknown src {k}")
            if t == "conventions":
                for r in b.get("rows", []):
                    text_ok(cid, w + ".row", r.get("text", ""))
                    for k in r.get("src", []):
                        if k not in K: E(cid, w + f": unknown src {k}")
            if t == "figure":
                import figures, tempfile
                try:
                    with tempfile.TemporaryDirectory() as d: figures.compile_svg(b["engine"], b["code"], os.path.join(d, "x.svg"))
                except Exception as ex: E(cid, w + f": figure does not compile: {str(ex)[:200]}")
        if nviews < 1: E(cid, "no views block")
        ntypes = {b.get("type") for b in L.get("blocks", [])}
        for need in ("exercise", "check", "summary"):
            if need not in ntypes: E(cid, "no " + need + " block")
        if uncited: E(cid, f"{uncited} sections/definitions without src")
        words = sum(len(json.dumps(b).split()) for b in L.get("blocks", []))
        print(cid, "blocks", len(L.get("blocks", [])), "~words", words, "sources", len(K), "views", nviews, "requires", len(L.get("requires", [])), "checks", len(L.get("checks", [])))
print("OK" if not errs else "\n".join(errs))

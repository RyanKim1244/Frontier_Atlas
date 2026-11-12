"""Write the inputs for one school cluster: brief.json (concepts of the cluster) and all_concepts.json (valid [[link]] ids:
published pages + this cluster). Usage: make_inputs.py <work-folder> id1 id2 ..."""
import json, os, sys, glob, importlib.util as u
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", ".."); W = sys.argv[1]; ids = sys.argv[2:]
sys.path.insert(0, os.path.join(P, "atlas")); os.environ["ATLAS_SCHOOL_EXTRA"] = ""
import catalog_r4 as cat
pub = [{"id": c["id"], "title": c["title"]} for c in cat.C]
s = u.spec_from_file_location("cur", os.path.join(H, "..", "curriculum.py")); m = u.module_from_spec(s); s.loader.exec_module(m)
raw = json.load(open(os.path.join(H, "..", "concepts_raw.json")))["merged"]["concepts"]; R = {c["id"]: c for c in raw}
later = lambda i: [c["id"] for c in raw if i in c["prerequisites"]]
brief = []
for (cid, title, short, area, fields, stage, pre) in m.C:
    if cid not in ids: continue
    r = R.get(cid, {})
    brief.append(dict(id=cid, title=title, fields=fields, prerequisites=pre, stage=m.STAGE_DETAIL.get(cid, stage),
                      curriculum_refs=r.get("sources", []), related_existing_page=r.get("existing_match", ""), later_concepts=later(cid)))
known = {c["id"] for c in pub}
allc = pub + [{"id": b["id"], "title": b["title"]} for b in brief if b["id"] not in known]
json.dump(brief, open(os.path.join(W, "brief.json"), "w"), ensure_ascii=False, indent=1)
json.dump(allc, open(os.path.join(W, "all_concepts.json"), "w"), ensure_ascii=False)
json.dump([f["id"] for f in cat.FIELDS], open(os.path.join(W, "field_ids.json"), "w"))
print(len(brief), "concepts;", len(allc), "link ids")

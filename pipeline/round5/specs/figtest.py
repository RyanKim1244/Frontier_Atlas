"""Compile every figure block of a page file to PNG in figpng/ for visual inspection. Usage: figtest.py file.json"""
import json, os, subprocess, sys, tempfile
sys.path.insert(0, "/home/claude/frontier_atlas/pipeline/atlas")
import figures
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(D, "figpng"); os.makedirs(OUT, exist_ok=True)
for x in json.load(open(sys.argv[1])):
    for i, b in enumerate(x["lesson"]["blocks"]):
        if b.get("type") != "figure": continue
        name = f"{x['id']}_{i}"
        try:
            with tempfile.TemporaryDirectory() as d:
                figures.compile_svg(b["engine"], b["code"], os.path.join(d, "f.svg"), png=os.path.join(OUT, name + ".png"))
            print("ok", name)
        except Exception as ex:
            print("FAIL", name, str(ex)[:300])

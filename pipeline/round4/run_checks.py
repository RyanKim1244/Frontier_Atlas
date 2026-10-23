"""Run every `checks` snippet of lesson files in fresh `python3 -I -c` processes (parallel). Usage: run_checks.py file.json ..."""
import json, sys, subprocess, concurrent.futures as cf
def lessons(path):
    for x in json.load(open(path)):
        yield x["id"], (x["lesson"] if "lesson" in x else x)
def run(job):
    f, cid, i, code = job
    try:
        r = subprocess.run(["python3", "-I", "-c", code], capture_output=True, text=True, timeout=600)
        return (f, cid, i, r.returncode == 0, (r.stderr or "")[-300:])
    except subprocess.TimeoutExpired:
        return (f, cid, i, False, "timeout")
jobs = [(f, cid, i, c["python"]) for f in sys.argv[1:] for cid, L in lessons(f) for i, c in enumerate(L.get("checks", []))]
bad = []
with cf.ThreadPoolExecutor(16) as ex:
    for res in ex.map(run, jobs):
        if not res[3]: bad.append(res)
print(len(jobs), "checks,", len(bad), "failed")
for b in bad: print("FAIL", b[0].split("/")[-1], b[1], b[2], b[4])

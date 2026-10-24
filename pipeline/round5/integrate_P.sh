#!/bin/sh
# Publish reviewed round-5 pages: integrate_P.sh <batch-folder> id1 id2 ...
set -e
B=$1; shift; P=/home/claude/frontier_atlas/pipeline; S=/tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad
mkdir -p $P/round5/concepts $P/round5/reviews
for id in "$@"; do
  python3 -I $B/validate.py $B/final_s_$id.json | tail -1 | grep -qx OK
  python3 -I $P/round4/run_checks.py $B/final_s_$id.json
  python3 -I - "$B" "$id" "$P/round5/concepts/final_$id.json" <<'PY'
import json, sys
B, i, out = sys.argv[1:4]
x = json.load(open(f"{B}/final_s_{i}.json"))
import os
rv = json.load(open(f"{B}/review_r_{i}.json")) + (json.load(open(f"{B}/review_a_{i}.json")) if os.path.exists(f"{B}/review_a_{i}.json") else [])
x[0]["lesson"]["fixed"] = sum(1 for r in rv for k in r.get("issues", []) if k.get("severity") == "error")
json.dump(x, open(out, "w"), ensure_ascii=False, indent=0)
PY
  test -f $B/review_a_$id.json  # material added by the sufficiency check must be reviewed too
  cp $B/review_r_$id.json $B/review_a_$id.json $B/suff_s_$id.json $B/dossier_$id.json $P/round5/reviews/
done
cd /home/claude/frontier_atlas && python3 -I pipeline/atlas/build.py | tail -1
IDS=$(echo "$@" | tr ' ' ',')
(cd site && python3 -m http.server 8769 >/dev/null 2>&1 & echo $! > $S/srv.pid); sleep 1
mkdir -p $S/shots; cd $S/prev && timeout 400 node r5sweep.mjs "$IDS" 8769 $S/shots; kill $(cat $S/srv.pid)

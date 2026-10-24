#!/bin/sh
set -e
W=/tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad/round4/W; P=/home/claude/frontier_atlas/pipeline
python3 $P/round4/run_checks.py $W/final_$1.json
cp $W/final_$1.json $P/round4/concepts/final_$1.json; cp $W/review_$1.json $P/round4/concepts/review_$1.json
cd /home/claude/frontier_atlas && python3 -I pipeline/atlas/build.py | tail -1
IDS=$(python3 -c "import json;print(','.join(\"'\"+x['id']+\"'\" for x in json.load(open('$W/final_$1.json'))))")
cd /tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad/prev && sed "s/8767/8768/; s/const ids = \[.*\];/const ids = [$IDS];/" r4sweep.mjs > r4w.mjs && timeout 250 node r4w.mjs

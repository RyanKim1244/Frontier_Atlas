#!/bin/sh
# integrate_L.sh N : re-run checks of a reviewed lesson batch and copy it into the pipeline
set -e
L=/tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad/round4/L
P=/home/claude/frontier_atlas/pipeline
python3 $P/round4/run_checks.py $L/final_$1.json
cp $L/final_$1.json $P/lessons/final_r4_$1.json
cp $L/review_$1.json $P/lessons/review_r4_$1.json
[ -f $L/entry_fixes_$1.json ] && cp $L/entry_fixes_$1.json $P/round4/entry_fixes_$1.json
echo integrated $1

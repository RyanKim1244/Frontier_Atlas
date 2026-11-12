#!/bin/sh
# Usage: widemath.sh <pages.json> [more.json ...] -> formulas wider than a 390px phone column, per page (private preview build).
set -e
NM=${MATHJAX_NM:-/tmp/claude-0/-home-claude/e8759fbc-2379-5c50-9620-ea9c32ce3dd6/scratchpad/mj/node_modules}
FILES=""; for f in "$@"; do FILES="$FILES${FILES:+:}$(readlink -f "$f")"; done
OUT=$(mktemp -d); cd /home/claude/frontier_atlas && ATLAS_OUT=$OUT ATLAS_SCHOOL_EXTRA=$FILES python3 -I pipeline/atlas/build.py >/dev/null
IDS=$(python3 -I -c "import json,sys;print(','.join(x['id'] for f in sys.argv[1:] for x in json.load(open(f))))" "$@")
NODE_PATH=$(npm root -g) node pipeline/school/specs/widemath.mjs $OUT $IDS $NM; rm -rf $OUT

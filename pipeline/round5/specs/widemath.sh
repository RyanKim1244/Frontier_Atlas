#!/bin/sh
# Usage: widemath.sh <pages.json>  -> lists formulas wider than their column on a phone (390px), per page, with TeX and widths.
# Builds a private preview of the site with these pages (nothing is published).
set -e
F=$(readlink -f "$1"); S=/tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad
OUT=$(mktemp -d); PORT=$(python3 -c "import socket;s=socket.socket();s.bind(('',0));print(s.getsockname()[1])")
cd /home/claude/frontier_atlas && ATLAS_OUT=$OUT ATLAS_R5_EXTRA=$F python3 -I pipeline/atlas/build.py >/dev/null
IDS=$(python3 -I -c "import json,sys;print(','.join(x['id'] for x in json.load(open(sys.argv[1]))))" "$F")
(cd $OUT && exec python3 -m http.server $PORT >/dev/null 2>&1) & SRV=$!
sleep 1; cd $S/prev && timeout 600 node widemath.mjs $PORT $IDS; kill $SRV; rm -rf $OUT

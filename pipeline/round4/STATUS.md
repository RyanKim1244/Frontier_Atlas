# Round 4 status (2026-10-24)

Published:
- Lessons for all 188 original concepts (15 batches, each written, independently reviewed, checks re-run).
- Reviewed corrections to catalog entries (entry_fixes_*.json, applied by build.py).
- Bridge ladders: 7 batches, 207 reviewed steps (ladders/ladder_final_*.json).
- Lebl exercises: Basic Analysis I-II and Notes on Diffy Qs, attached by section (lebl_map.json); exercises whose topic page is still missing appear automatically once it exists.
- New topic concepts: batches 1-7 of 13 (concepts/final_*.json), 49 concepts.
- Areas are topics only (curriculum.py MOVE / RENAME_AREAS / DROP_AREAS).

Paused (usage): new-concept batches 8-13 (work/W/brief_8..13.json, 42 concepts: Fourier/PDE remainder, topology, differential geometry, functional analysis, probability, statistics, numerics, combinatorics, geometry, p-adics).
Pipeline: writer_prompt.md -> draft_N.json -> reviewer_prompt.md -> final_N.json -> integrate_W.sh N.
Not started: OpenIntro Statistics exercises (needs the statistics concepts of batch 11).

# Round 4 status (2026-10-24)

Published:
- Lessons for all 188 original concepts (15 batches, each written, independently reviewed, checks re-run).
- Reviewed corrections to catalog entries (entry_fixes_*.json, applied by build.py).
- Bridge ladders: 7 batches, 207 reviewed steps (ladders/ladder_final_*.json).
- Lebl exercises: Basic Analysis I-II and Notes on Diffy Qs, attached by section (lebl_map.json); exercises whose topic page is still missing appear automatically once it exists.
- New topic concepts: all 13 batches (91 concepts), each written, independently reviewed, checks re-run.
- Areas are topics only (curriculum.py MOVE / RENAME_AREAS / DROP_AREAS).

Next: OpenIntro Statistics exercises (statistics concepts now exist); ladders for more concepts; physics.
Pipeline: writer_prompt.md -> draft_N.json -> reviewer_prompt.md -> final_N.json -> integrate_W.sh N.
Not started: OpenIntro Statistics exercises (needs the statistics concepts of batch 11).

# Splitting a published page into one page per concept

Folder: /tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad/round5/P1
Read page_spec.md (schema, rules 1-11) first. The input page is reviewed and published; its content is correct. Your job is
structural: move blocks to the right page, and write only the bridging text a split needs. Do not rewrite correct material,
do not add new mathematics.

The reason: the page mixes several concepts (each with its own definitions, theorems and textbook chapter). The site wants one
concept per page, linked by prerequisites (brief.json gives the new ids, titles and prerequisites).

## For each resulting page (an object {"id","entry","lesson"} with lesson.v = 2)
- blocks: the blocks that belong to that concept, in a sensible teaching order (usually the existing order).
- intro: a new short intro (what question this concept answers; why a reader of papers needs it), following the sources.
- connection: a closing block linking prerequisites and follow-ups with [[id]] (ids from all_concepts.json; planned ids are
  fine, they show as "in preparation").
- Cross-references: wherever a moved block's text says "above", "the previous section", "the theorem on ...", and the target
  is now on another page, replace with a [[id|...]] link. Search for such phrases systematically.
- sources: exactly the sources cited (src keys) by the page's blocks, plus the dossier papers (kind "paper") that use this
  concept; keep the same keys. At least 3 papers if the dossier has them; report if not.
- requires: the original items whose "where" lands on this page, plus items about this concept; fix each "where" to a section
  title on this page or [[id]].
- checks: move each check to the page whose blocks state the claim it verifies. Every original check must end up on exactly
  one page or in the seeds file.
- entry: keep the original entry for the page that keeps the original id (adjust sum/key if its scope narrowed); write new
  entries for new pages (format in page_spec.md; msc only if sure; links to fields not among the page's own fields).
- exercises: an exercise block that mixes concepts is split between the pages.
- minutes: recompute honestly.

## Seeds
Material that belongs to a concept that is not part of this split (listed in your task) is removed from the page and saved,
unchanged, in seeds_<original-id>.json: [{"for": "<future concept title>", "blocks": [...], "sources": [...], "checks": [...],
"requires": [...]}]. Leave on the page at most one sentence pointing to it (no link if the concept has no id).

## Output
split_<original-id>.json (array of page objects) and seeds_<original-id>.json, plus changes_<original-id>.json:
[{"page": id, "new_or_changed_blocks": [indices], "notes": "..."}] listing every block whose text you wrote or edited, so a
reviewer can check exactly those. validate.py and run_checks.py must pass on the split file.
Reply briefly: pages and their block/word counts, seeds saved, checks distribution, anything awkward.

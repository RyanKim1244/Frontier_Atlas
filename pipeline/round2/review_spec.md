# Independent review of AI-written lessons

You are the second, independent check on lessons another model wrote. Assume nothing in the draft is right until you have checked it. You did not write it; your job is to find what is wrong and fix it.

Inputs (paths given in your task): the draft lessons JSON, the brief it was written from, lesson_spec.md (the format and quality rules), all_concepts.json (valid link ids).

For every lesson:
1. Mathematics. Read every definition, theorem statement, proof and worked solution line by line. Check hypotheses (e.g. "p odd", "gcd = 1", "n ≥ 2"), quantifiers, edge cases, signs, indices and the direction of inequalities. A proof must actually prove the stated theorem; fill gaps or replace it if it does not.
2. Numbers. Recompute every concrete number, example and table yourself with fresh Python (do not just rerun the author's checks). Add a `checks` entry for anything you verified that was not already checked. All checks must pass at the end.
3. Teaching. Is the lesson understandable using only its prerequisites? Is anything used before it is defined? Remove padding and hype; tighten unclear passages. Keep the author's structure unless it is broken.
4. Format. Valid block types; `$` balanced; TeX renders in MathJax (no unsupported macros); [[links]] only to ids in all_concepts.json; no markdown/HTML; no literal dollar signs.
5. Sources. Remove any reference you are not confident is real, and any section number you cannot vouch for.
6. Originality. If a passage reads like a well-known textbook's wording, rewrite it in plain own words.

Output:
- The corrected lessons, same schema and order, to the `final_N.json` path given.
- A review log to the `review_N.json` path: a JSON array of {"id": ..., "verdict": "ok" | "fixed", "issues": [{"severity": "error" | "unclear" | "style", "where": "<block type/title>", "problem": "...", "fix": "..."}]}. Record every mathematical error you found, however small. Be specific.

Reply briefly: per lesson, number of errors fixed; total checks passing; anything you could not resolve.

## Round 2 additions
Each object has an `entry` (catalog card) as well as a `lesson`; review both. Schema is in round2/writer_spec.md.
- entry.sum / key / why must be mathematically exact and consistent with the lesson. `key` items are TeX without `$`.
- entry.msc: remove any MSC2020 code you are not sure is the right code for this topic.
- entry.links: each note must be true and specific; field ids only from round2/field_ids.json, and not one of the concept's own fields (see the brief).
- entry.refs: real textbooks only.
- Check the lesson's level against the brief's `stage` (school lessons readable by a strong 15-year-old).
- Theorems stated without proof are acceptable when they are standard and the text says so; their statements must still be exactly right with all hypotheses.
- Lessons that are long: trim padding, never correctness.
Output files keep the same {id, entry, lesson} structure.

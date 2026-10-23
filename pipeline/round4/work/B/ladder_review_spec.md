# Independent review of bridge ladders

Another model wrote ladders of problems leading from olympiad/textbook level up to research problems (format: ladder_spec.md). You are the independent check. Assume nothing is right until you have checked it.

For every rung:
1. Statement. Is it mathematically exact (hypotheses, quantifiers, ranges, constants, exponents)? Is it TRUE as stated? A "Prove that" rung must be a proved result. If the published result is stronger or weaker than stated, fix the statement to match what is proved, or weaken it to something certainly true.
2. Citation. Look it up (WebSearch / WebFetch: arXiv, zbMATH, MathSciNet-style records, journal pages, the authors' pages, surveys). Confirm that the cited work exists, that the authors and year are right, and that it actually proves the rung. Fix venue/year errors. If you cannot confirm a citation, replace it with one you can confirm, or delete the rung. Classic rungs need a real textbook or survey where the fact appears; folklore with no confirmable source can stay only if the statement is elementary and you verify it yourself (computation or a short proof you check).
3. Small facts (exact values like S(3) = 13, W(3,2) = 9): recompute with Python where feasible.
4. Order. Rungs should go from most accessible to closest to the frontier. Reorder if needed.
5. `bridges_to`: each listed research problem must really be the natural next step from the rung. Remove links that are not.
6. Format: site text conventions (no markdown/HTML, balanced $, MathJax-compatible TeX), valid concept ids, no solutions or answer-revealing hints, own wording.

Output:
- `ladder_final_N.json`: the corrected ladders, same schema.
- `ladder_review_N.json`: [{"concept": ..., "rung": "<title>", "verdict": "ok|fixed|removed", "checked": "<what you looked up, with URL>", "problem": "...", "fix": "..."}] — one entry per rung.

Reply briefly: per concept, rungs kept/fixed/removed, and anything still uncertain.

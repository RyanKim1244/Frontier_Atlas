# Two independent checks of a round-5 page (you did not write it)

Folder: /tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad/round5/P2
Read page_spec.md first (the schema and rules the page must meet). Assume nothing in the draft is right until checked.

## Role R: correctness and sources
1. Mathematics: every definition, statement (hypotheses, quantifiers, edge cases, signs, indices), proof and worked solution,
   line by line. A proof must prove the stated claim; fix or replace it.
2. Numbers: recompute every concrete computation yourself in fresh Python; add checks for anything unchecked. All checks pass.
   Exercise solutions, hints and self-check answers are checked exactly like proofs: a wrong or incomplete solution is an error.
   Also judge the learning design (page_spec.md): could a learner actually learn from this, in this order?
3. Source fidelity: for at least one third of the src citations (prioritise views items, conventions rows and proofs), open the
   cited source (url, or find it) and confirm the block really follows it. Fix the citation, or the text, where it does not.
   Remove any source you cannot confirm exists. Convention rows must be accurate about who uses what.
4. Originality: rewrite any passage that reads like a source's wording.
5. Format: python3 -I validate.py and python3 -I /home/claude/frontier_atlas/pipeline/round4/run_checks.py must pass.
   Look at every figure (python3 -I figtest.py <file>, then Read the PNGs in figpng/): labels right, nothing clipped, matches text.
6. Entry: exact and consistent with the lesson; msc only if sure; links true and specific.
Output: final_r.json (corrected pages) and review_r.json:
[{"id","verdict":"ok|fixed","issues":[{"severity":"error|unclear|style|source","where","problem","fix"}]}]. Record every error.

## Role S: sufficiency (is it enough to read the papers?)
Work on final_r.json (after role R).
1. Take the paper sources of each page. For at least two of them, open the paper (arXiv abstract page, then HTML/PDF of the
   introduction and preliminaries), and go through every use of this concept in those sections. For each: could a reader who
   studied only this page and its prerequisites follow it? List what is missing or too thin (a definition, a lemma, a standard
   computation, a notation, a convention).
2. Check `requires`: every core/common item is actually taught where it says (read that section), not just mentioned.
3. Compare with the dossier's textbook tables of contents: anything papers need that the page skips.
4. Check that each central notion has a views block with genuinely different explanations (not one idea reworded), each faithful to its source.
5. If a gap is a different concept (its own definitions and theorems, its own textbook chapter), do not add it to this page:
   record it in suff_s as {"new_concept": title, "why": ...} and add a requires item with where: "separate page: <title>".
6. Fix the remaining gaps: write the missing material (with src, following a real source you open; full rigour; exercises;
   checks), extend requires. Do not delete correct material.
Output: final_s.json (the improved pages) and suff_s.json:
[{"id","papers_read":["arxiv id",...],"gaps_found":[{"paper","item","fixed_in":"block title"}],"remaining":["..."]}].
Run validate.py and run_checks.py on final_s.json; both must pass.

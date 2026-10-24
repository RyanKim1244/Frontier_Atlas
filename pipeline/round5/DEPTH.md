# Depth standard (replaces "one lesson per concept")

Problem: published lessons are about 14k characters each, the length of one textbook section. Example: `homology` has
simplicial and singular homology and spheres, but no exact sequences, relative homology, excision, Mayer–Vietoris or
cellular homology, which nearly every paper using homology assumes.

## Rules
1. **Few at a time.** Batches of at most 3 concepts. A batch is finished only when it passes every check below.
2. **Sufficiency is checked against real papers.** For each concept a separate agent picks 3–5 recent arXiv papers
   (different subfields) that use it and lists what they assume without explanation: definitions, theorems, notation,
   standard computations and tricks. Also the tables of contents of 2–3 standard textbooks (contents only, no text copied).
   The result is the concept's `requirements` list. Every item must be taught on the page or on a linked page.
3. **Several explanations of the same thing.** For each central definition and theorem, as fits:
   - intuition / picture (with a figure where it helps)
   - formal definition, plus equivalent definitions and why they agree
   - conventions that differ between books (sign, normalisation, notation), in a table
   - computation: how it is actually calculated, worked through
   - other viewpoints: geometric, algebraic, categorical, probabilistic, physical
   - motivation: what problem it was invented for
   - examples and counterexamples, from easy to hard
4. **Proofs.** Full proofs of the main theorems; a proof left out names where it is done.
5. **Exercises in every section,** graded, not one at the end.
6. **A concept may be several pages** (a short chapter) when one page cannot hold it.
7. **Checking.** Writer → independent reviewer (correctness) → separate sufficiency checker (re-reads the requirements
   list and one of the papers, marks what is still missing) → fixes → checks and render sweep re-run by me.
8. **Existing pages count too.** The 279 published pages are re-audited against the same standard.

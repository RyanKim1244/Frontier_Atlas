# Round 4 notes (lessons for existing concepts)

These concepts already have a catalog entry (summary, key statements, why it matters). You write the lesson only, in the format of lesson_spec.md. The brief gives each concept's entry; stay consistent with it. If the entry itself contains a mathematical error, write the lesson correctly and note the error in your reply.

- `stage` says where readers usually meet the concept: school (readable by a strong 15-year-old), olympiad, undergraduate, graduate, research. Pitch the lesson there and assume only the listed prerequisites.
- Graduate topics (analytic number theory, sieves, L-functions): give the idea and the main statements precisely; prove what can be proved in a page (e.g. Chebyshev bounds, Mertens' theorems, the large sieve inequality in a simple form) and say clearly when a proof is omitted. Worked examples can be computations (e.g. comparing pi(x) with li(x) numerically) as well as derivations.
- Research-frontier concepts (status open or claimed): explain the problem, the best classical results with dates and names you are sure of, why it is hard, and what a proof would imply. For anything from 2026 (see the brief's `timeline`), use only what the brief says, attribute it, and call claims claims. Do not invent results, dates, names or numbers. If you are unsure whether a result exists, leave it out.
- Olympiad-stage concepts (inequalities, functional equations, combinatorics techniques): the examples should be olympiad-style problems of your own construction or classic folklore exercises; do not work out IMO, USAMO or Putnam problems.
- `checks`: Python with the standard library, sympy, numpy or mpmath (all installed). Verify every number, identity and small case you state; for asymptotic statements check numerically at a few values where meaningful (e.g. sum of 1/p up to 10^6 vs log log x + M).
- [[links]] only to ids in all_concepts.json in this folder.
- Exercises: 2–4, no solutions.

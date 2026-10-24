# Round 5 status (2026-10-24 evening)

Published (depth standard, reviewed): localization, local-rings, homological-algebra, derived-functors, tor, ext,
de-rham-cohomology, poincare-duality. Exercises from Stacks/Napkin: round5/exercises/. Problem attach: round5/attach/.

In progress (work saved in round5/work/P2/, specs in round5/specs/; scratch copies used by the tools live in the session scratchpad):
- cohomology (singular cohomology and the cup product): draft_cohomology.json done and validated; correctness review (Role R)
  was stopped before finishing -> rerun Role R, then Role S, then review of S additions, then publish (integrate_P.sh).
- depth-cohen-macaulay: draft done (too long, ~220 min); Role R stopped. Rerun Role R with the rule-11 instruction (separate by classification, not length): move
  Gorenstein/canonical modules, local cohomology, Stanley-Reisner, matrix factorizations to seeds.
- dedekind-domains: dossier done; writer stopped mid-way (check for outline_/draft_ files in work/P2); rerun the writer.

Pipeline per concept: dossier -> outline -> writer (page_spec.md, learning design) -> Role R -> Role S -> review of S additions
-> validate.py + run_checks.py + widemath.sh + render sweep -> publish. Exercises: exercise_spec.md. One concept per page.
New concepts proposed by the drafts: manifold-duality (added to curriculum), krull-dimension, associated-primes,
regular-local-rings, local-cohomology, gorenstein-rings, stanley-reisner-rings, matrix-factorizations, cohomology operations,
characteristic classes, equivariant cohomology, algebraic de Rham cohomology (seeds in round5/seeds/).
Open items: 145 concepts have no exercises yet; old 279 pages are thin by the new standard; MSE/MathOverflow not reachable
(add to allowed domains); Supabase migrations nested_replies and post_titles must be run by the owner.

## Standing plan (agreed 2026-10-24)
Goal: all of mathematics. Every batch of 3 mixes new concepts and upgrades of existing (v1) pages to the depth standard.
- Upgrade queue (most depended-on first, by number of concepts that build on them): functions, euclid-basics, limits,
  real-numbers, seq-limits, divisibility, derivative, trig, exp-log, riemann-integral, continuity, diff-rules, fta, mvt,
  series, vectors-plane, ftc, congruences, linear-systems, matrices, ...
- New-concept queue: finish cohomology, depth-cohen-macaulay, dedekind-domains; then the concepts current pages point to
  (krull-dimension, associated-primes, manifold-duality, spectral-sequences, sheaf-cohomology, ...), plus missing
  foundations found in the taxonomy (research/taxonomy.json, tier 1 first).
- An upgrade uses the same pipeline (dossier -> outline -> write -> R -> S -> review of S -> exercises -> publish), keeping
  correct existing material and its checks; foundations are written for a first-time learner (school/undergraduate stage).

# Round 5 status (2026-10-24 evening)

Published (depth standard, reviewed): localization, local-rings, homological-algebra, derived-functors, tor, ext,
de-rham-cohomology, poincare-duality. Exercises from Stacks/Napkin: round5/exercises/. Problem attach: round5/attach/.

In progress (work saved in round5/work/P2/, specs in round5/specs/; scratch copies used by the tools live in the session scratchpad):
- cohomology (singular cohomology and the cup product): draft_cohomology.json done and validated; correctness review (Role R)
  was stopped before finishing -> rerun Role R, then Role S, then review of S additions, then publish (integrate_P.sh).
- depth-cohen-macaulay: draft done (too long, ~220 min); Role R stopped. Rerun Role R with the rule-11 instruction: move
  Gorenstein/canonical modules, local cohomology, Stanley-Reisner, matrix factorizations to seeds.
- dedekind-domains: dossier done; writer stopped mid-way (check for outline_/draft_ files in work/P2); rerun the writer.

Pipeline per concept: dossier -> outline -> writer (page_spec.md, learning design) -> Role R -> Role S -> review of S additions
-> validate.py + run_checks.py + widemath.sh + render sweep -> publish. Exercises: exercise_spec.md. One concept per page.
New concepts proposed by the drafts: manifold-duality (added to curriculum), krull-dimension, associated-primes,
regular-local-rings, local-cohomology, gorenstein-rings, stanley-reisner-rings, matrix-factorizations, cohomology operations,
characteristic classes, equivariant cohomology, algebraic de Rham cohomology (seeds in round5/seeds/).
Open items: 145 concepts have no exercises yet; old 279 pages are thin by the new standard; MSE/MathOverflow not reachable
(add to allowed domains); Supabase migrations nested_replies and post_titles must be run by the owner.

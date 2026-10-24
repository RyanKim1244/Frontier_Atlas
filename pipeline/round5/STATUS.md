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

## School mathematics from the first year (agreed 2026-10-24)
Coverage must start at elementary school: every concept in school textbooks gets its own page (grouped by topic, never by
grade), so a learner can climb step by step from counting to research.
Next research task (before writing): build the full school concept list from curricula and open textbooks, compare it with
the existing concepts, and add the missing ones to the curriculum with prerequisites.
- Topic lists (reference only, no text copied): Korean national curriculum achievement standards (2022 revision),
  US Common Core, England national curriculum.
- Open textbooks usable for structure and for exercises (licence to be confirmed per source): Illustrative Mathematics K-12
  (CC BY 4.0), OpenStax Prealgebra / Elementary Algebra / Intermediate Algebra / College Algebra / Precalculus / Calculus
  (CC BY 4.0), CK-12 (check licence; often NC -> excluded).

## Olympiad mathematics (agreed 2026-10-24)
Olympiad concepts are thin too. Next session starts from the beginning: school mathematics + olympiad topics, researched together.
- Build an olympiad topic list (algebra, combinatorics, geometry, number theory: techniques and standard results, e.g.
  invariants and monovariants, extremal principle, orders and primitive roots, lifting the exponent, Vieta jumping,
  inversion, projective geometry, complex and barycentric coordinates, inequalities beyond AM-GM, functional equations by type).
- Use the olympiad problems left unattached in round5/attach/ (no tag was central) as evidence of missing concepts.
- Licensed sources only for text and exercises; topic lists from handouts are reference only.

## Keeping up with the frontier (agreed 2026-10-24)
Alongside filling concepts, follow recent mathematics: new results, claimed solutions, AI-assisted proofs and formalisations.
Each check: update the timeline events and research-problem statuses (erdosproblems.com, formal-conjectures, Clay), link each
item to its concepts, and move concepts needed to understand new results up the writing queue. Sources: arXiv math listings,
erdosproblems.com, Quanta, mathematicians' blogs (e.g. Tao), formalisation projects (Lean/mathlib). Facts verified at the source.

## Target: February 2027 (owner starts university then); a soft target, quality first, delay is acceptable
About 17 weeks. Expected size: roughly 1,500-2,500 concepts (school + olympiad + undergraduate + graduate core + tiers 1-3).
Throughput needed: on the order of 100+ concepts per week; the pilot pipeline cost ~1M tokens per concept, far too slow.
Next session must first redesign for throughput without dropping the checks that caught real errors:
- research per topic cluster (one dossier set for 10-20 related concepts), not per concept;
- cheaper models for classification, exercise sourcing, formula-width fixes; strongest model for writing and correctness review;
- many batches in parallel; school-level concepts are smaller and faster;
- a written definition of "complete" per tier (what every page must have) agreed with the owner.

## Olympiad problems: added by the owner (2026-10-25)
The owner adds olympiad past problems himself (pipeline/src/olympiad_user/*.json, format in its README). Claude does not
collect olympiad problems; for newly added ones Claude only tags concepts and decides attachment (easy positions only:
IMO/USAMO P1, P4; Putnam A1, A2, B1, B2; other contests by judged difficulty), and checks the statements render.

## Link-only practice (2026-10-25)
Problems we cannot reproduce (university past exams, qualifying exams, NC/ND textbook exercises) are linked on the concept
page under "More practice elsewhere" (round5/practice_links/, format in its README), clearly marked as external. Collected
together with licensed exercises (specs/exercise_spec.md, "Link-only practice").

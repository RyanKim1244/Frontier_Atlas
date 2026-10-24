# Roadmap: all of mathematics (research done 2026-10-24, nothing written yet)

Goal: enough foundation to read a paper in any arXiv math category.
Method: the 32 arXiv math categories mapped to MSC2020 sub-areas; each sub-area marked as covered by an existing page or needing new ones.
Data: `research/taxonomy.json` (merged; built by `research/merge.py`), `research/sources.json`, `research/coverage.json`.

## Size
| | pages |
|---|---|
| Published now | 279 |
| Round 5 (planned, `curriculum.py`) | 42 |
| New from the taxonomy: tier 1 (needed for most papers in a field) | 171 |
| tier 2 (needed for a large share) | 252 |
| tier 3 (frontier specialities) | 122 |
| **Total when done** | **866** |

Checks on the merged list: no id clashes with existing pages, every prerequisite exists, no cycles, 31 duplicates between parts A and B merged
(lower tier kept), 5 tiers raised so no topic sits below a prerequisite.

## Order
1. Round 5 (42 graduate-core pages): the base everything else rests on.
2. Tier 1 (171), in dependency order.
3. Tier 2 (252).
4. Tier 3 (122).
Within each tier: by dependency, not by field. Cost from round 4: about 60k tokens per page (writer + reviewer),
so round 5 about 2.5M, tier 1 about 10M, tier 2 about 15M, tier 3 about 7M.

## Structure changes
- Rename the planned functional-analysis `distributions` to `schwartz-distributions` (clashes with the published probability page).
- New areas (14): category, homotopy, geomtop, grouptheory, commalg, specfun, history, mathphys, optimization, information,
  quantum-algebra, ktheory, symplectic, convex-metric. Plus alggeo from round 5.
- Splits (10): geometric-group-theory (5 pages), galois-cohomology, ergodic-theory, elliptic-pde, homological-algebra,
  model-theory, operator-algebras, forcing, automorphic-forms, symplectic-geometry. See `taxonomy.json` → `splits`.

## Exercise sources by field (commercial use allowed; details and licence texts in `research/sources.json`)
- Algebra, groups, rings, fields: Judson AATA (GFDL); Napkin (CC BY-SA 4.0, text only)
- Linear algebra: Hefferon, Beezer FCLA (GFDL), Kuttler/Lyryx (CC BY 4.0)
- Algebraic geometry, commutative algebra: Stacks Project (GFDL) exercises
- Complex analysis: Lebl (CC BY-SA)
- ODE / PDE: Judson ODE Project (GFDL), Ivrii PDE (CC BY-SA 4.0)
- Probability and statistics: Grinstead–Snell (GFDL), Siegrist Random (CC BY 2.0), OpenIntro (CC BY-SA 3.0; must not use the OpenIntro name)
- Combinatorics: Bogart (GFDL)
- Logic: Open Logic Project, forall x Calgary (CC BY 4.0)
- Category theory: HoTT book (CC BY-SA 3.0), Milewski (CC BY-SA 4.0)
- Research problems: Open Problem Garden (GFDL), MathOverflow/Math SE (CC BY-SA), arXiv papers under CC BY / BY-SA / CC0 only
- Gaps with no usable open exercise source: functional analysis, harmonic analysis, optimisation, mathematical physics,
  algebraic topology, differential geometry, graduate number theory. Here exercises are written by us (as for lessons), reviewed the same way.
GFDL material is kept in separate files from CC BY-SA material, with the licence text attached.

## Figures
See `FIGURES.md`: Asymptote for geometry, TikZ / tikz-cd for diagrams, matplotlib for graphs; all built to SVG at build time.

## Open doubts
- MSC codes for classes 20 and above are partly from memory (the official sites were blocked); verify before publishing.
- DG, DS, FA, GR, ST, OC, IT topics rest more on arXiv descriptions than on opened textbook contents.
- Tiers are judgement, not measured.

# Round 5 plan (not started)

Goal: complete mathematics first (physics comes after). Round 5 fills the graduate core; later rounds go deeper until the atlas reaches roughly 600-800 concepts.
Topic list with prerequisites: curriculum.py (42 concepts, ordered by dependency).

## Also needed (depth, not new topics)
- Split broad pages into sub-pages: homology (simplicial / singular / cellular, exact sequences, Mayer–Vietoris),
  Lebesgue (measure, integration theorems, product measures), Galois theory (correspondence, solvability, examples),
  spectral theorem (finite-dim / compact / unbounded), Fourier analysis (series, transform, Poisson, uncertainty).
- Exercises for the new advanced concepts: open-licensed sources still to check — OpenIntro Statistics (CC BY-SA 3.0,
  already cloned), Hefferon Linear Algebra (CC BY-SA, GitLab), Judson AATA and Beezer FCLA (GFDL; decide on licence).
- Bridge ladders for more research-heavy concepts (same spec as round 4).

## Cost estimate (from round 4)
About 6 batches of 7 concepts: one writer and one reviewer per batch, roughly 0.2M tokens each, so about 2.5M tokens.
Run in dependency order: algebra (localisation, homological algebra, categories) -> topology (covering spaces, cohomology, homotopy) -> differential geometry -> analysis (distributions, Sobolev, operators) -> algebraic geometry -> number theory -> advanced.

## After round 5 (to reach 'all of mathematics')
Per subject, the remaining layers seen in the TOC surveys (round4/work/gaps_advanced.json 'deferred_not_proposed'):
- Analysis: Riesz representation, interpolation of operators, singular integrals, Littlewood–Paley, Hardy spaces, wavelets.
- Geometry/topology: knot theory, 3-manifolds, Lie groups' structure (maximal tori, Weyl group), complex manifolds, Kähler geometry.
- Algebra: noncommutative rings, Artin–Wedderburn, quivers, algebraic groups, homotopical algebra.
- Number theory: elliptic curves in depth (heights, Selmer groups), Iwasawa theory, transcendence theory, analytic L-functions of degree > 1.
- Probability/statistics: large deviations, random matrices, concentration, Bayesian inference, time series.
- Logic/computation: computability degrees, proof theory, type theory, complexity classes beyond P/NP.
- Combinatorics: matroids, design theory, coding theory, extremal set theory in depth.
- Applied: numerical PDE, optimisation (nonconvex, stochastic), information theory, control.

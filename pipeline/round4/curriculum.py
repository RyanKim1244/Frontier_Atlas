# Round 4 curriculum: topics missing from the atlas, found by comparing against textbook and curriculum tables of contents
# (Korean 2022 curriculum, Common Core / AP / A level / IB, and standard undergraduate and graduate texts; see round4/toc_*.json).
# One page per topic, whatever the level: a lesson starts where a newcomer starts and continues as far as the topic goes.
# (id, title, short, area, fields, stage, prerequisites)
C = [
 # logic and foundations
 ("sets-relations", "Sets, relations and orderings", "Sets & relations", "logic", ["logic", "combinatorics"], "school", []),
 ("logic-basics", "Propositional and predicate logic", "Logic", "logic", ["logic", "computer-science"], "school", []),
 ("proof-methods", "Methods of proof", "Proof methods", "logic", ["logic"], "school", ["logic-basics", "sets-relations"]),
 ("induction", "Mathematical induction and recursion", "Induction", "logic", ["logic", "combinatorics"], "school", ["proof-methods"]),
 ("ordinals-cardinals", "Countability, cardinals and ordinals", "Cardinals & ordinals", "logic", ["logic", "combinatorics"], "undergraduate", ["sets-relations", "functions", "induction"]),
 ("completeness-theorem", "Gödel's completeness and compactness theorems", "Completeness theorem", "logic", ["logic"], "undergraduate", ["logic-basics", "induction"]),
 ("incompleteness", "Gödel's incompleteness theorems", "Incompleteness", "logic", ["logic", "computer-science"], "undergraduate", ["completeness-theorem", "computability"]),
 # computation
 ("algorithms", "Algorithms and their complexity", "Algorithms", "computation", ["computer-science"], "undergraduate", ["induction", "asymptotics"]),
 ("automata", "Finite automata and regular languages", "Automata", "computation", ["computer-science", "logic"], "undergraduate", ["sets-relations", "induction"]),
 ("computability", "Turing machines and computability", "Computability", "computation", ["computer-science", "logic"], "undergraduate", ["automata"]),
 # functions and equations
 ("quadratics", "Quadratic equations and quadratic functions", "Quadratics", "functions", ["algebra"], "school", ["functions"]),
 ("solving-inequalities", "Solving inequalities", "Solving inequalities", "functions", ["algebra"], "school", ["quadratics"]),
 ("rational-functions", "Rational functions and partial fractions", "Rational functions", "functions", ["algebra", "calculus"], "school", ["polynomials-roots", "functions"]),
 ("hyperbolic-functions", "Hyperbolic functions", "Hyperbolic functions", "functions", ["calculus", "special-functions"], "school", ["exp-log", "diff-rules"]),
 # calculus
 ("integral-applications", "Applications of the integral: area, volume, length and work", "Applications of integrals", "calculus", ["calculus", "physics"], "school", ["ftc"]),
 ("parametric-polar", "Parametric curves and polar coordinates", "Parametric & polar curves", "calculus", ["calculus", "geometry"], "school", ["trig", "derivative"]),
 # differential equations
 ("ode-systems", "Systems of linear differential equations", "Linear systems of ODEs", "odes", ["differential-equations", "linear-algebra"], "undergraduate", ["ode-linear", "eigen"]),
 ("laplace-transform", "The Laplace transform", "Laplace transform", "odes", ["differential-equations", "harmonic-analysis"], "undergraduate", ["ode-linear", "improper-integrals"]),
 ("series-solutions-ode", "Power-series solutions and the method of Frobenius", "Series solutions", "odes", ["differential-equations", "special-functions"], "undergraduate", ["ode-linear", "power-series"]),
 ("sturm-liouville", "Boundary value problems and Sturm–Liouville theory", "Sturm–Liouville", "odes", ["differential-equations", "pde", "linear-algebra"], "undergraduate", ["ode-linear", "inner-products", "fourier-series"]),
 # dynamical systems
 ("phase-plane", "The phase plane, equilibria and stability", "Phase plane & stability", "dynamics", ["dynamics", "differential-equations"], "undergraduate", ["ode-systems", "partial-derivatives"]),
 ("bifurcations", "Bifurcations", "Bifurcations", "dynamics", ["dynamics", "differential-equations"], "undergraduate", ["phase-plane"]),
 ("limit-cycles", "Limit cycles and the Poincaré–Bendixson theorem", "Limit cycles", "dynamics", ["dynamics", "differential-equations"], "undergraduate", ["phase-plane"]),
 ("chaos", "Chaos and strange attractors", "Chaos", "dynamics", ["dynamics", "physics"], "undergraduate", ["limit-cycles", "bifurcations"]),
 # Fourier analysis
 ("fourier-series", "Fourier series", "Fourier series", "harmonic", ["harmonic-analysis", "calculus"], "undergraduate", ["riemann-integral", "trig", "series"]),
 ("fourier-transform", "The Fourier transform", "Fourier transform", "harmonic", ["harmonic-analysis", "pde", "physics"], "undergraduate", ["fourier-series", "improper-integrals"]),
 # partial differential equations
 ("heat-equation", "The heat equation", "Heat equation", "pde", ["pde", "physics", "probability"], "undergraduate", ["partial-derivatives", "fourier-series"]),
 ("wave-equation", "The wave equation", "Wave equation", "pde", ["pde", "physics"], "undergraduate", ["partial-derivatives", "fourier-series"]),
 ("laplace-equation", "Laplace's equation and harmonic functions", "Laplace's equation", "pde", ["pde", "physics", "complex-analysis"], "undergraduate", ["partial-derivatives", "vector-calculus", "fourier-series"]),
 ("calculus-of-variations", "The calculus of variations", "Calculus of variations", "pde", ["pde", "physics", "real-analysis"], "undergraduate", ["partial-derivatives", "lagrange-multipliers", "integration-techniques"]),
 # real analysis
 ("inverse-function-theorem", "The inverse and implicit function theorems", "Inverse function theorem", "realanalysis", ["real-analysis", "calculus"], "undergraduate", ["partial-derivatives", "linear-maps", "contraction-mapping"]),
 ("contraction-mapping", "The contraction mapping principle and Picard's theorem", "Contraction mapping", "realanalysis", ["real-analysis", "differential-equations"], "undergraduate", ["metric-spaces", "ode-first"]),
 ("arzela-ascoli", "The Arzelà–Ascoli and Stone–Weierstrass theorems", "Arzelà–Ascoli & Stone–Weierstrass", "realanalysis", ["real-analysis", "topology"], "undergraduate", ["uniform-convergence", "compactness"]),
 ("lp-spaces", "L^p spaces", "L^p spaces", "realanalysis", ["real-analysis", "functional-analysis"], "graduate", ["lebesgue", "normed-spaces"]),
 # complex analysis
 ("entire-functions", "Entire functions and infinite products", "Entire functions", "complex", ["complex-analysis"], "undergraduate", ["holomorphic", "residues"]),
 ("conformal-maps", "Conformal maps and the Riemann mapping theorem", "Conformal maps", "complex", ["complex-analysis", "geometry"], "undergraduate", ["holomorphic", "arzela-ascoli"]),
 # linear algebra
 ("dual-spaces", "Dual spaces and quotient spaces", "Duality", "linalg", ["linear-algebra"], "undergraduate", ["linear-maps"]),
 ("tensor-products", "Tensor products and exterior algebra", "Tensors & exterior algebra", "linalg", ["linear-algebra", "algebra", "physics"], "undergraduate", ["dual-spaces", "determinants"]),
 ("least-squares", "Orthogonal projection, least squares and QR", "Least squares", "linalg", ["linear-algebra", "statistics", "numerical-analysis"], "undergraduate", ["inner-products", "linear-maps"]),
 # abstract algebra
 ("solvable-groups", "Solvable and nilpotent groups", "Solvable groups", "abstract", ["algebra"], "undergraduate", ["group-homomorphisms", "group-actions"]),
 ("ufds", "Euclidean domains, PIDs and unique factorisation", "Unique factorisation domains", "abstract", ["algebra", "number-theory"], "undergraduate", ["rings", "fta"]),
 ("modules", "Modules and the structure theorem over a PID", "Modules", "abstract", ["algebra", "linear-algebra"], "undergraduate", ["ufds", "linear-maps"]),
 ("noetherian-rings", "Noetherian rings and Hilbert's basis theorem", "Noetherian rings", "abstract", ["algebra", "algebraic-geometry"], "undergraduate", ["rings", "modules"]),
 ("categories-functors", "Categories, functors and natural transformations", "Categories", "abstract", ["category-theory", "algebra"], "graduate", ["groups", "vector-spaces", "topological-spaces"]),
 # representation theory and Lie theory
 ("group-representations", "Representations of finite groups", "Group representations", "lie", ["representation-theory", "algebra", "physics"], "undergraduate", ["group-actions", "inner-products"]),
 ("character-theory", "Characters of finite groups", "Character theory", "lie", ["representation-theory", "algebra"], "undergraduate", ["group-representations"]),
 ("lie-groups", "Lie groups and matrix groups", "Lie groups", "lie", ["representation-theory", "differential-geometry", "physics"], "graduate", ["groups", "smooth-manifolds"]),
 ("lie-algebras", "Lie algebras and the exponential map", "Lie algebras", "lie", ["representation-theory", "algebra", "physics"], "graduate", ["lie-groups"]),
 # topology
 ("topological-spaces", "Topological spaces, continuity and connectedness", "Topological spaces", "topology", ["topology"], "undergraduate", ["metric-spaces"]),
 ("fundamental-group", "The fundamental group and covering spaces", "Fundamental group", "topology", ["topology", "algebra"], "undergraduate", ["topological-spaces", "groups"]),
 ("classification-of-surfaces", "The classification of surfaces", "Classification of surfaces", "topology", ["topology", "geometry"], "undergraduate", ["topological-spaces", "planar-graphs"]),
 ("homology", "Homology", "Homology", "topology", ["topology", "algebra"], "graduate", ["fundamental-group", "group-homomorphisms"]),
 # differential geometry
 ("curves", "Curves: arc length, curvature and the Frenet frame", "Curves & curvature", "diffgeo", ["differential-geometry", "geometry", "calculus"], "undergraduate", ["parametric-polar", "vectors-plane", "derivative"]),
 ("surfaces-curvature", "Surfaces and Gaussian curvature", "Surfaces & curvature", "diffgeo", ["differential-geometry", "geometry"], "undergraduate", ["curves", "partial-derivatives"]),
 ("gauss-bonnet", "Geodesics and the Gauss–Bonnet theorem", "Gauss–Bonnet", "diffgeo", ["differential-geometry", "topology"], "undergraduate", ["surfaces-curvature", "classification-of-surfaces"]),
 ("smooth-manifolds", "Smooth manifolds and tangent spaces", "Smooth manifolds", "diffgeo", ["differential-geometry", "topology"], "graduate", ["topological-spaces", "inverse-function-theorem"]),
 ("differential-forms", "Differential forms and the general Stokes theorem", "Differential forms", "diffgeo", ["differential-geometry", "calculus", "physics"], "undergraduate", ["tensor-products", "vector-calculus"]),
 ("riemannian-geometry", "Riemannian metrics, geodesics and curvature", "Riemannian geometry", "diffgeo", ["differential-geometry", "physics"], "graduate", ["smooth-manifolds", "tensor-products", "surfaces-curvature"]),
 # functional analysis
 ("normed-spaces", "Normed and Banach spaces", "Banach spaces", "functional", ["functional-analysis", "real-analysis", "linear-algebra"], "undergraduate", ["metric-spaces", "vector-spaces"]),
 ("hilbert-spaces", "Hilbert spaces", "Hilbert spaces", "functional", ["functional-analysis", "linear-algebra", "physics"], "undergraduate", ["normed-spaces", "inner-products"]),
 ("hahn-banach", "The Hahn–Banach theorem and dual spaces", "Hahn–Banach", "functional", ["functional-analysis"], "graduate", ["normed-spaces", "dual-spaces"]),
 ("compact-operators", "Compact operators and the Fredholm alternative", "Compact operators", "functional", ["functional-analysis", "pde"], "graduate", ["hilbert-spaces", "spectral-theorem", "arzela-ascoli"]),
 # probability
 ("joint-distributions", "Joint distributions, covariance and conditional expectation", "Joint distributions", "probability", ["probability"], "undergraduate", ["random-variables", "distributions", "multiple-integrals"]),
 ("moment-generating", "Probability and moment generating functions", "Generating functions in probability", "probability", ["probability"], "undergraduate", ["random-variables", "generating-functions", "power-series"]),
 ("monte-carlo", "Simulation and Monte Carlo methods", "Monte Carlo", "probability", ["probability", "computer-science"], "undergraduate", ["random-variables", "limit-theorems"]),
 ("entropy", "Entropy and information", "Entropy", "probability", ["probability", "computer-science", "physics"], "undergraduate", ["random-variables", "exp-log", "convexity"]),
 ("martingales", "Conditional expectation and martingales", "Martingales", "probability", ["probability"], "graduate", ["joint-distributions", "limit-theorems"]),
 ("brownian-motion", "Random walks and Brownian motion", "Brownian motion", "probability", ["probability", "physics", "pde"], "graduate", ["limit-theorems", "martingales"]),
 # statistics
 ("descriptive-statistics", "Describing data: summaries and displays", "Describing data", "statistics", ["statistics"], "school", []),
 ("sampling-design", "Sampling, surveys and experiments", "Sampling & experiments", "statistics", ["statistics"], "school", ["descriptive-statistics", "probability-basics"]),
 ("point-estimation", "Estimators and maximum likelihood", "Estimation", "statistics", ["statistics", "probability"], "undergraduate", ["distributions", "limit-theorems"]),
 ("confidence-intervals", "Sampling distributions and confidence intervals", "Confidence intervals", "statistics", ["statistics", "probability"], "school", ["limit-theorems", "sampling-design"]),
 ("hypothesis-testing", "Hypothesis testing", "Hypothesis testing", "statistics", ["statistics", "probability"], "school", ["confidence-intervals"]),
 ("t-tests", "Inference for means: t-tests and analysis of variance", "t-tests & ANOVA", "statistics", ["statistics"], "undergraduate", ["hypothesis-testing"]),
 ("chi-square-tests", "Chi-square tests", "Chi-square tests", "statistics", ["statistics"], "undergraduate", ["hypothesis-testing", "distributions"]),
 ("linear-regression", "Correlation and linear regression", "Regression", "statistics", ["statistics", "linear-algebra"], "school", ["descriptive-statistics", "least-squares"]),
 # numerical analysis and optimisation
 ("root-finding", "Numerical solution of equations: bisection and Newton's method", "Root-finding", "numerics", ["numerical-analysis", "calculus"], "school", ["continuity", "derivative"]),
 ("interpolation-quadrature", "Interpolation and numerical integration", "Interpolation & quadrature", "numerics", ["numerical-analysis", "real-analysis"], "undergraduate", ["taylor", "riemann-integral"]),
 ("numerical-odes", "Numerical methods for differential equations", "Numerical ODEs", "numerics", ["numerical-analysis", "differential-equations"], "undergraduate", ["ode-first", "taylor"]),
 ("linear-programming", "Linear programming and duality", "Linear programming", "numerics", ["optimisation", "linear-algebra", "computer-science"], "school", ["linear-systems", "solving-inequalities"]),
 ("convex-optimisation", "Convex optimisation", "Convex optimisation", "numerics", ["optimisation", "real-analysis"], "undergraduate", ["convexity", "lagrange-multipliers", "inner-products"]),
 ("gradient-descent", "Gradient descent and stochastic optimisation", "Gradient descent", "numerics", ["optimisation", "ai-research", "calculus"], "undergraduate", ["partial-derivatives", "convexity"]),
 # combinatorics and graph theory
 ("partitions", "Partitions of integers and sets", "Partitions", "discrete", ["combinatorics", "number-theory"], "olympiad", ["counting", "generating-functions"]),
 ("planar-graphs", "Planar graphs and Euler's formula", "Planar graphs", "discrete", ["combinatorics", "topology"], "school", ["graph-basics"]),
 ("graph-algorithms", "Shortest paths, spanning trees and graph search", "Graph algorithms", "discrete", ["combinatorics", "computer-science"], "undergraduate", ["graph-basics", "algorithms"]),
 ("network-flows", "Network flows and the max-flow min-cut theorem", "Network flows", "discrete", ["combinatorics", "computer-science", "optimisation"], "undergraduate", ["graph-algorithms", "cycles-matchings"]),
 # geometry
 ("conic-sections", "Conic sections", "Conics", "geometry", ["geometry", "algebra"], "school", ["analytic-geometry", "quadratics"]),
 ("area-volume", "Length, area and volume", "Area & volume", "geometry", ["geometry", "calculus"], "school", ["euclid-basics", "circles"]),
 ("solid-geometry", "Lines, planes and solids in space", "Solid geometry", "geometry", ["geometry", "linear-algebra"], "school", ["euclid-basics", "vectors-plane"]),
 ("constructions", "Straightedge-and-compass constructions", "Constructions", "geometry", ["geometry", "algebra"], "school", ["euclid-basics", "circles", "fields-ext"]),
 # number theory
 ("p-adic-numbers", "The p-adic numbers", "p-adic numbers", "algebraic", ["number-theory", "algebra"], "undergraduate", ["p-adic-valuation", "hensel", "metric-spaces"]),
]

# New areas (topic groupings). Existing areas keep their ids; "precalc" is renamed to Functions and "analysis"/"frontier" are dissolved below.
AREAS = [
 {"id": "logic", "name": "Logic and foundations", "blurb": "Sets, logic, proof and induction, up to Gödel's theorems.", "fields": ["logic"]},
 {"id": "complex", "name": "Complex analysis", "blurb": "Holomorphic functions, contour integrals, continuation and conformal maps.", "fields": ["complex-analysis"]},
 {"id": "harmonic", "name": "Fourier analysis", "blurb": "Fourier series, the Fourier transform and Poisson summation.", "fields": ["harmonic-analysis"]},
 {"id": "odes", "name": "Differential equations", "blurb": "Ordinary differential equations: first order, linear, systems, transforms and boundary value problems.", "fields": ["differential-equations"]},
 {"id": "dynamics", "name": "Dynamical systems", "blurb": "Phase portraits, stability, bifurcations, limit cycles and chaos.", "fields": ["dynamics"]},
 {"id": "pde", "name": "Partial differential equations", "blurb": "The heat, wave and Laplace equations, variational problems and fluid flow.", "fields": ["pde"]},
 {"id": "functional", "name": "Functional analysis", "blurb": "Banach and Hilbert spaces and the operators on them.", "fields": ["functional-analysis"]},
 {"id": "topology", "name": "Topology", "blurb": "Spaces up to continuous deformation: connectedness, the fundamental group, surfaces and homology.", "fields": ["topology"]},
 {"id": "diffgeo", "name": "Differential geometry", "blurb": "Curves, surfaces, manifolds and curvature.", "fields": ["differential-geometry"]},
 {"id": "lie", "name": "Representations and Lie theory", "blurb": "Groups acting linearly: representations, characters, Lie groups and Lie algebras.", "fields": ["representation-theory"]},
 {"id": "statistics", "name": "Statistics", "blurb": "Describing data, designing studies, estimation, testing and regression.", "fields": ["statistics"]},
 {"id": "numerics", "name": "Numerical analysis and optimisation", "blurb": "Computing answers: root-finding, quadrature, numerical ODEs and optimisation.", "fields": ["numerical-analysis", "optimisation"]},
]
NEW_FIELDS = [{"id": "statistics", "name": "Statistics"}, {"id": "differential-geometry", "name": "Differential geometry"},
              {"id": "functional-analysis", "name": "Functional analysis"}, {"id": "representation-theory", "name": "Representation theory"},
              {"id": "numerical-analysis", "name": "Numerical analysis"}, {"id": "optimisation", "name": "Optimisation"},
              {"id": "category-theory", "name": "Category theory"}]

# Existing concepts moved to topic areas (id -> area), so that no area is a level (school, frontier) rather than a topic.
MOVE = {
 "complex-numbers": "complex", "holomorphic": "complex", "residues": "complex", "continuation": "complex", "gamma": "complex",
 "fourier-poisson": "harmonic", "series": "calculus", "asymptotics": "analytic", "partial-summation": "analytic", "mellin": "analytic",
 "ode-first": "odes", "ode-linear": "odes", "vectors-plane": "linalg",
 "rh": "analytic", "grh": "analytic", "quasi-rh": "analytic", "no-siegel": "analytic", "twin-primes": "analytic", "goldbach": "analytic",
 "bsd": "algebraic", "p-vs-np": "computation", "navier-stokes": "pde", "yang-mills": "diffgeo", "hodge": "topology", "poincare": "topology",
}
# Extra prerequisites for existing concepts, now that the topics they rest on exist.
REWIRE = [("fourier-poisson", ["fourier-transform"]), ("navier-stokes", ["heat-equation"]), ("poincare", ["fundamental-group", "classification-of-surfaces"]),
          ("hodge", ["homology"]), ("yang-mills", ["lie-groups", "differential-forms"]), ("p-vs-np", ["algorithms", "computability"]),
          ("spectral-theorem", []), ("lebesgue", []), ("markov-chains", []), ("limit-theorems", []), ("elliptic-curves", []),
          ("probabilistic-method", []), ("ideals", ["ufds"]), ("graph-coloring", ["planar-graphs"]), ("primality", ["algorithms"])]
RENAME_AREAS = {"precalc": ("Functions", "Functions and their graphs: polynomials, exponentials, logarithms and trigonometric functions.")}
DROP_AREAS = ["analysis", "frontier"]

# Second extension: combinatorics, olympiad algebra and geometry areas, Millennium problems.
import catalog_src as cat
import catalog_ext
from catalog_src import C, REF, EVENTS, FIELDS, BANDS
from catalog_ext import ext, OWN

REF.update({
    "Stanley": "Stanley, Enumerative Combinatorics, Vol. 1",
    "AS": "Alon & Spencer, The Probabilistic Method",
    "Bollobas": "Bollobás, Modern Graph Theory",
    "Diestel": "Diestel, Graph Theory",
    "Jukna": "Jukna, Extremal Combinatorics",
    "PftB": "Andreescu & Feng, A Path to Combinatorics for Undergraduates",
    "HLP": "Hardy, Littlewood & Pólya, Inequalities",
    "Steele": "Steele, The Cauchy–Schwarz Master Class",
    "EGMO": "Chen, Euclidean Geometry in Mathematical Olympiads",
    "Coxeter": "Coxeter & Greitzer, Geometry Revisited",
    "Venema": "Prasolov, Problems in Plane and Solid Geometry",
    "Matousek": "Matoušek, Lectures on Discrete Geometry",
    "Clay": "Carlson, Jaffe & Wiles (eds.), The Millennium Prize Problems",
    "Sipser": "Sipser, Introduction to the Theory of Computation",
    "Artin": "Artin, Algebra",
    "Engel2": "Engel, Problem-Solving Strategies",
})

FIELDS.extend([
    {"id": "topology", "name": "Topology"},
    {"id": "algebraic-geometry", "name": "Algebraic geometry"},
    {"id": "pde", "name": "Partial differential equations"},
])
for f in FIELDS:
    if f["id"] in ("combinatorics", "geometry", "algebra"): f["built"] = "partial"

BANDS.insert(5, {"id": "discrete", "name": "Combinatorics", "blurb": "Counting, graphs, extremal and probabilistic arguments.", "fields": ["combinatorics"]})
BANDS.insert(6, {"id": "olyalg", "name": "Algebra & inequalities", "blurb": "Inequalities, functional equations, polynomials and sequences.", "fields": ["algebra", "real-analysis"]})
BANDS.insert(7, {"id": "geometry", "name": "Geometry", "blurb": "Plane geometry from angle chasing to inversion, and its discrete side.", "fields": ["geometry"]})

D, A, G = "discrete", "olyalg", "geometry"
# ---------------- Combinatorics ----------------
ext("counting", D, "Counting and bijections", "Counting", [],
    r"Counting a set by splitting it into cases, by a bijection with a set that is easier to count, or by inclusion–exclusion. Binomial coefficients are the basic language.",
    [r"\Big|\bigcup_{i=1}^n A_i\Big| = \sum_{\emptyset\ne I\subseteq[n]} (-1)^{|I|+1}\Big|\bigcap_{i\in I}A_i\Big|", r"\binom{n}{k} = \binom{n-1}{k} + \binom{n-1}{k-1}"],
    "Every probability, every expected value and most extremal bounds start as a count.",
    ["05A05", "05A19"], [("probability", "Finite probability is counting divided by counting."), ("computer-science", "Counting objects is how running times and data-structure sizes are estimated.")],
    ["Stanley", "PftB"], aliases=["combinatorics", "inclusion-exclusion", "bijection", "binomial"], fields=["combinatorics"])
ext("pigeonhole", D, "Pigeonhole and double counting", "Pigeonhole & double counting", ["counting"],
    r"If $n+1$ objects go into $n$ boxes, some box gets two. Double counting evaluates one quantity in two ways, such as the number of (vertex, edge) incidences, to get an identity or inequality.",
    [r"\sum_{v} \deg v = 2|E|", r"\text{some box holds at least } \lceil N/k \rceil \text{ objects}"],
    "Both are the first move in extremal problems: they turn a structure into a count that cannot be too large.",
    ["05A99", "05D99"], [("number-theory", "Dirichlet's approximation theorem is a pigeonhole argument on fractional parts.")],
    ["PftB", "Engel"], aliases=["Dirichlet box principle", "double counting", "handshake lemma"], fields=["combinatorics"])
ext("invariants", D, "Invariants and monovariants", "Invariants", [],
    r"For a process that repeats a move, find a quantity the move never changes (an invariant) or always changes in one direction (a monovariant). Invariants rule out end states; monovariants prove termination.",
    [r"\text{move } \Rightarrow\ \Phi(\text{state}) \text{ unchanged, or } \Phi \text{ strictly decreases in } \mathbb N"],
    "This is the olympiad form of conserved quantities in physics and of termination proofs in computer science.",
    ["05A99", "97K20"], [("physics", "Conserved quantities play the same role for dynamical systems."), ("computer-science", "Termination proofs of algorithms use a decreasing potential function.")],
    ["Engel"], aliases=["monovariant", "potential function", "colouring argument"], fields=["combinatorics"])
ext("comb-games", D, "Combinatorial games and strategies", "Games", ["invariants"],
    r"Two players alternate moves with full information. Positions split into winning and losing ones; strategy stealing, pairing strategies and the Sprague–Grundy theory of nim-values decide who wins.",
    [r"\mathcal G(P) = \operatorname{mex}\{\mathcal G(Q) : P \to Q\}", r"\mathcal G(P_1 + P_2) = \mathcal G(P_1) \oplus \mathcal G(P_2)"],
    "Games are the cleanest place to practise quantifier alternation: a strategy is a proof object.",
    ["91A46"], [("computer-science", "Game-tree search and the complexity of games (PSPACE) come from the same model."), ("logic", "Determinacy of infinite games is a topic in set theory.")],
    ["Engel"], aliases=["winning strategy", "nim", "Sprague–Grundy", "strategy stealing"], fields=["combinatorics"])
ext("generating-functions", D, "Generating functions and recurrences", "Generating functions", ["counting", "series"],
    r"Encode a sequence as $\sum a_n x^n$; combinatorial constructions become algebraic operations, and recurrences become equations for the series.",
    [r"\sum_{n\ge0} p(n) x^n = \prod_{k\ge1} \frac{1}{1-x^k}", r"a_{n} = a_{n-1} + a_{n-2} \iff \sum a_n x^n = \frac{a_0 + (a_1 - a_0)x}{1-x-x^2}"],
    "They connect counting to analysis: singularities of the series give asymptotics, as in the Hardy–Ramanujan partition formula.",
    ["05A15"], [("number-theory", "The partition generating function is a modular form, the source of the circle method."), ("complex-analysis", "Coefficient asymptotics come from singularity analysis.")],
    ["Stanley"], aliases=["recurrence", "partitions", "Fibonacci"], fields=["combinatorics", "algebra"])
ext("graph-basics", D, "Graphs, trees and paths", "Graphs", ["counting"],
    r"A graph is a set of vertices with edges between pairs. Degrees, paths, connectivity, trees (connected graphs with no cycles) and Euler tours are the basic notions.",
    [r"\text{tree on } n \text{ vertices} \iff \text{connected with } n-1 \text{ edges}", r"\text{Euler tour exists} \iff \text{connected and all degrees even}"],
    "Graphs model any pairwise relation, so most of combinatorics and much of computer science is written in this language.",
    ["05C05", "05C38"], [("computer-science", "Graph search, shortest paths and network flow are the core algorithms."), ("physics", "Lattice models and Feynman diagrams are graphs.")],
    ["Diestel", "Bollobas"], aliases=["graph theory", "tree", "Euler", "tournament", "connectivity"], fields=["combinatorics"])
ext("cycles-matchings", D, "Cycles, matchings and Hamiltonicity", "Cycles & matchings", ["graph-basics"],
    r"Hall's theorem characterises when a bipartite graph has a matching covering one side; Dirac's theorem gives a degree condition for a Hamiltonian cycle; Erdős–Gallai bounds edges without long cycles.",
    [r"\text{Hall: } |N(S)| \ge |S|\ \ \forall S\subseteq X", r"\delta(G) \ge n/2 \Rightarrow G \text{ Hamiltonian (Dirac)}"],
    "Matchings are the prototype of a min–max theorem; Hamiltonicity is the prototype of an NP-complete property.",
    ["05C70", "05C45", "05C38"], [("computer-science", "Matching is solvable in polynomial time; Hamiltonian cycle is NP-complete.")],
    ["Diestel", "Bollobas"], aliases=["Hall's theorem", "perfect matching", "Hamiltonian cycle", "Dirac"], fields=["combinatorics"])
ext("graph-coloring", D, "Graph colouring", "Colouring", ["graph-basics"],
    r"A proper colouring gives adjacent vertices different colours; $\chi(G)$ is the fewest colours needed. Brooks, the four colour theorem and Hadwiger's conjecture are the landmarks.",
    [r"\chi(G) \le \Delta(G) + 1", r"\chi(G) \ge \frac{|V|}{\alpha(G)}"],
    "Colouring is scheduling and register allocation; chromatic number problems for geometric graphs are among the oldest open questions.",
    ["05C15"], [("computer-science", "Register allocation and scheduling are colouring problems."), ("geometry", "The chromatic number of the plane (Hadwiger–Nelson) is between 5 and 7.")],
    ["Diestel"], aliases=["chromatic number", "four colour theorem", "Hadwiger", "Brooks"], fields=["combinatorics"])
ext("extremal-graphs", D, "Extremal graph theory", "Extremal graphs", ["graph-basics", "pigeonhole"],
    r"How many edges can a graph on $n$ vertices have without containing a fixed subgraph $H$? Turán answers it for cliques; Erdős–Stone for all non-bipartite $H$; bipartite $H$ remain largely open.",
    [r"\operatorname{ex}(n, K_{r+1}) = \Big(1-\frac1r\Big)\frac{n^2}{2}\ \ (\text{Turán graph})", r"\operatorname{ex}(n,H) = \Big(1-\frac{1}{\chi(H)-1}+o(1)\Big)\binom n2"],
    "The bipartite case connects to Sidon sets and finite geometry, and is where algebraic constructions beat random ones.",
    ["05C35"], [("number-theory", "Extremal $C_4$-free graphs come from Sidon sets and finite fields.")],
    ["Bollobas", "Jukna"], aliases=["Turán", "forbidden subgraph", "Zarankiewicz", "Erdős–Stone"], fields=["combinatorics"])
ext("ramsey", D, "Ramsey theory", "Ramsey theory", ["graph-basics", "pigeonhole"],
    r"Every $2$-colouring of the edges of a large complete graph contains a monochromatic $K_k$. The Ramsey number $R(k)$ is the threshold; $\sqrt2^{\,k} \le R(k) \le 4^k$, improved to $(4-\varepsilon)^k$ in 2023.",
    [r"R(k,\ell) \le \binom{k+\ell-2}{k-1}", r"R(k) \le (4-\varepsilon)^k \ \ \text{(Campos–Griffiths–Morris–Sahasrabudhe 2023)}"],
    "Complete disorder is impossible: this one principle spans graphs, arithmetic progressions and logic.",
    ["05D10", "05C55"], [("logic", "Ramsey's original 1930 theorem was a lemma in decision procedures for logic."), ("number-theory", "Schur and van der Waerden are Ramsey theorems for arithmetic.")],
    ["GRS", "Bollobas"], aliases=["Ramsey number", "R(k)", "monochromatic"], fields=["combinatorics"])
ext("probabilistic-method", D, "The probabilistic method", "Probabilistic method", ["counting"],
    r"To show an object exists, pick one at random and show the probability it works is positive. Linearity of expectation, alterations, the Lovász local lemma and concentration inequalities are the main tools.",
    [r"\Pr\big[\text{some } K_k \text{ monochromatic}\big] \le \binom nk 2^{1-\binom k2} < 1 \Rightarrow R(k) > n", r"\mathbb E[X] \ge t \Rightarrow \Pr[X\ge t] > 0"],
    "Erdős's 1947 Ramsey lower bound started it; it now drives coding theory, randomized algorithms and much of extremal combinatorics.",
    ["05D40", "60C05"], [("probability", "It applies probability to prove deterministic statements."), ("computer-science", "Derandomisation turns these proofs into algorithms.")],
    ["AS"], aliases=["random construction", "Lovász local lemma", "first moment", "deletion method"], fields=["combinatorics", "probability"])
ext("set-systems", D, "Extremal set theory", "Set systems", ["counting", "pigeonhole"],
    r"How large can a family of subsets of $[n]$ be under a restriction? Sperner bounds antichains, Erdős–Ko–Rado bounds intersecting families of $k$-sets, and the sunflower lemma finds structured subfamilies.",
    [r"|\mathcal F| \le \binom{n}{\lfloor n/2\rfloor}\ \ \text{(Sperner)}", r"|\mathcal F| \le \binom{n-1}{k-1}\ \ \text{if pairwise intersecting},\ n\ge 2k"],
    "These bounds are the combinatorial core of results in coding theory, complexity lower bounds and the union-closed sets conjecture.",
    ["05D05"], [("computer-science", "Sunflowers and set-system bounds give circuit lower bounds.")],
    ["Jukna"], aliases=["Sperner", "Erdős–Ko–Rado", "intersecting family", "sunflower", "antichain"], fields=["combinatorics"])
ext("hypergraphs", D, "Hypergraphs", "Hypergraphs", ["graph-basics", "set-systems"],
    r"Edges with any number of vertices. Turán and Ramsey questions become much harder: the Turán density of the $3$-uniform $K_4^{(3)}$ is still unknown.",
    [r"\pi\big(K_4^{(3)}\big) \overset{?}{=} \tfrac59 \ \ \text{(Turán's conjecture)}"],
    "Hypergraph regularity and container methods power modern proofs of Szemerédi-type theorems.",
    ["05C65"], [("number-theory", "Hypergraph removal lemmas prove multidimensional Szemerédi theorems.")],
    ["Jukna"], aliases=["uniform hypergraph", "Turán density", "containers"], fields=["combinatorics"])
ext("grids-tilings", D, "Grids, tilings and board colourings", "Grids & tilings", ["invariants"],
    r"Problems on chessboards and grids: tiling regions with dominoes or polyominoes, placing pieces, and colouring the board so a counting argument rules a configuration out.",
    [r"\text{a mutilated } 8\times8 \text{ board (two opposite corners removed) has no domino tiling}"],
    "The colouring trick is an invariant in disguise; domino tilings link to determinants and statistical physics.",
    ["05B45", "52C20"], [("physics", "Counting domino tilings is the dimer model (Kasteleyn, Temperley–Fisher).")],
    ["Engel"], aliases=["chessboard", "domino", "polyomino", "tiling"], fields=["combinatorics"])
ext("discrete-geometry", D, "Combinatorial geometry", "Combinatorial geometry", ["pigeonhole", "euclid-basics"],
    r"Finite point sets in the plane: how many unit distances, how many distinct distances, when points must contain a convex $k$-gon, how lines and points can be incident.",
    [r"\#\text{unit distances} \le O(n^{4/3})\ \ \text{(Spencer–Szemerédi–Trotter)}", r"\#\text{distinct distances} \ge c\,\frac{n}{\log n}\ \ \text{(Guth–Katz)}"],
    "Erdős's distance problems pushed incidence geometry into polynomial methods; in May 2026 an AI model found a counterexample to his unit distance conjecture.",
    ["52C10", "52C35"], [("combinatorics", "Incidence bounds are extremal graph theory on geometric graphs."), ("ai-research", "OpenAI reported in May 2026 a counterexample to Erdős's 1946 unit distance conjecture.")],
    ["Matousek"], aliases=["unit distance", "distinct distances", "Erdős–Szekeres", "Happy ending", "incidences"], fields=["geometry", "combinatorics"])
ext("infinite-combinatorics", D, "Infinite combinatorics and partition calculus", "Infinite combinatorics", ["ramsey"],
    r"Ramsey theory for infinite sets and cardinals. The arrow notation $\kappa \to (\lambda)^n_r$ asks whether every colouring of $n$-subsets of $\kappa$ with $r$ colours has a homogeneous set of size $\lambda$.",
    [r"\aleph_0 \to (\aleph_0)^n_r \ \ \text{(infinite Ramsey)}", r"2^{\aleph_0} \not\to (\aleph_1)^2_2 \ \ \text{(Sierpiński)}"],
    "Several of these questions are independent of ZFC, so the answer depends on the axioms.",
    ["03E02", "05D10"], [("logic", "Partition relations for large cardinals are set theory proper.")],
    ["GRS"], aliases=["partition calculus", "arrow notation", "Erdős–Rado"], fields=["combinatorics", "logic"])

# ---------------- Algebra & inequalities ----------------
ext("amgm", A, "AM–GM and power means", "AM–GM", [],
    r"For non-negative reals the arithmetic mean is at least the geometric mean, with equality when all are equal. More generally the power means $M_p$ increase with $p$.",
    [r"\frac{x_1+\cdots+x_n}{n} \ge \sqrt[n]{x_1\cdots x_n}", r"M_p(x) = \Big(\tfrac1n\textstyle\sum x_i^p\Big)^{1/p}\ \text{is increasing in } p"],
    "Most competition inequalities reduce to weighted AM–GM after the right substitution.",
    ["26D15"], [("real-analysis", "AM–GM is the concavity of $\\log$.")],
    ["HLP", "Steele"], aliases=["arithmetic mean", "geometric mean", "power mean", "inequality"], fields=["real-analysis", "algebra"])
ext("cauchy-schwarz", A, "Cauchy–Schwarz, Hölder and rearrangement", "Cauchy–Schwarz", ["amgm"],
    r"$(\sum a_ib_i)^2 \le (\sum a_i^2)(\sum b_i^2)$, its Engel form $\sum a_i^2/b_i \ge (\sum a_i)^2/\sum b_i$, Hölder's generalisation, and the rearrangement inequality for similarly ordered sequences.",
    [r"\Big(\sum a_ib_i\Big)^2 \le \sum a_i^2 \sum b_i^2", r"\sum \frac{a_i^2}{b_i} \ge \frac{(\sum a_i)^2}{\sum b_i}"],
    "Cauchy–Schwarz is the inequality of inner-product spaces, used everywhere from Fourier analysis to quantum mechanics.",
    ["26D15", "15A45"], [("harmonic-analysis", "Bessel, Plancherel and large-sieve inequalities are Cauchy–Schwarz in function spaces."), ("physics", "The uncertainty principle is a Cauchy–Schwarz inequality.")],
    ["Steele", "HLP"], aliases=["Hölder", "Titu", "Engel form", "rearrangement", "Chebyshev sum"], fields=["real-analysis", "algebra"])
ext("convexity", A, "Convexity, Jensen and majorization", "Convexity & Jensen", ["amgm"],
    r"A convex function lies below its chords, so $f(\text{mean}) \le \text{mean of } f$. Tangent-line tricks, Karamata's majorization inequality and smoothing arguments extend this.",
    [r"f\Big(\sum w_ix_i\Big) \le \sum w_i f(x_i)\ \ (f \text{ convex},\ \textstyle\sum w_i = 1)"],
    "Convexity is the reason optimisation problems have unique answers, from mechanics to machine learning.",
    ["26A51", "26D15"], [("computer-science", "Convex optimisation is the solvable core of machine learning and operations research."), ("probability", "Jensen's inequality is the basic inequality for expectations.")],
    ["HLP"], aliases=["Jensen", "Karamata", "majorization", "smoothing", "tangent line trick"], fields=["real-analysis"])
ext("symmetric-ineq", A, "Symmetric and polynomial inequalities", "Symmetric inequalities", ["amgm", "polynomials-roots"],
    r"Inequalities in symmetric polynomials of a few variables: Schur's inequality, Muirhead, sum-of-squares decompositions and the $uvw$ method that reduces to the case of two equal variables.",
    [r"\sum_{\text{cyc}} a^t(a-b)(a-c) \ge 0\ \ (a,b,c\ge0,\ t>0)\ \ \text{(Schur)}"],
    "Deciding when a polynomial is a sum of squares is Hilbert's 17th problem, solved by Artin in 1927.",
    ["26D05", "12D15"], [("algebra", "Positivstellensätze in real algebraic geometry generalise SOS certificates."), ("computer-science", "SOS relaxations are semidefinite programs.")],
    ["HLP"], aliases=["Schur", "Muirhead", "SOS", "uvw", "homogenization"], fields=["algebra", "real-analysis"])
ext("real-functional-eq", A, "Functional equations over the reals", "Functional equations", [],
    r"Find all $f:\mathbb R\to\mathbb R$ with an identity such as $f(x+y)=f(x)+f(y)$. The moves are substitutions, proving injectivity or surjectivity, and pinning down $f$ on rationals before using a regularity condition.",
    [r"f(x+y)=f(x)+f(y),\ f \text{ monotone} \Rightarrow f(x)=cx\ \ \text{(Cauchy)}"],
    "Without a regularity condition Cauchy's equation has wild solutions built from a Hamel basis, an early use of the axiom of choice.",
    ["39B22"], [("logic", "Non-linear solutions of Cauchy's equation need the axiom of choice."), ("real-analysis", "Continuity or measurability forces linear solutions.")],
    ["Engel"], aliases=["Cauchy equation", "functional equation", "injective", "surjective"], fields=["algebra", "real-analysis"])
ext("polynomials-roots", A, "Polynomials, roots and Vieta's formulas", "Polynomials", [],
    r"A degree-$n$ polynomial has at most $n$ roots; its coefficients are the elementary symmetric functions of the roots. Interpolation, the factor theorem and comparing coefficients solve most problems.",
    [r"\prod_{i=1}^n (x - r_i) = x^n - e_1x^{n-1} + e_2x^{n-2} - \cdots + (-1)^n e_n", r"P(a) = 0 \iff (x-a) \mid P(x)"],
    "Polynomials are the objects of algebraic geometry and the workhorse of the polynomial method in combinatorics.",
    ["12D10", "26C10"], [("algebraic-geometry", "Varieties are zero sets of polynomials."), ("combinatorics", "The polynomial method (Combinatorial Nullstellensatz, Dvir) solves extremal problems.")],
    ["Artin"], aliases=["Vieta", "roots", "interpolation", "symmetric functions"], fields=["algebra"])
ext("sequences", A, "Sequences, recurrences and limits", "Sequences", [],
    r"Sequences defined by a rule: bound them, find their limit, prove periodicity or eventual behaviour. Linear recurrences solve by characteristic roots; non-linear ones by monotonicity and invariants.",
    [r"a_{n+2} = pa_{n+1} + qa_n \Rightarrow a_n = \alpha r_1^n + \beta r_2^n", r"\text{bounded and monotone} \Rightarrow \text{convergent}"],
    "Discrete dynamical systems start here; the Collatz problem shows how quickly simple rules become intractable.",
    ["11B37", "40A05"], [("dynamics", "Iterating a map is a discrete dynamical system."), ("number-theory", "Linear recurrences mod $p$ are periodic and carry arithmetic information.")],
    ["Engel"], aliases=["recurrence", "limit", "periodicity", "Collatz"], fields=["real-analysis", "algebra"])
ext("floor-functions", A, "Floor functions and fractional parts", "Floor & fractional parts", ["divisibility"],
    r"Identities and estimates for $\lfloor x\rfloor$ and $\{x\} = x - \lfloor x\rfloor$, Beatty sequences, and equidistribution of $\{n\alpha\}$.",
    [r"\sum_{k=0}^{n-1}\Big\lfloor x + \frac kn\Big\rfloor = \lfloor nx\rfloor\ \ \text{(Hermite)}", r"\tfrac1\alpha + \tfrac1\beta = 1,\ \alpha\notin\mathbb Q \Rightarrow \{\lfloor n\alpha\rfloor\} \sqcup \{\lfloor n\beta\rfloor\} = \mathbb N_{>0}"],
    "Counting lattice points under a curve is a floor sum; Weyl's equidistribution theorem is about fractional parts.",
    ["11A25", "11K06"], [("number-theory", "Lattice point counts and Dirichlet's divisor problem are floor sums.")],
    ["Engel"], aliases=["floor", "ceiling", "Beatty", "Hermite identity"], fields=["number-theory", "algebra"])
ext("groups", A, "Groups and symmetry", "Groups", [],
    r"A group is a set with an associative operation, an identity and inverses. Lagrange's theorem, group actions and orbit counting (Burnside) are the first tools.",
    [r"|H| \text{ divides } |G|\ \ \text{(Lagrange)}", r"\#\text{orbits} = \frac1{|G|}\sum_{g\in G}|\operatorname{Fix}(g)|\ \ \text{(Burnside)}"],
    "Symmetry is group theory; Fermat's little theorem is Lagrange's theorem for $(\\mathbb Z/p)^\\times$.",
    ["20-01", "20B05"], [("physics", "Symmetry groups classify particles and conservation laws."), ("number-theory", "Unit groups mod $n$ and class groups are where groups first meet arithmetic.")],
    ["Artin"], aliases=["group theory", "Lagrange", "Burnside", "symmetry"], fields=["algebra"])
ext("linear-algebra", A, "Linear algebra methods", "Linear algebra", [],
    r"Vector spaces, rank and determinants as tools: bound a family by showing its members are linearly independent in a space of known dimension.",
    [r"v_1,\dots,v_m \in \mathbb F^n \text{ independent} \Rightarrow m \le n"],
    "The dimension argument gives some of the sharpest bounds in combinatorics (Frankl–Wilson, Fisher's inequality).",
    ["15A03", "05D05"], [("combinatorics", "Oddtown and Fisher-type theorems are rank arguments."), ("physics", "Quantum states live in vector spaces.")],
    ["Artin", "Jukna"], aliases=["rank", "determinant", "dimension argument", "oddtown"], fields=["algebra"])

# ---------------- Geometry ----------------
ext("euclid-basics", G, "Angles, triangles and similarity", "Angles & similarity", [],
    r"Angle chasing, congruent and similar triangles, the laws of sines and cosines, and areas. Nearly every olympiad geometry solution is built from these.",
    [r"\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R", r"c^2 = a^2 + b^2 - 2ab\cos C"],
    "Euclid's Elements is the first axiomatic theory; its parallel postulate led to non-Euclidean geometry.",
    ["51M04"], [("physics", "Similarity and trigonometry are the geometry of measurement.")],
    ["Coxeter", "EGMO"], aliases=["angle chasing", "similar triangles", "law of sines", "Euclidean geometry"], fields=["geometry"])
ext("circles", G, "Circles and power of a point", "Circles", ["euclid-basics"],
    r"Inscribed angles, cyclic quadrilaterals, tangents, and the power of a point $P$ with respect to a circle: for any line through $P$ meeting the circle at $A,B$, $PA\cdot PB$ is constant.",
    [r"PA \cdot PB = |PO|^2 - r^2", r"ABCD \text{ cyclic} \iff \angle A + \angle C = 180^\circ"],
    "Radical axes and coaxal circles organise most configurations with several circles.",
    ["51M04", "51M15"], [],
    ["EGMO", "Coxeter"], aliases=["cyclic quadrilateral", "radical axis", "tangent", "inscribed angle"], fields=["geometry"])
ext("triangle-centres", G, "Triangle centres and classical configurations", "Triangle centres", ["circles"],
    r"Incentre, circumcentre, orthocentre, centroid and their circles: the Euler line, the nine-point circle, the incircle and excircles, Ceva's and Menelaus's theorems.",
    [r"OH^2 = 9R^2 - (a^2+b^2+c^2)", r"\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB} = 1\ \ \text{(Ceva)}"],
    "Recognising a standard configuration is often the whole solution.",
    ["51M04"], [],
    ["EGMO", "Coxeter"], aliases=["Euler line", "nine-point circle", "incircle", "Ceva", "Menelaus", "orthocenter"], fields=["geometry"])
ext("geo-transformations", G, "Transformations and inversion", "Transformations", ["circles"],
    r"Homotheties, rotations, reflections, spiral similarities and inversion map a configuration to a simpler one. Inversion turns circles through the centre into lines.",
    [r"P \mapsto P' \text{ on ray } OP,\ \ OP\cdot OP' = r^2"],
    "Thinking in transformations is Klein's Erlangen programme: a geometry is the study of invariants of a group.",
    ["51M05", "51B10"], [("algebra", "Möbius transformations form the group $PGL_2(\\mathbb C)$."), ("complex-analysis", "Inversion is the conformal map $z \\mapsto 1/\\bar z$.")],
    ["EGMO", "Coxeter"], aliases=["inversion", "homothety", "spiral similarity", "projective"], fields=["geometry"])
ext("analytic-geometry", G, "Coordinates, vectors and complex numbers", "Coordinates & complex", ["euclid-basics", "complex-numbers"],
    r"Place the figure in coordinates, use vectors, complex numbers on the unit circle, or barycentric coordinates, and compute.",
    [r"a,b,c,d \text{ on the unit circle: } ab \parallel cd \iff ab = cd"],
    "Computation is a guaranteed fallback; choosing the frame that keeps it short is the skill.",
    ["51N20"], [("algebra", "Bashing a configuration is solving a polynomial system, which Gröbner bases automate.")],
    ["EGMO"], aliases=["complex bash", "barycentric", "coordinates", "vectors"], fields=["geometry", "algebra"])
ext("geo-inequalities", G, "Geometric inequalities and extremal geometry", "Geometric inequalities", ["euclid-basics", "amgm"],
    r"Inequalities among lengths, areas and angles of figures: the triangle inequality, Euler's $R \ge 2r$, the isoperimetric inequality, Erdős–Mordell.",
    [r"R \ge 2r", r"PA+PB+PC \ge 2(PD+PE+PF)\ \ \text{(Erdős–Mordell)}", r"4\pi A \le L^2"],
    "The isoperimetric inequality is the model for a large part of geometric analysis.",
    ["51M16", "52A40"], [("real-analysis", "The isoperimetric inequality is a variational problem.")],
    ["Coxeter"], aliases=["isoperimetric", "Erdős–Mordell", "triangle inequality"], fields=["geometry", "real-analysis"])

# ---------------- Millennium Prize Problems ----------------
F = "frontier"
ext("bsd", F, "The Birch and Swinnerton-Dyer conjecture", "BSD conjecture", ["elliptic-curves", "l-functions"],
    r"The rank of the group of rational points of an elliptic curve $E/\mathbb Q$ equals the order of vanishing of $L(E,s)$ at $s=1$. Known when that order is $0$ or $1$ (Gross–Zagier, Kolyvagin).",
    [r"\operatorname{rank} E(\mathbb Q) = \operatorname{ord}_{s=1} L(E,s)"],
    "It is one of the seven Millennium Prize Problems and would give an algorithm for deciding whether a cubic curve has infinitely many rational points.",
    ["11G40", "14G10"], [("algebraic-geometry", "Elliptic curves are abelian varieties of dimension one.")],
    ["ST", "Clay"], status="open", aliases=["Birch–Swinnerton-Dyer", "rank", "Millennium"], fields=["number-theory", "algebraic-geometry"])
ext("p-vs-np", F, "P versus NP", "P vs NP", ["graph-basics"],
    r"Is every problem whose solutions can be checked in polynomial time also solvable in polynomial time? Most researchers expect $\mathrm P \ne \mathrm{NP}$; known proof techniques (relativisation, natural proofs, algebrisation) provably cannot settle it.",
    [r"\mathrm P \overset{?}{=} \mathrm{NP}"],
    "A Millennium Prize Problem; modern cryptography assumes the answer is no.",
    ["68Q15"], [("cryptography", "Public-key cryptography needs one-way functions, which require $\\mathrm P \\ne \\mathrm{NP}$."), ("logic", "Descriptive complexity recasts the question in finite model theory.")],
    ["Sipser", "Clay"], status="open", aliases=["NP-complete", "complexity", "Cook–Levin", "Millennium"], fields=["computer-science", "logic"])
ext("navier-stokes", F, "Navier–Stokes existence and smoothness", "Navier–Stokes", ["fourier-poisson"],
    r"Do smooth initial data for the three-dimensional incompressible Navier–Stokes equations always give a smooth solution for all time? Leray (1934) constructed weak solutions; their uniqueness and regularity are open.",
    [r"\partial_t u + (u\cdot\nabla)u = \nu\Delta u - \nabla p,\qquad \nabla\cdot u = 0"],
    "A Millennium Prize Problem about the basic equations of fluid flow.",
    ["35Q30", "76D05"], [("physics", "These are the equations of viscous incompressible fluids."), ("ai-research", "In 2025 Google DeepMind and collaborators used neural-network solvers to find unstable self-similar blow-up candidates for related fluid equations.")],
    ["Clay"], status="open", aliases=["fluid", "blow-up", "regularity", "Millennium"], fields=["pde", "physics"])
ext("yang-mills", F, "Yang–Mills existence and mass gap", "Yang–Mills mass gap", ["groups"],
    r"Construct a quantum Yang–Mills theory on $\mathbb R^4$ for any compact simple gauge group satisfying the standard axioms, and prove it has a mass gap $\Delta > 0$.",
    [r"\operatorname{spec}(H) \subset \{0\} \cup [\Delta, \infty),\quad \Delta > 0"],
    "A Millennium Prize Problem; it asks for a mathematical foundation for the theory that describes the strong force.",
    ["81T13", "70S15"], [("physics", "Quantum chromodynamics is a Yang–Mills theory with gauge group $SU(3)$.")],
    ["Clay"], status="open", aliases=["gauge theory", "quantum field theory", "mass gap", "Millennium"], fields=["physics"])
ext("hodge", F, "The Hodge conjecture", "Hodge conjecture", ["complex-numbers", "polynomials-roots"],
    r"On a non-singular complex projective variety, every rational cohomology class of type $(p,p)$ is a rational combination of classes of algebraic subvarieties.",
    [r"H^{2p}(X,\mathbb Q)\cap H^{p,p}(X) \overset{?}{=} \operatorname{span}_{\mathbb Q}\{[Z] : Z \subset X \text{ algebraic}\}"],
    "A Millennium Prize Problem connecting topology, analysis and algebra on the same space.",
    ["14C30"], [("topology", "Cohomology classes are topological invariants."), ("complex-analysis", "Hodge theory decomposes cohomology by harmonic forms.")],
    ["Clay"], status="open", aliases=["algebraic cycles", "cohomology", "Millennium"], fields=["algebraic-geometry", "topology"])
ext("poincare", F, "The Poincaré conjecture", "Poincaré conjecture", [],
    r"Every simply connected closed $3$-manifold is homeomorphic to the $3$-sphere. Proved by Perelman (2002–03) using Ricci flow with surgery; the only Millennium Problem solved.",
    [r"\partial_t g = -2\operatorname{Ric}(g)"],
    "Perelman declined both the Fields Medal (2006) and the Millennium Prize (2010).",
    ["57M40", "53E20"], [("pde", "Ricci flow is a non-linear heat equation for metrics."), ("geometry", "Thurston's geometrisation, which Perelman also proved, classifies 3-manifolds.")],
    ["Clay"], aliases=["Perelman", "Ricci flow", "3-manifold", "Millennium"], fields=["topology", "geometry"])

# wiring
def con(i): return next(c for c in C if c["id"] == i)
con("ramsey-arithmetic")["pre"].append("ramsey")
con("vieta-jumping")["pre"].append("polynomials-roots")

EVENTS.extend([
    dict(id="euclid-el", y=-300, label="c. 300 BC", title="Euclid's Elements", who="Euclid", text=r"Axiomatic plane geometry; Book IX also proves there are infinitely many primes.", nodes=["euclid-basics", "fta"]),
    dict(id="euler-k", y=1736, label="1736", title="The bridges of Königsberg", who="Leonhard Euler", text=r"Shows no walk crosses each bridge once, the first theorem of graph theory.", nodes=["graph-basics"]),
    dict(id="cauchy-ineq", y=1821, label="1821", title="Cauchy's inequality", who="Augustin-Louis Cauchy", text=r"$(\sum a_ib_i)^2 \le \sum a_i^2\sum b_i^2$ in his Cours d'analyse; Schwarz proved the integral form in 1888.", nodes=["cauchy-schwarz"]),
    dict(id="jensen", y=1906, label="1906", title="Jensen's inequality", who="Johan Jensen", text=r"Convex functions lie below their chords, in any number of points.", nodes=["convexity"]),
    dict(id="ramsey30", y=1930, label="1930", title="Ramsey's theorem", who="Frank Ramsey", text=r"Proved as a lemma about decision procedures in logic.", nodes=["ramsey"]),
    dict(id="hall", y=1935, label="1935", title="Hall's marriage theorem", who="Philip Hall", text=r"A bipartite graph has a matching saturating one side iff every subset has enough neighbours.", nodes=["cycles-matchings"]),
    dict(id="turan", y=1941, label="1941", title="Turán's theorem", who="Pál Turán", text=r"The densest graph with no $K_{r+1}$ is the balanced complete $r$-partite graph.", nodes=["extremal-graphs"]),
    dict(id="erdos47", y=1947, label="1947", title="Random graphs bound Ramsey numbers", who="Paul Erdős", text=r"A counting argument shows $R(k) > 2^{k/2}$, the start of the probabilistic method.", nodes=["probabilistic-method", "ramsey"]),
    dict(id="ekr", y=1961, label="1961", title="Erdős–Ko–Rado theorem", who="Erdős, Ko, Rado", text=r"Intersecting families of $k$-subsets of $[n]$, $n\ge2k$, have at most $\binom{n-1}{k-1}$ members.", nodes=["set-systems"]),
    dict(id="cook", y=1971, label="1971", title="NP-completeness", who="Stephen Cook; Leonid Levin", text=r"SAT is NP-complete, which makes P versus NP precise.", nodes=["p-vs-np"]),
    dict(id="4ct", y=1976, label="1976", title="The four colour theorem", who="Kenneth Appel, Wolfgang Haken", text=r"Every planar map can be coloured with four colours; the first major computer-assisted proof.", nodes=["graph-coloring"]),
    dict(id="clay", y=2000, label="2000", title="The Millennium Prize Problems", who="Clay Mathematics Institute", text=r"Seven problems, a million dollars each: RH, P vs NP, Navier–Stokes, Yang–Mills, Hodge, BSD and Poincaré.", nodes=["rh", "p-vs-np", "navier-stokes", "yang-mills", "hodge", "bsd", "poincare"]),
    dict(id="perelman", y=2003, label="2002–03", title="Perelman proves Poincaré", who="Grigori Perelman", text=r"Ricci flow with surgery proves the Poincaré and geometrisation conjectures.", nodes=["poincare"]),
    dict(id="guth-katz", y=2010.9, label="2010", title="The distinct distances problem", who="Larry Guth, Nets Katz", text=r"$n$ points determine $\gg n/\log n$ distinct distances, via the polynomial method.", nodes=["discrete-geometry"]),
    dict(id="cgms", y=2023.2, label="2023", title="Exponential improvement for Ramsey numbers", who="Campos, Griffiths, Morris, Sahasrabudhe", text=r"$R(k) \le (4-\varepsilon)^k$, the first exponential improvement since 1935.", nodes=["ramsey"]),
    dict(id="unit-dist", y=2026.385, label="20 May 2026", ai=True, title="Unit distance conjecture disproved", who="OpenAI internal model", text=r"Reported counterexample to Erdős's 1946 conjecture on the maximum number of unit distances; Tim Gowers praised the proof.", nodes=["discrete-geometry"], url="https://www.quantamagazine.org/how-ai-tore-through-a-mathematical-community-20260803/", src="Quanta"),
])

for c in C:
    if "fields" not in c or c["id"] in OWN:
        band = next(b for b in BANDS if b["id"] == c["band"])
        c["fields"] = OWN.get(c["id"], band["fields"][:1])

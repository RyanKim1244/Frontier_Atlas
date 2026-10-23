# Extends catalog_src: cross-field areas, field membership, olympiad and combinatorial concepts, new events.
import catalog_src as cat
from catalog_src import concept, C, REF, EVENTS, FIELDS, BANDS

REF.update({
    "Engel": "Engel, Problem-Solving Strategies",
    "TV": "Tao & Vu, Additive Combinatorics",
    "GRS": "Graham, Rothschild & Spencer, Ramsey Theory",
    "Guy": "Guy, Unsolved Problems in Number Theory",
    "Tenenbaum": "Tenenbaum, Introduction to Analytic and Probabilistic Number Theory",
    "Bugeaud": "Bugeaud, Approximation by Algebraic Numbers",
    "EG": "Erdős & Graham, Old and New Problems and Results in Combinatorial Number Theory",
})

# Areas are clusters of concepts. They are not owned by one field: each lists the fields it belongs to.
BANDS[:] = [
    {"id": "foundations", "name": "Elementary number theory", "blurb": "Divisibility, congruences and Diophantine equations: the olympiad core.", "fields": ["number-theory"]},
    {"id": "analysis", "name": "Analysis", "blurb": "Real, complex and harmonic analysis, used far beyond number theory.", "fields": ["real-analysis", "complex-analysis", "harmonic-analysis"]},
    {"id": "analytic", "name": "Analytic number theory", "blurb": "Primes through zeta and L-functions, sieves and exponential sums.", "fields": ["number-theory"]},
    {"id": "algebraic", "name": "Algebraic number theory", "blurb": "Number fields, ideals, reciprocity and their L-functions.", "fields": ["number-theory", "algebra"]},
    {"id": "combinatorial", "name": "Combinatorial & additive", "blurb": "Where number theory and combinatorics are the same subject: sumsets, progressions, colourings.", "fields": ["combinatorics", "number-theory"]},
    {"id": "computation", "name": "Computation & cryptography", "blurb": "Algorithms built on number theory.", "fields": ["number-theory", "computer-science", "cryptography"]},
    {"id": "frontier", "name": "Frontier", "blurb": "Open problems and 2026 claims under verification.", "fields": ["number-theory"]},
]
FIELDS.insert(1, {"id": "real-analysis", "name": "Real analysis"})
for f in FIELDS:
    if f["id"] == "combinatorics": f["built"] = "partial"
FIELDS.append({"id": "logic", "name": "Logic & set theory"})

# Field membership. A concept belongs to every field listed; the first is its home.
OWN = {
    "series": ["real-analysis"], "asymptotics": ["real-analysis", "number-theory"], "partial-summation": ["real-analysis", "number-theory"],
    "complex-numbers": ["complex-analysis", "algebra"], "holomorphic": ["complex-analysis"], "residues": ["complex-analysis"],
    "continuation": ["complex-analysis"], "gamma": ["special-functions", "complex-analysis"], "fourier-poisson": ["harmonic-analysis"],
    "mellin": ["harmonic-analysis", "complex-analysis"], "elliptic-curves": ["number-theory", "algebra", "geometry"],
    "primality": ["number-theory", "computer-science"], "rsa": ["cryptography", "number-theory"], "discrete-log": ["cryptography", "number-theory", "computer-science"],
    "quadratic-forms": ["number-theory", "algebra"], "continued-fractions": ["number-theory", "real-analysis"],
}

def ext(id, band, title, short, pre, sum, key=(), why="", msc=(), links=(), refs=(), status=None, aliases=(), fields=None):
    concept(id, band, title, short, pre, sum, key, why, msc, links, refs, status, aliases)
    if fields: OWN[id] = fields

# ---- olympiad toolkit (elementary) ----
ext("diophantine", "foundations", "Elementary Diophantine equations", "Diophantine equations", ["divisibility", "congruences", "fta"],
    r"Equations to be solved in integers. The elementary toolkit is factoring, bounding one variable by another, and reducing modulo a well-chosen number to rule out cases.",
    [r"x^2 - y^2 = n \iff (x-y)(x+y) = n", r"y^2 \equiv 2,3 \pmod 4 \ \text{has no solution}"],
    "Most olympiad number theory is a Diophantine equation in disguise, and the same moves (size, parity, a modulus) recur in research on the abc conjecture and on Fermat-type equations.",
    ["11D04", "11D09"], [("algebra", "Factoring over larger rings, such as $\\mathbb Z[i]$ or $\\mathbb Z[\\omega]$, turns many of these equations into statements about ideals.")],
    ["NZM", "AAF"], aliases=["integer equations", "find all integers"])
ext("digits-bases", "foundations", "Digits and base representations", "Digits and bases", ["congruences"],
    r"Writing $n = \sum a_i b^i$ with $0 \le a_i < b$. Digit sums, last digits and base changes are controlled by congruences modulo $b-1$, $b+1$ and powers of $b$.",
    [r"n \equiv s_{10}(n) \pmod 9", r"\nu_2\!\binom{m+n}{m} = \#\{\text{carries when adding } m,n \text{ in base } 2\}"],
    "Digit problems test whether you can translate a statement about writing into a statement about arithmetic.",
    ["11A63"], [("computer-science", "Base-$2$ representations are machine arithmetic; carries and digit sums govern algorithms from addition to the Fast Fourier Transform.")],
    ["NZM", "AAF"], aliases=["digit sum", "decimal digits", "binary"])
ext("vieta-jumping", "foundations", "Vieta jumping", "Vieta jumping", ["diophantine"],
    r"For a symmetric quadratic condition such as $a^2+b^2 = k(ab+1)$, the second root $a' = kb - a$ of the quadratic in $a$ is again an integer. Replacing $(a,b)$ by $(a',b)$ gives a descent that must end at a small solution.",
    [r"a + a' = kb,\qquad a a' = b^2 - k"],
    "It is the elementary shadow of the action of an automorphism group on the integer points of a conic, the same structure behind Markov numbers.",
    ["11D09"], [("algebra", "The move is a reflection in the automorphism group of a binary quadratic form."), ("geometry", "Each jump moves between integer points on a hyperbola.")],
    ["AAF", "Engel"], aliases=["root flipping", "descent"], fields=["number-theory", "algebra"])
ext("lte-zsigmondy", "foundations", "Lifting the exponent and Zsigmondy's theorem", "LTE & Zsigmondy", ["p-adic-valuation", "order-primroot"],
    r"For an odd prime $p \mid a-b$, $p \nmid ab$, the lifting-the-exponent lemma gives $\nu_p(a^n-b^n)$ exactly. Zsigmondy's theorem says $a^n-b^n$ has a prime factor not dividing any earlier $a^k-b^k$, with a short list of exceptions.",
    [r"\nu_p(a^n - b^n) = \nu_p(a-b) + \nu_p(n)", r"\text{exceptions: } 2^6-1,\ \ n=2,\ a+b=2^k"],
    r"Together they settle almost any problem of the form $n^k \mid a^n \pm 1$.",
    ["11A41", "11A51"], [("algebra", "Primitive prime divisors of $a^n-b^n$ are primes $p$ for which $a/b$ has order exactly $n$ modulo $p$, so Zsigmondy is a statement about cyclotomic polynomials.")],
    ["AAF"], aliases=["LTE", "primitive prime divisor", "Bang"])
ext("binomial-factorial", "foundations", "Primes in factorials and binomial coefficients", "Factorials & binomials", ["p-adic-valuation"],
    r"Legendre's formula gives the exponent of $p$ in $n!$; Kummer's theorem says the exponent of $p$ in $\binom{m+n}{m}$ is the number of carries when $m$ and $n$ are added in base $p$.",
    [r"\nu_p(n!) = \sum_{k\ge1}\left\lfloor \frac{n}{p^k}\right\rfloor = \frac{n - s_p(n)}{p-1}"],
    "Integrality of factorial ratios, Chebyshev's bounds for primes and many Erdős problems all start here.",
    ["11B65", "05A10"], [("combinatorics", "Binomial coefficients count subsets; their arithmetic is a meeting point of the two subjects.")],
    ["NZM", "EG"], aliases=["Legendre's formula", "Kummer's theorem", "central binomial coefficient"], fields=["number-theory", "combinatorics"])
ext("integer-polynomials", "foundations", "Polynomials with integer coefficients", "Integer polynomials", ["divisibility", "congruences"],
    r"For $P \in \mathbb Z[x]$, $a-b \mid P(a)-P(b)$. This single fact, with factorisation, Gauss's lemma and the behaviour of roots modulo primes, drives most olympiad polynomial problems.",
    [r"a - b \mid P(a) - P(b)", r"\#\{t : P^{(k)}(t)=t\} \le \deg P \ \ (\deg P>1)"],
    "Polynomials are where algebra and number theory first share problems; the prime divisors of $P(n)$ lead to Chebotarev's density theorem.",
    ["11C08", "12D05"], [("algebra", "Irreducibility criteria and Gauss's lemma are ring theory in $\\mathbb Z[x]$.")],
    ["AAF"], aliases=["polynomial", "Schur's theorem on prime divisors"], fields=["number-theory", "algebra"])
ext("integer-functional-eq", "foundations", "Functional equations on the integers", "Integer functional equations", ["divisibility", "fta"],
    r"Find all $f:\mathbb Z\to\mathbb Z$ (or on $\mathbb N$, $\mathbb Q^+$) with a divisibility or multiplicative condition. Typical moves are plugging in primes, comparing valuations and proving $f$ is multiplicative.",
    [r"f(m)-f(n) \text{ divisible by } f(m-n)"],
    "They train the habit of extracting structure from a single identity, which is how characters and multiplicative functions are classified.",
    ["39B52", "11A25"], [("algebra", "Solutions are often group homomorphisms, for example from $(\\mathbb Q^+,\\times)$ to itself.")],
    ["Engel"], aliases=["functional equation", "bonza"], fields=["number-theory", "algebra"])

# ---- combinatorial & additive ----
ext("combinatorial-nt", "combinatorial", "Combinatorial number theory", "Combinatorial NT", ["divisibility", "fta"],
    r"Questions about sets of integers where the argument is a counting or extremal one: pigeonhole on residues or exponent vectors, double counting, and constructions.",
    [r"\text{among } n+1 \text{ integers in } [1,2n],\ \text{one divides another}"],
    "This is the native language of Erdős, and most of his problems below are stated in it.",
    ["11B75", "05D05"], [("combinatorics", "The methods are extremal combinatorics applied to arithmetic structure.")],
    ["EG", "Guy"], aliases=["extremal set", "pigeonhole"], fields=["number-theory", "combinatorics"])
ext("additive-combinatorics", "combinatorial", "Sumsets and additive combinatorics", "Additive combinatorics", ["combinatorial-nt", "fourier-poisson"],
    r"The study of $A+B = \{a+b\}$ for finite sets. Small doubling $|A+A| \le K|A|$ forces structure (Freiman), and Fourier analysis on $\mathbb Z/N$ measures how random a set is.",
    [r"|A+B| \ge \min(p,\ |A|+|B|-1) \ \text{in } \mathbb Z/p", r"|A+A| \le K|A| \Rightarrow A \subset \text{a generalised progression of size } O_K(|A|)"],
    "It connected number theory to ergodic theory and theoretical computer science, and produced the Green–Tao theorem.",
    ["11B13", "11P70", "05D99"], [("harmonic-analysis", "Roth's proof and its successors run on Fourier coefficients of indicator functions."), ("computer-science", "Property testing and pseudorandomness use the same inverse theorems.")],
    ["TV"], aliases=["sumset", "Freiman", "Cauchy–Davenport", "Plünnecke"], fields=["combinatorics", "number-theory", "harmonic-analysis"])
ext("ramsey-arithmetic", "combinatorial", "Arithmetic Ramsey theory", "Arithmetic Ramsey", ["combinatorial-nt"],
    r"Colour the integers with finitely many colours; some colour class contains a given structure. Schur: a monochromatic $x+y=z$. Van der Waerden: arbitrarily long monochromatic progressions. Rado: exactly which linear systems are partition regular.",
    [r"\forall\, r\ \exists\, N:\ [1,N] = C_1\cup\cdots\cup C_r \Rightarrow \exists i,\ x,y,z\in C_i,\ x+y=z"],
    "Colouring statements are the qualitative form of density statements, and the gap between the two is where most of the difficulty lies.",
    ["05D10", "11B25"], [("combinatorics", "These are Ramsey's theorem applied to arithmetic configurations."), ("logic", "Some Ramsey-type statements about integers are true but unprovable in Peano arithmetic (Paris–Harrington).")],
    ["GRS"], aliases=["Schur", "van der Waerden", "Rado", "colouring"], fields=["combinatorics", "number-theory"])
ext("arithmetic-progressions", "combinatorial", "Arithmetic progressions in dense sets", "Progressions", ["additive-combinatorics", "ramsey-arithmetic"],
    r"Szemerédi (1975): a set of positive upper density contains arbitrarily long progressions. Quantitative bounds for $r_k(N)$, the largest progression-free subset of $[1,N]$, are the active question; Green and Tao found long progressions in the primes.",
    [r"r_3(N) \le N \exp\!\big(-c(\log N)^{1/12}\big)\ \ \text{(Kelley–Meka 2023)}", r"\sum_{n\in A} \tfrac1n = \infty \overset{?}{\Rightarrow} A \text{ has arbitrarily long APs}"],
    "The Erdős–Turán problem (Erdős #3, a 5000-dollar prize) is the headline; an October 2026 AI-produced manuscript claims a bound strong enough to settle it.",
    ["11B25", "05D10"], [("dynamics", "Furstenberg proved Szemerédi's theorem by ergodic theory (multiple recurrence)."), ("ai-research", "Claimed quasipolynomial bounds from the October 2026 OpenAI release are still being checked.")],
    ["TV", "GRS"], aliases=["Szemerédi", "Roth", "Green–Tao", "Erdős–Turán", "r_k(N)"], fields=["combinatorics", "number-theory", "dynamics"])
ext("sidon-sets", "combinatorial", "Sidon sets", "Sidon sets", ["additive-combinatorics"],
    r"A set where all pairwise sums $a+b$ ($a\le b$) are distinct. In $[1,N]$ the maximum size is $\sqrt N + O(N^{1/4})$; whether the error is $O_\varepsilon(N^\varepsilon)$ is Erdős problem #30, with a 1000-dollar prize.",
    [r"\sqrt N \lesssim |A| \le \sqrt N + 0.998\,N^{1/4} \ \text{(Balogh–Füredi–Roy)}"],
    "Sidon sets are the simplest structure whose extremal size is still not known to the right order of error.",
    ["11B83", "05B10"], [("combinatorics", "They are the integer analogue of graphs with no 4-cycle, and finite-field constructions (Singer, Bose) are optimal."), ("computer-science", "Sidon sets give codes and hashing schemes with distinct pairwise sums.")],
    ["TV", "EG"], aliases=["B_2 sequence", "Golomb ruler"], fields=["combinatorics", "number-theory"])
ext("additive-bases", "combinatorial", "Additive bases and complete sequences", "Additive bases", ["additive-combinatorics"],
    r"$A$ is a basis of order $h$ if every large integer is a sum of $h$ elements of $A$; $A$ is complete if every large integer is a sum of distinct elements. Lagrange, Waring and Goldbach are statements of this kind.",
    [r"r_A(n) = \#\{(a,b)\in A^2 : a+b=n\}", r"\text{Erdős–Turán: } r_A(n)\ge1 \ \forall n \Rightarrow \limsup r_A(n) = \infty\ ?"],
    "It is the additive counterpart of factorisation: which sparse sets still generate everything.",
    ["11B13", "11P05"], [("combinatorics", "Probabilistic constructions (Erdős) give thin bases with $r_A(n) \\asymp \\log n$.")],
    ["TV", "EG"], aliases=["basis of order h", "complete sequence", "Erdős–Turán conjecture for bases"], fields=["number-theory", "combinatorics"])
ext("unit-fractions", "combinatorial", "Egyptian fractions", "Unit fractions", ["divisibility", "combinatorial-nt"],
    r"Writing rationals as sums of distinct $1/n$. Every rational has such representations; the questions are how short, how small the denominators, and which colourings or dense sets must contain a representation of $1$.",
    [r"\frac{4}{n} = \frac1x+\frac1y+\frac1z \ \ (\text{Erdős–Straus, open})", r"\text{any } r\text{-colouring of } \mathbb N \text{ has a monochromatic } \textstyle\sum 1/n_i = 1 \ \text{(Croot 2003)}"],
    "Bloom's 2021 density theorem, built on Croot's method, is a model of how analytic tools enter elementary-looking questions.",
    ["11D68"], [("combinatorics", "Croot's and Bloom's results are Ramsey- and density-type theorems for the equation $\\sum 1/n_i = 1$.")],
    ["Guy", "EG"], aliases=["Egyptian fraction", "Erdős–Straus"], fields=["number-theory", "combinatorics"])
ext("covering-systems", "combinatorial", "Covering systems", "Covering systems", ["crt", "combinatorial-nt"],
    r"A finite set of congruences $a_i \bmod n_i$ covering every integer, such as $0\bmod2,\ 0\bmod3,\ 1\bmod4,\ 5\bmod6,\ 7\bmod12$. Hough (2015) proved the smallest modulus of a covering with distinct moduli is bounded.",
    [r"\textstyle\bigcup_i \{x : x\equiv a_i \bmod n_i\} = \mathbb Z,\quad n_1<n_2<\cdots<n_k"],
    "Coverings produce Sierpiński numbers (odd $k$ with every $k2^n+1$ composite) and are a test case for the probabilistic method.",
    ["11B25", "11A07"], [("combinatorics", "Hough's proof and later work use the Lovász local lemma style of probabilistic argument.")],
    ["Guy", "EG"], aliases=["covering congruences", "Sierpiński number", "minimum modulus"], fields=["number-theory", "combinatorics"])
ext("primitive-sets", "combinatorial", "Primitive sets", "Primitive sets", ["combinatorial-nt", "mertens"],
    r"A set of integers $>1$ in which no element divides another. Erdős proved $\sum 1/(a\log a)$ is bounded over primitive sets and conjectured the primes maximise it; Lichtman proved this in 2022.",
    [r"\sum_{a\in A}\frac{1}{a\log a} \le \sum_{p}\frac{1}{p\log p} \ \ \text{(Lichtman 2022)}"],
    "It shows how a combinatorial condition (no divisibility) interacts with the multiplicative structure measured by Mertens-type sums.",
    ["11B83", "11N25"], [("combinatorics", "Primitive sets are antichains in the divisibility order.")],
    ["EG"], aliases=["antichain", "Erdős primitive set conjecture"], fields=["number-theory", "combinatorics"])
ext("discrepancy", "combinatorial", "Discrepancy", "Discrepancy", ["ramsey-arithmetic"],
    r"How evenly can a $\pm1$ sequence be balanced on a family of sets? Erdős asked whether $\sup_{n,d}|\sum_{k\le n} f(kd)|$ is unbounded for every $f:\mathbb N\to\{\pm1\}$; Tao proved it in 2015.",
    [r"\sup_{n,d}\Big|\sum_{k=1}^{n} f(kd)\Big| = \infty \ \ \text{(Tao 2015)}"],
    "Tao's proof combined the Polymath5 reduction to multiplicative functions, an entropy decrement argument and the Matomäki–Radziwiłł theorem on short averages.",
    ["11K38", "05D99"], [("combinatorics", "Discrepancy theory is a branch of combinatorics with roots in Weyl's equidistribution."), ("computer-science", "A SAT solver showed in 2014 that discrepancy $2$ is impossible beyond length $1160$.")],
    ["TV"], aliases=["Erdős discrepancy problem", "EDP"], fields=["combinatorics", "number-theory"])

# ---- analytic additions ----
ext("diophantine-approx", "analytic", "Diophantine approximation and irrationality", "Diophantine approximation", ["continued-fractions"],
    r"How well can a real number be approximated by $p/q$? Dirichlet gives $|\alpha - p/q| < 1/q^2$ infinitely often; Roth (1955) shows algebraic irrationals cannot do much better. Irrationality proofs (Apéry's $\zeta(3)$) are quantitative statements of this kind.",
    [r"\Big|\alpha-\frac pq\Big| < \frac{1}{q^{2+\varepsilon}} \ \text{has finitely many solutions for algebraic } \alpha \ \text{(Roth)}"],
    "Transcendence, the abc conjecture and the irrationality of zeta values all reduce to how small a linear form in numbers can be.",
    ["11J68", "11J72"], [("dynamics", "Badly approximable numbers are bounded orbits of the geodesic flow on the modular surface.")],
    ["HW", "Bugeaud"], aliases=["irrationality", "Roth's theorem", "Liouville", "Apéry"], fields=["number-theory", "real-analysis"])
ext("smooth-powerful", "analytic", "Smooth, powerful and squarefree numbers", "Smooth & powerful numbers", ["fta", "asymptotics"],
    r"$n$ is $y$-smooth if all its prime factors are $\le y$, powerful if $p\mid n \Rightarrow p^2 \mid n$, squarefree if no $p^2$ divides it. Their counts are governed by Dickman's function, $\zeta(3/2)/\zeta(3)\cdot\sqrt x$ and $6x/\pi^2$.",
    [r"\Psi(x, x^{1/u}) \sim \rho(u)\,x", r"\#\{n\le x \text{ squarefree}\} \sim \frac{6}{\pi^2}x"],
    "Smooth numbers are the engine of the fastest factoring algorithms; powerful numbers are where the abc conjecture bites.",
    ["11N25"], [("cryptography", "The quadratic and number field sieves factor by collecting smooth values."), ("computer-science", "Running times of index-calculus algorithms are $L$-functions of smoothness probabilities.")],
    ["Tenenbaum", "CP"], aliases=["Dickman", "squarefree", "abc", "friable"])
ext("prime-patterns", "analytic", "Primes in sequences and gaps", "Prime patterns", ["pnt", "sieve-basics"],
    r"Which sequences contain infinitely many primes, how large gaps between consecutive primes can be, and how often primes fall in short intervals. Most such questions are open; sieves and the circle method give the partial results.",
    [r"\limsup \frac{p_{n+1}-p_n}{\log p_n} = \infty \ \text{(Westzynthius 1931)}", r"\max_{p_n\le x}(p_{n+1}-p_n) \gg \frac{\log x\,\log\log x\,\log\log\log\log x}{\log\log\log x}\ \text{(Ford–Green–Konyagin–Maynard–Tao)}"],
    "Large gaps are built by covering an interval with residue classes, so this topic shares a toolkit with covering systems.",
    ["11N05", "11N13"], [("combinatorics", "Large-gap constructions use hypergraph covering lemmas (Rödl nibble).")],
    ["Guy", "FI"], aliases=["prime gaps", "large gaps", "primes of the form"])
ext("probabilistic-nt", "analytic", "Probabilistic number theory", "Probabilistic NT", ["arithmetic-functions", "pnt"],
    r"Arithmetic functions behave like sums of independent random variables. Erdős–Kac: $\omega(n)$, the number of prime factors, is normally distributed with mean and variance $\log\log n$.",
    [r"\frac{1}{x}\#\Big\{n\le x : \frac{\omega(n)-\log\log n}{\sqrt{\log\log n}} \le t\Big\} \to \Phi(t)"],
    "It turned heuristics such as Cramér's model of the primes into theorems where it could, and tells you what to expect where it cannot.",
    ["11K65", "11N37"], [("probability", "The proofs are moment and characteristic-function arguments from probability theory.")],
    ["Tenenbaum"], aliases=["Erdős–Kac", "Turán–Kubilius", "normal order"], fields=["number-theory", "probability"])

# Wire some existing concepts to the new ones.
next(c for c in C if c['id'] == 'divisibility')['short'] = 'Divisibility & gcd'
def con(i): return next(c for c in C if c["id"] == i)
con("bounded-gaps")["pre"].append("prime-patterns")

# ---- events for the new concepts ----
EVENTS.extend([
    dict(id="legendre", y=1808, label="1808", title="Legendre's formula for $\\nu_p(n!)$", who="Adrien-Marie Legendre", text=r"The exponent of $p$ in $n!$ is $\sum_k \lfloor n/p^k\rfloor$.", nodes=["binomial-factorial"]),
    dict(id="kummer", y=1852, label="1852", title="Kummer's carries theorem", who="Ernst Kummer", text=r"$\nu_p\binom{m+n}{m}$ counts the carries in adding $m$ and $n$ in base $p$.", nodes=["binomial-factorial", "digits-bases"]),
    dict(id="zsigmondy", y=1892, label="1892", title="Primitive prime divisors", who="Karl Zsigmondy", text=r"$a^n-b^n$ has a prime factor dividing no earlier $a^k-b^k$, apart from a short list of exceptions.", nodes=["lte-zsigmondy"]),
    dict(id="schur", y=1916, label="1916", title="Schur's theorem", who="Issai Schur", text=r"Every finite colouring of $\mathbb N$ has a monochromatic solution of $x+y=z$, found while studying Fermat's equation modulo $p$.", nodes=["ramsey-arithmetic"]),
    dict(id="vdw", y=1927, label="1927", title="Van der Waerden's theorem", who="B. L. van der Waerden", text=r"Every finite colouring of $\mathbb N$ contains arbitrarily long monochromatic arithmetic progressions.", nodes=["ramsey-arithmetic", "arithmetic-progressions"]),
    dict(id="sidon", y=1932, label="1932", title="Sidon's question", who="Simon Sidon", text=r"Asked Erdős how dense a set with distinct pairwise sums can be, in work on Fourier series.", nodes=["sidon-sets"]),
    dict(id="erdos-turan", y=1936, label="1936", title="Erdős and Turán on progressions", who="Paul Erdős, Pál Turán", text=r"Conjectured that dense sets contain long progressions, the problem Szemerédi solved and whose reciprocal-sum form is Erdős #3.", nodes=["arithmetic-progressions"]),
    dict(id="erdos-kac", y=1940, label="1940", title="The Erdős–Kac theorem", who="Paul Erdős, Mark Kac", text=r"$\omega(n)$ is asymptotically normal with mean and variance $\log\log n$.", nodes=["probabilistic-nt"]),
    dict(id="covering", y=1950, label="1950", title="Covering systems introduced", who="Paul Erdős", text=r"Used a covering of $\mathbb Z$ by congruences to show a positive proportion of odd numbers are not $2^k+p$.", nodes=["covering-systems"]),
    dict(id="roth-ap", y=1953, label="1953", title="Roth's theorem on 3-term progressions", who="Klaus Roth", text=r"Dense sets contain $3$-term progressions, by Fourier analysis on $\mathbb Z/N$.", nodes=["arithmetic-progressions", "additive-combinatorics"]),
    dict(id="roth-approx", y=1955, label="1955", title="Roth's approximation theorem", who="Klaus Roth", text=r"Algebraic irrationals have approximation exponent exactly $2$; Fields Medal 1958.", nodes=["diophantine-approx"]),
    dict(id="szemeredi", y=1975, label="1975", title="Szemerédi's theorem", who="Endre Szemerédi", text=r"Every set of positive density contains arbitrarily long progressions.", nodes=["arithmetic-progressions"]),
    dict(id="vieta-1988", y=1988.5, label="1988", title="IMO 1988 Problem 6", who="Proposed by West Germany", text=r"No member of the problem committee solved it in the allotted time; it popularised Vieta jumping.", nodes=["vieta-jumping"]),
    dict(id="croot", y=2003, label="2003", title="Monochromatic Egyptian fractions", who="Ernie Croot", text=r"Any finite colouring of the integers has a monochromatic set with $\sum 1/n = 1$.", nodes=["unit-fractions"]),
    dict(id="green-tao", y=2004, label="2004", title="The primes contain arbitrarily long progressions", who="Ben Green, Terence Tao", text=r"A relative Szemerédi theorem applied to a pseudorandom majorant of the primes.", nodes=["arithmetic-progressions", "prime-patterns"]),
    dict(id="hough", y=2015, label="2015", title="Minimum modulus of covering systems is bounded", who="Bob Hough", text=r"Settled Erdős's minimum modulus problem negatively: distinct-moduli coverings have least modulus at most $10^{16}$.", nodes=["covering-systems"]),
    dict(id="tao-edp", y=2015.7, label="2015", title="The Erdős discrepancy problem", who="Terence Tao", text=r"Proved $\sup|\sum_{k\le n} f(kd)| = \infty$ for every $\pm1$ sequence, building on Polymath5.", nodes=["discrepancy"]),
    dict(id="lichtman", y=2022, label="2022", title="Erdős primitive set conjecture", who="Jared Duker Lichtman", text=r"The primes maximise $\sum 1/(a\log a)$ over primitive sets.", nodes=["primitive-sets"]),
    dict(id="kelley-meka", y=2023, label="2023", title="Strong bounds for 3-progressions", who="Zander Kelley, Raghu Meka", text=r"$r_3(N) \le N\exp(-c(\log N)^{1/12})$, close to Behrend's construction.", nodes=["arithmetic-progressions"]),
    dict(id="bloom-23", y=2026.766, label="8 Oct 2026", ai=True, title="23 Erdős problems in the OpenAI release", who="Thomas Bloom (erdosproblems.com)", text=r"Bloom listed the release's claims touching Erdős problems, including #3 via a 198-page quasipolynomial bound for Szemerédi's theorem whose Lean file proves only a weaker statement. He called it a summary of claims, not an endorsement.", nodes=["arithmetic-progressions", "additive-combinatorics"], url="https://officechai.com/ai/openai-has-also-included-proofs-for-23-erdos-problems-in-its-latest-math-proof-drop/", src="OfficeChai"),
])
for e in EVENTS:
    if e["id"] == "release": e["title"] = "372 proof claims released; Siegel zeros excluded"

for c in C:
    band = next(b for b in BANDS if b["id"] == c["band"])
    c["fields"] = OWN.get(c["id"], band["fields"][:1] if band["id"] != "combinatorial" else band["fields"])

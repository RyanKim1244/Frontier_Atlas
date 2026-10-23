import json

def R(title, kind, q, concepts, source, bridges, note, year=None):
    d = {"title": title, "kind": kind, "q": q, "concepts": concepts, "source": source}
    if year is not None:
        d["year"] = year
    d["bridges_to"] = bridges
    d["note"] = note
    return d

prime = [
 R("Bertrand's postulate", "classic",
   r"""Prove that for every integer $n\ge 1$ there is a prime $p$ with $n<p\le 2n$. Deduce that $p_{n+1}<2p_n$ for every $n\ge 1$, where $p_n$ denotes the $n$th prime.""",
   ["prime-patterns", "binomial-factorial", "fta"],
   "Aigner & Ziegler, Proofs from THE BOOK, Chapter 2 (Bertrand's postulate)", [],
   "The first unconditional upper bound for prime gaps, proved by elementary estimates on the central binomial coefficient."),
 R("Average size and second moment of prime gaps", "classic",
   r"""Let $d_n=p_{n+1}-p_n$. Assuming the prime number theorem in the form $p_n\sim n\log n$, prove:

(a) for every $\varepsilon>0$ there are infinitely many $n$ with $d_n>(1-\varepsilon)\log p_n$ and infinitely many $n$ with $d_n<(1+\varepsilon)\log p_n$;

(b) $\sum_{n\le N} d_n^2\gg N(\log N)^2$ for all large $N$.""",
   ["prime-patterns", "pnt", "cauchy-schwarz", "asymptotics"],
   "Folklore consequences of the prime number theorem; the lower bound in (b) is recorded at erdosproblems.com/233 (Erdős Problem #233)", ["ERDOS-233"],
   "Fixes the natural scale $\\log p_n$ for gaps; (b) is the trivial lower bound matching Heath-Brown's conjectured upper bound $N(\\log N)^2$."),
 R("Westzynthius: gaps are unboundedly larger than average", "theorem",
   r"""Let $p_n$ denote the $n$th prime. Prove that
$$\limsup_{n\to\infty}\frac{p_{n+1}-p_n}{\log p_n}=\infty.$$""",
   ["prime-patterns", "crt", "sieve-basics", "pnt"],
   "E. Westzynthius, Über die Verteilung der Zahlen, die zu den n ersten Primzahlen teilerfremd sind, Societas Scientiarum Fennica, Commentationes Physico-Mathematicae 5 (1931), no. 25", ["ERDOS-5"],
   "Shows that $\\infty$ is a limit point of the normalized gaps, via long runs of integers each sharing a factor with the primorial.", 1931),
 R("Rankin's lower bound for large gaps", "theorem",
   r"""Prove that there is a constant $c>0$ such that
$$p_{n+1}-p_n>c\,\frac{\log p_n\,\log\log p_n\,\log\log\log\log p_n}{(\log\log\log p_n)^2}$$
for infinitely many $n$.""",
   ["prime-patterns", "crt", "smooth-powerful", "sieve-basics"],
   "R. A. Rankin, The difference between consecutive prime numbers, J. London Math. Soc. 13 (1938)", ["ERDOS-4", "GREEN-46"],
   "The Erdős–Rankin method: cover an interval by one residue class per small prime, using smooth numbers to handle the hardest part; Erdős Problem 4 asks to make $c$ arbitrarily large.", 1938),
 R("Long gaps between primes (Ford–Green–Konyagin–Maynard–Tao)", "theorem",
   r"""Prove that for all sufficiently large $X$,
$$\max_{p_n\le X}(p_{n+1}-p_n)\gg\frac{\log X\,\log\log X\,\log\log\log\log X}{\log\log\log X}.$$""",
   ["prime-patterns", "crt", "bounded-gaps", "probabilistic-method", "sieve-basics"],
   "K. Ford, B. Green, S. Konyagin, J. Maynard, T. Tao, Long gaps between primes, J. Amer. Math. Soc. 31 (2018), 65–105", ["ERDOS-4", "GREEN-46"],
   "Gains a factor $\\log\\log\\log X$ over Rankin (settling Erdős Problem 4 in a strong form) by combining the covering argument with Maynard's sieve weights; improving it further is the residue-class covering question of Green's Problem 46.", 2018),
 R("Goldston–Pintz–Yıldırım: small normalized gaps", "theorem",
   r"""Prove that
$$\liminf_{n\to\infty}\frac{p_{n+1}-p_n}{\log p_n}=0.$$""",
   ["prime-patterns", "bounded-gaps", "bombieri-vinogradov", "selberg-sieve"],
   "D. A. Goldston, J. Pintz, C. Y. Yıldırım, Primes in tuples I, Ann. of Math. (2) 170 (2009), 819–862", ["ERDOS-5"],
   "Shows that $0$ is a limit point of the normalized gaps, the case $C=0$ of Erdős Problem 5 (normalizing by $\\log n$ or $\\log p_n$ is equivalent).", 2009),
 R("Bounded gaps between primes (Maynard)", "theorem",
   r"""Prove that for every integer $m\ge 1$ there is a constant $C_m$ such that $p_{n+m}-p_n\le C_m$ for infinitely many $n$. In particular show that $p_{n+1}-p_n\le 600$ for infinitely many $n$.""",
   ["prime-patterns", "bounded-gaps", "bombieri-vinogradov", "selberg-sieve"],
   "J. Maynard, Small gaps between primes, Ann. of Math. (2) 181 (2015), 383–413", ["ERDOS-6"],
   "Multidimensional sieve weights give many primes in a single admissible tuple, which is the engine behind the solution of Erdős Problem 6 and the later rungs.", 2015),
 R("Monotone runs of prime gaps", "theorem",
   r"""Let $d_n=p_{n+1}-p_n$. Prove that for every $m\ge 1$ there are infinitely many $n$ with $d_n<d_{n+1}<\cdots<d_{n+m}$, and infinitely many $n$ with $d_n>d_{n+1}>\cdots>d_{n+m}$.""",
   ["prime-patterns", "bounded-gaps"],
   "W. D. Banks, T. Freiberg, C. L. Turnage-Butterbaugh, Consecutive primes in tuples, Acta Arith. 167 (2015), no. 3", ["ERDOS-6", "ERDOS-852"],
   "Upgrades Maynard's theorem to control which members of a tuple are consecutive primes, settling the Erdős–Turán question (Erdős Problem 6); the same control over consecutive gaps is what Problems 852–853 ask about.", 2015),
 R("A positive proportion of limit points of normalized gaps", "theorem",
   r"""Let $L$ be the set of limit points in $[0,\infty)$ of the sequence $(p_{n+1}-p_n)/\log p_n$. Prove that for any nine real numbers $0\le\beta_1\le\beta_2\le\cdots\le\beta_9$, at least one difference $\beta_j-\beta_i$ with $1\le i<j\le 9$ lies in $L$. Deduce that the Lebesgue measure of $L\cap[0,T]$ is at least $T/8$ for every $T>0$.""",
   ["prime-patterns", "bounded-gaps", "lebesgue"],
   "W. D. Banks, T. Freiberg, J. Maynard, On limit points of the sequence of normalized prime gaps, Proc. London Math. Soc. (2016), arXiv:1404.5094", ["ERDOS-5", "ERDOS-234"],
   "The strongest type of result towards Erdős Problem 5 (whether every $C\\ge0$ is a limit point); Merikoski (arXiv:1811.03008) later improved the proportion to $1/3$ and showed $L$ has bounded gaps.", 2016),
 R("Strings of consecutive primes in one residue class (Shiu)", "theorem",
   r"""Let $q\ge 1$ and $a$ be integers with $\gcd(a,q)=1$, and let $k\ge 1$. Prove that there are infinitely many $r$ such that the $k$ consecutive primes $p_{r+1},p_{r+2},\ldots,p_{r+k}$ are all congruent to $a$ modulo $q$.""",
   ["prime-patterns", "l-functions", "sieve-basics", "congruences"],
   "D. K. L. Shiu, Strings of congruent primes, J. London Math. Soc. (2) 61 (2000)", ["ERDOS-427", "ERDOS-141"],
   "Directly answers Erdős Problem 427 (choose a string of $d$ consecutive primes $\\equiv1\\bmod d$); it is the nearest proven statement to finding consecutive primes in arithmetic progression (Problem 141), where the differences, not just the residues, must be fixed.", 2000),
]

smooth = [
 R("Counting squarefree numbers", "classic",
   r"""Let $Q(x)$ be the number of squarefree positive integers $n\le x$. Prove that
$$Q(x)=\frac{6}{\pi^2}x+O(\sqrt{x}).$$""",
   ["smooth-powerful", "mobius", "zeta", "asymptotics"],
   "Hardy & Wright, An Introduction to the Theory of Numbers, Ch. XVIII", [],
   "The model computation: write the indicator of squarefree numbers as $\\sum_{d^2\\mid n}\\mu(d)$ and sum."),
 R("No two elements with square product", "theorem",
   r"""For $N\ge1$ let $F_2(N)$ be the largest size of a set $A\subseteq\{1,\ldots,N\}$ such that $ab$ is not a perfect square for any two distinct $a,b\in A$. Prove that $F_2(N)$ equals the number of squarefree integers in $\{1,\ldots,N\}$, so that $F_2(N)\sim\frac{6}{\pi^2}N$.""",
   ["smooth-powerful", "pigeonhole", "combinatorial-nt"],
   "P. Erdős, A. Sárközy, V. T. Sós, On product representations of powers, I, European J. Combin. 16 (1995), 567–588", ["ERDOS-121"],
   "The case $k=2$ of the function $F_k(N)$ in Erdős Problem 121: square classes (squarefree kernels) are the right bookkeeping.", 1995),
 R("Structure and count of powerful numbers", "classic",
   r"""Call $n\ge1$ powerful if $p\mid n$ implies $p^2\mid n$ for every prime $p$. Prove that every powerful $n$ can be written uniquely as $n=a^2b^3$ with $a,b$ positive integers and $b$ squarefree. Deduce that the number $P(x)$ of powerful $n\le x$ satisfies
$$P(x)=\frac{\zeta(3/2)}{\zeta(3)}\sqrt{x}+O(x^{1/3}).$$""",
   ["smooth-powerful", "fta", "zeta", "asymptotics"],
   "S. W. Golomb, Powerful numbers, Amer. Math. Monthly 77 (1970), 848–852; the asymptotic goes back to P. Erdős and G. Szekeres, Acta Sci. Math. (Szeged) 7 (1934), 95–102", [],
   "Gives the density of powerful numbers (about $\\sqrt{x}$ of them up to $x$), the heuristic baseline for every question about consecutive or additive patterns of powerful numbers.", 1970),
 R("Consecutive powerful numbers", "classic",
   r"""(a) Prove that there are no four consecutive positive integers that are all powerful.

(b) Prove that there are infinitely many positive integers $n$ such that $n$ and $n+1$ are both powerful.""",
   ["smooth-powerful", "pell", "congruences"],
   "S. W. Golomb, Powerful numbers, Amer. Math. Monthly 77 (1970), 848–852", ["ERDOS-364"],
   "Pairs are plentiful via Pell equations and quadruples are impossible mod 4; triples (Erdős Problem 364) sit exactly between what is easy in both directions.", 1970),
 R("Smooth numbers with one large prime factor", "classic",
   r"""Let $\Psi(x,y)$ be the number of $n\le x$ all of whose prime factors are at most $y$. Using Mertens' theorem, prove that for each fixed $u\in[1,2]$,
$$\Psi(x,x^{1/u})=(1-\log u)\,x+O\Big(\frac{x}{\log x}\Big)\quad(x\to\infty).$$""",
   ["smooth-powerful", "mertens", "asymptotics"],
   "Tenenbaum, Introduction to Analytic and Probabilistic Number Theory, Ch. III.5", [],
   "Computes Dickman's function on $[1,2]$, where $\\rho(u)=1-\\log u$, by an inclusion-exclusion that uses only one large prime factor."),
 R("Consecutive powerful numbers, neither a square", "theorem",
   r"""Prove that there are infinitely many positive integers $n$ such that $n$ and $n+1$ are both powerful and neither $n$ nor $n+1$ is a perfect square.""",
   ["smooth-powerful", "pell", "quadratic-forms"],
   "D. T. Walker, Consecutive integer pairs of powerful numbers and related Diophantine equations, Fibonacci Quart. 14 (1976), 111–116", ["ERDOS-365"],
   "Gives infinitely many counterexamples to part (a) of Erdős Problem 365 (Golomb had found $23^3$, $23^3+1$); part (b), the $(\\log x)^{O(1)}$ count, remains open.", 1976),
 R("Dickman's theorem", "theorem",
   r"""Let $\rho:(0,\infty)\to\mathbb{R}$ be the continuous function with $\rho(u)=1$ for $0<u\le1$ and $u\rho'(u)=-\rho(u-1)$ for $u>1$. Prove that for each fixed $u\ge1$,
$$\Psi(x,x^{1/u})\sim\rho(u)\,x\quad(x\to\infty).$$""",
   ["smooth-powerful", "mertens", "pnt", "asymptotics"],
   "K. Dickman, On the frequency of numbers containing prime factors of a certain relative magnitude, Ark. Mat. Astr. Fys. 22A (1930)", [],
   "Extends the previous rung to all $u$ by an integral-delay recursion; smooth-number counts like this drive the large-gap constructions in prime-patterns.", 1930),
 R("Products of consecutive integers are never powers (Erdős–Selfridge)", "theorem",
   r"""Prove that for integers $n\ge1$, $k\ge2$ and $\ell\ge2$, the product $n(n+1)\cdots(n+k-1)$ is never an $\ell$th power of an integer.""",
   ["smooth-powerful", "binomial-factorial", "diophantine"],
   "P. Erdős, J. L. Selfridge, The product of consecutive integers is never a power, Illinois J. Math. 19 (1975), 292–301", ["ERDOS-137"],
   "Erdős Problem 137 asks for the much weaker conclusion 'never powerful' for $k\\ge3$, which is open even though 'never a perfect power' is known.", 1975),
 R("Coprime arithmetic progressions of powerful numbers", "theorem",
   r"""Prove that there are infinitely many pairs of positive integers $(N,d)$ with $\gcd(N,d)=1$ such that $N,N+d,N+2d,N+3d$ are all powerful. Prove also that there are infinitely many such pairs with $\gcd(N,d)=1$ for which $N,N+d,N+2d$ are all $3$-full (every prime factor occurs to at least the third power).""",
   ["smooth-powerful", "arithmetic-progressions", "diophantine", "pell"],
   "P. Bajpai, M. A. Bennett, T. H. Chan, Arithmetic progressions in squarefull numbers, Int. J. Number Theory (2024), arXiv:2302.03113", ["ERDOS-937"],
   "Resolves Erdős Problem 937; without coprimality the problem is trivial (scale any progression by a suitable square), and the same paper shows under abc that these lengths are optimal.", 2024),
 R("Five elements with square product (Tao)", "theorem",
   r"""For $N\ge1$ let $F_5(N)$ be the largest size of a set $A\subseteq\{1,\ldots,N\}$ such that no product of five distinct elements of $A$ is a perfect square. Prove that there is a constant $c>0$ such that $F_5(N)\le(1-c+o(1))N$ as $N\to\infty$.""",
   ["smooth-powerful", "probabilistic-method", "combinatorial-nt"],
   "T. Tao, On product representations of squares, arXiv:2405.11610 (2024)", ["ERDOS-121"],
   "Answers Erdős Problem 121 in the negative (the conjecture was $F_5(N)=(1-o(1))N$), contrasting with $F_3(N)=(1-o(1))N$ proved by Erdős–Sárközy–Sós.", 2024),
]

dioph = [
 R("Dirichlet's approximation theorem", "classic",
   r"""Let $\alpha$ be an irrational real number. Prove that there are infinitely many pairs of integers $(p,q)$ with $q\ge1$ such that
$$\Big|\alpha-\frac{p}{q}\Big|<\frac{1}{q^2}.$$""",
   ["diophantine-approx", "pigeonhole", "continued-fractions"],
   "Hardy & Wright, An Introduction to the Theory of Numbers, Ch. XI", [],
   "The baseline exponent $2$ that every later rung either improves on (for special numbers) or shows to be essentially optimal."),
 R("Liouville's inequality", "classic",
   r"""Let $\alpha$ be a real algebraic number of degree $d\ge2$. Prove that there is a constant $c(\alpha)>0$ such that
$$\Big|\alpha-\frac{p}{q}\Big|>\frac{c(\alpha)}{q^d}$$
for all integers $p$ and $q\ge1$. Deduce that $\sum_{n\ge1}10^{-n!}$ is transcendental.""",
   ["diophantine-approx", "polynomials-roots", "mvt"],
   "Hardy & Wright, An Introduction to the Theory of Numbers, Ch. XI", [],
   "The basic mechanism of irrationality and transcendence proofs: a number with too-good rational approximations cannot be rational or algebraic of low degree."),
 R("Khintchine's theorem", "theorem",
   r"""For real $x$ let $\|x\|$ be the distance from $x$ to the nearest integer. Let $\psi:\mathbb{N}\to[0,\infty)$ be non-increasing. Prove that if $\sum_{q\ge1}\psi(q)<\infty$ then for almost every $\alpha\in\mathbb{R}$ the inequality $\|q\alpha\|<\psi(q)$ has only finitely many solutions $q\in\mathbb{N}$, while if $\sum_{q\ge1}\psi(q)=\infty$ then for almost every $\alpha$ it has infinitely many solutions.""",
   ["diophantine-approx", "lebesgue", "continued-fractions"],
   "A. Khintchine, Einige Sätze über Kettenbrüche, mit Anwendungen auf die Theorie der Diophantischen Approximationen, Math. Ann. 92 (1924)", ["ERDOS-999"],
   "The convergence half is Borel–Cantelli; the divergence half needs monotonicity, and removing it (with coprimality) is exactly the Duffin–Schaeffer problem.", 1924),
 R("Irrationality of the Lambert series at 1/2 (Erdős)", "theorem",
   r"""Prove that
$$\sum_{n\ge1}\frac{1}{2^n-1}=\sum_{n\ge1}\frac{\tau(n)}{2^n}$$
is irrational, where $\tau(n)$ is the number of divisors of $n$.""",
   ["diophantine-approx", "arithmetic-functions", "digits-bases", "series"],
   "P. Erdős, On arithmetical properties of Lambert series, J. Indian Math. Soc. (N.S.) 12 (1948), 63–66", ["ERDOS-257", "ERDOS-1049"],
   "The case $A=\\mathbb{N}$ of Erdős Problem 257 and the case $t=2$ of Problem 1049: the binary expansion of the sum is controlled by the divisor function.", 1948),
 R("Borwein's irrationality of q-harmonic type series", "theorem",
   r"""Let $q\ge2$ be an integer and $r\ne0$ a rational number with $r\ne-q^n$ for all $n\ge1$. Prove that
$$\sum_{n\ge1}\frac{1}{q^n+r}$$
is irrational.""",
   ["diophantine-approx", "series", "integer-polynomials"],
   "P. B. Borwein, On the irrationality of Σ 1/(q^n+r), J. Number Theory 37 (1991), 253–259", ["ERDOS-1050", "ERDOS-1049"],
   "Settles Erdős Problem 1050 ($q=2$, $r=-3$) and the integer-$t$ case of Problem 1049 via Padé approximation; the rational non-integer $t$ case of 1049 stays open.", 1991),
 R("Roth's theorem", "theorem",
   r"""Let $\alpha$ be a real algebraic irrational number and $\varepsilon>0$. Prove that there are only finitely many pairs of integers $(p,q)$ with $q\ge1$ such that
$$\Big|\alpha-\frac{p}{q}\Big|<\frac{1}{q^{2+\varepsilon}}.$$""",
   ["diophantine-approx", "polynomials-roots"],
   "K. F. Roth, Rational approximations to algebraic numbers, Mathematika 2 (1955), 1–20", [],
   "Shows Dirichlet's exponent $2$ is sharp for every algebraic irrational, improving Liouville's $d$ all the way down.", 1955),
 R("Littlewood's conjecture for cubic fields (Cassels–Swinnerton-Dyer)", "theorem",
   r"""For real $x$ let $\|x\|$ be the distance from $x$ to the nearest integer. Let $K$ be a real cubic number field and let $\alpha,\beta\in K$ be such that $1,\alpha,\beta$ are linearly independent over $\mathbb{Q}$. Prove that
$$\liminf_{n\to\infty}n\,\|n\alpha\|\,\|n\beta\|=0.$$""",
   ["diophantine-approx", "ideals", "quadratic-forms"],
   "J. W. S. Cassels, H. P. F. Swinnerton-Dyer, On the product of three homogeneous linear forms and indefinite ternary quadratic forms, Philos. Trans. Roy. Soc. London Ser. A 248 (1955), 73–96", ["ERDOS-495"],
   "Littlewood's conjecture is trivial unless both $\\alpha,\\beta$ are badly approximable; cubic pairs are the most natural such pairs, and this is the case proved.", 1955),
 R("The Duffin–Schaeffer conjecture (Koukoulopoulos–Maynard)", "theorem",
   r"""Let $\psi:\mathbb{N}\to[0,\infty)$ be any function and let $\varphi$ be Euler's totient function. Prove that for almost every $\alpha\in\mathbb{R}$ the inequality
$$\Big|\alpha-\frac{a}{q}\Big|<\frac{\psi(q)}{q}$$
has infinitely many solutions in integers $a,q$ with $q\ge1$ and $\gcd(a,q)=1$ if and only if $\sum_{q\ge1}\varphi(q)\psi(q)/q=\infty$.""",
   ["diophantine-approx", "lebesgue", "arithmetic-functions", "probabilistic-method"],
   "D. Koukoulopoulos, J. Maynard, On the Duffin–Schaeffer conjecture, Ann. of Math. (2) 192 (2020), 251–307", ["ERDOS-999"],
   "Removes the monotonicity hypothesis from Khintchine's theorem (with reduced fractions), resolving Erdős Problem 999.", 2020),
 R("Exceptions to Littlewood have dimension zero (Einsiedler–Katok–Lindenstrauss)", "theorem",
   r"""For real $x$ let $\|x\|$ be the distance from $x$ to the nearest integer. Prove that the set of pairs $(\alpha,\beta)\in\mathbb{R}^2$ with
$$\liminf_{n\to\infty}n\,\|n\alpha\|\,\|n\beta\|>0$$
has Hausdorff dimension $0$.""",
   ["diophantine-approx", "lebesgue"],
   "M. Einsiedler, A. Katok, E. Lindenstrauss, Invariant measures and the set of exceptions to Littlewood's conjecture, Ann. of Math. (2) 164 (2006), 513–560", ["ERDOS-495"],
   "The strongest known result toward the Littlewood conjecture (Erdős Problem 495), obtained by measure rigidity for diagonal actions on $\\mathrm{SL}_3(\\mathbb{R})/\\mathrm{SL}_3(\\mathbb{Z})$.", 2006),
 R("Irrationality of the sum over primes (Tao–Teräväinen)", "theorem",
   r"""Let $\omega(n)$ be the number of distinct prime factors of $n$. Prove that
$$\sum_{n\ge2}\frac{\omega(n)}{2^n}=\sum_{p\ \mathrm{prime}}\frac{1}{2^p-1}$$
(verify this identity first) and that this number is irrational.""",
   ["diophantine-approx", "arithmetic-functions", "prime-patterns", "probabilistic-nt"],
   "T. Tao, J. Teräväinen, Quantitative correlations and some problems on prime factors of consecutive integers, arXiv:2512.01739 (2025)", ["ERDOS-69", "ERDOS-257"],
   "Settles Erdős Problem 69 and the case $A=$ primes of Problem 257, extending Erdős's $A=\\mathbb{N}$ rung; it needs correlation estimates for $\\omega(n)$ and $\\omega(n+h)$ in place of the divisor-function structure.", 2025),
]

out = [
 {"concept": "prime-patterns", "ladder": prime},
 {"concept": "smooth-powerful", "ladder": smooth},
 {"concept": "diophantine-approx", "ladder": dioph},
]

concepts = {c["id"] for c in json.load(open("all_concepts.json"))}
brief = json.load(open("brief_4.json"))
assert [b["id"] for b in brief] == [o["concept"] for o in out]
for b, o in zip(brief, out):
    rp = {r["id"] for r in b["research_problems"]}
    assert 6 <= len(o["ladder"]) <= 10, (o["concept"], len(o["ladder"]))
    for r in o["ladder"]:
        for c in r["concepts"]:
            assert c in concepts, c
        assert o["concept"] in r["concepts"]
        for x in r["bridges_to"]:
            assert x in rp, (o["concept"], x)
        for k in ("q", "title", "note"):
            assert r[k].count("$") % 2 == 0, (r["title"], k)
        assert r["kind"] in ("classic", "theorem", "special-case")
json.dump(out, open("ladder_4.json", "w"), ensure_ascii=False, indent=1)
print([len(o["ladder"]) for o in out])

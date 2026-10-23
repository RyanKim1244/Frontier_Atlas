# Problem banks. Generated problems compute their own answers; hand-written ones are checked in build.py.
import math, random
from fractions import Fraction as F
import numpy as np
import sympy as sp
import mpmath as mp

def fill(_tpl, **kw):
    for k, v in kw.items():
        _tpl = _tpl.replace("<<" + k + ">>", str(v))
    return _tpl

def frac_tex(x):
    x = F(x)
    if x.denominator == 1:
        return str(x.numerator)
    s = "-" if x < 0 else ""
    return s + r"\frac{%d}{%d}" % (abs(x.numerator), x.denominator)

BANK = {}
def add(cid, p):
    BANK.setdefault(cid, []).append(p)

def P(t, d, q, a=None, ex="", hint="", tol=None, opts=None, src="generated"):
    p = {"t": t, "d": d, "q": q, "src": src}
    if a is not None:
        if isinstance(a, sp.Basic):
            a = int(a) if a.is_Integer else F(int(a.p), int(a.q)) if a.is_Rational else float(a)
        if isinstance(a, np.integer): a = int(a)
        if isinstance(a, F):
            p["a"] = float(a); p["exact"] = [a.numerator, a.denominator]
        elif isinstance(a, int):
            p["a"] = a; p["exact"] = [a, 1]
        else:
            p["a"] = float(a)
            if tol is None and float(a).is_integer(): p["exact"] = [int(a), 1]
    if tol is not None: p["tol"] = tol
    if opts is not None: p["opts"] = opts
    if hint: p["hint"] = hint
    if ex: p["ex"] = ex
    return p

def H(t, d, q, a=None, ex="", hint="", tol=None, opts=None):
    return P(t, d, q, a, ex, hint, tol, opts, src="original")

R = random.Random(20261023)
primes_small = list(sp.primerange(3, 200))

# ---------------- generators ----------------
def gen():
    # divisibility
    for d, lo, hi, scale in [(1, 10, 99, 1), (2, 100, 9999, 1), (3, 10**5, 10**6, 1)]:
        for _ in range(6):
            g = R.randint(2, 30) if d > 1 else R.randint(1, 9)
            a, b = g * R.randint(lo // g + 1, hi // g), g * R.randint(lo // g + 1, hi // g)
            if a == b: b += g
            chain, x, y = [], max(a, b), min(a, b)
            while y: chain.append(x); x, y = y, x % y
            chain.append(x)
            add("divisibility", P("num", d, fill(r"Compute $\gcd(<<a>>, <<b>>)$.", a=a, b=b), math.gcd(a, b),
                ex=r"Remainders: $" + r" \to ".join(map(str, chain)) + r" \to 0$.", hint=r"Replace $(a,b)$ by $(b, a \bmod b)$ until the remainder is $0$."))
    for _ in range(6):
        a, b = R.randint(12, 400), R.randint(12, 400)
        add("divisibility", P("num", 1 if a * b < 20000 else 2, fill(r"Compute $\operatorname{lcm}(<<a>>, <<b>>)$.", a=a, b=b), a * b // math.gcd(a, b),
            ex=fill(r"$\gcd = <<g>>$, so $\operatorname{lcm} = <<a>>\cdot<<b>>/<<g>>$.", a=a, b=b, g=math.gcd(a, b)), hint=r"$\operatorname{lcm}(a,b) = ab/\gcd(a,b)$."))
    # bezout
    for _ in range(10):
        a, b = R.randint(20, 900), R.randint(20, 900)
        g = math.gcd(a, b)
        x = next(x for x in range(1, b // g + 1) if (g - a * x) % b == 0)
        add("bezout", P("num", 2, fill(r"Find the smallest positive integer $x$ for which $<<a>>x + <<b>>y = \gcd(<<a>>, <<b>>)$ has an integer solution $y$.", a=a, b=b), x,
            ex=fill(r"$\gcd = <<g>>$ and $y = <<y>>$.", g=g, y=(g - a * x) // b), hint="Run the extended Euclidean algorithm, then shift by multiples of $b/g$."))
    for _ in range(8):
        a, b = R.randint(3, 15), R.randint(3, 15)
        while math.gcd(a, b) != 1: b += 1
        n = R.randint(60, 400)
        cnt = sum(1 for x in range(n // a + 1) if (n - a * x) % b == 0)
        add("bezout", P("num", 3, fill(r"How many pairs of nonnegative integers $(x, y)$ satisfy $<<a>>x + <<b>>y = <<n>>$?", a=a, b=b, n=n), cnt,
            ex="Solutions differ by multiples of $(%d, -%d)$; count those with both coordinates nonnegative." % (b, a)))
    # fta
    for _ in range(8):
        n = R.choice([2, 3, 5, 7, 11]) ** R.randint(1, 4) * R.choice([1, 3, 5, 7, 13]) ** R.randint(1, 3) * R.choice([1, 2, 17, 19])
        f = sp.factorint(n)
        add("fta", P("num", 1 if n < 2000 else 2, fill(r"How many positive divisors does $<<n>>$ have?", n=n), sp.divisor_count(n),
            ex="$" + str(n) + " = " + r" \cdot ".join("%d^{%d}" % (p, e) if e > 1 else str(p) for p, e in sorted(f.items())) + "$, so $\\tau(n) = " + r"\cdot".join(str(e + 1) for e in f.values()) + "$."))
    for _ in range(6):
        ps = R.sample(list(sp.primerange(2, 60)), 3)
        n = math.prod(p ** R.randint(1, 2) for p in ps)
        add("fta", P("num", 2, fill(r"What is the largest prime factor of $<<n>>$?", n=n), max(ps), ex="$" + str(n) + " = " + r" \cdot ".join("%d^{%d}" % (p, e) for p, e in sorted(sp.factorint(n).items())) + "$."))
    # congruences
    for _ in range(10):
        a, k = R.randint(3, 99), R.randint(20, 400)
        add("congruences", P("num", 2, fill(r"Find the last two digits of $<<a>>^{<<k>>}$ (answer as a number from $0$ to $99$).", a=a, k=k), pow(a, k, 100),
            hint="Work modulo $4$ and modulo $25$, or find the cycle of powers modulo $100$."))
    for _ in range(6):
        n, k, m = R.randint(10, 60), R.randint(2, 5), R.choice([7, 9, 11, 13])
        add("congruences", P("num", 3, fill(r"Find the remainder of $1^{<<k>>} + 2^{<<k>>} + \cdots + <<n>>^{<<k>>}$ on division by $<<m>>$.", k=k, n=n, m=m), sum(pow(i, k, m) for i in range(1, n + 1)) % m,
            hint="The terms repeat with period $m$."))
    # modular inverses
    for _ in range(12):
        m = R.choice([R.choice(primes_small[5:]), R.randint(20, 300)])
        a = R.randint(2, m - 1)
        while math.gcd(a, m) != 1: a = R.randint(2, m - 1)
        add("mod-inverse", P("num", 1 if m < 50 else 2, fill(r"Find the inverse of $<<a>>$ modulo $<<m>>$ (an integer from $1$ to $<<m1>>$).", a=a, m=m, m1=m - 1), pow(a, -1, m),
            ex=fill(r"$<<a>> \cdot <<i>> = <<p>> \equiv 1 \pmod{<<m>>}$.", a=a, i=pow(a, -1, m), p=a * pow(a, -1, m), m=m)))
    for _ in range(6):
        m = R.randint(30, 200); g = R.choice([2, 3, 4, 6]); m -= m % g
        a = g * R.randint(2, m // g - 1); b = g * R.randint(1, m // g - 1)
        n = sum(1 for x in range(m) if (a * x - b) % m == 0)
        add("mod-inverse", P("num", 3, fill(r"How many solutions modulo $<<m>>$ does $<<a>>x \equiv <<b>> \pmod{<<m>>}$ have?", a=a, b=b, m=m), n,
            ex=fill(r"$\gcd(<<a>>, <<m>>) = <<g>>$ divides $<<b>>$, so there are $<<g>>$ solutions.", a=a, m=m, g=math.gcd(a, m), b=b) if n else "No solutions: the gcd does not divide the right side."))
    # CRT
    for k, d in [(2, 1), (2, 2), (3, 2), (3, 3)]:
        for _ in range(4):
            while True:
                ms = R.sample([3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27], k)
                if all(math.gcd(x, y) == 1 for i, x in enumerate(ms) for y in ms[i + 1:]): break
            rs = [R.randint(0, m - 1) for m in ms]
            M = math.prod(ms)
            x = next(x for x in range(M) if all(x % m == r for m, r in zip(ms, rs)))
            if x == 0: x = M
            sys_tex = r",\ ".join(r"x \equiv %d \pmod{%d}" % (r, m) for r, m in zip(rs, ms))
            add("crt", P("num", d, "Find the smallest positive integer $x$ with $" + sys_tex + "$.", x, ex="The solution is unique modulo $%d$." % M))
    # Fermat/Euler
    for _ in range(8):
        p = R.choice(primes_small[2:25]); a = R.randint(2, p - 1); k = R.randint(10**5, 10**9)
        add("fermat-euler", P("num", 2, fill(r"Find $<<a>>^{<<k>>} \bmod <<p>>$.", a=a, k=k, p=p), pow(a, k, p),
            ex=fill(r"$<<k>> \equiv <<r>> \pmod{<<p1>>}$, so the answer is $<<a>>^{<<r>>} \bmod <<p>>$.", k=k, r=k % (p - 1), p1=p - 1, a=a, p=p), hint=r"Reduce the exponent modulo $p-1$."))
    for _ in range(6):
        n = R.choice([20, 21, 24, 26, 28, 33, 35, 36, 40, 45, 50, 63]); a = R.randint(2, n - 1)
        while math.gcd(a, n) != 1: a += 1
        k = R.randint(10**4, 10**8)
        add("fermat-euler", P("num", 3, fill(r"Find $<<a>>^{<<k>>} \bmod <<n>>$.", a=a, k=k, n=n), pow(a, k, n), hint=fill(r"$\varphi(<<n>>) = <<f>>$.", n=n, f=sp.totient(n))))
    for a, b, c, m in [(7, 7, 7, 10), (3, 3, 3, 100), (2, 3, 4, 1000)]:
        add("fermat-euler", P("num", 4, fill(r"Find $<<a>>^{<<b>>^{<<c>>}} \bmod <<m>>$.", a=a, b=b, c=c, m=m), pow(a, b ** c, m), hint="Reduce the exponent modulo the order of $a$, using Euler's theorem at each level."))
    # Wilson
    for p in R.sample(primes_small[3:30], 4):
        add("wilson", P("num", 2, fill(r"Find $(<<p2>>)! \bmod <<p>>$.", p2=p - 2, p=p), math.factorial(p - 2) % p, ex=r"$(p-1)! \equiv -1$ and $p - 1 \equiv -1$, so $(p-2)! \equiv 1$."))
    for p in [x for x in primes_small if x % 4 == 1][2:6]:
        add("wilson", P("num", 3, fill(r"Find $\left(\left(\tfrac{<<p>>-1}{2}\right)!\right)^2 \bmod <<p>>$.", p=p), pow(math.factorial((p - 1) // 2), 2, p), ex=r"Pair $k$ with $p - k$ in Wilson's theorem: $\bigl(\tfrac{p-1}2\bigr)!^2 \equiv (-1)^{(p+1)/2} \equiv -1$ for $p \equiv 1 \pmod 4$."))
    for n in [4, 6, 9, 15, 25, 49]:
        add("wilson", P("num", 2, fill(r"Find $(<<n1>>)! \bmod <<n>>$.", n1=n - 1, n=n), math.factorial(n - 1) % n, ex=r"For composite $n > 4$, $(n-1)! \equiv 0 \pmod n$; $n = 4$ is the exception."))
    # arithmetic functions
    for _ in range(8):
        n = R.randint(30, 3000)
        add("arithmetic-functions", P("num", 1 if n < 300 else 2, fill(r"Compute $\varphi(<<n>>)$.", n=n), sp.totient(n), hint=r"$\varphi(n) = n\prod_{p\mid n}(1 - 1/p)$."))
    for _ in range(6):
        n = R.randint(20, 2000)
        add("arithmetic-functions", P("num", 2, fill(r"Compute $\sigma(<<n>>)$, the sum of the positive divisors of $<<n>>$.", n=n), sp.divisor_sigma(n)))
    for N in [20, 50, 100, 200]:
        add("arithmetic-functions", P("num", 3, fill(r"Compute $\sum_{k=1}^{<<N>>} \varphi(k)$.", N=N), sum(sp.totient(k) for k in range(1, N + 1)), hint=r"It counts pairs $1 \le a \le b \le N$ with $\gcd(a,b) = 1$."))
    # Möbius
    for _ in range(6):
        n = R.randint(30, 3000)
        add("mobius", P("num", 1, fill(r"Compute $\mu(<<n>>)$.", n=n), sp.mobius(n)))
    for N in [10, 30, 50, 100]:
        add("mobius", P("num", 3, fill(r"Compute the Mertens function $M(<<N>>) = \sum_{n \le <<N>>} \mu(n)$.", N=N), sum(sp.mobius(k) for k in range(1, N + 1))))
    for N in [50, 100, 500, 1000, 10000]:
        add("mobius", P("num", 2 if N <= 100 else 3, fill(r"How many squarefree integers are there in $[1, <<N>>]$?", N=N), sum(1 for k in range(1, N + 1) if sp.mobius(k) != 0),
            hint=r"$\sum_{d^2 \le N} \mu(d) \lfloor N/d^2 \rfloor$.", ex=fill(r"Close to $6N/\pi^2 \approx <<e>>$.", e=round(6 * N / math.pi ** 2, 1))))
    # order and primitive roots
    for _ in range(8):
        p = R.choice(primes_small[3:30]); a = R.randint(2, p - 1)
        add("order-primroot", P("num", 2, fill(r"Find the order of $<<a>>$ modulo $<<p>>$.", a=a, p=p), sp.n_order(a, p), hint=fill(r"The order divides $<<p1>>$.", p1=p - 1)))
    for p in R.sample(primes_small[3:40], 8):
        add("order-primroot", P("num", 2, fill(r"Find the smallest primitive root modulo $<<p>>$.", p=p), sp.primitive_root(p), hint=fill(r"$g$ is a primitive root iff $g^{(p-1)/q} \not\equiv 1$ for each prime $q \mid <<p1>>$.", p1=p - 1)))
    for p in R.sample(primes_small[5:45], 6):
        add("order-primroot", P("num", 1, fill(r"How many primitive roots are there modulo $<<p>>$?", p=p), sp.totient(p - 1), ex=fill(r"$\varphi(<<p1>>) = <<f>>$.", p1=p - 1, f=sp.totient(p - 1))))
    # p-adic valuation
    for _ in range(8):
        p = R.choice([2, 3, 5, 7, 11]); n = R.randint(50, 2000)
        v = sum(n // p ** k for k in range(1, 20))
        add("p-adic-valuation", P("num", 2, fill(r"Compute $v_{<<p>>}(<<n>>!)$, the exponent of $<<p>>$ in $<<n>>!$.", p=p, n=n), v, hint="Legendre's formula."))
    for n in [100, 250, 1000, 2026, 10**4, 10**6]:
        add("p-adic-valuation", P("num", 1 if n <= 250 else 2, fill(r"How many zeros does $<<n>>!$ end with?", n=n), sum(n // 5 ** k for k in range(1, 20)), hint="Count factors of $5$."))
    for _ in range(6):
        p = R.choice([3, 5, 7]); b = R.randint(2, 9); a = b + p * R.randint(1, 4); n = p ** R.randint(1, 3) * R.randint(1, 4)
        if a % p == 0 or b % p == 0: continue
        val = 0; x = a ** n - b ** n
        while x % p == 0: x //= p; val += 1
        add("p-adic-valuation", P("num", 3, fill(r"Compute $v_{<<p>>}(<<a>>^{<<n>>} - <<b>>^{<<n>>})$.", p=p, a=a, b=b, n=n), val, ex=r"Lifting the exponent: $v_p(a - b) + v_p(n)$."))
    # Lucas
    for _ in range(8):
        p = R.choice([2, 3, 5, 7]); n = R.randint(50, 500); k = R.randint(1, n - 1)
        add("lucas", P("num", 2, fill(r"Compute $\binom{<<n>>}{<<k>>} \bmod <<p>>$.", n=n, k=k, p=p), math.comb(n, k) % p, hint=fill(r"Write $<<n>>$ and $<<k>>$ in base $<<p>>$.", n=n, k=k, p=p)))
    for n in [10, 31, 64, 100, 255, 2026]:
        add("lucas", P("num", 2, fill(r"How many entries of row $<<n>>$ of Pascal's triangle, $\binom{<<n>>}{0}, \dots, \binom{<<n>>}{<<n>>}$, are odd?", n=n), 2 ** bin(n).count("1"), ex=fill(r"$<<n>>$ has $<<s>>$ ones in binary, so $2^{<<s>>}$.", n=n, s=bin(n).count("1"))))
    # quadratic residues
    for _ in range(10):
        p = R.choice(primes_small[3:40]); a = R.randint(2, p - 1)
        add("quadratic-residues", P("num", 2, fill(r"Compute the Legendre symbol $\left(\frac{<<a>>}{<<p>>}\right)$ ($1$ or $-1$).", a=a, p=p), sp.legendre_symbol(a, p), hint=r"Use reciprocity, or Euler's criterion."))
    for _ in range(6):
        n = R.choice([15, 21, 33, 35, 39, 45, 51, 55, 57, 65, 77, 85, 91]); a = R.randint(2, n - 1)
        while math.gcd(a, n) != 1: a += 1
        add("quadratic-residues", P("num", 3, fill(r"Compute the Jacobi symbol $\left(\frac{<<a>>}{<<n>>}\right)$.", a=a, n=n), sp.jacobi_symbol(a, n)))
    for _ in range(4):
        p = R.choice(primes_small[5:30]); a = R.randint(0, p - 1)
        add("quadratic-residues", P("num", 1, fill(r"How many $x \in \{0, 1, \dots, <<p1>>\}$ satisfy $x^2 \equiv <<a>> \pmod{<<p>>}$?", p1=p - 1, a=a, p=p), sum(1 for x in range(p) if (x * x - a) % p == 0)))
    # Hensel
    for p, k in [(3, 3), (5, 2), (5, 3), (7, 2), (11, 2), (13, 2)]:
        a = R.choice([x for x in range(1, p) if sp.legendre_symbol(x, p) == 1])
        m = p ** k
        sols = [x for x in range(m) if (x * x - a) % m == 0]
        add("hensel", P("num", 2, fill(r"How many solutions does $x^2 \equiv <<a>> \pmod{<<m>>}$ have modulo $<<m>>$?", a=a, m=m), len(sols), ex=r"Each of the two roots mod $p$ lifts uniquely, since $f'(x) = 2x \not\equiv 0$."))
        add("hensel", P("num", 3, fill(r"Find the smallest positive $x$ with $x^2 \equiv <<a>> \pmod{<<m>>}$.", a=a, m=m), min(s for s in sols if s > 0), hint="Find a root mod $p$, then lift with Newton's step."))
    # sums of squares
    def r2(n): return sum(1 for x in range(-int(n ** .5) - 1, int(n ** .5) + 2) for y in range(-int(n ** .5) - 1, int(n ** .5) + 2) if x * x + y * y == n)
    for n in R.sample([5, 13, 25, 65, 85, 125, 130, 145, 169, 221, 325, 425, 1105, 21, 50, 100], 8):
        add("sums-of-squares", P("num", 2 if n < 200 else 3, fill(r"How many ordered integer pairs $(x, y)$ satisfy $x^2 + y^2 = <<n>>$?", n=n), r2(n), hint=r"$r_2(n) = 4\sum_{d\mid n}\chi_{-4}(d)$: count divisors $\equiv 1$ minus divisors $\equiv 3 \pmod 4$."))
    for N in [50, 100, 200, 500]:
        add("sums-of-squares", P("num", 3, fill(r"How many integers $n \in [1, <<N>>]$ are sums of two squares (zero allowed)?", N=N), sum(1 for n in range(1, N + 1) if r2(n) > 0)))
    # Pythagorean
    def prim(N): return sum(1 for m in range(2, int(N ** .5) + 2) for n in range(1, m) if (m - n) % 2 and math.gcd(m, n) == 1 and m * m + n * n <= N)
    for N in [50, 100, 300, 1000, 10000]:
        add("pythagorean", P("num", 2 if N <= 100 else 3, fill(r"How many primitive Pythagorean triples have hypotenuse at most $<<N>>$?", N=N), prim(N), ex=fill(r"About $N/(2\pi) \approx <<e>>$.", e=round(N / (2 * math.pi), 1))))
    for c in [65, 85, 145, 325, 1105]:
        n = sum(1 for m in range(2, 40) for k in range(1, m) if (m - k) % 2 and math.gcd(m, k) == 1 and m * m + k * k == c)
        add("pythagorean", P("num", 3, fill(r"How many primitive Pythagorean triples $a < b < c$ have hypotenuse $c = <<c>>$?", c=c), n, hint=r"$c = m^2 + n^2$ with $m > n$ coprime of opposite parity."))
    # continued fractions
    def cf_sqrt(n):
        a0 = math.isqrt(n); m, d, a, per = 0, 1, a0, []
        while True:
            m = d * a - m; d = (n - m * m) // d; a = (a0 + m) // d; per.append(a)
            if a == 2 * a0: return a0, per
    for n in R.sample([x for x in range(2, 120) if math.isqrt(x) ** 2 != x], 8):
        a0, per = cf_sqrt(n)
        add("continued-fractions", P("num", 2, fill(r"What is the period length of the continued fraction of $\sqrt{<<n>>}$?", n=n), len(per), ex="$\\sqrt{%d} = [%d;\\overline{%s}]$." % (n, a0, ",".join(map(str, per)))))
    for _ in range(6):
        terms = [R.randint(0, 3)] + [R.randint(1, 6) for _ in range(R.randint(2, 4))]
        v = F(terms[-1])
        for t in reversed(terms[:-1]): v = t + 1 / v
        add("continued-fractions", P("num", 1, "Evaluate $[" + str(terms[0]) + ";" + ",".join(map(str, terms[1:])) + "]$ as a fraction.", v, hint="Work from the last term upward."))
    # Pell
    for d in R.sample([2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 17, 19, 21, 29, 31, 61], 10):
        a0, per = cf_sqrt(d)
        L = len(per); seq = ([a0] + per * 2)[: (L if L % 2 == 0 else 2 * L)]
        h0, h1, k0, k1 = 1, seq[0], 0, 1
        for a in seq[1:]: h0, h1, k0, k1 = h1, a * h1 + h0, k1, a * k1 + k0
        assert h1 * h1 - d * k1 * k1 == 1
        add("pell", P("num", 2 if h1 < 1000 else 3 if h1 < 10**6 else 4, fill(r"Find the smallest $x > 1$ such that $x^2 - <<d>>y^2 = 1$ has an integer solution $y$.", d=d), h1, ex=fill(r"$(x, y) = (<<x>>, <<y>>)$.", x=h1, y=k1)))
    # quadratic forms / class numbers
    def hD(D):
        h, a = 0, 1
        while 3 * a * a <= -D:
            for b in range(-a + 1, a + 1):
                if (b * b - D) % (4 * a): continue
                c = (b * b - D) // (4 * a)
                if c < a: continue
                if b < 0 and c == a: continue
                if math.gcd(math.gcd(a, abs(b)), c) == 1: h += 1
            a += 1
        return h
    global HD
    HD = hD
    for D in [-23, -31, -47, -56, -71, -84, -87, -104, -116, -119]:
        add("quadratic-forms", P("num", 3, fill(r"How many reduced primitive positive definite binary quadratic forms have discriminant $<<D>>$?", D=D), hD(D), hint=r"List $|b| \le a \le c$ with $b^2 - 4ac = D$."))
    for d in [5, 6, 10, 13, 14, 17, 21, 23, 26, 30, 43, 163]:
        D = -d if d % 4 == 3 else -4 * d
        add("class-group", P("num", 3, fill(r"Compute the class number of $\mathbb Q(\sqrt{-<<d>>})$.", d=d), hD(D), ex=fill(r"Its discriminant is $<<D>>$; count reduced forms.", D=D)))
    # series
    for _ in range(4):
        r = F(R.randint(1, 4), R.randint(5, 9))
        add("series", P("num", 1, "Compute $\\sum_{n \\ge 0} \\left(" + frac_tex(r) + "\\right)^n$.", 1 / (1 - r)))
    for k in [2, 3, 4, 5]:
        add("series", P("num", 2, fill(r"Compute $\displaystyle\sum_{n \ge 1} \frac{1}{n(n+<<k>>)}$.", k=k), F(sum(F(1, j) for j in range(1, k + 1)), k), hint=r"$\frac{1}{n(n+k)} = \frac1k\left(\frac1n - \frac1{n+k}\right)$."))
    # partial summation
    for n in [4, 5, 6, 8]:
        add("partial-summation", P("num", 1, fill(r"Compute the harmonic number $H_{<<n>>} = 1 + \frac12 + \cdots + \frac1{<<n>>}$ as a fraction.", n=n), sum(F(1, j) for j in range(1, n + 1))))
    for N in [10, 30, 100, 1000]:
        add("partial-summation", P("num", 2, fill(r"Compute $\sum_{n \le <<N>>} \tau(n)$.", N=N), sum(N // k for k in range(1, N + 1)), hint=r"Swap the order: $\sum_{n \le N}\tau(n) = \sum_{d \le N}\lfloor N/d\rfloor$."))
    add("asymptotics", P("num", 2, r"Euler's constant $\gamma = \lim (H_n - \log n)$ to four decimal places.", 0.5772, tol=6e-5, ex=r"$\gamma = 0.5772156649\ldots$"))
    # complex numbers
    for _ in range(8):
        a, b, n = R.randint(-3, 3) or 1, R.randint(1, 3), R.randint(3, 8)
        z = complex(a, b) ** n
        add("complex-numbers", P("num", 1 if n < 5 else 2, fill(r"Find the real part of $(<<z>>)^{<<n>>}$.", z=("%d + %di" % (a, b)).replace("+ -", "- "), n=n), int(round(z.real))))
    # holomorphic
    for k in [2, 3, 4, 5, 6]:
        add("holomorphic", P("num", 2, fill(r"Compute $\displaystyle\frac{1}{2\pi i}\oint_{|z|=1} \frac{e^z}{z^{<<k1>>}}\,dz$.", k1=k + 1), F(1, math.factorial(k)), ex=fill(r"It is the coefficient of $z^{<<k>>}$ in $e^z$: $1/<<k>>!$.", k=k)))
    for a, inside in [(0.5, 1), (2, 0), (-0.3, 1), (1.5, 0)]:
        add("holomorphic", P("num", 1, fill(r"Compute $\displaystyle\frac{1}{2\pi i}\oint_{|z|=1} \frac{dz}{z - <<a>>}$.", a=a).replace("- -", "+ "), inside, ex="It is $1$ if the pole is inside the circle and $0$ otherwise."))
    # residues
    for a in [1, 2, 3, 5, 7, 10]:
        add("residues", P("num", 2, fill(r"$\displaystyle\int_{-\infty}^{\infty}\frac{dx}{x^2 + <<a2>>}$ is what multiple of $\pi$?", a2=a * a), F(1, a), ex=fill(r"Residue at $z = <<a>>i$: $\frac{1}{2<<a>>i}$, so the integral is $\pi/<<a>>$.", a=a)))
    for a in [1, 2, 3]:
        add("residues", P("num", 3, fill(r"$\displaystyle\int_{-\infty}^{\infty}\frac{dx}{(x^2 + <<a2>>)^2}$ is what multiple of $\pi$?", a2=a * a), F(1, 2 * a ** 3), hint=r"Double pole at $z = ai$."))
    for _ in range(8):
        while True:
            deg = R.randint(3, 6); j = R.randint(0, deg); coef = [R.choice([-1, 1]) for _ in range(deg + 1)]
            coef[deg - j] = R.choice([-1, 1]) * (deg + 3)
            roots = np.roots(coef)
            if all(abs(abs(r) - 1) > 0.05 for r in roots): break
        poly = ""
        for i, c in enumerate(coef):
            e = deg - i
            mon = "" if e == 0 else ("z" if e == 1 else "z^{%d}" % e)
            cs = str(abs(c)) if (abs(c) != 1 or e == 0) else ""
            if not poly: poly = ("-" if c < 0 else "") + cs + mon
            else: poly += (" - " if c < 0 else " + ") + cs + mon
        add("residues", P("num", 3, "How many zeros does $" + poly + "$ have in the disc $|z| < 1$?", sum(1 for r in roots if abs(r) < 1), hint="Rouché: compare with the dominant term on $|z| = 1$."))
    # continuation
    for k in [2, 3, 5, -2]:
        add("continuation", P("num", 1, fill(r"The continuation of $\sum_{n \ge 0} z^n$ to $z = <<k>>$ equals?", k=k), F(1, 1 - k)))
    for n in [1, 3, 5, 7]:
        v = sp.zeta(-n)
        add("continuation", P("num", 2, fill(r"Compute $\zeta(-<<n>>)$.", n=n), F(int(v.p), int(v.q)), ex=r"$\zeta(-n) = -B_{n+1}/(n+1)$."))
    # gamma
    for n in [4, 6, 7, 9]:
        add("gamma", P("num", 1, fill(r"Compute $\Gamma(<<n>>)$.", n=n), math.factorial(n - 1)))
    for n in [1, 2, 3, 4]:
        v = F(math.factorial(2 * n), 4 ** n * math.factorial(n))
        add("gamma", P("num", 2, fill(r"$\Gamma(<<n>> + \tfrac12)$ is what multiple of $\sqrt\pi$?", n=n), v, hint=r"$\Gamma(\tfrac12) = \sqrt\pi$ and $\Gamma(s+1) = s\Gamma(s)$."))
    for a, b in [(2, 3), (3, 3), (2, 5), (4, 3)]:
        add("gamma", P("num", 2, fill(r"Compute the Beta integral $\int_0^1 x^{<<a1>>}(1-x)^{<<b1>>}\,dx$.", a1=a - 1, b1=b - 1), F(math.factorial(a - 1) * math.factorial(b - 1), math.factorial(a + b - 1)), hint=r"$B(a,b) = \Gamma(a)\Gamma(b)/\Gamma(a+b)$."))
    # Fourier / Poisson
    for k in [2, 3, 5]:
        add("fourier-poisson", P("num", 2, fill(r"With $\theta(t) = \sum_{n\in\mathbb Z} e^{-\pi n^2 t}$, compute $\theta(1/<<t>>)/\theta(<<t>>)$.", t=k * k), k, tol=1e-9))
    # Mellin
    for a, n in [(2, 3), (3, 2), (1, 5), (2, 4), (4, 2), (5, 3)]:
        add("mellin", P("num", 2, fill(r"Compute the Mellin transform of $e^{-<<a>>x}$ at $s = <<n>>$, i.e. $\int_0^\infty x^{<<n1>>} e^{-<<a>>x}\,dx$.", a=a, n=n, n1=n - 1), F(math.factorial(n - 1), a ** n), hint=r"Substitute $u = ax$: the answer is $\Gamma(s)/a^s$."))
    # Dirichlet series coefficients
    for n in [12, 36, 60, 100, 360]:
        add("dirichlet-series", P("num", 1, fill(r"What is the coefficient of $<<n>>^{-s}$ in $\zeta(s)^2$?", n=n), sp.divisor_count(n), ex=r"$\zeta(s)^2 = \sum \tau(n) n^{-s}$."))
    for n in [30, 12, 77]:
        add("dirichlet-series", P("num", 2, fill(r"What is the coefficient of $<<n>>^{-s}$ in $1/\zeta(s)$?", n=n), sp.mobius(n)))
    for n in [18, 35, 50]:
        add("dirichlet-series", P("num", 2, fill(r"What is the coefficient of $<<n>>^{-s}$ in $\zeta(s)/\zeta(2s)$?", n=n), abs(sp.mobius(n)), ex=r"$\zeta(s)/\zeta(2s) = \sum |\mu(n)| n^{-s}$."))
    # zeta values
    for k in [2, 3, 4, 5]:
        v = sp.zeta(2 * k) / sp.pi ** (2 * k)
        v = sp.nsimplify(v)
        add("zeta", P("num", 2, fill(r"$\zeta(<<n>>)$ is $\pi^{<<n>>}$ times which rational number?", n=2 * k), F(int(v.p), int(v.q))))
    for n in [9, 11, 13]:
        v = sp.zeta(-n)
        add("zeta", P("num", 3, fill(r"Compute $\zeta(-<<n>>)$.", n=n), F(int(v.p), int(v.q)), hint=r"$\zeta(-n) = -B_{n+1}/(n+1)$."))
    # functional equation
    for N in [7, 15, 31, 100]:
        add("functional-equation", P("num", 1, fill(r"How many trivial zeros does $\zeta$ have in $-<<N>> < s < 0$?", N=N), (N - 1) // 2))
    # Chebyshev
    for n in [8, 12, 15, 20]:
        add("chebyshev", P("num", 2, fill(r"Compute $e^{\psi(<<n>>)}$.", n=n), math.lcm(*range(1, n + 1)), hint=r"$e^{\psi(n)} = \operatorname{lcm}(1, \dots, n)$."))
    for n in [10, 20, 30]:
        add("chebyshev", P("num", 2, fill(r"Compute $e^{\vartheta(<<n>>)}$, where $\vartheta(x) = \sum_{p \le x} \log p$.", n=n), math.prod(sp.primerange(2, n + 1)), ex="The product of the primes up to $%d$." % n))
    for n in [32, 49, 81, 100, 121]:
        f = sp.factorint(n)
        add("chebyshev", P("num", 1, fill(r"Compute $e^{\Lambda(<<n>>)}$.", n=n), list(f)[0] if len(f) == 1 else 1))
    # Mertens
    for x in [100, 1000, 10**5]:
        add("mertens", P("num", 3, fill(r"Compute $\sum_{p \le <<x>>} 1/p$ to three decimal places.", x=x), round(sum(1 / p for p in sp.primerange(2, x + 1)), 4), tol=6e-4, ex=r"Mertens: $\log\log x + 0.2615\ldots$"))
    for x in [100, 1000]:
        v = math.prod(1 - 1 / p for p in sp.primerange(2, x + 1)) * math.log(x)
        add("mertens", P("num", 4, fill(r"Compute $\log <<x>> \cdot \prod_{p \le <<x>>}(1 - 1/p)$ to three decimal places.", x=x), round(v, 4), tol=6e-4, ex=fill(r"Compare $e^{-\gamma} = 0.5615\ldots$; at $x = <<x>>$ the value is $<<v>>$.", x=x, v=round(v, 4))))
    # PNT
    for x in [50, 100, 200, 500, 1000, 5000, 10**4, 10**5, 10**6]:
        add("pnt", P("num", 1 if x <= 200 else 2, fill(r"Compute $\pi(<<x>>)$, the number of primes up to $<<x>>$.", x=x if x < 10**4 else "10^{%d}" % round(math.log10(x))), sp.primepi(x),
            ex=fill(r"$x/\log x \approx <<e>>$.", e=round(x / math.log(x), 1))))
    # zeros
    zs = [float(mp.zetazero(k).imag) for k in range(1, 30)]
    for T in [20, 30, 40, 60, 80, 100]:
        add("nontrivial-zeros", P("num", 2, fill(r"How many zeros $\rho$ of $\zeta$ have $0 < \operatorname{Im}\rho < <<T>>$?", T=T), sum(1 for z in zs if z < T),
            ex=fill(r"The Riemann–von Mangoldt main term gives about $<<e>>$.", e=round(T / (2 * math.pi) * math.log(T / (2 * math.pi * math.e)) + 7 / 8, 1))))
    for k in [2, 3, 5, 10]:
        ordn = {2: "second", 3: "third", 5: "fifth", 10: "tenth"}[k]
        add("nontrivial-zeros", P("num", 3, "Give the imaginary part of the " + ordn + " nontrivial zero to two decimal places.", round(zs[k - 1], 4), tol=0.006, ex="$%.6f\\ldots$" % zs[k - 1]))
    # characters
    def char_count_primitive(q): return sum(sp.mobius(q // d) * sp.totient(d) for d in sp.divisors(q))
    def elems_order_le2(q): return sum(1 for a in range(1, q + 1) if math.gcd(a, q) == 1 and (a * a) % q == 1 % q)
    for q in [7, 12, 15, 16, 20, 24]:
        add("dirichlet-characters", P("num", 1, fill(r"How many Dirichlet characters are there modulo $<<q>>$?", q=q), sp.totient(q)))
    for q in [9, 12, 15, 16, 20, 21, 25, 36]:
        add("dirichlet-characters", P("num", 3, fill(r"How many primitive Dirichlet characters are there modulo $<<q>>$?", q=q), char_count_primitive(q), hint=r"$\sum_{d\mid q}\mu(q/d)\varphi(d)$."))
    for q in [8, 15, 24, 35, 105]:
        add("dirichlet-characters", P("num", 2, fill(r"How many real (values $\pm1, 0$) Dirichlet characters are there modulo $<<q>>$?", q=q), elems_order_le2(q), hint="Real characters correspond to elements of order at most 2 in the group of characters, which matches the count in $(\\mathbb Z/q)^\\times$."))
    for p, k in [(13, 3), (13, 4), (31, 5), (37, 6)]:
        add("dirichlet-characters", P("num", 2, fill(r"How many characters modulo $<<p>>$ have order exactly $<<k>>$?", p=p, k=k), sp.totient(k) if (p - 1) % k == 0 else 0, ex="The character group is cyclic of order $%d$." % (p - 1)))
    # Gauss sums
    for p in [5, 7, 11, 13, 17, 19]:
        add("gauss-sums", P("num", 2, fill(r"For the quadratic character $\chi$ modulo $<<p>>$, compute $g(\chi)^2$.", p=p), p * (1 if p % 4 == 1 else -1), ex=r"$g^2 = \left(\frac{-1}{p}\right) p$."))
    for p in [7, 13, 19]:
        add("exponential-sums", P("num", 2, fill(r"Compute $\Bigl|\sum_{n=0}^{<<p1>>} e^{2\pi i n^2/<<p>>}\Bigr|^2$.", p1=p - 1, p=p), p))
    for q, a in [(10, 3), (12, 12), (7, 14)]:
        add("exponential-sums", P("num", 1, fill(r"Compute $\sum_{n=0}^{<<q1>>} e^{2\pi i \cdot <<a>> n / <<q>>}$.", q1=q - 1, a=a, q=q), q if a % q == 0 else 0))
    # L-functions
    for q, a in [(7, 1), (10, 3), (11, 2), (12, 7), (13, 4), (17, 16), (19, 10), (24, 23)]:
        p = next(p for p in sp.primerange(2, 10**4) if p % q == a)
        add("l-functions", P("num", 1, fill(r"Find the smallest prime $p \equiv <<a>> \pmod{<<q>>}$.", a=a, q=q), p))
    for q, a, x in [(4, 1, 1000), (4, 3, 1000), (3, 1, 10**4), (10, 7, 10**4), (7, 3, 10**5)]:
        add("l-functions", P("num", 2, fill(r"How many primes $p \le <<x>>$ satisfy $p \equiv <<a>> \pmod{<<q>>}$?", x=x if x < 10**4 else "10^{%d}" % round(math.log10(x)), a=a, q=q), sum(1 for p in sp.primerange(2, x + 1) if p % q == a),
            ex=fill(r"Dirichlet predicts about $\pi(x)/\varphi(q) \approx <<e>>$.", e=round(sp.primepi(x) / sp.totient(q), 1))))
    # class number formula (D < -4: L(1,chi_D) sqrt|D| / pi = h)
    for D in [-7, -8, -11, -15, -20, -23, -24, -39]:
        w = 2
        add("class-number-formula", P("num", 3, fill(r"Using Dirichlet's formula, compute $L(1,\chi_{<<D>>})\sqrt{<<aD>>}/\pi$.", D=D, aD=-D), hD(D), ex=fill(r"It equals $h(<<D>>)$ since $w = 2$.", D=D)))
    # sieve
    for N in [210, 1000, 2026, 10**4]:
        add("sieve-basics", P("num", 2, fill(r"How many integers in $[1, <<N>>]$ are divisible by none of $2, 3, 5, 7$?", N=N), sum(1 for n in range(1, N + 1) if all(n % p for p in (2, 3, 5, 7))), hint="Inclusion–exclusion over divisors of $210$."))
    # gaps and twins
    for N in [100, 1000, 10**4, 10**5, 10**6]:
        ps = list(sp.primerange(2, N + 3))
        add("twin-primes", P("num", 2, fill(r"How many twin prime pairs $(p, p+2)$ have $p + 2 \le <<N>>$?", N=N if N < 10**4 else "10^{%d}" % round(math.log10(N))), sum(1 for a, b in zip(ps, ps[1:]) if b - a == 2 and b <= N)))
    for N in [100, 1000, 10**4, 10**5]:
        ps = list(sp.primerange(2, N + 1))
        add("bounded-gaps", P("num", 2, fill(r"What is the largest gap $p_{n+1} - p_n$ between consecutive primes below $<<N>>$?", N=N if N < 10**4 else "10^{%d}" % round(math.log10(N))), max(b - a for a, b in zip(ps, ps[1:]))))
    # Goldbach and three primes
    for n in [28, 50, 100, 128, 210, 1000]:
        add("goldbach", P("num", 2, fill(r"In how many ways can $<<n>>$ be written as $p + q$ with primes $p \le q$?", n=n), sum(1 for p in sp.primerange(2, n // 2 + 1) if sp.isprime(n - p))))
    for n in [15, 21, 27, 33, 45]:
        ps = list(sp.primerange(2, n))
        add("ternary-goldbach", P("num", 3, fill(r"In how many ways can $<<n>>$ be written as $p_1 + p_2 + p_3$ with primes $p_1 \le p_2 \le p_3$?", n=n),
            sum(1 for i, a in enumerate(ps) for j, b in enumerate(ps[i:], i) if b >= a and n - a - b >= b and sp.isprime(n - a - b))))
    # Waring
    def min_squares(n):
        best = [0] + [9] * n
        for m in range(1, n + 1):
            best[m] = min(best[m - k * k] + 1 for k in range(1, math.isqrt(m) + 1))
        return best[n]
    for n in [7, 12, 28, 60, 79, 112]:
        add("waring", P("num", 2, fill(r"What is the least number of squares of positive integers that sum to $<<n>>$?", n=n), min_squares(n), hint=r"Legendre: $n$ needs four squares exactly when $n = 4^a(8b+7)$."))
    def min_cubes(n):
        best = [0] + [99] * n
        for m in range(1, n + 1):
            best[m] = min(best[m - k ** 3] + 1 for k in range(1, round(m ** (1 / 3)) + 2) if k ** 3 <= m)
        return best[n]
    for n in [23, 15, 50, 239]:
        add("waring", P("num", 3, fill(r"What is the least number of positive cubes that sum to $<<n>>$?", n=n), min_cubes(n), ex="Only $23$ and $239$ need nine cubes."))
    # pair correlation
    for T in [100, 10**4, 10**6]:
        add("pair-correlation", P("num", 3, fill(r"The mean spacing of zeros at height $T$ is $2\pi/\log(T/2\pi)$. Compute it for $T = <<T>>$ to two decimals.", T=T if T < 10**4 else "10^{%d}" % round(math.log10(T))), round(2 * math.pi / math.log(T / (2 * math.pi)), 4), tol=0.006))
    # Gaussian and Eisenstein integers
    def chi4(d): return 0 if d % 2 == 0 else (1 if d % 4 == 1 else -1)
    def chi3(d): return 0 if d % 3 == 0 else (1 if d % 3 == 1 else -1)
    for a, b in [(3, 4), (5, 12), (7, -2), (11, 6)]:
        add("gaussian-integers", P("num", 1, fill(r"Compute the norm $N(<<z>>)$.", z=("%d + %di" % (a, b)).replace("+ -", "- ")), a * a + b * b))
    for n in [5, 25, 65, 9, 45]:
        add("gaussian-integers", P("num", 3, fill(r"How many ideals of $\mathbb Z[i]$ have norm $<<n>>$?", n=n), sum(chi4(d) for d in sp.divisors(n)), hint=r"$\sum_{d \mid n}\chi_{-4}(d)$."))
    for a, b in [(3, 1), (4, -1), (5, 2), (7, 3)]:
        add("eisenstein-integers", P("num", 1, fill(r"Compute $N(<<a>> + <<b>>\omega) = a^2 - ab + b^2$.", a=a, b=b).replace("+ -", "- "), a * a - a * b + b * b))
    for n in [7, 13, 49, 21, 91]:
        add("eisenstein-integers", P("num", 3, fill(r"How many ideals of $\mathbb Z[\omega]$ have norm $<<n>>$?", n=n), sum(chi3(d) for d in sp.divisors(n)), hint=r"$\sum_{d \mid n}\chi_{-3}(d)$."))
    # cyclotomic
    for n in [7, 12, 15, 24, 30]:
        add("cyclotomic", P("num", 1, fill(r"What is the degree $[\mathbb Q(\zeta_{<<n>>}) : \mathbb Q]$?", n=n), sp.totient(n)))
    x = sp.symbols("x")
    for n in [5, 8, 9, 12, 30]:
        add("cyclotomic", P("num", 2, fill(r"Compute $\Phi_{<<n>>}(1)$.", n=n), int(sp.cyclotomic_poly(n, 1)), hint=r"$\Phi_n(1) = p$ if $n$ is a power of the prime $p$, and $1$ otherwise ($n > 1$)."))
    for n in [6, 10, 12]:
        add("cyclotomic", P("num", 2, fill(r"Compute $\Phi_{<<n>>}(2)$.", n=n), int(sp.cyclotomic_poly(n, 2))))
    for p in [7, 13, 11, 19]:
        add("cubic-characters", P("num", 1, fill(r"How many characters of order exactly $3$ are there modulo $<<p>>$?", p=p), 2 if p % 3 == 1 else 0))
    for p, a in [(7, 6), (13, 5), (19, 7), (31, 2)]:
        add("cubic-characters", P("num", 2, fill(r"How many $x$ modulo $<<p>>$ satisfy $x^3 \equiv <<a>> \pmod{<<p>>}$?", p=p, a=a), sum(1 for t in range(p) if (t ** 3 - a) % p == 0)))
    # elliptic curves
    for _ in range(12):
        while True:
            p = R.choice([5, 7, 11, 13, 17, 19, 23, 29, 31]); a, b = R.randint(0, p - 1), R.randint(0, p - 1)
            if (4 * a ** 3 + 27 * b * b) % p: break
        n = p + 1 + sum(sp.legendre_symbol((t ** 3 + a * t + b) % p, p) if (t ** 3 + a * t + b) % p else 0 for t in range(p))
        add("elliptic-curves", P("num", 2 if p < 15 else 3, fill(r"How many points, including the point at infinity, does $y^2 = x^3 + <<a>>x + <<b>>$ have over $\mathbb F_{<<p>>}$?", a=a, b=b, p=p), n, ex=fill(r"Hasse allows $<<lo>>$ to $<<hi>>$.", lo=math.ceil(p + 1 - 2 * p ** .5), hi=math.floor(p + 1 + 2 * p ** .5))))
    # primality
    for a in [2, 3, 5, 7]:
        n = next(n for n in range(9, 10**4, 2) if not sp.isprime(n) and math.gcd(a, n) == 1 and pow(a, n - 1, n) == 1)
        add("primality", P("num", 3, fill(r"What is the smallest odd composite $n$ with $\gcd(<<a>>, n) = 1$ and $<<a>>^{n-1} \equiv 1 \pmod n$?", a=a), n))
    for N in [2000, 10**4, 10**5]:
        add("primality", P("num", 4, fill(r"How many Carmichael numbers are at most $<<N>>$?", N=N if N < 10**4 else "10^{%d}" % round(math.log10(N))),
            sum(1 for n in range(3, N + 1, 2) if not sp.isprime(n) and all((n - 1) % (p - 1) == 0 and e == 1 for p, e in sp.factorint(n).items()) and len(sp.factorint(n)) >= 2), hint="Korselt's criterion."))
    for n in [8051, 10403, 25217, 1000009]:
        add("primality", P("num", 2, fill(r"Find the smallest prime factor of $<<n>>$.", n=n), min(sp.factorint(n))))
    # RSA
    for _ in range(8):
        p, q = R.sample([11, 13, 17, 19, 23, 29, 31, 37, 41, 43], 2); phi = (p - 1) * (q - 1)
        e = R.choice([e for e in [3, 5, 7, 11, 13, 17] if math.gcd(e, phi) == 1])
        add("rsa", P("num", 2, fill(r"For RSA with $p = <<p>>$, $q = <<q>>$ and $e = <<e>>$, find the private exponent $d$ with $0 < d < \varphi(n)$.", p=p, q=q, e=e), pow(e, -1, phi), ex=fill(r"$\varphi(n) = <<f>>$.", f=phi)))
    for _ in range(6):
        p, q = R.sample([11, 13, 17, 19, 23, 29, 31], 2); n = p * q; phi = (p - 1) * (q - 1)
        e = next(e for e in [3, 5, 7, 11, 13] if math.gcd(e, phi) == 1); m = R.randint(2, n - 1); c = pow(m, e, n)
        add("rsa", P("num", 3, fill(r"RSA with $n = <<n>>$ and $e = <<e>>$: decrypt the ciphertext $c = <<c>>$.", n=n, e=e, c=c), m, hint="Factor $n$, compute $d$, then $c^d \\bmod n$."))
    # discrete log
    for _ in range(10):
        p = R.choice(primes_small[5:40]); g = sp.primitive_root(p); x = R.randint(2, p - 2)
        add("discrete-log", P("num", 2 if p < 60 else 3, fill(r"$<<g>>$ is a primitive root modulo $<<p>>$. Find $x \in [0, <<p2>>]$ with $<<g>>^x \equiv <<h>> \pmod{<<p>>}$.", g=g, p=p, p2=p - 2, h=pow(g, x, p)), x))

gen()

# ---------------- hand-written ----------------
def hand():
    A = add
    A("divisibility", H("choice", 1, r"Which identity drives the Euclidean algorithm?", opts=[r"$\gcd(a,b) = \gcd(b, a \bmod b)$", r"$\gcd(a,b) = \gcd(a+b, ab)$", r"$\gcd(a,b)\operatorname{lcm}(a,b) = a + b$", r"$\gcd(a,b) = \gcd(a^2, b^2)$"], a=0, ex=r"Any common divisor of $a$ and $b$ divides $a - qb$, and conversely."))
    A("divisibility", H("proof", 3, r"Prove Lamé's bound: if the Euclidean algorithm on $a > b$ takes $n$ steps, then $b \ge F_{n+1}$ (Fibonacci). Post your proof for review."))
    A("bezout", H("choice", 1, r"For which $c$ does $12x + 18y = c$ have integer solutions?", opts=[r"multiples of $6$", r"multiples of $12$", r"all integers", r"multiples of $36$"], a=0))
    A("bezout", H("proof", 3, r"Show that every integer $n > ab - a - b$ can be written as $ax + by$ with $x, y \ge 0$ when $\gcd(a,b) = 1$, and that $ab - a - b$ cannot (the Frobenius number)."))
    A("fta", H("choice", 1, r"What is the key step in Euclid's proof that there are infinitely many primes?", opts=["Consider the product of all known primes plus one", "Show that $\\sum 1/p$ diverges", "Use that every even number is a sum of two primes", "Bound the gaps between primes"], a=0, ex=r"$p_1 \cdots p_n + 1$ has a prime factor not in the list. The second option is Euler's proof."))
    A("fta", H("choice", 2, r"In $\mathbb Z[\sqrt{-5}]$, which shows unique factorization fails?", opts=[r"$6 = 2\cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$", r"$4 = 2 \cdot 2$", r"$5 = \sqrt{-5}\cdot(-\sqrt{-5})$", r"$9 = 3\cdot 3$"], a=0))
    A("congruences", H("num", 1, r"What is $2^{100} \bmod 13$?", a=3, hint="Find the cycle of powers of $2$ modulo $13$.", ex=r"$2^{12} \equiv 1$ and $100 = 12\cdot8 + 4$, so $2^4 = 16 \equiv 3$."))
    A("congruences", H("proof", 2, r"Show that $n^5 - n$ is divisible by $30$ for every integer $n$."))
    A("crt", H("num", 1, r"Sunzi's problem: the smallest positive $x$ with $x \equiv 2 \pmod 3$, $x \equiv 3 \pmod 5$, $x \equiv 2 \pmod 7$.", a=23, ex="$23$, the answer given in the Sunzi Suanjing."))
    A("fermat-euler", H("proof", 2, r"Prove Fermat's little theorem by counting necklaces of length $p$ with $a$ colours."))
    A("wilson", H("choice", 2, r"For which $n > 1$ is $(n-1)! \equiv -1 \pmod n$?", opts=["exactly the primes", "all odd $n$", "primes and $4$", "all $n$"], a=0))
    A("arithmetic-functions", H("num", 1, r"$\sigma(28)$, the sum of the divisors of $28$.", a=56, ex=r"$56 = 2\cdot 28$: $28$ is perfect."))
    A("arithmetic-functions", H("proof", 3, r"Prove Euclid–Euler: an even number is perfect iff it is $2^{p-1}(2^p - 1)$ with $2^p - 1$ prime."))
    A("mobius", H("num", 1, r"$\sum_{d \mid 100}\varphi(d)$.", a=100, ex=r"Always $\sum_{d\mid n}\varphi(d) = n$; inverting gives $\varphi = \mu * \mathrm{id}$."))
    A("order-primroot", H("choice", 2, r"For which $n$ does a primitive root modulo $n$ exist?", opts=[r"$1, 2, 4, p^k, 2p^k$ ($p$ odd)", "all $n$", "primes only", "odd $n$"], a=0))
    A("p-adic-valuation", H("proof", 3, r"Prove the lifting-the-exponent lemma $v_p(a^n - b^n) = v_p(a - b) + v_p(n)$ for odd $p \mid a - b$, $p \nmid ab$."))
    A("lucas", H("choice", 2, r"Kummer's theorem: $v_p\binom{n}{k}$ equals", opts=[r"the number of carries when adding $k$ and $n - k$ in base $p$", r"the number of base-$p$ digits of $n$", r"$v_p(n) - v_p(k)$", r"$\lfloor n/p \rfloor - \lfloor k/p\rfloor$"], a=0))
    A("quadratic-residues", H("num", 2, r"$\left(\frac{17}{31}\right)$ ($1$ or $-1$).", a=-1, hint=r"$17 \equiv 1 \pmod 4$, so $\left(\frac{17}{31}\right) = \left(\frac{31}{17}\right) = \left(\frac{14}{17}\right)$.", ex=r"$\left(\frac{2}{17}\right)\left(\frac{7}{17}\right) = \left(\frac{17}{7}\right) = \left(\frac{3}{7}\right) = -1$."))
    A("quadratic-residues", H("choice", 2, r"For an odd prime $p$, $\left(\frac{-1}{p}\right) = 1$ exactly when", opts=[r"$p \equiv 1 \pmod 4$", r"$p \equiv 3 \pmod 4$", r"$p \equiv \pm 1 \pmod 8$", "always"], a=0))
    A("quadratic-residues", H("proof", 3, r"Prove quadratic reciprocity using Gauss sums: show $g^2 = \left(\frac{-1}{p}\right)p$ and compute $g^{q-1}$ modulo $q$."))
    A("hensel", H("choice", 2, r"Hensel's lemma lifts a root $x_0$ of $f$ modulo $p$ uniquely when", opts=[r"$f'(x_0) \not\equiv 0 \pmod p$", r"$f(x_0) \equiv 1 \pmod p$", r"$p = 2$", r"$f$ is linear"], a=0))
    A("sums-of-squares", H("choice", 1, r"Which number is not a sum of two squares?", opts=["$21$", "$25$", "$45$", "$65$"], a=0, ex=r"$21 = 3\cdot 7$ has primes $\equiv 3 \pmod 4$ to odd powers."))
    A("sums-of-squares", H("proof", 3, r"Prove Fermat's two-squares theorem with Zagier's one-sentence involution on $\{(x,y,z): x^2 + 4yz = p\}$."))
    A("pythagorean", H("choice", 1, r"Which is a primitive Pythagorean triple?", opts=["$(20, 21, 29)$", "$(6, 8, 10)$", "$(9, 12, 15)$", "$(5, 11, 13)$"], a=0))
    A("continued-fractions", H("choice", 2, r"Which numbers have eventually periodic continued fractions?", opts=["quadratic irrationals", "all irrationals", "algebraic numbers", r"multiples of $\pi$"], a=0, ex="Lagrange's theorem (1770); Euler proved the converse."))
    A("pell", H("num", 2, r"The fundamental solution of $x^2 - 61y^2 = 1$ has $x = ?$", a=1766319049, ex=r"$(x,y) = (1766319049, 226153980)$, Fermat's famous challenge."))
    A("quadratic-forms", H("choice", 2, r"Which form of discriminant $-20$ is reduced?", opts=[r"$2x^2 + 2xy + 3y^2$", r"$3x^2 + 2xy + 2y^2$", r"$x^2 + 4xy + 9y^2$", r"$5x^2 + y^2$"], a=0, ex=r"Reduced means $|b| \le a \le c$; the forms of discriminant $-20$ are $x^2 + 5y^2$ and $2x^2 + 2xy + 3y^2$."))
    A("series", H("choice", 1, r"For real $p$, $\sum 1/n^p$ converges exactly when", opts=["$p > 1$", r"$p \ge 1$", "$p > 0$", "$p > 2$"], a=0))
    A("asymptotics", H("choice", 1, r"Which is true as $x \to \infty$?", opts=[r"$\log x = o(x^{\varepsilon})$ for every $\varepsilon > 0$", r"$x^{0.01} = O(\log^{100} x)$", r"$e^{\sqrt{\log x}} = O(\log x)$", r"$x/\log x \sim x$"], a=0))
    A("asymptotics", H("choice", 2, r"$\pi(x) \sim x/\log x$ means", opts=[r"$\pi(x)\log x / x \to 1$", r"$|\pi(x) - x/\log x|$ is bounded", r"$\pi(x) \le x/\log x$", r"$\pi(x) - x/\log x \to 0$"], a=0))
    A("partial-summation", H("proof", 3, r"Use Abel summation to deduce $\sum_{p \le x} 1/p = \log\log x + O(1)$ from $\sum_{p \le x} (\log p)/p = \log x + O(1)$."))
    A("complex-numbers", H("num", 1, r"$(1 + i)^8$.", a=16, hint=r"$1 + i = \sqrt2\,e^{i\pi/4}$."))
    A("residues", H("choice", 2, r"The argument principle counts", opts=["zeros minus poles inside the contour", "zeros on the contour", "poles only", "the winding of the contour around 0"], a=0))
    A("continuation", H("choice", 2, r"What does $\zeta(-1) = -\tfrac1{12}$ mean?", opts=[r"the analytic continuation of $\sum n^{-s}$ has value $-\tfrac1{12}$ at $s = -1$", r"$1 + 2 + 3 + \cdots$ converges to $-\tfrac1{12}$", "partial sums tend to $-1/12$", "it is a numerical coincidence"], a=0))
    A("gamma", H("num", 2, r"$\Gamma(1/2)^2$ is what multiple of $\pi$?", a=1, hint=r"$\int_{-\infty}^\infty e^{-x^2}dx = \sqrt\pi$."))
    A("fourier-poisson", H("choice", 2, r"The Fourier transform of $e^{-\pi x^2}$ is", opts=[r"$e^{-\pi \xi^2}$", r"$e^{-\xi^2}$", r"$1/(1 + \xi^2)$", r"$\sqrt\pi\, e^{-\xi^2}$"], a=0))
    A("mellin", H("choice", 3, r"Perron's formula expresses $\sum_{n\le x} a_n$ as", opts=[r"$\frac{1}{2\pi i}\int_{(c)} D(s)\frac{x^s}{s}\,ds$", r"$\int_0^x D(s)\,ds$", r"$D(x)$", r"$\sum_n a_n x^n$"], a=0))
    A("dirichlet-series", H("num", 2, r"The probability that a random positive integer is squarefree, to four decimals.", a=0.6079, tol=6e-4, ex=r"$\prod_p(1 - p^{-2}) = 1/\zeta(2) = 6/\pi^2$."))
    A("zeta", H("num", 1, r"$\zeta(0)$.", a=-0.5))
    A("zeta", H("num", 1, r"$\zeta(-1)$.", a=F(-1, 12), ex=r"The meaning of the slogan $1 + 2 + 3 + \cdots = -\tfrac1{12}$."))
    A("functional-equation", H("choice", 2, r"If $\rho = 0.3 + 20i$ were a zero of $\zeta$, which must also be a zero?", opts=[r"$0.7 + 20i$", r"$-0.3 + 20i$", r"$0.3 + 40i$", r"$1.3 + 20i$"], a=0, ex=r"Combine $s \leftrightarrow 1 - s$ with conjugation: $\rho \mapsto 1 - \bar\rho$. Such a zero would disprove RH."))
    A("chebyshev", H("proof", 3, r"Prove Chebyshev's bound $\psi(x) \le 2x\log 2 + O(\log x)$ using $\binom{2n}{n} \le 4^n$."))
    A("mertens", H("choice", 3, r"Mertens' third theorem says $\prod_{p\le x}(1 - 1/p) \sim$", opts=[r"$e^{-\gamma}/\log x$", r"$1/\log x$", r"$6/\pi^2$", r"$e^{\gamma}\log x$"], a=0))
    A("pnt", H("choice", 1, "The key step in the 1896 proofs of the prime number theorem is", opts=[r"$\zeta(1 + it) \ne 0$", "assuming RH", "all zeros are real", r"$\zeta(2) = \pi^2/6$"], a=0))
    A("nontrivial-zeros", H("num", 2, r"How many zeros have $0 < \operatorname{Im}\rho < 50$?", a=10, ex="$14.13, 21.02, 25.01, 30.42, 32.94, 37.59, 40.92, 43.33, 48.01, 49.77$, all on the line."))
    A("explicit-formula", H("choice", 2, r"A zero $\rho = \beta + i\gamma$ contributes to $\psi(x) - x$ a term of size", opts=[r"$x^{\beta}$", r"$x^{\gamma}$", r"$\log x$", "independent of $x$"], a=0, ex=r"$|x^\rho/\rho| = x^\beta/|\rho|$."))
    A("explicit-formula", H("num", 2, r"The constant term $\log 2\pi$ in the explicit formula, to three decimals.", a=1.8379, tol=6e-4))
    A("zero-free-region", H("num", 1, r"Minimum of $3 + 4\cos\theta + \cos 2\theta$.", a=0, hint=r"$\cos 2\theta = 2\cos^2\theta - 1$.", ex=r"$2(1 + \cos\theta)^2 \ge 0$."))
    A("zero-free-region", H("choice", 2, r"What do the 1899 and 1958 zero-free regions have in common?", opts=[r"their width tends to $0$ as $|t| \to \infty$", "they fail for L-functions", "they exclude only real zeros", "they do not imply the prime number theorem"], a=0, ex="Which is why a fixed-width region, the quasi-Riemann hypothesis, was a separate problem."))
    A("dirichlet-characters", H("choice", 2, r"Orthogonality of characters is used to", opts=["isolate one residue class $a \\bmod q$", "prove $\\zeta(2) = \\pi^2/6$", "count zeros of $\\zeta$", "factor integers"], a=0))
    A("gauss-sums", H("proof", 3, r"Prove $|g(\chi)|^2 = q$ for a primitive character $\chi$ modulo $q$."))
    A("l-functions", H("num", 2, r"$L(1,\chi_{-4}) = 1 - \tfrac13 + \tfrac15 - \cdots$ is what multiple of $\pi$?", a=F(1, 4), ex="Leibniz's series."))
    A("l-functions", H("choice", 3, r"Dirichlet's theorem needs which fact?", opts=[r"$L(1,\chi) \ne 0$ for every nonprincipal $\chi$", "GRH", r"$L(s,\chi)$ has no zeros", "the prime number theorem"], a=0))
    A("class-number-formula", H("choice", 3, r"Why do Siegel zeros connect to class numbers?", opts=[r"a zero $\beta$ near $1$ forces $L(1,\chi_D)$, hence $h(D)$, to be small", "class numbers are zeros", r"$h(D) = \beta$", "they are unrelated"], a=0))
    A("siegel-zeros", H("choice", 2, "Siegel zeros can occur only for", opts=["real (quadratic) characters", "all complex characters", r"$\zeta$ only", "Hecke L-functions only"], a=0, ex="For complex characters the classical zero-free region already excludes real exceptional zeros."))
    A("siegel-zeros", H("choice", 2, "The weakness of Siegel's theorem is that", opts=["its constant is ineffective", "it contradicts the prime number theorem", r"it holds only for prime $q$", "it assumes RH"], a=0))
    A("siegel-walfisz", H("choice", 3, r"Siegel–Walfisz gives uniform results for moduli up to", opts=[r"$(\log x)^A$", r"$x^{1/2}$", r"$x$", r"$\sqrt{\log\log x}$"], a=0))
    A("sieve-basics", H("choice", 2, "Brun's theorem (1919) states that", opts=[r"$\sum 1/p$ over twin primes converges", "there are infinitely many twin primes", "every even number is a sum of two primes", "twin primes have density zero but sum diverges"], a=0))
    A("selberg-sieve", H("choice", 3, "The Selberg sieve chooses weights $\\lambda_d$ by", opts=["minimising a quadratic form", "setting $\\lambda_d = \\mu(d)$", "random choice", "the circle method"], a=0))
    A("large-sieve", H("choice", 3, r"The large sieve constant in $\sum_q \sum_a |S(a/q)|^2 \le \Delta \sum |a_n|^2$ can be taken as", opts=[r"$N + Q^2$", r"$NQ$", r"$N^2 + Q$", r"$\log N$"], a=0))
    A("bombieri-vinogradov", H("choice", 3, "Bombieri–Vinogradov is often described as", opts=["GRH on average over moduli", "a proof of GRH", "a zero-free region", "a result on twin primes"], a=0))
    A("bounded-gaps", H("choice", 2, "The best known unconditional bound for $\\liminf (p_{n+1} - p_n)$ is", opts=["$246$", "$2$", "$70{,}000{,}000$", "$600$"], a=0, ex="Zhang's 2013 bound was $7 \\times 10^7$; Maynard and Polymath8 reduced it to $246$."))
    A("exponential-sums", H("proof", 3, r"Prove Weyl's criterion: $(x_n)$ is equidistributed mod 1 iff $\frac1N\sum_{n\le N} e(hx_n) \to 0$ for every integer $h \ne 0$."))
    A("circle-method", H("choice", 3, "Why does the circle method prove three-primes Goldbach but not two?", opts=["minor-arc bounds beat the main term with three exponential sums but not with two", "two primes have no major arcs", "the singular series vanishes for two", "computers cannot check two"], a=0))
    A("ternary-goldbach", H("choice", 1, "Who proved every odd number greater than 5 is a sum of three primes?", opts=["Helfgott (2013)", "Vinogradov (1937)", "Goldbach (1742)", "Hardy and Littlewood (1923)"], a=0, ex="Vinogradov proved it for sufficiently large odd numbers."))
    A("waring", H("num", 1, r"$g(3)$, the number of cubes every positive integer needs at most.", a=9))
    A("moments", H("proof", 4, r"Summarise how an amplifier boosts one character in a family average and why that helps detect an exceptional zero. Post for discussion."))
    A("moments", H("choice", 3, r"$\int_0^T |\zeta(\tfrac12 + it)|^2\,dt \sim$", opts=[r"$T\log T$", r"$T$", r"$T^2$", r"$T(\log T)^4/(2\pi^2)$"], a=0, ex=r"Hardy–Littlewood. The fourth moment is $\frac{T}{2\pi^2}(\log T)^4$ (Ingham)."))
    A("zero-density", H("choice", 3, r"Zero-density estimates say that zeros with real part $\ge \sigma > \tfrac12$ are", opts=["rare: $N(\\sigma,T) = o(T)$", "absent", "dense", "all real"], a=0))
    A("lindelof", H("choice", 3, r"The convexity bound for $\zeta(\tfrac12 + it)$ is", opts=[r"$|t|^{1/4 + \varepsilon}$", r"$|t|^{1/2}$", r"$\log |t|$", r"$|t|^{\varepsilon}$"], a=0))
    A("pair-correlation", H("choice", 2, "Montgomery's pair correlation matches the eigenvalue statistics of", opts=["random Hermitian matrices (GUE)", "Poisson processes", "the harmonic oscillator", "random permutations"], a=0))
    A("gaussian-integers", H("choice", 1, r"Which prime stays prime in $\mathbb Z[i]$?", opts=["$7$", "$5$", "$13$", "$2$"], a=0, ex=r"$p \equiv 3 \pmod 4$ is inert; $2 = -i(1+i)^2$ ramifies."))
    A("eisenstein-integers", H("num", 1, r"How many units does $\mathbb Z[\omega]$ have?", a=6, ex=r"$\pm 1, \pm\omega, \pm\omega^2$."))
    A("eisenstein-integers", H("num", 2, r"Into how many prime ideals does $7$ split in $\mathbb Z[\omega]$?", a=2, ex=r"$7 = (3 + \omega)(3 + \omega^2)$."))
    A("ideals", H("choice", 2, r"Dedekind domains have unique factorization of", opts=["ideals into prime ideals", "elements into irreducibles", "units", "polynomials"], a=0))
    A("class-group", H("choice", 2, r"Which $d$ gives class number $1$ for $\mathbb Q(\sqrt{-d})$?", opts=["$163$", "$5$", "$15$", "$23$"], a=0, ex="Heegner numbers: $1, 2, 3, 7, 11, 19, 43, 67, 163$."))
    A("cyclotomic", H("choice", 2, r"Gauss's 17-gon is constructible because", opts=[r"$\varphi(17) = 16$ is a power of $2$", "$17$ is prime", r"$17 \equiv 1 \pmod 4$", r"$\mathbb Q(\zeta_{17})$ has class number 1"], a=0))
    A("cubic-characters", H("choice", 3, r"For a cubic character $\chi$ modulo $p$, $g(\chi)^3 =$", opts=[r"$p\,J(\chi,\chi)$", r"$p$", r"$-p$", r"$p^{3/2}$"], a=0))
    A("dedekind-zeta", H("choice", 2, r"$\zeta_K(s)$ for $K = \mathbb Q(\sqrt{-3})$ equals", opts=[r"$\zeta(s)\,L(s,\chi_{-3})$", r"$\zeta(s)^2$", r"$\zeta(2s)$", r"$L(s,\chi_{-4})$"], a=0))
    A("hecke-l", H("proof", 4, r"The 2026 manuscript transfers a zero-free half-plane from finite-order Hecke L-functions over $\mathbb Q(\sqrt{-3})$ to Dirichlet L-functions. Explain what connection makes this possible, using the manuscript and follow-up papers."))
    A("elliptic-curves", H("choice", 2, r"Hasse's theorem bounds $\#E(\mathbb F_p)$ within", opts=[r"$p + 1 \pm 2\sqrt p$", r"$p \pm 1$", r"$2p$", r"$p^2$"], a=0))
    A("primality", H("num", 1, r"The smallest Carmichael number.", a=561, ex=r"$561 = 3\cdot 11\cdot 17$, and $2, 10, 16$ all divide $560$."))
    A("rsa", H("choice", 2, "RSA would be broken by an efficient algorithm for", opts=["factoring $n$", "computing $\\gcd$s", "primality testing", "modular exponentiation"], a=0))
    A("discrete-log", H("choice", 2, "Baby-step giant-step solves the discrete log modulo $p$ in about", opts=[r"$\sqrt p$ steps", "$p$ steps", r"$\log p$ steps", r"$p^2$ steps"], a=0))
    A("rh", H("choice", 2, "Which statement is equivalent to the Riemann hypothesis?", opts=[r"$\psi(x) = x + O(x^{1/2 + \varepsilon})$ for every $\varepsilon > 0$", r"$\pi(x) \sim x/\log x$", r"$\zeta(1 + it) \ne 0$", r"$\zeta(s) \ne 0$ for $\operatorname{Re}s > \tfrac78$"], a=0, ex="The second and third are the prime number theorem; the fourth is quasi-RH with $7/8$."))
    A("rh", H("proof", 4, r"Using the explicit formula, sketch why RH implies $\psi(x) = x + O(\sqrt x \log^2 x)$."))
    A("grh", H("choice", 3, "Under GRH, the Miller–Rabin test becomes deterministic using bases up to", opts=[r"$2(\log n)^2$", r"$\sqrt n$", r"$n/2$", "$100$"], a=0, ex="Bach's bound."))
    A("quasi-rh", H("num", 1, r"The manuscript's zero-free half-plane is $\operatorname{Re}s > \theta$ with $\theta =$", a=F(7, 8)))
    A("quasi-rh", H("num", 2, r"With the functional equation, nontrivial zeros lie in $\theta' \le \operatorname{Re}\rho \le \tfrac78$. What is the width of that strip?", a=F(3, 4), hint=r"$\rho$ zero implies $1 - \bar\rho$ zero.", ex=r"$[\tfrac18, \tfrac78]$, width $\tfrac34$."))
    A("quasi-rh", H("proof", 5, r"Compare a fixed-width zero-free region with de la Vallée Poussin's shrinking one: what error term for $\psi(x) - x$ does each give through the explicit formula? Post your derivation."))
    A("no-siegel", H("choice", 2, r"If quasi-RH with $\tfrac78$ holds, why are Siegel zeros excluded?", opts=[r"a real zero near $1$ would lie in $\operatorname{Re}s > \tfrac78$", "Siegel zeros lie on the critical line", "the functional equation forbids real zeros", r"Siegel zeros only occur for $\zeta$"], a=0))
    A("no-siegel", H("proof", 5, r"If there are no Siegel zeros, how do the constants in the Siegel–Walfisz theorem change? Write it up for discussion."))
    A("twin-primes", H("choice", 3, "The known barrier for sieve methods on twin primes is", opts=["the parity problem", "the Riemann hypothesis", "the circle method", "Siegel zeros"], a=0))
    A("goldbach", H("choice", 1, "Goldbach's conjecture first appeared in", opts=["a 1742 letter to Euler", "Euclid's Elements", "Riemann's 1859 paper", "Hardy and Littlewood (1923)"], a=0))

hand()

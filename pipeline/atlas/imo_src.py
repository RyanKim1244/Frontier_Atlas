# IMO number theory problems, 1959–2026. Statements follow the official wording (cross-checked against the
# compfiles Lean statements, Apache-2.0). Only statements: solutions are deliberately not included yet.
IMO = []
def imo(year, n, concepts, q):
    IMO.append(dict(year=year, pos=n, concepts=concepts, q=q.strip()))

imo(1959, 1, ["divisibility"], r"Prove that the fraction $\dfrac{21n+4}{14n+3}$ is irreducible for every natural number $n$.")
imo(1960, 1, ["digits-bases", "diophantine"], r"Determine all three-digit numbers $N$ having the property that $N$ is divisible by $11$, and $N/11$ is equal to the sum of the squares of the digits of $N$.")
imo(1962, 1, ["digits-bases", "congruences"], r"""Find the smallest natural number $n$ which has the following properties:

(a) its decimal representation has $6$ as the last digit;

(b) if the last digit $6$ is erased and placed in front of the remaining digits, the resulting number is four times as large as the original number $n$.""")
imo(1964, 1, ["order-primroot", "congruences"], r"""(a) Find all positive integers $n$ for which $2^n-1$ is divisible by $7$.

(b) Prove that there is no positive integer $n$ for which $2^n+1$ is divisible by $7$.""")
imo(1967, 3, ["binomial-factorial", "divisibility"], r"Let $k, m, n$ be natural numbers such that $m+k+1$ is a prime greater than $n+1$. Let $c_s = s(s+1)$. Prove that the product $(c_{m+1}-c_k)(c_{m+2}-c_k)\cdots(c_{m+n}-c_k)$ is divisible by the product $c_1c_2\cdots c_n$.")
imo(1968, 2, ["digits-bases", "diophantine"], r"Find all natural numbers $x$ such that the product of their digits (in decimal notation) is equal to $x^2-10x-22$.")
imo(1969, 1, ["integer-polynomials", "fta"], r"Prove that there are infinitely many natural numbers $a$ with the following property: the number $z = n^4 + a$ is not prime for any natural number $n$.")
imo(1970, 4, ["fta", "congruences"], r"Find the set of all positive integers $n$ with the property that the set $\{n, n+1, n+2, n+3, n+4, n+5\}$ can be partitioned into two sets such that the product of the numbers in one set equals the product of the numbers in the other set.")
imo(1971, 3, ["fermat-euler", "divisibility"], r"Prove that the set of integers of the form $2^k-3$ $(k = 2, 3, \ldots)$ contains an infinite subset in which every two members are relatively prime.")
imo(1972, 3, ["binomial-factorial", "p-adic-valuation"], r"Let $m$ and $n$ be arbitrary non-negative integers. Prove that $\dfrac{(2m)!\,(2n)!}{m!\,n!\,(m+n)!}$ is an integer. ($0! = 1$.)")
imo(1974, 3, ["binomial-factorial", "congruences"], r"Prove that for every positive integer $n$ the number $\displaystyle\sum_{k=0}^{n}\binom{2n+1}{2k+1}2^{3k}$ is not divisible by $5$.")
imo(1975, 4, ["digits-bases", "congruences"], r"When $4444^{4444}$ is written in decimal notation, the sum of its digits is $A$. Let $B$ be the sum of the digits of $A$. Find the sum of the digits of $B$. ($A$ and $B$ are written in decimal notation.)")
imo(1976, 3, ["diophantine"], r"A rectangular box can be filled completely with unit cubes. If one places as many cubes as possible, each with volume $2$, in the box, so that their edges are parallel to the edges of the box, one can fill exactly $40\%$ of the box. Determine the possible dimensions of all such boxes.")
imo(1976, 4, ["combinatorial-nt"], r"Determine, with proof, the largest number which is the product of positive integers whose sum is $1976$.")
imo(1977, 3, ["fta", "ideals"], r"Let $n$ be a given integer $> 2$, and let $V_n$ be the set of integers $1 + kn$, where $k = 1, 2, \ldots$. A number $m \in V_n$ is called indecomposable in $V_n$ if there do not exist numbers $p, q \in V_n$ such that $pq = m$. Prove that there exists a number $r \in V_n$ that can be expressed as the product of elements indecomposable in $V_n$ in more than one way. (Products which differ only in the order of their factors will be considered the same.)")
imo(1977, 5, ["diophantine", "sums-of-squares"], r"Let $a$ and $b$ be positive integers. When $a^2+b^2$ is divided by $a+b$, the quotient is $q$ and the remainder is $r$. Find all pairs $(a,b)$ such that $q^2 + r = 1977$.")
imo(1978, 1, ["congruences", "order-primroot", "crt"], r"$m$ and $n$ are natural numbers with $1 \le m < n$. In their decimal representations, the last three digits of $1978^m$ are equal, respectively, to the last three digits of $1978^n$. Find $m$ and $n$ such that $m+n$ has its least value.")
imo(1979, 1, ["mod-inverse", "congruences"], r"Let $p$ and $q$ be natural numbers such that $$\frac pq = 1 - \frac12 + \frac13 - \frac14 + \cdots - \frac{1}{1318} + \frac{1}{1319}.$$ Prove that $p$ is divisible by $1979$.")
imo(1981, 4, ["divisibility", "fta"], r"""(a) For which values of $n > 2$ is there a set of $n$ consecutive positive integers such that the largest number in the set is a divisor of the least common multiple of the remaining $n-1$ numbers?

(b) For which values of $n > 2$ is there exactly one set having the stated property?""")
imo(1982, 4, ["diophantine", "congruences", "cyclotomic"], r"Prove that if $n$ is a positive integer such that the equation $$x^3 - 3xy^2 + y^3 = n$$ has a solution in integers $(x,y)$, then it has at least three such solutions. Show that the equation has no solutions in integers when $n = 2891$.")
imo(1983, 3, ["bezout", "diophantine"], r"Let $a$, $b$ and $c$ be positive integers, no two of which have a common divisor greater than $1$. Show that $2abc - ab - bc - ca$ is the largest integer which cannot be expressed in the form $xbc + yca + zab$, where $x$, $y$ and $z$ are non-negative integers.")
imo(1984, 2, ["integer-polynomials", "p-adic-valuation", "congruences"], r"""Find one pair of positive integers $a$ and $b$ such that:

(i) $ab(a+b)$ is not divisible by $7$;

(ii) $(a+b)^7 - a^7 - b^7$ is divisible by $7^7$.

Justify your answer.""")
imo(1984, 6, ["divisibility", "p-adic-valuation"], r"Let $a$, $b$, $c$ and $d$ be odd integers such that $0 < a < b < c < d$ and $ad = bc$. Prove that if $a + d = 2^k$ and $b + c = 2^m$ for some integers $k$ and $m$, then $a = 1$.")
imo(1985, 4, ["fta", "combinatorial-nt"], r"Given a set $M$ of $1985$ distinct positive integers, none of which has a prime divisor greater than $23$, prove that $M$ contains a subset of $4$ elements whose product is the $4$th power of an integer.")
imo(1986, 1, ["congruences", "diophantine"], r"Let $d$ be any positive integer not equal to $2$, $5$ or $13$. Show that one can find distinct $a$, $b$ in the set $\{2, 5, 13, d\}$ such that $ab - 1$ is not a perfect square.")
imo(1987, 6, ["quadratic-forms", "class-group"], r"Let $n$ be an integer greater than or equal to $2$. Prove that if $k^2 + k + n$ is prime for all integers $k$ such that $0 \le k \le \sqrt{n/3}$, then $k^2 + k + n$ is prime for all integers $k$ such that $0 \le k \le n-2$.")
imo(1988, 6, ["vieta-jumping", "diophantine"], r"Let $a$ and $b$ be positive integers such that $ab + 1$ divides $a^2 + b^2$. Show that $\dfrac{a^2+b^2}{ab+1}$ is the square of an integer.")
imo(1989, 5, ["crt"], r"Prove that for each positive integer $n$ there exist $n$ consecutive positive integers none of which is an integral power of a prime number.")
imo(1990, 3, ["order-primroot", "lte-zsigmondy"], r"Determine all integers $n > 1$ such that $\dfrac{2^n+1}{n^2}$ is an integer.")
imo(1990, 4, ["integer-functional-eq", "fta"], r"Let $\mathbb Q^+$ be the set of positive rational numbers. Construct a function $f : \mathbb Q^+ \to \mathbb Q^+$ such that $$f(x f(y)) = \frac{f(x)}{y}$$ for all $x, y \in \mathbb Q^+$.")
imo(1990, 5, ["combinatorial-nt", "fta"], r"""Given an initial integer $n_0 > 1$, two players, $A$ and $B$, choose integers $n_1, n_2, n_3, \ldots$ alternately according to the following rules. Knowing $n_{2k}$, $A$ chooses any integer $n_{2k+1}$ such that $n_{2k} \le n_{2k+1} \le n_{2k}^2$. Knowing $n_{2k+1}$, $B$ chooses any integer $n_{2k+2}$ such that $n_{2k+1}/n_{2k+2}$ is a prime raised to a positive integer power. Player $A$ wins the game by choosing the number $1990$; player $B$ wins by choosing the number $1$.

For which $n_0$ does (a) $A$ have a winning strategy? (b) $B$ have a winning strategy? (c) neither player have a winning strategy?""")
imo(1991, 2, ["arithmetic-functions", "divisibility"], r"Let $n > 6$ be an integer and $a_1, a_2, \ldots, a_k$ be all the natural numbers less than $n$ and relatively prime to $n$. If $$a_2 - a_1 = a_3 - a_2 = \cdots = a_k - a_{k-1} > 0,$$ prove that $n$ must be either a prime number or a power of $2$.")
imo(1991, 3, ["combinatorial-nt", "fta"], r"Let $S = \{1, 2, 3, \ldots, 280\}$. Find the smallest integer $n$ such that each $n$-element subset of $S$ contains five numbers which are pairwise relatively prime.")
imo(1992, 1, ["divisibility", "diophantine"], r"Find all integers $a$, $b$, $c$ with $1 < a < b < c$ such that $(a-1)(b-1)(c-1)$ is a divisor of $abc - 1$.")
imo(1992, 6, ["sums-of-squares", "combinatorial-nt"], r"""For each positive integer $n$, $S(n)$ is defined to be the greatest integer such that, for every positive integer $k \le S(n)$, $n^2$ can be written as the sum of $k$ positive squares.

(a) Prove that $S(n) \le n^2 - 14$ for each $n \ge 4$.

(b) Find an integer $n$ such that $S(n) = n^2 - 14$.

(c) Prove that there are infinitely many integers $n$ such that $S(n) = n^2 - 14$.""")
imo(1994, 3, ["digits-bases", "binomial-factorial"], r"For any positive integer $k$, let $f(k)$ be the number of elements in the set $\{k+1, k+2, \ldots, 2k\}$ whose base-$2$ representation has precisely three $1$s. (a) Prove that, for each positive integer $m$, there exists at least one positive integer $k$ such that $f(k) = m$. (b) Determine all positive integers $m$ for which there exists exactly one $k$ with $f(k) = m$.")
imo(1994, 4, ["divisibility", "diophantine"], r"Determine all ordered pairs $(m,n)$ of positive integers such that $\dfrac{n^3+1}{mn-1}$ is an integer.")
imo(1994, 6, ["combinatorial-nt", "fta"], r"Show that there exists a set $A$ of positive integers with the following property: for any infinite set $S$ of primes there exist two positive integers $m \in A$ and $n \notin A$ each of which is a product of $k$ distinct elements of $S$ for some $k \ge 2$.")
imo(1995, 6, ["combinatorial-nt", "cyclotomic"], r"Let $p$ be an odd prime number. How many $p$-element subsets $A$ of $\{1, 2, \ldots, 2p\}$ are there, the sum of whose elements is divisible by $p$?")
imo(1996, 4, ["diophantine", "quadratic-residues"], r"The positive integers $a$ and $b$ are such that the numbers $15a + 16b$ and $16a - 15b$ are both squares of positive integers. What is the least possible value that can be taken on by the smaller of these two squares?")
imo(1996, 6, ["bezout", "combinatorial-nt"], r"""Let $p$, $q$, $n$ be three positive integers with $p + q < n$. Let $(x_0, x_1, \ldots, x_n)$ be an $(n+1)$-tuple of integers satisfying the following conditions:

(a) $x_0 = x_n = 0$;

(b) for each $i$ with $1 \le i \le n$, either $x_i - x_{i-1} = p$ or $x_i - x_{i-1} = -q$.

Show that there exist indices $i < j$ with $(i,j) \ne (0,n)$, such that $x_i = x_j$.""")
imo(1997, 5, ["diophantine", "fta"], r"Find all pairs $(a,b)$ of integers $a \ge 1$, $b \ge 1$ that satisfy the equation $a^{b^2} = b^a$.")
imo(1998, 3, ["arithmetic-functions"], r"For any positive integer $n$, let $d(n)$ denote the number of positive divisors of $n$ (including $1$ and $n$ itself). Determine all positive integers $k$ such that $$\frac{d(n^2)}{d(n)} = k$$ for some $n$.")
imo(1998, 4, ["divisibility", "diophantine"], r"Determine all pairs $(a,b)$ of positive integers such that $ab^2 + b + 7$ divides $a^2b + a + b$.")
imo(1999, 4, ["order-primroot", "lte-zsigmondy"], r"Determine all pairs $(n,p)$ of positive integers such that $p$ is a prime, $n$ not exceeding $2p$, and $(p-1)^n + 1$ is divisible by $n^{p-1}$.")
imo(2000, 5, ["lte-zsigmondy", "order-primroot"], r"Does there exist a positive integer $n$ such that $n$ has exactly $2000$ prime divisors and $n$ divides $2^n + 1$?")
imo(2001, 6, ["divisibility", "diophantine"], r"Let $a, b, c, d$ be integers with $a > b > c > d > 0$. Suppose that $$ac + bd = (b + d + a - c)(b + d - a + c).$$ Prove that $ab + cd$ is not prime.")
imo(2002, 4, ["arithmetic-functions", "divisibility"], r"Let $n$ be an integer greater than $1$. The positive divisors of $n$ are $d_1, d_2, \ldots, d_k$, where $1 = d_1 < d_2 < \cdots < d_k = n$. Define $D = d_1d_2 + d_2d_3 + \cdots + d_{k-1}d_k$. Prove that $D < n^2$, and determine all $n$ for which $D$ is a divisor of $n^2$.")
imo(2003, 2, ["vieta-jumping", "diophantine"], r"Determine all pairs of positive integers $(a,b)$ such that $$\frac{a^2}{2ab^2 - b^3 + 1}$$ is a positive integer.")
imo(2003, 6, ["order-primroot", "cyclotomic"], r"Let $p$ be a prime number. Prove that there exists a prime number $q$ such that for every integer $n$, the number $n^p - p$ is not divisible by $q$.")
imo(2004, 6, ["digits-bases", "crt"], r"We call a positive integer alternating if every two consecutive digits in its decimal representation are of different parity. Find all positive integers $n$ such that $n$ has a multiple which is alternating.")
imo(2005, 4, ["fermat-euler", "congruences"], r"Consider the sequence $a_1, a_2, \ldots$ defined by $$a_n = 2^n + 3^n + 6^n - 1 \qquad (n = 1, 2, \ldots).$$ Determine all positive integers that are relatively prime to every term of the sequence.")
imo(2006, 4, ["diophantine"], r"Determine all pairs $(x,y)$ of integers such that $$1 + 2^x + 2^{2x+1} = y^2.$$")
imo(2006, 5, ["integer-polynomials"], r"Let $P(x)$ be a polynomial of degree $n > 1$ with integer coefficients, and let $k$ be a positive integer. Consider the polynomial $Q(x) = P(P(\ldots P(P(x))\ldots))$, where $P$ occurs $k$ times. Prove that there are at most $n$ integers $t$ such that $Q(t) = t$.")
imo(2007, 5, ["vieta-jumping", "quadratic-residues"], r"Let $a$ and $b$ be positive integers. Show that if $4ab - 1$ divides $(4a^2 - 1)^2$, then $a = b$.")
imo(2008, 3, ["quadratic-residues", "prime-patterns"], r"Prove that there exist infinitely many positive integers $n$ such that $n^2 + 1$ has a prime divisor which is greater than $2n + \sqrt{2n}$.")
imo(2009, 1, ["divisibility", "congruences"], r"Let $n$ be a positive integer and let $a_1, \ldots, a_k$ $(k \ge 2)$ be distinct integers in the set $\{1, \ldots, n\}$ such that $n$ divides $a_i(a_{i+1} - 1)$ for $i = 1, \ldots, k-1$. Prove that $n$ does not divide $a_k(a_1 - 1)$.")
imo(2011, 1, ["divisibility"], r"Given any set $A = \{a_1, a_2, a_3, a_4\}$ of four distinct positive integers, we denote the sum $a_1 + a_2 + a_3 + a_4$ by $s_A$. Let $n_A$ denote the number of pairs $(i,j)$ with $1 \le i < j \le 4$ for which $a_i + a_j$ divides $s_A$. Find all sets $A$ of four distinct positive integers for which $n_A$ achieves its largest possible value.")
imo(2011, 5, ["integer-functional-eq", "divisibility"], r"Let $f$ be a function from the set of integers to the set of positive integers. Suppose that, for any two integers $m$ and $n$, the difference $f(m) - f(n)$ is divisible by $f(m-n)$. Prove that, for all integers $m$ and $n$ with $f(m) \le f(n)$, the number $f(n)$ is divisible by $f(m)$.")
imo(2013, 1, ["divisibility"], r"Prove that for any pair of positive integers $k$ and $n$, there exist $k$ positive integers $m_1, m_2, \ldots, m_k$ (not necessarily different) such that $$1 + \frac{2^k - 1}{n} = \left(1 + \frac{1}{m_1}\right)\left(1 + \frac{1}{m_2}\right)\cdots\left(1 + \frac{1}{m_k}\right).$$")
imo(2015, 2, ["diophantine", "p-adic-valuation"], r"Determine all triples $(a, b, c)$ of positive integers such that each of the numbers $$ab - c,\quad bc - a,\quad ca - b$$ is a power of $2$. (A power of $2$ is an integer of the form $2^n$, where $n$ denotes some non-negative integer.)")
imo(2016, 4, ["integer-polynomials", "crt"], r"A set of positive integers is called fragrant if it contains at least two elements and each of its elements has a prime factor in common with at least one of the other elements. Let $P(n) = n^2 + n + 1$. What is the least possible value of the positive integer $b$ such that there exists a non-negative integer $a$ for which the set $$\{P(a+1), P(a+2), \ldots, P(a+b)\}$$ is fragrant?")
imo(2017, 1, ["congruences", "quadratic-residues"], r"For each integer $a_0 > 1$, define the sequence $a_0, a_1, a_2, \ldots$ by $$a_{n+1} = \begin{cases}\sqrt{a_n} & \text{if } \sqrt{a_n} \text{ is an integer},\\ a_n + 3 & \text{otherwise},\end{cases}$$ for each $n \ge 0$. Determine all values of $a_0$ for which there is a number $A$ such that $a_n = A$ for infinitely many values of $n$.")
imo(2017, 6, ["crt", "integer-polynomials", "bezout"], r"An ordered pair $(x,y)$ of integers is a primitive point if the greatest common divisor of $x$ and $y$ is $1$. Given a finite set $S$ of primitive points, prove that there exist a positive integer $n$ and integers $a_0, a_1, \ldots, a_n$ such that, for each $(x,y)$ in $S$, we have $$a_0x^n + a_1x^{n-1}y + a_2x^{n-2}y^2 + \cdots + a_{n-1}xy^{n-1} + a_ny^n = 1.$$")
imo(2018, 5, ["p-adic-valuation", "divisibility"], r"Let $a_1, a_2, \ldots$ be an infinite sequence of positive integers. Suppose that there is an integer $N > 1$ such that, for each $n \ge N$, the number $$\frac{a_1}{a_2} + \frac{a_2}{a_3} + \cdots + \frac{a_{n-1}}{a_n} + \frac{a_n}{a_1}$$ is an integer. Prove that there is a positive integer $M$ such that $a_m = a_{m+1}$ for all $m \ge M$.")
imo(2019, 4, ["p-adic-valuation", "binomial-factorial"], r"Find all pairs $(k,n)$ of positive integers such that $$k! = (2^n - 1)(2^n - 2)(2^n - 4)\cdots(2^n - 2^{n-1}).$$")
imo(2022, 3, ["quadratic-forms"], r"Let $k$ be a positive integer and let $S$ be a finite set of odd prime numbers. Prove that there is at most one way (up to rotation and reflection) to place the elements of $S$ around a circle such that the product of any two neighbours is of the form $x^2 + x + k$ for some positive integer $x$.")
imo(2022, 5, ["p-adic-valuation", "binomial-factorial", "lte-zsigmondy"], r"Find all triples $(a, b, p)$ of positive integers with $p$ prime and $$a^p = b! + p.$$")
imo(2023, 1, ["arithmetic-functions", "divisibility"], r"Determine all composite integers $n > 1$ that satisfy the following property: if $d_1, d_2, \ldots, d_k$ are all the positive divisors of $n$ with $1 = d_1 < d_2 < \cdots < d_k = n$, then $d_i$ divides $d_{i+1} + d_{i+2}$ for every $1 \le i \le k-2$.")
imo(2023, 3, ["integer-polynomials"], r"For each integer $k \ge 2$, determine all infinite sequences of positive integers $a_1, a_2, \ldots$ for which there exists a polynomial $P$ of the form $P(x) = x^k + c_{k-1}x^{k-1} + \cdots + c_1x + c_0$, where $c_0, c_1, \ldots, c_{k-1}$ are non-negative integers, such that $$P(a_n) = a_{n+1}a_{n+2}\cdots a_{n+k}$$ for every integer $n \ge 1$.")
imo(2024, 2, ["order-primroot", "fermat-euler", "divisibility"], r"Determine all pairs $(a,b)$ of positive integers for which there exist positive integers $g$ and $N$ such that $$\gcd(a^n + b,\ b^n + a) = g$$ holds for all integers $n \ge N$.")
imo(2025, 3, ["integer-functional-eq", "fermat-euler", "order-primroot"], r"Let $\mathbb N$ denote the set of positive integers. A function $f : \mathbb N \to \mathbb N$ is said to be bonza if $$f(a) \ \text{divides}\ b^a - f(b)^{f(a)}$$ for all positive integers $a$ and $b$. Determine the smallest real constant $c$ such that $f(n) \le cn$ for all bonza functions $f$ and all positive integers $n$.")
imo(2026, 1, ["fta", "p-adic-valuation", "bezout"], r"""There are $2026$ integers greater than $1$ written on a blackboard, not necessarily different. In a move, Confucius chooses two integers $m > 1$ and $n > 1$ from different places on the blackboard and replaces these two integers with $\gcd(m,n)$ and $\operatorname{lcm}(m,n)/\gcd(m,n)$. He continues to make moves while it is possible to do so.

(a) Prove that, regardless of the choices of Confucius, after finitely many moves, exactly one integer $M$ on the blackboard is greater than $1$.

(b) Prove that the value of $M$ does not depend on the choices of Confucius.""")
imo(2026, 6, ["combinatorial-nt", "fta"], r"Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i) > 1$ for every $i = 1, 2, \ldots, n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T} = a_n + L$ for every positive integer $n$.")

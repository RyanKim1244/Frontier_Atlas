# The seven Millennium Prize Problems (Clay Mathematics Institute, 2000), stated in our own words.
CLAY = [
    dict(key="rh", title="The Riemann hypothesis", concepts=["rh", "nontrivial-zeros"], fields=["number-theory", "complex-analysis"], status="open",
         q=r"Prove that every non-trivial zero of the Riemann zeta function $\zeta(s)$ has real part $\tfrac12$."),
    dict(key="pnp", title="P versus NP", concepts=["p-vs-np"], fields=["computer-science", "logic"], status="open",
         q=r"Is every decision problem whose solutions can be verified in polynomial time also solvable in polynomial time? That is, is $\mathrm P = \mathrm{NP}$?"),
    dict(key="ns", title="Navier–Stokes existence and smoothness", concepts=["navier-stokes"], fields=["pde", "physics"], status="open",
         q=r"For the incompressible Navier–Stokes equations in $\mathbb R^3$, $$\partial_t u + (u\cdot\nabla)u = \nu\Delta u - \nabla p,\qquad \nabla\cdot u = 0,$$ prove or disprove that every smooth, divergence-free initial velocity field with sufficient decay gives a solution that stays smooth and has bounded energy for all time."),
    dict(key="ym", title="Yang–Mills existence and mass gap", concepts=["yang-mills"], fields=["physics"], status="open",
         q=r"Prove that for any compact simple gauge group $G$, a non-trivial quantum Yang–Mills theory exists on $\mathbb R^4$ satisfying axioms at least as strong as the Wightman axioms, and that it has a mass gap $\Delta > 0$."),
    dict(key="hodge", title="The Hodge conjecture", concepts=["hodge"], fields=["algebraic-geometry", "topology"], status="open",
         q=r"On a non-singular complex projective algebraic variety, is every Hodge class (a rational cohomology class of type $(p,p)$) a rational linear combination of the classes of algebraic subvarieties?"),
    dict(key="bsd", title="The Birch and Swinnerton-Dyer conjecture", concepts=["bsd", "elliptic-curves"], fields=["number-theory", "algebraic-geometry"], status="open",
         q=r"For an elliptic curve $E$ over $\mathbb Q$, prove that the rank of the group $E(\mathbb Q)$ of rational points equals the order of vanishing of the $L$-function $L(E,s)$ at $s = 1$."),
    dict(key="poincare", title="The Poincaré conjecture", concepts=["poincare"], fields=["topology", "geometry"], status="solved", slabel="Proved",
         q=r"Is every simply connected, closed $3$-manifold homeomorphic to the $3$-sphere?",
         notes="Proved by Grigori Perelman in 2002–03 using Richard Hamilton's Ricci flow with surgery. The Clay Institute awarded the prize in 2010; Perelman declined it."),
]

## -*- encoding: utf-8 -*-
"""
This file (./float_doctest.sage) was *autogenerated* from ./float.tex,
with sagetex.sty version 2011/05/27 v2.3.1.
It contains the contents of all the sageexample environments from this file.
You should be able to doctest this file with:
sage -t ./float_doctest.sage
It is always safe to delete this file; it is not used in typesetting your
document.

Sage example in ./float.tex, line 127::

    sage: xrdf = RDF(3.0)

Sage example in ./float.tex, line 137::

    sage: R100 = RealField(100) # précision : 100 bits.
    sage: x100 = R100(3/8); x100
    0.37500000000000000000000000000

Sage example in ./float.tex, line 148::

    sage: Rdefaut = RealField()  # précision par défaut de 53 bits
    sage: xdefaut = Rdefaut(2/3)

Sage example in ./float.tex, line 154::

    sage: xrdf.prec()
    53
    sage: x100.prec()
    100
    sage: xdefaut.prec()
    53

Sage example in ./float.tex, line 168::

    sage: x = 1.0; print type(x)
    <type 'sage.rings.real_mpfr.RealLiteral'>
    sage: x.prec()
    53

Sage example in ./float.tex, line 182::

    sage: x = 1.0         # x appartient à RealField()
    sage: x = 0.1e+1      # idem : x appartient à RealField()
    sage: x = 1           # x est entier
    sage: x = RDF(1)      # x est un flottant double précision machine
    sage: x = RDF(1.)     # idem : x est un flottant double précision
    sage: x = RDF(0.1e+1) # idem
    sage: x = 4/3         # x est un nombre rationnel
    sage: R = RealField(20)
    sage: x = R(1)        # x est un flottant de précision 20 bits

Sage example in ./float.tex, line 194::

    sage: RDF(8/3)
    2.66666666667
    sage: R100 = RealField(100); R100(8/3)
    2.6666666666666666666666666667

Sage example in ./float.tex, line 202::

    sage: x = R100(8/3)
    sage: R = RealField(); R(x)
    2.66666666666667
    sage: RDF(x)
    2.66666666667

Sage example in ./float.tex, line 216::

    sage: 1.0/0.0
    +infinity
    sage: RDF(1)/RDF(0)
    +infinity
    sage: RDF(-1.0)/RDF(0.)
    -infinity

Sage example in ./float.tex, line 225::

    sage: 0.0/0.0
    NaN
    sage: RDF(0.0)/RDF(0.0)
    NaN

Sage example in ./float.tex, line 256::

    sage: R2 = RealField(2)

Sage example in ./float.tex, line 303::

    sage: x2 = R2(1.); x2.ulp()
    0.50
    sage: xr = 1.; xr.ulp()
    2.22044604925031e-16

Sage example in ./float.tex, line 356::

    sage: a = 10000.0; b = 9999.5; c = 0.1; c
    0.100000000000000
    sage: a1 = a+c # on perturbe a
    sage: a1-b
    0.600000000000364

Sage example in ./float.tex, line 373::

    sage: a = 1.0; b = 10.0^4; c = 1.0
    sage: delta = b^2-4*a*c
    sage: x = (-b-sqrt(delta))/(2*a); y = (-b+sqrt(delta))/(2*a)
    sage: x, y
    (-9999.99990000000, -0.000100000001111766)

Sage example in ./float.tex, line 382::

    sage: x+y+b/a
    0.000000000000000
    sage: x*y-c/a
    1.11766307320238e-9

Sage example in ./float.tex, line 394::

    sage: y = (c/a)/x; y
    -0.000100000001000000
    sage: x+y+b/a
    0.000000000000000

Sage example in ./float.tex, line 410::

    sage: x1 = R2(1/2); x2 = R2(4); x3 = R2(-4)
    sage: x1, x2, x3
    (0.50, 4.0, -4.0)
    sage: x1+(x2+x3)
    0.50
    sage: (x1+x2)+x3
    0.00

Sage example in ./float.tex, line 431::

    sage: x = RDF(1/3)
    sage: for i in range(1,100): x = 4*x-1; print x
    0.333333333333
    0.333333333333
    0.333333333333
    ...
    -1.0
    -5.0
    -21.0
    -85.0
    -341.0
    -1365.0
    -5461.0
    -21845.0
    ...

Sage example in ./float.tex, line 461::

    sage: x = RDF(1/2)
    sage: for i in range(1,100): x = 3*x-1; print x
    0.5
    0.5
    0.5
    ...
    0.5

Sage example in ./float.tex, line 484::

    sage: x = RDF(1/3)

Sage example in ./float.tex, line 488::

    sage: x = 1/3

Sage example in ./float.tex, line 545::

    sage: def sumharmo(P):
    ....:    RFP = RealField(P)
    ....:    y = RFP(1.); x = RFP(0.); n = 1
    ....:    while x <> y:
    ....:        y = x; x += 1/n; n += 1
    ....:    return P, n, x

Sage example in ./float.tex, line 556::

    sage: sumharmo(2)
    (2, 5, 2.0)
    sage: sumharmo(20)
    (20, 131073, 12.631)

Sage example in ./float.tex, line 590::

    sage: def iter(y,delta,a,n):
    ....:     for i in range(0,n):
    ....:         y += delta
    ....:         delta *= a
    ....:     return y

Sage example in ./float.tex, line 600::

    sage: def exact(y,delta,a,n):
    ....:     return y+delta*(1-a^n)/(1-a)

Sage example in ./float.tex, line 608::

    sage: y0 = RDF(10^13); delta0 = RDF(1); a = RDF(1-10^(-8)); n = 100000
    sage: ii = iter(y0,delta0,a,n)
    sage: s = exact(10^13,1,1-10^(-8),n)
    sage: print "exact - sommation classique:", s-ii # abs tol 0.1
    exact - sommation classique: -45.5

Sage example in ./float.tex, line 618::

    sage: def sumcomp(y,delta,e,n,a):
    ....:     for i in range(0,n):
    ....:         b = y
    ....:         e += delta
    ....:         y = b+e
    ....:         e += (b-y)
    ....:         delta = a*delta # nouvelle valeur de delta
    ....:     return y

Sage example in ./float.tex, line 662::

    sage: c = sumcomp(y0,delta0,RDF(0.0),n,a)
    sage: print "exact-sommation compensee:", s-c
    exact-sommation compensee: 0.0

Sage example in ./float.tex, line 681::

    sage: x = CDF(2,1.); x
    2.0 + 1.0*I
    sage: y = CDF(20,0); y
    20.0

Sage example in ./float.tex, line 688::

    sage: z = ComplexDoubleElement(2.,1.); z
    2.0 + 1.0*I

Sage example in ./float.tex, line 697::

    sage: C = ComplexField(); C(2,3)
    2.00000000000000 + 3.00000000000000*I
    sage: C100 = ComplexField(100); C100(2,3)
    2.0000000000000000000000000000 + 3.0000000000000000000000000000*I

Sage example in ./float.tex, line 714::

    sage: R200 = RealField(200); R200.pi()
    3.1415926535897932384626433832795028841971693993751058209749
    sage: R200.euler_constant()
    0.57721566490153286060651209008240243104215933593992359880577

Sage example in ./float.tex, line 723::

    sage: x = RDF.pi()/2; x.cos() # approximation flottante de zero!
    6.12323399574e-17
    sage: x.cos().arccos() - x
    0.0

"""

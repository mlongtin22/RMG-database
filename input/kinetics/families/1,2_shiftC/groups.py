#!/usr/bin/env python
# encoding: utf-8

name = "1,2_shiftC/groups"
shortDesc = u""
longDesc = u"""
1,2-methyl shift from a Carbon to another Carbon.
Could possibly be generalized to include  1,2-methyl shift from an Oxygen to Carbon and vice versa.
1,2-methyl shift from Sulfur to Carbon has separate family (1,2_shiftS).
"""

template(reactants=["cCCJ"], products=["cCCJ"], ownReverse=True)

reversible = True
recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

boundaryAtoms = ["*1", "*3"]

entry(
    index = 0,
    label = "cCCJ",
    group = 
"""
1 *1 C u0 c0 {2,S}
2 *2 C u0 {1,S} {3,S}
3 *3 C u1 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "CJ",
    group = 
"""
1 *3 C u1
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "C",
    group = 
"""
1 *1 C u0 c0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "cCsCJ",
    group = 
"""
1 *1 C  u0 c0 {2,S}
2 *2 Cs u0 {1,S} {3,S}
3 *3 C  u1 {2,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "cCs(-HH)CJ",
    group = 
"""
1 *1 C  u0 c0 {2,S}
2 *2 Cs u0 {1,S} {3,S} {4,S} {5,S}
3 *3 C  u1 {2,S}
4    H  u0 {2,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "cCs(-HR!H)CJ",
    group = 
"""
1 *1 C   u0 c0 {2,S}
2 *2 Cs  u0 {1,S} {3,S} {4,S} {5,S}
3 *3 C   u1 {2,S}
4    H   u0 {2,S}
5    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "cCs(-R!HR!H)CJ",
    group = 
"""
1 *1 C   u0 c0 {2,S}
2 *2 Cs  u0 {1,S} {3,S} {4,S} {5,S}
3 *3 C   u1 {2,S}
4    R!H u0 {2,S}
5    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "cCdCJ",
    group = 
"""
1 *1 C  u0 c0 {2,S}
2 *2 Cd u0 {1,S} {3,S}
3 *3 C  u1 {2,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "CdsJ",
    group = 
"""
1 *3 Cd u1 {2,D}
2    C  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "CsJ",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    R  u0 {1,S}
3    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "CsJ-HH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "CsJ-CsH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "CsJ-CsCs",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "CsJ-SsH",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "CsJ-SsSs",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "CsJ-CsSs",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S}
2    Cs  u0 {1,S}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "CsJ-TwoDe",
    group = 
"""
1 *3 Cs               u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "CsJ-CdCd",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cd u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "CsJ-OneDe",
    group = 
"""
1 *3 Cs               u1 {2,S} {3,S}
2    R                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "CsJ-OneDeH",
    group = 
"""
1 *3 Cs               u1 {2,S} {3,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "CsJ-(CdCdCd)H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cd u0 {1,S} {4,D}
4    Cd u0 {3,D} {5,S}
5    Cd u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "CsJ-CdH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "CsJ-OneDeCs",
    group = 
"""
1 *3 Cs               u1 {2,S} {3,S}
2    Cs               u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "CsJ-CdCs",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "CsJ-OneDeSs",
    group = 
"""
1 *3 Cs            u1 {2,S} {3,S}
2    S2s           u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "CsJ-CdSs",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    Cd  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "CH3",
    group = 
"""
1 *1 C u0 c0 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "cCs(-HC)CJ",
    group = 
"""
1 *1 C   u0 c0 {2,S}
2 *2 Cs  u0 {1,S} {3,S} {4,S} {5,S}
3 *3 C   u1 {2,S}
4    H   u0 {2,S}
5    C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "CO",
    group = 
"""
1 *1 CO u0 c0
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "CO_O",
    group = 
"""
1 *1 CO u0 c0 {2,S}
2    O  u0 c0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: cCCJ
    L2: cCsCJ
        L3: cCs(-HH)CJ
        L3: cCs(-HR!H)CJ
            L4: cCs(-HC)CJ
        L3: cCs(-R!HR!H)CJ
    L2: cCdCJ
L1: CJ
    L2: CdsJ
    L2: CsJ
        L3: CsJ-HH
        L3: CsJ-CsH
        L3: CsJ-CsCs
        L3: CsJ-SsH
        L3: CsJ-SsSs
        L3: CsJ-CsSs
        L3: CsJ-TwoDe
            L4: CsJ-CdCd
        L3: CsJ-OneDe
            L4: CsJ-OneDeH
                L5: CsJ-(CdCdCd)H
                L5: CsJ-CdH
            L4: CsJ-OneDeCs
                L5: CsJ-CdCs
            L4: CsJ-OneDeSs
                L5: CsJ-CdSs
L1: C
    L2: CH3
    L2: CO
        L3: CO_O
"""
)

forbidden(
    label = "CC_shift",
    group =
"""
1    C u0 p0 c0 {2,[S,D,T,B]}
2 *1 C u0 p0 c0 {1,[S,D,T,B]} {3,S}
3 *2 C u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid carbon chains larger than methyl from participating in this family.
""",
)

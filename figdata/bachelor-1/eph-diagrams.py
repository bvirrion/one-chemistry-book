"""Potential-pH diagrams of water, iron, copper, zinc and chlorine (ch. 14),
computed from NBS-82 Gibbs energies of formation (ledger rows dfg:...).

Convention: every dissolved species, at a boundary, is at the working
concentration c counted in atoms of the element (c = 0.010 mol/L here, a
species with m atoms of the element at c/m); gases at 1 bar; solids of
activity 1.

Method: every species is written as formed from the element X in its
reference state,  X + o H2O -> species + h' H+ + n e-  (per atom of X).
At given (pH, E) the species of smallest
    g = [dfg(species) + RT ln a - o dfg(H2O)]/m + h' RT ln10 (-pH) - n F E
is the stable one. A boundary between i and j is the straight line
g_i = g_j; the script keeps the parts of each line where i and j are both
of smallest g, and writes them as segments separated by 'nan' rows.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _thermo import dfg, T  # noqa: E402
from _ledger import value  # noqa: E402

C = 0.010
F = value("const:F") / 1000          # kJ/(V mol)
RT = value("const:R") * T / 1000     # kJ/mol
L10 = RT * math.log(10)

# species: (name in the ledger, atoms of X m, O atoms o, H atoms h, charge q, dissolved?)
SYSTEMS = {
    "iron": [("Fe(cr)", 1, 0, 0, 0, False), ("Fe2+(ao)", 1, 0, 0, 2, True),
             ("Fe3+(ao)", 1, 0, 0, 3, True), ("Fe(OH)2(cr)", 1, 2, 2, 0, False),
             ("Fe(OH)3(cr)", 1, 3, 3, 0, False)],
    "copper": [("Cu(cr)", 1, 0, 0, 0, False), ("Cu+(ao)", 1, 0, 0, 1, True),
               ("Cu2+(ao)", 1, 0, 0, 2, True), ("Cu2O(cr)", 2, 1, 0, 0, False),
               ("CuO(cr)", 1, 1, 0, 0, False)],
    "zinc": [("Zn(cr)", 1, 0, 0, 0, False), ("Zn2+(ao)", 1, 0, 0, 2, True),
             ("Zn(OH)2(cr)", 1, 2, 2, 0, False), ("Zn(OH)4^2-(ao)", 1, 4, 4, -2, True)],
    "chlorine": [("Cl-(ao)", 1, 0, 0, -1, True), ("Cl2(ao)", 2, 0, 0, 0, True),
                 ("HClO(ao)", 1, 1, 1, 0, True), ("ClO-(ao)", 1, 1, 0, -1, True)],
}
# reference state of the element, per atom: Cl is written from Cl2(g)/2 = 0
ELEMENT_REF = {"iron": 0.0, "copper": 0.0, "zinc": 0.0, "chlorine": 0.0}


def coefficients(sp, m, o, h, q, dissolved, c=C):
    """g = a0 + a1 pH + a2 E (kJ per atom of the element)."""
    act = c / m if dissolved else 1.0
    g0 = (dfg(sp) + RT * math.log(act) - o * dfg("H2O(l)")) / m
    hp = (2 * o - h) / m              # H+ released per atom
    n = (q + 2 * o - h) / m           # electrons released per atom (oxidation state)
    return g0, -hp * L10, -n * F


def stable(system, ph, e, c=C):
    gs = [sum(k * v for k, v in zip(coefficients(*s, c=c), (1, ph, e))) for s in SYSTEMS[system]]
    return min(range(len(gs)), key=gs.__getitem__), gs


def boundaries(system, c=C, ph_range=(0, 14), e_range=(-1.6, 2.0), steps=2800):
    sp = SYSTEMS[system]
    co = [coefficients(*s, c=c) for s in sp]
    segs = []
    for i in range(len(sp)):
        for j in range(i + 1, len(sp)):
            a0, a1, a2 = (co[i][k] - co[j][k] for k in range(3))
            pts = []
            if abs(a2) > 1e-12:            # E = -(a0 + a1 pH)/a2
                for s in range(steps + 1):
                    ph = ph_range[0] + (ph_range[1] - ph_range[0]) * s / steps
                    pts.append((ph, -(a0 + a1 * ph) / a2))
            elif abs(a1) > 1e-12:          # vertical line pH = -a0/a1
                ph = -a0 / a1
                for s in range(steps + 1):
                    pts.append((ph, e_range[0] + (e_range[1] - e_range[0]) * s / steps))
            run = []
            for ph, e in pts:
                ok = ph_range[0] <= ph <= ph_range[1] and e_range[0] <= e <= e_range[1]
                if ok:
                    _, gs = stable(system, ph, e, c)
                    gmin = min(gs)
                    ok = gs[i] - gmin < 1e-6 and gs[j] - gmin < 1e-6
                if ok:
                    run.append((ph, e))
                elif run:
                    segs.append((sp[i][0], sp[j][0], run[0], run[-1]))
                    run = []
            if run:
                segs.append((sp[i][0], sp[j][0], run[0], run[-1]))
    return [s for s in segs if math.dist(s[2], s[3]) > 1e-3]


def water_lines(ph):
    """E of H+/H2 and O2/H2O at 1 bar."""
    e_o2 = -(2 * dfg("H2O(l)")) / (4 * F) - L10 / F * ph
    return -L10 / F * ph, e_o2


def rows(system):
    out = []
    for _, _, p, q in boundaries(system):
        out += [p, q, (float("nan"), float("nan"))]
    return out


def triple_point(system, a, b, d, c=C):
    """(pH, E) where species a, b and d (indices) have equal g."""
    co = [coefficients(*s, c=c) for s in SYSTEMS[system]]
    (p0, p1, p2), (q0, q1, q2) = ([co[a][k] - co[b][k] for k in range(3)],
                                  [co[b][k] - co[d][k] for k in range(3)])
    det = p1 * q2 - p2 * q1
    ph = (-p0 * q2 + p2 * q0) / det
    e = (-p1 * q0 + p0 * q1) / det
    return ph, e


def triple_point_cl2(c=C):
    """pH above which Cl2(aq) has no domain (it disproportionates)."""
    return triple_point("chlorine", 0, 1, 2, c)[0]


if __name__ == "__main__":
    for name in SYSTEMS:
        write_table(__file__, ("pH", "E"), rows(name), part=name, digits=5)
    write_table(__file__, ("pH", "H2", "O2"),
                [(p,) + water_lines(p) for p in (0, 14)], part="water", digits=5)

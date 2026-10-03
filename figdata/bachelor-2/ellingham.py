"""Ellingham diagram (chapter 6): standard Gibbs energy of oxidation per mole
of O2 against T.
- From JANAF Gibbs energies of formation (rows janafG:<oxide>.<T>, every
  200 K from 300 to 2100 K; the JANAF formation functions already include
  the changes of state of the elements and oxides);
- for ZnO and HgO (not in JANAF), in the Ellingham approximation from the
  CODATA key values, with the melting and boiling of the metal taken from the
  JANAF zinc table and the CODATA mercury rows: Delta_r G is the largest of
  the values computed with each phase of the metal (the metal reacts from its
  most stable phase).
Part a: the lines; part b: the Boudouard equilibrium C + CO2 = 2 CO."""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

R = value("const:R")
TS = [300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100]
# reaction per mole of O2: {oxide: multiplier of its DfG}; carbon and
# hydrogen lines as combinations
JANAF_LINES = {
    "Cu2O": {"Cu2O": 2},                 # 4 Cu + O2 = 2 Cu2O
    "FeO": {"FeO": 2},                   # 2 Fe + O2 = 2 FeO
    "Cr2O3": {"Cr2O3": 2 / 3},           # 4/3 Cr + O2 = 2/3 Cr2O3
    "SiO2": {"SiO2": 1},
    "TiO2": {"TiO2": 1},
    "Al2O3": {"Al2O3": 2 / 3},
    "MgO": {"MgO": 2},
    "CaO": {"CaO": 2},
    "C-CO": {"CO": 2},                   # 2 C + O2 = 2 CO
    "C-CO2": {"CO2": 1},                 # C + O2 = CO2
    "CO-CO2": {"CO2": 2, "CO": -2},      # 2 CO + O2 = 2 CO2
    "H2-H2O": {"H2O": 2},                # 2 H2 + O2 = 2 H2O(g)
}


def janaf_line(name):
    pts = []
    for T in TS:
        try:
            g = sum(m * value("janafG:%s.%d" % (sp, T)) for sp, m in JANAF_LINES[name].items())
        except KeyError:
            continue
        pts.append((T, g))
    return pts


def janaf_at(name, T):
    pts = janaf_line(name)
    return float(np.interp(T, [p[0] for p in pts], [p[1] for p in pts]))


def zinc_phases():
    """(DH, DS) of 2 Zn + O2 = 2 ZnO, kJ and kJ/K, with Zn solid, liquid,
    gas (Ellingham approximation in each)."""
    h0 = 2 * value("dfh:ZnO_cr")
    s0 = (2 * value("s0:ZnO_cr") - 2 * value("s0:Zn_cr") - value("s0:O2_g")) / 1000.0
    tm, tb = 692.73, 1180.173
    hfus = value("hT:Zn_l.692") - value("hT:Zn_cr.692")
    hvap = value("hT:Zn_g.1180") + value("dfh:Zn_g") - value("hT:Zn_l.1180")
    sol = (h0, s0)
    liq = (h0 - 2 * hfus, s0 - 2 * hfus / tm)
    gas = (liq[0] - 2 * hvap, liq[1] - 2 * hvap / tb)
    return sol, liq, gas


def mercury_phases():
    h0 = 2 * value("dfh:HgO_cr")
    s_l = (2 * value("s0:HgO_cr") - 2 * value("s0:Hg_l") - value("s0:O2_g")) / 1000.0
    s_g = (2 * value("s0:HgO_cr") - 2 * value("s0:Hg_g") - value("s0:O2_g")) / 1000.0
    return (h0, s_l), (h0 - 2 * value("dfh:Hg_g"), s_g)


def from_phases(phases, T):
    return max(h - T * s for h, s in phases)


def zno(T):
    return from_phases(zinc_phases(), T)


def hgo(T):
    return from_phases(mercury_phases(), T)


def crossing(f, g, lo, hi):
    """Temperature where f(T) = g(T), by bisection."""
    a, b = lo, hi
    for _ in range(100):
        m = 0.5 * (a + b)
        if (f(a) - g(a)) * (f(m) - g(m)) <= 0:
            b = m
        else:
            a = m
    return 0.5 * (a + b)


def zinc_carbon_temperature():
    return crossing(zno, lambda T: janaf_at("C-CO", T), 900, 1700)


def hgo_decomposition_temperature():
    return crossing(hgo, lambda T: 0.0, 400, 1000)


def boudouard_x_co(T, p_bar=1.0):
    """Mole fraction of CO over carbon, C + CO2 = 2 CO, total pressure p."""
    g = 2 * janaf_at_species("CO", T) - janaf_at_species("CO2", T)
    K = math.exp(-g * 1000.0 / (R * T))
    a = K / p_bar
    return (-a + math.sqrt(a * a + 4 * a)) / 2


def janaf_at_species(sp, T):
    xs = TS
    ys = [value("janafG:%s.%d" % (sp, t)) for t in TS]
    return float(np.interp(T, xs, ys))


if __name__ == "__main__":
    for name in JANAF_LINES:
        write_table(__file__, ("T", "G"), janaf_line(name), part="a-" + name)
    write_table(__file__, ("T", "G"), [(T, zno(T)) for T in range(300, 2101, 20)], part="a-ZnO")
    write_table(__file__, ("T", "G"), [(T, hgo(T)) for T in range(300, 1101, 20)], part="a-HgO")
    write_table(__file__, ("T", "xCO"), [(T, boudouard_x_co(T)) for T in range(500, 1501, 10)], part="b")

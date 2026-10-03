"""Standard molar entropy of zinc from 0 K to 1500 K (JANAF tables Zn-004,
Zn-005, ledger rows s0T:*): it rises with T, jumps at the melting point
(692.73 K) by DfusH/Tfus and at the boiling point (1180.173 K) by DvapH/Tb.
Between the tabulated points the curve is drawn with S(T2) = S(T1) +
Cp ln(T2/T1), Cp interpolated (in the solid below 300 K the tabulated
points are joined directly)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

TM, TB = 692.73, 1180.173
SOLID = [0, 100, 200, 250, 298.15, 400, 500, 600]
LIQUID = [800, 1000]
GAS = [1300, 1400, 1500]


def s_solid_points():
    pts = [(T, value("s0T:Zn_crl.%g" % T)) for T in SOLID]
    pts.append((TM, value("s0T:Zn_cr.692")))
    return pts


def s_liquid_points():
    pts = [(TM, value("s0T:Zn_l.692"))]
    pts += [(T, value("s0T:Zn_crl.%g" % T)) for T in LIQUID]
    pts.append((TB, value("s0T:Zn_l.1180")))
    return pts


def s_gas_points():
    pts = [(TB, value("s0T:Zn_g.1180"))]
    pts += [(T, value("s0T:Zn_g.%d" % T)) for T in GAS]
    return pts


def fusion_jump():
    """(Delta S at the melting point from the table, DfusH/Tfus)."""
    dh = (value("hT:Zn_l.692") - value("hT:Zn_cr.692")) * 1000.0
    return value("s0T:Zn_l.692") - value("s0T:Zn_cr.692"), dh / TM, dh


def vaporisation_jump():
    hl = value("hT:Zn_l.1180")
    hg = value("hT:Zn_g.1180") + value("dfh:Zn_g")   # same zero: Zn(cr) at 298.15 K
    dh = (hg - hl) * 1000.0
    return value("s0T:Zn_g.1180") - value("s0T:Zn_l.1180"), dh / TB, dh


def entropy_from_cp(T1, T2):
    """S(T2) - S(T1) for the solid between 300 and 600 K by integrating
    Cp/T with Cp linear between the tabulated values (Simpson on ln T)."""
    ts = [300.0, 400.0, 500.0, 600.0]
    cps = [value("cpT:Zn_cr.%d" % t) for t in ts]

    def cp(T):
        for i in range(len(ts) - 1):
            if ts[i] <= T <= ts[i + 1]:
                f = (T - ts[i]) / (ts[i + 1] - ts[i])
                return cps[i] + f * (cps[i + 1] - cps[i])
        raise ValueError(T)
    n = 400
    h = (T2 - T1) / n
    tot = 0.0
    for k in range(n + 1):
        T = T1 + k * h
        w = 1 if k in (0, n) else (4 if k % 2 else 2)
        tot += w * cp(T) / T
    return tot * h / 3


if __name__ == "__main__":
    write_table(__file__, ("T", "S"), s_solid_points(), part="solid")
    write_table(__file__, ("T", "S"), s_liquid_points(), part="liquid")
    write_table(__file__, ("T", "S"), s_gas_points(), part="gas")

"""Thermodynamics of the hydrogen-oxygen cell (chapter 9).
- a: standard cell voltage E = -Delta_r G / (2F) of H2 + 1/2 O2 = H2O against
  T, for liquid water (JANAF table H-063, 298-500 K) and for water vapour
  (table H-064, 298-1000 K);
- b: thermodynamic efficiency Delta_r G / Delta_r H of the same reaction (water
  vapour) against T, and the Carnot efficiency 1 - T0/T of a heat engine
  between T and T0 = 298.15 K (to 1500 K)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

F = value("const:F")
T0 = 298.15
LIQ = {298.15: "298", 300: "300", 400: "400", 500: "500"}
GAS = {298.15: "298", 300: "300", 400: "400", 500: "500", 600: "600", 700: "700",
       800: "800", 900: "900", 1000: "1000"}
GAS_HOT = {1100: "1100", 1300: "1300", 1500: "1500"}


def e_liquid():
    return [(T, -value("janafG:H2O_l.%s" % k) * 1000 / (2 * F)) for T, k in LIQ.items()]


def e_gas():
    return [(T, -value("janafG:H2O.%s" % k) * 1000 / (2 * F)) for T, k in GAS.items()]


def efficiency_gas():
    out = []
    for T, k in list(GAS.items()) + list(GAS_HOT.items()):
        if T == 298.15:
            continue
        g = value("janafG:H2O.%s" % k)
        h = value("janafdfH:H2O_g.%s" % k)
        out.append((T, g / h))
    return out


def standard_values():
    """Delta_r H, Delta_r G, T Delta_r S (kJ) and E (V) at 298.15 K, liquid water."""
    h = value("dfh:H2O-l")
    s = value("s0:H2O_l") - value("s0:H2_g") - 0.5 * value("s0:O2_g")
    g = h - T0 * s / 1000
    return h, g, T0 * s / 1000, -g * 1000 / (2 * F), s


if __name__ == "__main__":
    write_table(__file__, ("T", "E"), e_liquid(), part="a-liquid")
    write_table(__file__, ("T", "E"), e_gas(), part="a-gas")
    write_table(__file__, ("T", "eta"), efficiency_gas(), part="b")
    write_table(__file__, ("T", "eta"), [(T, 1 - T0 / T) for T in range(300, 1501, 10)], part="b-carnot")

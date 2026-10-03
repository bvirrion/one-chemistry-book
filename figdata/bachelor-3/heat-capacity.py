"""Ch. 11, molar heat capacity C_V,m / R of gases against temperature:
N2 and Cl2 (classical rotation, harmonic vibration with the fundamental) with
the JANAF values (C_p/R - 1) as points, and H2 as normal hydrogen (ortho:para
frozen at 3:1) and as equilibrium hydrogen (spin isomers converting)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402
from _statmech import R, cv_diatomic, cv_h2  # noqa: E402

JANAF_T = (100, 200, 300, 500, 1000, 1500, 2000, 3000)


def temps():
    return [10 ** (1 + 0.01 * i) for i in range(0, 249)]   # 10 K to about 3000 K


def rows():
    out = []
    for T in temps():
        n2 = cv_diatomic("N2", T) if T >= 50 else float("nan")
        cl2 = cv_diatomic("Cl2", T) if T >= 50 else float("nan")
        out.append((T, n2, cl2, cv_h2(T, "normal"), cv_h2(T, "equilibrium")))
    return out


def janaf_rows():
    return [(T, value(f"janaf:N2.Cp.{T}") / R - 1, value(f"janaf:Cl2.Cp.{T}") / R - 1) for T in JANAF_T]


if __name__ == "__main__":
    write_table(__file__, ("T", "N2", "Cl2", "nH2", "eH2"), rows())
    write_table(__file__, ("T", "N2", "Cl2"), janaf_rows(), part="janaf")

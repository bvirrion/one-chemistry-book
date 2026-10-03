"""Ch. 12, the maximum primary kinetic isotope effect k_H/k_D =
exp[h c (nu_H - nu_D) / 2 k T] when a stretching vibration X-H becomes the
reaction coordinate, against temperature, for C-H, N-H and O-H stretches
(nu_H: fundamentals of CH4, NH3 and H2O; nu_D from the ratio of reduced
masses, X-H against X-D). The measured CD4 fundamental is given for
comparison."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

C2 = value("const:h") * value("const:c") * 100 / value("const:kB")    # cm K
STRETCH = {"CH": ("vib:CH4.nu1", 12.0), "NH": ("vib:NH3.sym", 14.0), "OH": ("vib:H2O.sym", 16.0)}


def nu_d(bond):
    key, m = STRETCH[bond]
    nh = value(key)
    mu_h, mu_d = m * 1 / (m + 1), m * 2 / (m + 2)
    return nh / math.sqrt(mu_d / mu_h)


def kie(bond, T, nu_h=None, nud=None):
    nh = nu_h if nu_h is not None else value(STRETCH[bond][0])
    nd = nud if nud is not None else nu_d(bond)
    return math.exp(C2 * (nh - nd) / (2 * T))


def rows():
    return [(T,) + tuple(kie(b, T) for b in ("CH", "NH", "OH")) for T in range(200, 801, 5)]


if __name__ == "__main__":
    write_table(__file__, ("T", "CH", "NH", "OH"), rows())
    print("nu_D:", {b: round(nu_d(b), 1) for b in STRETCH}, "CD4 measured", value("vib:CD4.nu1"))
    print("KIE 298:", {b: round(kie(b, 298.15), 2) for b in STRETCH},
          "CH4/CD4 measured at 310.15:", round(kie("CH", 310.15, nud=value("vib:CD4.nu1")), 3))

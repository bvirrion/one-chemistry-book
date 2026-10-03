"""Ch. 1, tunnelling through a rectangular barrier (a model, not a molecule):
height V0 = 0.40 eV, width a = 50 pm; exact transmission probability
T = 1 / (1 + V0^2 sinh^2(kappa a) / (4 E (V0 - E))) for E < V0, for a proton
and a deuteron, against E / V0."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

V0_EV, A = 0.40, 50e-12


def hbar():
    return value("const:h") / (2 * math.pi)


def mass(p):
    return value("const:mp") if p == "H" else value("codata:md")


def kappa(eps, p):
    V0 = V0_EV * value("const:eV")
    return math.sqrt(2 * mass(p) * V0 * (1 - eps)) / hbar()


def transmission(eps, p):
    s = math.sinh(kappa(eps, p) * A)
    return 1 / (1 + s * s / (4 * eps * (1 - eps)))


def thick_limit(eps, p):
    return 16 * eps * (1 - eps) * math.exp(-2 * kappa(eps, p) * A)


if __name__ == "__main__":
    rows = [(e, transmission(e, "H"), transmission(e, "D"))
            for e in [i / 100 for i in range(2, 100, 2)]]
    write_table(__file__, ("eps", "TH", "TD"), rows)

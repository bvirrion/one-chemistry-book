"""Ch. 17, a model surfactant with the CMC of sodium dodecyl sulfate
(8.2 mM at 25 degC, ledger): surface tension from the Szyszkowski
equation gamma = gamma0 - n R T Gamma_max ln(1 + K c) below the CMC (n = 2
for an ionic surfactant without added salt; Gamma_max = 3.2e-6 mol/m2 and K
chosen so that gamma(CMC) = 39 mN/m: model values), constant above; and the
conductivity, linear in c with a smaller slope above the CMC (model molar
conductivities 7.0 and 2.8 mS m2/mol)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

T = 298.15
CMC = value("cmc:SDS")              # mol/L
G0 = value("st:H2O.25C") * 1e-3     # N/m
GMAX, N_ION = 3.2e-6, 2
G_CMC = 0.039


def K():
    """L/mol such that gamma(CMC) = G_CMC"""
    R = value("const:R")
    return (math.exp((G0 - G_CMC) / (N_ION * R * T * GMAX)) - 1) / CMC


def gamma(c):
    R = value("const:R")
    cc = min(c, CMC)
    return G0 - N_ION * R * T * GMAX * math.log(1 + K() * cc)


def surface_excess(c, h=1e-6):
    """Gibbs: Gamma = -(1/(n R T)) d gamma / d ln c"""
    R = value("const:R")
    d = (gamma(c * (1 + h)) - gamma(c * (1 - h))) / (math.log(1 + h) - math.log(1 - h))
    return -d / (N_ION * R * T)


def kappa(c):
    """mS/cm for c in mol/L"""
    l1, l2 = 7.0e-3, 2.8e-3          # S m2/mol
    cm = c * 1000
    s = l1 * cm if c <= CMC else l1 * CMC * 1000 + l2 * (cm - CMC * 1000)
    return s * 10                     # S/m -> mS/cm


if __name__ == "__main__":
    write_table(__file__, ("logc", "gamma_mN"),
                [(lc, 1000 * gamma(10 ** lc)) for lc in [-5 + 0.02 * i for i in range(176)]], part="gamma")
    write_table(__file__, ("c_mM", "kappa"), [(0.2 * i, kappa(0.2e-3 * i)) for i in range(0, 101)], part="kappa")
    print("K %.4g L/mol, Gamma near CMC %.3g mol/m2, area per molecule %.3f nm2"
          % (K(), surface_excess(0.9 * CMC), 1e18 / (surface_excess(0.9 * CMC) * value("const:NA"))))

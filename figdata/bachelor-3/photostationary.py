"""Ch. 14, E/Z photoisomerisation of a model photoswitch (an azobenzene-like
molecule; absorption coefficients and quantum yields are model values) in
the optically thin limit: irradiated at 365 nm for 60 s, then at 440 nm for
60 s, starting from pure E. The fraction of Z tends to the photostationary
value [Z]/[E] = eps_E Phi_EZ / (eps_Z Phi_ZE) at each wavelength.
The rate constant of each direction is (photon flux x ln10 x eps x Phi)
with a photon flux chosen for the figure."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402

BANDS = {365: dict(eE=22000.0, eZ=1500.0, pEZ=0.11, pZE=0.40),
         440: dict(eE=500.0, eZ=1300.0, pEZ=0.25, pZE=0.50)}
FLUX = 4.0e-5        # einstein cm-2 s-1 scaled so that k = FLUX ln10 eps Phi is in s-1 (model)


def rates(lam):
    b = BANDS[lam]
    c = FLUX * math.log(10)
    return c * b["eE"] * b["pEZ"], c * b["eZ"] * b["pZE"]


def z_pss(lam):
    kez, kze = rates(lam)
    return kez / (kez + kze)


def z_of_t(t):
    """fraction of Z: exact solution of the two first-order phases"""
    k1, k2 = rates(365)
    z1 = z_pss(365)
    if t <= 60:
        return z1 * (1 - math.exp(-(k1 + k2) * t))
    z60 = z1 * (1 - math.exp(-(k1 + k2) * 60))
    k3, k4 = rates(440)
    z2 = z_pss(440)
    return z2 + (z60 - z2) * math.exp(-(k3 + k4) * (t - 60))


if __name__ == "__main__":
    write_table(__file__, ("t", "Z"), [(0.5 * i, z_of_t(0.5 * i)) for i in range(241)])
    print("pss 365: %.3f, 440: %.3f; rates" % (z_pss(365), z_pss(440)), rates(365), rates(440))

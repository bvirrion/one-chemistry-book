"""Absorption spectra of two food dyes and a calibration line (grade 11, absorbance).

SYNTHETIC: the band shapes are sums of Gaussians chosen to look like the real
spectra; only the wavelength of maximum absorption and the absorptivity at
that wavelength are data (ledger lmax:E133, abs:E133, lmax:E102, abs:E102,
from the JECFA specifications). The calibration "measurements" are the exact
Beer-Lambert values plus small fixed offsets, written out below.

  part a: wavelength (nm), A of E133 at 5.0 mg/L, A of E102 at 15 mg/L (1 cm)
  part b: the five standards of E133 at 629 nm: C (mg/L), A
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table

LMAX_E133, ABS_E133 = 629.0, 164.0     # nm, L/(g.cm)  (ledger)
LMAX_E102, ABS_E102 = 427.0, 53.0      # nm, L/(g.cm)  (ledger)
PATH_CM = 1.0


def _shape_e133(lam):
    """Main band at 629 nm plus a weak shoulder on the short side (max 1 at 629)."""
    main = math.exp(-0.5 * ((lam - LMAX_E133) / 24.0) ** 2)
    shoulder = 0.22 * math.exp(-0.5 * ((lam - (LMAX_E133 - 50.0)) / 16.0) ** 2)
    norm = 1.0 + 0.22 * math.exp(-0.5 * (50.0 / 16.0) ** 2)
    return (main + shoulder) / norm


def _shape_e102(lam):
    return math.exp(-0.5 * ((lam - LMAX_E102) / 38.0) ** 2)


def absorbance_e133(lam, conc_mg_l, path_cm=PATH_CM):
    return ABS_E133 * path_cm * conc_mg_l / 1000.0 * _shape_e133(lam)


def absorbance_e102(lam, conc_mg_l, path_cm=PATH_CM):
    return ABS_E102 * path_cm * conc_mg_l / 1000.0 * _shape_e102(lam)


def spectra(c133=5.0, c102=15.0, lo=380, hi=750, step=2):
    return [(lam, round(absorbance_e133(lam, c133), 4), round(absorbance_e102(lam, c102), 4))
            for lam in range(lo, hi + 1, step)]


STANDARDS = (1.0, 2.0, 3.0, 4.0, 5.0)                   # mg/L
OFFSETS = (0.004, -0.003, 0.002, -0.004, 0.003)        # fixed "measurement" scatter


def calibration():
    return [(c, round(ABS_E133 * PATH_CM * c / 1000.0 + d, 3))
            for c, d in zip(STANDARDS, OFFSETS)]


def slope_through_origin(points):
    """Least-squares slope of a line through the origin."""
    return sum(c * a for c, a in points) / sum(c * c for c, _ in points)


if __name__ == "__main__":
    write_table(__file__, ("lambda", "E133", "E102"), spectra(), part="a", digits=4)
    write_table(__file__, ("C", "A"), calibration(), part="b", digits=4)

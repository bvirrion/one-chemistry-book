"""Energy levels of the hydrogen atom and its Balmer lines (ch. 1).

E_n = -hc R_H / n^2 with R_H = R_inf / (1 + m_e/m_p) (reduced mass);
a line n2 -> n1 has 1/lambda = R_H (1/n1^2 - 1/n2^2) (vacuum wavelength).
Constants from the shared ledger.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402


def rydberg_h():
    """R_H in 1/m."""
    return value("const:Rinf") / (1 + value("const:me") / value("const:mp"))


def level_ev(n):
    """Energy of level n in eV (zero = ionised atom)."""
    h, c, ev = value("const:h"), value("const:c"), value("const:eV")
    return -h * c * rydberg_h() / ev / n ** 2


def wavelength_nm(n_low, n_high):
    """Vacuum wavelength of the line n_high -> n_low, in nm."""
    return 1e9 / (rydberg_h() * (1 / n_low ** 2 - 1 / n_high ** 2))


def series_limit_nm(n_low):
    return 1e9 * n_low ** 2 / rydberg_h()


if __name__ == "__main__":
    write_table(__file__, ("n", "E_eV"), [(n, level_ev(n)) for n in range(1, 8)])
    write_table(__file__, ("n_high", "lambda_nm"),
                [(n, wavelength_nm(2, n)) for n in range(3, 7)], part="balmer")

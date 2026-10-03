"""Gibbs energy of a closed system of perfect gases against the extent of
N2O4 = 2 NO2 at 298.15 K and 1 bar, from 1 mol of N2O4:
G(xi) - G(0) = xi DrG + RT [(1 - xi) ln x(N2O4) + 2 xi ln x(NO2)],
DrG from the ledger (thermo-data.py). Its minimum is the equilibrium
state, where DrG + RT ln Q = 0."""
import importlib.util
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "thermo", os.path.join(os.path.dirname(__file__), "thermo-data.py"))
thermo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(thermo)

T = 298.15
R = thermo.R


def drG0():
    return thermo.drG("n2o4-dissociation", T) * 1000.0       # J/mol


def g(xi):
    """G(xi) - G(0) in kJ (xi in mol, 1 mol of N2O4 at the start)."""
    a = (1 - xi) / (1 + xi)
    b = 2 * xi / (1 + xi)
    mix = 0.0
    if xi < 1:
        mix += (1 - xi) * math.log(a)
    if xi > 0:
        mix += 2 * xi * math.log(b)
    return (xi * drG0() + R * T * mix) / 1000.0


def slope(xi):
    """dG/dxi = DrG0 + RT ln Q, J/mol."""
    q = (2 * xi / (1 + xi)) ** 2 / ((1 - xi) / (1 + xi))
    return drG0() + R * T * math.log(q)


def xi_eq():
    K = math.exp(-drG0() / (R * T))
    return math.sqrt(K / (4 + K))


if __name__ == "__main__":
    rows = [(k / 200.0, g(k / 200.0)) for k in range(0, 201)]
    write_table(__file__, ("xi", "G"), rows)

"""Exact pH of a solution of ethanoic acid against pC = -log C (ch. 10),
from the charge balance h = C Ka/(h + Ka) + Ke/h solved by bisection on
log h, with the two approximation lines pH = (pKa + pC)/2 and pH = pC."""
import importlib.util
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "aqc", os.path.join(os.path.dirname(__file__), "aqueous-constants.py"))
_aqc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_aqc)


def pke():
    return _aqc.pka("water")


def ph_weak_acid(c, pka, pke_=None):
    ka, ke = 10 ** -pka, 10 ** -(pke_ if pke_ is not None else pke())
    f = lambda h: h - c * ka / (h + ka) - ke / h
    lo, hi = -14.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(10 ** mid) > 0:
            hi = mid
        else:
            lo = mid
    return -(lo + hi) / 2


if __name__ == "__main__":
    pka = value("pka:ethanoic")
    rows = []
    for i in range(0, 161):
        pc = i / 20
        rows.append((pc, ph_weak_acid(10 ** -pc, pka), (pka + pc) / 2, pc))
    write_table(__file__, ("pC", "pH", "weak", "strong"), rows)

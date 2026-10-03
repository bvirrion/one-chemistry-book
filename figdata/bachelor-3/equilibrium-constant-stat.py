"""Ch. 11, equilibrium constants from partition functions: log10 K of
I2(g) = 2 I(g) against 1000 K / T (statistical, with D0 from the JANAF 0 K
enthalpies and the 2P1/2 level of I) with the JANAF values as points, and K of
H2 + D2 = 2 HD from 30 to 2000 K."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402
from _statmech import k_i2, k_hd  # noqa: E402

JANAF_T = (800, 1000, 1200, 1500)


def i2_rows():
    return [(1000 / T, math.log10(k_i2(T))) for T in range(700, 1701, 20)]


def i2_janaf():
    return [(1000 / T, 2 * value(f"janaf:I.logKf.{T}")) for T in JANAF_T]


def hd_rows():
    return [(T, k_hd(T)) for T in range(30, 2001, 10)]


if __name__ == "__main__":
    write_table(__file__, ("invT", "logK"), i2_rows(), part="i2")
    write_table(__file__, ("invT", "logK"), i2_janaf(), part="i2-janaf")
    write_table(__file__, ("T", "K"), hd_rows(), part="hd")

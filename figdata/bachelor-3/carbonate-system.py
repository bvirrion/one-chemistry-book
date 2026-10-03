"""Ch. 32, the carbonate system in fresh water at 25 C. Part a: fractions of
dissolved inorganic carbon as CO2(aq), HCO3- and CO3^2- against pH, with
pKa1 = 6.35 and pKa2 = 10.33 (ledger). Part b: pH of rain in equilibrium with
CO2 at partial pressures from 100 to 2000 ppm of 1 atm: [H+]^2 = Ka1 KH p + Kw
(the carbonate term is negligible below pH 7), KH from the ledger."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

KA1 = 10 ** -value("pka4:H2CO3.1")
KA2 = 10 ** -value("pka4:H2CO3.2")
KW = 10 ** -value("pkw4:25C")
KH = value("henry:CO2") * 1e-3        # mol/(L Pa)
P0 = value("const:atm")


def fractions(pH):
    h = 10 ** -pH
    d = h * h + KA1 * h + KA1 * KA2
    return h * h / d, KA1 * h / d, KA1 * KA2 / d


def rain_pH(ppm):
    co2 = KH * ppm * 1e-6 * P0
    h = math.sqrt(KA1 * co2 + KW)
    return -math.log10(h)


if __name__ == "__main__":
    write_table(__file__, ("pH", "a0", "a1", "a2"), [(4 + 0.05 * j,) + fractions(4 + 0.05 * j) for j in range(0, 181)])
    write_table(__file__, ("ppm", "pH"), [(p, rain_pH(p)) for p in range(100, 2001, 20)], part="b")
    print(rain_pH(value("atm:CO2.2025")), rain_pH(280))

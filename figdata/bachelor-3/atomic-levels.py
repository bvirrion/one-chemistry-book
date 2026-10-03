"""Ch. 2, level diagrams from NIST ASD rows: (a) carbon 2p2, terms at their
J-weighted barycentres and the levels (fine structure, in a zoom); (b) helium
1s2s and 1s2p, singlets and triplets. Each level is a horizontal segment; a
'nan' row separates segments (pgfplots: unbounded coords=jump)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

NAN = float("nan")
CARBON = {"3P0": 0.0, "3P1": "lev:C.3P1", "3P2": "lev:C.3P2", "1D2": "lev:C.1D2", "1S0": "lev:C.1S0"}
HELIUM = {"3S": "lev:He.2s3S1", "1S": "lev:He.2s1S0", "1P": "lev:He.2p1P1"}


def level(key):
    v = CARBON.get(key, key)
    return v if isinstance(v, float) else value(v)


def barycentre(levels):
    """levels: [(J, E)] -> sum (2J+1) E / sum (2J+1)"""
    return sum((2 * j + 1) * e for j, e in levels) / sum(2 * j + 1 for j, _ in levels)


def carbon_terms():
    p = barycentre([(0, level("3P0")), (1, level("3P1")), (2, level("3P2"))])
    return {"3P": p, "1D": level("1D2"), "1S": level("1S0")}


def lande_ratio(e0, e1, e2):
    """(E(J=2)-E(J=1)) / (E(J=1)-E(J=0)); Lande's rule gives 2"""
    return (e2 - e1) / (e1 - e0)


def helium_triplet_p():
    return barycentre([(2, value("lev:He.2p3P2")), (1, value("lev:He.2p3P1")),
                       (0, value("lev:He.2p3P0"))])


def exchange_K_eV():
    """K(1s,2s) = (E(1S) - E(3S)) / 2, in eV"""
    d = value("lev:He.2s1S0") - value("lev:He.2s3S1")      # cm-1
    return d / 2 * 100 * value("const:h") * value("const:c") / value("const:eV")


def configuration_mean():
    """degeneracy-weighted mean of the 15 states of 2p2 (9, 5, 1)"""
    t = carbon_terms()
    return (9 * t["3P"] + 5 * t["1D"] + t["1S"]) / 15


def seg(x0, x1, y):
    return [(x0, y), (x1, y), (NAN, NAN)]


if __name__ == "__main__":
    t = carbon_terms()
    rows = seg(0, 1, configuration_mean())           # configuration
    for y in t.values():
        rows += seg(2, 3, y)
    rows += seg(4, 5, t["1D"]) + seg(4, 5, t["1S"])
    write_table(__file__, ("x", "E"), rows, part="carbon")
    z = []
    for k in ("3P0", "3P1", "3P2"):
        z += seg(0, 1, level(k))
    write_table(__file__, ("x", "E"), z, part="carbon-zoom")
    he = seg(0, 1, value(HELIUM["1S"])) + seg(0, 1, value(HELIUM["1P"]))
    he += seg(2, 3, value(HELIUM["3S"])) + seg(2, 3, helium_triplet_p())
    write_table(__file__, ("x", "E"), [(x, e if e != e else e / 1000) for x, e in he], part="helium")

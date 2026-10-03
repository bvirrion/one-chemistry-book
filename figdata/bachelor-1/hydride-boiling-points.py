"""Boiling points of the hydrides of groups 14-17 against the period, and of
the linear alkanes C1-C10 (ch. 4). Values from the ledger (WebBook in K,
PubChem in degC), returned in degC."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value, _load  # noqa: E402

GROUPS = {
    14: ("CH4", "SiH4", "GeH4"),
    15: ("NH3", "PH3", "AsH3", "SbH3"),
    16: ("H2O", "H2S", "H2Se"),
    17: ("HF", "HCl", "HBr", "HI"),
}
ALKANES = ("CH4", "C2H6", "C3H8", "C4H10", "C5H12", "C6H14", "C7H16", "C8H18",
           "C9H20", "C10H22")


def bp_c(formula):
    row = _load()["bp:" + formula]
    v = float(row[2])
    return v - 273.15 if row[3] == "K" else v


def series(group):
    """[(period, bp in degC)] for the hydrides of a group."""
    return [(p, bp_c(f)) for p, f in enumerate(GROUPS[group], 2)]


def water_without_hbond():
    """Linear extrapolation of the group-16 line through H2S and H2Se back to period 2."""
    (p3, b3), (p4, b4) = series(16)[1:3]
    return b3 - (b4 - b3) * (p3 - 2) / (p4 - p3)


if __name__ == "__main__":
    for g in GROUPS:
        write_table(__file__, ("period", "bp_C"), series(g), part="g%d" % g)
    write_table(__file__, ("n", "bp_C"), [(n, bp_c(f)) for n, f in enumerate(ALKANES, 1)],
                part="alkanes")

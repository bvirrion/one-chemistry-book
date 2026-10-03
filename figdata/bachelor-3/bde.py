"""Ch. 27, C-H bond dissociation enthalpies at 298.15 K from gas-phase
enthalpies of formation (ledger): BDE(R-H) = dfH(R.) + dfH(H.) - dfH(RH),
for methane, ethane, propane (secondary C-H), isobutane (tertiary C-H) and
toluene (benzylic C-H)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

BONDS = (  # label, radical row, parent row
    ("methyl", "dfh4:CH3r", "dfh:CH4_g"),
    ("primary", "dfh4:C2H5r", "dfh:C2H6_g"),
    ("secondary", "dfh4:iC3H7r", "dfh:C3H8_g"),
    ("tertiary", "dfh4:tC4H9r", "dfh4:iC4H10"),
    ("benzylic", "dfh4:PhCH2r", "dfh4:toluene_g"),
)


def bde(radical, parent):
    return value(radical) + value("dfh4:H") - value(parent)


if __name__ == "__main__":
    rows = [(i + 1, bde(r, p)) for i, (lab, r, p) in enumerate(BONDS)]
    write_table(__file__, ("i", "bde"), rows, digits=4)
    for (lab, r, p), (_, b) in zip(BONDS, rows):
        print(lab, round(b, 1))

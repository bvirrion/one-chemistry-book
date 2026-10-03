"""Synthesis strategy (grade 12): atom economies of five syntheses. COMPUTED.

Atom economy = M(desired product) / sum of M(reactants), with the
stoichiometric coefficients, from the book's 0.1-rounded atomic weights
(ledger aw: rows). The two ibuprofen routes use the reactant lists of the
CANN-SCRANTON tables (ledger ibu:boots-ae, ibu:bhc-ae); the other three are
the chapter's own examples.
"""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table

AW = {"H": 1.0, "C": 12.0, "N": 14.0, "O": 16.0, "Na": 23.0, "Cl": 35.5, "Br": 79.9}


def molar_mass(formula):
    m = 0.0
    for el, n in re.findall(r"([A-Z][a-z]?)(\d*)", formula):
        m += AW[el] * (int(n) if n else 1)
    return round(m, 1)


def atom_economy(product, reactants):
    """Per cent; reactants is a list of (coefficient, formula)."""
    total = sum(c * molar_mass(f) for c, f in reactants)
    return 100.0 * molar_mass(product) / total


IBUPROFEN = "C13H18O2"
BOOTS = [(1, "C10H14"), (1, "C4H6O3"), (1, "C4H7ClO2"), (1, "C2H5ONa"),
         (1, "H3O"), (1, "NH3O"), (1, "H4O2")]
BHC = [(1, "C10H14"), (1, "C4H6O3"), (1, "H2"), (1, "CO")]

CASES = [
    ("addition", "C2H5Br", [(1, "C2H4"), (1, "HBr")]),
    ("ester", "C4H8O2", [(1, "C2H4O2"), (1, "C2H6O")]),
    ("bhc", IBUPROFEN, BHC),
    ("boots", IBUPROFEN, BOOTS),
    ("substitution", "C2H6O", [(1, "C2H5Br"), (1, "NaOH")]),
]


def table():
    return [(i + 1, name, round(atom_economy(p, r), 1)) for i, (name, p, r) in enumerate(CASES)]


if __name__ == "__main__":
    write_table(__file__, ("i", "name", "AE"), table(), digits=6)

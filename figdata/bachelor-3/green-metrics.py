"""Ch. 31, atom economies and the minimum E-factors they imply. Molar masses
from the book's atomic weights (ledger values rounded to 0.1, as
tools/molar_mass.py). AE = M(product)/sum M(reactants), with every reagent
that enters the product's synthesis counted (the usual bookkeeping for
multistep routes); minimum E-factor (all yields 100 %, no solvent) =
(1 - AE)/AE. Routes: ibuprofen by the six-step route (Friedel-Crafts,
Darzens, hydrolysis and decarboxylation, oxime, nitrile, hydrolysis) and by
the three-step catalytic route; ethylene oxide by the chlorohydrin route and
by direct oxidation."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
from _table import write_table  # noqa: E402
import chem  # noqa: E402
import molar_mass  # noqa: E402

W = molar_mass.book_weights()

ROUTES = {
    # name: (product, [reactants with multiplicity])
    "ibuprofen-6": ("C13H18O2", [("C10H14", 1), ("C4H6O3", 1), ("C4H7ClO2", 1), ("C2H5ONa", 1),
                                 ("H3O", 1), ("NH3O", 1), ("H2O", 2)]),
    "ibuprofen-3": ("C13H18O2", [("C10H14", 1), ("C4H6O3", 1), ("H2", 1), ("CO", 1)]),
    "EO-chlorohydrin": ("C2H4O", [("C2H4", 1), ("Cl2", 1), ("CaO2H2", 1)]),
    "EO-direct": ("C2H4O", [("C2H4", 2), ("O2", 1)]),
}
PRODUCT_COUNT = {"EO-direct": 2}


def M(f):
    return chem.molar_mass(f, W)


def atom_economy(name):
    prod, reac = ROUTES[name]
    n = PRODUCT_COUNT.get(name, 1)
    return n * M(prod) / sum(k * M(r) for r, k in reac)


def e_min(name):
    ae = atom_economy(name)
    return (1 - ae) / ae


if __name__ == "__main__":
    rows = [(i + 1, 100 * atom_economy(n), e_min(n)) for i, n in enumerate(ROUTES)]
    write_table(__file__, ("i", "AE", "Emin"), rows, digits=4)
    for n in ROUTES:
        print(n, round(100 * atom_economy(n), 1), round(e_min(n), 2))

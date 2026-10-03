"""Bond order against bond length and dissociation energy (chapter 14).
Bond lengths: WebBook ground-state re (rows re:<mol>); dissociation energies
D0 from JANAF formation enthalpies at 0 K (rows janafH0:<sp>):
D0(AB) = DfH0(A) + DfH0(B) - DfH0(AB). Bond orders from the MO diagrams of
the chapter."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

EV = value("const:F") / 1000  # kJ/mol per eV
# molecule: (atoms, bond order, period-2 homonuclear?)
MOLS = {
    "Li2": (("Li", "Li"), 1.0), "C2": (("C", "C"), 2.0), "N2": (("N", "N"), 3.0),
    "O2": (("O", "O"), 2.0), "F2": (("F", "F"), 1.0), "CO": (("C", "O"), 3.0),
    "NO": (("N", "O"), 2.5),
}


def d0_kj(mol):
    a, b = MOLS[mol][0]
    h_mol = 0.0 if mol in ("N2", "O2", "F2") else value("janafH0:%s" % mol)
    return value("janafH0:%s" % a) + value("janafH0:%s" % b) - h_mol


def re_pm(mol):
    return 100 * value("re:%s" % mol)


def ion_d0_ev(mol, atom_ie, mol_ie):
    """D0 of the cation from the cycle D0(AB+) = D0(AB) + IE(atom) - IE(AB)."""
    return d0_kj(mol) / EV + atom_ie - mol_ie


if __name__ == "__main__":
    rows = [(MOLS[m][1], re_pm(m), d0_kj(m) / EV) for m in ("Li2", "C2", "N2", "O2", "F2")]
    write_table(__file__, ("bo", "re", "D0"), rows, part="homo")
    rows = [(MOLS[m][1], re_pm(m), d0_kj(m) / EV) for m in ("CO", "NO")]
    write_table(__file__, ("bo", "re", "D0"), rows, part="hetero")

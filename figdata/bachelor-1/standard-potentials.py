"""Standard potentials at 25 degC of the couples of chs. 13-15, computed from
NBS-82 Gibbs energies of formation (ledger rows dfg:...):
E0 = -Delta_r G0/(nF) for Ox + n e- -> Red, the standard hydrogen electrode
being the reference (H+ and H2 have zero Gibbs energy of formation).
The values printed in the chapters are those of this table, to 2 decimals
(tests/bachelor-1/test_standard-potentials.py asserts them)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _thermo import e0  # noqa: E402

H, W = "H+(ao)", "H2O(l)"
COUPLES = {   # name: (reduction Ox + n e- -> Red, without the electrons; n)
    "Li+/Li": ({"Li+(ao)": -1, "Li(cr)": 1}, 1),
    "K+/K": ({"K+(ao)": -1, "K(cr)": 1}, 1),
    "Na+/Na": ({"Na+(ao)": -1, "Na(cr)": 1}, 1),
    "Mg2+/Mg": ({"Mg2+(ao)": -1, "Mg(cr)": 1}, 2),
    "Al3+/Al": ({"Al3+(ao)": -1, "Al(cr)": 1}, 3),
    "Zn2+/Zn": ({"Zn2+(ao)": -1, "Zn(cr)": 1}, 2),
    "Fe2+/Fe": ({"Fe2+(ao)": -1, "Fe(cr)": 1}, 2),
    "Ni2+/Ni": ({"Ni2+(ao)": -1, "Ni(cr)": 1}, 2),
    "Pb2+/Pb": ({"Pb2+(ao)": -1, "Pb(cr)": 1}, 2),
    "H+/H2": ({H: -2, "H2(g)": 1}, 2),
    "S4O62-/S2O32-": ({"S4O6^2-(ao)": -1, "S2O3^2-(ao)": 2}, 2),
    "Cu2+/Cu+": ({"Cu2+(ao)": -1, "Cu+(ao)": 1}, 1),
    "AgCl/Ag": ({"AgCl(cr)": -1, "Ag(cr)": 1, "Cl-(ao)": 1}, 1),
    "Hg2Cl2/Hg": ({"Hg2Cl2(cr)": -1, "Hg(l)": 2, "Cl-(ao)": 2}, 2),
    "Cu2+/Cu": ({"Cu2+(ao)": -1, "Cu(cr)": 1}, 2),
    "Fe(CN)63-/Fe(CN)64-": ({"Fe(CN)6^3-(ao)": -1, "Fe(CN)6^4-(ao)": 1}, 1),
    "Cu+/Cu": ({"Cu+(ao)": -1, "Cu(cr)": 1}, 1),
    "I2/I-": ({"I2(cr)": -1, "I-(ao)": 2}, 2),
    "O2/H2O2": ({"O2(g)": -1, H: -2, "H2O2(ao)": 1}, 2),
    "Fe3+/Fe2+": ({"Fe3+(ao)": -1, "Fe2+(ao)": 1}, 1),
    "Hg22+/Hg": ({"Hg2^2+(ao)": -1, "Hg(l)": 2}, 2),
    "Ag+/Ag": ({"Ag+(ao)": -1, "Ag(cr)": 1}, 1),
    "Br2/Br-": ({"Br2(l)": -1, "Br-(ao)": 2}, 2),
    "O2/H2O": ({"O2(g)": -1, H: -4, W: 2}, 4),
    "MnO2/Mn2+": ({"MnO2(cr)": -1, H: -4, "Mn2+(ao)": 1, W: 2}, 2),
    "Cl2/Cl-": ({"Cl2(g)": -1, "Cl-(ao)": 2}, 2),
    "PbO2/Pb2+": ({"PbO2(cr)": -1, H: -4, "Pb2+(ao)": 1, W: 2}, 2),
    "MnO4-/Mn2+": ({"MnO4-(ao)": -1, H: -8, "Mn2+(ao)": 1, W: 4}, 5),
    "HClO/Cl2": ({"HClO(ao)": -2, H: -2, "Cl2(g)": 1, W: 2}, 2),
    "F2/F-": ({"F2(g)": -1, "F-(ao)": 2}, 2),
    "O3/O2": ({"O3(g)": -1, H: -2, "O2(g)": 1, W: 1}, 2),
    "NO3-/NO": ({"NO3-(ao)": -1, H: -4, "NO(g)": 1, W: 2}, 3),
    "Cl2aq/Cl-": ({"Cl2(ao)": -1, "Cl-(ao)": 2}, 2),
    "HClO/Cl2aq": ({"HClO(ao)": -2, H: -2, "Cl2(ao)": 1, W: 2}, 2),
    "H2O2/H2O": ({"H2O2(ao)": -1, H: -2, W: 2}, 2),
}


def table():
    return {k: e0(r, n) for k, (r, n) in COUPLES.items()}


def E0(name):
    r, n = COUPLES[name]
    return e0(r, n)


if __name__ == "__main__":
    write_table(__file__, ("couple", "E0_V"),
                sorted(table().items(), key=lambda kv: kv[1]), digits=5)

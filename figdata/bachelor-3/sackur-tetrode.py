"""Ch. 10, statistical standard molar entropies at 298.15 K and 1 bar
(Sackur-Tetrode translation, high-temperature rigid rotor, harmonic
oscillator, electronic degeneracy) of Ar, N2, CO, HCl, Cl2 and I2, and of the
Cl atom (two spin-orbit levels), against the tabulated (CODATA key) values.
No figure: the chapter prints the table, and the test checks it against
this script. Cl2 and I2 use the constants of the main isotopologue and the
standard atomic weights."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _ledger import value  # noqa: E402
from _statmech import s_molecule, s_trans, s_elec, ATOMS  # noqa: E402

REF = {"Ar": "s0:Ar_g", "N2": "s0:N2_g", "CO": "s0:CO_g", "HCl": "s0:HCl_g",
       "Cl2": "s0:Cl2_g", "I2": "s0:I2_g", "Cl": "s0:Cl_g"}


def table():
    rows = {"Ar": dict(trans=s_trans(ATOMS["Ar"]), rot=0.0, vib=0.0, elec=0.0)}
    rows["Ar"]["total"] = rows["Ar"]["trans"]
    for n in ("N2", "CO", "HCl", "Cl2", "I2"):
        rows[n] = s_molecule(n)
    el = s_elec([(4, 0.0), (2, value("lev:Cl.2P1_2"))])
    t = s_trans(value("aw:Cl"))
    rows["Cl"] = dict(trans=t, rot=0.0, vib=0.0, elec=el, total=t + el)
    for n, r in rows.items():
        r["ref"] = value(REF[n])
    return rows


if __name__ == "__main__":
    for n, r in table().items():
        print(n, " ".join("%s=%.2f" % (k, v) for k, v in r.items()))

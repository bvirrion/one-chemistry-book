"""Every acidity constant, solubility product, formation constant and
standard potential of chs. 10-15 that is computed from NBS-82 Gibbs
energies (25 degC). The values printed in the chapters are those of this
table, rounded; tests/bachelor-1/test_aqueous-constants.py asserts them."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _thermo import pK  # noqa: E402
from _ledger import value  # noqa: E402,F401

H = "H+(ao)"
PKA = {
    "water": {"H2O(l)": -1, H: 1, "OH-(ao)": 1},
    "ammonium": {"NH4+(ao)": -1, "NH3(ao)": 1, H: 1},
    "hydrofluoric": {"HF(ao)": -1, "F-(ao)": 1, H: 1},
    "hypochlorous": {"HClO(ao)": -1, "ClO-(ao)": 1, H: 1},
    "nitrous": {"HNO2(ao)": -1, "NO2-(ao)": 1, H: 1},
    "phosphoric1": {"H3PO4(ao)": -1, "H2PO4-(ao)": 1, H: 1},
    "phosphoric2": {"H2PO4-(ao)": -1, "HPO4^2-(ao)": 1, H: 1},
    "phosphoric3": {"HPO4^2-(ao)": -1, "PO4^3-(ao)": 1, H: 1},
    "carbonic1": {"CO2(ao)": -1, "H2O(l)": -1, "HCO3-(ao)": 1, H: 1},
    "carbonic2": {"HCO3-(ao)": -1, "CO3^2-(ao)": 1, H: 1},
    "hydrogensulfate": {"HSO4-(ao)": -1, "SO4^2-(ao)": 1, H: 1},
    "sulfurous1": {"H2SO3(ao)": -1, "HSO3-(ao)": 1, H: 1},
    "sulfurous2": {"HSO3-(ao)": -1, "SO3^2-(ao)": 1, H: 1},
    "hydrogensulfide": {"H2S(ao)": -1, "HS-(ao)": 1, H: 1},
    "peroxide": {"H2O2(ao)": -1, "HO2-(ao)": 1, H: 1},
}

OH = "OH-(ao)"
# solubility products: solid -> ions (pKs = -log Ks)
PKS = {
    "AgCl": {"AgCl(cr)": -1, "Ag+(ao)": 1, "Cl-(ao)": 1},
    "AgBr": {"AgBr(cr)": -1, "Ag+(ao)": 1, "Br-(ao)": 1},
    "AgI": {"AgI(cr)": -1, "Ag+(ao)": 1, "I-(ao)": 1},
    "Ag2CrO4": {"Ag2CrO4(cr)": -1, "Ag+(ao)": 2, "CrO4^2-(ao)": 1},
    "Ag2SO4": {"Ag2SO4(cr)": -1, "Ag+(ao)": 2, "SO4^2-(ao)": 1},
    "CaCO3": {"CaCO3(cr)": -1, "Ca2+(ao)": 1, "CO3^2-(ao)": 1},
    "CaF2": {"CaF2(cr)": -1, "Ca2+(ao)": 1, "F-(ao)": 2},
    "MgF2": {"MgF2(cr)": -1, "Mg2+(ao)": 1, "F-(ao)": 2},
    "BaSO4": {"BaSO4(cr)": -1, "Ba2+(ao)": 1, "SO4^2-(ao)": 1},
    "CaOH2": {"Ca(OH)2(cr)": -1, "Ca2+(ao)": 1, OH: 2},
    "MgOH2": {"Mg(OH)2(cr)": -1, "Mg2+(ao)": 1, OH: 2},
    "FeOH2": {"Fe(OH)2(cr)": -1, "Fe2+(ao)": 1, OH: 2},
    "FeOH3": {"Fe(OH)3(cr)": -1, "Fe3+(ao)": 1, OH: 3},
    "ZnOH2": {"Zn(OH)2(cr)": -1, "Zn2+(ao)": 1, OH: 2},
    # gibbsite is tabulated as Al2O3.3H2O, i.e. two Al(OH)3
    "AlOH3": {"Al2O3.3H2O(cr)": -0.5, "Al3+(ao)": 1, OH: 3},
    # oxides, written with water so that they compare with the hydroxides
    "CuO": {"CuO(cr)": -1, "H2O(l)": -1, "Cu2+(ao)": 1, OH: 2},
    "Ag2O": {"Ag2O(cr)": -1, "H2O(l)": -1, "Ag+(ao)": 2, OH: 2},
}
# formation constants: log10 of K for ion + ligands -> complex
LOGB = {
    "ZnOH": {"Zn2+(ao)": -1, OH: -1, "ZnOH+(ao)": 1},
    "ZnOH2aq": {"Zn2+(ao)": -1, OH: -2, "Zn(OH)2(ao)": 1},
    "ZnOH3": {"Zn2+(ao)": -1, OH: -3, "Zn(OH)3-(ao)": 1},
    "ZnOH4": {"Zn2+(ao)": -1, OH: -4, "Zn(OH)4^2-(ao)": 1},
    "AlOH4": {"Al3+(ao)": -1, OH: -4, "Al(OH)4-(ao)": 1},
    "FeOH": {"Fe3+(ao)": -1, OH: -1, "FeOH2+(ao)": 1},
    "AgNH3": {"Ag+(ao)": -1, "NH3(ao)": -1, "AgNH3+(ao)": 1},
    "AgNH32": {"Ag+(ao)": -1, "NH3(ao)": -2, "Ag(NH3)2+(ao)": 1},
    "AgCl2": {"Ag+(ao)": -1, "Cl-(ao)": -2, "AgCl2-(ao)": 1},
    "CuNH3_1": {"Cu2+(ao)": -1, "NH3(ao)": -1, "CuNH3^2+(ao)": 1},
    "CuNH3_2": {"Cu2+(ao)": -1, "NH3(ao)": -2, "Cu(NH3)2^2+(ao)": 1},
    "CuNH3_3": {"Cu2+(ao)": -1, "NH3(ao)": -3, "Cu(NH3)3^2+(ao)": 1},
    "CuNH3_4": {"Cu2+(ao)": -1, "NH3(ao)": -4, "Cu(NH3)4^2+(ao)": 1},
    "FeSCN": {"Fe3+(ao)": -1, "SCN-(ao)": -1, "FeSCN^2+(ao)": 1},
    "FeF": {"Fe3+(ao)": -1, "F-(ao)": -1, "FeF^2+(ao)": 1},
}

# other equilibria: log10 K
LOGK = {
    "henryCO2": {"CO2(g)": -1, "CO2(ao)": 1},       # K_H = [CO2(aq)]/p(CO2), bar
}


def table():
    t = {"pka_" + k: pK(r) for k, r in PKA.items()}
    t.update({"pks_" + k: pK(r) for k, r in PKS.items()})
    t.update({"logb_" + k: -pK(r) for k, r in LOGB.items()})
    t.update({"logk_" + k: -pK(r) for k, r in LOGK.items()})
    return t


def pka(name):
    return pK(PKA[name])


def pks(name):
    return pK(PKS[name])


def logb(name):
    return -pK(LOGB[name])


def logk(name):
    return -pK(LOGK[name])


if __name__ == "__main__":
    write_table(__file__, ("name", "value"), sorted(table().items()), digits=5)

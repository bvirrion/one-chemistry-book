import importlib.util
import os

spec = importlib.util.spec_from_file_location("ac", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "aqueous-constants.py"))
ac = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ac)
t = ac.table()

PRINTED = {   # values as printed in the chapters (2 decimals)
    "water": 14.00, "ammonium": 9.25, "hydrofluoric": 3.16, "hypochlorous": 7.55,
    "nitrous": 3.22, "phosphoric1": 2.15, "phosphoric2": 7.21, "phosphoric3": 12.34,
    "carbonic1": 6.37, "carbonic2": 10.33, "hydrogensulfate": 1.99,
    "sulfurous1": 1.77, "sulfurous2": 7.22, "hydrogensulfide": 6.99, "peroxide": 11.69,
}

PRINTED_PKS = {   # chapter 11, table of solubility products
    "AgCl": 9.75, "AgBr": 12.27, "AgI": 16.07, "Ag2CrO4": 11.95, "BaSO4": 9.97,
    "CaCO3": 8.30, "CaF2": 9.84, "CaOH2": 5.33, "MgOH2": 11.25, "FeOH2": 16.31,
    "ZnOH2": 16.38, "FeOH3": 38.55, "AlOH3": 34.75,
}
PRINTED_LOGB = {"ZnOH4": 14.45, "AlOH4": 33.52, "FeOH": 11.82}
PRINTED_LOGK = {"henryCO2": -1.47}


def test_printed_solubility_and_formation_constants():
    for k, v in PRINTED_PKS.items():
        assert round(ac.pks(k), 2) == v, (k, ac.pks(k))
    for k, v in PRINTED_LOGB.items():
        assert round(ac.logb(k), 2) == v, (k, ac.logb(k))
    for k, v in PRINTED_LOGK.items():
        assert round(ac.logk(k), 2) == v, (k, ac.logk(k))


def test_printed_values():
    for k, v in PRINTED.items():
        assert round(t["pka_" + k], 2) == v, (k, t["pka_" + k])


def test_cross_check_with_measured_pka():
    # independent check: methanoic acid from NBS-82 against the IUPAC dataset
    computed = ac.pK({"HCOOH(ao)": -1, "HCOO-(ao)": 1, "H+(ao)": 1})
    assert abs(computed - ac.value("pka:methanoic")) < 0.05

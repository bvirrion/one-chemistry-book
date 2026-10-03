import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("sp", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "standard-potentials.py"))
sp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sp)
t = sp.table()

PRINTED = {   # chapters 13-15, volts, 2 decimals
    "Li+/Li": -3.04, "K+/K": -2.94, "Na+/Na": -2.71, "Mg2+/Mg": -2.36, "Al3+/Al": -1.68,
    "Zn2+/Zn": -0.76, "Fe2+/Fe": -0.41, "Ni2+/Ni": -0.24, "Pb2+/Pb": -0.13, "H+/H2": 0.00,
    "S4O62-/S2O32-": 0.02, "Cu2+/Cu+": 0.16, "AgCl/Ag": 0.22, "Hg2Cl2/Hg": 0.27,
    "Cu2+/Cu": 0.34, "Fe(CN)63-/Fe(CN)64-": 0.36, "Cu+/Cu": 0.52, "I2/I-": 0.53,
    "O2/H2O2": 0.69, "Fe3+/Fe2+": 0.77, "Hg22+/Hg": 0.80, "Ag+/Ag": 0.80,
    "Br2/Br-": 1.08, "O2/H2O": 1.23, "MnO2/Mn2+": 1.23, "NO3-/NO": 0.96, "F2/F-": 2.89, "O3/O2": 2.07, "Cl2/Cl-": 1.36,
    "PbO2/Pb2+": 1.46, "MnO4-/Mn2+": 1.51, "HClO/Cl2": 1.63, "H2O2/H2O": 1.76,
}


def test_printed_values():
    for k, v in PRINTED.items():
        assert round(t[k], 2) == v, (k, t[k])


def test_chlorine_problem_data():
    # chapter 14 problem prints these to 3 decimals
    assert round(t["Cl2aq/Cl-"], 3) == 1.396
    assert round(t["HClO/Cl2aq"], 3) == 1.594
    ph = (1.594 - 1.396 - 2 * 0.0296 * math.log10(50)) / 0.0592
    assert round(ph, 1) == 1.6


def test_combined_potentials_cu():
    # n3 E3 = n1 E1 + n2 E2: Cu2+/Cu from Cu2+/Cu+ and Cu+/Cu
    assert abs(2 * t["Cu2+/Cu"] - (t["Cu2+/Cu+"] + t["Cu+/Cu"])) < 1e-9


def test_second_kind_electrode():
    # E0(AgCl/Ag) = E0(Ag+/Ag) - (RT ln10/F) pKs(AgCl)
    import importlib.util as u
    s = u.spec_from_file_location("ac", os.path.join(
        os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "aqueous-constants.py"))
    ac = u.module_from_spec(s)
    s.loader.exec_module(ac)
    slope = ac.value("const:R") * 298.15 * math.log(10) / ac.value("const:F")
    assert abs(t["AgCl/Ag"] - (t["Ag+/Ag"] - slope * ac.pks("AgCl"))) < 1e-9
    assert round(slope, 3) == 0.059

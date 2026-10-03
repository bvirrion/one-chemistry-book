import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("thermo", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "thermo-data.py"))
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)

PRINTED_DRH = {   # kJ/mol as printed, chapter 1
    "methane-combustion-l": -890.3, "methane-combustion-g": -802.3,
    "butane-combustion-l": -2877.6, "butane-combustion-g": -2657.6,
    "propane-combustion-l": -2219.2, "co-combustion": -283.0,
    "c-to-co": -110.5, "ammonia-synthesis": -91.9, "no-formation": 90.3,
    "water-vaporisation": 44.0, "octane-combustion-l": -5470.3,
    "ethene-hydrogenation": -136.3, "benzene-combustion-l": -3267.6,
}


def test_printed_reaction_enthalpies():
    for rx, v in PRINTED_DRH.items():
        assert abs(t.drH(rx) - v) <= 0.05 + 1e-9, (rx, t.drH(rx))


def test_hess_cycle_closes():
    # C -> CO -> CO2 equals C -> CO2
    assert abs(t.drH("c-to-co") + t.drH("co-combustion") - t.drH("c-to-co2")) < 1e-9


def test_combustion_agrees_with_measurement():
    # computed combustion enthalpies agree with the measured ones (ledger)
    assert abs(-t.drH("methane-combustion-l") - t.value("dch:CH4")) < 1.0
    assert abs(-t.drH("propane-combustion-l") - t.value("dch:C3H8")) < 0.5


def test_gibbs_and_k():
    rx = "ammonia-synthesis"
    assert abs(t.drG(rx) - (t.drH(rx) - 298.15 * t.drS(rx) / 1000)) < 1e-12
    assert math.isclose(math.log(t.K(rx)), -t.drG(rx) * 1000 / (t.R * 298.15))


def test_bond_enthalpies():
    b = t.bonds()
    assert round(b["C-H"]) == 416 and round(b["O-H"]) == 464
    assert round(b["H-H"]) == 436 and round(b["N#N"]) == 945
    assert round(b["C=O"]) == 804 and round(b["O=O"]) == 498


def test_born_haber_and_kirchhoff():
    lat, ie, ea = t.born_haber_nacl()
    assert round(lat) == 787 and round(ie, 1) == 495.8 and round(ea, 1) == 348.6
    est, janaf, dcp = t.kirchhoff_ammonia()
    assert round(dcp, 1) == -44.3 and round(est, 1) == -109.7 and round(janaf, 1) == -105.2
    assert round(t.dfh_ethanol_l(), 1) == -276.9

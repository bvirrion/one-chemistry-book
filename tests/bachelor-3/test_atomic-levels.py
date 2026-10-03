import importlib.util
import os

spec = importlib.util.spec_from_file_location("al", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "atomic-levels.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_levels_at_ledger_values():
    t = m.carbon_terms()
    assert t["1D"] == m.value("lev:C.1D2") and t["1S"] == m.value("lev:C.1S0")
    assert abs(t["3P"] - 29.59) < 0.01


def test_lande_ratios_printed():
    assert round(m.lande_ratio(0, m.level("3P1"), m.level("3P2")), 2) == 1.64
    o = m.lande_ratio(m.value("lev:O.3P0"), m.value("lev:O.3P1"), 0)   # inverted
    assert round(o, 2) == 2.30


def test_exchange_integral():
    assert round(m.exchange_K_eV(), 3) == 0.398
    assert m.value("lev:He.2s3S1") < m.value("lev:He.2s1S0")


def test_configuration_mean():
    assert round(m.configuration_mean(), 1) == 4858.5

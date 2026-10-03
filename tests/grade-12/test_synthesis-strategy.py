"""Tests for figdata/grade-12/synthesis-strategy.py."""
import importlib.util, os

spec = importlib.util.spec_from_file_location(
    "ss", os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12", "synthesis-strategy.py"))
ss = importlib.util.module_from_spec(spec); spec.loader.exec_module(ss)


def test_molar_masses_match_book():
    assert ss.molar_mass("C13H18O2") == 206.0
    assert sum(c * ss.molar_mass(f) for c, f in ss.BOOTS) == 514.5
    assert sum(c * ss.molar_mass(f) for c, f in ss.BHC) == 266.0


def test_ibuprofen_routes_match_source_percentages():
    rows = {name: ae for _, name, ae in ss.table()}
    assert round(rows["boots"]) == 40 and round(rows["bhc"]) == 77


def test_addition_is_complete_and_order_decreasing():
    aes = [ae for _, _, ae in ss.table()]
    assert aes[0] == 100.0
    assert aes == sorted(aes, reverse=True)

"""Tests for figdata/grade-11/infrared.py: bands at the ledger positions."""
import importlib.util, os

spec = importlib.util.spec_from_file_location(
    "infrared", os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11", "infrared.py"))
ir = importlib.util.module_from_spec(spec); spec.loader.exec_module(ir)


def test_carbonyl_minima_at_ledger_positions():
    assert ir.minimum("propanone", 1600, 1800) == 1715     # ir:CO-ketone
    assert ir.minimum("ester", 1600, 1800) == 1735         # ir:CO-ester
    assert ir.minimum("acid", 1600, 1800) == 1710          # ir:CO-acid


def test_OH_bands():
    assert ir.minimum("ethanolG", 3500, 3800) == 3666      # ir:ethanol-OH (gas, free)
    assert 3300 <= ir.minimum("ethanolL", 3100, 3700) <= 3400   # ir:OH-bonded
    assert 2500 <= ir.minimum("acid", 2400, 3400) <= 3300       # ir:OH-acid
    # hydrogen bonding: the liquid band is lower and much wider than the gas one
    assert ir.minimum("ethanolL", 3100, 3700) < ir.minimum("ethanolG", 3500, 3800)


def test_no_carbonyl_in_alcohol_or_amine():
    assert ir.transmittance("ethanolL", 1715) > 90
    assert ir.transmittance("amine", 1715) > 90


def test_transmittance_bounds_and_axis():
    rows = ir.table()
    assert rows[0][0] == 4000 and rows[-1][0] == 500       # decreasing wavenumber
    assert all(0 <= v <= 100 for r in rows for v in r[1:])

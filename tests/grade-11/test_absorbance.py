"""Tests for figdata/grade-11/absorbance.py."""
import importlib.util, os

spec = importlib.util.spec_from_file_location(
    "absorbance", os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11", "absorbance.py"))
ab = importlib.util.module_from_spec(spec); spec.loader.exec_module(ab)


def test_maxima_at_ledger_wavelengths():
    fine133 = max(range(380, 751), key=lambda l: ab.absorbance_e133(l, 5.0))
    fine102 = max(range(380, 751), key=lambda l: ab.absorbance_e102(l, 15.0))
    assert abs(fine133 - 629) <= 1          # ledger lmax:E133
    assert fine102 == 427                   # ledger lmax:E102


def test_peak_values_are_beer_lambert():
    assert abs(ab.absorbance_e133(629, 5.0) - 0.82) < 1e-9     # 164 L/(g cm) x 5 mg/L
    assert abs(ab.absorbance_e102(427, 15.0) - 0.795) < 1e-9   # 53.0 x 15 mg/L


def test_yellow_dye_absent_at_629_and_blue_small_at_427():
    assert ab.absorbance_e102(629, 15.0) < 0.001
    assert ab.absorbance_e133(427, 5.0) < 0.001


def test_calibration_line_through_origin_with_slope_a_l():
    pts = ab.calibration()
    assert [c for c, _ in pts] == [1.0, 2.0, 3.0, 4.0, 5.0]
    k = ab.slope_through_origin(pts)
    assert abs(k - 0.164) < 0.001                          # A per (mg/L)
    assert all(abs(a - 0.164 * c) <= 0.005 for c, a in pts)

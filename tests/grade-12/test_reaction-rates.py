"""Tests for figdata/grade-12/reaction-rates.py."""
import importlib.util, os, math

spec = importlib.util.spec_from_file_location(
    "rr", os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12", "reaction-rates.py"))
rr = importlib.util.module_from_spec(spec); spec.loader.exec_module(rr)


def test_half_life_halves():
    for k in (rr.K1, rr.K2):
        t = rr.half_life(k)
        assert abs(rr.conc(t, k) - rr.A0 / 2) < 1e-9
    assert round(rr.half_life(rr.K1), 1) == 13.9 and round(rr.half_life(rr.K2), 1) == 6.9


def test_tangent_slope_is_minus_k_a0():
    h = 1e-6
    slope = (rr.conc(h, rr.K1) - rr.conc(0, rr.K1)) / h
    assert abs(slope + rr.K1 * rr.A0) < 1e-4
    rows = rr.curves()
    assert rows[0][3] == rr.A0 and abs(rows[20][3] - (rr.A0 - 0.5 * 10)) < 1e-9   # t = 10 min


def test_dye_data_first_order():
    rows = rr.dye()
    k = -rr.ln_slope(rows)
    assert abs(k - math.log(2) / 6.0) / (math.log(2) / 6.0) < 0.02
    assert rows[0][1] == 0.800 and rows[3][1] == 0.402          # t = 6 min: half, + offset
    # time to 1 %: ln(100)/k, about 6.6 half-lives, 40 min
    t1 = math.log(100) / rr.DYE_K
    assert round(t1 / 6.0, 1) == 6.6 and round(t1) == 40

import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("sp", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "solubility-ph.py"))
sp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sp)


def test_slopes_of_the_zinc_model():
    a, b = sp.zinc(7.0)[0], sp.zinc(8.0)[0]
    assert abs((b - a) + 2) < 1e-3
    a, b = sp.zinc(13.0)[0], sp.zinc(14.0)[0]
    assert abs((b - a) - 2) < 1e-3


def test_slopes_of_the_aluminium_model():
    a, b = sp.aluminium(3.0)[0], sp.aluminium(4.0)[0]
    assert abs((b - a) + 3) < 1e-3
    a, b = sp.aluminium(12.0)[0], sp.aluminium(13.0)[0]
    assert abs((b - a) - 1) < 1e-3


def test_full_zinc_curve_has_a_floor():
    lo = min(sp.zinc(x / 20)[1] for x in range(120, 281))
    assert round(lo, 1) == -5.6 or round(lo, 1) == -5.7
    assert all(sp.zinc(x / 20)[1] >= sp.zinc(x / 20)[0] - 1e-9 for x in range(120, 281))


def test_thresholds_order():
    starts = [t[2] for t in sp.thresholds()]
    assert starts == sorted(starts)
    for _, _, start, end in sp.thresholds():
        assert end > start


def test_mine_effluent_problem_with_printed_data():
    # printed data: pKe 14.00, pKs 38.55 / 16.38 / 11.25, log b4 14.45, log b1 11.82
    L = math.log10
    assert round(14 - (38.55 + L(1e-3)) / 3, 2) == 2.15
    assert round(14 - (16.38 + L(5e-3)) / 2, 2) == 6.96
    assert round(14 - (11.25 + L(2e-2)) / 2, 2) == 9.22
    assert round(14 - (38.55 - 6) / 3, 2) == 3.15

    def dissolved_iron(ph):
        return 10 ** (3.45 - 3 * ph) * (1 + 10 ** (ph - 2.18))
    lo, hi = 3.0, 4.5
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if dissolved_iron(mid) > 1e-6 else (lo, mid)
    assert round(lo, 2) == 3.64      # the named number: window 3.64 - 6.96
    assert round(14 + (L(5e-3) - (14.45 - 16.38)) / 2, 2) == 13.81


def test_minimum_of_the_zinc_model_with_printed_data():
    assert round(14 - 14.45 / 4, 2) == 10.39
    assert abs(2 * 10 ** (-(16.38 + 1.93) / 2) - 1.4e-9) < 0.05e-9

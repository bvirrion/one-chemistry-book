import importlib.util
import os

spec = importlib.util.spec_from_file_location("ee", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "extent-equilibrium.py"))
ee = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ee)


def test_shift_equilibrium():
    x = ee.xi_eq_shift()
    assert 0 < x < 1
    assert abs(ee.q_shift(x) - ee.K_SHIFT) < 1e-9
    assert round(x, 3) == 0.607


def test_q_increases_with_extent():
    q = [ee.q_shift(i / 100) for i in range(1, 99)]
    assert all(a < b for a, b in zip(q, q[1:]))


def test_carbonate_cases():
    assert ee.xi_eq_carbonate(0.010) is None          # all decomposes
    x = ee.xi_eq_carbonate(0.050)
    assert abs(ee.q_carbonate(x, 0.050) - ee.K_CARB) < 1e-12
    assert round(x, 4) == 0.0219
    assert round(ee.q_carbonate(1, 0.010), 3) == 0.091

import importlib.util
import os

spec = importlib.util.spec_from_file_location("rh", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "raoult-henry.py"))
rh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rh)


def test_ideal_is_straight():
    for x in (0.0, 0.3, 0.7, 1.0):
        p1, p2, p = rh.pressures(x, 0.0)
        assert abs(p - (rh.P2 + x * (rh.P1 - rh.P2))) < 1e-12


def test_raoult_and_henry_limits():
    h = 1e-6
    p1, _, _ = rh.pressures(1 - h)
    assert abs((rh.P1 - p1) / h - rh.P1) < 1e-3          # slope p1* at x1 -> 1
    p1, _, _ = rh.pressures(h)
    assert abs(p1 / h - rh.henry_constant_1()) < 1e-3     # Henry at x1 -> 0


def test_gibbs_duhem():
    # x1 dln g1 + x2 dln g2 = 0 for the Margules model
    for x in (0.2, 0.5, 0.8):
        d = 1e-6
        g1a, g2a = rh.gammas(x - d); g1b, g2b = rh.gammas(x + d)
        import math
        lhs = x * (math.log(g1b) - math.log(g1a)) + (1 - x) * (math.log(g2b) - math.log(g2a))
        assert abs(lhs) < 1e-9

import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("irl", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "integrated-rate-laws.py"))
irl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(irl)


def test_half_lives():
    for n in (0, 1, 2):
        t = irl.half_life(n)
        assert abs(irl.conc(n, t) - irl.A0 / 2) < 1e-12
    assert round(irl.half_life(0)) == 10 and round(irl.half_life(1), 2) == 13.86
    assert round(irl.half_life(2)) == 20


def test_linear_forms():
    # [A] linear (order 0), ln[A] linear (order 1), 1/[A] linear (order 2)
    for f in (lambda t: irl.conc(0, t), lambda t: math.log(irl.conc(1, t)),
              lambda t: 1 / irl.conc(2, t)):
        d1, d2 = f(5) - f(0), f(10) - f(5)
        assert abs(d1 - d2) < 1e-12


def test_same_initial_rate():
    h = 1e-6
    for n in (0, 1, 2):
        assert abs((irl.conc(n, 0) - irl.conc(n, h)) / h - irl.V0) < 1e-4

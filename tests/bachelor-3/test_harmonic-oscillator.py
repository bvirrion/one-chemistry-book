import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("ho", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "harmonic-oscillator.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_levels_and_normalisation():
    assert m.level(0) == 0.5 and m.level(3) - m.level(2) == 1
    for v in range(4):
        assert abs(m.integral(lambda y: m.psi(v, y) ** 2) - 1) < 1e-6
    assert abs(m.integral(lambda y: m.psi(0, y) * m.psi(2, y))) < 1e-6


def test_parity_and_turning_points():
    assert abs(m.psi(1, 0.7) + m.psi(1, -0.7)) < 1e-12
    assert abs(m.psi(2, 0.7) - m.psi(2, -0.7)) < 1e-12
    assert abs(m.turning(0) - 1) < 1e-12
    assert abs(m.turning(0) ** 2 / 2 - m.level(0)) < 1e-12

import importlib.util
import os

spec = importlib.util.spec_from_file_location("oy", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "overall-yield.py"))
oy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oy)


def test_two_steps():
    # the raspberry-ketone problem: 85 % then 92 %
    assert abs(oy.overall([0.85, 0.92]) - 0.782) < 1e-12


def test_curve_falls_geometrically():
    c = oy.curve(0.9, 10)
    assert c[0] == (0, 100.0)
    assert abs(c[10][1] - 100 * 0.9 ** 10) < 1e-9
    assert all(b[1] < a[1] for a, b in zip(c, c[1:]))


def test_ten_steps_at_90_percent():
    assert abs(oy.overall([0.9] * 10) - 0.3486784401) < 1e-9

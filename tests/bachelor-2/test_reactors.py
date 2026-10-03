import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("re", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "reactors.py"))
re_ = importlib.util.module_from_spec(spec)
spec.loader.exec_module(re_)


def test_closed_forms():
    for da in (0.5, 1.0, 4.0):
        assert abs(re_.x_cstr(da) - da / (1 + da)) < 1e-15
        assert abs(re_.x_pfr(da) - (1 - math.exp(-da))) < 1e-15
        assert re_.x_pfr(da) > re_.x_cascade(da, 5) > re_.x_cascade(da, 2) > re_.x_cstr(da)


def test_cascade_tends_to_plug_flow():
    assert abs(re_.x_cascade(3.0, 10000) - re_.x_pfr(3.0)) < 1e-3
    assert re_.x_cascade(3.0, 1) == re_.x_cstr(3.0)


def test_second_order_tank():
    x = re_.x_cstr_second_order(90.0)
    assert abs(90.0 * (1 - x) ** 2 - x) < 1e-12 and round(x, 3) == 0.900


def test_three_steady_states():
    roots = re_.steady_states()
    assert len(roots) == 3
    assert round(roots[1]) == 390 and round(roots[2]) == 430


def test_levenspiel_areas():
    X = 0.9
    assert abs(re_.tau_pfr(X) - math.log(10)) < 1e-12
    assert abs(re_.tau_cstr(X) - 9.0) < 1e-12

import importlib.util
import os

spec = importlib.util.spec_from_file_location("cr", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "consecutive-reactions.py"))
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)


def test_mass_balance():
    for t in (0, 0.3, 1, 3, 6):
        assert abs(sum(cr.abc(t, 1.0, 0.5)) - 1) < 1e-12


def test_maximum_of_b():
    k1, k2 = 1.0, 0.5
    tm = cr.t_max(k1, k2)
    h = 1e-5
    assert cr.abc(tm, k1, k2)[1] > cr.abc(tm - h, k1, k2)[1]
    assert cr.abc(tm, k1, k2)[1] > cr.abc(tm + h, k1, k2)[1]
    assert round(tm, 3) == 1.386


def test_steady_state_good_when_k2_large():
    for t in (0.5, 1, 2, 3):
        b = cr.abc(t, 1.0, 20.0)[1]
        assert abs(b - cr.b_ss(t, 1.0, 20.0)) / b < 0.06
    # and poor when k2 < k1
    assert abs(cr.abc(2, 1.0, 0.5)[1] - cr.b_ss(2, 1.0, 0.5)) > 0.1


def test_exercise_values():
    assert round(cr.t_max(0.10, 0.30), 2) == 5.49

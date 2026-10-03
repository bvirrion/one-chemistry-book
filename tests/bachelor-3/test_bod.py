import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("bod", os.path.join(D, "bod.py"))
bod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bod)


def test_asymptote_is_L0():
    assert abs(bod.bod(200) - bod.L0) < 1e-6
    assert bod.bod(0) == 0


def test_critical_point_is_the_minimum():
    tc = bod.t_critical()
    h = 1e-4
    assert bod.deficit(tc) > bod.deficit(tc - h) and bod.deficit(tc) > bod.deficit(tc + h)

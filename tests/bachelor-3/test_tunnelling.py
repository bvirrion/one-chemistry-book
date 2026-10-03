import importlib.util
import os

spec = importlib.util.spec_from_file_location("tu", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "tunnelling.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_bounds_and_isotope():
    for e in (0.1, 0.5, 0.9):
        assert 0 < m.transmission(e, "D") < m.transmission(e, "H") < 1


def test_thick_limit():
    e = 0.3
    assert abs(m.thick_limit(e, "D") / m.transmission(e, "D") - 1) < 0.05

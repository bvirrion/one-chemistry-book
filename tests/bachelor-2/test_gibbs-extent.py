import importlib.util
import os

spec = importlib.util.spec_from_file_location("ge", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "gibbs-extent.py"))
ge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ge)


def test_minimum_is_equilibrium():
    xe = ge.xi_eq()
    assert abs(ge.slope(xe)) < 1e-6
    assert ge.g(xe) < ge.g(xe - 0.01) and ge.g(xe) < ge.g(xe + 0.01)
    assert round(xe, 3) == 0.189


def test_numerical_slope():
    for xi in (0.1, 0.3, 0.6):
        h = 1e-6
        num = (ge.g(xi + h) - ge.g(xi - h)) / (2 * h) * 1000
        assert abs(num - ge.slope(xi)) < 1e-2

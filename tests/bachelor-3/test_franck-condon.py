import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("fc", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "franck-condon.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_sum_is_one_and_maximum_near_S():
    for S in (0.3, 1.5, 5.0):
        assert abs(sum(m.fc(v, S) for v in range(60)) - 1) < 1e-12
        vmax = max(range(30), key=lambda v: m.fc(v, S))
        assert abs(vmax - S) <= 1
    assert m.fc(0, 1e-9) > 0.999


def test_poisson_against_quadrature():
    S = 1.5
    d = math.sqrt(2 * S)
    for v in range(4):
        assert abs(m.overlap_numeric(v, d) ** 2 - m.fc(v, S)) < 1e-6


def test_iodine():
    assert round(m.huang_rhys_I2()) == 15

import importlib.util
import math
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("ek", os.path.join(D, "equilibrium-constant-stat.py"))
ek = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ek)


def test_i2_against_janaf():
    for inv, logk in ek.i2_janaf():
        assert abs(math.log10(ek.k_i2(1000 / inv)) - logk) < 0.05


def test_hd_limit():
    assert abs(ek.k_hd(3000) - 4) < 0.01
    assert round(ek.k_hd(298.15), 2) == 3.26
    ks = [k for _, k in ek.hd_rows()]
    assert all(b > a for a, b in zip(ks, ks[1:150]))


def test_vant_hoff():
    # d ln K / d(1/T) = -dH/R: the statistical K obeys it with dH = D0 + small terms
    T, h = 1000.0, 1e-7
    slope = (math.log(ek.k_i2(1 / (1 / T + h))) - math.log(ek.k_i2(1 / (1 / T - h)))) / (2 * h)
    dH = -slope * 8.314462618 / 1000
    assert 150 < dH < 156

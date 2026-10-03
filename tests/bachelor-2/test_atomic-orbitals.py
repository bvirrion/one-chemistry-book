import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("ao", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "atomic-orbitals.py"))
ao = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ao)


def test_normalised_and_orthogonal():
    for n, l in ((1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)):
        assert abs(ao.integrate(lambda r: ao.P(n, l, r), 0, 80) - 1) < 1e-6
    # radial parts of 1s and 2s are orthogonal (same angular part)
    ov = ao.integrate(lambda r: r * r * ao.R(1, 0, r) * ao.R(2, 0, r), 0, 80)
    assert abs(ov) < 1e-8


def test_most_probable_radii():
    assert abs(ao.most_probable(1, 0) - 1.0) < 0.01
    assert abs(ao.most_probable(2, 1) - 4.0) < 0.01
    assert abs(ao.most_probable(3, 2) - 9.0) < 0.01
    # mean radius of 1s is 3/2 a0
    assert abs(ao.integrate(lambda r: r * ao.P(1, 0, r), 0, 80) - 1.5) < 1e-6


def test_named_probability():
    p = ao.outside_probability_1s(2.0)
    assert abs(p - 13 * math.exp(-4)) < 1e-12 and round(p, 3) == 0.238
    assert abs(p - ao.integrate(lambda r: ao.P(1, 0, r), 2, 80)) < 1e-8


def test_slater():
    assert [round(ao.zstar_period2(k), 2) for k in (1, 4, 5, 6)] == [1.30, 3.25, 3.90, 4.55]
    assert round(ao.zstar_alkali(11, 3), 2) == 2.20 and round(ao.zstar_alkali(55, 6), 2) == 2.20
    assert round(ao.slater_ie_2p(4), 1) == 11.5     # carbon, measured 11.26 eV

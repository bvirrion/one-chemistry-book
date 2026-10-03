import importlib.util
import os

spec = importlib.util.spec_from_file_location("pd", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "polymer-distributions.py"))
pd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pd)


def test_flory_normalised_and_dispersity():
    for p in (0.9, 0.98, 0.99):
        nums = [(x, pd.flory_number(x, p)) for x in range(1, 20000)]
        assert abs(sum(n for _, n in nums) - 1) < 1e-9
        xn, xw = pd.averages(nums)
        assert abs(xn - pd.carothers(p)) < 1e-6
        assert abs(xw / xn - (1 + p)) < 1e-6
        assert abs(sum(pd.flory_mass(x, p) for x in range(1, 20000)) - 1) < 1e-9


def test_imbalance_reduces_to_carothers():
    assert abs(pd.imbalance(0.99, 1.0) - pd.carothers(0.99)) < 1e-9
    r = 1 / 1.01
    assert abs(pd.imbalance(1.0, r) - (1 + r) / (1 - r)) < 1e-9
    assert abs(pd.imbalance(1.0, r) - 201) < 1e-6


def test_poisson_dispersity():
    nu = 49
    nums = [(x, pd.poisson_number(x, nu)) for x in range(1, 400)]
    assert abs(sum(n for _, n in nums) - 1) < 1e-9
    xn, xw = pd.averages(nums)
    assert abs(xn - (nu + 1)) < 1e-6
    # exact: X_w/X_n = 1 + nu/(1+nu)^2, close to 1 + 1/X_n
    assert abs(xw / xn - (1 + nu / (1 + nu) ** 2)) < 1e-9
    assert abs(xw / xn - (1 + 1 / xn)) < 1e-3


def test_nylon_named_number():
    m0 = 226.32 / 2
    p = 1 - m0 / 20000
    assert abs(p - 0.99434) < 1e-5

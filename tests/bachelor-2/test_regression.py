import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("rg", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "regression.py"))
rg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rg)


def test_student_closed_forms():
    # nu = 1: Cauchy, t = tan(pi (p - 1/2)); nu = 2: t = (2p - 1)/sqrt(2p(1 - p))
    assert abs(rg.t_quantile(0.975, 1) - math.tan(math.pi * 0.475)) < 1e-3
    p = 0.975
    assert abs(rg.t_quantile(p, 2) - (2 * p - 1) / math.sqrt(2 * p * (1 - p))) < 1e-4


def test_student_tends_to_normal():
    # normal 97.5 % quantile, from the error function
    z = 1.959963985
    assert abs(0.5 * (1 + math.erf(z / math.sqrt(2))) - 0.975) < 1e-9
    assert 1.96 < rg.t_quantile(0.975, 30) < 2.05
    assert all(rg.t_quantile(0.975, a) > rg.t_quantile(0.975, b) for a, b in zip(rg.NUS, rg.NUS[1:]))


def test_least_squares_against_normal_equations():
    b, a, syx, res, _ = rg.fit(rg.CAL_X, rg.CAL_Y)
    assert abs(sum(res)) < 1e-12
    assert abs(sum(r * x for r, x in zip(res, rg.CAL_X))) < 1e-12
    assert abs(b - 0.00978) < 1e-9 and abs(a - 0.0026) < 1e-9


def test_lead_named_number():
    x0, s = rg.interpolate(rg.CAL_X, rg.CAL_Y, rg.SAMPLE_Y)
    t3 = rg.t_quantile(0.975, 3)
    c, u = x0 * rg.DILUTION, t3 * s * rg.DILUTION
    assert abs(c - 10.16) < 0.01 and abs(u - 0.24) < 0.01
    assert c - u < 10 < c + u


def test_standard_addition_intercept():
    b, a, _, _, _ = rg.fit(rg.ADD_X, rg.ADD_Y)
    assert abs(a / b - 3.12) < 0.02


def test_lod():
    b = rg.fit(rg.CAL_X, rg.CAL_Y)[0]
    assert abs(3 * rg.stdev(rg.BLANKS) / b - 0.354) < 0.001

import importlib.util
import math
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")


def load(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), os.path.join(D, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


m = load("boltzmann-populations")
sm = load("_statmech")


def test_populations_sum_to_one():
    for name, jmax in (("HCl", 60), ("CO", 200)):
        th = sm.theta_rot(name)
        for T in m.TEMPS:
            assert abs(sum(sm.populations_rot(th, T, jmax)) - 1) < 1e-9
    th = sm.theta_vib("I2")
    assert abs(sum(sm.populations_vib(th, 1000, 400)) - 1) < 1e-9


def test_most_populated_level():
    for name in ("HCl", "CO"):
        th = sm.theta_rot(name)
        for T in m.TEMPS:
            p = sm.populations_rot(th, T, 80)
            jm = max(range(len(p)), key=p.__getitem__)
            assert abs(jm - sm.j_most(th, T)) <= 0.5 + 1e-9
    assert max(range(15), key=sm.populations_rot(sm.theta_rot("HCl"), 300, 14).__getitem__) == 3


def test_ratio_formula():
    th, T = sm.theta_rot("HCl"), 300
    p = sm.populations_rot(th, T, 5)
    assert abs(p[3] / p[1] - 7 / 3 * math.exp(-th * (12 - 2) / T)) < 1e-12

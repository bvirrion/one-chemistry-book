import importlib.util
import os

spec = importlib.util.spec_from_file_location("tc", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "titration-curves.py"))
tc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tc)
E = tc.ETH


def test_strong_acid_curve():
    assert round(tc.curve(0, strong=0.1), 2) == 1.00
    assert abs(tc.curve(10, strong=0.1) - 7.0) < 0.01
    assert round(tc.curve(9.9, strong=0.1), 1) == 3.3
    assert round(tc.curve(10.1, strong=0.1), 1) == 10.7


def test_weak_acid_curve():
    assert round(tc.curve(0, weak=[(0.1, [E])]), 2) == 2.88
    assert round(tc.curve(5, weak=[(0.1, [E])]), 2) == 4.76      # half-equivalence: pKa
    assert round(tc.curve(10, weak=[(0.1, [E])]), 2) == 8.73     # 7 + (pKa + log C')/2


def test_mixture_and_phosphoric():
    assert round(tc.curve(7.5, strong=0.05, weak=[(0.05, [E])]), 2) == 4.76
    assert round(tc.curve(10, strong=0.05, weak=[(0.05, [E])]), 2) == 8.58
    assert round(tc.curve(10, weak=[(0.1, tc.PHOS)]), 2) == 4.71
    assert round(tc.curve(20, weak=[(0.1, tc.PHOS)]), 2) == 9.66


def test_potentiometric_points():
    assert round(tc.potentiometric(5), 2) == 0.77
    assert round(tc.potentiometric(10), 2) == 1.39
    assert round(tc.potentiometric(20), 2) == 1.51


def test_conductimetric():
    lam = tc.ionic_conductivities()
    assert round(lam["Cl-"], 1) == 76.2 and round(lam["Na+"], 1) == 50.3
    assert round(tc.conductimetric(0), 2) == 4.26
    k = [tc.conductimetric(v) for v in (0, 5, 10, 15, 20)]
    assert k[0] > k[1] > k[2] < k[3] < k[4]


def test_vitamin_c_problem():
    n_i2 = 20.00e-3 * 0.0250
    n_thio = 8.90e-3 * 0.0500
    n_asc = (n_i2 - n_thio / 2) * 100.0 / 10.00
    assert round(n_asc * 176.0, 2) == 0.49

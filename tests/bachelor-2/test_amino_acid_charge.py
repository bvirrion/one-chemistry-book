import importlib.util
import os

spec = importlib.util.spec_from_file_location("aa", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "amino-acid-charge.py"))
aa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aa)


def test_isoelectric_points():
    # neutral side chain: pI = (pKa1 + pKa2)/2
    gly = aa.groups("glycine")
    assert abs(aa.isoelectric(gly) - (gly[0][0] + gly[1][0]) / 2) < 1e-6
    # acidic: between the two carboxylic pKa; basic: between the two ammonium pKa
    asp = aa.groups("asp")
    assert abs(aa.isoelectric(asp) - (asp[0][0] + asp[1][0]) / 2) < 0.02
    lys = aa.groups("lys")
    assert abs(aa.isoelectric(lys) - (lys[1][0] + lys[2][0]) / 2) < 0.02


def test_limits():
    assert abs(aa.net_charge(aa.groups("lys"), 0) - 2) < 0.02
    assert abs(aa.net_charge(aa.groups("asp"), 14) + 2) < 1e-3
    assert abs(aa.net_charge(aa.groups("glycine"), 7) - 0) < 1e-2


def test_fractions_sum_to_one():
    for ph in (1, 2.35, 6, 9.78, 12):
        assert abs(sum(aa.glycine_fractions(ph)) - 1) < 1e-12
    c, z, a = aa.glycine_fractions(6.0)
    assert z > 0.999

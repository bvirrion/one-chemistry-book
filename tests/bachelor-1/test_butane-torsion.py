import importlib.util
import os

spec = importlib.util.spec_from_file_location("bt", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "butane-torsion.py"))
bt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bt)


def test_reproduces_the_cccbdb_table():
    # the source tabulates 16.56 (0 deg), 2.83 (62), 15.19 (119.2), 0 (180) kJ/mol
    for theta, e in ((0, 16.56), (62, 2.83), (119.2, 15.19), (90, 8.36)):
        assert abs(bt.butane(theta) - e) < 0.05, (theta, bt.butane(theta))
    assert abs(bt.butane(180)) < 1e-9
    assert round(bt.ethane(0), 1) == 12.2       # 12.25 in the source


def test_printed_values():
    t, e = bt.gauche_minimum()
    assert round(t) == 62 and round(e, 1) == 2.8
    assert round(2 * e, 1) == 5.7             # two gauche interactions: axial methyl estimate

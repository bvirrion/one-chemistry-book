import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("gm", os.path.join(D, "green-metrics.py"))
gm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gm)


def test_ibuprofen_routes():
    assert abs(100 * gm.atom_economy("ibuprofen-3") - 206.0 / 266.0 * 100) < 0.05
    assert abs(100 * gm.atom_economy("ibuprofen-6") - 206.0 / 514.5 * 100) < 0.05


def test_ethylene_oxide_routes():
    assert abs(gm.atom_economy("EO-direct") - 1.0) < 1e-12
    assert abs(gm.atom_economy("EO-chlorohydrin") - 44.0 / 173.1) < 1e-4


def test_e_min_relation():
    for n in gm.ROUTES:
        ae = gm.atom_economy(n)
        assert abs(gm.e_min(n) - (1 / ae - 1)) < 1e-12

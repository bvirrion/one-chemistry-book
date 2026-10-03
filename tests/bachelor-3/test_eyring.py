import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("ey", os.path.join(D, "eyring.py"))
ey = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ey)


def test_regression_recovers_parameters():
    h, d = ey.eyring(1), ey.eyring(2)
    assert abs(h["dH"] - ey.DH_H) < 3 * h["s_dH"]
    assert abs(d["dH"] - ey.DH_H - ey.ddh()) < 3 * d["s_dH"]
    assert abs(h["dS"] - ey.DS) < 3 * h["s_dS"]


def test_printed_values():
    h, d = ey.eyring(1), ey.eyring(2)
    assert round(h["dH"] / 1000, 1) == 61.9 and round(d["dH"] / 1000, 1) == 66.8
    assert round(ey.ddh() / 1000, 2) == 4.83
    assert ey.data()[0] == (278.15, 0.00989, 0.00117)

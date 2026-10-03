"""Tests for figdata/grade-12/ph-conductivity-titrations.py."""
import importlib.util, os

spec = importlib.util.spec_from_file_location(
    "tit", os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12",
                        "ph-conductivity-titrations.py"))
tit = importlib.util.module_from_spec(spec); spec.loader.exec_module(tit)


def test_strong_strong():
    assert abs(tit.ph_strong(20.0) - 7.00) < 0.005               # pH at equivalence
    assert abs(tit.v_of_max_slope(tit.curve(tit.ph_strong, 30.0)) - 20.0) < 0.06
    assert abs(tit.ph_strong(0) - 1.00) < 0.005


def test_weak_strong():
    rows = tit.curve(tit.ph_weak, 16.0)
    veq = tit.v_of_max_slope(rows)
    assert abs(veq - 10.1) < 0.06                                   # C V / C'
    assert abs(tit.ph_weak(veq / 2) - 4.76) < 0.05                  # half-equivalence
    assert tit.ph_weak(10.1) > 8.0


def test_conductivity_minimum_at_equivalence():
    rows = tit.conductimetric()
    vmin = min(rows, key=lambda r: r[1])[0]
    assert vmin == 10.0
    assert rows[0][1] > rows[20][1] < rows[-1][1]

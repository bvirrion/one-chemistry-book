import importlib.util
import os

spec = importlib.util.spec_from_file_location("se", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "standard-entropy.py"))
se = importlib.util.module_from_spec(spec)
spec.loader.exec_module(se)


def test_third_law_start_and_monotone():
    pts = se.s_solid_points() + se.s_liquid_points() + se.s_gas_points()
    assert pts[0] == (0, 0.0)
    assert all(b[1] >= a[1] for a, b in zip(pts, pts[1:]))


def test_jumps_are_transition_enthalpy_over_temperature():
    ds, dh_t, dh = se.fusion_jump()
    assert abs(ds - dh_t) < 0.01 and round(ds, 1) == 10.6 and round(dh / 1000, 2) == 7.32
    ds, dh_t, dh = se.vaporisation_jump()
    assert abs(ds - dh_t) < 0.05 and round(ds, 1) == 97.7 and round(dh / 1000, 1) == 115.3


def test_integral_of_cp_over_t():
    d = se.entropy_from_cp(300.0, 600.0)
    tab = se.value("s0T:Zn_crl.600") - 41.874   # S(300 K) of the table
    assert abs(d - tab) < 0.05
    # agreement with the CODATA key value at 298.15 K
    assert abs(se.value("s0T:Zn_crl.298.15") - 41.63) < 0.15

import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("mm", os.path.join(D, "michaelis-menten.py"))
mm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mm)


def test_half_rate_at_km_and_competitive_lines_meet():
    assert abs(mm.mm(mm.KM) - mm.VMAX / 2) < 1e-12
    rows = mm.lb_rows()
    x0 = [r for r in rows if abs(r[0]) < 1e-9][0]
    assert abs(x0[1] - x0[2]) < 1e-12              # same 1/V_max intercept
    assert abs(x0[3] - 2 * x0[1]) < 1e-12          # uncompetitive: intercept doubled


def test_fits():
    f = mm.fit_mm(mm.rate_data())
    assert abs(f["KM"] - mm.KM) < 3 * f["s_KM"] and abs(f["Vmax"] - mm.VMAX) < 3 * f["s_Vmax"]
    assert round(f["KM"], 3) == 0.801 and round(f["Vmax"], 3) == 0.502
    k = mm.fit_ki()
    assert abs(k["Ki"] - mm.KI) < 3 * k["s_Ki"] and round(k["Ki"], 1) == 24.9


def test_burst():
    kc = mm.K2 * mm.K3 / (mm.K2 + mm.K3)
    assert abs(kc - 100) < 1e-9
    late = mm.burst(0.05) - mm.burst(0.04)
    assert abs(late / 0.01 - mm.E0_SF * kc) < 1e-6

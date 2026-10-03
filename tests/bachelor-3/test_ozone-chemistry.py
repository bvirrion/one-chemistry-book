import importlib.util
import math
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("oz", os.path.join(D, "ozone-chemistry.py"))
oz = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oz)


def test_chapman_steady_state_is_the_ode_limit():
    sol = oz.runs(days=400)
    assert abs(sol[0.0][-1][1][0] / oz.o3_chapman() - 1) < 2e-3
    assert abs(sol[3.0e7][-1][1][0] / oz.o3_steady_with_cl(3.0e7) - 1) < 2e-3
    assert oz.o3_steady_with_cl(1e7) < oz.o3_chapman()


def test_printed_numbers():
    assert round(oz.o3_chapman() / 1e12, 1) == 5.7
    assert round(oz.chain()["cycles"]) == 40
    assert round(oz.leighton_ppb(1.5)) == 26


def test_leighton_relation():
    k = oz.value("kin:NO+O3.A") * math.exp(-oz.value("kin:NO+O3.EaR") / 298.15)
    n = 1e5 / (oz.value("const:kB") * 298.15) * 1e-6
    assert abs(oz.leighton_ppb(2.0) * 1e-9 * n * k - 2.0 * oz.J_NO2) < 1e-9

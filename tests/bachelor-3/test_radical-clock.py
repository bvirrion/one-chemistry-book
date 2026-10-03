import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("rc", os.path.join(D, "radical-clock.py"))
rc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rc)


def test_inverse_plot_slope():
    c1, c2 = 0.2, 0.8
    s = (1 / rc.ratio_cyc_direct(c2) - 1 / rc.ratio_cyc_direct(c1)) / (c2 - c1)
    assert abs(s - rc.KH / rc.KC) < 1e-9


def test_half_cyclised_at_kc_over_kh():
    assert abs(rc.frac_cyclised(rc.KC / rc.KH) - 0.5) < 1e-12

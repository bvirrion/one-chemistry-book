import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("sc", os.path.join(D, "surfactant-cmc.py"))
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)


def test_break_at_cmc():
    assert abs(sc.gamma(sc.CMC) - sc.G_CMC) < 1e-9
    assert sc.gamma(2 * sc.CMC) == sc.gamma(sc.CMC)
    k1 = (sc.kappa(0.8 * sc.CMC) - sc.kappa(0.4 * sc.CMC)) / (0.4 * sc.CMC)
    k2 = (sc.kappa(2.0 * sc.CMC) - sc.kappa(1.5 * sc.CMC)) / (0.5 * sc.CMC)
    assert abs(k2 / k1 - 0.4) < 1e-9


def test_gibbs_slope_gives_gamma_max_at_high_c():
    g = sc.surface_excess(0.99 * sc.CMC)
    assert 0.8 * sc.GMAX < g < sc.GMAX
    assert sc.surface_excess(1e-6) < 0.01 * sc.GMAX

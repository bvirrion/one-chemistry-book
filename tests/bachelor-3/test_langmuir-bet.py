import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("lb", os.path.join(D, "langmuir-bet.py"))
lb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lb)


def test_langmuir_half_coverage():
    K = lb.K_ADS(300)
    assert abs(lb.langmuir(1 / K, K) - 0.5) < 1e-12


def test_bet_linear_form_recovers_parameters():
    exact = [(x, lb.bet(x)) for x in lb.X_DATA]
    f = lb.fit_bet(exact)
    assert abs(f["vm"] - lb.VM) < 1e-9 and abs(f["c"] - lb.CB) < 1e-6
    g = lb.fit_bet()
    assert abs(g["vm"] - lb.VM) / lb.VM < 0.02


def test_catalyst_numbers():
    assert round(lb.area_bet(lb.fit_bet()["vm"])) == 196
    assert round(lb.dispersion()[0], 3) == 0.357
    assert round(lb.diameter_nm(), 1) == 3.1
    assert abs(lb.pt_geometry()[1] - 8.07) < 0.01

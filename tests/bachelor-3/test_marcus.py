import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("ma", os.path.join(D, "marcus.py"))
ma = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ma)


def test_activation_and_maximum():
    assert ma.dg_act(0) == ma.LAM / 4
    assert ma.dg_act(-ma.LAM) == 0
    ks = [(m, ma.log10k(-m)) for m in range(0, 251)]
    assert max(ks, key=lambda p: p[1])[0] == ma.LAM


def test_crossing_point_on_both_parabolas():
    for dg in ma.DGS:
        x = ma.crossing(dg)
        assert abs(ma.LAM * x * x - (ma.LAM * (x - 1) ** 2 + dg)) < 1e-9
        assert abs(ma.LAM * x * x - ma.dg_act(dg)) < 1e-9

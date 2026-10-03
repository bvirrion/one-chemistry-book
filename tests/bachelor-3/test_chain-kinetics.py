import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("ck", os.path.join(D, "chain-kinetics.py"))
ck = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ck)


def test_steady_state_law_after_induction():
    rows = ck.rows(ck.integrate(tmax=200.0, dt=2e-3, every=500))
    late = [r for r in rows if r[0] >= 30]
    assert all(abs(v - vss) / vss < 0.01 for _, _, v, vss, _ in late)
    early = [r for r in rows if 0 < r[0] <= 2]
    assert all(v < 0.5 * vss for _, _, v, vss, _ in early)        # induction period


def test_conservation():
    sol = ck.integrate(tmax=50.0, dt=2e-3, every=1000)
    for _, (h2, br2, hbr, br, h) in sol:
        assert abs(2 * h2 + hbr + h - 2) < 1e-9          # hydrogen atoms
        assert abs(2 * br2 + hbr + br - 2) < 1e-9        # bromine atoms

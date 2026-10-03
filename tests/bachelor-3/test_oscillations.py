import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("osc", os.path.join(D, "oscillations.py"))
osc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(osc)


def test_hopf_boundary():
    for b, unstable in ((1.9, False), (2.1, True), (3.0, True)):
        assert (osc.jacobian_eigs(1.0, b)[0].real > 0) == unstable
    assert abs(osc.jacobian_eigs(1.0, 2.0)[0].real) < 1e-12


def test_limit_cycle_and_invariant():
    ts, inner, outer, orbits = osc.runs()
    p = osc.period(ts)
    assert 6.5 < p < 7.8
    # both starts end on the same cycle: compare the X ranges of the last part
    ri = [y[0] for _, y in inner[-300:]]
    ro = [y[0] for _, y in outer[-300:]]
    assert abs(max(ri) - max(ro)) < 0.05
    for o in orbits:
        v = [osc.lv_invariant(*y) for _, y in o]
        assert max(v) - min(v) < 1e-6

import importlib.util
import os

spec = importlib.util.spec_from_file_location("ep", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "energy-profiles.py"))
ep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ep)


def test_stationary_points():
    h = 1e-6
    for pts in ep.PROFILES.values():
        for x, e in pts:
            assert abs(ep.energy(pts, x) - e) < 1e-12
            if 0 < x < 10:
                d = (ep.energy(pts, x + h) - ep.energy(pts, x - h)) / (2 * h)
                assert abs(d) < 1e-4


def test_monotonic_between_points():
    for pts in ep.PROFILES.values():
        for (x0, e0), (x1, e1) in zip(pts, pts[1:]):
            xs = [x0 + (x1 - x0) * i / 50 for i in range(51)]
            es = [ep.energy(pts, x) for x in xs]
            assert es == sorted(es) or es == sorted(es, reverse=True)


def test_catalyst_keeps_reaction_energy_and_lowers_barrier():
    u, c = ep.PROFILES["uncatalysed"], ep.PROFILES["catalysed"]
    assert u[-1][1] == c[-1][1]
    assert max(e for _, e in c) < max(e for _, e in u)

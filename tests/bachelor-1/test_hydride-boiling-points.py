import importlib.util
import os

spec = importlib.util.spec_from_file_location("hb", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "hydride-boiling-points.py"))
hb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hb)


def test_group14_monotonic():
    b = [v for _, v in hb.series(14)]
    assert b == sorted(b)


def test_hydrogen_bond_anomalies():
    for g in (15, 16, 17):
        s = hb.series(g)
        (p2, b2), (p3, b3), (p4, b4) = s[0], s[1], s[2]
        extrapolated = b3 - (b4 - b3)
        assert b2 > extrapolated + 30   # NH3, H2O, HF far above the trend
    assert hb.series(16)[0][1] > hb.series(15)[0][1] and hb.series(16)[0][1] > hb.series(17)[0][1]


def test_alkanes_increase():
    b = [hb.bp_c(f) for f in hb.ALKANES]
    assert all(x < y for x, y in zip(b, b[1:]))


def test_printed_values():
    assert round(hb.water_without_hbond()) == -79
    assert round(hb.bp_c("H2O"), 1) == 100.0
    assert round(hb.bp_c("H2S"), 1) == -60.3

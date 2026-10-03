import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("ta", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "type-a-uncertainty.py"))
ta = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ta)


def test_printed_statistics():
    # the values printed in ch. 29 (example and figure caption)
    assert len(ta.READINGS) == 20
    assert round(ta.mean(), 3) == 12.455
    assert round(ta.std(), 3) == 0.071
    assert round(ta.u_mean(), 3) == 0.016
    assert round(2 * ta.u_mean(), 2) == 0.03


def test_histogram_counts_every_reading_once():
    h = ta.histogram()
    assert sum(c for _, c in h) == len(ta.READINGS)
    assert dict(h)[12.45] == 7 and h[0][1] == 0 and h[-1][1] == 0


def test_gaussian_has_the_histogram_area():
    g = ta.gaussian(npts=2001)
    dx = g[1][0] - g[0][0]
    area = sum(y for _, y in g) * dx
    assert math.isclose(area / ta.BIN, len(ta.READINGS), rel_tol=2e-3)

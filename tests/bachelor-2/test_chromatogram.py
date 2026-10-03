import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("ch", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "chromatogram.py"))
ch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ch)


def test_van_deemter_minimum():
    u, h = ch.optimum()
    assert abs(u - 2.0) < 1e-12 and abs(h - 30.0) < 1e-12
    for du in (-0.3, 0.3):
        assert ch.van_deemter(u + du) > h


def test_problem_numbers():
    n = ch.plate_number(3.4, 0.20)
    assert abs(n - 4624) < 1e-6
    rs = ch.resolution(3.0, 0.18, 3.4, 0.20)
    assert abs(rs - 0.8 / 0.38) < 1e-12
    # resolution equation with k2 = 2.4, alpha = 2.4/2.0
    assert abs(ch.resolution_equation(n, 1.2, 2.4) - 2.0) < 0.01
    # halving the column: R_s / sqrt(2)
    assert abs(rs / math.sqrt(2) - 1.49) < 0.01


def test_resolution_peaks_separation():
    # at R_s = 1.5 the valley between the peaks is essentially at baseline
    assert ch.two_peaks(0.0, 1.5) < 0.03
    assert ch.two_peaks(0.0, 0.75) > 0.6


def test_caffeine_named_number():
    f = (1500 / 1000) / (50.0 / 40.0)
    assert abs(f - 1.2) < 1e-12
    c = (970 / 1010) / f * 40.0 * 10
    assert abs(c * 0.250 - 80.03) < 0.01

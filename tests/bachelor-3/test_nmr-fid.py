import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("nf", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "nmr-fid.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_peaks_at_offsets_and_width():
    f, r = m.spectrum()
    for f0 in m.OFFSETS:
        sel = [(abs(a - f0), b) for a, b in zip(f, r) if abs(a - f0) < 20]
        best = max(sel, key=lambda x: x[1])
        assert best[0] < 0.5
        assert abs(m.fwhm_of_line(f0) - 1 / (math.pi * m.T2)) < 0.3

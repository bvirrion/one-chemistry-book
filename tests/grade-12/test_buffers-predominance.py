"""Tests for figdata/grade-12/buffers-predominance.py."""
import importlib.util, os

spec = importlib.util.spec_from_file_location(
    "bp", os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12", "buffers-predominance.py"))
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)


def test_crossing_at_pka():
    assert abs(bp.frac_acid(4.76) - 0.5) < 1e-12
    c, z, a = bp.glycine(2.35)
    assert abs(c - z) < 1e-3
    c, z, a = bp.glycine(9.78)
    assert abs(z - a) < 1e-3


def test_fractions_sum_to_one():
    for ph in (0, 3, 6.0, 9, 14):
        assert abs(sum(bp.glycine(ph)) - 1) < 1e-12
    assert all(abs(r[1] + r[2] - 1) < 1e-3 for r in bp.table_a())


def test_buffer_barely_moves():
    rows = bp.table_c()
    assert abs(rows[0][2] - 4.76) < 1e-9
    assert max(r[2] for r in rows) - min(r[2] for r in rows) < 0.1
    assert rows[0][1] - rows[-1][1] > 4          # water: from 7 to about 2

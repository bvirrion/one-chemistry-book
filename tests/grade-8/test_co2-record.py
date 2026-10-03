"""Tests for figdata/grade-8/co2-record.py (NOAA GML Mauna Loa annual means)."""
import importlib.util, os

spec = importlib.util.spec_from_file_location(
    "co2", os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-8", "co2-record.py"))
co2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(co2)


def test_endpoints_match_ledger():
    d = dict(co2.record())
    assert d[1959] == 315.98          # ledger co2:mlo-1959
    assert d[2025] == 427.35          # ledger co2:mlo-2025


def test_every_year_present_and_rising():
    years = [y for y, _ in co2.record()]
    assert years == list(range(1959, 2026))
    vals = [v for _, v in co2.record()]
    assert all(b > a for a, b in zip(vals, vals[1:]))


def test_rise_quoted_in_chapter():
    assert round(co2.rise(1959, 2025), 1) == 111.4

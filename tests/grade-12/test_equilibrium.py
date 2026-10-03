"""Tests for figdata/grade-12/equilibrium.py."""
import importlib.util, os

spec = importlib.util.spec_from_file_location(
    "eq", os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12", "equilibrium.py"))
eq = importlib.util.module_from_spec(spec); spec.loader.exec_module(eq)


def test_both_runs_reach_two_thirds():
    rows = eq.table()
    assert abs(rows[-1][1] - 2 / 3) < 0.005
    assert abs(rows[-1][2] - 2 / 3) < 0.005


def test_runs_approach_from_both_sides():
    rows = eq.table()
    assert all(r[1] <= 2 / 3 + 1e-4 for r in rows)
    assert all(r[2] >= 2 / 3 - 1e-4 for r in rows)


def test_final_extents():
    assert abs(eq.final_extent(1, 1) - 2 / 3) < 1e-9
    assert round(eq.final_extent(1, 3), 3) == 0.903          # threefold excess: 90 %

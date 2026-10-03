"""Tests for figdata/grade-12/proton-nmr.py."""
import importlib.util, os, math

spec = importlib.util.spec_from_file_location(
    "nmr", os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12", "proton-nmr.py"))
nmr = importlib.util.module_from_spec(spec); spec.loader.exec_module(nmr)


def test_integration_steps_equal_proton_counts():
    # Lorentzian tails outside the window lose about 1-2 % of each signal
    for c, hs in (("ethanol", [2, 1, 3]), ("ethylethanoate", [2, 3, 3]),
                  ("propanone", [6]), ("propanoic", [1, 2, 3]),
                  ("methylethanoate", [3, 3])):
        got = nmr.steps(c)
        assert all(abs(g - h) <= 0.15 for g, h in zip(got, hs)), (c, got)


def test_multiplets_binomial_and_centred_on_ledger_shifts():
    ls = [l for l in nmr.lines("ethylethanoate") if 3.9 < l[0] < 4.4]
    assert len(ls) == 4                                       # quartet
    areas = [a for _, a in ls]
    assert [round(a / areas[0], 6) for a in areas] == [1, 3, 3, 1]
    assert abs(sum(p for p, _ in ls) / 4 - 4.12) < 1e-9       # nmr:ethylethanoate-OCH2
    tri = [l for l in nmr.lines("ethanol") if 1.0 < l[0] < 1.5]
    assert len(tri) == 3 and abs(tri[1][0] - 1.23) < 1e-9     # nmr:ethanol-CH3


def test_total_integral():
    rows = nmr.table("ethylethanoate")
    assert abs(rows[-1][2] - 8.0) < 0.15                      # 8 H, C4H8O2

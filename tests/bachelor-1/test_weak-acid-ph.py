import importlib.util
import os

spec = importlib.util.spec_from_file_location("wa", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "weak-acid-ph.py"))
wa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wa)
PKA = wa.value("pka:ethanoic")


def test_weak_acid_domain():
    for pc in (0.5, 1, 2):
        assert abs(wa.ph_weak_acid(10 ** -pc, PKA) - (PKA + pc) / 2) < 0.02


def test_dilute_limit_is_neutral():
    assert abs(wa.ph_weak_acid(1e-9, PKA) - 7.0) < 0.01


def test_printed_values():
    assert round(wa.ph_weak_acid(0.10, PKA), 2) == 2.88
    assert round(wa.ph_weak_acid(1e-6, PKA), 2) == 6.02

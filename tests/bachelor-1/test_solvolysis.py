import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("sv", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "solvolysis.py"))
sv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sv)


def test_printed_data():
    assert [sv.kappa(t) for t in sv.TIMES] == [0.0, 0.172, 0.329, 0.473, 0.605, 0.835, 1.11, 1.321]
    assert [sv.kappa(t, 35.0) for t in sv.TIMES] == [0.0, 0.507, 0.885, 1.168, 1.379, 1.654, 1.856, 1.94]


def test_analysis_recovers_k_and_ea():
    assert abs(sv.fit_k(25.0) - 3.0e-4) < 0.02e-4
    assert round(sv.activation_energy() / 1000) == 90
    assert round(math.log(2) / sv.fit_k(25.0) / 60) == 38       # half-life, min

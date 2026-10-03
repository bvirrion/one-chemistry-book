import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("cs", os.path.join(D, "carbonate-system.py"))
cs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cs)


def test_crossings_at_pka():
    a0, a1, _ = cs.fractions(6.35)
    assert abs(a0 - a1) < 1e-3
    _, a1, a2 = cs.fractions(10.33)
    assert abs(a1 - a2) < 1e-3
    assert abs(sum(cs.fractions(8.0)) - 1) < 1e-12


def test_rain_pH_today():
    assert abs(cs.rain_pH(cs.value("atm:CO2.2025")) - 5.6) < 0.05

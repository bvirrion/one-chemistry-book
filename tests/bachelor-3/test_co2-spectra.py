import importlib.util
import os

spec = importlib.util.spec_from_file_location("co2", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "co2-spectra.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_ir_bands_at_ledger_positions():
    for x0 in (m.value("vib:CO2.bend"), m.value("vib:CO2.asym")):
        assert m.ir(x0) > m.ir(x0 - 3) and m.ir(x0) > m.ir(x0 + 3)
    assert abs(m.ir(m.value("vib:CO2.asym")) - 1) < 0.01


def test_mutual_exclusion():
    assert m.ir(m.value("vib:CO2.sym")) < 0.005
    assert m.raman(m.value("vib:CO2.asym")) < 0.001 and m.raman(m.value("vib:CO2.bend")) < 0.001

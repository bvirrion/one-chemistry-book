import importlib.util
import os

spec = importlib.util.spec_from_file_location("ct", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "cell-thermodynamics.py"))
ct = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ct)


def test_standard_voltage():
    h, g, ts, e, s = ct.standard_values()
    assert round(e, 2) == 1.23
    assert round(g, 1) == -237.1          # CODATA values agree with JANAF -237.141
    assert abs(g - ct.value("janafG:H2O_l.298")) < 0.05
    assert round(s, 1) == -163.3


def test_voltage_falls_with_temperature():
    for series in (ct.e_liquid(), ct.e_gas()):
        es = [e for _, e in series]
        assert all(b < a for a, b in zip(es, es[1:]))
    assert round(ct.e_gas()[0][1], 2) == 1.18


def test_efficiency_beats_carnot_at_low_temperature():
    eta = dict(ct.efficiency_gas())
    assert eta[400] > 1 - ct.T0 / 400
    assert eta[1000] > 1 - ct.T0 / 1000
    # the Carnot efficiency overtakes the cell between 1100 and 1300 K
    assert eta[1100] > 1 - ct.T0 / 1100 and eta[1300] < 1 - ct.T0 / 1300

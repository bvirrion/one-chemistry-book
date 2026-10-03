import importlib.util
import os

spec = importlib.util.spec_from_file_location("di", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "diatomics.py"))
di = importlib.util.module_from_spec(spec)
spec.loader.exec_module(di)


def test_dissociation_energies():
    assert round(di.d0_kj("O2") / di.EV, 2) == 5.12
    assert round(di.d0_kj("N2") / di.EV, 2) == 9.76
    assert round(di.d0_kj("CO") / di.EV, 1) == 11.1


def test_order_length_trend():
    # along N2, O2, F2 the bond order falls, the bond lengthens and weakens
    seq = ["N2", "O2", "F2"]
    assert di.re_pm("N2") < di.re_pm("O2") < di.re_pm("F2")
    assert di.d0_kj("N2") > di.d0_kj("O2") > di.d0_kj("F2")


def test_ion_cycle():
    assert round(di.ion_d0_ev("O2", di.value("ie:O"), di.value("ie:O2")), 2) == 6.66
    assert round(di.ion_d0_ev("N2", di.value("ie:N"), di.value("ie:N2")), 2) == 8.71

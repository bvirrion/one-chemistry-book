import importlib.util
import os

spec = importlib.util.spec_from_file_location("ie", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1", "ionisation-energies.py"))
ie = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ie)
E = {s: e for _, s, e in ie.first_ie()}
Z = {s: z for z, s, _ in ie.first_ie()}


def test_noble_gases_are_maxima_alkali_minima():
    seq = [e for _, _, e in ie.first_ie()]
    for s in ("He", "Ne", "Ar"):
        z = Z[s]
        assert seq[z - 1] > seq[z - 2] and seq[z - 1] > seq[z]
    for s in ("Li", "Na", "K"):
        z = Z[s]
        assert seq[z - 1] < seq[z - 2] and seq[z - 1] < seq[z]
    assert E["Kr"] == max(E[s] for s in ("Ga", "Ge", "As", "Se", "Br", "Kr"))


def test_subshell_anomalies():
    assert E["B"] < E["Be"] and E["Al"] < E["Mg"] and E["Ga"] < E["Zn"]
    assert E["O"] < E["N"] and E["S"] < E["P"] and E["Se"] < E["As"]


def test_magnesium_jump():
    s = [e for _, e in ie.successive_mg()]
    assert s[2] / s[1] > 5 > s[1] / s[0]


def test_printed_values():
    assert round(E["Na"], 2) == 5.14 and round(E["Mg"], 2) == 7.65
    assert round(E["Al"], 2) == 5.99 and round(E["Ar"], 2) == 15.76

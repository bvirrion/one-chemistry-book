import importlib.util
import os

import numpy as np

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("ts", os.path.join(D, "tanabe-sugano.py"))
ts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ts)
lf = ts.spectrum_with_spin.__globals__


def test_free_ion_terms():
    B, C = 1000.0, 4500.0
    w, _, _ = lf["levels"](3, 0.0, B, C, 3)
    e = sorted(set(np.round(w - w.min(), 6)))
    assert len(e) == 2 and abs(e[1] - 15 * B) < 1e-6          # 4F, 4P
    w, _, _ = lf["levels"](8, 0.0, B, 4.71 * B, 2)
    e = sorted(set(np.round(w - w.min(), 6)))
    assert abs(e[1] - 15 * B) < 1e-6                         # 3F, 3P


def test_d3_quartets_and_closed_formula():
    B, C, D = 700.0, 3150.0, 17000.0
    w, _, _ = lf["levels"](3, D, B, C, 3)
    e = sorted(set(np.round(w - w.min(), 4)))
    assert abs(e[1] - D) < 1e-6                              # nu1 = Delta exactly
    assert abs(e[2] - ts.d3_nu2(D, B)) < 1e-4
    w, _, _ = lf["levels"](8, D, B, 4.71 * B, 2)
    e = sorted(set(np.round(w - w.min(), 4)))
    assert abs(e[1] - D) < 1e-6                              # d8: 3T2g at Delta


def test_free_ion_B_and_gems():
    assert round(ts.free_ion_B("Cr3")) == 917
    d1, b1 = ts.fit_d3(ts.value("lf:ruby.nu1"), ts.value("lf:ruby.nu2"))
    d2, b2 = ts.fit_d3(ts.value("lf:emerald.nu1"), ts.value("lf:emerald.nu2"))
    assert abs(ts.d3_nu2(d1, b1) - ts.value("lf:ruby.nu2")) < 0.01
    assert d1 - d2 == 1080 and 0.6 < b1 / ts.free_ion_B("Cr3") < 0.75

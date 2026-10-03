import importlib.util
import math
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("ed", os.path.join(D, "er-ddg.py"))
ed = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ed)


def test_er_is_boltzmann_ratio():
    er = (1 + ed.ee_from_ddg(9.0, 298.15)) / (1 - ed.ee_from_ddg(9.0, 298.15))
    assert abs(er - math.exp(9000 / (ed.R * 298.15))) < 1e-9 * er


def test_named_number():
    assert abs(ed.ddg_for_ee(0.95, 298.15) - 9.08) < 0.01


def test_chromatogram_areas_give_ee():
    a1, a2 = ed.areas()
    assert abs((a1 - a2) / (a1 + a2) - 0.95) < 1e-3

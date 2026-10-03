import importlib.util
import math
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("kie", os.path.join(D, "kie.py"))
kie = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kie)


def test_formula_and_limits():
    assert abs(kie.kie("CH", 298.15) - math.exp(kie.C2 * (2917 - kie.nu_d("CH")) / (2 * 298.15))) < 1e-9
    assert kie.kie("CH", 1e6) < 1.01                    # -> 1 at high temperature
    assert kie.kie("OH", 298.15) > kie.kie("NH", 298.15) > kie.kie("CH", 298.15)
    assert round(kie.kie("CH", 298.15), 1) == 6.5


def test_reduced_mass_ratio_close_to_measured_cd4():
    assert abs(kie.nu_d("CH") - kie.value("vib:CD4.nu1")) / kie.value("vib:CD4.nu1") < 0.02

import importlib.util
import os

spec = importlib.util.spec_from_file_location("el", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "ellingham.py"))
el = importlib.util.module_from_spec(spec)
spec.loader.exec_module(el)


def test_lines_follow_janaf():
    # 2 C + O2 = 2 CO at 1100 K is twice DfG(CO)
    assert abs(el.janaf_at("C-CO", 1100) - 2 * el.value("janafG:CO.1100")) < 1e-9
    # slopes: metal oxides rise (DS < 0), C/CO falls, C/CO2 nearly flat
    a = el.janaf_line("MgO")
    assert a[-1][1] > a[0][1]
    c = el.janaf_line("C-CO")
    assert c[-1][1] < c[0][1]
    d = el.janaf_line("C-CO2")
    assert abs(d[-1][1] - d[0][1]) < 5


def test_zinc_breaks():
    sol, liq, gas = el.zinc_phases()
    # slope -DS jumps by 2 DfusS at melting and by 2 DvapS at boiling (kJ/K)
    assert round(-(liq[1] - sol[1]), 4) == round(2 * 7.322 / 692.73, 4)
    assert abs(-(gas[1] - liq[1]) - 2 * 115.311 / 1180.173) < 1e-6
    # the phase actually used changes at the transition temperatures
    assert abs(el.zno(692.73) - (sol[0] - 692.73 * sol[1])) < 1e-2
    assert round(el.zinc_carbon_temperature(), -1) == 1220


def test_hgo_and_boudouard():
    assert round(el.hgo_decomposition_temperature()) == 734
    assert el.boudouard_x_co(1300) > 0.99 and el.boudouard_x_co(700) < 0.05
    T = 1000.0
    x = el.boudouard_x_co(T)
    g = 2 * el.janaf_at_species("CO", T) - el.janaf_at_species("CO2", T)
    import math
    assert abs(x * x / (1 - x) - math.exp(-g * 1000 / (el.R * T))) < 1e-9

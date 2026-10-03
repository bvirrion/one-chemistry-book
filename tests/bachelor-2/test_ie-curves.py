import importlib.util
import math
import os

spec = importlib.util.spec_from_file_location("ie", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "ie-curves.py"))
ie = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ie)


def test_fast_wave_limits_and_half_wave():
    assert abs(ie.fast_wave(2.0, 0.77, 1.0, -1.0) - 1.0) < 1e-9
    assert abs(ie.fast_wave(-1.0, 0.77, 1.0, -1.0) + 1.0) < 1e-9
    # zero current at E1/2 when the two limiting currents are opposite and equal
    assert abs(ie.fast_wave(0.77, 0.77, 1.0, -1.0)) < 1e-12
    # half of the anodic plateau at E1/2 when only the reduced form is present
    assert abs(ie.fast_wave(0.77, 0.77, 1.0, 0.0) - 0.5) < 1e-12


def test_wave_equation_inverts():
    for i in (-0.8, -0.2, 0.3, 0.9):
        E = ie.potential_of(i, 0.77, 1.0, -1.0)
        assert abs(ie.fast_wave(E, 0.77, 1.0, -1.0) - i) < 1e-9
    # 59 mV per decade of (i - ilc)/(ila - i) at 25 degC
    slope = math.log(10) / ie.F_RT
    assert abs(slope - 0.0592) < 1e-4


def test_slow_system_has_a_dead_zone():
    assert abs(ie.slow_wave(0.77, 0.77, 1.0, -1.0)) < 0.01
    assert ie.slow_wave(1.4, 0.77, 1.0, -1.0) > 0.9


def test_mixed_potentials():
    e_zn, i_zn = ie.mixed_potential(ie.H_ON_ZN)
    e_cu, i_cu = ie.mixed_potential(ie.H_ON_CU)
    # at the mixed potential the two currents cancel
    assert abs(ie.exp_branch(e_zn, ie.ZN_ONSET, 0.03, 1) + ie.exp_branch(e_zn, ie.H_ON_ZN, 0.06, -1)) < 1e-9
    # contact with copper raises both the potential and the dissolution current
    assert e_cu > e_zn and i_cu > 10 * i_zn
    # both lie above the zinc onset: zinc is oxidised
    assert e_zn > ie.ZN_ONSET


def test_corrosion_points():
    e_fe, i_fe = ie.corrosion_point(ie.iron)
    # iron alone corrodes at the oxygen limiting current, on the plateau
    assert abs(i_fe - 1.0) < 0.01 and e_fe < -0.2
    e_zn, i_zn = ie.corrosion_point(lambda E: ie.iron(E) + ie.zinc(E))
    assert e_zn < e_fe - 0.3 and ie.iron(e_zn) < 1e-3      # iron protected by zinc
    e_cu, i_cu = ie.corrosion_point(ie.iron, plateau=2.0)
    assert e_cu > e_fe and abs(i_cu - 2.0) < 0.02          # copper doubles the cathode


def test_passive_curve():
    peak = max(ie.passive(E / 1000) for E in range(-500, 0))
    plateau = ie.passive(0.5)
    assert peak > 20 * plateau and ie.passive(1.4) > plateau

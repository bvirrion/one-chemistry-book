import importlib.util
import os

spec = importlib.util.spec_from_file_location("vb", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "vacuum-boiling.py"))
vb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vb)
from _ledger import value  # noqa: E402  (path set up by the module)


def test_passes_through_normal_boiling_point():
    assert abs(vb.t_boil("bromobenzene", 1.01325) - value("tb:bromobenzene")) < 1e-9
    assert abs(vb.t_boil("benzaldehyde", 1.00) - value("tb:benzaldehyde")) < 1e-9


def test_against_measured_reduced_pressure_points():
    # WebBook reduced-pressure boiling points, not used in the fit
    assert abs(vb.t_boil("bromobenzene", 0.007) - value("tbp:bromobenzene.7mbar")) < 3
    assert abs(vb.t_boil("benzaldehyde", 0.013) - value("tbp:benzaldehyde.13mbar")) < 4


def test_monotonic():
    ts = [vb.t_boil("bromobenzene", p) for p in (0.01, 0.1, 1.0)]
    assert ts[0] < ts[1] < ts[2]

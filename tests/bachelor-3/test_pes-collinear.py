import importlib.util
import os

import numpy as np

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("pes", os.path.join(D, "pes-collinear.py"))
pes = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pes)


def test_asymptote_is_the_h2_morse_curve():
    r = np.linspace(0.5, 2.5, 21)
    far = pes.leps(r, np.full_like(r, 12.0))
    assert np.allclose(far, pes.singlet(r), atol=1e-6)
    assert abs(pes.singlet(pes.RE) + pes.DE) < 1e-12
    assert abs(pes.DE - 4.747) < 0.002            # D0 + G(0) of H2


def test_symmetric_saddle_and_barrier():
    rs, es = pes.saddle()
    assert abs(pes.leps(rs + 0.1, rs) - pes.leps(rs, rs + 0.1)) < 1e-12
    gx, gy = pes.grad(rs, rs)
    assert abs(gx) < 1e-3 and abs(gy) < 1e-3
    barrier = es + pes.DE
    assert 0 < barrier < 1.0 and rs > pes.RE
    # a maximum along the antisymmetric direction, a minimum along the symmetric one
    assert pes.leps(rs + 0.05, rs - 0.05) < es < pes.leps(rs + 0.05, rs + 0.05)


def test_mep_joins_the_valleys():
    path = pes.mep()
    (x0, y0), (x1, y1) = path[0], path[-1]
    assert abs(min(x0, y0) - pes.RE) < 0.01 and abs(min(x1, y1) - pes.RE) < 0.01
    assert max(x0, y0) > 2.9 and max(x1, y1) > 2.9

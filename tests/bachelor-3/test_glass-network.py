import importlib.util
import os
from collections import Counter

import numpy as np

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("gn", os.path.join(D, "glass-network.py"))
gn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gn)


def test_crystal_is_a_honeycomb():
    (pos, bonds), _ = gn.build()
    assert set(Counter(gn.rings(pos, bonds))) == {6}


def test_glass_rings_and_coordination():
    (cpos, cb), (pos, bonds, broken) = gn.build()
    c = Counter(gn.rings(pos, bonds))
    assert c[5] == 2 * len(gn.SW_BONDS) and c[7] == 2 * len(gn.SW_BONDS)
    # formers keep three neighbours, counting a broken bond as a non-bridging O
    nb = gn.neighbours(bonds, len(pos))
    cnb = gn.neighbours(cb, len(cpos))
    ends = Counter(k for b in broken for k in b)
    for v in range(len(pos)):
        if len(cnb[v]) == 3:
            assert len(nb[v]) + ends[v] == 3


def test_bond_lengths_close_to_d():
    _, (pos, bonds, broken) = gn.build()
    lengths = [np.linalg.norm(pos[i] - pos[j]) for i, j in bonds]
    assert 0.85 < min(lengths) and max(lengths) < 1.15
    for i, j in broken:
        assert np.linalg.norm(pos[i] - pos[j]) > 1.3

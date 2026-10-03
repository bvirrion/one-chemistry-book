"""Distribution of copper(II) and silver(I) among their ammine complexes
against pNH3 = -log[NH3] (ch. 12). Overall formation constants computed from
NBS-82 Gibbs energies in aqueous-constants.py."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "aqc", os.path.join(os.path.dirname(__file__), "aqueous-constants.py"))
aqc = importlib.util.module_from_spec(_spec)
aqc.__spec__ = _spec
_spec.loader.exec_module(aqc)


def log_betas(metal):
    if metal == "Cu":
        return [0.0] + [aqc.logb("CuNH3_%d" % n) for n in (1, 2, 3, 4)]
    return [0.0, aqc.logb("AgNH3"), aqc.logb("AgNH32")]


def successive(metal):
    """log K_i = log beta_i - log beta_(i-1)."""
    b = log_betas(metal)
    return [b[i] - b[i - 1] for i in range(1, len(b))]


def fractions(metal, pl):
    terms = [10 ** (lb - n * pl) for n, lb in enumerate(log_betas(metal))]
    s = sum(terms)
    return [t / s for t in terms]


if __name__ == "__main__":
    rows = [(x / 20,) + tuple(fractions("Cu", x / 20)) for x in range(0, 141)]
    write_table(__file__, ("pL", "M", "ML", "ML2", "ML3", "ML4"), rows, part="copper")
    rows = [(x / 20,) + tuple(fractions("Ag", x / 20)) for x in range(0, 141)]
    write_table(__file__, ("pL", "M", "ML", "ML2"), rows, part="silver")

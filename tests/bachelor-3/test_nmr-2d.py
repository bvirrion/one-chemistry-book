import importlib.util
import os

spec = importlib.util.spec_from_file_location("n2", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3", "nmr-2d.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_cosy_only_vicinal_and_symmetric():
    pairs = set(m.cosy_pairs())
    assert pairs == {("e", "c"), ("c", "e"), ("c", "b"), ("b", "c"), ("a", "d"), ("d", "a")}
    assert ("b", "a") not in pairs        # the ester oxygen breaks the coupling path


def test_hsqc_and_hmbc():
    assert len(m.hsqc_pairs()) == 5
    assert ("a", "CO") in m.hmbc_pairs() and ("b", "CO") in m.hmbc_pairs()
    assert ("e", "CO") not in m.hmbc_pairs()

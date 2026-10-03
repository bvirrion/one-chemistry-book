import importlib.util
import os

spec = importlib.util.spec_from_file_location("ap", os.path.join(
    os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2", "aromatic-profile.py"))
ap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ap)


def test_shapes():
    xs = [k * 0.01 for k in range(0, 401)]
    sub = [ap.substitution(x) for x in xs]
    add = [ap.addition(x) for x in xs]
    # first barrier is the highest point of the substitution profile
    assert max(sub) == max(sub[:200])
    # substitution product lies below the reactants, addition product above
    assert sub[-1] < sub[0] < add[-1]
    # an intermediate (a local minimum) exists near x = 2
    i = 200
    assert sub[i] < sub[100] and sub[i] < max(sub[250:350])

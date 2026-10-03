import importlib.util
import os

D = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3")
spec = importlib.util.spec_from_file_location("hn", os.path.join(D, "heterocycle-nmr.py"))
hn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hn)


def test_peak_positions():
    xs = hn.grid()
    for name in ("pyridine", "furan"):
        ys = [hn.spectrum(name, x) for x in xs]
        peaks = [xs[i] for i in range(1, len(xs) - 1) if ys[i] > ys[i - 1] and ys[i] > ys[i + 1]]
        assert sorted(round(p, 2) for p in peaks) == sorted(round(d, 2) for d, _, _ in hn.lines(name))


def test_integrals_are_proton_counts():
    a = hn.integrals("pyridine")
    r = [x / a[1] for x in a]   # relative to H4 (one proton)
    assert all(abs(x - y) < 0.07 * y for x, y in zip(r, (2, 1, 2)))  # Lorentzian tails outside the windows
    f = hn.integrals("furan")
    assert abs(f[0] / f[1] - 1) < 0.02

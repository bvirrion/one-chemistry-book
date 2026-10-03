"""Fixed-step fourth-order Runge-Kutta integration (Book 4 kinetics figures)."""


def rk4(f, y0, t0, t1, dt, every=1):
    """integrate y' = f(t, y) (y a list of floats); return the list of
    (t, y) kept every `every` steps, the first and last included"""
    y = list(y0)
    t = t0
    out = [(t, list(y))]
    n = int(round((t1 - t0) / dt))
    for i in range(1, n + 1):
        k1 = f(t, y)
        k2 = f(t + dt / 2, [a + dt / 2 * b for a, b in zip(y, k1)])
        k3 = f(t + dt / 2, [a + dt / 2 * b for a, b in zip(y, k2)])
        k4 = f(t + dt, [a + dt * b for a, b in zip(y, k3)])
        y = [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(y, k1, k2, k3, k4)]
        t = t0 + i * dt
        if i % every == 0 or i == n:
            out.append((t, list(y)))
    return out

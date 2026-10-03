"""Molar-mass distributions of polymers (chapter 29). Models, no measured data.
- a: Flory most-probable distribution, mass fraction w(x) = x (1-p)^2 p^(x-1)
     of x-mers, for p = 0.95, 0.98, 0.99 (x = 1..600);
- b: Carothers equation, X_n = 1/(1-p), for p from 0 to 0.995;
- c: mass fractions at the same X_n = 50: Flory (p = 1 - 1/X_n) and Poisson
     (living polymerisation, nu = X_n - 1 additions per chain:
     n(x) = e^-nu nu^(x-1)/(x-1)!), x = 1..150."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table

PS = (0.95, 0.98, 0.99)


def flory_number(x, p):
    return (1 - p) * p ** (x - 1)


def flory_mass(x, p):
    return x * (1 - p) ** 2 * p ** (x - 1)


def carothers(p):
    return 1 / (1 - p)


def imbalance(p, r):
    return (1 + r) / (1 + r - 2 * r * p)


def poisson_number(x, nu):
    k = x - 1
    return math.exp(-nu + k * math.log(nu) - math.lgamma(k + 1))


def averages(numbers):
    """(X_n, X_w) from a list of (x, number fraction)."""
    s0 = sum(n for _, n in numbers)
    s1 = sum(x * n for x, n in numbers)
    s2 = sum(x * x * n for x, n in numbers)
    return s1 / s0, s2 / s1


def mass_fractions(numbers):
    xn = sum(x * n for x, n in numbers) / sum(n for _, n in numbers)
    return [(x, x * n / xn) for x, n in numbers]


if __name__ == "__main__":
    xs = list(range(1, 601))
    rows = [(x,) + tuple(flory_mass(x, p) for p in PS) for x in xs]
    write_table(__file__, ("x", "p95", "p98", "p99"), rows, part="a")
    ps = [i / 1000 for i in range(0, 996, 5)]
    write_table(__file__, ("p", "Xn"), [(p, carothers(p)) for p in ps], part="b")
    xn = 50
    xs = list(range(1, 151))
    fl = mass_fractions([(x, flory_number(x, 1 - 1 / xn)) for x in xs])
    po = mass_fractions([(x, poisson_number(x, xn - 1)) for x in xs])
    write_table(__file__, ("x", "flory", "poisson"), [(x, a[1], b[1]) for x, a, b in zip(xs, fl, po)],
                part="c")

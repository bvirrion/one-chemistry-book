"""Chapter 5 (continuous reactors), all with model parameters (no data about a
real substance):
  part a: conversion of a first-order reaction against the Damkohler number
          Da = k tau, in one stirred tank, in 2 and 5 equal tanks in series
          and in a plug-flow reactor;
  part b: Semenov diagram of an adiabatic-with-cooling stirred tank: heat
          generated (S-shaped, in kelvin of adiabatic rise) and heat removed
          (straight line) against the tank temperature, with three steady
          states;
  part c: Levenspiel chart 1/r against X for a first-order reaction: the
          area under the curve is the plug-flow tau, the rectangle the
          stirred-tank tau."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402


def x_cstr(da):
    return da / (1.0 + da)


def x_pfr(da):
    return 1.0 - math.exp(-da)


def x_cascade(da, n):
    """n equal tanks, total Damkohler number da."""
    return 1.0 - (1.0 + da / n) ** (-n)


def x_cstr_second_order(da):
    """Order 2, equal feed concentrations, Da = k c0 tau:
    Da (1-X)^2 = X."""
    if da == 0:
        return 0.0
    return ((2 * da + 1) - math.sqrt(4 * da + 1)) / (2 * da)


# Semenov diagram (model)
T_IN = 300.0       # K, feed and coolant
DT_AD = 200.0      # K, adiabatic rise for full conversion
E_R = 12000.0      # K, activation temperature Ea/R
DA_IN = 2.0e-4     # Damkohler number at T_IN
KAPPA = 0.5        # UA/(F cp): cooling relative to the flow's heat capacity


def da(T):
    return DA_IN * math.exp(E_R * (1.0 / T_IN - 1.0 / T))


def generated(T):
    """Heat generated per unit flow heat capacity, K: DT_AD X(T)."""
    return DT_AD * x_cstr(da(T))


def removed(T):
    """Heat removed by the outflow and the cooling, K: (1 + kappa)(T - T_IN)."""
    return (1.0 + KAPPA) * (T - T_IN)


def steady_states(lo=300.0, hi=520.0, n=22000):
    roots = []
    prev = generated(lo) - removed(lo)
    for k in range(1, n + 1):
        T = lo + (hi - lo) * k / n
        cur = generated(T) - removed(T)
        if prev == 0 or prev * cur < 0:
            a, b = T - (hi - lo) / n, T
            for _ in range(60):
                m = 0.5 * (a + b)
                if (generated(a) - removed(a)) * (generated(m) - removed(m)) <= 0:
                    b = m
                else:
                    a = m
            roots.append(0.5 * (a + b))
        prev = cur
    return roots


def levenspiel(k=1.0, c0=1.0, xmax=0.95, n=96):
    """1/r = 1/(k c0 (1 - X)) for a first-order reaction."""
    return [(xmax * i / n, 1.0 / (k * c0 * (1 - xmax * i / n))) for i in range(n + 1)]


def tau_pfr(X, k=1.0):
    return -math.log(1 - X) / k


def tau_cstr(X, k=1.0):
    return X / (k * (1 - X))


if __name__ == "__main__":
    rows = []
    for i in range(0, 201):
        d = 10.0 * i / 200
        rows.append((d, x_cstr(d), x_cascade(d, 2), x_cascade(d, 5), x_pfr(d)))
    write_table(__file__, ("Da", "cstr", "two", "five", "pfr"), rows, part="a")
    rows = [(T, generated(T), removed(T)) for T in [300.0 + 1.0 * i for i in range(0, 221)]]
    write_table(__file__, ("T", "gen", "rem"), rows, part="b")
    write_table(__file__, ("X", "invr"), levenspiel(), part="c")

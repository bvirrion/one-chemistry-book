"""Ch. 30, overall yield. A linear route of n steps of yield y gives y^n; a
convergent route with the same total number of steps n = 2m + 1, made of two
branches of m steps joined by one coupling step, gives y^(m + 1) along its
longest linear sequence (each branch is run on enough material). Part a:
linear overall yield against n for y = 0.80, 0.90, 0.95; part b: convergent
for the same y and odd n."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

YS = (0.80, 0.90, 0.95)


def linear(y, n):
    return y ** n


def convergent(y, n):
    m = (n - 1) // 2
    return y ** (m + 1)


if __name__ == "__main__":
    write_table(__file__, ("n",) + tuple("y%d" % int(100 * y) for y in YS),
                [(n,) + tuple(linear(y, n) for y in YS) for n in range(0, 31)])
    write_table(__file__, ("n",) + tuple("y%d" % int(100 * y) for y in YS),
                [(n,) + tuple(convergent(y, n) for y in YS) for n in range(1, 31, 2)], part="b")
    print(linear(0.9, 21), convergent(0.9, 21), linear(0.75, 14))

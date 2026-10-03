"""Ch. 21, the molar-mass distribution of a polymer made on a single-site
catalyst with a constant probability p that a growing chain adds one more
monomer rather than being transferred (Schulz-Flory, most probable
distribution): number fraction x_n = (1 - p) p^(n-1), mass fraction
w_n = n (1 - p)^2 p^(n-1). Here p = 0.999 (mean degree of polymerisation
1000, model); monomer ethene, 28.05 g/mol."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402

P = 0.999
M0 = 28.05


def xn(n, p=P):
    return (1 - p) * p ** (n - 1)


def wn(n, p=P):
    return n * (1 - p) ** 2 * p ** (n - 1)


def moments(p=P, nmax=40000):
    mn_num = sum(n * xn(n, p) for n in range(1, nmax))
    mw_num = sum(n * wn(n, p) for n in range(1, nmax))
    return mn_num, mw_num, mw_num / mn_num


if __name__ == "__main__":
    write_table(__file__, ("M_kg", "x", "w"),
                [(n * M0 / 1000, 1000 * xn(n), 1000 * wn(n)) for n in range(1, 8001, 40)])
    print(moments())

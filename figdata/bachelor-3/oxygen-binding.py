"""Ch. 24, oxygen binding. Saturation curves theta(p) of myoglobin (one site,
hyperbola, p50 = 0.37 kPa) and haemoglobin (Hill equation, n = 2.7,
p50 = 3.5 kPa at pH 7.4; 4.0 kPa at a lower pH, the Bohr shift): model values,
the data of the chapter's problem. Part b: the Hill plot
log10(theta/(1 - theta)) against log10(p/kPa)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

P50_MB, P50_HB, P50_HB_ACID, N_HB = 0.37, 3.5, 4.0, 2.7


def hill(p, p50, n):
    return p ** n / (p50 ** n + p ** n)


def mb(p):
    return hill(p, P50_MB, 1.0)


def hb(p, p50=P50_HB):
    return hill(p, p50, N_HB)


if __name__ == "__main__":
    ps = [0.05 * k for k in range(0, 281)]
    write_table(__file__, ("p", "Mb", "Hb", "Hbacid"), [(p, mb(p), hb(p), hb(p, P50_HB_ACID)) for p in ps])
    rows = []
    for k in range(0, 61):
        lp = -1.5 + 0.05 * k
        p = 10 ** lp
        rows.append((lp, math.log10(mb(p) / (1 - mb(p))), math.log10(hb(p) / (1 - hb(p)))))
    write_table(__file__, ("lgp", "Mb", "Hb"), rows, part="b")
    print(hb(13), hb(5), hb(5, P50_HB_ACID), mb(5))

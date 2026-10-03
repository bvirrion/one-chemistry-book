"""Ch. 32, dose-response. Log-logistic model of the fraction of individuals
responding (or the effect, 0 to 1) at dose d: f = 1/(1 + (D50/d)^n), with
median dose D50 = 200 mg/kg and slopes n = 2 and 6 (model). Part b: the
model test doses (geometric series from 10 to 160 mg/kg) with the responses of
the n = 6 curve, used to read a NOAEL and a LOAEL with a 5 % effect criterion."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

D50 = 200.0
DOSES = (10, 20, 40, 80, 160)


def response(d, n, d50=D50):
    return 1 / (1 + (d50 / d) ** n) if d > 0 else 0.0


def noael_loael(n=6, crit=0.05):
    noael, loael = None, None
    for d in DOSES:
        if response(d, n) < crit:
            noael = d
        elif loael is None:
            loael = d
    return noael, loael


if __name__ == "__main__":
    ds = [10 ** (0.5 + 3.0 * j / 200) for j in range(201)]   # 3.2 to 3200 mg/kg
    write_table(__file__, ("d", "n2", "n6"), [(d, response(d, 2), response(d, 6)) for d in ds])
    write_table(__file__, ("d", "r"), [(d, response(d, 6)) for d in DOSES], part="b")
    print(noael_loael(), [round(response(d, 6), 4) for d in DOSES])

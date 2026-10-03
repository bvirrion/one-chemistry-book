"""Current-potential curves (chapter 10). MODEL curves: the values of the
diffusion coefficients, layer thickness and overpotentials are illustrative
(said in the captions), not data. Currents in units of the anodic limiting
current of a reference solution; anodic currents positive.
- a: fast couple, both forms at equal concentration (E0 = 0.77 V, n = 1);
- b: the same couple with the reduced form only;
- c: a slow couple (anodic and cathodic branches shifted by 0.35 V);
- d: water on two electrodes (cathodic wall near 0 V or near -0.8 V,
  anodic wall near +1.6 V), pH 0;
- e: limiting current against concentration (amperometric line);
- f: zinc in acid (chapter 11): oxidation of zinc (fast, no plateau, zinc
  ions dilute) and reduction of H+ on zinc (slow) or on copper (less slow):
  the mixed potentials;
- g: electrolysis of acidic zinc sulfate: Zn2+ deposition (fast, plateau)
  before H+ reduction on zinc, oxygen evolution at the anode;
- h: operating point of a cell: anodic curve of the negative electrode,
  cathodic curve of the positive one, at a current I;
- i: Evans diagram of iron in aerated neutral water: iron oxidation (fast)
  and the reduction of dissolved O2 (slow, diffusion-limited plateau);
- j: iron coupled to zinc (zinc oxidation added) and to copper (O2 plateau
  doubled by the copper area);
- k: active-passive-transpassive curve of a passivable metal (model)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
from _ledger import value  # noqa: E402

R = value("const:R")
F = value("const:F")
T = 298.15
F_RT = F / (R * T)


def fast_wave(E, E_half, i_la, i_lc, n=1):
    """Steady-state wave of a fast system (anodic limit i_la > 0, cathodic
    limit i_lc < 0): i = (i_lc + theta i_la)/(1 + theta), theta = exp(nF(E-E1/2)/RT)."""
    x = n * F_RT * (E - E_half)
    if x > 50:
        return i_la
    if x < -50:
        return i_lc
    th = math.exp(x)
    return (i_lc + th * i_la) / (1 + th)


def potential_of(i, E_half, i_la, i_lc, n=1):
    return E_half + math.log((i - i_lc) / (i_la - i)) / (n * F_RT)


def slow_wave(E, E0, i_la, i_lc, eta=0.35, alpha=0.5, n=1):
    """Model of a slow system: each branch is a fast-like wave displaced by an
    overpotential eta and broadened by a transfer coefficient alpha."""
    ia = i_la / (1 + math.exp(-alpha * n * F_RT * (E - E0 - eta)))
    ic = i_lc / (1 + math.exp(alpha * n * F_RT * (E - E0 + eta)))
    return ia + ic


def water(E, cath_wall, an_wall=1.6, k=0.12):
    """Water walls modelled as exponential rises (no plateau: the solvent is
    never exhausted), current in the same units, clipped for the plot."""
    i = 0.0
    if E > an_wall - 0.4:
        i += math.exp((E - an_wall) / k * 2.3) * 0.5
    if E < cath_wall + 0.4:
        i -= math.exp((cath_wall - E) / k * 2.3) * 0.5
    return max(-10.0, min(10.0, i))


def exp_branch(E, onset, b, sign, a=0.02, cap=10.0):
    """Exponential branch: anodic (sign +1) grows above onset, cathodic (-1)
    below it, with b volts per factor e."""
    x = sign * (E - onset) / b
    return sign * min(cap, a * math.exp(min(x, 50)))


ZN_ONSET, H_ON_ZN, H_ON_CU = -0.88, -0.70, -0.45


def mixed_potential(cath_onset, zn_onset=ZN_ONSET, ba=0.03, bc=0.06):
    """Potential where the zinc anodic current equals minus the H+ cathodic
    current, and that current."""
    E = solve_root(lambda E: exp_branch(E, zn_onset, ba, 1) + exp_branch(E, cath_onset, bc, -1),
                   zn_onset - 0.3, cath_onset + 0.3)
    return E, exp_branch(E, zn_onset, ba, 1)


def solve_root(f, lo, hi):
    flo = f(lo)
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


FE_ONSET, ZN2_ONSET = -0.55, -0.95


def iron(E):
    return exp_branch(E, FE_ONSET, 0.04, 1)


def zinc(E):
    return exp_branch(E, ZN2_ONSET, 0.04, 1)


def oxygen(E, plateau=1.0, e_half=0.1, w=0.05):
    """Cathodic wave of dissolved O2: slow (its rise far below the Nernst
    potential of O2/H2O), then a diffusion plateau -plateau."""
    x = (E - e_half) / w
    return -plateau / (1 + math.exp(min(x, 50)))


def corrosion_point(anodic, plateau=1.0):
    E = solve_root(lambda E: anodic(E) + oxygen(E, plateau), -1.5, 0.5)
    return E, anodic(E)


def passive(E, e_act=-0.45, e_pass=-0.20, peak=1.0, ipass=0.03, e_tp=1.2):
    up = 1 / (1 + math.exp(-(E - e_act) / 0.03))
    down = 1 / (1 + math.exp((E - e_pass) / 0.025))
    return peak * up * down + ipass * up + min(5.0, 0.02 * math.exp(min((E - e_tp) / 0.05, 50)))


def grid(lo, hi, n=241):
    return [lo + (hi - lo) * k / (n - 1) for k in range(n)]


if __name__ == "__main__":
    E0 = 0.77
    write_table(__file__, ("E", "i"), [(E, fast_wave(E, E0, 1.0, -1.0)) for E in grid(0.3, 1.25)], part="a")
    write_table(__file__, ("E", "i"), [(E, fast_wave(E, E0, 1.0, 0.0)) for E in grid(0.3, 1.25)], part="b")
    write_table(__file__, ("E", "i"), [(E, slow_wave(E, E0, 1.0, -1.0)) for E in grid(-0.2, 1.75)], part="c")
    write_table(__file__, ("E", "i"), [(E, water(E, 0.0)) for E in grid(-1.2, 2.0, 321)], part="d-Pt")
    write_table(__file__, ("E", "i"), [(E, water(E, -0.8)) for E in grid(-1.2, 2.0, 321)], part="d-high")
    write_table(__file__, ("c", "i"), [(c / 10, c / 10) for c in range(0, 11)], part="e")
    G = grid(-1.1, -0.3, 321)
    write_table(__file__, ("E", "i"), [(E, exp_branch(E, ZN_ONSET, 0.03, 1)) for E in G], part="f-Zn")
    write_table(__file__, ("E", "i"), [(E, exp_branch(E, H_ON_ZN, 0.06, -1)) for E in G], part="f-HZn")
    write_table(__file__, ("E", "i"), [(E, exp_branch(E, H_ON_CU, 0.06, -1)) for E in G], part="f-HCu")
    G = grid(-1.6, 2.4, 401)
    write_table(__file__, ("E", "i"), [(E, fast_wave(E, -0.76, 0.0, -1.0, n=2) + exp_branch(E, -1.15, 0.05, -1, a=0.05))
                                       for E in G], part="g-cath")
    write_table(__file__, ("E", "i"), [(E, exp_branch(E, 1.8, 0.05, 1, a=0.05)) for E in G], part="g-an")
    G = grid(-1.2, 0.8, 321)
    write_table(__file__, ("E", "i"), [(E, exp_branch(E, -0.85, 0.04, 1, a=0.05)) for E in G], part="h-neg")
    write_table(__file__, ("E", "i"), [(E, exp_branch(E, 0.45, 0.08, -1, a=0.05)) for E in G], part="h-pos")
    G = grid(-1.1, 0.5, 321)
    write_table(__file__, ("E", "i"), [(E, iron(E)) for E in G], part="i-Fe")
    write_table(__file__, ("E", "i"), [(E, oxygen(E)) for E in G], part="i-O2")
    write_table(__file__, ("E", "i"), [(E, zinc(E)) for E in G], part="j-Zn")
    write_table(__file__, ("E", "i"), [(E, oxygen(E, 2.0)) for E in G], part="j-O2Cu")
    G = grid(-0.7, 1.5, 441)
    write_table(__file__, ("E", "i"), [(E, passive(E)) for E in G], part="k")

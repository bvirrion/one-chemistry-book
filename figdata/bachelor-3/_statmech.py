"""Statistical thermodynamics of ideal gases (Book 4, ch. 10-11): partition
functions and molar entropies of atoms and diatomic molecules from the ledger
constants. Conventions: rotational constant B0 = Be - alpha_e/2, vibrational
quantum G(1) - G(0) = omega_e - 2 omega_e x_e (when x_e is known), standard
pressure 1 bar, nuclear spin and isotope mixing left out (the convention of
the thermodynamic tables)."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _ledger import value  # noqa: E402

H = value("const:h")
C = value("const:c")
KB = value("const:kB")
NA = value("const:NA")
R = value("const:R")
U = value("const:u")
P0 = value("const:pstd")

# molar masses (g/mol) from the standard atomic weights; spectroscopic
# constants of the main isotopologue; symmetry number
MOLECULES = {
    "N2": dict(mass=2 * value("aw:N"), key="N2", sigma=2, g0=1),
    "CO": dict(mass=value("aw:C") + value("aw:O"), key="CO", sigma=1, g0=1),
    "HCl": dict(mass=value("aw:H") + value("aw:Cl"), key="HCl", sigma=1, g0=1),
    "Cl2": dict(mass=2 * value("aw:Cl"), key="Cl2", sigma=2, g0=1),
    "I2": dict(mass=2 * value("aw:I"), key="I2", sigma=2, g0=1),
}
ATOMS = {"Ar": value("aw:Ar")}


def theta_rot(name):
    k = MOLECULES[name]["key"]
    b0 = value(f"diat:{k}.Be") - value(f"diat:{k}.ae") / 2
    return H * C * 100 * b0 / KB


def theta_vib(name):
    k = MOLECULES[name]["key"]
    return H * C * 100 * (value(f"diat:{k}.we") - 2 * value(f"diat:{k}.wexe")) / KB


def thermal_wavelength(mass_gmol, T):
    m = mass_gmol * 1e-3 / NA
    return H / math.sqrt(2 * math.pi * m * KB * T)


def q_trans_per_volume(mass_gmol, T):
    return thermal_wavelength(mass_gmol, T) ** -3


def q_rot_exact(theta, T, sigma=1, jmax=None):
    """Rigid-rotor sum; for a homonuclear molecule (sigma = 2) the even- and
    odd-J sums are averaged, which is the high-temperature nuclear-spin
    average divided out"""
    jmax = jmax or int(30 * math.sqrt(T / theta)) + 30
    s = sum((2 * j + 1) * math.exp(-theta * j * (j + 1) / T) for j in range(jmax + 1))
    return s / sigma


def q_rot_high(theta, T, sigma=1):
    return T / (sigma * theta)


def q_vib(theta, T):
    """levels measured from the zero-point level"""
    return 1 / (1 - math.exp(-theta / T))


def populations_rot(theta, T, jmax):
    q = q_rot_exact(theta, T)
    return [(2 * j + 1) * math.exp(-theta * j * (j + 1) / T) / q for j in range(jmax + 1)]


def j_most(theta, T):
    return math.sqrt(T / (2 * theta)) - 0.5


def populations_vib(theta, T, vmax):
    x = theta / T
    return [(1 - math.exp(-x)) * math.exp(-v * x) for v in range(vmax + 1)]


def s_trans(mass_gmol, T=298.15, p=None):
    p = p or P0
    lam = thermal_wavelength(mass_gmol, T)
    return R * (math.log(KB * T / (p * lam ** 3)) + 2.5)


def s_rot(theta, T=298.15, sigma=1):
    return R * (math.log(T / (sigma * theta)) + 1)


def s_vib(theta, T=298.15):
    x = theta / T
    return R * (x / math.expm1(x) - math.log(-math.expm1(-x)))


def s_elec(levels, T=298.15):
    """levels: list of (g, energy in cm-1)"""
    xs = [(g, H * C * 100 * e / (KB * T)) for g, e in levels]
    q = sum(g * math.exp(-x) for g, x in xs)
    u = sum(g * x * math.exp(-x) for g, x in xs) / q
    return R * (math.log(q) + u)


def s_molecule(name, T=298.15):
    m = MOLECULES[name]
    parts = dict(trans=s_trans(m["mass"], T),
                 rot=s_rot(theta_rot(name), T, m["sigma"]),
                 vib=s_vib(theta_vib(name), T),
                 elec=R * math.log(m["g0"]))
    parts["total"] = sum(parts.values())
    return parts


# ---- ch. 11: heat capacities, nuclear-spin statistics, equilibrium constants

def einstein_cv(theta, T):
    """vibrational C_V / R of one harmonic mode"""
    x = theta / T
    return x * x * math.exp(-x) / (-math.expm1(-x)) ** 2


def rot_levels(key, jmax=40, distortion=False):
    """rotational term values F(J) in cm-1 of a diatomic, rigid rotor with B0;
    distortion=True adds the D_e term (known here for H2 only, used for the
    energy of J = 1, never in sums: it turns F(J) over near J = 25)"""
    b0 = value(f"diat:{key}.Be") - value(f"diat:{key}.ae") / 2
    d = value("diat:H2.De") if (key == "H2" and distortion) else 0.0
    return [b0 * j * (j + 1) - d * (j * (j + 1)) ** 2 for j in range(jmax + 1)]


def _moments(levels_cm, weights, T):
    """q, <e>/kT and C/R for a set of levels (cm-1) with weights"""
    c2 = H * C * 100 / KB
    xs = [c2 * e / T for e in levels_cm]
    w = [g * math.exp(-x) for g, x in zip(weights, xs)]
    q = sum(w)
    m1 = sum(wi * x for wi, x in zip(w, xs)) / q
    m2 = sum(wi * x * x for wi, x in zip(w, xs)) / q
    return q, m1, m2 - m1 * m1


# nuclear-spin weights of the even and odd rotational levels (homonuclear)
SPIN_WEIGHTS = {"H2": (1, 3), "D2": (6, 3)}


def q_rot_spin(key, T, parity=None, jmax=None):
    """rotational sum including nuclear-spin weights; parity 'even' or 'odd'
    restricts it to one spin isomer (rigid rotor)"""
    jmax = jmax or 40
    F = rot_levels(key, jmax)
    ge, go = SPIN_WEIGHTS[key]
    tot = 0.0
    for j, f in enumerate(F):
        if parity == "even" and j % 2:
            continue
        if parity == "odd" and not j % 2:
            continue
        g = (ge if j % 2 == 0 else go) * (2 * j + 1)
        tot += g * math.exp(-H * C * 100 * f / (KB * T))
    return tot


def para_fraction_h2(T):
    e = q_rot_spin("H2", T, "even")
    return e / (e + q_rot_spin("H2", T, "odd"))


def ortho_fraction_d2(T):
    e = q_rot_spin("D2", T, "even")
    return e / (e + q_rot_spin("D2", T, "odd"))


def cv_rot_h2(T, mode):
    """rotational C_V/R of H2: mode 'para', 'ortho', 'normal' (3:1 frozen) or
    'equilibrium' (spin isomers converting freely)"""
    F = rot_levels("H2", 40)
    js = range(len(F))
    if mode in ("para", "ortho"):
        sel = [j for j in js if (j % 2 == 0) == (mode == "para")]
        return _moments([F[j] - F[sel[0]] for j in sel], [2 * j + 1 for j in sel], T)[2]
    if mode == "normal":
        return 0.25 * cv_rot_h2(T, "para") + 0.75 * cv_rot_h2(T, "ortho")
    return _moments(F, [(1 if j % 2 == 0 else 3) * (2 * j + 1) for j in js], T)[2]


def theta_vib_key(key):
    return H * C * 100 * (value(f"diat:{key}.we") - 2 * value(f"diat:{key}.wexe")) / KB


def cv_diatomic(name, T):
    """C_V,m/R of a heavy diatomic (classical rotation) with a harmonic vibration"""
    return 2.5 + einstein_cv(theta_vib(name), T)


def cv_h2(T, mode):
    return 1.5 + cv_rot_h2(T, mode) + einstein_cv(theta_vib_key("H2"), T)


def zpe(key):
    """zero-point energy in cm-1, G(0) = omega_e/2 - omega_e x_e/4"""
    return value(f"diat:{key}.we") / 2 - value(f"diat:{key}.wexe") / 4


MASS_ISO = {"H2": 2 * value("imass:H1"), "D2": 2 * value("imass:H2"),
            "HD": value("imass:H1") + value("imass:H2")}


def q_std_per_NA(mass_gmol, T, q_int):
    """standard molar partition function divided by N_A: (kT/p)/Lambda^3 x q_int"""
    return KB * T / P0 / thermal_wavelength(mass_gmol, T) ** 3 * q_int


def q_int_hydrogen(key, T):
    """internal partition function of H2, D2 or HD with the nuclear-spin states
    divided out (so that the spin factors cancel in K); vibration harmonic
    with the fundamental, from the zero-point level"""
    if key == "HD":
        F = rot_levels("HD", 40)
        qr = sum((2 * j + 1) * math.exp(-H * C * 100 * f / (KB * T)) for j, f in enumerate(F))
    else:
        nspin = {"H2": 4, "D2": 9}[key]
        qr = q_rot_spin(key, T) / nspin
    return qr * q_vib(theta_vib_key(key), T)


def k_hd(T):
    """K of H2 + D2 = 2 HD"""
    q = {k: q_std_per_NA(MASS_ISO[k], T, q_int_hydrogen(k, T)) for k in ("H2", "D2", "HD")}
    de0 = (2 * zpe("HD") - zpe("H2") - zpe("D2")) * H * C * 100 / KB   # in K
    return q["HD"] ** 2 / (q["H2"] * q["D2"]) * math.exp(-de0 / T)


def d0_i2():
    """dissociation energy of I2 at 0 K, kJ/mol, from JANAF 0 K formation enthalpies"""
    return 2 * value("janaf:I.dfH0") - value("janaf:I2g.dfH0")


def k_i2(T):
    """K of I2(g) = 2 I(g), standard state 1 bar"""
    m_i = value("aw:I")
    x = H * C * 100 * value("lev:I.2P1_2") / (KB * T)
    q_i = q_std_per_NA(m_i, T, 4 + 2 * math.exp(-x))
    q_i2 = q_std_per_NA(2 * m_i, T, T / (2 * theta_rot("I2")) * q_vib(theta_vib("I2"), T))
    return q_i ** 2 / q_i2 * math.exp(-d0_i2() * 1000 / (R * T))


def ortho_para_energy():
    """energy of H2 J = 1 above J = 0 (cm-1), with the distortion term"""
    F = rot_levels("H2", 1, distortion=True)
    return F[1] - F[0]

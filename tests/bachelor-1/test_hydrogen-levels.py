import importlib.util
import os

HERE = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location(
    "hl", os.path.join(HERE, "..", "..", "figdata", "bachelor-1", "hydrogen-levels.py"))
hl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hl)


def test_ground_level():
    # -13.598 eV, the measured ionisation energy (ledger ie:H)
    assert abs(hl.level_ev(1) - (-hl.value("ie:H"))) < 0.002


def test_balmer_lines_match_nist():
    # computed vacuum wavelengths vs observed (air) values: within 0.05 %
    for n, key in ((3, "asd:Halpha"), (4, "asd:Hbeta"), (5, "asd:Hgamma"), (6, "asd:Hdelta")):
        obs = hl.value(key)
        calc = hl.wavelength_nm(2, n)
        assert abs(calc - obs) / obs < 5e-4
        assert calc > obs  # air shortens wavelengths


def test_printed_values():
    assert round(hl.level_ev(1), 2) == -13.60
    assert round(hl.level_ev(2), 2) == -3.40
    assert round(hl.wavelength_nm(2, 3), 1) == 656.5
    assert round(hl.series_limit_nm(2), 1) == 364.7
    assert round(hl.series_limit_nm(1), 1) == 91.2

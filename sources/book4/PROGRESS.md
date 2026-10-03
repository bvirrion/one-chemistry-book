# Book 4 (University Chemistry, Year 3) — progress

Resume file: a fresh agent must be able to continue the book from this file
alone, with `sources/BATCH_BOOKS_1-4.md` (binding rules — read it first,
including every "Sync decisions" entry), `BRIEFS.md` (per-chapter plan, with
the table of debts Books 2–3 left to "the Year 3 volume") and
`DEFINITIONS.md` (678 terms in 359 labels) beside it.

## State

- **Book 4 COMPLETE 2026-10-03: Phases B, C and D done.** 33 chapters written,
  405 pp, 0/0/0, gates green, 188 tests pass, figdata deterministic, 1,632 term
  links (dry run 0, --check clean), full per-figure re-check at 72 dpi done
  (defects fixed: see FIGCHECK 'Phase C'). Report sent to the coordinator.
- **Phase A done 2026-10-02; Sync S3 received; Phase B done** (write
  in outline order, full chapter cycle). S3: map granted; style block "Book 4
  sync" added by the main session (`omchartable`, `\termsym`, `\kv`,
  `\hartree`, `\bohr`, Jablonski styles, `omfishhook`, `ompath`,
  `omsaddle`, `omts`, `ompes`, `omcv`, `omscan`, braces). Book 4 appended
  its own block `% Book 4 (shared pics):` (crystallographic glyphs and
  stereograms; tested on a scratch page). Book 3 builds `omp` (signed
  coefficient + rotation), `omdxz/omdyz`, `omcorrforbidden`, `omsymlabel`,
  `omlevel` length: grep before ch5/ch7/ch26; if missing, build under that
  name in the Book 4 block and tell the main session.
- Scratch helpers (not in the repo, recreate if lost): `fig.sh` / `figc.py`
  (find a caption with pdftotext -bbox, render a crop at 130 dpi),
  `data/diat.py` (WebBook diatomic constants), `data/asd.sh` (NIST ASD level
  CSV, format=3 with all columns), `data/commons.py` (licence check),
  `prog.py` (tick a chapter row here), `ai/batchA.txt` (AI prompts).
- Entry `one_chemistry_book_4_university_year_3.tex` builds **0 errors / 0
  undefined / 0 overfull, 44 pp** (33 placeholders + frontmatter), checked
  2026-10-02 under `nice -n 10` and a cgroup scope.
- Nothing written in `parts/bachelor-3/` yet (placeholders untouched);
  ledger `sources/ledger/book4.md` empty; `figdata/bachelor-3/`,
  `tests/bachelor-3/` do not exist yet; `images/book4/` holds only the
  scaffold's `CREDITS.md` and `ai/PROMPTS.md`; the credits page
  `frontmatter/image-credits-book4.tex` is the scaffold's;
  `tools/term_config/book4_en.py` is the empty placeholder.
- No file outside Book 4's own was edited. `styles/onechemistry.sty` was not
  touched (needs listed below, for the sync).

## Chapter status

| ch | slug | ledger | text | exos/pb | solutions | figures | build+gates | FIGCHECK |
|---|---|---|---|---|---|---|---|---|
| 1 | quantum-model-systems | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2 | many-electron-atoms | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 3 | computational-chemistry | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 4 | point-groups | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 5 | group-theory-applied | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 6 | rovibrational-spectroscopy | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 7 | electronic-spectroscopy | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 8 | advanced-nmr | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 9 | x-ray-diffraction | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 10 | partition-functions | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 11 | statistical-thermo-applied | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 12 | rate-theories | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 13 | complex-kinetics | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 14 | photochemistry | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 15 | electrode-kinetics | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 16 | surfaces-catalysis | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17 | colloids | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 18 | complex-spectra-magnetism | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 19 | complex-mechanisms | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 20 | organometallic-bonding | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 21 | homogeneous-catalysis | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 22 | solid-state | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 23 | inorganic-materials | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 24 | bioinorganic | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 25 | supramolecular | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 26 | pericyclic | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 27 | radicals-carbenes | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 28 | asymmetric-synthesis | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 29 | heterocycles | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 30 | total-synthesis | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 31 | green-industrial | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 32 | environmental-toxicology | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 33 | lab-techniques-3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

Legend: – not started, ✓ done; build+gates means `latexmk` 0/0/0 and
`bash tools/gates.sh bachelor-3` green after that chapter.

## Page projection

Target ~380 pp. Plan per chapter: ~9.5 body pp (≈ 650–700 source lines)
+ ~1.9 solution pp (≈ 130 lines) ≈ 11.4 pp → 33 × 11.4 ≈ 376 pp + ~10 pp
frontmatter + ~10 pp index ≈ 396 pp if achieved. Books 1–3 all landed
13–14 % short (Book 2: 7.6 + 1.6 pp per chapter); the plan therefore aims
above target. Checkpoints after ch. 10, 20 and 33: measured pp per chapter;
> 15 % under (i.e. < 323 pp projected) ⇒ restore depth before going on.

| checkpoint | chapters done | pages | pp/ch | projection | verdict |
|---|---|---|---|---|---|
| Phase A | 0 | 44 (stubs) | – | ~380–396 | – |
| ch. 10 | 10 | 153 (23 stubs left) | 10.9 net (153 − 44)/10 | 44 + 33 × 10.9 ≈ 404 | on track (> 323); keep depth, no padding |
| ch. 20 | 20 | 268 (13 stubs left) | 11.2 net (268 − 44)/20 | 44 + 33 × 11.2 ≈ 414 | on track (> 323); about 9 % above the 380 target, acceptable |
| ch. 30 | 30 | 374 (3 stubs left) | 11.0 net (374 − 44)/30; ch21–30 10.6 | 374 + 3 × 10.6 ≈ 406 | on track (> 323); about 7 % above the 380 target, acceptable |

## Budgets and counts

- **Web searches (WebSearch tool): 0 used.** Estimate for the book: **~350**
  (of the ~600 per-book plan). Reachability probes and Commons queries are
  done with curl (not web searches): 2026-10-02, ~30 curl requests.
- Reachable (curl ✓): Basis Set Exchange API (STO-3G exponents verified),
  CCCBDB, NIST WebBook (diatomic constants of HCl), NIST ASD, COD CSV,
  NMRShiftDB, NIST kinetics, IUPAC atmospheric kinetics (aeris), PubChem
  PUG REST, ChEBI, RCSB PDB, Gernot Katzer's character tables, Symmetry@
  Otterbein, webqc, Nobel site (to check), EPA CompTox (not needed).
  **Unreachable from this machine:** Bilbao Crystallographic Server, JPL
  data evaluation, ioffe.ru, IUPAC Gold Book and PAC (403). Commons API
  search throttled after ~10 queries (wait and retry with a pause).
- AI images: 0 (plan ~20 in 4 batches). Photographs: 0 (plan ~22).
- Ledger rows: 0 (plan ~400).
- figdata scripts: 0 (plan ~60 + 1 test-only check; list below).

## figdata plan (`figdata/bachelor-3/<name>.py` + `tests/bachelor-3/test_<name>.py`)

Helpers (underscore, skipped by `make figdata`): `_ledger.py` (copy of Book
2's reader, reading every ledger by id), `_qm.py` (s-type Gaussian
integrals: overlap, kinetic, nuclear attraction with the Boys function
F₀ via `math.erf`, two-electron (ss|ss); used by `minimal-basis-hf`),
`_ode.py` (fixed-step RK4 for the kinetics scripts). numpy + standard
library only (no scipy in the venv); every script single-threaded,
seconds of CPU.

| ch | script | computes | test asserts (defining points) |
|---|---|---|---|
| 1 | `particle-in-box` | ψₙ, Eₙ for n = 1–4; λ of three cyanine dyes (free-electron model) | Eₙ ∝ n² (E₂/E₁ = 4); n − 1 nodes; ∫ψ² = 1, ⟨ψ₁|ψ₂⟩ = 0 (numerical); λ = 8mcL²/h(N+1) |
| 1 | `harmonic-oscillator` | Hermite functions ψ₀–ψ₃, levels, turning points | spacing ħω; E₀ = ½ħω; normalisation; ψ₀ zero-free, ψ₁ odd; turning points at ±√((2v+1)ħ/mω) |
| 1 | `tunnelling` | exact transmission through a rectangular barrier for H and D | T ≤ 1; thick-barrier limit 16ε(1−ε)e^{−2κa}; T(H)/T(D) > 1 and → ratio of exponentials |
| 2 | `atomic-levels` | level diagrams of C 2p², He 1s2s/1s2p, Na 3p from `lev:` rows | positions equal ledger energies; Landé ratio E(³P₂)−E(³P₁) : E(³P₁)−E(³P₀) ≈ 2:1 within the data; K = ½[E(¹S) − E(³S)] |
| 3 | `minimal-basis-hf` | RHF/STO-3G of H₂ (curve vs R) and HeH⁺ (SCF iterations), STO-nG fits | E(H₂, R = 1.4 a₀) = −1.1167 Eₕ and S₁₂ = 0.6593 (classic minimal-basis benchmark, ζ_H = 1.24, tol 1e-4); E(HeH⁺, 1.4632 a₀) = −2.8607 Eₕ with the benchmark's ζ_He = 2.0925 (tol 1e-4) — the book prints the standard STO-3G (ζ_He = 1.69, BSE) value, checked against CCCBDB if listed; SCF converges; STO-3G overlap with the 1s STO > 0.99; RHF H₂ at large R above 2E(H) |
| 4 | (test only) `test_character-tables` | parses every character table printed in ch4/ch5 | rows orthogonal, Σ gᶜχᵢχⱼ = hδᵢⱼ; Σd² = h; number of irreps = number of classes |
| 5 | `reduction` | Γ₃ₙ and its reduction for H₂O, NH₃, CH₄, CO₂ (D₂ₕ), BF₃, XeF₄, SF₆; IR/Raman counts | H₂O Γ_vib = 2A₁ + B₂; NH₃ 2A₁ + 2E; CH₄ A₁ + E + 2T₂; 3N − 6 / 3N − 5 modes; SF₆ IR = 2 T₁ᵤ |
| 5 | `co2-spectra` | synthetic IR and Raman spectra of CO₂ at ledger bands | IR maxima at ν₂, ν₃ only (no band at ν₁); Raman at the Fermi dyad |
| 6 | `rotational-spectrum` | CO lines at 30 and 300 K; N₂ rotational Raman | spacing 2B; J_max formula; Raman spacing 4B, first line 6B; ortho/para alternation 2:1 |
| 6 | `morse-levels` | Morse and harmonic HCl curves, levels, Birge–Sponer | G(v) formula; Dₑ = ωₑ²/4ωₑxₑ; D₀ = Dₑ − G(0); number of bound levels |
| 6 | `rovib-band` | H³⁵Cl/H³⁷Cl fundamental with P/R branches | gap at the band origin (no Q); combination differences recover B₀, B₁; isotope shift from reduced masses |
| 7 | `franck-condon` | displaced-oscillator Franck–Condon factors (Poisson) | Σ FC = 1; maximum at n ≈ S; S = 0 gives a single 0–0 line |
| 7 | `photophysics` | mirror-image absorption/emission; decays with quencher; Stern–Volmer line | mirror symmetry about the 0–0 energy; τ = 1/(k_r + k_nr); slope = k_qτ₀ |
| 8 | `nmr-fid` | two-line FID and its Fourier transform | peaks at the offsets; FWHM = 1/(πT₂) |
| 8 | `nmr-relaxation` | inversion recovery, T₂ decay | M_z = 0 at T₁ ln 2; M_z(∞) = M₀ |
| 8 | `nmr-2d` | COSY and HSQC peak maps of the problem's ester | COSY cross peaks only between ³J-coupled protons, symmetric about the diagonal; HSQC peaks at bonded (δH, δC) pairs |
| 9 | `xrd-powder` | powder patterns (Cu Kα): NaCl, KCl, Cu, W; Scherrer broadening | 2θ from Bragg and ledger a; F-lattice and I-lattice absences; KCl odd lines ≈ 0 with f(K⁺) = f(Cl⁻); FWHM = Kλ/(L cos θ) |
| 10 | `boltzmann-populations` | rotational/vibrational populations of HCl, N₂, I₂ at three T | Σ = 1; J_max; n_J/n₀ formula |
| 10 | `partition-functions` | q_rot exact vs high-T, q_vib vs T | q_rot → T/σθ_r; q_vib → 1 (low T), → T/θ_v (high T) |
| 10 | `sackur-tetrode` | statistical S° of Ar, N₂, Cl₂, HCl, CO | agreement with ledger S° within 0.5 J K⁻¹ mol⁻¹ (CO flagged for ch11) |
| 11 | `heat-capacity` | C_V,m of N₂, Cl₂, normal and equilibrium H₂ vs T | limits 3/2, 5/2, 7/2 R; Einstein function value at T = θ_v |
| 11 | `ortho-para` | equilibrium para-H₂ and ortho-D₂ fractions vs T | 25 % para at high T; → 1 at 0 K; D₂ 2:1 |
| 11 | `equilibrium-constant-stat` | K of I₂ ⇌ 2I (vs JANAF), K of H₂ + D₂ ⇌ 2HD | |Δlog K| < 0.05 vs JANAF; K(HD) → 4 at high T |
| 12 | `pes-collinear` | LEPS surface for H + H₂, contours ("contour prepared"), MEP | saddle at r₁ = r₂; asymptote = ledger Morse curve of H₂; barrier > 0 |
| 12 | `eyring` | Eyring plots of the problem data with fitted lines and standard errors | regression recovers the generating ΔH‡, ΔS‡; s_b formula |
| 12 | `kie` | k_H/k_D vs T for C–H, N–H, O–H | formula; → 1 at high T |
| 13 | `chain-kinetics` | H₂ + Br₂ mechanism integrated vs the steady-state law | agreement within 1 % after induction |
| 13 | `lindemann` | fall-off curve | limits k∞ and k₀[M]; half at [M]½ = k∞/k₀ |
| 13 | `michaelis-menten` | v vs [S] with inhibitors; Lineweaver–Burk | v(K_M) = V_max/2; competitive lines share the 1/v intercept; uncompetitive parallel |
| 13 | `oscillations` | Brusselator and Lotka–Volterra | Hopf at B = 1 + A²; conserved quantity of LV constant to 1e-6 |
| 13 | `chemical-relaxation` | T-jump relaxation of A + B ⇌ C | τ formula |
| 14 | `photostationary` | E/Z under irradiation | pss formula |
| 14 | `ozone-chemistry` | Chapman steady state, Cl chain, Leighton | steady states = ODE long-time limits; Leighton relation |
| 15 | `butler-volmer` | i–η for three α; Tafel plot | Tafel slope ln 10·RT/(αnF); low-η slope 1/R_ct |
| 15 | `cottrell` | concentration profiles and i(t) | erf profile solves Fick (finite-difference check); i ∝ t^{−1/2} |
| 15 | `cyclic-voltammetry` | finite-difference CV (reversible and quasi-reversible) at four scan rates | ΔE_p within 57–60 mV (n = 1, 25 °C); i_p ∝ √v within 1 %; i_p = 0.4463 nFAc√(nFvD/RT) within 2 %; E½ = E°′ |
| 15 | `standard-addition` | stripping peaks with additions | x-intercept = −c₀ |
| 16 | `langmuir-bet` | Langmuir isotherms; BET and its linear form | θ = ½ at p = 1/K; linear BET recovers v_m, c |
| 16 | `surface-rates` | LH and ER rates | LH maximum at K_Ap_A = 1 + K_Bp_B |
| 17 | `surfactant-cmc` | γ vs log c, κ vs c | Gibbs slope → Γ; breaks at the CMC |
| 17 | `dlvo` | V(h) at three ionic strengths | Debye length formula; barrier vanishes above a threshold |
| 18 | `tanabe-sugano` | d³ and d⁸ diagrams by diagonalising the dⁿ ligand-field + electron-repulsion matrices (Slater–Condon F², F⁴ from B, C; Gaunt coefficients) | free-ion terms at Δ = 0 (⁴F/⁴P = 15B, ³F/³P = 15B); d³ ν₁ = Δₒ; spin multiplicities recovered; free-ion B from NIST levels |
| 18 | `curie` | χT vs T (Curie, spin crossover); χ vs 1/T | χT constant; T½ = ΔH/ΔS |
| 19 | `ligand-field-activation` | LFAE (Dq) for d⁰–d¹⁰ | d³ and LS d⁶ maxima; values from the CFSE tables |
| 19 | `marcus` | parabolas; ln k vs −ΔG° | maximum at −ΔG° = λ; ΔG‡ formula |
| 20 | `co-stretch` (conditional on sources) | ν(CO) of an isoelectronic series | values equal the ledger |
| 21 | `schulz-flory` | molar-mass distribution of a single-site polymer | Đ → 2 |
| 22 | `band-chain` | Hückel chain levels for N = 2…64; DOS | eigenvalues α + 2β cos(kπ/(N+1)); width → 4|β| |
| 22 | `semiconductor-carriers` | n_i(T) for Si, Ge; doped Si regimes | slope −E_g/2k; saturation at N_D |
| 23 | `nanoparticle-size` | surface fraction of magic clusters; confinement energy | N(n) formula; 1/R² law |
| 24 | `oxygen-binding` | Mb, Hb curves; Hill plot | θ(p₅₀) = ½; Hill slope n at θ = ½ |
| 25 | `binding-titration` | NMR titrations; Job plots | exact isotherm; x_max = 1/2, 1/3 |
| 26 | `polyene-mo` | Hückel coefficients of ethene, allyl, butadiene, hexatriene | signs and node counts; C₂/σ parities of each MO |
| 27 | `radical-clock` | product ratio vs [Bu₃SnH] | 1/ratio linear, slope k_H/k_c |
| 27 | `bde` | C–H BDEs from enthalpies of formation | BDE = ΔfH(R•) + ΔfH(H•) − ΔfH(RH) for each row |
| 28 | `kinetic-resolution` | ee vs conversion for s = 2, 10, 50 | Kagan equation |
| 28 | `er-ddg` | ee vs ΔΔG‡; a two-peak chiral chromatogram | er = exp(ΔΔG‡/RT); areas → ee |
| 29 | `heterocycle-nmr` | synthetic ¹H spectra of pyridine, pyrrole, furan | positions at ledger shifts; integrals 2:1:2, 2:2 |
| 30 | `overall-yield` | overall yield vs steps, linear and convergent | product law |
| 31 | `green-metrics` | AE and E for the ibuprofen and EO routes | AE equals Σ products/Σ reactants from `molar_mass` for each balanced route |
| 32 | `carbonate-system` | carbonate fractions; rain pH vs p(CO₂) | crossings at pK₁, pK₂; pH ≈ 5.6 at the ledger p(CO₂) |
| 32 | `dose-response` | log-logistic curves | 50 % at the median dose |
| 32 | `bod` | BOD curve, oxygen sag | asymptote L₀; sag minimum time formula |
| 33 | `qnmr` | sample + internal-standard spectrum | integrals ∝ proton counts; purity formula recovers the input |

## Image plan

- **AI (~20, 4 batches, run detached with `tools/ai_images.py --book 4`,
  JPEG only; grey stubs via `tools/ai_stubs.py` meanwhile; each reviewed for
  chemical accuracy):** A quantum and spectroscopy — ch1 dye vials on a lab
  bench, ch3 computing cluster room, ch4 symmetric everyday objects, ch7
  tonic water under UV, ch8 MRI scanner room, ch9 powder diffractometer lab
  (6); B physical chemistry — ch11 liquid-hydrogen tank, ch12 medicine
  tablets on a pharmacy shelf, ch14 city smog from a hill, ch15 glucose
  meter in use (no digits), ch16 ammonia plant, ch17 mayonnaise being
  whisked (6); C inorganic — ch21 chemical plant at dusk, ch22 rooftop solar
  panels, ch23 hydrothermal autoclave / quartz-growth plant (3); D organic
  and applied — ch26 person in sunlight on a terrace, ch28 API plant, ch29
  coffee cup and beans, ch31 modern chemical plant, ch33 research lab with a
  glovebox (5).
- **Photographs (~22, licence re-verified through the Commons API before
  insertion; found 2026-10-02 = title exists, licence not yet read):**
  found: `File:Erwin Schrödinger (1933).jpg` (ch1), `File:Helium discharge
  tube.jpg` (ch2), `File:SnowflakesWilsonBentley.jpg` (ch4), `File:ALMA
  antennas on Chajnantor.jpg` (ch6), `File:Fluorite fluorescence.jpg` or
  `File:FluoriteUV.jpg` (ch7), `File:900 magnet new.jpg` (ch8),
  `File:Wl-bragg.jpg` (ch9), `File:Ludwig Boltzmann Grave Zentralfriedhof
  Vienna 2022.jpg` (ch10), `File:Belousov Zhabotinsky reaction
  (4297013382).jpg` (ch13), `File:Hole in the Ozone Layer Over Antarctica -
  GPN-2002-000117.jpg` (ch14, NASA); to find (search throttled): catalytic
  converter honeycomb (ch16), Tyndall effect (ch17), ruby and emerald
  specimens (ch18), Taube or Marcus portrait (ch19), ferrocene crystals
  (ch20), silicon boule (ch22), NASA aerogel and the Lycurgus cup (ch23),
  horseshoe crab and a haemoglobin PDB render (ch24), pyrethrum daisies
  (ch27), Pacific yew (ch30), algal bloom from orbit (ch32, NASA), Schlenk
  line (ch33).

## Style-file needs (for the sync; nothing appended by Book 4)

See the Phase A report, point 4 (character tables, Jablonski styles,
Tanabe–Sugano and PES and CV plot styles, crystallographic glyphs and
stereograms, orbital-correlation requirements on Book 3's `omp`/`omcorr`,
`\termsym`, `\kv`, units `\hartree` and `\bohr`, `decorations.pathreplacing`,
a fishhook arrow style). Reuse first: Book 3's `omlevel`, `omcorr`, `oms`,
`omp`, `omd*`, `omoctahedron`…, cycle styles, `omretro`, `bubbler`,
`septum`; Book 2's `omcubeo`, `omnewman`, glassware; `\omorbs`, `omprofile`.

## Conventions settled in Phase A

- Recall boxes cite other volumes in prose ("the Year 1 volume, on …", "the
  Year 2 volume, on …", "the school volume"); `\cref{ch:b3:…}` only inside
  Book 4. No pointer to any later volume: unproved results are `\admitted`
  with "treated in more advanced courses" or "established experimentally".
- A term owned by Book 2 or 3 is never `\emph{}\index{}`-ed and never
  `\index{}`-ed at all here; named laws Book 4 owns carry their index in the
  owning statement only (S2 point 2).
- Homographs kept apart by phrase (see BRIEFS "Conventions": multiplicity,
  order, class, reduction, term, microstate, transmission, relaxation time,
  quencher, inert, resolution, turnover). The bare word "level" is never
  indexed. Expected linker STOPs: *hole* (ozone hole in ch14),
  *population*, *host*, *guest*, *sol*, *foam*, *gel* outside their owners
  if they over-link.
- Every computed number printed (STO-3G energies, statistical entropies,
  K values, Tanabe–Sugano fits, green metrics) comes from a tested figdata
  script or `tools/molar_mass.py`, never typed.
- Data that cannot be sourced become data of the exercise, presented as
  "a measured value" of the problem's own system (never as a fact about a
  named real substance), or are EXCLUDED and listed in the Phase D report.

## Open items (Phase A, for the sync)

- Rulings on the contested-low terms (DEFINITIONS.md "contested low"; report
  point 2).
- Style-file additions (report point 4); confirm the interface of Book 3's
  orbital pics (`omp` with a signed coefficient and an angle) before ch5.
- Sources at risk (report point 7): cyanine dye λmax, quinine photophysics,
  water-exchange and self-exchange rate constants, Hb/Mb p₅₀ and Hill n, CO
  M value, 18-crown-6 log K, Tolman parameters, ν(CO) of charged carbonyls,
  semiconductor band gaps and N_c/N_v (ioffe unreachable), CO and ice
  residual entropies, ferrioxalate quantum yield, Redfield ratio, seawater
  carbonate constants, H + H₂ barrier height, 5-hexenyl clock constant.
- Book 3's PROGRESS/BRIEFS may still change after this plan: re-run the
  ownership check (command below) before each chapter's definitions.

## Ownership check (re-run before each chapter)

```sh
# Book 1 + Book 2 harvests and Book 3's frozen map, against DEFINITIONS.md
perl -0777 -ne 'while(/\\emph\{([^}]*)\}\s*\\index\{([^}]*)\}/g){($t=$2)=~s/\s+/ /g; print "$t\n"}' parts/grade-*/[0-9]*.tex parts/bachelor-[12]/[0-9]*.tex > /tmp/harv.txt
grep '^| [0-9]' sources/book3/DEFINITIONS.md | awk -F'|' '{gsub(/^ +| +$/,"",$3); print $3}' >> /tmp/harv.txt
```

Result 2026-10-02: exact collisions only with the five intended Book 1
re-founds (*enzyme*, *micelle*, *green chemistry*, *atom economy*,
*greenhouse gas*); every other overlap is a longer compound phrase
(*activated complex* ⊃ Book 2 *complex*, *overall yield* ⊃ *yield*, …),
which the linker resolves by longest match and which names a different
notion.

## Traps (Book 4, from reading Books 1–3 and the tooling)

- Inherited traps of Books 1–3 apply (see `CLAUDE.md` "Traps met while
  writing" and `sources/book2/PROGRESS.md` "Traps"): chemfig has no
  `\lewis`; `\R` is ℝ (use `\cip{R}`); generic species go in math, not in
  `\ce`; primes never inside `\ce`; `% ledger:` on its own line; tick lists
  written out (no `...`); "French"/"programme" trip gate 7; `\foreach` in an
  axis needs `\pgfplotsinvokeforeach`; 3D cells at 60/100 with `omcubeo`;
  count chemfig ring bonds; never name a macro `\par`.
- **STO-3G exponents differ between sources**: BSE's He STO-3G uses ζ = 1.69
  (6.36242…), the classic HeH⁺ textbook benchmark uses ζ_He = 2.0925. Test
  the code on the benchmark, print the standard-basis value, say which.
- `pgfplots` contour maps need `contour prepared` with precomputed contour
  lines (no gnuplot, no shell escape): the figdata writes them.
- The harvester indexes any multi-word `\index` in any statement: theorem
  names this book owns are indexed only in the owning statement.
- Commons API search throttles after ~10 rapid queries: pause between calls.
- The Gold Book and IUPAC PAC are behind Cloudflare (403): IUPAC values must
  come from another primary page or be EXCLUDED.
- Never type Unicode Greek (π, θ) in `.tex`: pdflatex dies; `$\pi$`.
- `axis cs:{expr with \v}` inside a `\foreach` in an axis fails: write the
  coordinates out.
- `ffmpeg` inside `while read` eats stdin: `ffmpeg -nostdin`.
- Photos: check for flags, logos, institution names before use (nmr-magnet
  replaced by nmr-lab).
- A tdplot `shift={(0,s,0)}` drifts vertically on screen: place side-by-side
  cells with a canvas `xshift=s cm`.
- `x=3cm, y=3cm` scales unit-less pic coordinates: the Book 4 glyph pics now
  set `x=1cm, y=1cm` internally (fixed size); a figure-level `scale=` without
  `transform shape` trips the pic-scaling gate.
- Check that a construction passes through the point the caption names
  (Ewald circle drawn through the wrong node).

## EXCLUDED facts (for the Phase D report)

- ch10/11: calorimetric (third-law) entropy of CO and residual entropy of ice
  measured values: Clayton & Giauque / Giauque & Stout not open; the text gives
  only R ln 2 and Pauling's R ln(3/2) and says the gap is "of the order of".
- ch12: H + H2 barrier height of an accurate surface (no open source reached):
  the figure is a stated LEPS model (Sato 0.17), barrier 0.27 eV "in this model".
- ch13: water-neutralisation rate constant (Eigen): named, no number.
- ch14: ferrioxalate quantum yield: data of the exercise (1.25 at 365 nm) and
  "a calibrated quantum yield" in the method.
- ch15: lead guideline value in drinking water (WHO page has no number;
  no Book 3 `who:` row): not printed; ferrocene / hexacyanoferrate D: data of
  the problem.

## Shared-tooling / cross-book notes (for the report)

- Book 3 ledger rows used read-only: s0:* (CODATA-KEY), ghs:H2. A later Book 3
  row with the same id as one of mine (s0:I2_g, s0:Cl_g, s0:Kr_g, s0:Ne_g)
  would collide: tell Book 3 / main session.
- Python's stdlib has a C module `_stat`: a figdata helper named `_stat.py`
  is shadowed silently (import gives the stdlib module): renamed `_statmech.py`.
- A full build of Book 4 now takes about 45 s per pdflatex pass (> 120 s with
  latexmk's reruns): run builds with a 400 s timeout.
- Gate 7 (curriculum words) matches "programme" inside "temperature-programmed":
  the TPD definition became "thermal desorption spectroscopy" (report as a
  tooling false positive).
- A `% ledger:` comment inserted mid-paragraph swallows the rest of its line
  in the printed text too: always put it on a line of its own.
- `\foreach` variables passed into a pic argument that the pic compares with
  `\ifx` (Book 3's `omlevel`) are not expanded: write the pics out, or `\edef`.
- A bracketed optional title containing `]` (e.g. `[Re2Cl8]^{2-}`) must be
  braced: `\begin{proposition}[{...}]`.
- CCCBDB has no transition-metal carbonyls; the nu(CO) series of
  [V(CO)6]-/Cr(CO)6/[Mn(CO)6]+ is EXCLUDED (qualitative only); free CO 2143
  cm-1 computed from the WebBook constants.
- Book 2's ledger row `epsr:H2O` = 78.54 (NBS Circular 514, 1951) is above the
  modern consensus 78.4 (IAPWS R8-97, evaluated here as `eps:H2O.25C`): report
  to the main session (cross-book defect, Book 2 is not mine).
- Run cut by a network error (EAI_AGAIN) during ch25's figdata (2026-10-03);
  resumed from this file: ch21-24 were complete, ch25 had only its figdata
  script; finished in order.
- Chemfig: `[M]` at the start of a `\chemfig` is read as an angle (pgfmath
  "Unknown function M"); node names with decimals (`oa-1.25`) break pgf; use
  lettered names.
- The index (imakeidx + multicol) reported an "Overfull \vbox while \output is
  active" after ch28 grew it: `\renewcommand{\indexspace}{\par\vskip 8pt plus
  4pt minus 4pt\relax}` before `\printindex` in the entry file (as Books 1-2).
- `booktabs` is not loaded: `\toprule`/`\bottomrule` are undefined, use `\hline`.
- Legend samples of thin coloured lines look black at 130 dpi: check at 300 dpi
  before "fixing" them.
- WebBook has no gas-phase enthalpies of formation for most alkyl radicals;
  ATcT (atct.anl.gov) and the IUPAC Gold Book are behind Cloudflare; Burcat's
  BURCAT.THR (respecth.elte.hu mirror) quotes the ATcT values with references.
- Burcat's tert-butyl entry is garbled ("HF298=95855.04"); its NASA H/R term
  gives 55 (G3B3); the row uses Tsang's 52 quoted beside it.

## Solutions re-read (2026-10-03, main-session request)

Every solution of ch1–33 (12 exercises + the weekend problem each) re-read against its own question; every printed number recomputed by script (python one-liners in the scratch directory; ligand-field and Tanabe–Sugano values through `figdata/bachelor-3/_ligandfield.py`, glucose and DLVO values through their figdata scripts). Checked for: permutations, contradictions with the question's data, wrong species or quantity, rounding from rounded intermediates.

**Totals: 24 slips in 13 chapters (ch1, 2, 3, 6, 8, 9, 10, 13, 14, 15, 25, 30, 32); 20 chapters clean (ch4, 5, 7, 11, 12, 16–24, 26–29, 31, 33).** Two slips were in the question statements themselves (ch13 pb 11, the standard error of K_i; ch15 exo 12 and pb 13, S_xx of the calibration); one was a claim contradicted by the data (ch15 pb 11); one a self-contradicting range (ch1 pb 6); the rest are last-digit or rounded-intermediate slips. No chemistry error (wrong species, wrong product, wrong mechanism) was found.

| ch | item | slip | fix |
|---|---|---|---|
| 1 | pb 6 | "too short by factors 2.3 to 3.6" contradicts its own answers (524/147 = 3.6, 603/257 = 2.3, 711/374 = 1.9) | factors 3.6, 2.3 and 1.9 |
| 2 | exo 5 | interval ratio 27.0/16.4 = 1.646 printed 1.64 | 1.65 |
| 2 | exo 6 | A = 17.20/1.5 = 11.467 printed 11.46 | 11.47 |
| 3 | exo 11 | omega~ = 5451.5 cm-1 printed 5451 | 5452 |
| 3 | pb 22 | -2.8078 - (-2.8418) = 0.0340, printed 0.0341 | 0.0340 |
| 6 | exo 6 | D_e and D_0 from the printed 2990.95 and 52.82 are 42341 and 40859 cm-1; the solution printed the full-precision values 42342 and 40860 | 42341, 40859 |
| 6 | exo 9 | 4B0(J + 3/2) for J = 2 is 27.854 cm-1, printed 27.86 | 27.85 |
| 6 | exo 11 | Birge-Sponer sum 40856.8 printed 40858; D_e - G(0) 40859 | 40857 against 40859 |
| 6 | pb 20 | 2 x 2169.81 - 6 x 13.288 = 4259.892, printed 4259.90 | 4259.89 |
| 6 | pb 15 | "It is 12 MHz low" was ambiguous (the measured line is the higher one) | "The prediction is 12 MHz below the measured line" |
| 8 | exo 1 | 42.58 x 14.1 = 600.38, printed 600.3 | 600.4 |
| 9 | exo 5 | d110 = 154.06/(2 sin 20.135 deg) = 223.773, printed 223.78 | 223.77 |
| 10 | exo 12 | terms x/(e^x-1) = 0.5721 and -ln(1-e^-x) = 0.4420 at x = 1.0292, printed 0.5722 and 0.4421 (sum 8.43 unchanged) | 0.5721 + 0.4420 |
| 13 | pb 4 | (0.502 - 0.491)/0.005 = 2.2 standard errors from the printed values, printed 2.4 | 2.2 |
| 13 | pb 11 (question and answer) | the stated standard error of K_i, 0.7 uM, ignored the (negative) intercept-slope covariance of the 4-point fit; propagated correctly it is 0.90 uM | question gives 0.9 uM; interval 24.9 +/- 3.9 uM |
| 14 | exo 7 | RT at the stated 298 K is 2.478 kJ/mol, printed 2.479 (the 298.15 K value) | 2.478 |
| 14 | pb 16, 17, 19 | ClO lifetime computed from rounded k and [O]: 1/(4.033e-11 x 1.423e8) = 174 s, printed 175 s | 174 s throughout |
| 14 | pb 18, 21 | k[O] for ClO + O = 5.74e-3 s^-1, printed 5.72e-3 (rounded intermediates) | 5.74e-3 |
| 14 | pb 20 | k[O3] for Cl = 53.8 s^-1, printed 54.0 (result 0.99978 unchanged) | 53.8 |
| 15 | exo 12 and pb 13 (questions and answers) | S_xx of the seven glucose standards (2 to 20 mM) is 241.4 mM^2, printed 246 in both statements, hence b^2 S_xx = 203.9, printed 207.8 (results 0.090 / 0.104 / 0.090 mM unchanged) | 241 and 203.9 |
| 15 | pb 11 | "the residuals are below 1 %" is false: the 2 mM point is off by 1.6 % | "the residuals, at most 0.095 uA, scatter without trend" |
| 25 | exo 7 | -RT ln(2.0e5) at 298 K = -30.24 kJ/mol, printed -30.3, hence T dS = -9.7 instead of -9.8 | -30.2 and -9.8 |
| 30 | pb 14 | "42/1.8 = 24" is 23.3 as written; the unrounded linear yield 1.78 % gives 24 | 42/1.78 = 24 |
| 32 | exo 8 | BCF ratio PCB/benzene = 10^(0.85 x 4.54) = 7.2e3, printed "nearly ten thousand times" | "some seven thousand times" |

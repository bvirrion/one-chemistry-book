# Book 2 (University Chemistry, Year 1) — progress

Resume file: a fresh agent must be able to continue the book from this file
alone, with `sources/BATCH_BOOKS_1-4.md` (binding rules, read first),
`BRIEFS.md` (per-chapter plan) and `DEFINITIONS.md` (term list) beside it.

## State

- **Book 2 complete 2026-10-02 (Phases A-D)**: 29 chapters, 293 pp,
  0/0/0, gates OK, 2,471 term links (0 to insert on re-run), figdata stable,
  107 tests pass. Phase D report sent to the coordinator.
- Phase A done 2026-10-02; sync S1 + S1b received (all contested terms
  granted; hydroxide is `\ce{OH-}`; `\cip`, `\debye`, `\ppm`, `\omorbs`,
  `omprofile`, `omeph`, `\omperiodictable` exist).
- Shared pic block `% Book 2 (shared pics):` appended to the end of
  `styles/onechemistry.sty` (Newman, chair, crystal helpers, electrochemistry
  and organic apparatus), tested on a scratch page; interfaces documented in
  its comment. Book 1 owns volflask, pipette, gradcyl, cuvette, condcell,
  bunsen, gasjar, deliverytube, trough, evapdish, utube, balance, stand.
- Entry `one_chemistry_book_2_university_year_1.tex` builds 0 errors /
  0 undefined / 0 overfull, 40 pp (29 placeholders + frontmatter), at
  Phase A.
- Nothing written in `parts/bachelor-1/` yet; ledger `sources/ledger/book2.md`
  empty; `figdata/bachelor-1/`, `tests/bachelor-1/`, `images/book2/` empty
  apart from the scaffold's `CREDITS.md` and `ai/`.

## Chapter status

| ch | slug | ledger | text | exos/pb | solutions | figures | build+gates | FIGCHECK |
|---|---|---|---|---|---|---|---|---|
| 1 | quantum-numbers | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2 | periodicity | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 3 | lewis-resonance-vsepr | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 4 | intermolecular-forces-solvents | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 5 | crystals-metals | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 6 | crystals-ionic-covalent | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 7 | extent-q-and-k | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 8 | rate-laws | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 9 | elementary-steps | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 10 | predominant-reaction | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 11 | precipitation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 12 | complexation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 13 | nernst | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 14 | e-ph-diagrams | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 15 | titration-methods | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 16 | stereochemistry-in-depth | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17 | structure-spectroscopy | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 18 | electronic-effects | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 19 | nucleophilic-substitution | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 20 | elimination | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 21 | organomagnesium | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 22 | alcohol-activation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 23 | acetals-protection | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 24 | organic-redox | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 25 | electrophilic-additions | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 26 | s-block | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 27 | p-block-13-15 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 28 | p-block-16-18 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 29 | lab-techniques-1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

Legend: – not started, ✓ done; build+gates means `latexmk` 0/0/0 and
`bash tools/gates.sh bachelor-1` green after that chapter.

## Page projection

Target ~340 pp. Plan: 29 × 11.5 pp ≈ 334 pp of chapters + solutions
(solutions run in the appendix), + ~10 pp frontmatter + ~8 pp index ≈
350 pp. Checkpoints after ch. 10, 20 and 29: measured pages per chapter vs
11.5; > 15 % under ⇒ restore depth before continuing.

| checkpoint | chapters done | pages | pp/ch | projection | verdict |
|---|---|---|---|---|---|
| Phase A | 0 | 40 (stubs) | – | ~350 | – |
| ch. 10 | 10 | 134 (ch. 1-10 bodies pp. 9-94 = 86 pp; their solutions ~19 pp) | ~10.5 | 29 x 10.5 + 13 = ~318 | -6.5 % vs 340: within 15 %, keep depth (organic chapters carry more mechanism figures) |
| ch. 20 | 20 | 224 (ch. 1-20 bodies PDF pp. 11-176 = 166 pp; solutions of ch. 1-20 33 pp) | ~9.9 (ch. 11-20: 8.0 body + 1.7 solutions) | 29 x 9.9 + 16 = ~303 | -11 % vs 340: within 15 % but drifting; chs. 21-29 to aim at ~9.5 body pp: one more worked example and an in-the-lab box per organic chapter, photographs in the descriptive chapters 26-28 |
| ch. 29 (final) | 29 | 293 (bodies PDF pp. 11-232; solutions 233-279; index 280-293) | ~7.6 body + 1.6 solutions | 293 | -13.8 % vs 340: thinnest bodies ch. 20, 22, 23, 24, 25, 27 (6 pp each), then 14, 18, 19, 21, 28 (7 pp); reported in Phase D, not padded |

## Budgets and counts

- Web searches (WebSearch tool): **0 used** of a ~600 plan (estimate for
  the whole book ~350; see report point 7). Commons API queries via curl
  (not web searches): 4 batches, ~40 queries, 2026-10-02.
- AI images: 0 (plan ~25 in 5 batches). Photographs: 0 (plan ~25).
- Ledger rows: 0 (plan ~450).
- figdata scripts: 0 (plan 22, list in BRIEFS and in the Phase A report).

## Conventions settled in Phase A

- Recall boxes cite Book 1 in prose ("the school volume"), never `\cref`;
  `\cref{ch:b1:…}` for earlier Book 2 chapters.
- A notion owned by Y2/Y3 is never `\emph{}\index{}`-ed and never
  `\index{}`-ed at all in Book 2 (see traps).
- Ks, E° and E–pH boundaries are **computed** from NBS-82 ΔfG° ledger rows
  in tested figdata scripts (`standard-potentials.py`, Ks inside
  `solubility-ph.py` / `eph-diagrams.py`) unless an open primary table of
  E°/Ks is found; the printed values are asserted by the tests.
- figdata scripts read ledger values by id through a local helper
  `figdata/bachelor-1/_ledger.py` (underscore: skipped by `make
  figdata`), so no number is retyped.
- ¹H NMR spectra simulated at 400 MHz, first order, Lorentzian lines;
  IR spectra synthetic at ledger band positions; UV bands Gaussian at ledger
  λmax.
- Weekend problems: story + Parts I–IV, 24–26 questions, named final
  number printed in the last question's statement or answer.
- Electron "screening" (ch. 2) vs nuclear "shielding" (ch. 17): two words,
  no homograph.
- No "retrosynthesis/disconnection/synthon" (Y2), no "enantiomeric excess"
  (Y3), no "Le Chatelier/shift" language (Y2): Q/K arguments instead.

## Open items

- AI batch 2 landed and reviewed (2026-10-02 12:27): b1-10 descaling,
  b1-11 cave, b1-14 ship anodes, b1-15 teaching lab, b1-16 caraway-mint,
  b1-17 carrots-tomatoes, b1-17 nmr, b1-24 wine cellar, b1-25 bananas; stubs
  in ch. 10, 11 replaced. Batch 3 (ch. 26-29 scenes) still to run.
- Sources secured for chs. 11-15: NBS-82 (Ag, Zn, Cu, Fe, Mg, Ca, Ba, Al,
  Cr, Li, Na, K, Ni, Pb, Mn, Hg pages, SCN-, Fe(CN)6, FeSCN, FeF), NEA-TDB9
  (edta pKa and Ca/Mg/Ni-edta at I = 0; Ca oxalate), NIST-SP260-142 and
  NIST-JRES100 (limiting conductivities; Na+ and Cl- derived by
  Kohlrausch), IUPAC-PKA (indicators: methyl orange, methyl red, phenol
  red, thymol blue). EXCLUDED so far: Ag(S2O3)2 3- (no Gibbs energy in
  NBS-82, no open critical value: ch. 12 problem uses ammonia instead),
  Cr3+ (no Gibbs energy: dichromate E0 not printed), Cu(OH)2 Ks (CuO used,
  said so), CaC2O4 Ks only as whewellite from NEA (not yet printed),
  Ce4+/Ce3+ (permanganate used instead), CH3COO- conductivity (no
  conductimetric curve of a weak acid), methyl A-value (1,3-diaxial
  estimate from the butane gauche energy instead), specific rotations of
  carvone (none in PubChem; menthol only as the HSDB range).
- NBS-82 Gibbs energies read so far (ledger `dfg:`): O, H, F, Cl, Br, I, S,
  N, P, C (inorganic). Element tables at PDF page = printed page + 8
  (index p. 2-392): Zn 2-138, Cu 2-154, Ag 2-160, Fe 2-177, Mn 2-191, Cr
  2-197, Al 2-127, Ca 2-267, Mg 2-260, Ba 2-282, Hg 2-150, Pb 2-119, Ni
  2-166, Li 2-290, Na 2-299, K 2-328.
- `figdata/bachelor-1/_thermo.py` computes pK and E0 from `dfg:` rows;
  `aqueous-constants.py` lists every computed constant; its test pins the
  printed values.

## Open items (Phase A, for the sync — closed by S1)

- Rulings on the contested terms (DEFINITIONS.md "contested" rows; Phase A
  report point 2).
- Style-file additions (report point 4): Newman, chair, crystal-cell
  helpers, electrochemical and organic apparatus pics, orbital boxes,
  `omprofile`/`omeph` axis styles, siunitx `\debye`, `\ppm`.
- Sources at risk: stability constants (Cu–NH₃, Ag–S₂O₃, Ag–NH₃),
  limiting molar ionic conductivities, Ce⁴⁺/Ce³⁺ formal potential,
  methyl A-value, polyene λmax/ε, refractive indices. If no primary source
  is reachable, the value is not printed (EXCLUDED list in the Phase D
  report) and the exercise uses invented data instead.

## Traps (Book 2)

- Data sources that work by script (scratch `data/` helpers): NIST ASD
  (curl CSV), WebBook (ion energetics Mask=20, diatomic Mask=1000, phase
  Mask=4 -- many hydrides lack Tboil there: PubChem PUG-View `Boiling
  Point` instead), CCCBDB (`expgeom2x.asp` with a cookie jar; uppercase
  tags; dipoles from `diplistx.asp`), COD CSV (`/cod/result?formula=..&format=csv`;
  Wyckoff 1963 entries 9008xxx), Shannon database, PubChem PT JSON, JANAF
  `tables/X-00n.txt`, IUPAC pKa CSV (CC BY-NC 4.0, not CC BY), NBS
  Circular 514 (OCR text, PDF page in the row). AMCSD (rruff) times out.
  NBS-82 (Wagman) PDF is a scan without text: read pages as images.
- Book 1 already owns some rows (`rho:Fe`, `rho:NaCl`): grep all ledgers
  before minting and cite theirs.
- 3D cells (corrected after the main-session spot-check): at tdplot
  70/110 the BCC main diagonal projected onto a face diagonal and the old
  omcube dashed the wrong edges (the hidden vertex for 0<theta<90,
  90<phi<180 is the ORIGIN, not (0,a,0)). Now 60/100 with `omcubeo` /
  `omhexprismo`; the HCP prism has its own view 70/113 (at 60/100 a B atom
  fell 0.1 unit from a hidden vertex). Toward-viewer vector
  (sin t sin p, -sin t cos p, cos t); draw atoms by ascending depth along
  it. Check projected geometry by computing screen coordinates (minimum
  distance between atoms, clearance of each drawn diagonal), not only
  labels; keep anions larger than cations.

- **chemfig has no `\lewis`** (removed in chemfig 1.5+): lone pairs and
  charges with `\charge{90=\|,270=\|,45:2pt=$\scriptstyle\ominus$}{O}`
  (`\|` bar = lone pair, `\:` two dots, `\.` one electron). Book 2 draws
  lone pairs as bars in Lewis structures, as dots in the VSEPR gallery.
- Lewis drawings need `\large` and `atom sep=2.4em` to be legible;
  `\setchemfig` inside an `omfigure` stays local.
- `\foreach` inside a pgfplots `axis` does not expand `\x` in `axis cs`:
  write the draws out or use `\pgfplotsinvokeforeach`.
- mhchem: a charge after a group needs `^`: `\ce{-COO^-}`, not `\ce{-COO-}`
  (the trailing `-` prints as a bond). `\bond{...}` trips gate 3: write
  `$\ce{X-H}\cdots\ce{Y}$`.
- A `% ledger:` line must not swallow prose: put it on its own line, ids
  then `(` free text.
- Generic species (A, B, C) in equations fail the balance gate inside
  `\ce`: write math, `$\mathrm{A} + \mathrm{B} \rightleftharpoons \mathrm{C}$`;
  scratch `generic_eq.py <files>` converts them automatically.
- Gate 7 flags the word "French" even in history ("published in French"):
  rephrase.
- Tick lists `{a,b,...,c}` trip gate 3 (the `...` grep): write ticks out.
- mhchem cannot read primes (R', R''): generic groups with primes go in
  math, `$\mathrm{R'{-}X}$`, never in `\ce` (fatal build error and a gate
  failure).
- Ledger ids must start with a lowercase prefix (`lamsalt:HCl`, not
  `Lam:HCl`).
- Never type a source's authors or title from memory: read them off the
  PDF's first page (the JRES conductivity paper was first mis-attributed).
- Printed arithmetic with rounded data (pKe 14.00, 2-decimal pK) can differ
  by 0.01 from the figdata (pKe 13.995): print the rounded-data result,
  test both, say in prose that the figure is computed from Gibbs energies.
- `\label{fig:...}`/`\label{tab:...}` inside `omfigure` refer to the
  section (no figure counter): refer to figures in prose ("figure below").
- `\pgfmathtruncatemacro{\par}` breaks everything: never name a macro
  `\par`.
- imakeidx multicol: an overfull vbox on the last index page appears at
  some index lengths; the entry file now sets `\indexspace` with shrink
  (as Book 1).
- WebFetch and curl both blocked on degruyter/old.iupac.org (Cloudflare):
  IUPAC PAC PDFs are unreachable; the NEA TDB volumes on oecd-nea.org are
  open.

- **The harvester collects more than definitions**: `\emph{}\index{}`
  outside a `definition` and any **multi-word `\index{}` entry in any
  statement** become link targets (`tools/termlink/harvest.py`). Never
  `\index` a notion owned by another book.
- `\R` is `\mathbb{R}` in the style file: write CIP descriptors as
  `(\textit{R})`, `(\textit{S})`, never `\R`.
- The repo venv has numpy and pytest only (no scipy): root-finding by
  bisection on the charge balance, ODEs solved analytically.
- No `\cref` into Book 1 (prose only); `CONTRIBUTING.md`'s recall-box rule
  ("with a `\cref` to the owner") applies inside Book 1 only.
- Gate 7 greps "programme", "French", "collège"… in printed text, comments
  excepted: no "temperature programme" wording.
- A placeholder chapter keeps its `\noindent\emph{To be written.}` line
  until replaced (a run of bare `\section*` stubs cannot break pages).
- Build with `latexmk -g` after a chapter file changes from placeholder to
  real content only if the `.fls` misses it; always `nice -n 10`; never
  interrupt a run (recover by deleting this entry's `.aux .toc .out
  .fdb_latexmk` in `build/`).
- The term linker wraps words inside macro *options*: `f block=false` in
  `\omperiodictable[...]` and labels in chemfig `\arrow{->[...]}` became
  `\omterm{...}` and killed the build. Book 2's config masks both
  (EXTRA_PROTECT); check any key=value option that contains a defined word.
- Bare "group" is the periodic-table group only before a number: masked
  elsewhere, or "methyl group" links to the periodic table.
- A chemfig ring `*6(...)` must have six bonds in the cycle body: the
  cyclic hemiacetal was drawn as a five-bond open chain until counted
  (scratch check: count bonds outside branches).
- chemfig schemes sit flush on the caption: put `\par\vspace{6pt}` after
  `\schemestop` / `\chemmove` when the scheme has substituents below.
- Re-reading every solution with an independent reviewer found 37
  findings in chs. 1-28 (4 chemistry: an indicator "too early" that was
  too late, axial costs of OH/Cl taken as a methyl's, an alkoxide named
  after the alkane; 2 incomplete answers; 25 rounding chains). Fixed;
  rounding from rounded intermediates is the commonest slip.

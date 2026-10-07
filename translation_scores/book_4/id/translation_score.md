# Translation score — Chemistry Book 4 · Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 4 (University Chemistry, Year 3 — year `bachelor-3`, labels `b3`) |
| **Language** | Indonesian (`id`) |
| **Quality bar** | **native academic prose**: a third-year Indonesian university chemistry course (*Kimia Fisik III*, *Kimia Anorganik Lanjut*, *Kimia Organik Lanjut*, *Kimia Lingkungan* register) as it is written and taught. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **References measured before drafting** | the **English** canon; the shipped **Indonesian Books 2 and 3** (`parts/bachelor-1/id/`, `parts/bachelor-2/id/`, their term configs and scores) for series terminology and the impersonal *-lah* register; `indonesian_style_card.md`; `sources/TRANSLATION_BOOKS_3-4.md`, `sources/WAVE1_FINDINGS_B34.md`, `sources/WAVE2_FINDINGS_B34.md` |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-07 |
| **Scope** | A full first translation written directly at native register (no machine draft): 33 chapters and 33 solution twins, **66 files**, all written through `tools/id_apply.py`. Also the Indonesian image-credits page, a curated `tools/term_config/book4_id.py`, the link layer, Indonesian index keys, the overfull, orphan-heading and per-figure sweeps, and this score |

## Verdict in one line

An Indonesian Book 4 that reads as a third-year Indonesian chemistry course. Its vocabulary:

- quantum and spectroscopy: *fungsi eigen / nilai eigen*, *operator Hermitian*, *energi titik nol*, *rotor tegar*, *penerowongan*, *determinan Slater*, *medan swakonsisten*;
- symmetry and solids: *grup titik*, *representasi tak tereduksi*, *aturan eksklusi timbal balik*, *kisi resiprokal*, *fungsi partisi*;
- kinetics and surfaces: *kompleks teraktivasi*, *frekuensi perputaran*, *fisisorpsi / kemisorpsi*, *plot gunung api*, *konsentrasi misel kritis*;
- inorganic and organometallic: *transisi spin*, *donasi balik*, *hapisitas*, *senyawa sandwich*;
- organic: *konrotatori / disrotatori*, *suprafasial / antarafasial*, *kumpulan kiral*, *auksiliari kiral*, *urutan linear terpanjang*;
- green and environmental chemistry: *ekonomi atom*, *faktor-E*, *penilaian daur hidup*, *kebutuhan oksigen biokimia*;
- the lab: *jalur Schlenk*, *kotak sarung tangan*.

The register is impersonal *-lah* imperatives, with no *kamu/Anda* and decimal points as in the canon. Every structural, chemistry, prose and link gate is green on a forced build:

- **0 errors / 0 undefined / 0 overfull / 0 invalid in math mode**;
- `nullfont` 17 and `Missing character` 17, both the English baseline.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | All 66 files mirror their 66 twins (EN = ID): `exercise` 396, `problem` 33, `solution` 429, `omfigure` 199, `tikzpicture` 161, `definition` 323, `theorem` 65, `proposition` 184, `method` 89, `example` 53, `proof` 236, `\label` 1183, `\cref/\Cref` 205, `\emph` 677, `\index` 675, `\qty` 1997, `% ledger:` comments 167. A numeric census of every file (all digit tokens, as multisets) equals English, except deliberate TikZ label coordinates (listed under Figures) and one `\enlargethispage` |
| Chemistry fidelity | **99** | Byte-identical in order (gate 12, OK on 66 files): `\ce` 1657 = 1657, `\chemfig` 32 = 32, `\schemestart` 13 = 13, `\ghs` 80 = 80. `check_ce_balance.py`: 59 + 45 equations, 0 problems. `!chem` was never used. Arrow labels translated: 14/219, 226; 23/74, 83 (*hidrolisis / kondensasi*); 27/280 `->[$\ce{CH2}$ singlet]`; 27/374 *asam peroksi*; 29/386 `[{[3,3]}, lalu][siklisasi, $-\ce{NH3}$]` |
| Terminology | **96** | A running glossary was checked against Indonesian Books 2–3 (*tetapan*, *pereaksi*, *elektrode*, *amin* for ammine, *frekuensi perputaran* = TOF). See "Terminology decisions" below |
| Register & naturalness | **95** | The stem profile matches Book 2/3 id (*Hitunglah, Tuliskan, Tentukan, Jelaskan, Tunjukkan, Berikan, Nyatakan*). Definitions use *Yang disebut … adalah …*. Proofs are *Bukti*, *Bukti parsial*, *Argumen*, *Menurut definisi*. The final read fixed calques: *berutang warna* became *berwarna … karena*; *X gas* became *gas X*; a double *yang*; *aduk* (stir) misused for "adduct" became *hasil adisi*; a garbled enzyme definition was rewritten |
| Mathematics & notation | **97** | Math spans byte-identical (id_apply census). `\text{}` subscripts translated where they are words; conventional ones kept |
| Figures | **95** | `!draw` was used only on \foreach label lists: 05/271, 08/315, 09/77, 22/126, 24/106, 26/179, 33/413. Every figure page was rendered and read at 130 dpi, zooming to 300 dpi on suspects (199 figures on 174 pages). Eleven text collisions were fixed in the id files, with the drawing untouched (see "Layout") |
| Link layer | **96** | 1789 links on 257 targets (English 1634 / 253). Every English target is reached; the 4 extra are all the defined sense (*Hartree–Fock*, *parameter Racah*, *transisi spin*, *pori*). Dry run 0 |

**Overall: 96.**

### Terminology decisions

- **Homograph pairs kept apart in the wording itself:**
  - *karakter* (character of a representation) / *sifat* (bond character, s character);
  - *operator* (mathematics) / *operator* (person, protected);
  - *populasi* (states) / *populasi* (organisms, protected).
- **Matrix trace** is *jejak* (series form, Book 3 id *Jejak matriks*), and a chiral HPLC trace is *kromatogram*.
- **Spelling unified:**
  - quinine is *kinina* everywhere;
  - *(foto)sensitizer* matches the existing id editions, beside *(foto)sensitisasi*;
  - *doblet* matches Book 2 id.

## Gate output summary

```
bash tools/check_translation.sh bachelor-3 id ......... TRANSLATION GATE: PASSED
  indonesian prose gate: OK (66 files)
  latin prose gate: no multi-word findings (one-word tier read, 44 hits: cognates
     proton, deuteron, virtual, normal, total, donor, isolobal, diameter, linear,
     zigzag, Doping; eponyms Slater, Rayleigh, Stokes, Scherrer, Langmuir,
     Schottky, Frenkel, Hohenberg--Kohn, Lotka--Volterra, Brusselator,
     Diels--Alder, Chapman; units/symbols ppm, ppb, pss, fcc, org; the
     Cope/Claisen \foreach list)
  chemistry twin gate: OK (66 files)
forced build (scratchpad/build.sh), build/one_chemistry_book_4_university_year_3_id.log
  errors 0 · undefined 0 · Overfull 0 · nullfont 17 · Missing character 17 ·
  invalid in math mode 0 · pages 425 (English 405) · .fls Indonesian sources 66
python3 tools/link_defined_terms.py --book 4 --lang id ... links to insert: 0
```

### Link-layer curation (`tools/term_config/book4_id.py`)

- **STOP:** *migrasi*. Ion migration would otherwise have linked to the
  migratory-aptitude sense.
- **EXTRA:** *terkendali / dikendalikan difusi*, linked to the diffusion
  definition.
- **DERIVED:** reduplicated plurals of multi-word terms, which `lang_id.py`
  cannot reach:
  - *faktor-faktor Franck--Condon*, *fungsi-fungsi eigen*, *nilai-nilai eigen*;
  - *unsur-unsur simetri*, *operasi-operasi simetri*, *modus-modus normal*;
  - *puncak-puncak silang*, *pusat-pusat inversi*, *bidang-bidang kisi*;
  - *kompleks-kompleks teraktivasi*, *reaksi-reaksi berosilasi*, *suku-suku medan ligan*;
  - *fragmen-fragmen isolobal*, *keadaan-keadaan triplet*.
- **EXTRA_PROTECT** (beyond the stub's code masks):
  - *operator* as a person;
  - non-representation *karakter* (*karakter ganjil / pemutusan / s / π*);
  - *populasi* of algae, birds, and "half the population";
  - the porphyrin *lubang* (hole).

## Layout

- **Overfull boxes:** the first full builds had 15, in ch. 2, 3, 6 and 11, ch. 20, sol. 5, 13, 21, 27, 28, 30 and 33, and a 15 pt `\vbox` on the ch. 9 weekend problem. All were removed by rewording, each checked with a single-file probe compile.
- **Orphaned problem heading:** the ch. 31 weekend-problem heading was orphaned on an otherwise empty page. It is fixed with `\clearpage` + `\enlargethispage{3\baselineskip}`, as English does for ch. 9.
- **"Bagian" headings at a page foot:** four, in ch. 6, 10, 23 and 27. Every problem part list now opens with `beginpenalty=10000` (enumitem; 131 lists) to keep a part heading with its first question.
- **Tail pages:** two problem tails spilled onto their own page (ch. 5, ch. 26). Both problems were tightened by two or three one-line rewordings. In ch. 26 this made the box land 15 pt over its enlarged page, so it was tightened once more.
- **Figure fixes** (label position or wrapping only):
  - ch. 13: stopped-flow *pencampur*;
  - ch. 16: *persilangan* moved off the curves; volcano left label rewrapped;
  - ch. 17: *silinder (tampak samping)* on two lines;
  - ch. 21: *eliminasi reduktif* label;
  - ch. 24: *kemiringan 2.7*;
  - ch. 27: *5-exo* → *5-ekso*;
  - ch. 28: *muka Si* label;
  - ch. 31: LCA end-of-life box;
  - ch. 32: *limpasan*, with the two source boxes moved 0.5 cm left to give the label room;
  - ch. 33: *labu Schlenk*; the characterisation flowchart's X-ray box.

  In ch. 22, two `\fill` band rectangles that an early draft had replaced with comment translations were restored (caught by the TikZ command census).

## Shared-tool edits (append-only, reasoned, reported)

1. `check_indonesian_prose.py`, **ATTRIBUTION:**
   - *twanight.org* (ch. 6 photo credit);
   - *William Lawrence Bragg* (ch. 9 photo credit and history);
   - *Persamaan Young* (ch. 17 theorem title starting with an eponym);
   - *Benjamin List* (ch. 28 history).
   Domain names and full names otherwise fire the English-suffix rules.
2. `check_indonesian_prose.py`, **NOT_GATED:** *glutation* (sol. 19, the Indonesian spelling of glutathione).
3. `check_indonesian_prose.py`, **WORK_TITLE:** *Silent Spring* (ch. 32 history; nl and pt keep it verbatim).
4. `check_latin_prose.py`, **`ALLOWED_BY_LANG["id"]`:** *cis, trans, fac, mer, singlet, triplet, purge*. The reasons:
   - sol. 5 answers "cis 2, trans 1, fac 2, mer 3" (dup tier);
   - ch. 27 carbene nodes;
   - ch. 31 node *purge (Ar, CH4)*.
   The blocking tier was verified to go to 0.

## English-canon defects

- `parts/bachelor-3/solutions/32-environmental-toxicology.tex` line 96: "5.7 μg/L × 0.015 = 0.084 μg/L".
  - With the printed factors the product is 0.0855, which prints as 0.086.
  - The unrounded chain, 5.71 × e^(−4.23), gives 0.083.
  - 0.084 matches neither: it is a rounded-intermediate slip. The edition keeps the canon's numbers.

No other defect was found. Every exercise and problem answer was recomputed while drafting, and the numeric census confirms no number changed in translation.

## Coordinator addendum (2026-10-07)

After this edition was delivered the coordinator carried in the later English
canon fixes found by other editions (listed in `sources/WAVE1_FINDINGS_B34.md`
and `WAVE2_FINDINGS_B34.md`; the last ones: solutions/32 items 14-15 0.0145 and
0.083, solutions/02 gap 2047.98) and aligned the link layer with English, which
no longer links "indistinguishable" in its everyday sense (ch. 4 "from the
original/itself", ch. 10 orientations and sums). This edition now has **1787
links over 257 targets** (English 1,632 over 253); gates, dry run (0) and the
forced build re-checked. Score unchanged.

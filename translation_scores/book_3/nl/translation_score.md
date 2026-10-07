# Translation score — Chemistry Book 3 · Dutch (`nl`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 3 (University Chemistry, Year 2 — year `bachelor-2`, labels `b2`) |
| **Language** | Dutch (`nl`) |
| **Quality bar** | **native academic prose**: a Dutch-language second-year university chemistry course as it is written and taught. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **References measured before drafting** | the **English** canon (content); the shipped **Dutch Book 2** (`parts/bachelor-1/nl/`) and Dutch Book 1 for series terminology (*regel van Markovnikov*, *postulaat van Hammond*, *polariteitsinversie*, *beschermende groep*, *ontscherming*, *Dean--Stark-opvanger*, *fischerprojectie*, *standaardonzekerheid*), typography (`` `` '' `` quotes, decimal point, *Hfst.*, *publiek domein*) and the **imperative** exercise stem; `sources/TRANSLATION_BOOKS_3-4.md` |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-06 |
| **Scope** | A full first translation written directly at native register (no machine draft): 35 chapters and 35 solution twins, **70 files**. Also the Dutch image-credits page, a curated `tools/term_config/book3_nl.py`, the defined-term link layer, Dutch index keys, the overfull sweep, and this score |

## Verdict in one line

This Dutch Book 3 reads as a second-year Dutch/Flemish university chemistry
course — *reactie-enthalpie*, *gibbsenergie*, *chemische potentiaal*, *faseregel*,
*propstroomreactor*, *ellinghamdiagram*, *hefboomregel*, *stroom-potentiaalkromme*,
*overspanning*, *opofferingsanode*, *seculiere determinant*, *hückelmethode*,
*grensorbitalen*, *kristalveldstabilisatie-energie*, *oxidatieve additie*,
*whelandintermediair*, *nucleofiele acylsubstitutie*, *robinsonannulatie*,
*disconnectie*, *polymerisatiegraad*, *schotelgetal*, *stikstofregel*,
*breedbandontkoppeling*, *kwantificeringsgrens* — with imperative exercise
stems (*Bereken*, *Geef*, *Schrijf … op*, *Toon aan*, *Leg uit*) and every
structural, chemistry, prose and link gate green on a forced build:
**387 pages, 0 errors / 0 undefined / 0 overfull / 0 nullfont / 0 Missing character / 0 invalid-in-math, `.fls` = 70 files**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | All 70 files mirror their 70 twins. Counts (EN = NL): `exercise` 420, `problem` 35, `solution` 455, `omfigure` 188, `tikzpicture` 160, `definition` 197, `proposition` 176, `theorem` 37, `method` 76, `example` 36, `proof` 202, `history` 26, `safety` 14, `recall` 35, `\label` 1025, `\emph` 429, `\index` 417, `\qty` 1858, `\text` 244. Every body went through `tools/id_apply.py`; `.fls` = 70 files |
| Chemistry fidelity | **98** | `\ce` 2102 = 2102 byte-identical and in order (gate 12 OK on 70 files); `check_ce_balance.py`: 129 + 70 equations, 0 problems. Every scheme arrow label that holds words is translated (*syn-additie*, *additie*, *eliminatie*, *protonoverdracht*, *verhitten*, *katalyse*, *base*, *aldol*, *verhitten, base*), including the three that mix a word with `\ce{}` (*of*, *daarna*), once the coordinator's gate fix made their words prose. Every numeric token of every file equals its twin's (scripted census; the only differences are three rephrasings "onverzadigingsgraad 2/5") |
| Terminology | **96** | Settled per chapter in a glossary and kept consistent across the 35 chapters; Dutch eponym compounds follow Book 2's house style (single names lower-case and welded: *diels-alderreactie*, *wittigreactie*, *claisencondensatie*, *sandmeyerreactie*, *semenovdiagram*; double names as Book 2's *Dean--Stark-opvanger*: *Horner--Wadsworth--Emmons-reactie*, *Michaelis--Arbuzov-reactie*, *Wieland--Miescher-keton*; "van" forms where Dutch prefers them: *omlegging van McLafferty*, *vergelijking van Van Deemter*, *verdeling van Student*). Homographs kept apart in the wording itself: statistical "propagation" is *voortplanting van onzekerheden*, never the polymer *propagatie*. All 417 `\index{}` keys are Dutch; every accented or math key carries an ASCII sort key |
| Register / tone | **96** | Exercise stems: *Bereken*, *Geef*, *Schrijf … op*, *Teken*, *Leg uit*, *Toon aan*, *Verklaar*, the same distribution as Dutch Book 2; methods in the *je* voice; proofs as *Redenering* (Book 2's word) |
| Prose quality | **95** | Written natively; scripted sweeps for calques, doubled words, wrong *de/het* with neuter chemistry nouns, line-edge hyphens and orphaned English words. Long proofs (ch. 2, 13–16) still follow the English sentence boundaries closely |
| Link layer | **95** | **1,638 links, 180 targets** (EN 1,733 / 179): every English target reached, plus *doelmolecuul* (English never links its own "target molecule"). Idempotent: dry run "links to insert: 0", `--check` clean |
| Gates | **97** | `check_translation.sh bachelor-2 nl`: **PASSED** (gates 1–13). Build **387 pages, 0 errors / 0 undefined / 0 overfull / 0 nullfont / 0 Missing character / 0 invalid-in-math, `.fls` = 70 files** |

## Link census (curation in `tools/term_config/book3_nl.py`)

Curated from this edition's own harvest (same 196 harvested targets as English)
and per-target frequency and chapter-set censuses against the English links.
EXTRA covers the Dutch inflected adjectives (*aromatische*, *exotherme*,
*isobare diagram*, *gestabiliseerde ylide*, *tetraëdrische intermediair*…)
and the plurals WORD_TAIL cannot derive (*orbitalen*, *peroxyzuren*,
*isotopenpatronen*, *organocupraten*, *elastomeren*, *diënen*); the welded
*aldolreactie* is linked whole to the aldol definition. Masks, each a
homograph met after its definition: statistical *variantie* (ch. 29, 34),
Grignard *initiatie* (ch. 35), chromatographic *selectiviteit* (ch. 31),
spectral *resolutie* (ch. 33), the *retentiefactor $R_f$* of a TLC plate;
bare *fragment(en)* STOPped as in English.

Deficits left, all Dutch welded compounds the word boundary rightly refuses:
`chromatography:principle` 40 vs 51 (*gaschromatografie*,
*vloeistofchromatografie*), `polymer` 56 vs 65, `aldol` 38 vs 45,
`gibbs-energy` 12 vs 18 (*standaardvormingsgibbsenergie*), `saponification`
8 vs 12 (*verzepingsgetal*).

## Edits outside the patch applier (recorded)

- **`!draw` ranges:** `bachelor-2/08` EN 61; `19` EN 240; `20` EN 132–135; `23` EN 188 (*warm, geactiveerd*); `24` EN 201 (the reactivity ladder); `31` EN 78 (*begin, later, einde*).
- **Post-apply edits** (Dutch files only, after the link layer; `--check` still clean): `solutions/nl/15` pb 24 `$\boldsymbol{four}$` → `\textbf{vier}` (canon defect 2); overfull clearing in `nl/01` (a `\text{}` in the bond-enthalpy display), `nl/03`, `nl/06`, `nl/09`, `nl/10`, `nl/16`, `nl/28` (pattern table), `nl/31`, solutions 18 (`\-` hints in two complex names), 21, 25 (×2), 28, 29 (×2), 32; wording in `nl/04` and `nl/10` (*Vul … in in* → *Substitueer … in*); one line-edge rewrap in `nl/22`; two figure labels shortened after the per-figure check (`nl/31` *oplos-/middelen* box that touched its arrow, `nl/32` the drift-tube caption that crossed the grids).
- **Mirrored English-canon edits** (coordinator, 2026-10-06): solutions 01 (0.29 %, 334.5 ×3), 03 (2 % per 3 K), 07 (0.455), 11 (*bijna de helft*), 20 (*zes*, already so), 15 (`\textbf{vier}`); `nl/14` bond orders 2.5 and 2.5; `nl/32` exercise 8 (*slechts een kleine piek*); `nl/10` `\index{tegenelektrode}` joined to its word before the comma; `nl/23` keeps *1,3,5-tribroombenzeen* on one line.
- **Allow-list:** one commented, append-only `ALLOWED_BY_LANG["nl"]` entry in `tools/check_latin_prose.py` (*endo, exo, van, der, mol, ethanol, model, syn, meso*); it cleared the five blocking fragments with no change to the text.

## Suspected English-canon defects (reported, not fixed in English)

Items 1, 2, 3 and 5 below were fixed in English during the run (coordinator, 2026-10-06) and are mirrored here; 4 and 6 stand.

1. `parts/bachelor-2/solutions/17-frontier-orbitals.tex` 21–23 (exo 4): the CN carbon is said to sit "next to a ring carbon formed from the dienophile", but in cyclohex-3-ene-1-carbonitrile it **is** one of the two ring carbons formed from the dienophile. nl wrote it correctly from the start (identical to the corrected English).
2. `parts/bachelor-2/solutions/15-fragment-orbitals.tex` 116 (pb 24): `$\boldsymbol{four}$` — an English word set in math italic (and frozen by the math census in every edition). Suggest `\textbf{four}`; nl post-edited to `\textbf{vier}`.
3. `parts/bachelor-2/solutions/20-catalytic-cycles.tex` 46–47 (exo 8): "would give 18 with **seven** coordination positions" — oxidative addition of H₂ to four-coordinate [RhCl(PPh₃)₃] gives a six-coordinate octahedral complex. nl writes *zes*.
4. `parts/bachelor-2/solutions/34-measurement-statistics.tex` 84–85 (pb 10): the printed chain "(0.0010/0.00978)… ≈ 0.102 × 0.730 ≈ 0.076" is internally inconsistent (0.102 × 0.730 = 0.0745); 0.076 is right only with the unrounded s_y/x = 0.001017 (0.104 × 0.730). nl keeps the English numbers.
5. `parts/bachelor-2/25-enolates-aldol.tex` 31 and `26-conjugate-additions.tex` 94, 100: scheme arrow labels mixing a word and `\ce{}` (`[\ce{H+} or \ce{HO-}]`, `[then \ce{H2O}]`) cannot be translated without failing gate 12, so editions that followed the run file printed English "or"/"then" (reported; resolved by the gate fix, and nl now prints *of*/*daarna*).
6. Exercise 10 of ch. 30 repeats exercise 11 of ch. 24 (saponification value of triolein, same answer 190) — repetition, not an error.

## Gate / tool bugs met

- **Gate conflict on mixed arrow labels** (defect 5): `_blank_arrow_labels` blanked a label only when it held no macro, so the `chem` census and gate 12 demanded the English words byte for byte, while `check_orphan_lines.py` flagged the frozen "then" lines. Reported; fixed by the coordinator during the run. Gate 12 also prints only the first divergence per file.
- **`check_orphan_lines.py` false positive** on pgfplots option code outside a drawing environment (`\pgfplotsset{… every node near coord/.append style …}` in ch. 32, `every axis plot` in ch. 33): the ENGLISH_ONLY word "every" fired on a pgf key. Reported; fixed by the coordinator during the run (the gate now skips those bodies; the lines are byte-identical to English again).
- **`check_orphan_lines.py` passes silently on a file argument** (globs nothing under a file, prints 0, exits 0) — the defect class of the biology prose gates.
- Local TeX Live hyphenates Dutch with English patterns; the overfull sweep was done under that handicap.

## Why not 100

- **Link density** is 5 % below English, all in welded compounds.
- **Six `!draw` ranges** leave those figures guarded only by the rendered PDF.
- **Hyphenation hints** (`\-`) in two complex names and an overfull sweep under English patterns; CI's Dutch patterns can only loosen it.
- A few long proofs keep the English sentence order more closely than a Dutch author would.

## Coordinator addendum (2026-10-07)

The bare noun of the "Enolates" definition (`def:b2:enolates-aldol:enolate`) was
linked once in English and in this edition, because only the "enolate ion"
phrase was harvested; the Arabic edition exposed it. An `EXTRA` entry was added
here and in English (79 links). This edition now has **1712 links over 181
targets** (English 1,811 over 180); gates, dry run (0) and chapter-set census
re-checked. Later canon fixes carried in by the coordinator are listed in
`sources/WAVE1_FINDINGS_B34.md` and `WAVE2_FINDINGS_B34.md`. Score unchanged.

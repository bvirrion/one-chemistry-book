# Translation score — Chemistry Book 4 · Brazilian Portuguese (`pt`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 4 (University Chemistry, Year 3 — year `bachelor-3`, labels `b3`) |
| **Language** | Brazilian Portuguese (`pt`), one variety throughout |
| **Quality bar** | **native academic prose**: a Brazilian third-year university chemistry course as it is written and taught. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **References measured before drafting** | the **English** canon (content); the shipped Portuguese **Books 1–2** of this repo for series terminology and house forms (*Problema de fim de semana*, *Parte I*, the solution headers, *CCD*, *grupo protetor*); the Portuguese **Book 3** (`bachelor-2/pt`) for the cross-volume vocabulary this book recalls; the **French** Book 4 as a same-book sense reference |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-06 |
| **Scope** | A full first translation written directly at native register (no machine draft): 33 chapters and 33 solution twins, **66 files**, every one written through `tools/id_apply.py`. Also the Portuguese image-credits page, a curated `tools/term_config/book4_pt.py`, the defined-term link layer, Portuguese index keys, the overfull, page-foot and per-figure sweeps, and this score |

## Verdict in one line

This Portuguese Book 4 reads as a Brazilian third-year course in physical,
inorganic and organic chemistry: the vocabulary of Brazilian university
chemistry (*função de partição*, *representação irredutível*, *energia do
ponto zero*, *cruzamento intersistemas*, *rendimento quântico*,
*sobretensão*, *grau de recobrimento*, *banda proibida*, *adição oxidativa /
eliminação redutiva*, *conrotatório / disrotatório*, *reservatório quiral*,
*economia atômica*, *fator E*, *linha de Schlenk*), the imperative *você*
exercise stem, Brazilian spelling, and every structural, chemistry, prose and
link gate green on a forced build: **0 errors / 0 undefined / 0 overfull**,
`nullfont` and `Missing character` at the Book 4 baseline of **17**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | All 66 files mirror their 66 twins. Counts (EN = PT): `exercise` 396, `problem` 33, `solution` 429, `[resume]` 99, `omfigure` 199, `tikzpicture` 161, `axis` 108, `\node` 654, `\includegraphics` 42, `\emph` 677, `\index` 675, `\label` 1183, `\item` 1118, `\qty` 1997, `\num` 197, `\unit` 112. Environments (EN = PT): definition 323, proposition 184, theorem 65, method 89, example 53, proof 236, remark 5, recall 33, inthelab 33, history 33, safety 22, `\admitted` 16, `% ledger:` comments 167. `\cref`/`\Cref` and `\ref` targets identical (the 33 `\Cref` at a sentence start in English become `\cref` after a Portuguese article, *O \cref{…}*, which is why the case-sensitive counts differ) |
| Chemistry fidelity | **99** | `\ce` 1657 = 1657, `\chemfig` 32 = 32, `\schemestart` 13 = 13, `\ghs` 80 = 80, byte-identical in order (gate 12, chemistry twin: OK on 66 files). `check_ce_balance.py`: 104 equations, 0 problems. Never `!chem`. Arrow labels translated through the census's word-only blanking |
| Terminology | **96** | Brazilian university usage, settled per chapter and kept in one glossary (counts over course + solutions): *estado de transição* 64, *banda proibida* 26, *função de partição* 20, *economia atômica* 19, *fator E* 19, *conrotatório* 17, *rendimento quântico* 14, *energia do ponto zero* 12, *adição oxidativa* 12, *representação irredutível* 11, *teoria do estado de transição* 8, *cruzamento intersistemas* 7, *deslocamento de Stokes* 7, *eliminação redutiva* 7, *reservatório quiral* 7, *complexo ativado* 7, *tabela de caracteres* 6, *sobretensão* 5, *ciclo catalítico* 5, *linha de Schlenk* 5, *grau de recobrimento* 4, *constante rotacional* 4, *concentração micelar crítica* 3, *relógio radicalar* 3, *caderno de laboratório* 3. All 675 `\index{}` keys are Portuguese; every accented key carries an ASCII sort key. The English abbreviations the field keeps in Brazil are kept (*BOD/COD*, *PMI*, *LLS*, *HRMS*, *NOAEL/LOAEL*, *PNEC/PEC*), always expanded in Portuguese at the definition |
| Register / tone | **97** | The exercise stem is the Brazilian imperative: *Calcule* ×294, *Dê* ×68, *Escreva* ×53, *Mostre* ×40, *Explique* ×28, *Deduza* ×25, *Compare* ×25, *Verifique* ×23, *Preveja* ×20, *Estime* ×15, *Desenhe* ×11. 0 *tu*, 0 *vós*; *você* 16 times (English *you* 19). A script sweep for European-Portuguese markers (*facto, equipa, ecrã, registo, contacto, acção, objecto, electr-, secção, protões, iões, catião, anião, -génio, fenómeno, estar a + infinitive*) over course **and** solutions finds 0 outside labels and file names. Cross-volume references read *o volume do 1.º ano / do 2.º ano*; no programme is ever named |
| LaTeX hygiene | **99** | Final forced build through the shared `build.sh` wrapper: **rc 0, 0 errors, 0 undefined, 0 overfull, `invalid in math mode` 0, `nullfont` 17 and `Missing character` 17 (the Book 4 baseline, same as English)**, **419 pages** (English 405). `.fls`: **66** Portuguese sources. Valid UTF-8, 0 TeX accent escapes, no line starting on `. , ; : ) ? !`. Overfull boxes from the early builds (3, then 4 hbox + 1 vbox) were all cleared by rewording, never with `%`. **Page-foot sweep:** every page with four lines or fewer was listed; two pages carried only a section heading because the unbreakable weekend-problem box no longer fitted under it (`pt/04` methane, `pt/31` ibuprofen); both problems were tightened by a few words (title, data paragraph, three items each) so heading and box now share a page, as in English. The ch. 26 problem had been tightened the same way earlier |
| Cross-refs / rule compliance | **98** | Labels, solution keys, `[resume]`, math spans, image paths and `% ledger:` comments are byte-identical to English. No programme, curriculum, country or university name in visible text. No English source, other edition or shared tool was touched; no allow-list entry was needed. No repo-wide git command, no commit, no subagent |
| Figures | **96** | All TikZ / pgfplots / chemfig code is byte-identical except seven `!draw` ranges (below). Only node text, axis labels, legends, tick labels, table cells and captions were localized. **Per-figure check:** the 147 figures whose drawing text was translated (140 found by the scripted list, 7 more after the list learned to split a `{\small` caption after a blank line) were rendered one page per figure at 130 dpi, about 120 pages, and read; every fixed figure was re-rendered from the final build or a single-chapter probe and read again. **Twenty-three collisions were found and fixed, all by label text only** (line breaks, `\shortstack`, size, a leading `\hspace*`, shorter wording), never by moving a coordinate: *retorno* (ch. 1), the two *(de cima)* labels (ch. 4), the water-mode labels (ch. 5), *fund.* (ch. 7), *transl.* (ch. 11), *mistura* (ch. 13), *encontro* (ch. 16), *cilindro (de lado)* (ch. 17), the ruby/emerald photo labels over their caption (ch. 18, by `[b]` minipages), *inclinação 2.7* (ch. 24), *25 °C (mais baixa)* clipped at the axis (ch. 28), the pyridine NMR label clipped at the axis (ch. 29), *iodolactonização / Baeyer–Villiger* and the *trans*-diamine box (ch. 30), the raw-material and end-of-life boxes and the ammonia converter box (ch. 31), *saturado*, the fields box and *escoamento* (ch. 32), the two characterisation-flow boxes (ch. 33) |
| Solutions | **97** | All 396 exercise solutions and 33 weekend-problem solutions present. Numbers were recomputed while translating; multi-line math spans keep their English line breaks, as `id_apply`'s math census requires. Gate 11 (problem numbering) green |
| Defined-term links (`\omterm`) | **95** | **1755 links over 258 distinct targets**, against English's **1632 over 252**. **Every target English links is reached** (0 missed). Portuguese also reaches six English never links, each read in context and in the defined sense: *volume de ativação* ×5 (ch. 19 + sol. 19), *Hartree–Fock* ×2, *spin-crossover* ×2, *tipos de gap* ×2, *difração de pó* ×1, *agóstica* ×1. `book4_pt.py` was curated from this edition's own harvest (670 terms, 762 linkable after the irregular plurals and gender forms), never seeded. `--unwrap --apply` then `--apply` leaves the plain dry run at **links to insert: 0**. The largest positive differences are the defined sense: *energia(s) do ponto zero* +22 (Portuguese repeats the noun and has a plural English never matches), *banda proibida* +16 (English writes *gap* in prose), *degenerescência(s)* +9 |
| MT-artifact freedom | **96** | Gate 10 (orphan lines): **0**. Gate 9 (twin prose comparison): **0 multi-word findings**, 36 advisory one-word findings, all read: eponyms (*Slater, Rayleigh, Stokes, Chapman, Hohenberg–Kohn, Cope, Claisen*), cognates (*linear, virtual, vertical, metal, total, Spin-orbital*), symbols and units (`$[Q]$ / mol L$^{-1}$`, `$\delta_{\mathrm H}$ / ppm`) and the abbreviations *org*, *equiv.* |

**Overall: 96.** The weighting favours terminology, register, link curation and MT-artifact freedom; structure and build are gated mechanically.

## Gate output summary

```
bash tools/check_translation.sh bachelor-3 pt ............ TRANSLATION GATE: PASSED
  gates 1-8, 10, 11, 13 .... green (completeness, structure, hygiene, UTF-8,
                             orphan lines 0, problem numbering, ce balance)
  gate 9 ................... no multi-word findings; 36 one-word (advisory, cognates)
  gate 12 .................. chemistry twin gate: OK (66 files)
python3 tools/check_orphan_lines.py parts/bachelor-3/pt parts/bachelor-3/solutions/pt   0
python3 tools/check_ce_balance.py   parts/bachelor-3/pt parts/bachelor-3/solutions/pt   104 equations, 0 problems

final forced build (scratchpad build.sh, one_chemistry_book_4_university_year_3_pt)
  rc 0 · pages 419 (EN 405) · errors 0 · undefined 0 · overfull 0
  nullfont 17 · Missing character 17 (Book 4 baseline) · invalid in math mode 0
  .fls Portuguese sources 66

python3 tools/link_defined_terms.py --book 4 --lang pt     -> links to insert: 0
\omterm 1755 links / 258 targets (EN 1632 / 252), 0 English targets missed
```

## The link layer: what the censuses found

Portuguese homographs met **after** their definition, each masked in
`book4_pt.py` (`EXTRA_PROTECT`) with its evidence:

- ***caráter / caracteres*** is both the group-theory CHARACTER (ch. 4–5) and
  ordinary "character": *caráter ímpar*, *caráter de ruptura*, *caráter s*,
  *caráter $…$*, and the *caracteres singleto / tripleto* of ch. 7.
- ***população*** (Boltzmann population) vs a toxicology *população de teste*
  and *populações densas*.
- ***operador*** (quantum operator) vs the plant operator (*operadores
  treinados*, *o operador trabalha*, *operadores usam*).
- ***sol*** (the colloid, ch. 17) vs the sun (*raios de sol*, *luz do sol*,
  *ao sol*, *Sol, pele*).
- ***migração*** (migratory insertion) vs a group *migração* in a
  rearrangement, ***buraco*** (positive hole) vs the *buraco do anel*, and
  ***indistinguível*** where it means "the same as" a sum.

Forms the harvest cannot derive, added to `DERIVED` and kept only where the
form occurs: the irregular plurals in *-ção → -ções*, *-al → -ais*, *-el →
-eis*, *-il → -is* (*representações irredutíveis*, *operações de simetria*,
*integrais de troca*, *funções de partição moleculares*, *reações
pericíclicas*…); the gender forms *conrotatória*, *disrotatória*, *ativa no
IV / no Raman*; and *isolobais*, *indistinguíveis*, *lábeis*, *pró-quirais*.

## Edits outside the patch applier (recorded)

- **`!draw` ranges, seven** (English line numbers): `bachelor-3/05` 271 (the
  `\foreach` of mode labels, applied as 273), `/08` 315, `/09` 77, `/22` 126,
  `/24` 106, `/26` 179, `/33` 413. A range at `/26` 362 was prepared and not
  needed (*Cope / Claisen* are the same in Portuguese).
- **Figure label fixes after application**, all text-only, listed under
  *Figures* above.
- **Overfull and page-foot clearing** by rewording: the early overfull boxes,
  and the weekend problems of ch. 4, 26 and 31 tightened so the unbreakable
  box shares a page with its heading.
- **`\index` line ends:** three `\emph{…}` followed by an `\index` on the next
  line received a trailing `%` (ch. 27 ×2, ch. 28), so no space is printed
  before the comma.

## Suspected English-canon defects (reported, not fixed)

1. `parts/bachelor-3/10-partition-functions.tex`, line 405: `\omterm{def:b3:many-electron-atoms:indistinguishable}{indistinguishable}` links the everyday sense ("is indistinguishable from the sum above about 30 K", i.e. numerically equal) to the quantum-indistinguishability definition. Portuguese masks it.
2. `parts/bachelor-3/30-total-synthesis.tex`, line 323: "but the area that removes it only with its square of the size" — garbled wording (meaning: the cooling area grows only as the square of the size). Portuguese renders the intended sense.
3. `parts/bachelor-3/11-statistical-thermo-applied.tex`, line 115 (layout): the node `$\frac32$: translation` at `(axis cs:10.5,1.5)` is crossed by the equilibrium-H₂ curve in the English PDF; Portuguese shortened it to *transl.*
4. `parts/bachelor-3/29-heterocycles.tex`, line 119 (layout): the node `pyridine: H2/6, H4, H3/5 (2\,:\,1\,:\,2)` runs past the axis and is clipped in the English PDF (p. 287 shows "pyridine: H2/6, H4, H3"); Portuguese breaks it over two lines.
5. `parts/bachelor-3/18-complex-spectra-magnetism.tex`, lines 30–37 (layout, latent): the ruby/emerald photos sit in `[t]` minipages inside `omfigure`'s `[b]` minipage, so the labels' depth is not counted and they nearly touch the caption in English (p. 178); in Portuguese they overprinted it. `[b]` minipages fix it.

## Gate / tool bugs met

None in the shared tools for this run, and no allow-list entry was added. One
note for the scratch tooling only: a figure list built by splitting the
`omfigure` body on the first blank line misses figures whose drawing itself
contains a `{\small …}` title; splitting on blank line + `{\small` found seven
more figures to check.

## Why not 100

- **Seven `!draw` ranges** leave those figures guarded only by the rendered PDF (all re-rendered and read).
- **Link density is +7.5 %** against English (1755 vs 1632), mostly plurals and repeated nouns English never matches; every high-ratio target was read.
- **Three weekend problems were tightened** by a few words to keep heading and box on one page; no question was dropped, but the wording is slightly terser than English there.
- **Register is measured, not perfect.** Stems, variety markers and spelling were audited by script; some long proofs still follow the English sentence boundaries more closely than a Brazilian author would.

## Coordinator addendum (2026-10-07)

After this edition was delivered the coordinator carried in the later English
canon fixes found by other editions (listed in `sources/WAVE1_FINDINGS_B34.md`
and `WAVE2_FINDINGS_B34.md`; the last ones: solutions/32 items 14-15 0.0145 and
0.083, solutions/02 gap 2047.98) and aligned the link layer with English, which
no longer links "indistinguishable" in its everyday sense (ch. 4 "from the
original/itself", ch. 10 orientations and sums). This edition now has **1751
links over 258 targets** (English 1,632 over 253); gates, dry run (0) and the
forced build re-checked. Score unchanged.

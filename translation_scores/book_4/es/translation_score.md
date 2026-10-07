# Translation score — Chemistry Book 4 · Spanish (`es`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 4 (University Chemistry, Year 3 — years `bachelor-3`, labels `b3`) |
| **Language** | Spanish (`es`) |
| **Quality bar** | **native academic prose**: a third-year university chemistry course in Spanish as it is written and lectured. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **References measured before drafting** | the **English** canon (content); the shipped Spanish Books 1–3 of this repo for series terminology and the impersonal *-se* exercise stem (*Calcúlese*, *Demuéstrese*, *Escríbanse*); IUPAC Spanish nomenclature; `sources/TRANSLATION_BOOKS_3-4.md` and its reading list |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-06 |
| **Scope** | A full first translation written directly at native register (no machine draft): 33 chapters and 33 solution twins, **66 files**, every body through `tools/id_apply.py`. Also the Spanish image-credits page, a curated `tools/term_config/book4_es.py`, the defined-term link layer, Spanish index keys, the overfull and per-figure sweeps, and this score |

## Verdict in one line

A Spanish Book 4 that reads as a third-year Spanish university chemistry
course — *función propia*, *operador hermítico*, *energía de punto cero*,
*determinante de Slater*, *símbolo de término*, *superficie de energía
potencial*, *función de base*, *campo autoconsistente*, *grupo puntual*,
*representación irreducible*, *tabla de caracteres*, *banda caliente*,
*cruce entre sistemas*, *red recíproca*, *función de partición*, *complejo
activado*, *frecuencia de recambio*, *corriente de intercambio*, *concentración
micelar crítica*, *efecto trans*, *síntesis con plantilla*, *retrosíntesis*,
*economía atómica*, *DBO / DQO*, *DL50 / CE50*, *línea de Schlenk*, *caja de
guantes* — with every structural, chemistry, prose and link gate green on a
forced build of **0 errors / 0 undefined / 0 overfull**, `nullfont` 17 and
`Missing character` 17 (both the English baseline).

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | All 66 files mirror their twins. Counts (EN = ES): `exercise` 396, `problem` 33, `solution` 429, `[resume]` 99, `omfigure` 199, `tikzpicture` 161, `axis` 108, `\node` 654, `\includegraphics` 42, `\chemfig` 32, `\ce{` 1657, `\arrow` 16, `\cref`+`\Cref` 205, `\label` 1183, `\item` 1118, `\section` 261, `\begin`/`\end` 2723, `\qty` 1998, `\num` 197, `definition` 323, `proposition` 184, `method` 89, `example` 53, `proof` 236, `\emph` 677, `\index` 675, `% ledger:` 167; blank lines equal file by file |
| Chemistry fidelity | **99** | Every `\ce`, `\chemfig`, scheme and `\ghs` byte-identical (gate 12: chemistry twin OK on 66 files; gate 13 green). Never `!chem`. Arrow labels translated (`->[$\ce{CH2}$ singlete]`, `->[$\ce{H2SO4}$ (óleum)][Beckmann]`, `->[$h\nu$][vía $\mathrm T_1$]`, `[ciclación, $-\ce{NH3}$]`) |
| Terminology | **96** | One choice per notion held across the book: *tiempo de semirreacción* (half-life), *ammina/ammínico* (the Book 2 es convention for the NH3 ligand), *degeneración*, *contribución orbital*, *razón nefelauxética*, *transferencia de carga*, *volumen de activación*, *cuasirreversible*, *hueco* (semiconductor), *acervo quiral*, *auxiliar quiral*, *resolución cinética*, *relación enantiomérica*, *bioisóstero*, *secuencia lineal más larga*, *idealidad*, *análisis del ciclo de vida*, *límite del sistema*. Math-mode labels localized after the patch (`\mathrm{nulo}`, `\text{cte}`, `\text{patrón}`, `k_{\text{rápida}}`, `\mathrm{DBO_5}`, `\mathrm{DL_{50}}`, `\mathrm{FBC}`, `C_{\mathrm{suelo}}`). All 675 index keys in Spanish, accented keys with ASCII sort keys |
| Register / tone | **96** | Exercise and problem stems in the impersonal *-se*: *Calcúlese* ×215, *Calcúlense* ×70, *Demuéstrese* ×38, *Enúnciese* ×33, *Dese/Dense* ×66, *Escríbase/Escríbanse* ×40, *Explíquese* ×27, *Dedúzcase* ×22, *Dibújese/Dibújense* ×10; **0** *usted* and **0** *tú* imperatives. Course text impersonal |
| LaTeX hygiene | **99** | Forced build: **0 errors, 0 undefined, 0 overfull, 0 `invalid in math mode`**, `nullfont` 17 and `Missing character` 17 (English baseline: the backticks of ch. 12), **425 pp** (English 405), `.fls` Spanish sources **66**, English chapter files **0**. Eleven overfull boxes on the first build, all cleared by rewording; the last, a weekend-problem box of ch. 26 taller than its page (heading orphaned on the page before), by tightening four items |
| Figures | **96** | Drawing code byte-identical except seven deliberate `!draw` ranges (05/271, 08/315, 09/77, 22/126, 24/106, 26/179, 33/413) and four more for Spanish label room (13/567 mixer label, 29/119-121 later aligned on the English fix, 30/264-270 and 30/292-298 node positions). Every figure page rendered at 130 dpi and read; collisions found and fixed: ch. 1 *retroceso*, ch. 3 flow-chart nodes, ch. 7 *básico*, ch. 13 mixer label, ch. 16 volcano labels, ch. 17 cylinder label, ch. 22 band labels, ch. 29 pyridine label, ch. 30 two route charts, ch. 31 life-cycle boxes, ch. 32 nutrient-flow boxes. A bbox overlap scan of the final PDF: 0 hits |
| Solutions | **96** | All 396 exercise and 33 problem solutions present and native; chapters 18–33 recomputed while translating; the English canon edits of 2026-10-06 mirrored (02 1.65 and A = 11.47; 06 R(0) = 2905.58; sol. 08 item 11; sol. 10 ex. 1 wording; sol. 15 b²S_xx = 203.5; 11, 18, 29 figure fixes; 30 the restored verb) |
| Defined-term links (`\omterm`) | **96** | **1777 links over 256 targets** against English's **1629 over 252**: every English target reached, plus four English never links (*volumen de activación* 5, *transición de espín* 2, *campo autoconsistente* 2, *bandas prohibidas directas/indirectas* 2). `--apply` twice changes nothing; dry run **links to insert: 0**. 29 `DERIVED` accent-shift plurals, 2 `EXTRA`, 12 `EXTRA_PROTECT` patterns for the homographs below |
| MT-artifact freedom | **96** | Gate 10: **0 orphan lines**. Latin prose gate: **0 multi-word findings**; 34 advisory one-word hits read, all correct Spanish (cognates, eponyms, units, symbols) |

**Overall: 96.**

## Gate output summary

```
bash tools/check_translation.sh bachelor-3 es        TRANSLATION GATE: PASSED
  gates 1-13; chemistry twin gate OK (66 files)
  latin prose gate: no multi-word findings; 34 one-word advisory hits, read

build/one_chemistry_book_4_university_year_3_es.log (grep -a)
  '^!' 0 · undefined 0 · Overfull 0 · invalid in math mode 0
  nullfont 17 · Missing character 17 (English baseline)
  pages 425 (English 405) · .fls Spanish sources 66 · English sources 0

python3 tools/link_defined_terms.py --book 4 --lang es    links to insert: 0
```

## Homographs handled in `book4_es.py`

*carácter* (of a representation / *carácter s*, *singlete*, *impar*, *de
ruptura*), *hueco* (semiconductor hole / the hole of a glass network or of the
porphyrin ring), *población* (Boltzmann population / a test population, algal
populations), *sol* (colloid / the sun), *operador* (quantum operator / a
laboratory operator), *producto directo* (of representations / the uncyclised
product of a radical clock, ch. 27), *indistinguibles* (identical particles /
"indistinguishable from the starting orientation", ch. 10), plus masks for
`\setchemfig`, chemfig arrow labels and pgfplots tick labels.

## Coordinator addendum (2026-10-07)

After this edition was delivered the coordinator carried in the later English
canon fixes found by other editions (listed in `sources/WAVE1_FINDINGS_B34.md`
and `WAVE2_FINDINGS_B34.md`; the last ones: solutions/32 items 14-15 0.0145 and
0.083, solutions/02 gap 2047.98) and aligned the link layer with English, which
no longer links "indistinguishable" in its everyday sense (ch. 4 "from the
original/itself", ch. 10 orientations and sums). This edition now has **1777
links over 256 targets** (English 1,632 over 253); gates, dry run (0) and the
forced build re-checked. Score unchanged.

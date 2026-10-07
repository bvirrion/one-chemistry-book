# Translation score — Chemistry Book 3 · Spanish (`es`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 3 (University Chemistry, Year 2) — `bachelor-2` |
| **Language** | Spanish (`es`) |
| **Quality bar** | **native academic prose** — a second-year university chemistry course in Spanish as it is actually written and lectured. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Register references** | the **English** canon (content); the Spanish Book 2 edition (`book_2/es`) for every shared term and house form; the impersonal *-se* exercise stem; IUPAC Spanish nomenclature (*but-3-en-2-ona*, *etanoato de etilo*, *hidróxido de sodio*) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-06 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 35 chapters + 35 solution twins = **70 files**, all written through `tools/id_apply.py`; a curated `tools/term_config/book3_es.py`; the defined-term link layer; Spanish index keys; the Spanish image-credits page; the overfull and figure sweeps; this score |

## Verdict in one line

A Spanish Book 3 that reads as a second-year Spanish university chemistry
course — *magnitud de reacción*, *potencial químico*, *regla de las fases*,
*diagrama de Ellingham*, *curva intensidad--potencial*, *sobretensión*,
*método CLOA*, *orbitales frontera*, *serie espectroquímica*, *adición
oxidante*, *intermedio de Wheland*, *aminación reductora*, *sustitución
nucleófila de acilo*, *condensación aldólica*, *anulación de Robinson*,
*iluro estabilizado*, *desconexión* y *sintón*, *polimerización por etapas*,
*factor de retención*, *regla del nitrógeno*, *desviación típica de la media*,
*tratamiento final* — with every structural, prose, chemistry and link gate
green on a forced build of **0 errors / 0 undefined / 0 overfull / 0 nullfont**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Counted over all 70 files against their twins, all exact: **420 `exercise`**, **35 `problem`**, **455 `\begin{solution}`**, **105 `[resume]`**, **188 `omfigure`**, **160 `tikzpicture`**, **84 `axis`**, **585 `\node`**, **64 `\includegraphics`**, **102 `\chemfig`**, **2102 `\ce{`**, **39 `\arrow`**, **1025 `\label`**, **1170 `\item`**, **1858 `\qty`**, **24 `\num`**, **197 `definition`**, **176 `proposition`**, **37 `theorem`**, **76 `method`**, **36 `example`**, **202 `proof`**, **429 `\emph`**, **417 `\index`** (`\cref` 141 vs 140: one `\Cref … to \cref` became *Del `\cref` al `\cref`*) |
| Terminology | **96** | One choice per notion, held across the book and aligned with the Spanish Book 2 edition (*halogenoalcano*, *reactivo de Grignard*, *organomagnesiano*, *aparato de Dean--Stark*, *RMN*, *regla $n + 1$*, *cuadruplete (c)*, *sextuplete*). Notable choices: *magnitud de reacción*; *varianza* (phase rule) kept apart from the statistical *varianza* by link masks; *cromatografía líquida de alta eficacia* (not *de alta resolución*, to keep *resolución* for the chromatographic quantity); *perfil isotópico* (not *patrón*, which is the *patrón interno*); *tratamiento final* (work-up), *agente desecante*, *borboteador*, *embudo de decantación*; *ion dipolar* (zwitterion); *base nitrogenada*; *interconversión de grupos funcionales (IGF)*; *poder de resolución*. All 417 index keys in Spanish with ASCII sort keys |
| Register / tone | **96** | Exercise and problem stems in the impersonal *-se*: *Calcúlese* ×212, *Calcúlense* ×67, *Escríbase* ×69, *Escríbanse* ×20, *Explíquese* ×52, *Demuéstrese* ×17, *Dese/Dense* ×62, *Dibújese/Dibújense* ×40, *Propóngase* ×21, *Indíquese* ×31 …; script audit **0** *usted* and **0** *tú* imperatives. House forms *Problema de fin de semana --- …*, *Parte I --- …*, `\section*{Capítulo \ref{…} --- …}`, *el volumen del primer/tercer año*, *el volumen escolar*. Article agreement before every `\cref` checked by script (Capítulo, Método, Teorema masc.; Proposición, Definición fem.) |
| LaTeX hygiene | **99** | Forced build: **0 errors, 0 undefined, 0 overfull, 0 `nullfont`, 0 *Missing character*, 0 *invalid in math mode***, **389 pp** (English 373); `.fls` Spanish sources **70**, English chapter files pulled in **0**. Thirteen overfull boxes met on the way (long inline formulas, unbreakable `\ce` chains, one table) all cleared by rewording, never by touching code. Sweeps: no line-end word hyphen, no line-start punctuation, no straight double quote, no `...`, no repeated word |
| Cross-refs / rule compliance | **98** | Labels, `\cref` targets, solution keys, `[resume]`, math spans, image paths, every `\ce`/`\chemfig`/scheme and every `% ledger:` comment byte-identical (gate 12 green). No programme or country named. Shared files touched: `tools/check_latin_prose.py` (one append-only, commented es entry, *endo*, *exo*), this edition's term config, credits page and score. No git write. Deliberate divergences recorded below |
| Figures | **95** | Drawing code byte-identical; node text, axis labels, legends, tick labels, word-only arrow labels and captions localised. `!draw` used five times, always on a `\foreach` label list and never on coordinates: ch. 08 EN 61, ch. 19 EN 240 (visible colour names only, keys untouched), ch. 20 EN 131--135, ch. 23 EN 188, ch. 31 EN 78. Pages with long Spanish labels rendered and read; two collisions fixed (ch. 32 drift-tube label over *rejillas*; ch. 35 wash labels over the boxes). Mixed arrow labels translated (*o*, *luego*) |
| Solutions | **97** | All 420 exercise and 35 problem solutions present and native; problem chains recomputed while translating (Carothers, Flory, Wieland--Miescher mass balance, lead calibration, caffeine by internal standard, Grignard heat and purity-corrected yield, McLafferty and isotope patterns). Canon defects found are listed below; the one with a printed wrong value in a body text (ch. 14) is corrected in Spanish |
| Defined-term links (`\omterm`) | **96** | **1781 links over 183 targets** against English's **1733 over 179** — every English target reached, plus four the Spanish text names where English rephrases (*análisis retrosintético*/*molécula objetivo*, *muro del disolvente*, *desplazamiento del equilibrio*, *entalpía estándar de formación*). Dry run **links to insert: 0**; `--check` clean. Curated from this edition's harvest: `STOP` *fragmento(s)* (as English), `EXTRA` *aldólica(s)*, 16 `DERIVED` plurals and genders (*órdenes de enlace*, *sobretensiones*, *paramagnético*, *exotérmico*, *aromática*, *isotáctico* …), 20 `EXTRA_PROTECT` patterns for the homographs below |
| MT-artifact freedom | **96** | Gate 10: **0 orphan lines** (no workaround left). Gate 9: **0 blocking findings**; 111 advisory one-word hits, read: symbol subscripts identical by convention (*fus*, *vap*, *trs*, *corr*, *cat*, *Red*), proper names (Raoult, Henry, Carnot, Wheland), Latin and cognates (*liquidus*, *solidus*, *metal*, *detector*, *gases*, *normal*, *base*) |

**Overall: 96.**

## Gate output summary

```
bash tools/check_translation.sh bachelor-2 es        TRANSLATION GATE: PASSED
  gate 9 ................. no multi-word findings (111 advisory one-word hits, read)
  gate 10 orphan lines ... 0
  gate 12 chemistry twin . OK (70 files)

build/one_chemistry_book_3_university_year_2_es.log (grep -a)
  '^!' 0 · undefined 0 · Overfull 0 · nullfont 0 · Missing character 0 · invalid in math mode 0
  pages 389 (English 373) · .fls Spanish sources 70 · English chapter sources 0

python3 tools/link_defined_terms.py --book 3 --lang es    links to insert: 0
```

## Homographs handled in `book3_es.py`

*fragmento(s)* (ch. 15 method / ozonolysis, MS and retrosynthetic fragments),
*varianza* (phase rule / statistics), *propagación* (chain step / uncertainty),
*iniciación* (radical / Grignard start), *selectividad* (reactor /
chromatographic factor), *resolución* (chromatographic / resolving power,
spectral resolution, solving a structure), *residuos* (calibration residuals /
waste), and the TLC $R_f$ kept apart from the column's factor de retención.

## Deliberate divergences from the English twin

None remain after the coordinator's follow-up (2026-10-06):

- The mixed arrow labels are translated now that `id_apply` and gate 12 freeze
  only the `\ce{}`/`$…$` parts of a label: ch. 25 EN 31 `[\ce{H+} o \ce{HO-}]`,
  ch. 26 EN 94, 100 `[luego \ce{H2O}]`, each `\arrow` back on its own line as in
  English. The `\pgfplotsset` bodies of ch. 32/33 are back in the English layout
  (gate 10 now skips them).
- The English canon now carries the fixes this edition had found or made
  locally (`solutions/15` `\textbf{four}`, ch. 14 bond orders 2.5 and 2.5,
  ch. 23 one-line *1,3,5-tribromobenceno*), so the Spanish files simply follow
  their twins. The other canon corrections are mirrored: `solutions/11` item 7
  (*casi la mitad del trabajo*), `solutions/20` exercise 8 (*seis* posiciones),
  ch. 10 `\emph{contraelectrodo}\index{contraelectrodo},` on one line, ch. 32
  exercise 8 (*solo muestra un pequeño pico en 58*), `solutions/07` item 12
  (0.455), `solutions/01` (0.29 %, 334.5 at three sites), `solutions/03` item
  10 (*un 2 % cada 3 K*).
- Kept by choice: ch. 01 `\Delta_{\text{ret}}H` (*reticular*) for the
  English `\text{lat}`.

## Coordinator addendum (2026-10-07)

The bare noun of the "Enolates" definition (`def:b2:enolates-aldol:enolate`) was
linked once in English and in this edition, because only the "enolate ion"
phrase was harvested; the Arabic edition exposed it. An `EXTRA` entry was added
here and in English (79 links). This edition now has **1858 links over 184
targets** (English 1,811 over 180); gates, dry run (0) and chapter-set census
re-checked. Later canon fixes carried in by the coordinator are listed in
`sources/WAVE1_FINDINGS_B34.md` and `WAVE2_FINDINGS_B34.md`. Score unchanged.

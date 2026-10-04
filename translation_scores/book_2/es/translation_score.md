# Translation score — Chemistry Book 2 · Spanish (`es`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 2 (University Chemistry, Year 1) — `bachelor-1` |
| **Language** | Spanish (`es`) |
| **Quality bar** | **native academic prose** — a first-year university chemistry course in Spanish as it is actually written and lectured. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Register references** | the **English** canon (content); the impersonal *-se* exercise stem (*Calcúlese*, *Escríbanse*, *Demuéstrese*) of the Spanish university-year editions of the sibling series; IUPAC Spanish nomenclature (*propan-2-ol*, *etanoato de etilo*, *hidróxido de sodio*) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-04 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 29 chapters + 29 solution twins = **58 files**, all written through `tools/id_apply.py`; a curated `tools/term_config/book2_es.py`; the defined-term link layer; Spanish index keys; the Spanish image-credits page; the overfull and per-figure sweeps; this score |

## Verdict in one line

A Spanish Book 2 that reads as a first-year Spanish university chemistry
course — *número cuántico azimutal*, *carga nuclear efectiva*, *modelo RPECV*,
*avance de la reacción*, *tiempo de semirreacción*, *aproximación del estado
estacionario*, *disolución tampón*, *ecuación de Nernst*, *diagrama
potencial--pH*, *proyección de Newman*, *sustitución nucleófila*, *reactivo de
Grignard*, *síntesis de Williamson*, *grupo protector*, *proceso Solvay*,
*incertidumbre típica* — with every structural, prose, chemistry and link gate
green on a forced build of **0 errors / 0 undefined / 0 overfull / 0 nullfont**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Counted over all 58 files against their twins, all exact: **348 `exercise`**, **29 `problem`**, **377 `\begin{solution}`**, **87 `[resume]`**, **148 `omfigure`**, **96 `tikzpicture`**, **47 `axis`**, **587 `\node`**, **49 `\includegraphics`**, **101 `\chemfig`**, **3432 `\ce{`**, **34 `\arrow`**, **221 `\cref`**, **829 `\label`** (set diff 0), **916 `\item`**, **1475 `\qty`**, **67 `\num`**, **162 `definition`**, **128 `proposition`**, **52 `method`**, **60 `example`**, **109 `proof`**, **390 `\emph`**, **364 `\index`** |
| Terminology | **96** | Standard Spanish university chemistry, one choice per notion held across the book (glossary in the agent's notes): *efecto pantalla* (screening) kept apart from the NMR *apantallamiento*; *tiempo de semirreacción* (not *periodo*, which is the row of the table); *par no enlazante*, *forma resonante*, *número estérico*; *celda unidad*, *multiplicidad*, *compacidad*, *hueco octaédrico/tetraédrico*; *grado de avance final*, *reactivo limitante*; *anfolito*, *efecto nivelador*, *diagrama de predominio*; *semipila*, *puente salino*, *electrodo estándar de hidrógeno (EEH)*; *diastereoisómeros*, *compuesto meso*, *conformación alternada/eclipsada*, *inversión del anillo*; *desplazamiento químico*, *constante de acoplamiento*, *regla $n+1$*; *carbocatión*, *grupo saliente*, *inversión de Walden*, *regla de Zaitsev*; *pictograma de peligro*, *palabra de advertencia* (*Peligro*/*Atención*), *indicación de peligro*, *consejo de prudencia*, *ficha de datos de seguridad*; *evaluación de tipo A/B*, *incertidumbre expandida*, *desviación normalizada*. All 364 index keys rewritten in Spanish with ASCII sort keys (`\index{configuracion electronica@configuración electrónica}`) |
| Register / tone | **96** | Exercise and problem stems in the impersonal *-se* (*Calcúlese* ×157, *Escríbase* ×93, *Escríbanse* ×36, *Explíquese* ×54, *Demuéstrese* ×45, *Dese/Dense* ×65, *Dibújese* ×33 …); script audit: **0** *usted* imperatives (*Calcule*, *Escriba*, *Explique* …), **0** *tú* imperatives. Course text impersonal; house forms *Problema de fin de semana --- …*, *Parte I --- …*, solutions header `\section*{Capítulo \ref{…} --- …}`. (The recall-box title *Lo que ya sabes* is a shared string owned by the Book 1 `es` agent) |
| LaTeX hygiene | **99** | Forced build: **0 errors, 0 undefined, 0 overfull, 0 `nullfont`, 0 `invalid in math mode`**, 304 pp (English 293), `.fls` Spanish sources **58**, English chapter files pulled in **0**. Eight overfull boxes met on the way (seven text, one flow sheet) were all cleared by rewording or shortening labels, never by touching code. Sweeps after the link layer: no line-end quote, no line-start punctuation, no line-end word hyphen, no non-ASCII index key, no non-ASCII inside `\qty`/`\unit`/`\num`/`\ce` |
| Cross-refs / rule compliance | **99** | Labels, `\cref` targets, solution keys, `[resume]`, math spans, image paths, every `\ce`/`\chemfig`/scheme and every `% ledger:` comment byte-identical (gate 12 green). No programme or country named. No English or other-edition file touched; shared files edited only `tools/check_latin_prose.py` (append-only, reasoned) and this edition's own term config and credits page. No git write, no commit |
| Figures | **96** | Drawing code byte-identical; only node text, axis labels, legends, `yticklabels`, arrow labels and captions localized. `!draw` used twice (`\foreach` label lists: ch. 16 EN 199, ch. 17 EN 68). ~75 figures with prose labels rendered and read page by page; nine Spanish label collisions found and fixed by shorter wording (ion-hydration captions, steady-state label, ring-flip arrow, 1,2-shift arrow, Solvay and Ostwald flow-sheet boxes, contact-process labels, condenser labels). One collision is inherited from English (ch. 8 tangent label over the y-axis title) and reported |
| Solutions | **97** | All 348 exercise and 29 problem solutions present and native; chapters 23–29 recomputed while translating (every problem chain re-derived: Solvay, Bayer, Haber/Ostwald, contact process, Dean--Stark volumes, sulfuric-acid second acidity, extraction limits, uncertainty budgets) — no defect found in those chapters |
| Defined-term links (`\omterm`) | **96** | **2592 links over 146 targets** against English's **2470 over 144** — every English target reached, plus two English never links (*síntesis de Williamson*, *efecto nivelador*) where the Spanish text names the defined notion. `--apply` twice changes nothing; dry run **links to insert: 0**. Curated from this edition's own harvest (389 → 422 linkable terms): `DROP` of the bare *fuerte/débil*, 33 `DERIVED` plurals and genders the tail cannot reach (*electrón → electrones*, *carbocatión → carbocationes*, *hidrófilo → hidrófila* …), `NO_CAPITAL` for *Red* (the reduced form, Ox/Red), and 20 `EXTRA_PROTECT` patterns for the Spanish homographs (see below). Both censuses run after the last edit |
| MT-artifact freedom | **96** | Gate 10: **0 orphan lines**. Gate 9: **0 blocking findings**; 23 advisory one-word hits, all correct Spanish (Lyman, Balmer, Paschen, Fischer, Cram, *gauche*, *anti*, *axial*, *acetal*, *bases*, Pauling, `$\delta$ (ppm)`, *inv*/*ret* abbreviations). `\text{}` census in course and solutions: all Spanish (`\text{sup}`, `\text{inf}`, `\text{ne}`, `\text{enl}`, `\text{semipila}`, `\text{EEH}`, `\text{aldehído}`, `\text{alícuota}` …) |

**Overall: 96.**

## Gate output summary

```
bash tools/check_translation.sh bachelor-1 es        TRANSLATION GATE: PASSED
  gates 1-13 (completeness, structure, hygiene, UTF-8, twin prose gate,
  orphan lines, problem numbering, chemistry twin + ledger ids, ce balance)
  gate 9 advisory ........ 23 one-word hits, read, all correct Spanish

build/one_chemistry_book_2_university_year_1_es.log (grep -a)
  '^!' 0 · undefined 0 · Overfull 0 · nullfont 0 · invalid in math mode 0
  pages 304 (English 293) · .fls Spanish sources 58 · English sources 0

python3 tools/link_defined_terms.py --book 2 --lang es    links to insert: 0
```

## Homographs handled in `book2_es.py`

*fuerte/débil* (acid strength / any strength: dropped bare), *grupo* (periodic
group only before a number), *multiplicidad* (cell / NMR signal), *hidratación*
(alkene / ions), *posiciones ecuatoriales* (trigonal bipyramid / cyclohexane),
*protección* (protecting group / personal protection), *peligro* (the defined
hazard / the GHS08 name *peligro para la salud* and the signal word
*Peligro*), *red* (lattice / covalent, ice and silicate networks), *periodo*
(row / *periodo de inducción*), *bloque* (s/p block / *bloques de cinc*),
*cuantitativa* (reaction / *medida cuantitativa*, *la hacen cuantitativa las
teorías*), *actividad* (thermodynamic / *pérdida de actividad* óptica), and
*Red* capitalised (Ox/Red). Two lookaheads were made link-tolerant after the
second `--apply` showed they failed once their neighbour was already linked.

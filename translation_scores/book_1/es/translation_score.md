# Translation score — Chemistry Book 1 · Spanish (`es`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 1 (School Chemistry, Grades 1–12) |
| **Language** | Spanish (`es`), peninsular |
| **Quality bar** | **native school prose at every level** — a Spanish children's science book in the first years, a Spanish ESO physics-and-chemistry textbook in the middle years, a Spanish bachillerato chemistry course in the last three. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); the shipped Spanish editions of One Biology Book 1–5 (`../one-biology-book/parts/*/es/`) for typography (``…'' quotes, `---` incisos, the *tú* imperative of the exercise stems) and settled vocabulary; the Spanish physics editions for shared physical vocabulary |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-04 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 49 chapters + 49 solution twins = **98 files**; `frontmatter/preface.es.tex` (shared with Book 2 `es`) and `frontmatter/image-credits.es.tex`; the `\bookline` of `one_chemistry_book_1_school_es.tex` (*Libro 1: Química escolar -- Años 1 a 12*, matching the part titles *Año N*); the four box names in `styles/lang/es.tex` reviewed and kept (*Lo que ya sabes*, *En el laboratorio*, *Historia*, *Seguridad*); a curated `tools/term_config/book1_es.py`; the defined-term link layer; Spanish index keys with ASCII sort keys; the overfull sweep; a per-figure label check; and this score |

## Verdict in one line

A Spanish Book 1 that reads as one Spanish school chemistry course from the
first year to the last — short *tú* sentences for the youngest readers, the
impersonal *se* of the ESO textbook, the *tú* imperative of every exercise
stem as in the shipped biology editions, Spanish inverted question marks and
IUPAC-Spanish names (*etanoato de etilo*, *butan-2-ol*, *ácido etanoico*) —
with every structural, prose and chemistry gate green over all twelve years
and a forced build of **0 errors / 0 undefined / 0 overfull / 0 nullfont /
0 invalid-in-math**, 447 pages, 98/98 files in the `.fls`.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted over all 98 files against their 98 twins: **665 `exercise`**, **42 `problem`**, **707 `\begin{solution}`**, **112 `[resume]`**, **260 `omfigure`**, **137 `tikzpicture`**, **25 `axis`**, **495 `\node`**, **123 `\includegraphics`**, **369 `\emph`**, **301 `\index`**, **142 `\cref`**, **1352 `\label`**, **1054 `\item`**, **2196 `\qty`**, **2267 `\ce`**, **128 `\chemfig`**, **186 `% ledger:`** comments, and per environment **184 `definition`, 115 `proposition`, 65 `method`, 155 `example`, 52 `proof`, 72 `remark`, 47 `recall`, 29 `inthelab`, 15 `history`, 23 `safety`** — all equal to English. `\label` set diff **0 / 0**. Every file was written through `tools/id_apply.py`, so every unnamed line is byte-identical to English. A per-file **number census** against the English twin (scripted) finds no numeric difference except where Spanish writes a number as a word (*los años ochenta*, *de quince pulgadas*, *a principios del siglo XX*, *el volumen del primer año*) and two deliberate clarifications (*rot.~1, rot.~2 y rot.~3* naming the pens of the grade-7 figure; *nunca lo hace pasar de 7* in a grade-9 solution) |
| Terminology | **96** | Spanish school and bachillerato vocabulary, one word per notion across the twelve years: *sustancia pura / mezcla homogénea / heterogénea*, *soluto, disolvente, disolución saturada* (never *solución*, kept for the solutions of exercises), *decantación, filtración, filtrado, tamizado*, *triángulo del fuego, combustible*, *cambio químico / transformación física*, *ecuación ajustada, coeficiente estequiométrico*, *termoplástico / termoestable, PEAD / PEBD*, *número atómico, número másico*, *ion espectador* (no accent, RAE 2010), *cantidad de sustancia, constante de Avogadro, masa molar*, *concentración en masa / molar, disolución madre, factor de dilución, escala de patrones*, *tabla de avance, avance máximo, reactivo limitante, mezcla estequiométrica*, *cromatografía en capa fina, eluyente, factor de retención*, *estructura de Lewis, par enlazante / par no enlazante (par libre)*, *enlace polar, electronegatividad, enlace de hidrógeno*, *fórmula molecular / semidesarrollada / esquelética*, *grupo funcional*, *número de onda, transmitancia, región de la huella dactilar*, *par redox, semiecuación*, *valorante, disolución valorada, volumen de equivalencia*, *RMN del protón, desplazamiento químico, singlete / doblete / triplete / cuadruplete, regla de los n+1*, *representación de Cram, carbono asimétrico, enantiómeros, diastereoisómeros, forma meso, conformación alternada / eclipsada*, *sitio dador / aceptor, flecha curva, etapa elemental, intermedio de reacción*, *factor cinético, bloqueo cinético, periodo de semirreacción* (and *periodo de semidesintegración* for the physics remark, where Spanish has its own word), *catálisis homogénea / heterogénea, convertidor catalítico*, *cociente de reacción, tasa de avance final, sentido directo / inverso*, *ácido de Brønsted, ion oxonio, anfolito, producto iónico del agua, pKa*, *diagrama de predominio, zona de viraje, disolución tampón, relación de Henderson*, *valoración pH-métrica / conductimétrica, ley de Kohlrausch, semiequivalencia*, *pila, semipila, puente salino, constante de Faraday*, *reacción quimioselectiva, grupo protector, economía atómica, química verde, fluido supercrítico*, *unidad de repetición, grado de polimerización, polímero de adición / de condensación*. Idioms where Spanish has its own: *agua oxigenada de 20 volúmenes*, *vinagre de 6 grados*, *pHmetro*. All 301 `\index{}` keys rewritten in Spanish, with ASCII sort keys on the 171 accented ones (`acido carboxilico@ácido carboxílico`) so that *ácido*, *átomo*, *éster*, *ánodo* sort under their letter instead of after *z* |
| Register / tone | **97** | Measured against the shipped biology `es` editions before scoring, not assumed: the exercise stem is the **tú** imperative throughout (*Calcula* ×150, *Da* ×91, *Escribe* ×88, *Nombra* ×47, *Explica* ×44, *Dibuja* ×42, *Mira* ×25, *Deduce* ×25, *Comprueba* ×18 …), exactly as in biology (730 *tú* stems, **0** *usted*); script audit over course **and** solutions: **0** *usted / ustedes / vosotros* forms, **0** *Calcule / Explique / Escriba*. Inverted question marks balanced in every file (scripted census; the only unmatched `?` are inside TikZ `\pgfmathsetmacro` conditionals and Mendeléiev's printed ``? = 68''). Course text in the impersonal *se* from the ESO years on; the youngest grades in short *tú* sentences |
| Readability / naturalness | **95** | Drafted line range by line range directly in Spanish; Spanish word order where English is nominal (*Un catalizador hace una reacción diez veces más rápida*), Spanish connectors (*así que*, *es decir*, *por tanto*), and Spanish clause length rather than English chains. Weekend-problem titles read as Spanish questions (*¿cuántas botellas de 25 g hacen falta para un forro polar?*). Decimal **point** kept in running prose, deliberately, because siunitx prints every `\qty` with a point and a comma in the words beside a point in the numbers read worse than either alone; the biology editions use the comma in prose — a known, documented divergence |
| Chemistry & numbers | **97** | `\ce`, `\chemfig`, schemes and `% ledger:` comments byte-identical (gate 12 and gate 13 green on every year). Every solution re-read against its question in Spanish, and the scripted number census confirms every value survived translation. Four suspected English-canon defects reported, not repaired silently (see below); two of them corrected in the Spanish wording where the English is plainly wrong and the fix changes no number |
| Figures | **95** | Every figure carrying translated text was rendered at 130 dpi and read page by page (the `!draw` ranges, every `xticklabels`/`yticklabels` list, every lengthened label). Fixed on that pass: a chromatography figure whose Spanish labels ran under the neighbouring chromatogram (grade 7), two conductivity and metal-in-acid label pairs that touched (grade 9), the settling-tank box of the water-treatment chain (grade 3), the ibuprofen route boxes and the polymer-chain captions, where English hyphenation patterns split *catal-izada* and *ram-ificadas* (now *cata-lizada* and explicit line breaks). One residual: in the grade-11 colour wheel, *amarillo* and *naranja* touch the edge of their sectors (the words are longer than *yellow*, *orange* and the font is set in the drawing code) — legible, but tighter than English |
| Term links | **96** | **5,965** `\omterm` links (English 5,775, +3.3 %), **173** distinct targets: **all 172** of English's, none missing, plus `galvanising` (3 links, the defined sense). Frequency **and** chapter-set censuses run against English, both before and after curation; the residual excesses are each the defined sense (*periodo de semirreacción* is linked in its plural, which English's *half-lives* is not; *disuelve / disolver* are linked where English links *dissolves / dissolve*, the participle *disuelto* being left out as English leaves out *dissolved*). `links to insert: 0` on the final dry run |

## Term-link curation (`tools/term_config/book1_es.py`)

The two censuses found these Spanish collisions, each documented in the config:

* **disolución** is both the mixture and the act of dissolving — both the
  grade-2 definition — while *solución* is reserved for exercise solutions.
  English STOPs *solution*; Spanish STOPs the bare *disolución* the same way
  and keeps every multi-word term (*disolución acuosa / tampón / patrón …*),
  which keeps the target at English's reach.
* **capa** is an electron shell and, far more often, a layer (of solvent, of
  zinc, of sand, of oil, *capa fina*): masked unless a shell number or
  *externa / ocupada / completa* follows. English has two words.
* **reactivo** is reagent *and* reactant: left to the nearest-preceding rule
  (a reagent is a reactant of its test reaction, so the later chapters land on
  a true statement); the **adjective** *reactivo* (*grupo reactivo*, *tan
  reactivo*, *no metales de color y reactivos*) is masked — English's
  *reactive* is a different word.
* **E** (isomer) plus the plural tail matched **Es** ("it is") at the head of
  four questions: masked.
* **mol** is the name of the unit (the term) and its symbol in prose
  (*\frac{2}{3} mol de éster*): the symbol after a number or formula is masked.
* **vaso de precipitados** is a BEAKER, not a precipitate: the phrase is
  masked (found by the coordinator's verification, 5 links in grade 10, 11
  and 12; the precipitate target now has 28 links against English's 31, in
  no chapter English does not link).
* **grupo** only before a group number, as in English.
* Spanish word order and morphology: *doble enlace* (the usual order) as well
  as the defined *enlace doble*; the singulars of terms defined in the plural
  (*isómero, enantiómero, diastereoisómero, miscible*); the other gender of
  adjectives (*exotérmico, hidrófilo, quimioselectivo*); the plurals whose
  accent drops (*catión → cationes*, *reacción química → reacciones
  químicas*); the conjugated verbs of grades 2–4; *par libre*, the synonym the
  later chapters use, now named in the grade-10 definition itself.

## `!draw` opt-outs

Every one is the documented pattern (translatable text the draw census
cannot blank); each figure was then checked on the rendered page:
grade-4/01 133–134 (`xticklabels` added); grade-4/02 158–159 (`\foreach`
labels); grade-5/01 95–96, 105–106, 139–140; grade-5/02 148–149;
grade-7/01 335; grade-8/01 151, 153–154 (node text after a nested `($…$)`
coordinate); grade-8/03 133 (resin codes, *PEAD / PEBD / OTROS*);
grade-9/02 53–55, 168, 227–229; grade-9/03 67–70; grade-9/04 38;
grade-10/04 294–297 (`\cube` label argument); grade-11/01 42–45 (colour
names); grade-11/03 247–248 and grade-11/04 161–165 (nested-`at` labels);
grade-11/06 145–147; grade-11/09 243–244 (`yticklabels`); grade-12/01 91,
95 and 183–184; grade-12/07 198; grade-12/08 143–145; grade-12/11 230–231
(`xticklabels`), 312 and 315–317 (English line numbers).

## Samples (Spanish, with verdict)

1. **grade 2, definition** — «Un sólido se \emph{disuelve} en agua cuando,
   mezclado con el agua y removido, desaparece de la vista y deja el líquido
   \emph{transparente}, es decir, que se puede ver a través de él.»
   → **native**: the reflexive *se disuelve* and the gloss *es decir* are how
   a Spanish primary book explains a word.
2. **grade 10, proposition** — «Cuanto más cerca está de un átomo
   electronegativo o de un doble enlace, mayor es su desplazamiento.»
   → **native**: the *cuanto más … mayor* correlative, not a calque of *the
   nearer … the larger*.
3. **grade 12, catalysis** — «Un catalizador cambia el camino, no el
   destino.» → **native**: a Spanish proposition title that keeps the
   English antithesis without its word order.
4. **grade 12, equilibrium** — «En la botella cerrada, el dióxido de
   carbono sale del agua y vuelve a ella al mismo ritmo, y la composición no
   cambia; al abrir el tapón, el gas que sale ya no vuelve.» → **native**.
5. **grade 12, problem** — «El etanoato de etilo huele a caramelo de pera:
   ¿es coherente con la familia encontrada?» → **native**: *pear drops*
   rendered by the sweet a Spanish reader knows.

No sample in the edition reads as MT: the draft was written in Spanish
against the English twin, range by range, never post-edited from a machine
pass.

## Why not 100

* **Four suspected English-canon defects** (reported separately): the
  linalool boiling point needed by grade-10/01 exercise 12 and problem Q9 is
  given only in the solutions; grade-11/05 exercise 11 asks for "two
  families" whose solution answers three; grade-12/01 problem Q9 speaks of a
  "ring oxygen" in an open-chain ester; grade-12/07 problem Q4 says "left of"
  on a vertical pKa scale. The first two are reproduced; the last two are
  worded correctly in Spanish (no number changes).
* **Hyphenation patterns are English.** This TeX Live has no `spanish.ldf`
  (nor `french.ldf`), so `onechemistry.sty` builds every non-English edition
  without babel and TeX hyphenates Spanish with English patterns. The prose
  breaks are mostly acceptable, but some are not Spanish syllables; the
  visible ones in figures were fixed by hand, the prose ones cannot be.
* **Twenty-nine `!draw` opt-outs**, each the documented pattern, each a
  place where only the rendered page guards the figure.
* **Decimal point in prose**, chosen for consistency with siunitx, where the
  biology editions use the comma.
* **One tight figure** (the grade-11 colour wheel).

## Coordinator amendment (2026-10-04, after the Book 2 `es` edition landed)

Half-life is now *tiempo de semirreacción* in this book too (32 sites in
`grade-12/04` course and solutions, plus the `\index` sort key), to match the
Spanish Book 2 edition, which uses the usual kinetics term throughout. The
physics aside (*periodo de semidesintegración*) is unchanged. Re-linked
(26 half-life links, unchanged), gates green for all twelve years, forced
build 447 pp, 0/0/0. Score unchanged.

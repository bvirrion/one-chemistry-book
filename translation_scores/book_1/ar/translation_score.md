# Translation score — Chemistry Book 1 · Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 1 (School Chemistry, Grades 1–12) |
| **Language** | Arabic (`ar`), Modern Standard Arabic, right to left, built with LuaLaTeX + babel `bidi=basic` |
| **Quality bar** | **native school prose at every level** — an Arabic children's science book in grades 1–5, an Arabic middle-school textbook in grades 6–9, an Arabic secondary chemistry course in grades 10–12. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); the shipped Arabic editions of One Biology Book (`../one-biology-book/parts/*/ar/`) and their score files for typography, the imperative 2nd-person-singular exercise stem and the decimal-point / ASCII-digit conventions; `../arabic_style_card.md`; the Arabic physics editions for shared physical vocabulary |
| **Overall score** | **95 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-04 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 49 chapters + 49 solution twins = **98 files**; `frontmatter/preface.ar.tex` (shared with Book 2 `ar`) and `frontmatter/image-credits.ar.tex`; the box names and periodic-table legend strings of `styles/lang/ar.tex` checked (kept); a curated `tools/term_config/book1_ar.py`; the defined-term link layer; Arabic index keys; a right-to-left layout pass over every TikZ/pgfplots label and every inline chemical scheme; the overfull sweep; and this score |

## Verdict in one line

An Arabic Book 1 that reads as one Arabic school chemistry course from the
first year to the last — short sentences and the second person for the
youngest readers, the impersonal textbook voice from grade 6, the imperative
exercise stem throughout (اذكر، سمِّ، احسب، أعطِ، اكتب، علّل), Arabic
punctuation (، ؛ ؟) and guillemets «…» — with every structural, prose and
chemistry gate green over all twelve years and a forced build of
**0 errors / 0 undefined / 0 overfull / 0 nullfont / 0 invalid-in-math**, 418 pages (English 432).

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted over all 98 files against their 98 twins: **665 `exercise`**, **42 `problem`**, **707 `\begin{solution}`**, **112 `[resume]`**, **260 `omfigure`**, **137 `tikzpicture`**, **25 `axis`**, **495 `\node`**, **123 `\includegraphics`**, **369 `\emph`**, **301 `\index`**, **142 `\cref`**, **1352 `\label`**, **1054 `\item`**, **2199 `\qty`**, **2267 `\ce`**, **128 `\chemfig`**, **186 `% ledger:`**, and per environment **184 `definition`, 115 `proposition`, 65 `method`, 155 `example`, 52 `proof`, 72 `remark`, 47 `recall`, 29 `inthelab`, 15 `history`, 23 `safety`** — all equal to English; `\label` set diff **0 / 0**. Every file written through `tools/id_apply.py`; deliberate post-write edits (arrow direction, LTR grouping, Arabic separators) are scripted and idempotent, never hand edits. A per-solution **number census** against English differs only where Arabic writes a small number as a word (إلكترونان، ثمانية بروتونات، بخمس وعشرين مرة) |
| Terminology | **95** | One consistent school vocabulary across the twelve years, with the Arabic school terms (not calques): مادة نقية / خليط متجانس / غير متجانس، مذاب، مذيب، محلول مشبع، ترويق، ترشيح، راشح، مثلث النار، وقود، تحول كيميائي / فيزيائي، معادلة موزونة، معامل ستوكيومتري، لدائن حرارية / متصلدة بالحرارة، عدد ذري، عدد كتلي، نظير، أيون متفرج، كمية المادة، ثابت أفوغادرو، كتلة مولية، تركيز كتلي / مولي، محلول أم، معامل التخفيف، سلّم مرجعي، جدول التقدم، المتفاعل المحدِّد، خليط ستوكيومتري، كروماتوغرافيا الطبقة الرقيقة، مُزيح، معامل الاحتجاز، بنية لويس، زوج رابط / حر، رابطة قطبية، كهرسلبية، رابطة هيدروجينية، صيغة جزيئية / نصف بنيوية / هيكلية، مجموعة وظيفية، عدد موجي، نفاذية، منطقة البصمة، مزدوجة أكسدة واختزال، نصف معادلة، المحلول المعايِر / المراد معايرته، حجم التكافؤ، الانزياح الكيميائي، أحادية / ثنائية / ثلاثية / رباعية، قاعدة n+1، تمثيل كرام، كربون غير متناظر، متماكبات مرآوية / لامرآوية، شكل ميزو، تشكّل متعاقب / مكسوف، موقع مانح / مستقبِل، سهم منحنٍ، خطوة أولية، وسيط التفاعل، عامل حركي، إيقاف بالتبريد، زمن نصف التفاعل، حفز متجانس / غير متجانس، محوّل حفّاز، خارج التفاعل، نسبة التقدم النهائي، حمض برونستد، أيون الأكسونيوم، أمفوليت، الجداء الأيوني للماء، pKa، مخطط الغلبة، مجال تغيّر اللون، محلول منظِّم، علاقة هندرسون، المعايرة بقياس pH / بقياس الموصلية، قانون كولراوش، نصف التكافؤ، المصعد / المهبط، الجسر الملحي، ثابت فاراداي، الانتقائية الكيميائية، مجموعة حماية، الاقتصاد الذري، الكيمياء الخضراء، مائع فوق حرج، الوحدة المتكررة، درجة البلمرة، بوليمر إضافة / تكاثف. IUPAC names in Arabic order (إيثانوات الإيثيل، بوتان-2-ول، حمض 2-هيدروكسي البروبانويك، 2,3-ثنائي ميثيل بنتان); the periodic-table group is **زمرة** (keeping مجموعة for groups of atoms). All 301 `\index{}` keys rewritten in Arabic, indefinite lemmas (`\emph{definite}\index{indefinite}`) |
| Register / tone | **96** | Measured against the shipped Arabic biology editions: exercise stems imperative 2sg (لماذا ×49، ما ×34، أي ×28، انظر ×24، اكتب ×23، ارسم ×16، أعطِ ×14، سمِّ ×13 …) as in biology (لماذا، ما، سمِّ، اذكر، فسّر، أعطِ …); course text impersonal and passive from grade 6; no transliterated English function words; no tatweel anywhere (a technical object is named instead: «قيمة pH»، «بالمركب»); box names «ما تعرفه من قبل»، «في المختبر»، «لمحة تاريخية»، «السلامة» |
| Typography | **96** | Arabic comma, semicolon and question mark; Latin full stop; guillemets «…»; ASCII digits and decimal point, as the series' siunitx setting and the shipped Arabic biology editions do; accusative tanween on the alif (ـًا). Final sweeps over all 98 files and the two front-matter files: **0** lines ending on a standalone و (the conjunction is always attached at the next line's start), **0** tatweel, **0** bidi control characters, **0** lines opening on punctuation outside drawing code, **0** straight-quote pairs; list-like lines inside Arabic paragraphs carry Arabic separators |
| Fidelity / accuracy | **96** | Every course paragraph, worked example, exercise and solution translated against its twin with the numbers recomputed while translating (all grade-11 and grade-12 weekend problems re-derived: the ester molar masses, the breath tube, the iron tablet, the ethanol burner, the NMR solvent, tartaric acid, bromoethane, the fading dye, the hairdresser's peroxide, Berthelot's constant and the threefold excess, the ant's venom, the blood buffer, the vinegar, the phone battery, the ibuprofen routes, the PET jacket). Deliberate, documented divergences: see below |
| Right-to-left layout | **94** | The dimension that has no gate. Every class found by reading rendered pages and `pdftotext -bbox` coordinates (not by eye — the eye misreads mixed-direction lines), and fixed in this edition's own files by script: couple notation, inline schemes, word equations, node text, legends, axis labels (details below). Two classes are style-level and are reported, not fixed (theorem-head parentheses; pgfplots-label bracket shapes) |
| Figures | **95** | All drawing code byte-identical except the **24 `!draw` ranges** listed below (translated `\foreach` label lists, added `yticklabels`/`xticklabels`, one `\cube` argument); every node, legend and axis label translated; mixed Arabic/Latin node text made right to left (see below) |
| Links | **94** | **5341 `\omterm` links on 166 targets** against English's **5773 on 172**; the 7 English targets not reached are each linked once or twice in English (abundance 1, Ka 2, resource 1, resin code 1, complementary colours 1, molar absorption coefficient 2, organic compound 1 — the Arabic sentence uses a plural or a math symbol there); one target English never links (galvanising) is linked once. Curated from this edition's own harvest; both homograph censuses run after the last prose edit and the link layer, every flag read in context. Dry run: **links to insert: 0** |
| MT-artifact freedom | **96** | Gate 9 (Arabic prose) clean over all twelve years; `\text{}` census over course **and** solutions: every translatable `\text{}` translated, the survivors are symbols (A, B, C, L, NaOH, Ox, Red, M\,C\,H); 0 English `\index` keys (pKa is the symbol) |

**Overall: 95** (weighted toward terminology, register, RTL layout, link
curation and MT-artifact freedom; structure and build are gated mechanically).

## Gates and build

```
bash tools/check_translation.sh grade-N ar   (N = 1 … 12)
  12 / 12 PASSED   (structural censuses, labels, ledger ids, Arabic prose
                    gate 9, chemistry twin gate 12, equation balance 13)

forced build (latexmk -g), build/one_chemistry_book_1_school_ar.log (grep -a)
  '^!' ............. 0        undefined ........ 0
  Overfull ......... 0        nullfont ......... 0  (English baseline 0)
  'invalid in math mode' 0    pages ............ 418 (English 432)
  .fls Arabic chapter/solution files 98 · English chapter files 0

python3 tools/link_defined_terms.py --book 1 --lang ar     (plain dry run)
  links to insert: 0 across 0 files
\label set diff 0 / 0 · \index 301 = 301 · \ce 2267 = 2267 · ledger 186 = 186
```

## Right-to-left layout: what was found and fixed

Direction bugs never reach a log. Each class below was found on rendered
pages and confirmed with `pdftotext -bbox` glyph coordinates.

1. **Couple notation reversed.** `\ce{Cu^{2+}}/\ce{Cu}` set in an Arabic line
   is two LTR boxes laid out right to left, so the page read *Cu/Cu²⁺* — the
   oxidant and reductant swapped. Every couple written as two `\ce` joined by
   `/` (g11/07, g11/08, g12/05, g12/07, g12/08 and their solutions) is
   wrapped in `$…$`, one LTR unit; the `\ce` arguments are untouched.
2. **Inline chemfig schemes** (g12/03 three mechanisms, g12/07 the acid in
   water, g12/12 the PET scheme) ran right to left, reactants on the right of
   a → arrow. Each scheme paragraph is wrapped in `\babelsublr{…}` so it reads
   left to right like every `\ce` equation of the book; the `\chemmove`
   curly arrows are positioned by node name and are unaffected.
3. **Word equations in Arabic** (g7/03 course and solutions, g10/07 display)
   read right to left: their arrows are flipped to ⟵ (and the display is
   reordered), so reactants stay first in reading order. Equations split
   across RTL table columns (g10/06, g10/07) get ⟵ for the same reason.
   Dangling math (`$a\,\ce{A} + b\,\ce{B} \longrightarrow$ نواتج`, `$2\times$ …`)
   is rewritten as one math span or in words.
4. **Mixed Arabic/Latin TikZ node text.** The style forces every picture to
   left-to-right; a node line mixing Arabic with formulas or numbers then
   came out in left-to-right segment order, and simply switching it to RTL
   reverses bare Latin and digit runs glyph by glyph (*316 ppm* → *mpp 613*).
   Recipe, verified on a test document and on the real pages: wrap the line
   in `\foreignlanguage{arabic}{…}` and box each bare Latin word or number in
   `\babelsublr{…}` (`\ce`, `\qty`, `$…$` are boxed already); a bracketed
   group with no Arabic inside is boxed whole, and a line that is one
   bracketed Arabic group keeps its brackets outside the switch. Applied by
   script to every mixed node, label, legend entry, `\foreach` label item and
   pgfplots axis label (≈ 100 lines). A pgfplots axis label with no Arabic in
   it is boxed left to right as a whole (the style sets labels right to left,
   which printed "pH" as "Hp" and "(mL)" with its brackets turned outward).
   One node whose bracket pair was split across two lines (g11/08, the
   permanganate flask) was reworded without the brackets.
5. **Inline math-mode `\ce{… <=> …}`** draws its harpoons on top of the
   preceding species in an RTL line (g11/07 l.55): set in text mode instead.

**Reported, not fixed (shared style):** (a) the parenthesised note of a
theorem head prints as )title( — `\thmnote` brackets are not mirrored; the
shipped Arabic biology PDFs show the same; (b) pgfplots axis labels are made
RTL with the raw `\pardir TRT\textdir TRT`, which does not mirror brackets,
so a label ending in a bracketed unit printed )mL( and a Latin-only label
"pH" printed "Hp" — worked round in this edition (item 4), but the style
should set the direction through babel; (c) the node-direction behaviour of item 4, which every Arabic
edition of the series inherits.

## Defined-term links

| | English | Arabic |
|---|---:|---:|
| `\omterm` links | 5773 | 5341 |
| distinct targets | 172 | 166 |
| English targets not reached | — | 7 (each linked 1–2× in English) |
| dry run, links to insert | 0 | 0 |

*Frequency census* survivors, each read in context and correct: the
solution target (محلول, Arabic has no exercise-"solution" homograph, so
every occurrence is the chemist's solution: 384 vs 115), electronegativity
(the adjective كهرسلبية is the same word), the reaction quotient and the
indicator (both in their own chapters). *Chapter-set* survivors (≈ 20
targets) were each read: all the defined sense.

Arabic homographs found by the two censuses, each handled in
`tools/term_config/book1_ar.py` with its evidence: مادة (grade-1 material /
matter, substance), جسم (object / «جسم صلب», the human body), رمز, إضافة (the
reaction category / the ordinary noun "adding"), ترسيب (settling / precipitation),
طبقة (electron shell / any layer: an extraction layer, ice, a spongy deposit, a
catalyst coat), تفكك (dissociation of an ionic solid / decomposition, radioactive
decay), إماهة (hydration of ions / hydration of ethene — the coordinator's
canon fix), معايرة (titration / calibrating a pH meter, volumetric glassware),
كاشف (reagent / indicator / the photodetector «الكاشف الضوئي»), مردود (synthesis
yield / heating efficiency), خام (ore / crude oil, crude solid), نظير (isotope /
"counterpart"), تآكل (corrosion / weathering), «محلول متعادل» (pH-neutral /
electrically neutral), «للاشتعال» in hazard statements, and the bare letters
E and Z (DROP). Broken plurals of the most frequent terms (ذرات، جزيئات، أيونات،
إلكترونات، بروتونات، نيوترونات، فلزات، إسترات، كحولات، بوليمرات) are declared in
`EXTRA`, since no tail rule can reach them.

## Deliberate divergences from the English

- g7/01: a table "read from left to right" → «من اليمين إلى اليسار».
- g7/03: the word-equation definition and method say reactants on the
  **right**, products on the **left**, with ⟵, matching item 3 above.
- g11/05: ester names put the acid part first (إيثانوات الإيثيل), so the
  worked example and its caption say the acid part gives the **first** word;
  family endings are given as Arabic suffixes (‑ول، ‑ال، ‑ون، حمض …‑ويك).
- g11/07, g12/03: "the electrons cancel" is «تُحذف من الطرفين», never the
  ambiguous «تُختزل».
- g1 and g2 remarks whose English point is a pun on English words (names that
  are also materials; sugar that "melts") are adapted to the Arabic words that
  carry the same point.
- g12/04 legend "(warmer)" → «، أسخن», and four node lines lose a bracket
  pair that babel cannot keep paired at a line edge.
- Left/right in figure captions are kept literally (figures are drawn left to
  right); in a two-panel figure set side by side as boxes, "left/right"
  follow the RTL order of the boxes (g9/06).
- Photographers are transliterated in captions (فيرنر شيلمان); Wikimedia user
  names stay Latin (Dnn87, GuidoB, Stephanb, Elcobbola); the credits page
  gives each transliteration with the original in parentheses.

## English-canon findings

None outstanding: every numerical answer recomputed during translation agrees
with its question. (The two canon fixes the coordinator announced during the
run — the hydration head of g12/11 and the "optically active" wording of
g12/02 problem item 14 — are applied.)

## `!draw` ranges (24)

g4/01 133–134 (xticklabels added) · g4/02 158–159 · g5/01 95–96, 105–106,
139–140 · g5/02 148–149 · g7/01 335–336 · g8/03 133 · g9/02 53–55, 168,
227–229 · g9/03 67–70 · g9/04 38 · g10/04 294–297 (`\cube` argument) ·
g11/01 42–45 · g11/06 143–151 · g11/09 243–244 (yticklabels added) ·
g12/01 88–95, 183–184 · g12/07 195–201 · g12/08 142–145 · g12/11 230–231
(xticklabels), 312, 315–317.

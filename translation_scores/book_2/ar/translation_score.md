# Translation score — Chemistry Book 2 · Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 2 (University Chemistry, Year 1; `parts/bachelor-1`) |
| **Language** | Arabic (`ar`), Modern Standard Arabic |
| **Quality bar** | **native academic Arabic** — a first-year university chemistry course as it is lectured and printed in Arabic (impersonal course text, second-person singular imperatives in exercise stems: احسب، فسّر، بيّن، أعطِ، اذكر). English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Sense / register references measured before drafting** | the English canon (content); the Arabic chemistry Book 1 (`parts/grade-*/ar/`) for settled terminology (السهم المنحني، إعادة التبلور، كروماتوغرافيا الطبقة الرقيقة، معامل الاحتجاز، المصعد/الجبهة، إماهة، الفلزات القلوية، نقطة النهاية/التكافؤ …), its credits convention and its RTL recipes (`ar1/post.py`, `rtlnode.py`); Arabic biology Book 3 for register; the French Book 2 as a sense twin |
| **Overall score** | **95 / 100** |
| **Ship threshold** | ≥ 95 — **met for the 28 chapters written; chapter 6's body is blocked (see below) and builds from the English fallback** |
| **Date** | 2026-10-04 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): **57 of 58 files** (28 chapter bodies + all 29 solution twins; the ch. 6 body is drafted in the agent's scratch patch but could not be written, see "Blocked"), `frontmatter/image-credits-book2.ar.tex`, a curated `tools/term_config/book2_ar.py`, the link layer, Arabic index keys, RTL direction fixes, the overfull sweep, per-chapter probe builds with figure-page checks, and this score |

## Verdict in one line

An Arabic Book 2 that reads as an Arabic university chemistry course, with
every structural census equal to English, a forced build of **0 errors /
0 undefined / 0 nullfont / 0 invalid-in-math**, one overfull box (in the English
ch. 6 fallback, not in an Arabic file), and two reported gate problems: the
ch. 6 body is blocked by an Arabic prose-gate false positive on TikZ colour
keys, and 9 `pX` notation hits (pCl, pAg, pNH₃) are the same gate's false
positives, written with `--force-classes prose`.

## Blocked: chapter 6 body

`parts/bachelor-1/ar/06-crystals-ionic-covalent.tex` is **not written**. Its
patch passes every `id_apply` census but the Arabic prose gate flags the colour
names of TikZ option lists (`fill=green!…`, `black`, `gray`, `orange`,
`violet`, `blue`, `yellow`) that the drawing census requires byte-identical. A
fix to `tools/check_arabic_prose.py` (skip option lists inside TikZ nodes /
allow these colour keys) was attempted and **refused by the permission system**
("modify shared resources"); following that ruling the patch was not forced
in. The finished patch is `…/scratchpad/ar2/p/06.patch` (body; solutions
already written). Once the gate is fixed by the coordinator:
`./ap.sh p/06.patch`, then relink (`--unwrap --apply`, `--apply`).

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **98** | Counted over the 57 written files against their twins: **336 `exercise`**, **28 `problem`**, **377 `solution`**, **141 `omfigure`**, **89 `tikzpicture`**, **483 `\node`**, **44 `\includegraphics`**, **215 `\cref`**, **798 `\label`**, **886 `\item`**, **23 schemes**, **101 `\chemfig`**, **157 `definition` / 122 `proposition` / 105 `proof`**, **381 `\emph`**, **355 `\index`** (+ 9 in ch. 6 = 364), **1420 `\qty`**, **3347 `\ce`**, **139 `% ledger:`** — all equal to English; `\text{}` counts equal per file. Every body written through `tools/id_apply.py`. **−2** for the missing ch. 6 body |
| Terminology | **96** | Arabic chemistry vocabulary aligned with Book 1: مدار، عدد كمي، الحجب، الشحنة النووية الفعلية، الكهرسلبية، بنية لويس، الهجين الرنيني، العدد الفراغي، التهجين، تآثرات فان دير فالس، الرص المتراص، المواقع البينية، تقدم التفاعل، طاقة التنشيط، تقريب الحالة المستقرة، مسلّمة هاموند، أمفوليت، تأثير التسوية، جداء الذوبانية، الربيطة، المعقد المخلبي، نصف الخلية، الجسر الملحي، معادلة نرنست، مخطط الجهد--pH، المحلول المعايِر، متماكبات مرآوية/لامرآوية، التشكّل المتخالف/المتطابق/المنحرف، الدوران النوعي، الانزياح الكيميائي، الاقتران سبين--سبين، التأثير التحريضي/الميزوميري، الانشطار المتجانس/غير المتجانس، الكاتيون الكربوني، المحب للنواة/للإلكترونات، المجموعة المغادرة، انقلاب والدن، الوضع المضاد المستوي، قاعدة زايتسيف/ماركوفنيكوف، كاشف غرينيار، انقلاب القطبية، نصف الأسيتال، مجموعة الحماية، مانح الهيدريد، الانتقائية الكيميائية، أيون الهالونيوم، تأثير الزوج الخامل، تثبيت النيتروجين، الكالكوجينات، المركبات بين الهالوجينية، الخطر/الخطورة، عدم اليقين المعياري، التقييم من النوع A/B، الانحراف المطبَّع، معامل التوزيع، معامل الاحتجاز. All index keys in Arabic; the one key that merged two English entries (screening/shielding → حجب) split as `حجب (رنين مغناطيسي نووي)`. One drift normalised before linking: كمون → جهد (standard potentials) in chs 26–29 to match chs 13–15 |
| Register / tone | **96** | Exercise stems in the 2nd-person singular imperative; course text impersonal; «» quotes, Arabic ، ؛ ؟; ASCII digits and decimal point; no tatweel anywhere (checked); house forms kept (`مسألة نهاية الأسبوع --- …`، `الجزء الأول --- …`، `مجلد السنة الثانية`، `المجلد المدرسي (الصف …)`) |
| LaTeX hygiene / RTL | **95** | Forced build (`latexmk -g` under systemd-run, LuaLaTeX): **0 errors, 0 undefined, 0 nullfont, 0 invalid in math mode, 0 missing characters**; **1 overfull** (9.3 pt, in the English ch. 6 fallback, not an Arabic file — the ch. 11 one was cleared by re-ordering the sentence); `.fls` Arabic sources **57**; **282 pp** (English 293). RTL work beyond the Book 1 recipes, every case verified with bbox/pixel measurement: relation and arrow chains between separate items (`A $>$ B $>$ C`, `X $\to$ SN2`) are laid right-to-left with the glyph unmirrored and so state the inverse — all such chains (chs 3, 4, 10, 14, 16, 18, 19, 24, 25) boxed `\babelsublr{…}` with Arabic items in `\foreignlanguage{arabic}{…}`; titles with a numbered part marker `(1)` printed `)1(` in the running header — boxed in chs 5, 27, 28, 29 (and the ch. 6 patch); theorem-note titles ending in an LTR cluster fixed (chs 11, 12, 16); edge parentheses removed from RTL figure nodes; `Pt--Rh` node reversed → written in Arabic. **−1** for the residual cosmetic RTL limits shared with Book 1 (e.g. `\qty` prints number then unit in reading order) |
| Cross-refs / rule compliance | **97** | Labels, `\cref`s, solution keys, `[resume]`, math, `\ce`/`\chemfig`/schemes and ledger comments byte-identical (id_apply censuses). `--force-classes prose` used for chs 11 and 12 only (pCl/pAg/pNH₃ notation, gate false positives); `!draw` twice (ch. 16 EN l. 199 carvone `\foreach` labels; ch. 17 EN l. 68 colour-wheel `\foreach`); `!delims` once (ch. 17 EN l. 73: the delims census reads the node line break `\\(` as a `\(` delimiter). No curriculum or country of a programme named. Shared files touched: none outside this edition (the gate fix was refused). No git command, no commit |
| Figures | **95** | Drawing code byte-identical; node text, axis labels, legends, `yticklabels` (ch. 26 countries) and captions localised. Caption side words swapped where separate boxes are mirrored by RTL (chs 5, 6, 7, 12, 26 l. 91, 29 l. 215; ch. 27 "from left to right" → من اليمين إلى اليسار for four photographs); single tikzpictures not swapped. Every figure page of every chapter rendered from a probe build and read; colour-wheel implication made an LTR formula (`\babelsublr`), TLC "eluent" written الطور المتحرك (المصعد is the anode) |
| Solutions | **97** | All 336 exercise and 28+1 problem solutions native; every number re-derived while translating (no English-canon slip found); scripted number-multiset comparison per solution against English: the 7 differences are all intended (numbers spelled as words: رابطتا، الثماني، صفرًا; a name written in full) |
| Defined-term links (`\omterm`) | **95** | **2305 links over 141 targets** against English **2462 over 144** (English without ch. 6: 2377); the three missing targets are ch. 6-only (structure type, ionic crystal, radius ratio, molecular crystal) plus one polyprotic link. `book2_ar.py` curated from this edition's harvest: `DROP` for bare قوي/ضعيف and جزيئية (molecular vs molecularity); **138 `EXTRA`** plural, dual, accusative and indefinite-construct (idafa) forms re-pointed at Book 2 labels (أزواج حرة، بنى لويس، روابط هيدروجينية، متماكبان مرآويان، أسهم منحنية، عدد أكسدة، قانون سرعة، حفّاز …); **54 `EXTRA_PROTECT`** patterns for the Arabic homographs (valence vs equivalence تكافؤ، بالتناسب، دورة الجير/دورة حفزية، الفئة 2، شبكة بلاتين/شبكة تساهمية، معايرة المنصة، NMR الحجب، إماهة أيونات، المواضع الاستوائية، «خطر»/خطر صحي، GHS03 مؤكسد، adjectival كهرسلبية، titles with nested braces). Frequency and chapter-set censuses read target by target; dry run **links to insert: 0** |
| MT-artifact freedom | **96** | Arabic prose gate: only the 9 `pX` notation false positives remain; tatweel, ASCII quotes, bidi controls, Latin punctuation after Arabic: none; `\text{}` subscripts translated (مرجع، العيّنة، منقلب/محتفظ، إيثر، أسيتال، نيومنثيل/منثيل، القيمة …) |

**Overall: 95.**

## Gate output summary

```
bash tools/check_translation.sh bachelor-1 ar
  FAIL chapter missing ......... ar/06-crystals-ionic-covalent.tex (blocked, see above)
  FAIL Arabic prose hygiene .... 9 hits, all pX notation (ch. 11 pCl x3, pAg x1;
                                 ch. 12 pNH3 x5): gate false positives
  chemistry twin gate ......... OK (57 files)
  all other gates ............. pass

forced build, build/one_chemistry_book_2_university_year_1_ar.log (grep -a)
  '^!' 0 · undefined 0 · Overfull 1 (English ch. 6 fallback) · nullfont 0
  invalid in math mode 0 · pages 282 (English 293) · .fls Arabic sources 57

python3 tools/link_defined_terms.py --book 2 --lang ar   -> links to insert: 0
\index 355 = 355 (+9 ch. 6) · \emph 381 = 381 · \qty 1420 = 1420 · \ce 3347 = 3347
```

## Reported for the coordinator

- **Gate bug (blocking):** `tools/check_arabic_prose.py` reads TikZ colour keys
  in node option lists as English prose; blocks ch. 6. Also flags `pCl`,
  `pAg`, `pNH` (the Hindi gate allow-lists them).
- **Tool limits:** `id_apply` delims census counts `\\(` as a `\(` delimiter;
  the linker's heading mask (`protect.py`) nests one brace level only, so a
  title with `\texorpdfstring{\babelsublr{…}}{…}` got linked until masked here.
- **Style (Arabic):** running headers print `)1(` for `(1)` in chapter titles;
  `\chaptername` prints «باب» in headers/chapter openings although
  `styles/lang/ar.tex` sets «الفصل» (babel's captions override it); inline
  relation glyphs between separate items are never mirrored, so every Arabic
  edition with `A $>$ B` chains between words states the inverse.
- **Other edition (not touched):** Book 1 `ar` g10/02 l. 130–131 links «الزمرة»
  to the period definition and splits «الفلزات القلوية الترابية».

## Coordinator amendment (2026-10-04, after delivery)

The chapter 6 body, blocked at delivery by a gate bug (`check_arabic_prose.py`
read TikZ colour keys inside `\node[...]` options as English), was applied by
the coordinator from this agent's own finished patch (`ar2/p/06.patch`, through
`ar2/ap.sh`: `id_apply` with every census, then the RTL post-edits), after
fixing that gate (balanced `[...]` options skipped, as in
`check_hindi_prose.py`) and allowing the p-function symbols pCl/pAg/pBr/pNH
that had forced `--force-classes prose` on chapters 11–12. `id_apply`'s
delimiter census was fixed too (`\\(` is a line break, not `\(`).

After the fix: 58/58 files, `check_translation.sh bachelor-1 ar` PASSED (all
gates, including the prose gate on chapters 11–12), forced build 281 pp,
0 errors / 0 undefined / 0 overfull / 0 missing characters, `.fls` 58,
2,376 links over 145 targets (English 2,462 / 144); the two English targets
not reached are each linked once in English. Score unchanged at 95.

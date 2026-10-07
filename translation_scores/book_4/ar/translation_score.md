# Translation score — Chemistry Book 4 · Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 4 (University Chemistry, Year 3; `parts/bachelor-3`) |
| **Language** | Arabic (`ar`), Modern Standard Arabic |
| **Quality bar** | **native academic Arabic** — a third-year university chemistry course as it is lectured and printed in Arabic (impersonal course text, second-person singular imperatives in exercise stems: احسب، فسّر، أعطِ، اكتب، بيّن، ارسم). English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Sense / register references measured before drafting** | the English canon with every wave-1/wave-2 canon fix and the later coordinator edits; the Arabic Books 2 and 3 (`parts/bachelor-1/ar/`, `parts/bachelor-2/ar/`) for settled terminology, house forms and the credits convention; `arabic_style_card.md`, `sources/WAVE1_FINDINGS_B34.md`, `sources/WAVE2_FINDINGS_B34.md` |
| **Overall score** | **95 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-07 |
| **Scope** | All **66 files** (33 chapter bodies + 33 solution files), written directly at native register through `tools/id_apply.py` (no machine draft); `frontmatter/image-credits-book4.ar.tex`; a curated `tools/term_config/book4_ar.py`; the link layer; Arabic index keys; RTL fixes; per-chapter probe builds with every figure page read; this score |

## Verdict in one line

An Arabic Book 4 that reads as an Arabic university chemistry course, every
structural census equal to English, `check_translation.sh bachelor-3 ar`
PASSED, a forced build of **387 pp (English 405), 0 errors / 0 undefined /
0 overfull / 0 invalid-in-math, nullfont 17 and 23 missing characters (both
exactly the baseline)**, `.fls` 66, and **1,549 links over 261 targets**
(English 1,634 / 253; no English target missed).

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **97** | Counts equal to English: `\label` 1,183, `\ce` 1,657, `\index` 675, `\emph` 677, `\text` 67, `\chemfig` 32, `tikzpicture` 161; every environment count equal (gate 4); `% ledger:` ids equal (gate 12). `\qty` 1,996 against 1,997: ch. 11 problem "the first \qty{24}{h}" written «في الساعات الأربع والعشرين الأولى». The coordinator's solutions/32 items 14–15 edit (0.0145, 0.083) mirrored byte for byte |
| Terminology | **96** | Arabic Books 2–3 vocabulary kept (متماكبات مرآوية/لامرآوية، محب للنواة/للإلكترونات، الربيطة، الهابتية، التبرع العكسي، الإضافة التأكسدية، خط شلنك، صندوق القفازات، الاقتصاد الذري، كيمياء خضراء، معامل ستيودنت …); Book 4 terms settled once per chapter and used throughout (photochemistry, electrode kinetics, surfaces, colloids, ligand-field spectra and magnetism, inorganic mechanisms, organometallics, catalysis, solid state, materials, bioinorganic, supramolecular, pericyclic, radicals/carbenes, asymmetric synthesis, heterocycles, total synthesis, green chemistry: العامل E، كثافة الكتلة في العملية، كفاءة كتلة التفاعل، تقييم دورة الحياة، البصمة الكربونية؛ environment and toxicology: قدرة الاحترار العالمي، المطر الحمضي، القلوية، عسر الماء، الطلب البيوكيميائي/الكيميائي على الأكسجين، الإثراء الغذائي، الانتواع الكيميائي، معامل التوزيع بين الأوكتانول والماء، التراكم/التضخم الحيوي، الجرعة المميتة الوسطى، حاصل الخطر؛ research practice: الرنين المغناطيسي النووي الكمي، اختبار الدلالة، فرضية العدم، دفتر المختبر، بيانات FAIR، النزاهة البحثية، تحكيم الأقران، تسلسل الضوابط). Personal names transliterated in captions; photo credits keep user names, institutions and licences verbatim (four captions changed back from transliterated user names to Shandchem, Kaldari, Soramimi, Polimerek) |
| Register / tone | **96** | Exercise stems in the 2nd-person singular imperative, measured against Book 2 `ar` (B2: احسب 283، اكتب 149، فسّر 94، بيّن 82، أعطِ 81، ارسم 71; B4: احسب 357، أعطِ 84، بيّن 77، فسّر 72، اكتب 62، ارسم 27 — fewer writing/drawing stems because Book 4 asks for more calculation); weekend-problem items 22 % احسب (Book 2 19 %); course text impersonal; «» quotes, Arabic ، ؛ ؟; ASCII digits; no tatweel; no line-final detached «و» except three before display math; three «بال\emph{…}» joins that would break letter joining across the font switch reworded (ch. 15, 25) |
| LaTeX hygiene / RTL | **94** | Forced build through `build.sh`: 0/0/0, invalid-in-math 0, nullfont 17 and missing characters 23 (17 nullfont backticks ch. 12 + 5 U+000A + 1 U+007F = baseline, every line read), `.fls` 66, 387 pp. RTL work, each case checked on the rendered page: Arabic node text in `\foreignlanguage{arabic}` with Latin runs in `\babelsublr`; Latin–hyphen–math clusters boxed (my `gluefix.py` extended to `$cis$-$\ce{…}$`, `\textit{cis}-$\ce{…}$`, `$[1,5]$-H`); brackets at Arabic node edges replaced by commas, `\shortstack` or rephrasing (incl. ch. 14 ozone axis label); one RTL overfull (ch. 22, unbreakable inline formula) fixed by rewording; **new trap:** `\babelsublr{/ \unit{…}}` inside an Arabic pgfplots axis label stops the build ("Missing number … \xparse function is not expandable"); `\babelsublr{(\unit{…})}` works. **−1** for the residual cosmetic RTL limits shared with Books 1–3 (a bare number + Latin unit prints unit-first in reading order; mixed Latin credits lines on the Image Credits page wrap as one LTR run) |
| Cross-refs / rule compliance | **97** | Labels, `\cref`s, solution keys, math, `\ce`/`\chemfig`/schemes, MOdiagram, omchartable, `\termsym`, `\kv` and `% ledger:` ids byte-identical (id_apply censuses; gate 12). `!draw` ranges: **05/271, 08/315, 09/77, 22/126, 24/106, 26/179, 26/362, 33/413** (all `\foreach` label lists). pgfplots `xticklabels` translated at 31/114 and 31/122. Allow-list entries appended to `tools/check_arabic_prose.py` (commented, before `__main__`): Baldwin descriptors `exo/endo-tet/trig/dig` and `(trig)/(dig)`; Commons user names `Polimerek`, `Shandchem`, `Kaldari`, `Soramimi`; `qnmr`. No programme or country named. No git command, no commit |
| Figures | **95** | Drawing code identical to English except the `!draw` ranges and label-position tweaks (ch. 32 runoff label `pos` 0.4→0.45, ch. 33 workflow box split onto three lines, both after the Arabic text collided); node text, axis labels, legends and captions localised; every figure page of every chapter rendered from a probe build and read |
| Solutions | **96** | All 396 exercise and 33 problem solutions native; every number re-derived while translating chs 14–33 (no English-canon defect found there); a scripted per-block number-multiset comparison against English leaves 19 differences, all intended (numbers written as words: ثمانية عشر، الأربع عشرة، مرة ونصف، الخمس والستين …) |
| Defined-term links (`\omterm`) | **95** | **1,549 links over 261 targets** against English **1,634 over 253**; **no English target missed**. Eight targets English never reaches, each the right sense because Arabic prints the full term where English prints an abbreviation or a different word: `computational-chemistry:hartree-fock` (7, «المجال المتسق ذاتيًا» for SCF), `quantum-model-systems:schrodinger` (10, «مؤثر هاملتون»), `green-industrial:rme` (4), `environmental-toxicology:oxygen-demand` (3, BOD/COD), `complex-spectra-magnetism:cooperative` (2), `inorganic-materials:cvd` (1), `inorganic-materials:pores` (1), `organometallic-bonding:agostic` (1). Same cause for the frequency outliers (`asymmetric-synthesis:ee` 56 vs 4 — English writes "ee"; `colloids:stability` 8 vs 3 — "CCC"; `qnmr` 6 vs 1; `singlet-triplet` 20 vs 6). `book4_ar.py`: **86 EXTRA** plural, dual, accusative and construct forms, **11 EXTRA_PROTECT** for six homographs (الحمل، هجرة، القلوية، مستوي الانزلاق، إشغال، ثقب) plus heading/arrow/tick masks. Dry run **links to insert: 0** |
| MT-artifact freedom | **96** | Arabic prose gate clean on all 66 files; `\text{}` contents translated (only `aq` left, a state symbol); no tatweel, no bidi controls |

**Overall: 95.**

## Gate output summary

```
bash tools/check_translation.sh bachelor-3 ar          -> TRANSLATION GATE: PASSED
  arabic prose gate: OK (66 files) · chemistry twin gate: OK (66 files)

build.sh one_chemistry_book_4_university_year_3_ar (forced)
  rc=0 pages=387 errors=0 undefined=0 overfull=0 nullfont=17 missingchar=23 invalidmath=0
  .fls Arabic sources 66

python3 tools/link_defined_terms.py --book 4 --lang ar  -> links to insert: 0
\label 1183 = 1183 · \ce 1657 = 1657 · \index 675 = 675 · \emph 677 = 677 · \text 67 = 67
\qty 1996 vs 1997 (ch. 11 "24 h" in words)
```

## Coordinator addendum (2026-10-07)

After this edition was delivered the coordinator carried in the later English
canon fixes found by other editions (listed in `sources/WAVE1_FINDINGS_B34.md`
and `WAVE2_FINDINGS_B34.md`; the last ones: solutions/32 items 14-15 0.0145 and
0.083, solutions/02 gap 2047.98) and aligned the link layer with English, which
no longer links "indistinguishable" in its everyday sense (ch. 4 "from the
original/itself", ch. 10 orientations and sums). This edition now has **1549
links over 261 targets** (English 1,632 over 253); gates, dry run (0) and the
forced build re-checked. Score unchanged.

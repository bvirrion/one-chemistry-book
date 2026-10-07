# Translation score — Chemistry Book 3 · Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 3 (University Chemistry, Year 2; `parts/bachelor-2`) |
| **Language** | Arabic (`ar`), Modern Standard Arabic |
| **Quality bar** | **native academic Arabic** — a second-year university chemistry course as it is lectured and printed in Arabic (impersonal course text, second-person singular imperatives in exercise stems: احسب، فسّر، أعطِ، اكتب، بيّن، ارسم). English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Sense / register references measured before drafting** | the English canon as it stands after the wave-1 canon fixes; the Arabic Book 2 (`parts/bachelor-1/ar/`) for settled terminology, house forms and the credits convention; `arabic_style_card.md` and `sources/WAVE1_FINDINGS_B34.md` |
| **Overall score** | **95 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-06 |
| **Scope** | All **70 files** (35 chapter bodies + 35 solution files), written directly at native register through `tools/id_apply.py` (no machine draft); `frontmatter/image-credits-book3.ar.tex`; a curated `tools/term_config/book3_ar.py`; the link layer; Arabic index keys; RTL fixes; per-chapter probe builds with every figure page read; this score |

## Verdict in one line

An Arabic Book 3 that reads as an Arabic university chemistry course, every
structural census equal to English, `check_translation.sh bachelor-2 ar`
PASSED, a forced build of **348 pp, 0 errors / 0 undefined / 0 overfull /
0 nullfont / 0 invalid-in-math / 3 missing characters (the U+000A baseline)**,
`.fls` 70, and **1,614 links over 183 targets** (English 1,733 / 179; no
English target missed).

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **97** | Per-file counts equal to English: `\index` 417, `\emph` 429, `\label` 1,025, `\ce` 1,398 + 704, `\text` 199 + 45, `\qty` in solutions 855; every environment count equal (gate 4). `\qty` in bodies 1,008 against 1,003: **+4 in ch. 4** (pressures and temperatures written into figure nodes as `\qty` so that their digits read correctly in RTL) and **+1 in ch. 35** (`\qty{1}{bar}` for a bare "1 bar" in a caption). Added lines (no English twin): «لدينا» before a statement that opens on a display (ch. 1 l. 413, ch. 2 l. 308, ch. 4 l. 109, ch. 23 solutions Q4) and a lead sentence before `center` in the methods of ch. 21 (l. 290) and ch. 27 (l. 222–223) — amsthm garbles the head of an Arabic statement whose body starts with a display |
| Terminology | **96** | Arabic Book 2 vocabulary kept (متماكبات مرآوية/لامرآوية، تشكّل منحرف/متطابق، محب للنواة/للإلكترونات، ألكان مهلجن، كاشف غرينيار …); Book 3 terms settled once and used throughout: الجهد الكيميائي، الحجم المولي الجزئي، الخاصية التجميعية، الأزيوتروب، فجوة الامتزاج، النقطة الأوتكتيكية، المركب المحدَّد، فرط الجهد، التيار الحدي، نافذة الكهرنشاطية، التخميل، المدار الرابط/المضاد للربط، تكامل كولوم/الرنين، مدارات حدودية، HOMO/LUMO، قاس/لين، تفاعل متضافر، المحب للديين، الربيطة، عدد المخالب، الهابتية، طاقة استقرار المجال البلوري، عالي/منخفض السبين، التبرع العكسي، الإضافة التأكسدية، الحذف الاختزالي، الإدخال الهجري، التبادل الفلزي، طليعة الحفاز، عدد/تردد الدوران، أيون الإينولات، الإلحاق الحلقي، سنثون، فك، الكروماتوغرافيا الومضية، معامل الاحتجاز، الزمن الميت، عدد الأطباق، الميز، الصحة/الإحكام، قابلية التكرار/الاستنساخ، المعالجة اللاحقة. Personal names transliterated in captions; photo credits keep user names, institutions and licences verbatim |
| Register / tone | **96** | Exercise stems in the 2nd-person singular imperative, measured against Book 2 `ar` (B2: احسب 99، اكتب 55، فسّر 51، بيّن 69 …; B3: احسب 116، فسّر 75، أعطِ 49، اكتب 26، بيّن 35 …); course text impersonal; «» quotes, Arabic ، ؛ ؟; ASCII digits; no tatweel, no bidi controls; **233 conjunctions و left detached by a line break** (`… و⏎\qty{…}` prints «و 300») found by a scan and re-attached to the next line in every file and patch |
| LaTeX hygiene / RTL | **94** | Forced build through `build.sh`: 0/0/0, nullfont 0, invalid-in-math 0, missing characters 3 (= baseline), `.fls` 70, 348 pp (English 373), no blank page. RTL work, each case verified with `pdftotext -bbox`: Latin words and multi-digit numbers in Arabic node text and axis labels boxed `\babelsublr`; Latin glued to math in prose boxed; relation chains LTR-boxed; caption sides swapped for mirrored side-by-side boxes; base-pair `\chemmove` figures boxed LTR. **New:** a bracket that ends (or abuts LTR material in) an Arabic TikZ node or pgfplots label printed facing the wrong way («(مهبط(»), because a node box resolves to LTR and bidi=basic has no N0 rule — **52 node/label texts across 17 chapters** wrapped in `\shortstack{…}` (one `\foreignlanguage` per line; `\shortstack[l]` does NOT fix it, `[r]` and the default do), one split parenthetical (ch. 7 Vigreux label) rephrased; a rendered-PDF bracket checker confirms none is left. **−1** for the residual cosmetic RTL limits shared with Books 1–2 (`\qty` prints unit before number in reading order, mixed NMR data lists wrap oddly) |
| Cross-refs / rule compliance | **97** | Labels, `\cref`s, solution keys, math, `\ce`/`\chemfig`/schemes and `% ledger:` ids byte-identical (id_apply censuses; gate 12). `!draw` ranges: **ch. 8 EN 61, ch. 19 EN 240** (colour-wheel `\foreach` labels), **ch. 20 EN 131–135** (step-name `\foreach` list + a dummy field), **ch. 23 EN 68–69 and 187–188** (`\foreach` labels), **ch. 31 EN 78** (start/later/end `\foreach`). No `--force-classes`. Allow-list entries appended to `tools/check_arabic_prose.py` (commented): `fac`, `mer`, `edta`; the `[west]` anchor of `\schemestart`; `dibal-h`; `icp`, `oes`, `ms`; `dept`, `pubchem`. All twelve wave-1 canon fixes and the later English edits (ch. 3 `ylabel shift`, solutions 20 benzyl line, solutions 1 ledger id) carried in. No programme or country named. No git command, no commit |
| Figures | **95** | Drawing code identical to English except the `!draw` ranges above; node text, axis labels, legends and captions localised; every figure page of every chapter rendered from a probe build and read; MOdiagram figures (ch. 14) render correctly with the coordinator's central hook, local wraps removed |
| Solutions | **96** | All 420 exercise and 35 problem solutions native; every number re-derived while translating (chs 15–35 in a dedicated pass); a scripted per-block number-multiset comparison against English leaves 20 differences, all intended (numbers written as words: ستة عشر، أربعة عشر، إلكترونان، وحدتان، «مجلد السنة الثالثة», CO/OC). One sense slip found and fixed by it (solutions 18 ex. 12: "two more" electrons, not ligands) |
| Defined-term links (`\omterm`) | **95** | **1,614 links over 183 targets** against English **1,733 over 179**; no English target missed. Four targets English never reaches: `def:b2:enolates-aldol:enolate` (35 — English's own terms for it all carry math or the rare phrase "enolate ion", so English links it 0 times; the Arabic «أيون الإينولات» is the right sense), `ellingham:aluminothermy` (1), `equilibrium-shifts:shift` (1), `frontier-orbitals:concerted` (2). `book3_ar.py`: STOP bare شظية/الشظية (chapter-local, as English); **73 EXTRA** plural, dual, accusative and indefinite-construct forms (المدارات الرابطة، مدارات جزيئية، فرط جهد، تكاملات الرنين، محبات للنواة قاسية، عالية السبين، أحماض دهنية، أنماط نظائرية، تصبّن …); **24 EXTRA_PROTECT** for the Arabic homographs: ميز (chromatographic resolution / resolving power, chs 32–33), الانتقائية (reactor / stereo-, regio-, chemoselectivity / selectivity factor), تحويل (conversion X / "converting A into B"), تشتت (dispersity / statistical dispersion, ch. 34), بدء/انتشار (chain steps / Grignard start, column diffusion, propagation of uncertainty), تكاملات الرنين المغناطيسي (NMR integrals), plus heading/arrow/tick masks. Frequency and chapter-set censuses read target by target; dry run **links to insert: 0** |
| MT-artifact freedom | **96** | Arabic prose gate clean on all 70 files; `\text{}` contents translated (only the symbols Ox/Red, as in Book 2); no tatweel, no bidi controls, no Latin punctuation after Arabic |

**Overall: 95.**

## Gate output summary

```
bash tools/check_translation.sh bachelor-2 ar          -> TRANSLATION GATE: PASSED
  arabic prose gate: OK (70 files) · chemistry twin gate: OK (70 files)

build.sh one_chemistry_book_3_university_year_2_ar (forced)
  rc=0 pages=348 errors=0 undefined=0 overfull=0 nullfont=0 missingchar=3 invalidmath=0
  .fls Arabic sources 70

python3 tools/link_defined_terms.py --book 3 --lang ar  -> links to insert: 0
\index 417 = 417 · \emph 429 = 429 · \label 1025 = 1025 · \ce 2102 = 2102
\qty 1863 vs 1858 (+4 ch. 4 nodes, +1 ch. 35 caption)
```

## Reported for the coordinator

- **Style (Arabic, all books):** brackets in TikZ nodes / pgfplots labels print
  facing the wrong way when they end the node or touch LTR material (no N0 in
  bidi=basic; the node box is LTR). `\shortstack{…}` (default or `[r]`) fixes
  it; `[l]` does not; `\begin{tabular}` also fixes it but trips gate 4's
  tabular count. Book 1 `ar` shows it (e.g. p. 85 «فحم متوهج (كربون)»); a
  central fix in the node hook would be better than per-node wraps.
- **Gate suggestion:** a line-final standalone «و» (or ف/ب/ل) is invisible to
  the prose gate but prints detached; worth a check.
- **Linker:** `lang_ar.py`'s HEAD takes one proclitic before ال, so
  «فبالتهوية» / «وبال…» never match (reworded once here).

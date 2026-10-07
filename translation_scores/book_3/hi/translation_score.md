# Translation score — Chemistry Book 3 · Hindi (`hi`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 3 (University Chemistry, Year 2; `parts/bachelor-2`) |
| **Language** | Hindi (`hi`) |
| **Quality bar** | **native academic Hindi** — a second-year university chemistry course as it is lectured and printed in Hindi (आप register, NCERT/CSTT technical vocabulary). English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Sense / register references measured before drafting** | the English canon (content); the shipped Hindi chemistry Books 1–2 (`parts/grade-*/hi/`, `parts/bachelor-1/hi/`) for settled terminology (कक्षक, आबंध, संभवन एन्थैल्पी, नाभिकरागी/इलेक्ट्रॉनरागी, निर्गामी समूह, रक्षी समूह, निक्षालक, प्रतिधारण गुणांक …), the house forms and the credits convention |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-06 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 35 chapters + 35 solution twins = **70 files**, `frontmatter/image-credits-book3.hi.tex`, a curated `tools/term_config/book3_hi.py`, the link layer, Hindi index keys, the overfull and orphan-heading sweeps, a per-figure page check, and this score |

## Verdict in one line

A Hindi Book 3 that reads as a Hindi second-year university chemistry course —
CSTT terminology from thermochemistry to structure determination, आप-register
imperatives in the exercises, danda punctuation, ASCII digits — with every gate
green (prose gate and chemistry twin gate OK on 70 files) and a forced build of
**0 errors / 0 undefined / 0 overfull / 0 nullfont / 0 invalid-in-math**, the
three `Missing character` lines being the run-wide U+000A baseline.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Counted over all 70 files against their twins: **420 `exercise`**, **35 `problem`**, **455 `\begin{solution}`**, **188 `omfigure`**, **160 `tikzpicture`**, **585 `\node`**, **64 `\includegraphics`**, **195 `\cref`**, **1025 `\label`**, **1170 `\item`**, **102 `\chemfig`**, **30 schemes**, **197 `definition` / 176 `proposition` / 202 `proof`**, **429 `\emph`**, **417 `\index`**, **2102 `\ce`**, **174 `% ledger:`** — all equal to English. `\qty` is **1864 against 1858**: six bare "bar" units of the English prose (ch. 1: 1, ch. 4: 4, ch. 35: 1) are set as `\qty{…}{bar}` so the Latin unit word does not sit in Devanagari prose — intended. Every body written through `tools/id_apply.py`; the only post-write layout edits are 31 group-local `\emergencystretch` settings on the opening line of an overfull proof/example/solution, and one figure key (below) |
| Terminology | **96** | CSTT/NCERT chemistry, Books 1–2 spellings kept: अभिक्रिया राशि, मानक संभवन एन्थैल्पी, जालक एन्थैल्पी, बॉर्न–हाबर चक्र, किरखॉफ़ का नियम, आंशिक मोलर राशि, रासायनिक विभव, राउल्ट/हेनरी का नियम, ले शातेलिए का सिद्धांत, स्वातंत्र्य कोटि, सतत रिएक्टर, रूपांतरण, वरणात्मकता, ऊष्मीय अनियंत्रण, एलिंगम आरेख, स्थिरक्वाथी/विषम-स्थिरक्वाथी, सैद्धांतिक प्लेट, गलनक्रांतिक, लिक्विडस/सॉलिडस, अधिविभव, मिश्र विभव, निष्क्रियण, बलिदानी ऐनोड, त्रिज्य/कोणीय नोड, अणुखंड कक्षक, हाकेल विधि, अग्रांत कक्षक, दंतुरता, फ़ैक/मेर, क्रिस्टल-क्षेत्र, उच्च/निम्न चक्रण, पश्च-दान, ऑक्सीकारी योग, अपचायी विलोपन, प्रवासी निवेशन, पारधात्वन, सम-योग/प्रति-योग, ओज़ोनी-अपघटन, व्हीलैंड मध्यवर्ती, डाइऐज़ोनियम, साबुनीकरण, ईनॉल/ईनोलेट, ऐल्डोल, माइकल योग, रॉबिन्सन वलयन, विटिग, इलाइड, पश्च-संश्लेषण, सिंथॉन, लांबिक रक्षी समूह, परिक्षेपिता, टैक्टिसिटी, समविभव बिंदु, उभयाविष्ट आयन, ऐनोमर, परिवर्ती घूर्णन, वर्णलेखन, उत्क्षालन (elution; निक्षालन stays leaching), प्रतिधारण गुणांक, विभेदन, द्रव्यमान स्पेक्ट्रममिति, विखंड आयन, मैकलैफ़र्टी पुनर्विन्यास, चतुष्क कार्बन, विश्वास्यता अंतराल, अवशिष्ट, संसूचन/मात्रांकन सीमा, यथार्थता/अभिनति/परिशुद्धता, अक्रिय वायुमंडल, फ़्लैश वर्णलेखन. 413 of 417 `\index{}` keys in Hindi (LCAO, DEPT, HOMO, LUMO kept as international acronyms). One drift normalised before linking: इनोलेट → ईनोलेट (ch. 17) |
| Register / tone | **96** | Exercise stems in the आप imperative (imperative share 0.76 against 0.81 in Hindi Book 2; the remainder are question-form stems, as in English); course text impersonal; 17.7 words per danda (Book 2: 17.0); no तुम register. House forms kept (`सप्ताहांत समस्या --- …`, `भाग I --- …।`, `(अभ्यास के आँकड़े)`, solutions header `\section*{अध्याय \ref{…} --- <शीर्षक>}`, `\section{अभ्यास}`); danda at every sentence end. Commons usernames transliterated in figure credits in the body, kept in Latin on the credits page (Book 2 convention) |
| LaTeX hygiene | **97** | Forced build through the shared wrapper (`latexmk -g`): **0 errors, 0 undefined, 0 overfull, `nullfont` 0, 0 `invalid in math mode`**, `Missing character` 3 (U+000A, the run-wide baseline), `.fls` Hindi source count **70**, **359 pp** (English 373). The 35 overfull boxes of the first complete build were cleared with group-local `\emergencystretch` (3em; 8em for s26 ex. 4, s27 ex. 8, s30 problem) on the opening line of each offending environment, verified chapter by chapter against the full-book `.aux` before the final build. **−1** because Book 2 cleared its overfulls by re-flowing phrasing instead |
| Cross-refs / rule compliance | **98** | Labels, `\cref`s, solution keys, `[resume]`, math, `\ce`/`\chemfig`/schemes and ledger comments byte-identical (chemistry twin gate OK). No curriculum or country of a programme named. Shared file touched: `tools/check_hindi_prose.py`, three append-only commented allow-list entries (chemfig anchor `west`; `DIBAL-H`; `ICP-OES`/`ICP-MS`). No git command, no commit |
| Figures | **95** | Drawing code byte-identical; node text, axis labels, legends, scheme arrow labels and captions localised. `!draw` five times (EN `19` l. 240 colour-wheel `\foreach` names; `20` ll. 132–135 catalytic-step names; `23` ll. 187–188 arrow conditions; `24` l. 201 ladder names; `31` l. 78 column-snapshot captions); `17` l. 308 `endo`/`exo` `\foreach` kept Latin, as the course text does. Every translated figure rendered at 130 dpi and read (126 figure clips plus full pages for the ones the clipper cut): one fix — ch. 3 tangent-construction plot, the y label collided with the `\bar V_1` intercept label, fixed with `ylabel shift=10pt` (the English has the same collision, reported). Remaining crowding shared with English: ch. 14 CO diagram, a correlation line crosses the `σ (C का एकाकी युग्म)` label as it crosses `σ (C lone pair)`. No weekend-problem heading orphaned at a page foot |
| Solutions | **97** | All 420 exercise and 35 weekend-problem solutions native; every number of chapters 17–35 re-derived while translating (including the ch. 35 reduced-pressure boiling points from the ledger) — no numeric defect found; one wording slip in the English reported (ch. 20 solution) |
| Defined-term links (`\omterm`) | **96** | **1775 links over 181 targets** against English **1733 over 179** — every English target reached. The two extra targets are same-sense Hindi inflections English does not write in its link form: `def:b2:equilibrium-shifts:shift` (2, "साम्य का/के विस्थापन", chs 4/24) and `def:b2:reaction-enthalpy:formation` (2, plural "मानक संभवन एन्थैल्पियों", ch. 1). `book3_hi.py` curated from this edition's harvest (413 harvested, 487 linkable, 67 `DERIVED` entries carrying 69 inflected forms) with 17 `EXTRA_PROTECT` patterns for the Hindi homographs read target by target (निष्कासन = purge vs removal; संचरण = chain propagation vs propagation of uncertainty; आरंभन; वरणात्मकता of a reactor vs of a column; विभेदन vs resolving power and spectral resolution; रूपांतरण vs the eutectic transformation; कक्षक ऊर्जा; plural स्वातंत्र्य कोटियाँ left unlinked as statistical degrees of freedom), plus arrow labels and tick labels as code. `--check` clean; dry run **links to insert: 0** |
| MT-artifact freedom | **96** | Hindi prose gate **OK on 70 files**; hyphen-welded Latin tokens the gate flags (s-cis, d--d, HOMO--LUMO, C--OH, cis--trans) rewritten in house form (`s-\textit{cis}`, d–d, HOMO और LUMO, कार्बन--हाइड्रॉक्सिल, cis और trans); usernames and database names transliterated in body credits (बेंजा-बीएमएम27, वेबबुक, पबकेम). No English left in captions, nodes or arrow labels outside the internationally Latin acronyms (NMR, DEPT, HPLC, ICP-MS, LDA, HWE …) |

**Overall: 96.**

## Gate output summary

```
bash tools/check_translation.sh bachelor-2 hi
  hindi prose gate: OK (70 files)
  chemistry twin gate: OK (70 files)
  TRANSLATION GATE: PASSED

forced build, build/one_chemistry_book_3_university_year_2_hi.log
  errors 0 · undefined 0 · overfull 0 · nullfont 0 · invalid in math mode 0
  Missing character 3 (U+000A baseline)
  pages 359 (English 373) · .fls Hindi sources 70

python3 tools/link_defined_terms.py --book 3 --lang hi   -> links to insert: 0
python3 tools/link_defined_terms.py --book 3 --lang hi --check -> every file matches
\omterm 1775 / 181 targets (English 1733 / 179) · \index 417 = 417 · \emph 429 = 429
\ce 2102 = 2102 · \qty 1864 (English 1858, +6 intended)
```

## Coordinator addendum (2026-10-07)

The bare noun of the "Enolates" definition (`def:b2:enolates-aldol:enolate`) was
linked once in English and in this edition, because only the "enolate ion"
phrase was harvested; the Arabic edition exposed it. An `EXTRA` entry was added
here and in English (79 links). This edition now has **1851 links over 182
targets** (English 1,811 over 180); gates, dry run (0) and chapter-set census
re-checked. Later canon fixes carried in by the coordinator are listed in
`sources/WAVE1_FINDINGS_B34.md` and `WAVE2_FINDINGS_B34.md`. Score unchanged.

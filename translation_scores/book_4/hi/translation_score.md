# Translation score — Chemistry Book 4 · Hindi (`hi`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 4 (University Chemistry, Year 3; `parts/bachelor-3`, labels `b3`) |
| **Language** | Hindi (`hi`) |
| **Quality bar** | **native academic Hindi**: a third-year university chemistry course as it is lectured and printed in Hindi (आप register, CSTT/NCERT technical vocabulary). English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Sense / register references measured before drafting** | the English canon (content); the shipped Hindi chemistry Books 1–3 (`parts/grade-*/hi/`, `parts/bachelor-1/hi/`, `parts/bachelor-2/hi/`) for settled terminology (नाभिकरागी/इलेक्ट्रॉनरागी, किरैल, त्रिविमजनक केंद्र, अप्रतिबिंबरूपी, एनामीन, ईनोलेट, एपॉक्साइड, स्थान-रसायन, अर्ध-आयु, ऊष्मामिति, पुनश्चक्रण/निष्कासन/पाश, रुद्धोष्म ताप-वृद्धि, यथातथ/एकसमस्थानिक द्रव्यमान …), the house forms and the credits convention; `sources/TRANSLATION_BOOKS_3-4.md` and the WAVE findings |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-07 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 33 chapters + 33 solution twins = **66 files**, every body through `tools/id_apply.py`; `frontmatter/image-credits-book4.hi.tex`; a curated `tools/term_config/book4_hi.py`; the link layer; Hindi index keys; the overfull, line-edge, spelling-variant and orphan-heading sweeps; a per-figure page check of all 199 figures; and this score |

## Verdict in one line

A Hindi Book 4 that reads as a Hindi third-year chemistry course: CSTT
terminology from quantum chemistry to environmental toxicology, आप-register
imperatives in the exercises, danda punctuation, ASCII digits. Every gate is
green (prose gate and chemistry twin gate OK on 66 files), and a forced build
gives **0 errors / 0 undefined / 0 overfull / 0 invalid-in-math**, with
`nullfont` 17 and `Missing character` 23. Both are the run baselines.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Counted over all 66 files against their twins (EN = HI): `exercise` 396, `problem` 33, `solution` 429, `[resume]` 99, `omfigure` 199, `tikzpicture` 161, `axis` 108, `\node` 654, `\includegraphics` 42, `\cref` 171 + `\Cref` 34, `\label` 1183, `\item` 1118, `\chemfig` 32, `\schemestart` 13, definition 323, proposition 184, theorem 65, method 89, example 53, proof 236, remark 5, recall/inthelab/history 33 each, safety 22, `\admitted` 16, `\emph` 677, `\index` 675, `\ce` 1657, `\ghs` 80, `\qty` 1998, `\num` 197, `% ledger:` 167. `\unit` is **121 against 112**: nine bare unit words of the English prose ("mV", "meV", "mM" in ch. 1, 2, 15) are set as `\unit{…}` so that no Latin word sits in Devanagari prose. This is intended. The only post-draft layout edits are 29 group-local `\emergencystretch` settings (3em; 10em for s33 ex. 11), written into the patches |
| Terminology | **96** | Books 1–3 spellings kept, and drifts normalised before linking: इनैमीन → एनामीन, इपॉक्स- → एपॉक्स- (Book 3's defined term), स्थिति-रसायन → स्थान-रसायन, अर्धायु → अर्ध-आयु, कैलोरीमिति → ऊष्मामिति, पारद → पारा, इनॉल → ईनॉल, हेक्सेनिल → हेक्सीनिल, plus a variant pass against Books 1–3 (अभिलिखित, विलोडित, ऐल्डोल, पॉलिईन, ख़तरनाक, लुइस, बँध- …). Chapter vocabulary highlights: संकारक/अभिलक्षणिक मान, शून्य-बिंदु ऊर्जा, सीढ़ी संकारक, चक्रण-कक्षक, स्लेटर सारणिक, स्व-संगत क्षेत्र, स्थितिज ऊर्जा पृष्ठ, बिंदु समूह, अलघुकरणीय निरूपण, अभिलक्षण सारणी, समस्थानिकरूपी, अधिस्वरक/तप्त बैंड, लार्मर आवृत्ति, व्युत्क्रम जालक, विभाजन फलन, समष्टि (population), सक्रियित संकुल, प्रकाशस्थायी अवस्था, वैद्युत द्विपरत, आवर्त आवृत्ति, मिसेल, लिगैंड-क्षेत्र पद, ट्रांस प्रभाव, समपालि, ओलेफ़िन मेटाथीसिस, बैंड अंतराल, कोटर (hole), क्रोगर–विंक, पेरोव्स्काइट, एंटैटिक अवस्था, परपोषी/अतिथि, सहघूर्णी/विघूर्णी, समफलकीय/विपरीतफलकीय, मूलक घड़ी, कार्बीनॉइड, प्रवास क्षमता, प्रतिबिंबरूपी आधिक्य, पूर्वकिरैल, बलगतिक विभेदन, विषमचक्र, π-अधिशेषी/π-न्यून, माइज़नहाइमर संकुल, पूर्ण/अर्धसंश्लेषण, अभिसारी संश्लेषण, आदर्शता, सोपानी अभिक्रिया, परमाणु मितव्ययिता, E-गुणक, जीवन-चक्र मूल्यांकन, क्षारीयता (alkalinity), सुपोषण, जैवसांद्रण गुणक, खुराक–अनुक्रिया, पारिविषविज्ञान, श्लेंक लाइन, ग्लवबॉक्स, कैन्युला, मात्रात्मक NMR, शून्य परिकल्पना, सहकर्मी समीक्षा. 671 of 675 `\index{}` keys are in Hindi (COSY, HSQC, HMBC, NOESY kept as international acronyms); keys led by a Greek letter carry a Devanagari sort key (`पाई-…@$\pi$-…`) |
| Register / tone | **96** | Exercise stems use the आप imperative: the share is 0.74, against 0.69 in Hindi Book 2; the rest are question-form stems, as in English. The course text is impersonal, at 21.7 words per danda (Book 2: 20.3), with no तुम register. House forms are kept: `सप्ताहांत समस्या --- …`, `भाग I --- …।`, `(अभ्यास के आँकड़े)`, `[तर्क]`, `[आंशिक उपपत्ति]`, `[परिभाषा से]`, the `\section*{अध्याय \ref{…} --- …}` solutions header, `\section{अभ्यास}` and प्रथम/द्वितीय वर्ष का खंड. A danda ends every sentence; display punctuation stays inside the display. Commons usernames are transliterated in the figure credits of the body and kept in Latin on the credits page, the Book 2 convention |
| LaTeX hygiene | **97** | Forced build through the shared wrapper (`latexmk -g`): **0 errors, 0 undefined, 0 overfull, 0 invalid in math mode**, `nullfont` 17 and `Missing character` 23 (both the run baseline), `.fls` Hindi source count **66**, **396 pp**. Line-edge sweeps (quote or punctuation at a line edge, Latin hyphen at a line end, space before danda, `\index` before punctuation) are clean. The 29 overfull boxes of the first complete build were cleared with group-local `\emergencystretch` on the opening line of each environment or paragraph, each verified in a single-chapter probe before the final build. One long compound got a discretionary hyphen: s14 ex. 6, `डाइमेथिल\-साइक्लोब्यूटेन`. **−1** because rephrasing would have been cleaner than stretch |
| Cross-refs / rule compliance | **98** | Labels, `\cref`s, solution keys, `[resume]`, math, `\ce`/`\chemfig`/schemes and ledger comments are byte-identical; the chemistry twin gate is OK and `check_ce_balance.py` finds 59 + 45 equations with 0 problems. No programme, country or university is named. The only shared file touched is `tools/check_hindi_prose.py`, with three append-only commented allow-list entries: `cos`, the pgf-math twin of `sin`; Baldwin's `tet/trig/dig` and the `exo-/endo-` hyphenations; and `qNMR`. No git command was run and nothing was committed |
| Figures | **95** | Drawing code is byte-identical; node text, axis labels, legends, tick labels (ch. 31 `xticklabels`), scheme arrow labels and captions are localised. `!draw` was used at EN `05` l. 271, `08` l. 315, `09` l. 77, `22` l. 126, `23` ll. 74 and 83 (scheme arrows), `24` l. 106, `26` ll. 179 and 362, and `33` l. 413. All 199 figures were rendered one page per figure at 130 dpi in synctex-mapped probes and read. **Two fixes:** ch. 14, where the "photostationary 0.80/0.16" labels collided with the curves (now स्थायी 0.80/0.16); and ch. 32, where the BOD "saturation" label lost its above-headline matras to the axis clip (now सन्तृप्त, a form with no top marks). No weekend-problem heading is orphaned at a page foot: the lowest heading (2.7 on p. 31) has its box beneath it |
| Solutions | **97** | All 396 exercise and 33 weekend-problem solutions are written in native Hindi. Every number of chapters 14–33 was re-derived while translating. A scripted number census (every digit string per file, EN against HI) leaves only intended differences: वर्ष labels, "150 million" written 15 करोड़, and "18 each" written 18-18. The coordinator's canon fix to s32 items 14–15 (0.0145, 0.083) is mirrored byte for byte |
| Defined-term links (`\omterm`) | **96** | **1757 links over 259 targets**, against English **1634 over 253**; every English target is reached. The six extra targets are same-sense terms English never repeats in its link form: हैमिल्टनी संकारक, राका प्राचल, चक्रण-पारगमन, स्व-संगत क्षेत्र, साइक्लोप्रोपेनन and सोपानी अभिक्रिया. `book4_hi.py` was curated from this edition's harvest (666 harvested, 812 linkable) with: 102 `DERIVED` inflections from an inflection scan of the corpus; 3 `EXTRA` entries for सक्रियण गिब्स ऊर्जा/एन्ट्रॉपी/एन्थैल्पी, said without की; and `EXTRA_PROTECT` masks for अविभेद्य in its everyday sense (ch. 10 and its solutions, as English masks), मृदु अम्ल "mild acid" (s30, not the HSAB soft acid) and the ch. 33 TikZ node. The chapter-set census shows no target missing from any chapter where English links it. `--check` is clean and the dry run gives **links to insert: 0** |
| MT-artifact freedom | **96** | The Hindi prose gate is **OK on 66 files**. Latin tokens the gate flags were rewritten in house form: fcc → फलक-केंद्रित घनीय, p--n → p–n, bpy → बाइपिरिडीन, org → कार्बनिक, L-DOPA → L-डोपा, and Commons usernames transliterated. There is no English left in captions, nodes or arrow labels outside internationally Latin acronyms and notation (NMR, HRMS, DMAP, GHS, LLS, PMI, E-, Re/Si, exo/endo, Baldwin descriptors) |

**Overall: 96.**

## Gate output summary

```
bash tools/check_translation.sh bachelor-3 hi
  hindi prose gate: OK (66 files)
  chemistry twin gate: OK (66 files)
  TRANSLATION GATE: PASSED

forced build, build/one_chemistry_book_4_university_year_3_hi.log
  errors 0 · undefined 0 · overfull 0 · nullfont 17 · invalid in math mode 0
  Missing character 23 (run baseline)
  pages 396 (English 405) · .fls Hindi sources 66

python3 tools/link_defined_terms.py --book 4 --lang hi          -> links to insert: 0
python3 tools/link_defined_terms.py --book 4 --lang hi --check  -> every file matches
\omterm 1757 / 259 targets (English 1634 / 253) · \index 675 = 675 · \emph 677 = 677
\ce 1657 = 1657 · \qty 1998 = 1998 · \unit 121 (English 112, +9 intended)
```

## Coordinator addendum (2026-10-07)

After this edition was delivered the coordinator carried in the later English
canon fixes found by other editions (listed in `sources/WAVE1_FINDINGS_B34.md`
and `WAVE2_FINDINGS_B34.md`; the last ones: solutions/32 items 14-15 0.0145 and
0.083, solutions/02 gap 2047.98) and aligned the link layer with English, which
no longer links "indistinguishable" in its everyday sense (ch. 4 "from the
original/itself", ch. 10 orientations and sums). This edition now has **1755
links over 259 targets** (English 1,632 over 253); gates, dry run (0) and the
forced build re-checked. Score unchanged.

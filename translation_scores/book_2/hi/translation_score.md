# Translation score — Chemistry Book 2 · Hindi (`hi`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 2 (University Chemistry, Year 1; `parts/bachelor-1`) |
| **Language** | Hindi (`hi`) |
| **Quality bar** | **native academic Hindi** — a first-year university chemistry course as it is lectured and printed in Hindi (आप register, NCERT/CSTT technical vocabulary). English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Sense / register references measured before drafting** | the English canon (content); the shipped Hindi chemistry Book 1 (`parts/grade-*/hi/`) for settled terminology (कक्षक, आबंध, संरूपण, प्रतिबिंबरूपी, वक्र तीर, मंदन गुणांक, पुनःक्रिस्टलन, विद्युत-ऋणात्मकता …) and the credits convention |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-04 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 29 chapters + 29 solution twins = **58 files**, `frontmatter/image-credits-book2.hi.tex`, a curated `tools/term_config/book2_hi.py`, the link layer, Hindi index keys, the overfull and orphan-heading sweeps, a per-figure page check, and this score |

## Verdict in one line

A Hindi Book 2 that reads as a Hindi university chemistry course — CSTT
terminology, आप-register imperatives in every exercise, danda punctuation, ASCII
digits — with every structural, prose and link gate green and a forced build of
**0 errors / 0 undefined / 0 overfull / 0 nullfont**; gate 12 is red only through
a reported `id_apply` arrow-label blanking bug, and the δ of five `\ce{}` partial
charges is lost to a reported font-setup gap.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Counted over all 58 files against their twins: **348 `exercise`**, **29 `problem`**, **377 `\begin{solution}`**, **148 `omfigure`**, **96 `tikzpicture`**, **587 `\node`**, **49 `\includegraphics`**, **221 `\cref`**, **829 `\label`**, **916 `\item`**, **23 schemes**, **101 `\chemfig`**, **162 `definition` / 128 `proposition` / 109 `proof`**, **390 `\emph`**, **364 `\index`**, **1474 `\qty`**, **3432 `\ce`**, **150 `% ledger:`** — all equal to English. Every body written through `tools/id_apply.py`; the only post-write layout edits are two `\clearpage\enlargethispage{3\baselineskip}` (on the blank line before the ch. 15 and ch. 16 weekend problems, whose boxes fill a page and had left their headings alone on a blank page) and three figure-label touches (below) |
| Terminology | **96** | CSTT/NCERT chemistry: कक्षक, क्वांटम संख्या, आवरण, प्रभावी नाभिकीय आवेश, विद्युत-ऋणात्मकता, उपसहसंयोजी आबंध, अनुनाद संकर, त्रिविम संख्या, संकरण, वान्डरवाल्स/कीसोम/डिबाई/लंदन अन्योन्यक्रिया, निविड़ संकुलन, अंतराकाशी स्थल, अभिक्रिया की प्रगति, द्रव्य-अनुपाती क्रिया का नियम, अर्ध-आयु, पूर्व-साम्य/स्थायी-अवस्था सन्निकटन, हैमंड अभिगृहीत, उभयधर्मी, समतलन प्रभाव, विलेयता गुणनफल, लिगैंड, कीलेट, अर्ध-सेल, लवण सेतु, नेर्न्स्ट समीकरण, विभव--pH आरेख, अनुमापक/विश्लेष्य, प्रतिबिंबरूपी/अप्रतिबिंबरूपी, सांतरित/ग्रसित/गाउश संरूपण, विशिष्ट घूर्णन, रासायनिक विस्थापन, परिरक्षण, चक्रण--चक्रण युग्मन, प्रेरणिक/मेसोमेरी प्रभाव, समांश/विषमांश विदलन, कार्बधनायन, नाभिकरागी/इलेक्ट्रॉनरागी, निर्गामी समूह, वाल्डेन प्रतीपन, प्रति-परिसमतलीय, ज़ैत्सेव/मार्कोवनिकोव का नियम, ग्रीन्यार अभिकर्मक, ध्रुवता प्रतिलोमन, हेमीऐसीटैल, रक्षी समूह, हाइड्राइड दाता, रसायनवरणात्मक, हैलोनियम आयन, अक्रिय युग्म प्रभाव, नाइट्रोजन स्थिरीकरण, कैल्कोजन, अंतराहैलोजन, संकट/जोखिम, A-/B-प्रकार मूल्यांकन, प्रसामान्यीकृत विचलन, मंदन गुणांक. All 364 `\index{}` keys in Hindi (σ/π/β keys sorted as सिग्मा/पाई/बीटा). One drift found and normalised before linking: विद्युतऋणात्मक → विद्युत-ऋणात्मक (Book 1 spelling) in chs 18–28 |
| Register / tone | **96** | Exercise stems in the आप imperative (परिकलित कीजिए, समझाइए, दिखाइए, बताइए, लिखिए …); course text impersonal; house forms kept (`सप्ताहांत समस्या --- …`, `भाग I --- …।`, solutions header `\section*{अध्याय \ref{…} --- <शीर्षक>}`); danda at every sentence end including formula-only lines; Indian number words (करोड़/लाख) where the English says million |
| LaTeX hygiene | **98** | Forced build (`latexmk -g` under systemd-run): **0 errors, 0 undefined, 0 overfull, `nullfont` 0, 0 `invalid in math mode`**, `.fls` Hindi source count **58**, **287 pp** (English 293). 15 overfull boxes of the first build cleared by re-flowing Hindi phrasing (no `\sloppy`, no `\emergencystretch`). Line-edge sweeps clean (no line-end quote/paren, no line start on punctuation or danda, no trailing space). **−1** for the 96 `Missing character δ` lines: `\ce{A^{\delta+}…}` (ch. 2 + 2s) typesets δ in the Devanagari text face, which has no Greek; reported |
| Cross-refs / rule compliance | **98** | Labels, `\cref`s, solution keys, `[resume]`, math, `\ce`/`\chemfig`/schemes and ledger comments byte-identical. No curriculum or country of a programme named. Shared files touched: `tools/check_hindi_prose.py` (append-only allow-list, commented) and this edition's config/credits/score. No git command, no commit |
| Figures | **95** | Drawing code byte-identical; node text, axis labels, legends, `xticklabels` (ch. 26 countries) and captions localized. `!draw` twice (`16` EN l. 199 carvone `\foreach` labels; `17` EN l. 68 colour-wheel `\foreach`). Every page holding a translated figure (67 pages) rendered and read: three Hindi-specific collisions fixed in node text only — ch. 8 tangent label stacked (`\shortstack[r]`), ch. 16 ring-flip label `\scriptsize`, ch. 26 Solvay tower label shortened; ch. 17 NMR multiplicity labels kept as the international `q, s, t` (Hindi words were clipped/overlapping) with a gloss added to the caption. Remaining crowding shared with English (reported): the `heterolysis` / `1,2-shift` arrow labels wider than their arrows, the NMR `q, 2H` labels on the formulas |
| Solutions | **97** | All 348 exercise and 29 weekend-problem solutions native; every number re-derived while translating, and a scripted number-multiset comparison per solution against English: the only differences are intended (द्वितीय for "Year 2", 16 लाख for "1.6 million") |
| Defined-term links (`\omterm`) | **96** | **2676 links over 145 targets** against English **2470 over 144** — every English target reached; the extra target is screening (आवरण), which Hindi uses as a noun where English writes the verb. `book2_hi.py` curated from this edition's harvest (376 → 506 linkable, with 124 `DERIVED` entries carrying 138 inflected forms): `STOP` प्रबल/दुर्बल, one `EXTRA` (लोप की दर), 24 `EXTRA_PROTECT` patterns for the Hindi homographs (समूह before a number only, आवर्त सारणी, उभयधर्मी = amphoteric, इलेक्ट्रॉन-न्यून = electron-poor, आवरण senses, NMR बहुकता, सक्रियता की हानि, … स्थिति, जलयोजन-ऊर्जा, स्वास्थ्य संकट, GHS03 caption, sealed बंद निकाय, arrow labels and tick labels as code). Frequency and chapter-set censuses read target by target after the last edit; `--check` clean; dry run **links to insert: 0** |
| MT-artifact freedom | **96** | Hindi prose gate (gate 7) **OK on 58 files**; gate 10 0 orphan lines; `\text{}` census: all translatable subscripts translated (संदर्भ, नमूना, प्रतीपन/धारण, ईथर, ऐसीटैल, निओमेंथिल …); survivors are orbital letters s/p/d/f and frozen `\mathrm{}` subscripts (eq, tot, org, aq, front, ref, flask, aliquot, dissolved) that the math census pins |

**Overall: 96.**

## Gate output summary

```
bash tools/check_translation.sh bachelor-1 hi
  gates 1-11, 13 ............. PASSED (hindi prose gate OK, 58 files)
  gate 12 chemistry twin ..... FAILED, 5 issues -- all five are translated
                               scheme arrow labels (chs 18, 19, 20, 22, 25):
                               id_apply._blank_arrow_labels blanks a label only
                               if it has [A-Za-z]{2,}, so a Devanagari label is
                               compared byte-for-byte. With the blanking fixed
                               (any non-ASCII label blanked too) the same gate
                               reports OK (58 files). check_ce_balance: 273 eq OK

forced build, build/one_chemistry_book_2_university_year_1_hi.log (grep -a)
  '^!' 0 · undefined 0 · Overfull 0 · nullfont 0 · invalid in math mode 0
  pages 287 (English 293) · .fls Hindi sources 58
  Missing character δ (U+03B4) 96 lines -- \ce{...\delta...}, ch. 2 / 2s

python3 tools/link_defined_terms.py --book 2 --lang hi   -> links to insert: 0
\index 364 = 364 · \emph 390 = 390 · \qty 1474 = 1474 · \ce 3432 = 3432
```

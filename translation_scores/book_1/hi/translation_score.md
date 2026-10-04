# Translation score — Chemistry Book 1 · Hindi (`hi`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 1 (School Chemistry, Grades 1–12) |
| **Language** | Hindi (`hi`) |
| **Quality bar** | **native school prose at every level** — a Hindi children's science book in grades 1–5, a Hindi middle-school science textbook in grades 6–9, a Hindi senior-secondary chemistry course in grades 10–12, in the established Hindi technical vocabulary of school and university chemistry. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); `hindi_style_card.md`; the shipped Hindi editions of One Biology Book 1–5 (`../one-biology-book/parts/*/hi/`) for typography (danda, ASCII digits, decimal point), the **तुम** register of the school years and the **आप** register of the senior years; the Hindi physics editions for the shared physical vocabulary |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-04 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 49 chapters + 49 solution twins = **98 files**; `frontmatter/preface.hi.tex` (shared with Book 2 `hi`) and `frontmatter/image-credits.hi.tex`; the four chemistry box names and the periodic-table legend strings in `styles/lang/hi.tex`; the `\bookline`/`\author` lines of `one_chemistry_book_1_school_hi.tex`; a curated `tools/term_config/book1_hi.py`; the defined-term link layer; Hindi index keys; the overfull sweep (16 boxes → 0, by single-chapter probes); and this score |

## Verdict in one line

A Hindi Book 1 that reads as one Hindi school chemistry course from the first
year to the last — तुम and short sentences for the youngest readers, the
explanatory textbook register of the middle years, आप and the -इए/कीजिए
exercise stems of the senior years, the danda, and the standard Hindi
technical terms (अभिक्रिया, अभिकारक, आबंध, विलयन, विलेयता, अनुमापन,
अपचयोपचय, साम्य स्थिरांक, प्रतिबिंबरूपी, बहुलक) — with every structural,
prose and chemistry gate green over all twelve years and a forced build of
**0 errors / 0 undefined / 0 overfull / 0 nullfont / 0 invalid-in-math**, 425 pages.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted over all 98 files against their 98 twins: **665 `exercise`**, **42 `problem`**, **707 `\begin{solution}`**, **112 `[resume]`**, **260 `omfigure`**, **137 `tikzpicture`**, **25 `axis`**, **495 `\node`**, **123 `\includegraphics`**, **369 `\emph`**, **301 `\index`**, **142 `\cref`**, **1352 `\label`**, **1054 `\item`**, **2199 `\qty`**, **2267 `\ce`**, **128 `\chemfig`**, **186 `% ledger:`** comments, and per environment **184 `definition`, 115 `proposition`, 65 `method`, 155 `example`, 52 `proof`, 72 `remark`, 47 `recall`, 29 `inthelab`, 15 `history`, 23 `safety`** — all equal to English. `\label` set diff **0 / 0**. Every body was written through `tools/id_apply.py` (line-range patches kept in the agent's scratch), so every unnamed line (mathematics, chemistry, TikZ, image paths, solution keys, ledger comments) is byte-identical to English; a private pre-check added two censuses `id_apply` does not have — the **order** of `\ce` spans and of math spans inside each range (Hindi SOV order reorders them constantly) and the presence of every `% ledger:` line inside a replaced range. A per-file **number census** against English finds only intended differences: "Year 1/2 volume" → *प्रथम/द्वितीय वर्ष*, Indian numbering (*15 करोड़ टन* for 150 million t, *46 करोड़* for 460 million), distributive *3-3 प्रोटॉन* |
| Terminology | **96** | The Hindi school and university chemistry vocabulary, one glossary held across the twelve years: *शुद्ध पदार्थ / समांगी / विषमांगी मिश्रण*, *विलेय, विलायक, संतृप्त विलयन, विलेयता*, *चालना, अवसादन, निस्तारण, छानना, निस्यंद*, *अग्नि त्रिभुज, ईंधन, दहन*, *उत्क्रमणीय / अनुत्क्रमणीय / रासायनिक परिवर्तन*, *अभिकारक, उत्पाद, शाब्दिक समीकरण, संतुलित समीकरण, रससमीकरणमितीय गुणांक*, *थर्मोप्लास्टिक / थर्मोसेट, रेज़िन पहचान कोड*, *नाभिक, परमाणु क्रमांक, द्रव्यमान संख्या, समस्थानिक*, *धनायन, ऋणायन, अवक्षेप, दर्शक आयन, संक्षारण, यशदलेपन*, *आवर्त सारणी, आवर्त, समूह, उपधातु*, *पदार्थ की मात्रा, मोल, आवोगाद्रो स्थिरांक, मोलर द्रव्यमान, मोलर आयतन*, *मोलर / द्रव्यमान सांद्रता, मूल विलयन, तनुकरण गुणांक, अंशांकन श्रेणी*, *प्रगति सारणी, अधिकतम प्रगति, सीमांत अभिकारक, रससमीकरणमितीय मिश्रण*, *पतली परत वर्णलेखन, निक्षालक, मंदन गुणांक*, *लुइस संरचना, आबंधी / एकाकी युग्म, द्वि- / त्रिआबंध*, *विद्युत-ऋणात्मकता, ध्रुवीय आबंध, हाइड्रोजन आबंध, वान्डरवाल्स अन्योन्यक्रिया*, *आण्विक / अर्ध-संरचना / कंकाल सूत्र, क्रियात्मक समूह, समावयवी*, *तरंग संख्या, पारगम्यता, अंगुलिछाप क्षेत्र*, *ऑक्सीकारक / अपचायक, अपचयोपचय युग्म, अर्ध-समीकरण*, *अनुमापक, तुल्यता आयतन*, *ऊष्माक्षेपी / ऊष्माशोषी, आबंध ऊर्जा*, *रासायनिक विस्थापन, एकक / द्विक / त्रिक / चतुष्क, समाकलन वक्र*, *क्रैम निरूपण, किरैल, असममित कार्बन, प्रतिबिंबरूपी, अप्रतिबिंबरूपी, मेसो रूप, सांतरित / ग्रसित संरूपण*, *इलेक्ट्रॉन-दाता / -ग्राही स्थल, वक्र तीर, मूल चरण, अभिक्रिया मध्यवर्ती, कार्बधनायन*, *गतिक कारक, शमन, अर्ध-आयु, दर स्थिरांक*, *समांगी / विषमांगी उत्प्रेरण, उत्प्रेरक परिवर्तक*, *अभिक्रिया भागफल, साम्य स्थिरांक, अग्र / प्रतीप दिशा*, *ब्रॉन्स्टेड अम्ल, ऑक्सोनियम आयन, उभयधर्मी, जल का आयनिक गुणनफल*, *प्रभाविता आरेख, रंग-परिवर्तन परास, बफ़र विलयन*, *pH-मितीय / चालकतामितीय अनुमापन, कोलराउश नियम*, *लवण सेतु, ऐनोड / कैथोड, फ़ैराडे स्थिरांक, संचायक, विद्युत-अपघटन*, *रक्षी समूह, परमाणु मितव्ययिता, हरित रसायन, अतिक्रांतिक तरल*, *एकलक, पुनरावृत्त इकाई, बहुलकीकरण की कोटि, योगज / संघनन बहुलक*. IUPAC names transliterated as Hindi chemistry writes them (*एथेनोइक अम्ल, एथिल एथेनोएट, ब्यूटेन-2-ऑल, (Z)-ब्यूट-2-ईन, L-टार्टरिक अम्ल*), stereodescriptors and acronyms kept in Latin (Z/E, L/D, NMR, PVC, PET). All 301 `\index{}` keys rewritten in Hindi |
| Register / tone | **97** | Measured, not assumed, over course **and** solutions with an imperative census: grades 1–9 use only तुम stems (*करो, बताओ, लिखो, समझाओ, निकालो* — 4/3/7/2/9/14/37/26/41 per grade) and **0** आप stems; grades 10–12 use only आप stems (*कीजिए, बताइए, लिखिए, समझाइए, निकालिए* — 85/154/156) and **0** तुम stems. Course prose is impersonal/passive where a Hindi textbook is. Box names: *पहले से ज्ञात* (pronoun-free, so it fits both registers — changed from the coordinator's *जो आप पहले से जानते हैं*), *प्रयोगशाला में*, *इतिहास*, *सुरक्षा* |
| Typography | **97** | Danda ends every Hindi sentence (a final sweep converted the 18 copied formula-only lines that still ended on a Latin full stop); the period stays inside display mathematics and inside `\text{…}.` at the end of an equation; ASCII digits and the decimal point, as the series' siunitx setting and the shipped Hindi biology editions do; Hindi quotation in ``…''; final sweeps: **0** lines opening on punctuation or a danda, **0** dangling hyphens, **0** Hindi letter followed by a Latin full stop |
| Fidelity / accuracy | **96** | Every course paragraph, worked example, exercise and solution was translated against its twin with the numbers recomputed while translating (every grade-10 to grade-12 weekend problem re-derived: the drip bag, the airbag, the iron tablet, the ethanol burner, the breath tube, the unknown solvent, Pasteur's crystals, bromoethane, the fading dye, the 20-volume peroxide, Berthelot's ester, the ant's venom, the blood buffer, the vinegar, the phone battery, the ibuprofen routes, the PET jacket); figure data were checked where a solution reads a figure (the catalysis half-volume times, the equilibrium curves at 20 h). Where Hindi word order had to be bent to keep the `\ce`/math order frozen, the sentence was rebuilt (*X बनाम Y*, relative clauses) rather than left awkward |
| Figures | **95** | All drawing code byte-identical except **24 documented `!draw` ranges** (listed below); TikZ node text, axis labels, legends, `{\small …}` captions, `\irpanel`/`\nmrpanel` titles localized; pgfplots `symbolic coords` kept ASCII with Hindi `xticklabels`/`yticklabels` added. The `\omperiodictable` legend strings come from `styles/lang/hi.tex` (*धातुएँ, उपधातुएँ, अधातुएँ, क्षार धातुएँ, क्षारीय मृदा धातुएँ, हैलोजन, उत्कृष्ट गैसें*), checked and kept |
| Links | **96** | **5958 `\omterm` links on 174 targets** against English's **5774 on 172**: every English target is linked (**0 missing**), plus two English defines but never matches (*शमन* quenching, *यशदलेपन* galvanising). Both homograph censuses (frequency and chapter set) run after the last prose edit; dry run over the wrapped tree: **links to insert: 0** |

## Gates

`bash tools/check_translation.sh grade-N hi` for N = 1 … 12: **12 / 12 PASSED**
(structural censuses, duplicate labels, Hindi prose gate 7 — residual
English, transliterated function words, Latin full stops, spaces in math —,
orphan lines, problem numbering, gate 12 chemistry twin incl. ledger ids,
gate 13 equation balance).

Build (`latexmk -g`, forced, under the run file's memory cap):
`grep -ac '^!'` **0**, `grep -aci undefined` **0**, `grep -ac Overfull`
**0**, `nullfont` **0** (English baseline 0), `invalid in math mode` **0**;
**425 pages** (English 432); the `.fls` lists **98** Hindi chapter and solution files = **98**
on disk. The first forced build had 16 overfull boxes, all `in paragraph`
(an unbreakable `\ce`/`\chemfig`/`\qty` after a short Devanagari run, with no
hyphenation to help): each was cleared in a single-chapter probe (the book's
own preamble, the chapter counter set to the real chapter number so the
example labels have their real width) by adding short words **before** the
frozen span, never by shortening.

## `!draw` ranges (English line numbers)

g4/01 133–134 (xticklabels beside ASCII symbolic x coords) · g4/02 158–159 ·
g5/01 95–96, 105–106, 139–140 · g5/02 148–149 · g7/01 335 · g8/03 133 ·
g9/02 53–62, 168, 227–229 · g9/03 67–70 · g9/04 38 · g10/04 294–297 (`\cube`
text arguments) · g11/01 42–45 (visible colour names; xcolor fields kept) ·
g11/06 145–147 · g11/09 245 (yticklabels beside ASCII symbolic y coords) ·
g12/01 91, 95, 183–184 · g12/07 198 · g12/08 143–145 · g12/11 312, 315–317.
All are `\foreach` label lists except the three marked.

## Link layer

`tools/term_config/book1_hi.py` was curated from this edition's own `--terms`
harvest (311 harvested), an inflection scan of the Hindi corpus and a context
read of every suspicious word — never translated from `book1_en.py`.

* **DERIVED** (≈120 entries): `lang_hi.py` derives nothing, so every oblique
  or plural the bodies write (*आयनों, परमाणुओं, धातुएँ/धातुओं, अभिक्रियाएँ,
  समावयवियों…*) is declared, each read as an inflection of the same word;
  derivations that are other words (*आयनिक, एस्टरीकरण, बहुलकीकरण, अवक्षेपण,
  निस्यंदन, मोलर, नाभिकीय, जंगल*) are not.
* **STOP**: *विलयन, सामग्री, वस्तु, उत्पाद, प्रतीक, धारिता* — the English
  everyday-word rule, checked in Hindi (*धारिता* is also the buffer's capacity
  before the cell chapter defines the cell's).
* **EXTRA**: *हवा → air* (the bodies use हवा beside वायु).
* **EXTRA_PROTECT**, Hindi homographs English does not have: *समूह* only
  before a number (and masked inside the definition of *क्रियात्मक समूह*,
  where the self-link fallback would send it to the periodic table); *मिलाना*
  "to add / to match" (*मिलाना चाहिए, मिलाना या कोई, मिलाना है।*); a bulb that
  *जलता है* lights up; *जलयोजन* of ethene (grade 12 ch. 11, exercise stem and
  the solution head *जलयोजन:*), per the coordinator's English fix.

Target counts that differ most from English, each read: *जलना/दहन* 131 vs 79
(the Hindi verb forms all carry the combustion sense), *आबंध ऊर्जा* 9 vs 1
(English plural *bond energies* rarely matches its own term), *अर्ध-आयु* 26 vs
11 (English *half-lives* does not match; Hindi uses one form), *मिलाना* 6 vs 35
(Hindi has one verb for "mix" and "add": only the restated definitions link;
the noun "a mix" is *मिश्रण*, which Hindi owns by the grade-6 definition and
which cannot point at the grade-2 box without taking every later *मिश्रण*
with it), *वस्तु* 18 vs 35.

## Samples (Hindi, with verdict)

1. **Grade 1, materials** — «नाश्ते की मेज़ को देखो। उस पर एक चम्मच है, दूध का
   एक गिलास है, … मेज़ भर चीज़ें, पर बनी हैं गिनी-चुनी सामग्रियों से।» →
   **native**: तुम-imperative and the rhythm of a Hindi primer.
2. **Grade 11, redox** — «कभी इस शब्द का अर्थ था ``ऑक्सीजन से संयोग करना'';
   अब इसका अर्थ कुछ अधिक व्यापक और अधिक उपयोगी है: इलेक्ट्रॉनों का खोना।» →
   **native**: the textbook's explanatory register.
3. **Grade 12, the reaction quotient** — «यदि $Q < K$, तो निकाय अग्र दिशा में
   विकसित होता है (उत्पाद बढ़ते हैं) जब तक $Q = K$ न हो जाए» → **native**:
   *अग्र / प्रतीप दिशा* is the Hindi chemistry phrase.
4. **Grade 12, stereochemistry** — «हमारी नाक, जो स्वयं ``हस्तता'' वाले अणुओं
   से बनी है, उन्हें अलग पहचान लेती है।» → **native**.
5. **Grade 12, catalysis** — «2024 में विश्व ने लगभग 15 करोड़ टन नाइट्रोजन वाली
   अमोनिया बनाई» → **native**: Indian numbering, not a calque of "150 million".

No passage reads as machine translation: the edition was drafted directly in
Hindi against the English twin, line range by line range.

## Canon findings (reported, not fixed)

The English canon as it stands today (after the coordinator's fixes of the
items the wave-1 editions reported) gave no blocking defect in this pass;
one wording hypothesis:

1. `parts/grade-12/solutions/02-stereochemistry.tex` pb q14 — the question
   asks "Is it chiral as a whole?" of a racemic mixture; the answer replies
   about optical activity ("as a whole it is not optically active"), which is
   the observable consequence, not the property asked.

## Why not 100

* **Twenty-four `!draw` opt-outs**: each is a place where the drawing census
  no longer guards the figure, and only the rendered page does.
* **One shared file extended**: `ALLOWED_WORDS` in `tools/check_hindi_prose.py`
  (append-only, with a comment) needed the licence codes *by-sa, by-nc-sa*
  for the photograph credits to pass. Two more false positives were worked
  round in the text, not in the gate: the transliterated-article check flags
  an initial (*ए.* for "A. Loll") and the French particle *de* written *द*
  (Péan de Saint-Gilles), so the credit names the photographers in full and
  the particle is written *दे*, the common Hindi spelling (as in *दे गॉल*).
* **The grade-2 "mix" target** is reached only by its restated definitions
  (6 links against English's 35): a property of Hindi's one verb for mix and
  add, documented in the config.
* **Link density is +3 %** against English, concentrated in the combustion
  verbs and the plural forms English does not match.

# Translation score — Chemistry Book 2 · Dutch (`nl`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 2 (University Chemistry, Year 1 — year `bachelor-1`, labels `b1`) |
| **Language** | Dutch (`nl`) |
| **Quality bar** | **native academic prose**: a Dutch-language first-year university chemistry course as it is written and taught. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **References measured before drafting** | the **English** canon (content); the shipped **Dutch Book 1** of this repo (`parts/grade-*/nl/`) for series terminology (*zoutzuur*, *Beeldverantwoording*, *publiek domein*), typography (`` `` '' `` quotes, decimal point) and the **imperative** exercise stem; `sources/TRANSLATION_BOOKS_1-2.md` and `sources/WAVE1_FINDINGS.md` |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-04 |
| **Scope** | A full first translation written directly at native register (no machine draft): 29 chapters and 29 solution twins, **58 files**. Also the Dutch image-credits page, a curated `tools/term_config/book2_nl.py`, the defined-term link layer, Dutch index keys, the overfull and page-break sweeps, and this score |

## Verdict in one line

This Dutch Book 2 reads as a first-year Dutch/Flemish university chemistry
course: *reactievoortgang*, *predominante reactie*, *potentiaal-pH-diagram*,
*eenheidscel*, *coördinatiegetal*, *stationaire-toestandsbenadering*, *regel van
Klechkowski*, *genormaliseerde afwijking*; imperative exercise stems (*Bereken*,
*Schrijf … op*, *Geef*, *Toon aan*, *Leg uit*); the methods in the *Zo … je …*
voice. Every structural, chemistry, prose and link gate is green on a forced
build: **0 errors / 0 undefined / 0 overfull / 0 nullfont**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | All 58 files mirror their 58 twins. Counts (EN = NL): `exercise` 348, `problem` 29, `solution` 377, `[resume]` 87, `omfigure` 148, `tikzpicture` 96, `axis` 47, `\node` 587, `\includegraphics` 49, `\emph` 390, `\index` 364, `\cref` 221, `\label` 829, `\item` 916, `\qty` 1474, `\num` 67, `\unit` 62. Environments (EN = NL): definition 162, proposition 128, theorem 6, method 52, example 60, proof 109, remark 21, recall 29, inthelab 11, history 11, safety 2, `\admitted` 19, `% ledger:` comments 150. `\label` set diff 0. Every body went through `tools/id_apply.py` |
| Chemistry fidelity | **99** | `\ce` 3432 = 3432, `\chemfig` 101 = 101, `\schemestart` 23 = 23, `\ghs` 16 = 16, byte-identical and in order (gate 12: OK on 58 files). `check_ce_balance.py`: 125 + 148 equations, 0 problems. Never `!chem`. Word-only arrow labels translated through the census's blanking: `->[traag]`, `->[snel]`, `->[heterolyse]`, `->[(hoofdproduct)]`, `->[1,2-verschuiving]`; `->[pyridine]` is the same word |
| Terminology | **96** | The Dutch university series, settled per chapter in a glossary before drafting. Highlights: *nevenkwantumgetal*, *kwantumhokjes*, *uitsluitingsprincipe van Pauli*, *effectieve kernlading*, *lewisstructuur*, *resonantiehybride*, *sterisch getal*, *keesom-/debye-/londoninteractie*, *relatieve permittiviteit*, *dichtste stapeling*, *octaëdrische holte*, *steenzout-/zinkblende-/fluoriettype*, *reactiequotiënt*, *standaardevenwichtsconstante*, *massawerkingswet*, *halveringstijd*, *isolatiemethode*, *postulaat van Hammond*, *snelheidsbepalende stap*, *voorevenwichtsbenadering*, *amfolyt*, *nivellerend effect*, *verdelingsdiagram*, *existentiegebied*, *meertandig ligand*, *pL-schaal*, *gammaregel*, *comproportionering*, *passiveringsgebied*, *terugtitratie*, *omslagtraject*, *wet van Kohlrausch*, *weergave volgens Cram*, *ringflip*, *rechts-/linksdraaiend*, *wet van Biot*, *chemische verschuiving*, *$n + 1$-regel*, *onverzadigingsgraad*, *mesomeer effect*, *gebogen pijl*, *waldeninversie*, *solvolyse*, *antiperiplanair*, *regel van Zaitsev*, *polariteitsinversie*, *ethersynthese van Williamson*, *sulfonaatester*, *hemiacetaal*, *beschermende groep*, *ontscherming*, *oxidatieniveau*, *chemoselectieve reactie*, *haloniumion*, *carbokationomlegging*, *zoutachtig hydride*, *effect van het inerte paar*, *stikstoffixatie*, *interhalogeenverbinding*, *signaalwoord*, *gevarenaanduiding*, *voorzorgsmaatregel*, *veiligheidsinformatieblad*, *standaardonzekerheid*, *type-A-/type-B-evaluatie*, *uitgebreide onzekerheid*, *retentiefactor*. Ch. 17's NMR shielding is *magnetische afscherming*, kept distinct from ch. 2's *afscherming*: one Dutch word for both would have made the harvest drop both as defined twice. All 364 `\index{}` keys are in Dutch; every accented key carries an ASCII sort key (`metalloide@metalloïde`, `verdelingscoefficient@verdelingscoëfficiënt`, `zuur volgens Bronsted@…`) |
| Register / tone | **97** | The exercise stem is the Dutch imperative: *Bereken* ×189, *Schrijf … op* ×112, *Geef* ×60, *Teken* ×43, *Toon aan* ×34, *Leg uit* ×26, *Leid af* ×19, *Verklaar* ×16, *Maak … kloppend* ×13, *Stel voor* ×12, *Bepaal* ×10, *Vergelijk* ×9, *Voorspel* ×8. Script audit over course **and** solutions: **0 formal *u/uw*** (all 39 hits are `\omorbs{u,…}` arguments or a vector component), *je* only in the methods' *Zo … je …* voice and a few problem stems (41), *we* sparingly (9). Course text is impersonal (passive, *men*). House forms: `Weekendprobleem --- …`, `Deel I --- …`, `Wat je al weet` recall boxes, solution headers `\section*{Hoofdstuk \ref{…} --- titel}`. Cross-volume references read *Boek 1 (jaar 10)*, *het schoolboek (jaar 12)* and *het deel van jaar~2*; no programme is ever named. Calques swept at the end (*in termen van* ×5 rewritten as *als functie van*, *aan de hand van*, *op basis van*) |
| LaTeX hygiene | **99** | Forced build (`latexmk -g`, inside the memory-capped `systemd-run` scope): **0 errors, 0 undefined, 0 overfull, `nullfont` 0, 0 `invalid in math mode`**, **302 pages** (English 293). `.fls`: **58** Dutch sources, 0 English chapter files. 0 TeX accent escapes; quotes are `` `` '' ``; decimal point kept in numbers (series rule). Line edges swept after the last edit: no line-end apostrophe, no line start on `. , ; : ) ? !` or `~;`/`~:`/`~?`/`~!`; the three line-end hyphens are Dutch suspended compounds (*koper- en uraniumertsen*, *zink- en aluminiumhydroxide*, *neerslag- (of zuur-base-)evenwichten*). No `%` hides a line break. All files valid UTF-8 |
| Cross-refs / rule compliance | **99** | Labels, `\cref` targets, solution keys, `[resume]`, math spans, image paths and `% ledger:` comments byte-identical to English. No programme, curriculum, country or university name in visible text. No English source, preface or other edition touched; **no shared tool edited** (no allow-list entry was needed). No repo-wide git command, no commit |
| Figures | **96** | All TikZ / pgfplots / chemfig code byte-identical except the two `!draw` ranges listed below; only node text, axis labels, legends, `yticklabels` (the ch. 26 lithium bar chart: *Brazilië, Argentinië, Chili, Australië*) and captions localized. One label shortened for width (ch. 28 contact process: *deels terug*, which had pushed the picture 21 pt past the margin). The ch. 29 distillation labels needed no anchor change: Dutch says *water in / water uit* |
| Solutions | **97** | All 348 exercise solutions and 29 weekend-problem solutions present and native. Every number in ch. 1–29 was recomputed while translating (Solvay, Bayer, contact process, Ostwald, MTBE, Grignard and adipic-acid yields, the lithium-brine balance, the uncertainty budgets, the extraction limit with its 32 portions). Every multi-line math span keeps its exact English line break. Gate 11 (problem numbering) green |
| Defined-term links (`\omterm`) | **95** | **2493 links over 146 distinct targets**, against English's **2470 over 144**. **Every target English links is reached**; Dutch also reaches two English never links (*nevenkwantumgetal / hoofdkwantumgetal* in ch. 1–2, and *ethersynthese van Williamson* in the ch. 22 problem). `book2_nl.py` was curated from this edition's own harvest (387 harvested terms on the same 169 targets as English, 484 linkable after curation), never seeded. `--apply` twice changes nothing; the plain dry run reports **links to insert: 0** |
| MT-artifact freedom | **96** | Gate 10 (orphan lines): **0**. Gate 9 (twin prose comparison): **0 blocking findings**, 38 advisory one-word findings, all read: eponyms and symbols (*Lyman, Balmer, Paschen, Fischer, Cram, Pauling*), true Dutch cognates (*syn, anti, gauche, flip, oleum, aluminium, ethanol, aldehyde, ether, Water, Lithium, Magnesium, Alkoxide, exact, water in*), the subscripts `inv/ret`, and the nodes *complex 1–3*. A twin-identity sweep (`same.py`, every Dutch line identical to an English line that still carries words) found two `@=` ranges that had copied English prose (solutions 24 and 29) — fixed. The `\text{}`/`\mathrm{}` census translated every translatable subscript (*beginstoffen/producten*, *overmaat*, *waarde*, *acetaal*, *afstand afgelegd door …*, *SWE*, `\mathrm{kolf}`, `\mathrm{opgelost}`); survivors are symbols (`\mathrm{eq}`, `ref`, `tot`, `org`, `front`, `inv`, `ret`) |

**Overall: 96.** The weighting favours terminology, register, link curation and MT-artifact freedom; structure and build are gated mechanically.

## Gate output summary

```
bash tools/check_translation.sh bachelor-1 nl ............ TRANSLATION GATE: PASSED
  gates 1-8, 10, 11, 13 .... green (completeness, labels, exercise/solution
                             parity, environment census, hygiene, UTF-8,
                             orphan lines 0, problem numbering, ce balance)
  gate 9 ................... no multi-word findings; 38 one-word (advisory, read)
  gate 12 .................. chemistry twin gate: OK (58 files)

forced build build/one_chemistry_book_2_university_year_1_nl.log (grep -a)
  '^!' 0 · undefined 0 · Overfull 0 · nullfont 0 (baseline 0)
  'invalid in math mode' 0 · pages 302 (EN 293) · .fls nl sources 58, EN 0

python3 tools/link_defined_terms.py --book 2 --lang nl     -> links to insert: 0
\index 364 = 364 · \label set diff 0 · \qty 1474 = 1474 · \ce 3432 = 3432
```

## The link layer: what the censuses found

Frequency and chapter-set censuses against the English twin were run after
the last prose edit and after the link layer; every flag was read in context.

Dutch homographs met **after** their definition, each masked in `book2_nl.py`:

- **Bare adjectives** *sterk / sterke / zwak / zwakke* are stoplisted **and** dropped (as French found, stoplisting alone falls through to the per-chapter map); the plurals and inflections of the four acid-strength terms are restored through `EXTRA`.
- ***groep*** links only before a number, excluding *vertrekkende / beschermende groep*.
- ***multipliciteit*** in its NMR sense (three ch. 17 phrases).
- ***hydratatie*** of the smaller halide ions (ch. 28), not the alkene hydration.
- ***axiale / equatoriale posities*** (VSEPR, ch. 28).
- ***bescherming*** as personal protection (ch. 29, three phrases); ***\emph{Gevaar}*** as the signal word.
- ***kwantitatief*** as an adverb of a theory or a measurement (*kwantitatief gemaakt*, *elektronen kwantitatief*, *kwantitatieve meting*).
- ***eindpunt*** of an experiment or of a problem; ***activiteit*** that disappears (optical, ch. 19); ***katalysator van de auto*** (ch. 9).
- ***koolstof-metaalbinding*** (ch. 21): the HEAD rule turned it into the metallic bond of ch. 5.
- ***niet mengbaar*** (English never links *immiscible*).

Forms the harvest cannot derive, added to `EXTRA` (each a real occurrence):
Dutch consonant doubling and irregular plurals (*waterstofbruggen*,
*kristallen*, *subschillen*, *acetalen*, *radicalen*, *oxidatiegetallen*,
*standaardpotentialen*, *resonantiestructuren* …), inflected adjectives of
multi-word terms (*polaire oplosmiddelen*, *ongepaarde elektronen*, *zure
oxiden*, *antiperiplanaire* …), the everyday short forms *vrij paar / vrije
paren / bindend paar* of the defined *vrij / bindend elektronenpaar*, and the
synonyms the definitions themselves give (*meerwaardig zuur*, *effect van het
gemeenschappelijke ion*). Without them hydrogen bonds fell from 41 English
links to 3.

Five sentences were reworded so a defined term could carry its link
(*opbrengst → rendement* in ch. 27, *ontwatering → dehydratatie* in ch. 28,
*interstitiële plaatsen van het metaalrooster → interstitiële holten van het
rooster van het metaal* in ch. 26, the ch. 12 *edtachelaat* compounds split,
and a wrong-sense *fase* in solution 23 rewritten as *stadium*); one wrong-sense
link was removed by rewording (*een zwak zuur product → een licht zuur
product*, ch. 14, which is "weakly acidic", not "a weak acid").

Largest remaining deficits, all Dutch compounds the word boundary rightly
refuses to enter: `lewis` 150 vs 162 (*elektronenparen* inside compounds),
`hemiacetal` 43 vs 50, `complex` 59 vs 65 (*hydroxocomplexen*,
*broomcomplex*), `crystal` 33 vs 39, `system` 14 vs 20 (*waterfase*,
*gasfase*), `orbital` 37 vs 43.

## Samples (Dutch, with verdict)

1. **ch. 7**, the reaction quotient: ``het product van de activiteiten van de reactieproducten gedeeld door dat van de beginstoffen, elk verheven tot de macht van zijn stoichiometrisch getal''. **Native.**
2. **ch. 22**, Williamson: ``Omvangrijk aan de kant van het alkoxide, klein aan de kant van het halogenide.'' **Native.** The verbless closing maxim of a Dutch practicum handout.
3. **ch. 23**, protection: ``Bescherming is een strategie, geen reflex.'' **Native.**
4. **ch. 27**, Haber: ``de chemie die de helft van de mensheid voedt en de chemie die doodt, worden gescheiden door de keuzes van chemici''. **Native.**
5. **ch. 29**, the two students: ``een meting is pas iets waard met haar onzekerheid, en een vergelijking pas met een regel''. **Native.** *pas … pas* carries the English emphasis.

## Edits outside the patch applier (recorded)

- **`!draw` ranges, two:** `bachelor-1/16`, EN line 199 (the carvone `\foreach` labels, *groene munt / karwij*); `bachelor-1/17`, EN line 68 (the colour wheel `\foreach`).
- **Post-apply prose edits** (all inside the Dutch files only, after the link layer, then relinked): the link rewordings listed above; overfull clearing in `nl/03` (proof lead and the `\text{bindingselektronen}` subscript), `nl/06` (comparison table: *hoogsmeltend / laagsmeltend*), `nl/08` (example lead), `nl/09` (proof lead), `nl/13` (`koper(II)\-sulfaat`), `nl/17` (`over\-een\-komt`), `nl/28` (contact-process label), solutions 20 (×2) and 21; five calques.
- **One page-break hint:** `nl/29`, before `\section{Scheiden}`: `\par\vspace{0pt plus 8\baselineskip}\penalty-200\vspace{0pt plus -8\baselineskip}` with a comment. It breaks only when fewer than about eight lines remain (the heading had been orphaned at the foot of p. 241 above an unbreakable definition box) and the two glues cancel otherwise, so it stays correct when CI's Dutch hyphenation moves the page breaks.

## Suspected English-canon defects (reported, not fixed)

No numerical defect was found in ch. 1–29 (every solution recomputed). The
English **link layer** has wrong-sense links that `book2_en.py` does not mask:

1. `parts/bachelor-1/09-elementary-steps.tex`, line 194: "a short induction \omterm{…periodicity:table}{period}" links a time period to the periodic-table definition.
2. `parts/bachelor-1/14-e-ph-diagrams.tex`, lines 5, 24, 294, 367: "\omterm{…periodicity:table}{blocks} of zinc", "The grey blocks", "The zinc block", "block" — sacrificial anodes linked to the s/p/d/f block.
3. `parts/bachelor-1/19-nucleophilic-substitution.tex`, line 238: "three groups \omterm{…periodicity:table}{block} it" — the verb.
4. `parts/bachelor-1/13-nernst.tex`, line 10: "makes the exchange of electrons \omterm{…extent-q-and-k:quantitative}{quantitative}", and `15-titration-methods.tex`, line 25: "the most common quantitative measurement" — the adjective, not the defined quantitative reaction (the same class as the "made quantitative" mask already in `book2_en.py`).

The Dutch edition masks all of these.

## Gate / tool bugs met

None new in this run. The `\pgfmathprintnumber` strip the French agent added
to `check_latin_prose.py` was already in place; the Dutch edition needed no
allow-list entry. Local TeX Live has no Dutch hyphenation patterns, so the
local build hyphenates Dutch with English patterns (e.g. *mag-ne-s-iu-malkox-ide*);
the overfull sweep was done under that handicap, and CI's real Dutch patterns can
only loosen it. Worth knowing for every `nl` edition.

## Why not 100

- **Link density** is at parity (2493 vs 2470) but distributed differently: Dutch compounds hide some links English has (*waterfase*, *hydroxocomplexen*), and the short forms *vrij paar* carry links English spreads over *lone pair*.
- **Two drawing exceptions** (`!draw` ranges) leave those figures guarded only by the rendered PDF.
- **One page-break hint** in ch. 29 is layout, not text, and was added by hand.
- **Hyphenation**: the build was cleared with English hyphenation patterns; three explicit `\-` hints remain in the text (`koper(II)\-sulfaat`, `over\-een\-komt`, `magnesium\-alkoxide`) plus `2-broom-2-methyl\-butaan`, harmless under Dutch patterns.
- **Register** was audited by script (stems, *u/je/we*, calques), but a few long proofs still follow the English sentence boundaries more closely than a Dutch author would.

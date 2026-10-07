# Translation score — Chemistry Book 4 · Dutch (`nl`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 4 (University Chemistry, Year 3 — year `bachelor-3`, labels `b3`) |
| **Language** | Dutch (`nl`) |
| **Quality bar** | **native academic prose**: a Dutch-language third-year university chemistry course as it is written and taught. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **References measured before drafting** | the **English** canon (content); the shipped **Dutch Books 1–2** of this repo (`parts/grade-*/nl/`, `parts/bachelor-1/nl/`) for series terminology (*Beeldverantwoording*, *publiek domein*, *beschermende groep*, *disconnectie*, *robinsonannulatie*), typography (`` `` '' `` quotes, decimal point), cross-volume references (*Boek 1 (jaar 11)*, *het deel van jaar~2*) and the **imperative** exercise stem; the in-progress Dutch Book 3 (`parts/bachelor-2/nl/`) for the lower-case eponym compounds (*diels-alderreactie*) and the prefix style of orbital symbols (*$d$-orbitaal*); `sources/TRANSLATION_BOOKS_3-4.md` and its reading list |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-06 |
| **Scope** | A full first translation written directly at native register (no machine draft): 33 chapters and 33 solution twins, **66 files**, every body through `tools/id_apply.py`. Also the Dutch image-credits page (`frontmatter/image-credits-book4.nl.tex`), a curated `tools/term_config/book4_nl.py`, the defined-term link layer, Dutch index keys, the overfull, page-break, figure and line-edge sweeps, and this score |

## Verdict in one line

This Dutch Book 4 reads as a third-year Dutch/Flemish university chemistry
course: *toestandssom*, *karaktertabel*, *irreducibele representatie*,
*symmetrieaangepaste combinatie*, *franck-condonprincipe*, *jablonskidiagram*,
*kwantumopbrengst*, *geactiveerd complex*, *zadelpunt*, *bedekkingsgraad*,
*elektrische dubbellaag*, *zetapotentiaal*, *ligandveldterm*,
*tanabe-suganodiagram*, *isolobale analogie*, *agostische interactie*,
*ladingsdragers*, *doteerstof*, *disconnectie*, *langste lineaire reeks*,
*levenscyclusanalyse*, *schlenklijn*, *handschoenkast*, *hiërarchie van
beheersmaatregelen*; imperative exercise stems (*Bereken*, *Geef*, *Toon aan*,
*Schrijf … op*, *Voorspel*, *Schat*, *Bepaal*); methods in the *je* voice;
an impersonal course text. Every structural, chemistry, prose and link gate is
green on a forced build: **0 errors / 0 undefined / 0 overfull**, `nullfont` and
"Missing character" at the English baseline (17 / 17).

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | All 66 files mirror their 66 twins. Counts (EN = NL): `exercise` 396, `problem` 33, `solution` 429, `[resume]` 99, `omfigure` 199, `tikzpicture` 161, `axis` 108, `\node` 654, `\includegraphics` 42, `\emph` 677, `\index` 675, `\cref` 171, `\Cref` 34, `\label` 1183, `\item` 1118, `\qty` 1997, `\num` 197, `\unit` 112. Environments (EN = NL): definition 323, proposition 184, theorem 65, method 89, example 53, proof 236, remark 5, recall 33, inthelab 33, history 33, safety 22, `\admitted` 16, `% ledger:` comments 167. No duplicate index key. Every body went through `tools/id_apply.py` |
| Chemistry fidelity | **99** | `\ce` 1657 = 1657, `\chemfig` 32 = 32, `\schemestart` 13 = 13, `\ghs` 80 = 80, byte-identical and in order (gate 12: OK on 66 files); gate 13 (balance) green. Never `!chem`. Word arrow labels translated through the census's blanking (27: `->[peroxyzuur][Baeyer-Villiger]`; 14 and 23 word labels); after the coordinator's brace-aware parser, the word parts of mixed labels too (27: `->[singulet $\ce{CH2}$]`; 29: `->[{[3,3]}, dan][cyclisatie, $-\ce{NH3}$]`). `$\ce{H2SO4}$ (oleum)` is the same word |
| Terminology | **96** | Settled per chapter in a glossary against Books 1–2 before drafting. Series terms kept (*disconnectie*, *robinsonannulatie*, *beschermende groep*, *hexatrieen/butadieen* without diaeresis as in Book 2). Highlights: *uitwisselingsintegraal*, *spinorbitaal*, *minimale basisset*, *gecontraheerde gaussfunctie*, *dichtheidsfunctionaaltheorie*, *schoenfliessymbool*, *direct product*, *IR-actief / Raman-actief*, *regel van wederzijdse uitsluiting*, *morsepotentiaal*, *vibronische koppeling*, *interne conversie*, *intersystem crossing* (the term Dutch chemists use), *stokesverschuiving*, *rotatieramanspectrum*, *karakteristieke rotatietemperatuur*, *thermische golflengte*, *fractioneringsfactor*, *flitsfotolyse*, *fotostationaire toestand*, *chemische actinometer*, *vergelijking van Tafel*, *piekstroom*, *helmholtzlaag*, *oppervlakte-excesconcentratie*, *debyelengte*, *hamakerconstante*, *magnetische susceptibiliteit*, *spin-crossover*, *mechanisme van de geconjugeerde base*, *elektronenoverdracht via de buiten-/binnensfeer*, *kegelhoek van Tolman*, *model van Dewar-Chatt-Duncanson*, *notatie van Kröger-Vink*, *netwerkwijzigers*, *pn-overgang*, *acceptorniveau*, *michaelisconstante*, *enaminekatalyse*, *fotoredoxkatalyse*, *aromatische overgangstoestand*, *ene-reactie*, *idealiteit*, *systeemgrens*, *biochemisch zuurstofverbruik*, *dosis-responsrelatie*. Eponyms follow the series rule (lower case in compounds: *wittigreactie*, *diels-alderreactie*, *baeyer-villigeroxidatie*, *jahn-tellereffect*, *hartree-focktheorie*; a capital only at a sentence or title start); orbital and configuration symbols take the Dutch prefix form (*$\pi^*$-orbitaal*, *$d^3$-ion*, *$\sigma$-binding*) except where the symbol is a summation index. All 675 `\index{}` keys are Dutch; accented keys carry ASCII sort keys |
| Register / tone | **97** | Exercise stems in the Dutch imperative, measured against Book 2 nl: *Bereken* ×130, *Geef* ×49, *Toon aan* ×25, *Schrijf … op* ×15, *Voorspel* ×15, *Bepaal* ×14, *Schat* ×14, *Stel … op* ×13, *Leid … af* ×12, *Verklaar* ×7, *Vergelijk* ×7, *Leg uit* ×7. Script audit over course **and** solutions: **0 formal *u/uw*** (every hit is math or TikZ code), *je* 27 (methods and problem stems), *we/ons* 24, sparingly. House forms as Book 2: `Weekendprobleem --- …`, `Deel I --- …`, `Wat je al weet`, solution headers `\section*{Hoofdstuk \ref{…} --- titel}`, *Beargumenteerd.* / *Gedeeltelijk bewijs.* proof heads. No programme, country or university named |
| LaTeX hygiene | **99** | Forced build through `build.sh` (memory-capped scope): **0 errors, 0 undefined, 0 overfull, `nullfont` 17 (= English), "Missing character" 17 (= English), 0 `invalid in math mode`**, **424 pages** (English 405). `.fls`: **66** Dutch sources. Quotes `` `` '' ``; decimal point kept. Line edges swept after the last edit: no line-end apostrophe, no line start on `. , ; : ) ? !` or `~;`; the only prose line-end hyphens are Dutch suspended compounds (*vibratie- en …*, ch. 1 and 10); every other line-end `-` is a minus inside a math span that keeps the English line break |
| Cross-refs / rule compliance | **99** | Labels, `\cref` targets, solution keys, `[resume]`, math-span order, image paths and `% ledger:` comments byte-identical to English. No English source, other edition or shared tool touched; no allow-list entry needed. No repo-wide git command, no commit |
| Figures | **96** | All TikZ / pgfplots / chemfig code byte-identical except the `!draw` ranges below; node text, axis labels, legends and captions localized. Every translated figure checked one page per figure at 130 dpi (300 dpi where a collision was suspected). Fixed on that pass: ch. 7 Franck–Condon labels (*grondtoestand* clipped by the axis, *aangeslagen* on the curve: nodes moved), ch. 14 *trechter* on the S$_1$ curve and the wavy arrow head (node raised), ch. 31 LCA box *einde levensduur* touching the cradle-to-grave boundary (now *levenseinde:\\ recycling,\\ verwijdering*), ch. 9 and ch. 26 weekend-problem pages (shortened so the `\enlargethispage` box fits) |
| Solutions | **96** | All 396 exercise solutions and 33 weekend-problem solutions present and native. A scripted re-read compared the number sequence of every file with its English twin (`\omterm`, labels and ledger ids stripped): every difference is a Dutch word-order move, a figure coordinate listed below, or *één enkele band* for "a band count of 1"; no number changed. Multi-line math spans keep their exact English line breaks. Gate 11 (problem numbering) green |
| Defined-term links (`\omterm`) | **95** | **1538 links over 259 distinct targets**, against English's **1632 over 252**. **Every target English links is reached**; Dutch also reaches seven English never links, each read in context and correct: *schrödingervergelijking* (×10), *activeringsvolume*, *chirale hulpgroep*, *blauwe koperproteïnen*, *elektronenoverdracht via de binnensfeer*, *agostische interactie*, *spin-crossover*. `book4_nl.py` was curated from this edition's own harvest (736 harvested terms, 776 linkable), never seeded. `--unwrap --apply` then `--apply`; the plain dry run reports **links to insert: 0** |
| MT-artifact freedom | **96** | Gate 10 (orphan lines): 0. Gate 9: **no multi-word finding**; 48 advisory one-word hits, all read: eponyms (*Slater, Rayleigh, Stokes, Scherrer, Langmuir, Schottky, Frenkel, Brusselator, Lotka--Volterra, Cope/Claisen*), true Dutch words (*Status, Water, Commutator, Pyridine, E-factor, epoxide, aziridine, compressor, sediment, guanine, cytosine, diameter, maximum, convergent, deuteron, zigzag*), *fcc(111)*, *7-dehydrocholesterol*, and the subscripts `direct`, `donor`, `complex`, `ring`, `org`, `equiv.`. The `\text{}`/`\mathrm{}` census translated every translatable subscript (*eind*, *gem/ber*, *nul*, *vrij/geb*, *lucht/uitl*, *spin-only* kept as the Dutch technical term) |

**Overall: 96.** The weighting favours terminology, register, link curation and MT-artifact freedom; structure and build are gated mechanically.

## Gate output summary

```
bash tools/check_translation.sh bachelor-3 nl ............ TRANSLATION GATE: PASSED
  gates 1-8, 10, 11, 13 .... green
  gate 9 ................... no multi-word findings; 48 one-word (advisory, read)
  gate 12 .................. chemistry twin gate: OK (66 files)

forced build build/one_chemistry_book_4_university_year_3_nl.log
  errors 0 · undefined 0 · overfull 0 · nullfont 17 · missing character 17
  invalid in math mode 0 · pages 424 (EN 405) · .fls nl sources 66

python3 tools/link_defined_terms.py --book 4 --lang nl     -> links to insert: 0
```

## The link layer: what the censuses found

Frequency and chapter-set censuses against English were run after the last
prose edit; every flag was read in context. The high-frequency flags are the
right sense: *bedekkingsgraad* 22 vs 4 (English writes "θ" where Dutch writes
the word), *labjournaal* 8 vs 3, *anharmonisch* 12 vs 5, *zadelpunt* 8 vs 3,
*totaalsynthese* 6 vs 3.

Dutch homographs met **after** their definition, masked in `book4_nl.py`:
*karakter* (of a representation / the $s$, $d$ or $\pi^*$ character of an
orbital / the bond-breaking character of a mechanism), *bezetting* (Boltzmann
population / occupancy of orbitals or of a Fermi level), *operator* (quantum /
plant operators), *gat* (semiconductor hole / a hole in a $d$ shell or a ring),
*migratie* (ionic migration / migration of a group), *sol* (colloid / *sol-gel*),
and the Maxwell–Boltzmann speed distribution (English does not link it to the
Boltzmann distribution either). Irregular plurals the word tail cannot derive
(*carbenen*, *micellen*, *ketenen*, *heterocycli*) and inflected multi-word
forms (*geactiveerde complex(en)*, *roterende assenstelsel*, *isothermen van
Langmuir*, *hernieuwbare grondstoffen*, *harde en zachte zuren*) are in `EXTRA`.
The chemfig `\setchemfig{}`/`\arrow{}` arguments and `xticklabels` lists are
protected.

## `!draw` ranges (English file:line)

- `bachelor-3/05`, 271 — water normal-mode `\foreach` labels (*symmetrische strekvibratie, buigvibratie, …*).
- `bachelor-3/07`, 171–173 — Franck–Condon *aangeslagen* / *grondtoestand* nodes repositioned (clipped and colliding in Dutch).
- `bachelor-3/08`, 315 — pulse-sequence names.
- `bachelor-3/09`, 77 — *kubisch P/I/F*.
- `bachelor-3/14`, 128 — *trechter* node raised off the S$_1$ curve.
- `bachelor-3/22`, 126 — *metaal / halfgeleider / isolator*.
- `bachelor-3/24`, 106 — *deoxy (hoogspin) / oxy (laagspin)*.
- `bachelor-3/26`, 179 — *disrotatorisch / conrotatorisch … behouden*; 288–291 and 303–306 — the *bindend / antibindend* nodes, written `at (x,y) [left] {text}`, whose text `id_apply`'s draw census does not blank.
- `bachelor-3/33`, 413 — hierarchy of controls.

## Suspected English-canon defects (reported, not fixed)

1. `parts/bachelor-3/02-many-electron-atoms.tex`, ~line 396: the spin–orbit constant is printed $A = 11.46$ cm$^{-1}$, but $\frac23 \times 17.20 = 11.467$, and the solution to exercise 6 prints 11.47.
2. `parts/bachelor-3/solutions/08-advanced-nmr.tex`, line 88 (weekend problem, answer 11): "A \ce{CH2}--\ce{CH3} bond joining the two methyls' neighbours: impossible here." The question asks what a cross peak between 0.95 and 1.25 ppm — the two **methyl** signals — would have meant: that the two methyls are coupled, i.e. adjacent (a CH$_3$–CH$_3$ unit), which is impossible here. As written the answer names a CH$_2$–CH$_3$ bond, which the molecule does contain twice. The Dutch follows the English until the canon is fixed.
3. `parts/bachelor-3/08-advanced-nmr.tex`, 437–438: "two- dimensional" (line-end hyphen + space) — already fixed by the coordinator.

## Gate / tool bugs met

- **`id_apply.py` draw census**: node text written `\node[...] at (x,y) [left] {text};` (options after the coordinate) is not blanked, so translating it costs a `!draw` (ch. 26).
- **Gate 9 `dup` check**: two legitimately identical English solution lines (solutions 05, items 13/14) trip the duplicate-line check in the twin; worked round by prefixing *IR-actief:* / *Raman-actief:*.
- **Mixed arrow labels** were frozen whole until the coordinator's brace-aware parser (now fixed).
- Not a tool bug, a trap: an `EXTRA_PROTECT` pattern that consumes a `$` (`gat\s+in\s+\$`) silently masks the whole following span, so links disappear without any error; use a look-ahead.
- Local TeX Live has no Dutch hyphenation patterns; the overfull sweep was done with English patterns (CI can only loosen it).

## Why not 100

- **Link density** is below English (1538 vs 1632) because Dutch welds compounds the word boundary rightly refuses to enter (*ligandveldsplitsing*, *metaalkatalysatoren*, *halfgeleiderlagen*), though every English target is reached.
- **Eleven `!draw` ranges** leave those figures guarded only by the rendered PDF.
- **Hyphenation**: cleared with English patterns locally.
- A few long proofs still follow the English sentence boundaries more closely than a Dutch author would.

## Coordinator addendum (2026-10-07)

After this edition was delivered the coordinator carried in the later English
canon fixes found by other editions (listed in `sources/WAVE1_FINDINGS_B34.md`
and `WAVE2_FINDINGS_B34.md`; the last ones: solutions/32 items 14-15 0.0145 and
0.083, solutions/02 gap 2047.98) and aligned the link layer with English, which
no longer links "indistinguishable" in its everyday sense (ch. 4 "from the
original/itself", ch. 10 orientations and sums). This edition now has **1537
links over 259 targets** (English 1,632 over 253); gates, dry run (0) and the
forced build re-checked. Score unchanged.

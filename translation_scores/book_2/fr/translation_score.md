# Translation score — Chemistry Book 2 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 2 (University Chemistry, Year 1 — years `bachelor-1`, labels `b1`) |
| **Language** | French (`fr`) |
| **Quality bar** | **native academic prose**: a French first-year university chemistry course as it is written and taught. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **References measured before drafting** | the **English** canon (content); the shipped **French Book 1** of this repo (`parts/grade-*/fr/`) for series terminology (*rapport frontal*, GHS codes kept as `GHS0n`), typography and the **infinitive** exercise stem; `sources/TRANSLATION_BOOKS_1-2.md` and `sources/WAVE1_FINDINGS.md` |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-04 |
| **Scope** | A full first translation written directly at native register (no machine draft): 29 chapters and 29 solution twins, **58 files**. Also the French image-credits page, a curated `tools/term_config/book2_fr.py`, the defined-term link layer, French index keys, the overfull and figure sweeps, and this score |

## Verdict in one line

This French Book 2 reads as a French L1 / first-year chemistry course. It uses:

- the vocabulary of the French tradition: *avancement*, *réaction prépondérante*, *diagramme potentiel–pH*, *maille*, *coordinence*, *AEQS*, *règle de Klechkowski*, *écart normalisé*;
- the infinitive exercise register;
- French spaced punctuation.

Every structural, chemistry, prose and link gate is green on a forced build: **0 errors / 0 undefined / 0 overfull / 0 nullfont**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | All 58 files are an exact mirror of their 58 twins. Counts (EN = FR): `exercise` 348, `problem` 29, `solution` 377, `[resume]` 87, `omfigure` 148, `tikzpicture` 96, `axis` 47, `\node` 587, `\includegraphics` 49, `\emph` 390, `\index` 364, `\cref` 221, `\label` 829, `\item` 916, `\qty` 1474, `\num` 67, `\unit` 62. Environments (EN = FR): definition 162, proposition 128, theorem 6, method 52, example 60, proof 109, remark 21, recall 29, inthelab 11, history 11, safety 2, `\admitted` 19, `% ledger:` comments 150. The `\label` set diff is 0. Every file was written through `tools/id_apply.py` |
| Chemistry fidelity | **99** | `\ce` 3433 = 3433, `\chemfig` 101 = 101, `\schemestart` 23 = 23, `\ghs` 16 = 16, all byte-identical in order (gate 12, chemistry twin: OK on 58 files). `check_ce_balance.py`: 125 + 148 equations, 0 problems. Never `!chem`. Arrow labels translated through the census's word-only blanking: `->[lente]`, `->[rapide]`, `->[hétérolyse]`, `->[(majoritaire)]`, `->[migration]` |
| Terminology | **96** | The standard French university series, settled per chapter. Highlights: *niveau d'énergie*, *cases quantiques*, *charge nucléaire effective*, *schéma de Lewis*, *formule mésomère*, *nombre stérique*, *coordinence*, *compacité*, *habitabilité*, *type blende / fluorine / sel gemme*, *avancement*, *taux d'avancement final*, *quotient de réaction*, *loi d'action des masses*, *temps de demi-réaction*, *méthode d'isolement*, *AEQS*, *étape cinétiquement déterminante*, *réaction prépondérante*, *solution équivalente*, *effet nivelant*, *échelle de pL*, *relation de Nernst*, *électrode standard à hydrogène*, *médiamutation*, *domaine de passivation*, *titrage en retour*, *loi de Kohlrausch*, *représentation de Cram*, *chaise / inversion de chaise*, *dextrogyre / lévogyre*, *loi de Biot*, *déplacement chimique*, *règle des n + 1*, *nombre d'insaturations*, *effet mésomère*, *inversion de Walden*, *solvolyse*, *antipériplanaire*, *règle de Zaïtsev*, *inversion de polarité*, *alcoolate*, *synthèse de Williamson*, *ester sulfonique*, *hémiacétal*, *groupe protecteur*, *niveau d'oxydation*, *réaction chimiosélective*, *ion halogénonium*, *réarrangement de carbocation*, *hydrure salin*, *effet de paire inerte*, *composé interhalogéné*, *mention d'avertissement*, *conseil de prudence*, *fiche de données de sécurité*, *incertitude-type*, *évaluation de type A / B*, *incertitude élargie*, *rapport frontal*. Ch. 18's *intermédiaire réactif* is deliberately kept distinct from ch. 9's *intermédiaire réactionnel*: one French word for two English terms would have made the harvest drop both as defined twice. All 364 `\index{}` keys are in French, and every accented key has an ASCII sort key. The 21 keys identical to English are true cognates (*ligand*, *anode*, *chiral*, *carbocation*, *absorbance*, *tosylate*, *protection*…) |
| Register / tone | **97** | The exercise stem is the French infinitive: *Calculer* ×205, *Écrire* ×134, *Donner* ×66, *Expliquer* ×54, *Montrer* ×37, *Dessiner* ×37, *Prévoir* ×17, *Proposer* ×16, *Comparer* ×15, *Tracer* ×14, *Déterminer* ×14. The script audit over course **and** solutions found **0 imperative-*vous* stems** and **0 tutoiement**. The course text is impersonal (*on*, passive). House forms: `Problème du week-end --- …`, `Partie I --- …`, and solution headers `\section*{Chapitre \ref{…} --- titre}`. Cross-volume references read *le livre 1 (année 10)*, *le volume scolaire (année 12)* and *le volume de deuxième année*, and no programme is ever named |
| LaTeX hygiene | **99** | Forced build (`latexmk -g`, under the memory-capped `systemd-run` scope): **0 errors, 0 undefined, 0 overfull, `nullfont` 0, `Missing character` 0, 0 `invalid in math mode`**, **305 pages** (English 293). `.fls`: **58** French sources and 0 English chapter files. Accents: **0 TeX accent escapes**, **33 raw `œ`**, **11 `«` / 11 `»`**. Spaced punctuation: **1921 `~:`**, **1169 `~;`**, **453 `~?`**. A final sweep fixed 14 unspaced `:`/`;` left in node text, tables and `\ce` lists. Line edges were swept after the last edit: no line-end elision apostrophe, no line-end hyphen, no line starting on `. , ; : ) ? !` or `~;`/`~:`/`~?`/`~!`. No `%` hides a line break. All files are valid UTF-8 |
| Cross-refs / rule compliance | **99** | Labels, `\cref` targets, solution keys, `[resume]`, math spans, image paths and `% ledger:` comments are byte-identical to English. No programme, curriculum, country or university name in visible text. No English source, preface or other edition was touched. Shared files edited: `tools/check_latin_prose.py`, one code-strip fix plus one reasoned `fr` allow-list entry, both reported. No repo-wide git command, no commit |
| Figures | **96** | All TikZ / pgfplots / chemfig code is byte-identical except two `!draw` ranges and one anchor (listed below). Only node text, axis labels, legends, tick labels and captions were localized. After the first build, every figure whose French label grew by more than 35 % was rendered and checked. **Eight collisions were found.** Seven were fixed by shortening the label: the σ-overlap legend (ch. 3), the CO₂ dipole caption (ch. 3), the two hydration-shell captions (ch. 4), "B (AEQS en tirets)" (ch. 9), the 1,2-shift arrow (ch. 25), and the Solvay boxes *carbonateur* / *distillateur* (ch. 26). One, the distillation "entrée d'eau" label (ch. 29), needed an anchor change |
| Solutions | **97** | All 348 exercise solutions and 29 weekend-problem solutions are present. Every number in ch. 1–29 was recomputed while translating (per-chapter checks; chains such as Solvay, Bayer, contact process, Ostwald, MTBE, Grignard yields, the uncertainty budgets and the lithium brine balance). Every multi-line math span keeps its exact English line break, as `id_apply`'s math census requires. Gate 11 (problem numbering) is green |
| Defined-term links (`\omterm`) | **95** | **2716 links over 149 distinct targets**, against English's **2471 over 144**. **Every target English links is reached**, and French also reaches five English never links (*synthèse de Williamson*, *effet nivelant*, *nombre quantique principal*, *ordre apparent*, *fixation de l'azote*). `book2_fr.py` was curated from this edition's own harvest (391 linkable terms on the same 169 targets as English), never seeded. See the census section below. `--apply` run twice changes nothing; the plain dry run reports **links to insert: 0** |
| MT-artifact freedom | **96** | Gate 10 (orphan lines): **0**. Gate 9 (twin prose comparison): **0 blocking findings**, 37 advisory one-word findings, all read and all cognates, eponyms or symbols (*Lyman*, *Balmer*, *graphite*, *zinc*, *fraction*, *syn/anti/gauche*, *carbocation*, *Complexation*, *Conventions*…). The `\text{}`/`\mathrm{}` census over course and solutions translated every translatable subscript (*sup/inf*, *éq*, *cste*, *réf*, *rét*, *ESH*, *excès*, *réactifs/produits*, *valeur*, *acétal/aldéhyde*, *distance parcourue par…*, `\mathrm{dissous}`, `\mathrm{fiole}`). Survivors are symbols or are frozen: `\mathrm{eq}`, `\mathrm{ref}` (an accent is invalid in `\mathrm`), `tot`, `org`, `front`, `inv`. The terminology-drift check (`check_term_display_drift.py`) found no drift: every multi-form target is a plural, a gender form or a sibling term |

**Overall: 96.** The weighting favours terminology, register, link curation and MT-artifact freedom; structure and build are gated mechanically.

## Gate output summary

```
bash tools/check_translation.sh bachelor-1 fr ............ TRANSLATION GATE: PASSED
  gates 1-8, 10, 11, 13 .... green (completeness, structure, hygiene, UTF-8,
                             orphan lines 0, problem numbering, ce balance)
  gate 9 ................... no multi-word findings; 37 one-word (advisory, cognates)
  gate 12 .................. chemistry twin gate: OK (58 files)

forced build build/one_chemistry_book_2_university_year_1_fr.log (grep -a)
  '^!' 0 · undefined 0 · Overfull 0 · nullfont 0 · Missing character 0
  'invalid in math mode' 0 · pages 305 (EN 293) · .fls fr chapters 58, EN 0

python3 tools/link_defined_terms.py --book 2 --lang fr     -> links to insert: 0
\index 364 = 364 · \label set diff 0 · \qty 1474 = 1474 · \ce 3433 = 3433
```

## The link layer: what the censuses found

The frequency and chapter-set censuses were run against the English twin after
the last prose edit and after the link layer. Each flag was read in context.

French homographs, each handled in `book2_fr.py` with its evidence:

- **Bare adjectives.** *fort / forte / faible* (*l'acide le plus fort*, *une faible constante*, *un faible avancement*) are **dropped**, not just stoplisted. A stoplisted term falls through to the per-chapter map and would have kept 18 wrong-sense links in ch. 10.
- ***groupe*** links only before a number, excluding *groupe donneur / attracteur / partant / protecteur*.
- ***multiplicité*** in its NMR sense is masked.
- ***hydratation des ions*** is masked; it is not the alkene hydration of ch. 25.
- ***positions axiales / équatoriales*** (VSEPR) is masked.
- ***protection*** is masked where it means personal protection: *protection individuelle*, *des yeux*, *écran de protection*.
- ***danger*** is masked in the pictogram name *danger pour la santé* and in the signal word *\emph{Danger}*.
- ***réseau*** is masked where it means a network rather than a lattice: covalent network, the hydrogen-bond network of ice, the SiO₄ framework.
- ***motif*** is masked where it means a silicate structural unit.
- ***période d'induction***, ***bloc de zinc***, and *quantitative* as an adjective of a theory or a measurement are masked.

Forms the harvest cannot derive, added to `EXTRA`:

- the masculine and plural adjectives *axial / axiaux / équatorial / équatoriaux* (the index carries *axiale*);
- the irregular plurals *cristaux*, *cristaux ioniques / covalents / moléculaires*;
- *niveaux d'oxydation*;
- the short form *moment(s) de liaison*.

After curation, three targets exceed English by more than 2×. All three are the defined sense:

| target | EN | FR | why |
|---|---:|---:|---|
| `def:b1:crystals-metals:lattice` | 22 | 79 | French *maille* is both "unit cell" and the everyday "cell". English bare *cell* is never linked, because it collides with the electrochemical cell; French has no such collision |
| `def:b1:extent-q-and-k:extent` | 1 | 28 | French *avancement* is the defined term itself. English defines *extent of reaction* but writes bare *extent* |
| `def:b1:crystals-metals:coordination` | 7 | 24 | *coordinence* is one word where English writes *coordination number* |

## Samples (French, with verdict)

1. **ch. 7**, the reaction quotient: «~le produit des activités des produits divisé par celui des activités des réactifs, chacune élevée à la puissance de son nombre stœchiométrique~». **Native.** This is the formulation of a French course.
2. **ch. 10**, the predominant-reaction method: «~repérer l'acide le plus fort et la base la plus forte présents~; si la constante de leur réaction est grande, la traiter comme totale~». **Native.** The infinitive method register.
3. **ch. 22**, Williamson: «~L'encombrement du côté de l'alcoolate, la petite taille du côté de l'halogénure.~» **Native.** A verbless closing maxim, the way a French teacher sums up.
4. **ch. 27**, Haber: «~la chimie qui nourrit la moitié de l'humanité et celle qui tue ne sont séparées que par les choix des chimistes~». **Native.** The *ne … que* restriction carries the English emphasis.
5. **ch. 29**, the two students: «~Une mesure ne vaut que par son incertitude, et une comparaison que par une règle.~» **Native.** The parallel *ne … que* with ellipsis of the verb.

## Edits outside the patch applier (recorded)

- **`!draw` ranges, two:**
  - `bachelor-1/16`, EN line 199: the carvone `\foreach` labels, *menthe verte / carvi*.
  - `bachelor-1/17`, EN line 68: the colour wheel `\foreach`, *rouge, orange, jaune, vert, bleu, violet*.
- **One drawing option changed:** `fr/29`, line 464 (EN 432). The distillation "entrée d'eau" node anchor went from `below` to `below left`, because the longer French label overlapped the receiver flask.
- **Post-apply edits inside math spans, four sites:** `solutions/fr/08-rate-laws.tex`, EN lines 84, 104, 109 and 117. `\qty{…}{day^{-1}}` became `d^{-1}`. This is the canon `day` defect below, repaired in French only.
- **Layout breaks, two:**
  - `fr/10`: a `\clearpage` before §10.4, to keep the heading off the foot of the page.
  - `fr/26`: a `\clearpage` + `\enlargethispage{3\baselineskip}` before the weekend problem. The box fills a page and cannot break under its heading.
- **Overfull clearing:** ten overfull boxes were cleared by rewording, never with `%`. The sites: `fr/11` zincate proof, `fr/13` Ag/AgCl proof, `fr/15` equivalence proof, `fr/25` section title, `fr/26` Solvay proof, `fr/27` Bayer proof, and solutions 04, 25 (×2) and 27.

## Suspected English-canon defects (reported, not fixed)

1. `parts/bachelor-1/solutions/04-intermolecular-forces-solvents.tex`, line 42 (exercise 6): "42 times", but 78.4/1.89 = 41.5. Problem question 8 of the same chapter says 41.
2. `parts/bachelor-1/08-rate-laws.tex`, line 328 (`ylabel \unit{day^{-1}}`) and line 460 (`\qty{1.27e-3}{day^{-1}}`, `\qty{3.48e-3}{day^{-1}}`): an English word inside a unit argument. The pre-run fix covered `days` only. Also in `solutions/08-rate-laws.tex`, lines 84, 104, 109 and 117. French writes `d^{-1}` everywhere; the four solution sites sit inside math spans.
3. `parts/bachelor-1/08-rate-laws.tex`, line 108: `\ce{aA -> products}` puts an English word inside `\ce`. The chemistry census and gate 12 freeze it, so the French edition shows "products". Suggested canon form: `\ce{aA ->}` followed by a translatable word, or math.
4. `parts/bachelor-1/26-s-block.tex`, lines 81–82: "With $E^\circ$ more than 2.7 V below the line of water at pH 7 (−0.41 V)". Li (−3.04), Na (−2.71) and K (−2.94) lie 2.63, 2.30 and 2.53 V below −0.41 V; none is more than 2.7 V below. It probably meant "E° below −2.7 V" or "more than 2.3 V below". Translated faithfully.
5. `parts/bachelor-1/20-elimination.tex`, line 110 (layout): the explanatory node at (2.6, 0.2) touches the equatorial "H" label of the chair. This is visible in the English PDF, p. 173, and identical in French.
6. Link layer, minor: `parts/bachelor-1/08-rate-laws.tex`, line 301 links *quantitative* in "made quantitative by the theories". That is the adjective, not the defined "quantitative reaction". The French edition masks it.
7. Wording only, not defects:
   - the `05` problem, lines 579–580 ("just above the transition, α-iron (still present below the transition)") reads confusingly;
   - the `06` proof, lines 235–236, is awkward English.

## Gate / tool bugs met

- **`tools/check_latin_prose.py`, axisstr tier.** A pgfplots number format inside `nodes near coords={\pgfmathprintnumber[fixed, fixed zerofill, precision=2]{…}}` supplied the "words" *fixed*, *zerofill* and *precision*. It fired the **blocking** tier on a figure with no prose (`02-periodicity`, the successive-ionisation-energy bars). The fix is a one-line strip of `\pgfmathprintnumber[…]` in `_strip_nonprose()`, with a comment. Every Latin edition of Book 2 would have hit it.
- **Same file, `ALLOWED_BY_LANG["fr"]`, appended with a reason:**
  - *constitution, configuration, conformation*: the ch. 16 definition title;
  - *butan, ol*: the IUPAC name `\cip{S}-butan-2-ol` in the ch. 22 scheme;
  - *inversion*: the node "SN2, inversion";
  - *dilution*: the contact-process box;
  - *exact*: the pH-curve legend.

  All are correct French spelt as in English. None was reworded.

## Why not 100

- **Four English-canon defects are reproduced**, because English is the source of truth: items 1, 3, 4 and 5 above. Only the `day` class could be repaired in French.
- **Link density is +10 %** against English (2716 vs 2471). This comes mostly from three targets where the French term is a single word that English never matches (*maille*, *avancement*, *coordinence*). Every link was read, but ch. 5–6 carry a denser link layer than the English pages.
- **Three drawing exceptions** (two `!draw` ranges and one anchor) leave those figures guarded only by the rendered PDF.
- **One shared gate file extended.** That is a gate limitation, not a text defect, but this edition had to touch it.
- **Register is measured, not perfect.** The exercise stems, the impersonal voice and the spaced punctuation were audited by script. A few long proofs still follow the English sentence boundaries more closely than a French author would.

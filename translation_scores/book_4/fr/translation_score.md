# Translation score — Chemistry Book 4 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 4 (University Chemistry, Year 3 — years `bachelor-3`, labels `b3`) |
| **Language** | French (`fr`) |
| **Quality bar** | **native academic prose**: a French third-year university chemistry course as it is written and taught. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **References measured before drafting** | the **English** canon (content); the shipped **French Books 1–3** of this repo for series terminology, typography and the **infinitive** exercise stem (Book 3 fr for *fréquence de cycles*, *volume de deuxième année*); `sources/TRANSLATION_BOOKS_3-4.md` and its reading list |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-06 |
| **Scope** | A full first translation written directly at native register (no machine draft): 33 chapters and 33 solution twins, **66 files**, every body through `tools/id_apply.py`. Also the French image-credits page, a curated `tools/term_config/book4_fr.py`, the defined-term link layer, French index keys, the overfull, punctuation and figure sweeps, and this score |

## Verdict in one line

This French Book 4 reads as a French third-year chemistry course. It uses:

- the vocabulary of the French tradition: *base d'orbitales*, *champ autocohérent*, *table de caractères*, *distance interréticulaire*, *fonction de partition*, *complexe activé*, *fréquence de cycles*, *coordinence*, *macrocycle*, *rétrosynthèse*, *facteur E*, *économie d'atomes*, *DBO / DCO*, *DL50 / CE50*, *PRG*, *rampe de Schlenk*, *boîte à gants*;
- the infinitive exercise register and an impersonal course text;
- French spaced punctuation and «~guillemets~».

Every structural, chemistry, prose and link gate is green on a forced build: **0 errors / 0 undefined / 0 overfull**, `nullfont` 17 and `Missing character` 17 (both the English baseline).

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | All 66 files mirror their 66 twins. Counts (EN = FR): `exercise` 396, `problem` 33, `solution` 429, `[resume]` 99, `omfigure` 199, `tikzpicture` 161, `axis` 108, `\node` 654, `\includegraphics` 42, `\emph` 677, `\index` 675, `\label` 1183, `\item` 1118, `\qty` 1997, `\num` 197, `\unit` 112. Environments (EN = FR): definition 323, proposition 184, theorem 65, method 89, example 53, proof 236, remark 5, recall 33, inthelab 33, history 33, safety 22, `\admitted` 16, `% ledger:` comments 167. `\cref` + `\Cref` 205 = 205 with identical targets per file (French capitalises fewer references at sentence start: 187 + 18 against 171 + 34) |
| Chemistry fidelity | **99** | `\ce` 1657 = 1657, `\chemfig` 32 = 32, `\schemestart` 13 = 13, `\ghs` 80 = 80, byte-identical in order (gate 12, chemistry twin: OK on 66 files). `check_ce_balance.py`: 59 + 45 equations, 0 problems. Never `!chem`. Arrow labels translated through the word-only and (after the coordinator's two gate fixes) mixed-label census: `->[$\ce{CH2}$ singulet]`, `->[{[3,3]}, puis][cyclisation, $-\ce{NH3}$]` |
| Terminology | **96** | Settled per chapter in a running glossary. Highlights: *fonction propre / valeur propre*, *opérateur hermitien*, *énergie de point zéro*, *opérateurs d'échelle*, *rotateur rigide*, *spin-orbitale*, *déterminant de Slater*, *terme spectroscopique*, *règle des intervalles de Landé*, *surface d'énergie potentielle*, *base d'orbitales* (never a bare *base*, which collides with the acid–base sense), *base à valence séparée*, *champ autocohérent*, *fonctionnelle d'échange–corrélation*, *point selle*, *groupe ponctuel*, *représentation irréductible*, *grand théorème d'orthogonalité*, *combinaison adaptée à la symétrie*, *règle d'exclusion mutuelle*, *isotopologue*, *bande harmonique* (never a bare *harmonique*), *bande chaude*, *différences de combinaison*, *force d'oscillateur*, *règle de Laporte*, *croisement intersystème*, *inhibition dynamique / statique*, *rapport gyromagnétique*, *angle de basculement*, *signal de précession libre*, *inversion-récupération*, *réseau réciproque*, *sphère d'Ewald*, *extinction systématique*, *position de Wyckoff*, *groupement formulaire*, *fonction de partition*, *AEQS*, *fréquence de cycles* (TOF; *fréquence de rotation* would have collided with ch. 6 *rotation*), *taux de recouvrement*, *concentration micellaire critique*, *coordinence*, *effet trans*, *isolobal*, *gabarit*, *rétrosynthèse*, *synthon*, *économie d'atomes*, *analyse du cycle de vie*, *demande biochimique / chimique en oxygène*, *potentiel de réchauffement global*, *rampe de Schlenk*, *cahier de laboratoire*. All 675 `\index{}` keys are in French, every accented key has an ASCII sort key, and the 35 keys identical to English are true cognates or eponyms (*ligand*, *fluorescence*, *phosphorescence*, *Raman*, *micelle*, *synthon*…) |
| Register / tone | **97** | The exercise stem is the French infinitive: *Calculer* ×225, *Donner* ×51, *Écrire* ×44, *Montrer* ×31, *Prévoir* ×19, *Expliquer* ×18, *Comparer* ×18, *Trouver* ×16, *Classer* ×13, *Dessiner* ×9, *Tracer* ×8, *Estimer* ×7, *Proposer* ×6. The script audit over course **and** solutions found **0 imperative-*vous* stems** and **0 tutoiement** (one *Que mesureriez-vous~?* in ch. 32 became *Que faudrait-il mesurer~?*). House forms: `Problème du week-end --- …`, `\textbf{Partie I --- …}`, `\section*{Chapitre \ref{…} --- …}`, `[Démonstration partielle]`. Cross-volume references read *le volume de première année* / *le volume de deuxième année*, *relève de cours plus avancés*, and no programme, country or university is ever named |
| LaTeX hygiene | **99** | Forced build through the shared wrapper (`latexmk -g`, memory-capped `systemd-run` scope): **0 errors, 0 undefined, 0 overfull**, `nullfont` **17** and `Missing character` **17** (the English baseline for Book 4, from shared style code), **0 `invalid in math mode`**, **431 pages** (English 405). `.fls`: **66** French sources and 0 English chapter files. Accents: **0 TeX accent escapes**, **72 raw `œ`**, **32 `«` / 32 `»`**. Spaced punctuation: **2296 `~:`**, **1439 `~;`**, **553 `~?`**. A final scripted sweep over prose, node text, titles and tick labels fixed the last unspaced `:`/`;` (incl. verbatim-copied solution lines, the ch. 19 `D:`/`A:` plot titles, the ch. 22 tick label and the ch. 28 peak labels). Line edges were swept after the last edit: no line-end elision apostrophe, no line-end hyphen, no line starting on `. , ; : ) ? !` or `~;`/`~:`/`~?`/`~!`. No `%` hides a line break. All files are valid UTF-8 |
| Cross-refs / rule compliance | **99** | Labels, `\cref` targets, solution keys, `[resume]`, math spans, image paths and `% ledger:` comments are byte-identical to English. No English source, preface or other edition was touched. The one shared file edited is `tools/check_latin_prose.py`: one append-only, commented `ALLOWED_BY_LANG["fr"]` entry, reported below. No repo-wide git command, no commit |
| Figures | **95** | All TikZ / pgfplots / chemfig code is byte-identical except seven `!draw` ranges (all `\foreach` label lists, listed below). Only node text, axis labels, legends, tick labels and captions were localized. After the first clean build, **every figure page was rendered at 130 dpi, one page per figure** (138 pages for the 157 figures with text; photographs and AI images checked on their pages too), and the English page was rendered beside it wherever a doubt arose. **Nineteen defects were found and fixed**: label/curve collisions (ch. 1 turning points, ch. 14 funnel, ch. 16 crossing, ch. 25 closure arrow, ch. 26 heat label, ch. 30 Corey arrow label, ch. 32 runoff label), labels clipped by the page or axis (ch. 7 *fondamental*, ch. 29 pyridine legend), legend/curve overlaps (ch. 21, ch. 28), box/text overflows (ch. 13 mixer, ch. 17 side-view label, ch. 22 conduction-band label, ch. 30 oseltamivir box, ch. 31 three LCA boxes, ch. 33 report box), and unspaced colons in two plot labels. Every fix was re-rendered and re-checked on the final build |
| Solutions | **97** | All 396 exercise solutions and 33 weekend-problem solutions are present. Numbers were recomputed while translating (rovibrational fits, Hartree–Fock and Hückel energies, partition functions, Eyring plots, Michaelis–Menten, Butler–Volmer and Tafel, Langmuir isotherms, Marcus, band gaps and carrier densities, E factors, atom economies, LCA and fugacity budgets); five canon discrepancies were found this way (below). Every multi-line math span keeps its exact English line break. Gate 11 (problem numbering) is green |
| Defined-term links (`\omterm`) | **95** | **1778 links over 258 distinct targets**, against English's **1632 over 252**. **Every target English links is reached** (MISSING 0), and French also reaches six English never links (*inhibition* ch. 13, *volume d'activation* ch. 19, *transition de spin* ch. 18, *méthode de Hartree–Fock* ch. 3, *gap direct / indirect* ch. 22, *équation de Stern–Volmer* ch. 7). `book4_fr.py` was curated from this edition's own harvest (700 linkable terms), never seeded. `--apply` run twice changes nothing; the plain dry run reports **links to insert: 0** |
| MT-artifact freedom | **96** | Gate 10 (orphan lines): **0**. Gate 9 (twin prose comparison): **0 blocking findings**, 75 advisory one-word findings, all read: cognates, eponyms and symbols in nodes, titles and legends (*Raman*, *Stokes*, *Langmuir*, *fluorescence*, *micelle*, *transport*…). A script scan for the two-letter English words gate 10 cannot see found and fixed *so* (ch. 18) and *and* (sol. 13). Two `[Partial proof]` headers (ch. 15, 17) that survived as verbatim lines were translated. Frozen math keeps the English acronyms the canon writes inside `\mathrm` (`BOD_5`, `LD_{50}`, `EC_{50}`, `RQ`, `PMI`, `AE`, `TOF`); the prose around each gives the French name (*DBO₅*, *DL50*, *CE50*, *quotient de risque*, *intensité massique du procédé*, *économie d'atomes*, *fréquence de cycles*) |

**Overall: 96.** The weighting favours terminology, register, link curation and MT-artifact freedom; structure and build are gated mechanically.

## Gate output summary

```
bash tools/check_translation.sh bachelor-3 fr ............ TRANSLATION GATE: PASSED
  gates 1-8, 10, 11, 13 .... green (completeness, structure, hygiene, UTF-8,
                             orphan lines 0, problem numbering, ce balance 59 + 45)
  gate 9 ................... no multi-word findings; 75 one-word (advisory, cognates)
  gate 12 .................. chemistry twin gate: OK (66 files)

forced build build/one_chemistry_book_4_university_year_3_fr.log (grep -a)
  '^!' 0 · undefined 0 · Overfull 0 · nullfont 17 (= EN) · Missing character 17 (= EN)
  'invalid in math mode' 0 · pages 431 (EN 405) · .fls fr chapters 66, EN 0

python3 tools/link_defined_terms.py --book 4 --lang fr     -> links to insert: 0
\index 675 = 675 · \label 1183 = 1183 · \qty 1997 = 1997 · \ce 1657 = 1657
```

## The link layer: what the censuses found

The frequency and chapter-set censuses were run against the English twin after
the last prose edit and after the link layer. Each flag was read in context.

French homographs, each handled in `book4_fr.py` with its evidence:

- ***migration(s)*** is **dropped**: French uses it for ions in a field, for 1,2-shifts and for groups in rearrangements, and only one sense is defined.
- ***sol*** (sol–gel) is masked wherever it means soil: *aux sols, du sol, dans les sols, d'un sol, sur le sol, usage des sols, Sols et sédiments* (ch. 32).
- ***gel*** is masked in *gel des porteurs* (carrier freeze-out, ch. 22).
- ***trous*** is masked in *dans les trous* (interstitial holes, not electron holes).
- ***population*** is masked in *populations denses* and *population d'essai* (ecotoxicology, not level populations).
- ***caractère*** is masked in *caractère singulet / vert* (character in the everyday sense, not a group character).
- ***opérateur*** is masked where it means a plant operator (*opérateurs formés*, *les opérateurs portent*).
- ***valeur moyenne*** is masked in *valeur moyenne de $\Delta_rH$* (an arithmetic mean, not a quantum expectation value).
- `\setchemfig`, arrow options and `ticklabels` bodies are protected.

Forms the harvest cannot derive, added to `EXTRA`: *quasi réversible* (→ reversibility), *peroxydable(s)* (→ peroxide formers), *gabarit* (→ template).

After curation, the targets above English by more than 2× are all the defined sense:

| target | EN | FR | why |
|---|---:|---:|---|
| `def:b3:surfaces-catalysis:coverage` | 4 | 24 | *taux de recouvrement* is the fixed French term; English writes bare *coverage* or *θ* and links it once per section |
| `thm:b3:electronic-spectroscopy:laporte` | 1 | 6 | *règle de Laporte* is named again in ch. 18 (ligand-field intensities) where English writes "Laporte-forbidden" |
| `def:b3:rate-theories:saddle` | 3 | 8 | *point selle* is one term; English alternates *saddle point* / *col* phrasing |
| `def:b3:lab-techniques-3:notebook` | 3 | 8 | *cahier de laboratoire* recurs where English writes *the notebook* / *record* |
| `def:b3:rovibrational-spectroscopy:anharmonic` | 5 | 10 | *anharmonique / anharmonicité* in ch. 10 and 12 where English writes *non-harmonic* |
| `def:b3:total-synthesis:total` | 3 | 6 | *synthèse totale* where English writes *a total route* |

## Samples (French, with verdict)

1. **ch. 2**, opening recall: «~Le volume de première année a désigné les électrons par quatre nombres quantiques~[…]~; le volume de deuxième année a donné~[…]~». **Native.** The passé composé of a recapitulating course.
2. **ch. 12**, history: «~En 1935, Henry Eyring, à Princeton, et Meredith Gwynne Evans et Michael Polanyi, à Manchester, publièrent indépendamment la théorie du complexe activé.~» **Native.** Passé simple, the register of French scientific history.
3. **ch. 22**, history: «~tous trois partagèrent le prix Nobel de physique 1956~». **Native.**
4. **ch. 31**, history: «~les industries de la chimie fine et de la pharmacie, bien que petites en tonnage, produisaient beaucoup plus de déchets par kilogramme de produit que la chimie lourde~». **Native.** *Chimie lourde / chimie fine* is the French industrial pair.
5. **ch. 8**, weekend problem: «~Le couplage du quadruplet vaut 7.2 Hz~: quelle est sa largeur, en ppm, à 400 MHz~?~» **Native.** The terse question form of a French problem sheet.

## Edits outside the patch applier (recorded)

- **`!draw` ranges, fourteen.** Seven are `\foreach` label lists whose words had to be translated: `bachelor-3/05` EN 271, `08` EN 315, `09` EN 77, `22` EN 126, `24` EN 106, `26` EN 179, `33` EN 413. Seven move a translated label that collided after the 130-dpi check: `07` EN 172 (anchor east at x 4.95), `13` EN 567 (mixer, anchor north west), `14` EN 128 (funnel raised), `22` EN 265 (conduction-band label shifted), `29` EN 119 (pyridine legend anchored east inside the axis), `32` EN 238 (fields box moved left) and EN 244 (runoff label at pos 0.5).
- **Font-size-only changes inside node text** (no `!draw` needed): `\tiny` on the ch. 16 *croisement*, ch. 25 *fermeture* and ch. 30 *iodolactonisation, Baeyer–Villiger* labels; `\footnotesize` on the ch. 26 *chaleur … antarafaciale* label.
- **Overfull clearing:** nine overfull boxes on the first build were cleared by rewording, never with `%`: `fr/03` (variational proof), `fr/08` and `fr/09` (weekend-problem boxes 15 pt too tall: titles and questions tightened), `fr/27`, `fr/33`, and solutions 13, 22 (title), 27, 30, 33.

## Suspected English-canon defects (reported, not fixed)

1. `parts/bachelor-3/02-many-electron-atoms.tex`, line 365: "1.64", but (43.4 − 16.4)/16.4 = 1.646, and `solutions/02` exercise 5 says 1.65.
2. `parts/bachelor-3/02-many-electron-atoms.tex`, line 396: "A = 11.46", but 17.20/1.5 = 11.467, and `solutions/02` exercise 6 says 11.47. **Fixed in the canon by the coordinator during the run (now 11.47) and mirrored in French.** The coordinator's second canon edit, `solutions/08` problem item 11 (*Coupled methyls, hence two CH3 on adjacent carbons*), is mirrored too.
3. `parts/bachelor-3/06-rovibrational-spectroscopy.tex`, line 291, and `solutions/06` exercise 7: R(0) − P(2) = 2905.57 − 2842.94 = 62.63 cm⁻¹, printed 62.64.
4. `parts/bachelor-3/solutions/10-partition-functions.tex`, exercise 1, lines 4–5: "the numbers of oscillators holding 0, 1, 2, 3, 4 quanta", but the labels that follow (*4, 0, 0, 0*…) are the quanta held by each of the four oscillators (four numbers, not five). French rephrased locally (*nombres de quanta des quatre oscillateurs, rangés par ordre décroissant*).
5. `parts/bachelor-3/solutions/15-electrode-kinetics.tex`, exercise 12 and problem question 13: b²Sxx printed 203.9, but 0.919² × 241 = 203.5 (minor rounding).

## Gate / tool bugs met

- **Chemistry census froze mixed arrow labels** (`27` EN 280, `singlet $\ce{CH2}$`): fixed by the coordinator during the run (only the `\ce{}`/`$…$` parts are compared now).
- **Arrow-label regex could not match a label containing nested brackets** (`29` EN 386, `{[3,3]}, then`: `ARROW_LABEL` used `[^\[\]]*`), so the whole arrow was byte-compared and the English *then* was frozen. Fixed by the coordinator (brace-aware parser); French now reads *puis*.
- **Gate 10's `ENGLISH_ONLY` list skips two-letter words**: an untranslated *so* (ch. 18) and *and* (sol. 13) passed every gate and were found by a local scan.
- **`tools/check_latin_prose.py`, `ALLOWED_BY_LANG["fr"]`, appended with a reason:** *cis, trans, fac, mer* (sol. 05 isomer counts), *absorbance, relative* (ch. 6 node *absorbance (relative)*), *triplet* (ch. 27 node), *iodolactonisation* (ch. 30 node), *purge* (ch. 31 node). All correct French spelt as in English; none was reworded.

## Why not 100

- **Three English-canon numerical discrepancies are reproduced** (items 1, 3 and 5), because English is the source of truth; item 2 was fixed in the canon and mirrored, item 4 repaired in wording.
- **Link density is +9 %** against English (1778 vs 1632), mostly from *taux de recouvrement*, which French writes as a fixed term where English writes θ.
- **Fourteen `!draw` ranges** leave those figures guarded only by the rendered PDF (all re-checked at 130 dpi on the final build).
- **Frozen math acronyms** (`BOD_5`, `LD_{50}`, `TOF`…) keep English letters inside formulas; the prose names them in French but a French reader sees two forms.
- **Register is measured, not perfect.** Some long proofs in ch. 3 and ch. 9 still follow the English sentence boundaries more closely than a French author would.

## Coordinator addendum (2026-10-07)

After this edition was delivered the coordinator carried in the later English
canon fixes found by other editions (listed in `sources/WAVE1_FINDINGS_B34.md`
and `WAVE2_FINDINGS_B34.md`; the last ones: solutions/32 items 14-15 0.0145 and
0.083, solutions/02 gap 2047.98) and aligned the link layer with English, which
no longer links "indistinguishable" in its everyday sense (ch. 4 "from the
original/itself", ch. 10 orientations and sums). This edition now has **1778
links over 258 targets** (English 1,632 over 253); gates, dry run (0) and the
forced build re-checked. Score unchanged.

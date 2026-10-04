# Translation score — Chemistry Book 1 · Brazilian Portuguese (`pt`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 1 (School Chemistry, Grades 1–12) |
| **Language** | Brazilian Portuguese (`pt`) |
| **Quality bar** | native Brazilian school chemistry — *ensino fundamental* for grades 1–9, *ensino médio* register for 10–12 — as a Brazilian textbook writes it. English is the source of truth for content, structure, labels, mathematics and drawing code |
| **Register reference measured before drafting** | the shipped Brazilian Portuguese biology editions (`../one-biology-book/parts/*/pt/`): imperative *você* exercise stems (*Calcule, Explique, Dê, Escreva*), decimal point kept in numbers, ``…'' quotes |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-04 |
| **Scope** | 49 chapters + 49 solution files = **98 files**, written directly in Portuguese through `tools/id_apply.py` (no machine draft); `tools/term_config/book1_pt.py` curated from this edition's own harvest; the preface and image-credits pages; ASCII sort keys on accented index entries; overfull and figure-label sweeps |

## Verdict in one line

A Brazilian school chemistry course from first grade to the end of *ensino
médio* that reads as written in Portuguese, built on a forced build at
**0 errors / 0 undefined / 0 overfull / 0 nullfont / 0 invalid-in-math**,
**440 pages**, **98/98** translated files in the `.fls`, and green
`check_translation.sh` (gates 1–13) for all twelve years.

## Dimension scores

| Dimension | Score | Notes |
|-----------|------:|-------|
| Structural fidelity | **99** | Counted over the 98 files against their twins: 665 `exercise`, 42 `problem`, 707 `solution`, 112 `[resume]`, 260 `omfigure`, 137 `tikzpicture`, 25 `axis`, 495 `\node`, 123 `\includegraphics`, 369 `\emph`, 301 `\index`, 142 `\cref`, 1352 `\label` (set diff 0), 1054 `\item`, 2267 `\ce`, 128 `\chemfig`, 73 `\ghs`, 186 `% ledger:`, 58 `\text{}`, every theorem-like environment — all exact. `\qty` 2197 vs 2196: one idiom (*de \qty{0.1}{mL} em \qty{0.1}{mL}*) |
| Terminology | **96** | Brazilian school usage throughout: *quantidade de matéria*, *massa molar*, *tabela de avanço*, *reagente limitante*, *rendimento*, *titulação / titulante / volume de equivalência*, *semirreação*, *par redox*, *reação de oxirredução*, *ligação de hidrogênio*, *interação de van der Waals*, *sítio doador/aceptor*, *seta curva*, *carbocátion*, *meia-vida*, *constante de velocidade*, *quociente de reação*, *taxa de avanço final*, *espécie anfótera*, *íon oxônio*, *produto iônico da água*, *solução-tampão*, *faixa de viragem*, *titulação potenciométrica / condutométrica*, *pilha / meia-pilha / ponte salina / ânodo / cátodo*, *economia atômica*, *química verde*, *grupo protetor*, *polietileno, poli(cloreto de vinila)*, IUPAC names in the Brazilian form (*butan-1-ol, propanona, ácido etanoico, etanoato de etila*). Dioxygen/dihydrogen rendered *gás oxigênio / gás hidrogênio*. All 301 index keys in Portuguese (4 true cognates shared: *material, metal, pH, pKa*); accented keys carry ASCII sort keys, so the index sorts á…z correctly |
| Register / tone | **96** | Child-directed *você* imperatives in grades 1–5, the same imperative stems later (*Dê* 28, *Olhe* 24, *Escreva* 22, *Desenhe* 15, *Calcule*, *Diga*) — the register of the shipped biology pt editions; infinitives only as subjects or in the green-chemistry principle list. Problems: *Problema de fim de semana — …*, *Parte I — …* |
| Fluency | **95** | Drafted sentence by sentence in Portuguese, not post-edited; reworded only for meaning, never to satisfy a gate. Overfull boxes cleared by adding break points (*de massa molar*) rather than shortening |
| Accuracy | **97** | Numeric census of every file against its twin (only idioms and spelled-out *Year 1 volume* differ); every solution re-read against its question while drafting grades 11–12; four suspected canon defects reported below rather than reproduced as nonsense |
| Term links | **95** | **5,888 links to 172 targets** against English's 5,775 / 172 — every English target reached. Curated homographs: *solução* (exercise), *grupo*, *camada* (layer vs shell — one pt word for two en words), *período*, *queima a pele*, the verb *mistura*, *E* the conjunction vs the *E* isomer, *solução neutra* (electrically neutral), *núcleo em colmeia*, *lamparina a álcool*; *ar* given an `EXTRA` (under the 3-character harvest floor; en links *air* 220 times, pt 237); irregular plurals and conjugations via `DERIVED`. Dry run: `links to insert: 0` |
| Figures | **95** | 29 `!draw` opt-outs (listed in the run report), each a `\foreach` list, symbolic tick label or node inside `at ($…$)`; per-figure check at 130 dpi of every page with translated figure text (≈120 pages) plus an automated text-overlap scan: 14 label collisions fixed (grade 1, 5, 7, 8, 9, 10, 11, 12) and re-checked on probe builds |

## Censuses

* `\text{}` census over course **and** solutions: 58 / 58, all Portuguese.
* Chapter-set census: the surviving flags are all the defined sense (*quantidade de matéria*, *massa molar*, conjugated *misturar*), except **`reagente` in grade 9 ch. 2 (5 links)**: pt has one word for *reagent* and *reactant*, so the test-reagent sense links to the reactant definition. Documented in the config; English sends those to *characteristic test*.
* Frequency census: *eletronegatividade* 14 vs 7 and *energia de ligação* 11 vs 1 — both the defined term, used more often in pt prose (English's *bond energies* plural is not derived by its own morphology).
* Line-edge sweeps (quote, punctuation, hyphen at line edges) and broken-`\index` sweep: 0.

## Why not 100

* The *reagente* merge above (5 links on a sibling target).
* Twenty-nine `!draw` opt-outs: each justified, but each is a figure the census no longer guards.
* Four suspected English-canon defects are reported, not fixed: two were rendered by meaning (grade 7 sol. 12 *blank* → *teste de controle*; grade 12 sol. 07 Q4 *left* → *abaixo*), one by the established pt wording (*(dados de referência)* for the printed *(ledger)*), and one left as is (grade 10 ch. 1: linalool's boiling point used in solutions but never given).

# Translation score — Chemistry Book 3 · Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 3 (University Chemistry, Year 2 — year `bachelor-2`, labels `b2`) |
| **Language** | Indonesian (`id`) |
| **Quality bar** | **native academic prose**: a second-year Indonesian university chemistry course (*Kimia Fisik II*, *Kimia Anorganik*, *Kimia Organik II*, *Kimia Analitik* register) as it is written and taught. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **References measured before drafting** | the **English** canon; the shipped **Indonesian Chemistry Book 2** (`parts/bachelor-1/id/`, `book2_id.py`, its score) for series terminology and the impersonal *-lah* register; the **French Book 3** (and es, nl, pt) as sense references; `sources/TRANSLATION_BOOKS_3-4.md`, `sources/WAVE1_FINDINGS_B34.md`, `indonesian_style_card.md` |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-06 |
| **Scope** | A full first translation written directly at native register (no machine draft): 35 chapters and 35 solution twins, **70 files**, all written through `tools/id_apply.py`. Also the Indonesian image-credits page, a curated `tools/term_config/book3_id.py`, the link layer, Indonesian index keys, the overfull, orphan-heading and figure sweeps, and this score |

## Verdict in one line

An Indonesian Book 3 that reads as a second-year Indonesian university
chemistry course — *energi Gibbs reaksi standar*, *potensial kimia*, *hukum
Raoult/Henry*, *aturan fase* and *varians*, *reaktor tangki berpengaduk
kontinu*, *diagram Ellingham*, *garis hubung* and *aturan tuas*, *kurva
arus--potensial*, *overpotensial*, *orbital perbatasan*, *medan ligan*,
*adisi oksidatif / eliminasi reduktif*, *zat antara Wheland*, *adisi
Michael*, *anulasi Robinson*, *pemutusan* and *sinton*, *waktu retensi*,
*bilangan pelat*, *pemutusan-$\alpha$*, *penataan ulang McLafferty*,
*selang kepercayaan*, *keterulangan / ketertiruan*, *pengolahan* — impersonal
*-lah* imperatives, no *kamu/Anda*, decimal points as in the canon; every
structural, chemistry, prose and link gate green on a forced build of **0
errors / 0 undefined / 0 overfull / 0 nullfont / 0 Missing character / 0
invalid in math mode**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | 70 files mirror their 70 twins: `exercise` 420 = 420, `problem` 35 = 35, `solution` 455 = 455, `omfigure` 188 = 188, `tikzpicture` 160 = 160, `definition` 197 = 197, `proposition` 176 = 176, `method` 76 = 76, `\label` 1025 = 1025, `\cref/\Cref` 195 = 195, `\emph` 429 = 429, `\index` 417 = 417 (no duplicate key), `\qty` 1858 = 1858; `% ledger:` comments byte-identical (gate 12). A numeric census of every file (all digit tokens, as multisets) is identical to English in all 70 files |
| Chemistry fidelity | **99** | `\ce` 2102 = 2102, `\chemfig` 102 = 102, all byte-identical in order (gate 12: OK on 70 files); gate 13 (balance) green. Never `!chem`. Word arrow labels translated (21/71 *adisi sin*; 24/79, 81, 88, 155; 25/164, 172; 26/164, 237, 243, 245; 27/78, 84); 25/31 `[\ce{H+} atau \ce{HO-}][katalisis]` and 26/94, 100 `[lalu \ce{H2O}]` accepted by the chem census |
| Terminology | **96** | Running glossary checked against Indonesian Book 2: series terms kept (*tetapan*, *pereaksi*, *elektrode*, *kemajuan reaksi*, *proyeksi Fischer*, *pergeseran kimia*, *adisi sin*, *metil jingga*, *KLT*, *corong pisah*, *air garam pekat*); English homograph pairs separated in the wording itself: *varians* (system, ch. 4) / *variansi* (statistics, ch. 29, 34); *propagasi* (chain step) / *perambatan* (uncertainty); *sisaan* (regression residual) / *residu*; *penjernihan* (water treatment) / *pengolahan* (work-up); *daur ulang* (recycle) / *didaur ulang* (plastics) |
| Register & naturalness | **95** | Impersonal stems throughout (*Hitunglah, Tuliskan, Tentukan, Jelaskan, Gambarlah, Tunjukkan, Usulkan, Ramalkan*); stem distribution measured against Book 2 id (same profile: *Sebuah / Tuliskan / Hitunglah / Dalam* lead); three *Anda* removed in the native pass (5/600, 9/538, 10/502); definitions *Yang disebut … adalah …*; IUPAC names in Indonesian form (*heksaaminkobalt(III) klorida*, *4-metilsikloheks-3-ena-1-karbaldehida*) |
| Mathematics & notation | **97** | Math spans byte-identical (id_apply); `\text{}` subscripts translated where they are words (*kor*, *kat*, *kisi*, *inisiasi/propagasi/terminasi*); conventional ones kept (*trs, fus, vap, ad, acc, eq, Red/Ox*) |
| Figures | **95** | `!draw` used only on the run file's ranges; every translated figure page sampled at 130 dpi: three collisions fixed by text (ch. 20 *melepas* \ce{PPh3}, ch. 32 drift-tube label, ch. 35 wash labels *cuci …*); ch. 33 flow box wraps *ketidak-jenuhan* on three lines (readable) |
| Link layer | **96** | 1836 links on 184 targets (English 1733 / 179): every English target reached; 5 more, all the defined sense (*pelarian termal*, *dinding pelarut*, *pergeseran kesetimbangan*, *entalpi pembentukan standar*, *gugus pelindung ortogonal*); both censuses read (below); dry run 0 |

**Overall: 96.**

## Gate output summary

```
bash tools/check_translation.sh bachelor-2 id ......... TRANSLATION GATE: PASSED
  indonesian prose gate: OK (70 files)
  latin prose gate: no multi-word findings (one-word tier read: cognates
     ideal, linear, tetrahedral, batch, purge, separator, anode, oven, data,
     elastomer; eponyms Raoult, Henry, Wheland; subscripts trs/fus/vap/Red)
  chemistry twin gate: OK (70 files)
forced build (build.sh), build/one_chemistry_book_3_university_year_2_id.log
  errors 0 · undefined 0 · Overfull 0 · nullfont 0 · Missing character 0 ·
  invalid in math mode 0 · pages 388 (English 373) · .fls Indonesian sources 70
python3 tools/link_defined_terms.py --book 3 --lang id ... links to insert: 0
```

### Censuses (after the final link layer)

*Frequency* (ID ≥ 8 and ≥ 2× EN, or |Δ| > 12): `atomic-orbitals:orbital-energy`
5 → 10, `ellingham:metallurgy` 3 → 9, `reaction-enthalpy:reaction-quantity`
5 → 10 — all the defined sense (*energi orbital*, *piro-/hidrometalurgi*,
*entalpi reaksi* where English varies wording).

*Chapter-set* (chapters English never links): 16 targets, every occurrence
read, all the defined sense (e.g. *lapisan pasif/pasivasi* in sol. 12,
*orbital ikatan* in ch. 18, *enolat termodinamik* in sol. 26, *reaksi Wittig*
in ch. 28's table, *tetapan/hukum Henry* in sol. 10).

Homographs handled in `book3_id.py`: STOP *fragmen*; protected *kegagalan
inisiasi* (sol. 35), chromatographic and Wittig *selektivitas* (ch. 27, 31),
*resolusi tinggi* and an NMR *resolusinya* (ch. 32, 33), *pemutusan
cincin / ikatan-ikatan / sederhana* (ch. 28, 32), adjectival *presisi*; plus
the stub's code masks.

## Layout

Two weekend-problem headings orphaned on an otherwise empty page (ch. 15,
ch. 26) — fixed with `\clearpage` + `\enlargethispage{3\baselineskip}`, as
the French edition did for its ch. 13 and 21. Overfull boxes from the first
builds (ch. 1, 4, 16; sol. 2, 11, 21, 27, 34) removed by rewording.

## Shared-tool edits (append-only, reasoned, reported)

1. `check_indonesian_prose.py` WORK_TITLE: *On the Equilibrium of Heterogeneous Substances* (ch. 2, Gibbs's memoir, kept verbatim like fr/es/pt/nl).
2. `check_indonesian_prose.py` GENE_SYMBOL: an Ox/Red-only run between math markers (ch. 10 `\text{Red}` subscripts, byte-identical to the canon).
3. `check_indonesian_prose.py` GENE_SYMBOL: a lone bracketed compass anchor `[west]` (ch. 21 `\schemestart[][west]`; `visible_text` keeps optional arguments — a gate bug).
4. `check_indonesian_prose.py` WORK_TITLE: *Popular Science Monthly* (ch. 22 credit, credits page).
5. `check_latin_prose.py` ALLOWED_BY_LANG `id`: *endo*, *exo* (ch. 17 `\foreach`), *mol*, *per* (ch. 6 axis node). The ch. 23 title *pH optimum* was reworded (*pH optimal*) rather than exempted.

## English-canon defects

None found. Every problem and exercise answer was recomputed while drafting
(e.g. sol. 24 item 20 1004.6 kg — consistent with unrounded 1129.37 mol;
sol. 34 items 10–21; sol. 27 item 15; sol. 32 items 10 and 25), and the
numeric census confirms no number was changed in translation.

## Coordinator addendum (2026-10-07)

The bare noun of the "Enolates" definition (`def:b2:enolates-aldol:enolate`) was
linked once in English and in this edition, because only the "enolate ion"
phrase was harvested; the Arabic edition exposed it. An `EXTRA` entry was added
here and in English (79 links). This edition now has **1922 links over 185
targets** (English 1,811 over 180); gates, dry run (0) and chapter-set census
re-checked. Later canon fixes carried in by the coordinator are listed in
`sources/WAVE1_FINDINGS_B34.md` and `WAVE2_FINDINGS_B34.md`. Score unchanged.

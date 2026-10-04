# Translation score — Chemistry Book 1 · Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Chemistry Book 1 (School Chemistry, Grades 1–12) |
| **Language** | Indonesian (`id`) |
| **Quality bar** | **native school prose at every level**: an Indonesian children's science book in grades 1–5, an SMP science textbook in grades 6–9, an SMA chemistry course in grades 10–12. English is the source of truth for content, structure, labels, mathematics, chemistry and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); the shipped Indonesian editions of One Biology Book 1–5 (`../one-biology-book/parts/*/id/`) for the *kamu* register, the bare-imperative exercise stem (*Sebutkan*, *Jelaskan*, *Hitung*, *Tentukan*, *Tuliskan*, *Gambarlah*) and the house forms of the weekend problems; Indonesian IUPAC chemical names (*natrium klorida*, *asam etanoat*, *butan-2-on*, *but-1-ena*) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-04 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 49 chapters + 49 solution twins = **98 files**, every one written through `tools/id_apply.py`; `frontmatter/preface.id.tex` (shared with Book 2 `id`) and `frontmatter/image-credits.id.tex`; a curated `tools/term_config/book1_id.py`; the defined-term link layer; Indonesian index keys; the overfull sweep; a label-length census of every TikZ node against English and a page check of every flagged and every grade-11/12 figure; and this score |

## Verdict in one line

An Indonesian Book 1 that reads as an Indonesian school chemistry course from
*benda dan bahan* in grade 1 to *kesetimbangan*, *pKa* and *ekonomi atom* in
grade 12, with every structural, prose, chemistry-twin and equation-balance
gate green on a forced build of **0 errors / 0 undefined / 0 overfull /
0 nullfont / 0 invalid-in-math-mode**, 450 pages (English 432).

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror over the 98 files against their 98 twins: **665 `exercise` / 665**, **42 `problem` / 42**, **707 `\begin{solution}` / 707**, **112 `[resume]` / 112**, **260 `omfigure` / 260**, **137 `tikzpicture` / 137**, **25 `axis` / 25**, **495 `\node` / 495**, **123 `\includegraphics` / 123**, **369 `\emph` / 369**, **301 `\index` / 301**, **142 `\cref` / 142**, **1352 `\label` / 1352** (set diff **0** both ways), **1054 `\item` / 1054**, **2199 `\qty` / 2199**, **141 `\num` / 141**, **2267 `\ce` / 2267**, **128 `\chemfig` / 128**, **73 `\ghs` / 73**, **186 `% ledger:` / 186**, and per environment 184 `definition`, 115 `proposition`, 65 `method`, 155 `example`, 52 `proof`, 72 `remark`, 47 `recall`, 29 `inthelab`, 15 `history`, 23 `safety` — all exact. Every `\ce`, `\chemfig`, scheme and ledger comment byte-identical (gate 12, chemistry twin) and every equation balanced (gate 13). A per-chunk number census (every number of every labelled block and every solution, English vs Indonesian) leaves only "Year 1/2 volume" → *buku Tahun Pertama/Kedua universitas* and one added "pena 3" |
| Terminology | **96** | Indonesian school and university chemistry: *zat murni*, *campuran homogen/heterogen*, *zat terlarut*, *pelarut*, *larutan jenuh*, *kelarutan*, *dapat bercampur*, *uji khas*, *reagen* (kept apart from *pereaksi*, the reactant), *kromatografi kertas / lapis tipis (KLT)*, *faktor retensi*, *persamaan setara*, *koefisien stoikiometri*, *angka indeks*, *kekekalan massa*, *nomor atom / massa*, *isotop*, *kation / anion*, *ion penonton*, *galvanisasi*, *tabel periodik*, *golongan* (never confused with the functional *gugus*), *kulit elektron*, *subkulit*, *elektron valensi / teras*, *aturan oktet / duplet*, *pasangan elektron bebas / ikatan*, *struktur Lewis*, *jumlah zat*, *tetapan Avogadro*, *massa molar*, *pengenceran*, *labu ukur*, *pipet volume*, *tabel kemajuan*, *pereaksi pembatas*, *rendemen*, *pemanasan dengan refluks*, *penyaringan vakum*, *rekristalisasi*, *absorbans*, *hukum Beer--Lambert*, *keelektronegatifan*, *ikatan hidrogen*, *interaksi van der Waals*, *solvasi / hidrasi*, *misel*, *isomer struktur*, *gugus fungsi*, *haloalkana*, *bilangan gelombang*, *daerah sidik jari*, *oksidator / reduktor*, *setengah reaksi*, *titran*, *titik / volume ekuivalen*, *eksoterm / endoterm*, *energi ikatan*, *pergeseran kimia*, *proton ekuivalen*, *kurva integrasi*, *aturan $n+1$*, *kiral*, *karbon asimetris*, *enantiomer*, *campuran rasemat*, *diastereomer*, *konformasi goyang / eklips*, *panah lengkung*, *situs donor / akseptor elektron*, *karbokation*, *zat antara reaksi*, *peredaman*, *faktor kinetik*, *waktu paruh*, *reaksi orde satu*, *katalisis homogen / heterogen*, *kuosien reaksi*, *tetapan kesetimbangan*, *asam / basa Brønsted*, *amfolit*, *ion oksonium*, *hasil kali ion air*, *tetapan keasaman*, *diagram predominansi*, *trayek perubahan warna*, *larutan penyangga*, *titrasi pH-metri / konduktometri*, *setengah ekuivalen*, *sel elektrokimia*, *jembatan garam*, *tetapan Faraday*, *gugus pelindung*, *kimia hijau*, *unit ulang*, *derajat polimerisasi*. All 301 `\index{}` keys rewritten in Indonesian |
| Register / tone | **96** | The *kamu* register throughout (0 *Anda* over course and solutions), measured against the Indonesian biology editions rather than assumed: *dapat* 4.4 vs *bisa* 0.05 per 1000 words (biology id: 3.8 / 0.06), *kamu* 0.32, *kita* 0.67. Exercise stems are bare imperatives with *-lah* where Indonesian textbooks use it (*Gambarlah*, *Periksalah*, *Tentukan*). Grades 1–5 are short and concrete; grades 10–12 use the SMA definition frame *Yang disebut \emph{x} adalah ...*, which also keeps every defined term lowercase in mid-sentence (no capitalised harvest) |
| LaTeX hygiene | **99** | Forced build (`latexmk -g`): **0 errors, 0 undefined, 0 overfull, `nullfont` 0, 0 `invalid in math mode`**, `.fls` Indonesian source count **98**, 0 English chapter files pulled in. Eight overfull boxes found on the way (two over-wide tables, three unbreakable `\ce` chains, one long compound word, one credit line, one figure caption) were fixed by rewording or rewrapping, never with `%` or `\hbox`. Line-edge sweeps after the last file: no line-end word hyphen, no line starting on `. , ; : ) ? !`, no doubled word, every file valid UTF-8 |
| Cross-refs / rule compliance | **99** | Labels, `\cref` targets, solution keys, `[resume]`, math spans (byte-for-byte, including internal line breaks), image paths and drawing code identical to English. No programme, curriculum or country name in visible text. No English source and no other edition touched; shared tools touched only by append-only, commented allow-list entries (listed below). No git command run, no commit |
| Figures | **96** | Drawing code byte-identical; only node text, axis labels, legends, `\foreach` label lists, `xticklabels`/`yticklabels` and captions localized. **`!draw` used in 25 ranges** (listed below): `\foreach` label lists, pgfplots `symbolic coords` blocks (ASCII coordinates kept, Indonesian tick labels added), node text the census cannot blank, and one Venn diagram where two labels needed `align=center` to break onto two lines. A label-length census of all 495 nodes against English flagged 41; every flagged figure and every grade-11/12 figure was inspected on its PDF page, and **eleven collisions** were fixed by rewrapping (titration flasks, bond-energy steps, adsorption steps, the Venn diagram, the classification tree, the carbon cycle, the condenser label, the recrystallisation steps, the E133 spectrum label, the zinc/copper panel, the "later" arrow that had been left in English) |
| Solutions | **97** | All 665 exercise solutions and all 42 weekend-problem solutions present and native; every number cross-checked against English by the per-chunk census; every grade-11/12 problem recomputed while translating (titration, bond energies, NMR integrations, rate laws, equilibria, pKa quadratics, buffers, Kohlrausch, Faraday, atom economies, polymer masses) — no canon numeric slip found |
| Defined-term links (`\omterm`) | **96** | **6309 links over 174 distinct targets** against English's **5775 over 172**: every English target reached (0 missing), two extra targets reached by Indonesian forms English misses (*sifat bahannya*, *galvanisasi*). `book1_id.py` curated from **this edition's own harvest** (305 terms): 7 STOP entries mirroring English's everyday-sense list (*larutan*, *bahan*, *benda*, *produk*, *periode*, *lambang*, *kapasitas*), 17 EXTRA short and affixed forms (*ikatan rangkap*, *pasangan bebas*, *kulit terluar*, *dicampur*, *menguap*...), 4 homograph protections (*larutan asam etanoat*, *pengendapan perak klorida*, *hidrasi etena*, *litium-ion*). Frequency and chapter-set censuses run after the last edit; the residual outliers (*waktu paruh*, *energi ikatan*, *keelektronegatifan*, *larutan standar*) are English under-linking irregular plurals, not homographs. `--apply` twice changes nothing; plain dry run **links to insert: 0** |
| MT-artifact freedom | **96** | Indonesian prose gate (gate 8): 0 findings in all twelve years. Twin-comparison gate (gate 9): 0 multi-word findings; the one-word advisory tier read in full — cognates (*proton*, *neutron*, *anion*, *generator*, *ester*, *aspirin*), the redox notation *Red*, the onomatopoeia *pop!*, and one genuine leftover (*later* in a grade-3 arrow label) that was fixed. Orphan-line gate (gate 10): 0. `\text{}` census over course and solutions: every word translated (*diperoleh*, *ikatan diputus*, *unit ulang*, *zat terlarut*...) |

**Overall: 96.**

## Gate output summary

```
bash tools/check_translation.sh grade-1 … grade-12 id
  all twelve years ........... TRANSLATION GATE: PASSED
                               (gates 1-13: completeness, labels, exercise/
                               solution parity, environment census, hygiene,
                               UTF-8, Indonesian prose gate, twin-comparison
                               prose gate, orphan lines, problem numbering,
                               chemistry twin, \ce balance)
  gate 9 advisory tier ....... read in full: cognates + one leftover, fixed

forced build, build/one_chemistry_book_1_school_id.log (grep -a)
  '^!' ................. 0        undefined ............ 0
  Overfull ............. 0        nullfont ............. 0
  'invalid in math mode' 0        pages ................ 450 (English 432)
  .fls Indonesian .tex . 98

python3 tools/link_defined_terms.py --book 1 --lang id      (plain dry run)
  links to insert: 0 across 0 files
links 6309 over 174 targets (English 5775 over 172; 0 English targets missed)
\index 301 = English 301 · \label set diff 0 · \qty 2199 = 2199 · \ce 2267 = 2267
```

## `!draw` ranges (English line numbers)

g1/01 174–185 · g4/01 133–134 · g4/02 158–159 · g5/01 95–96, 105–106,
139–140 · g5/02 148–149 · g7/01 335 · g8/03 133 · g9/02 53–55, 168, 227–229 ·
g9/03 67–70 · g9/04 38 · g10/04 294–297 · g10/07 257 · g11/01 42–45 ·
g11/06 144–151 · g11/09 243–244 · g12/01 88–98, 183–184 · g12/07 197–201 ·
g12/08 142–145 · g12/11 230–231, 312–320.

## Shared-tool appends (append-only, each with a comment)

`tools/check_indonesian_prose.py`: `ATTRIBUTION` += *NOAA Global Monitoring
Laboratory*, *Scripps Institution of Oceanography* (a data credit), *(Léon)
Péan de Saint-Gilles* (an accented name the ASCII tokenizer splits into "on",
"an"); `WORK_TITLE` += *Green Chemistry: Theory and Practice*; `NOT_GATED` +=
*karbokation*; `DECADE_SUFFIX` += the ketone ending *-on* after a locant and
the redox notation *Oks/Red*; `ID_MARKERS` += a chemistry vocabulary block,
table-row nouns and safety-clause words (the density class reads every table
row as a sentence). `tools/check_latin_prose.py`: `ALLOWED_BY_LANG["id"]` +=
*meter* (*pH meter*).

## Samples (Indonesian, with verdict)

1. **grade 2, opening** — "Sebutir gula batu jatuh ke dalam secangkir teh
   panas. Sendok mengaduk, gula batu itu hancur, dan sesaat kemudian tidak ada
   lagi yang terlihat" → **native**: *sebutir / secangkir* classifiers and the
   short paratactic clauses of an Indonesian primary reader.
2. **grade 11, titration** — "Yang disebut \emph{titik ekuivalen} adalah saat
   dalam titrasi ketika titran yang ditambahkan dan spesies yang dititrasi
   berada dalam perbandingan yang sesuai dengan persamaan reaksi: keduanya
   habis." → **native**: the SMA definition frame, *titran / yang
   dititrasi* as Indonesian analytical chemistry says it.
3. **grade 12, curly arrows** — "Panah itu berawal dari pasangan yang
   berpindah, yaitu pasangan elektron bebas atau sebuah ikatan, dan berakhir
   di tempat pasangan itu pergi." → **native**: *berawal / berakhir* with the
   *yaitu* apposition, not a calque of "it starts from ... and ends where".
4. **grade 12, buffers** — "Sepasang spesies, sebuah asam dan basanya
   sendiri, meredam guncangan-guncangan itu." → **native**: reduplicated
   plural and *meredam* (to damp) chosen over a literal "absorb".
5. **grade 12, polymers** — "Sifat-sifatnya --- lunak atau kaku, lentur atau
   rapuh, dapat dilelehkan atau tidak --- tidak terlalu ditentukan oleh
   atom-atom yang dikandungnya, melainkan oleh cara rantai panjangnya
   tersusun." → **native**: *tidak terlalu ... melainkan* carries the English
   "less from ... than from" as an Indonesian contrast, em-dash aside kept.

## Why not 100

* **No Indonesian hyphenation patterns in the TeX stack.** The log says
  "Hyphen rules for 'bahasa' set to \l@english", so Indonesian words are
  broken by English patterns (*ke-d-ua*, *da-p-at* are offered). No bad
  break survives in the PDF that was noticed, and every overfull was cleared
  by rewording, but the paragraph builder works with the wrong patterns. This
  is shared infrastructure for every `id` edition, not something this edition
  can fix.
* **25 `!draw` opt-outs** — each justified, but each a place where only the
  rendered page, not the census, guards the figure.
* **Shared prose gate extended** six times (all append-only, commented); the
  gate's line-based density class and ASCII-only tokenizer are reported as gate
  bugs rather than worked around in the prose.
* **Link density +9 %** against English, mostly from Indonesian forms English
  does not match (irregular plurals, affixed verbs). Every link class was read
  in context; a second pass might still thin the busiest chapters.
* **One English link-layer defect** (the solution to g12/11 exercise 1 links
  "Hydration" of ethene to the hydration-of-ions definition) is *not*
  reproduced here (the Indonesian config protects *Hidrasi:* and *hidrasi
  etena*), so the two editions differ at that one link.

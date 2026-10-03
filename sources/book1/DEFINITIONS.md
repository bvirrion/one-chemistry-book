# Book 1 — defined terms (Phase A, 2026-10-02)

Every term Book 1 will define: one row per term (an `\emph{term}\index{term}`
pair inside the `definition` with that label), pilots included. 183
definition environments, 300 terms, in 49 chapters. Generated from the
definition lines of `BRIEFS.md` (Phase A) and the three pilots; in Phase B a
row changes only with the brief, and a row never moves to another chapter
without a ruling.

Status column: **map** = the outline's Book 1 map gives the notion to this
chapter; **in-volume, not in map** = a Book 1-internal term placed at its
first natural use (no other chapter's brief defines it); **pilot** = already
written and approved; **Cn** = see § Contested below.

Check run 2026-10-02: no term appears in two rows (`sort | uniq -d` over the
term column prints nothing), except the deliberate multi-word pairs listed in
§ Homographs, which are different terms sharing a word.

## Contested and ambiguous notions (the map allows two readings)

- **C1 — "solution".** The map gives "dissolving, solution (everyday)" to g2
  (pilot, `def:g2:mixing-and-dissolving:dissolve`) and recalls it in g6. The
  term config's docstring anticipated a second, chemist's definition of
  "solution" in g6. **Proposal: one owner.** g2 keeps "solution"; g6
  `solutions-and-solubility` defines *solute*, *solvent*, *aqueous solution*
  and states in a proposition that any liquid can be the solvent. No second
  `\emph{solution}`. (Linker: "solution" stays a global term from g2 on;
  the exercise-solution homograph is handled by `EXTRA_PROTECT` /
  `NO_CAPITAL` in Phase C — see § Homographs.)
- **C2 — "mix" (g2, verb) vs "mixture" (g6).** Different terms; both kept.
  g6's definition says "a mixture contains several chemical species", which
  g2 could not say (no species yet).
- **C3 — "combustion".** The map gives "fire triangle, burning makes new
  substances" to g4 and "complete/incomplete combustion" to g8. **Proposal:**
  g4 `what-a-fire-needs` defines *burning* and *combustion* (one
  definition: "chemists call a burning a combustion"); g8 recalls it and
  defines only *complete combustion* / *incomplete combustion*.
- **C4 — "chemical change" (g5) vs "chemical reaction" (g7).** The map gives
  "chemical change (everyday, irreversible)" to g5 and "reactants, products,
  rearrangement of atoms" to g7, whose outline line also says "a chemical
  transformation versus a physical one". **Proposal:** g5 defines *reversible
  change*, *irreversible change* and *chemical change* (new substances
  appear); g7 recalls "chemical change" and defines *chemical reaction* (the
  model: reactants consumed, products formed), *reactant*, *product*,
  *physical transformation* and *word equation*. "Chemical transformation"
  is used in prose as a synonym of "chemical change", never defined.
  **C4b (boundary g7 / g8):** g7 states that atoms are rearranged, neither
  created nor destroyed (a proposition read off the models); g8 owns the
  *law* of conservation of mass, the chemical equation, coefficients and the
  balancing method. g7 shows correctly-counted models but teaches no
  balancing.
- **C5 — natural / manufactured (g5) vs natural / artificial / synthetic
  (g8).** **Proposal:** g5 defines *natural material* and *manufactured
  material*; g8 refines "manufactured" into *artificial material* (a natural
  material chemically transformed: viscose, paper) and *synthetic material*
  (made from species built by chemists: nylon, polyethene), and does not
  define "natural material" again.
- **C6 — "extraction".** The Book 1 map lists *extraction* under g10
  `chemical-species` ("extraction, TLC, Rf") **and** under g11 `dissolution`
  ("solvation, extraction, amphiphiles"). **Proposal:** g10 owns
  *extraction* and *liquid–liquid extraction* (the procedure, the separating
  funnel, the solvent chosen from a data table); g11 recalls them and adds
  only the *reason* (polarity, "like dissolves like") with the terms
  *dissociation*, *solvation*, *hydrophilic/hydrophobic*, *amphiphilic*,
  *micelle*.
- **C7 — "chemical element".** Could be owned by g9 `inside-the-atom`
  (defined by Z) or g9 `periodic-table-first-look` (whose outline line reads
  "Elements, symbols, atomic number"). **Proposal:** g9 `inside-the-atom`,
  because the definition needs Z and the isotope definition ("same element,
  different A") needs the element first. The periodic-table chapter recalls
  it. (The g7 pilot deliberately avoids the word: "about a hundred different
  kinds of atoms".)
- **C8 — "synthetic".** *synthetic material* (g8 `plastics`) and *synthetic
  species* (g10 `chemical-species`: a species made by chemists, possibly
  identical to a natural one) are different notions with a shared word. Both
  kept as multi-word terms; the bare word "synthetic" is never a term.
- **C9 — "family".** g10 `electron-shells` defines *chemical family* (a
  column of the periodic table with shared behaviour: alkali metals,
  halogens, noble gases). g11 `functional-groups` would naturally say
  "families of organic compounds". **Proposal:** g11 defines *functional
  group* and the family names (alcohol, aldehyde…), uses "family" in prose
  only, and the linker gets `STOP` for "family"/"families" outside g10.
- **C10 — "group".** *group* of the periodic table (g9
  `periodic-table-first-look`), *functional group* (g11), *alkyl group* (g11)
  and the pilot's "a group of atoms" (g7 molecule definition). **Proposal:**
  g9 defines *period* and *group*; linker `STOP` for "group"/"groups" and
  "period"/"periods" outside g9 (multi-word "functional group", "alkyl
  group" keep their own links).
- **C11 — "indicator".** The map gives it to g12 `buffers-predominance`,
  but g9 `acids-bases-ph` measures pH with pH paper and a universal
  indicator. **Proposal:** g9 defines *pH paper* and *pH meter* only and
  mentions "a coloured indicator" in prose (unlinked: the term is not yet
  defined); g12 defines *acid–base indicator* (HInd/Ind⁻, colour-change
  range).
- **C12 — "pH".** The map gives "H⁺, OH⁻, pH scale" to g9 and "Brønsted,
  Ka, pKa, Ke" to g12 `ka-and-pka`. The quantitative definition pH =
  −log([H₃O⁺]/c°) can only come in grade 12 (log guard). **Proposal:** g9
  owns the term *pH* (a number from 0 to 14, lower = more acidic); g12 gives
  the formula in a `definition` titled "The pH, precisely" with the label
  `def:g12:ka-and-pka:ph-log` and **no** `\emph{pH}\index{pH}` pair (the
  leaf "ph-log" and the 2-letter key keep the harvester off it), so the term
  keeps one owner and links to g9.
- **C13 — "conductivity".** g9 `ions` says ionic solutions "conduct
  electricity" (verb, everyday); g12 `ph-conductivity-titrations` defines
  *conductivity* and *molar ionic conductivity*. Not in the map; owner g12.
- **C14 — "evaporating".** g3 owns it as a separation method (map ✓); the
  change of state itself is physics. The definition is worded as a
  separation ("the water dries away, the dissolved solid stays").
- **C15 — "distillation".** Not in the Book 1 map. g10 `chemical-species`
  defines *distillation* and *hydrodistillation* (lavender oil); g11
  `organic-skeletons` tells fractional distillation of crude oil in prose
  only. The Year 1 lab chapter and the Year 2 phase-diagram chapter own the
  rigorous treatment (not a Book 1 concern).
- **C16 — terms the university map re-founds.** Book 1 defines, in-volume,
  several words a university chapter later re-founds rigorously, as the
  series map allows: *multiplet*, *n + 1 rule* (g12 `proton-nmr`; Year 1
  `structure-spectroscopy` adds coupling constants), *Cram representation*,
  *conformation* (g12 `stereochemistry`; Year 1 `stereochemistry-in-depth`
  adds Newman and CIP), *elementary step*, *reaction intermediate* (g12
  `curly-arrows`; Year 1 `elementary-steps`), *electron-donor/acceptor site*
  (g12; Year 1 `electronic-effects` says nucleophile/electrophile),
  *protecting group* (g12; Year 1 `acetals-protection`). Book 1 never uses
  the university names VSEPR, dipole moment, nucleophile, electrophile,
  Markovnikov, coupling constant, enthalpy, Nernst, standard potential as
  defined terms (they may appear once in a forward-pointing remark, never in
  `\emph{}\index{}`).
- **C17 — homographs for the linker (Phase C), from this term list:**
  *solution* (exercise solutions), *table* (periodic table vs a table),
  *group*, *period*, *family*, *shell*, *mole* (unit vs animal — fine in
  practice), *yield* (verb), *integration* (mathematics), *cell*
  (electrochemical cell vs biology's cell vs a table cell — multi-word term
  only), *system* (multi-word "chemical system" only), *phase* (stationary
  phase vs "phase" in physics — multi-word only), *reduction* (in cost),
  *charge* (partial charge multi-word only), *addition* (arithmetic!) and
  *substitution* (everyday) — the category terms of g12 `curly-arrows` need
  `STOP` outside g12 or `EXTRA_PROTECT` for "in addition", *equivalence*
  (logic), *product* (multiplication: "the product of"), *material*,
  *property*, *object* (g1 words used everywhere in their ordinary sense:
  candidates for `STOP` outside g1), *air*, *fuel*, *rust*, *recycling*
  (probably fine), *metal* (everyday before g9), *element* (only the
  multi-word "chemical element" is harvested), *base* (only "Brønsted base",
  "basic solution"), *bond* (only multi-word bond terms), *species* (only
  "chemical species").

## Terms used in Book 1 but not defined in it (their owner)

- **Physics (One Physics Book):** states of matter, melting / boiling
  temperature, change of state, density, mass, volume, temperature, heat,
  energy, pressure, gas (as a state), electric current, voltage, charge,
  circuit, light, wavelength, colour of light, magnet, radioactivity,
  half-life of a nucleus, magnetic field (NMR is told).
- **Mathematics (One Math Book):** fraction, percentage, power, scientific
  notation, proportionality, linear function, tangent, derivative, exp, ln,
  log10, quadratic equation.
- **Biology (One Biology Book):** cell (living), enzyme as a protein (the
  catalyst angle is defined here), DNA, protein, respiration, blood.
- **University chemistry (Books 2–4, never defined in Book 1):** VSEPR,
  dipole moment, standard potential, Nernst equation, enthalpy, entropy,
  nucleophile, electrophile, leaving group, SN1/SN2, E1/E2, Markovnikov,
  coupling constant, CIP priority rules (only "higher atomic number first"
  for Z/E), Type A/B uncertainty, lattice / unit cell.

## Notations (no harvested term)

- `not:g8:balanced-equations:states` — (s), (l), (g)
- `not:g9:ions:aq` — (aq)
- `not:g12:equilibrium:c-standard` — c° = 1 mol/L
- `def:g12:ka-and-pka:ph-log` — the quantitative pH (definition without a
  new term, C12)

## The term list

| # | grade | chapter | term | label | status |
|---|---|---|---|---|---|
| 1 | g1 | `materials-around-us` | material | `def:g1:materials-around-us:material` | map |
| 2 | g1 | `materials-around-us` | object | `def:g1:materials-around-us:object` | map |
| 3 | g1 | `materials-around-us` | property of a material | `def:g1:materials-around-us:property` | in-volume, not in map |
| 4 | g2 | `mixing-and-dissolving` | dissolve | `def:g2:mixing-and-dissolving:dissolve` | pilot; C1 (solution) |
| 5 | g2 | `mixing-and-dissolving` | solution | `def:g2:mixing-and-dissolving:dissolve` | pilot; C1 (solution) |
| 6 | g2 | `mixing-and-dissolving` | mix | `def:g2:mixing-and-dissolving:mix` | pilot (written) |
| 7 | g3 | `separating-mixtures` | settling | `def:g3:separating-mixtures:decant` | map |
| 8 | g3 | `separating-mixtures` | decanting | `def:g3:separating-mixtures:decant` | map |
| 9 | g3 | `separating-mixtures` | evaporating | `def:g3:separating-mixtures:evaporate` | C14 |
| 10 | g3 | `separating-mixtures` | filtering | `def:g3:separating-mixtures:filter` | map |
| 11 | g3 | `separating-mixtures` | filtrate | `def:g3:separating-mixtures:filter` | map |
| 12 | g3 | `separating-mixtures` | sieving | `def:g3:separating-mixtures:sieve` | in-volume, not in map |
| 13 | g4 | `air-a-mixture-of-gases` | air | `def:g4:air-a-mixture-of-gases:air` | map |
| 14 | g4 | `what-a-fire-needs` | burning | `def:g4:what-a-fire-needs:burning` | C3 |
| 15 | g4 | `what-a-fire-needs` | combustion | `def:g4:what-a-fire-needs:burning` | C3 |
| 16 | g4 | `what-a-fire-needs` | fire triangle | `def:g4:what-a-fire-needs:fire-triangle` | map |
| 17 | g4 | `what-a-fire-needs` | fuel | `def:g4:what-a-fire-needs:fuel` | map |
| 18 | g5 | `irreversible-changes` | irreversible change | `def:g5:irreversible-changes:chemical-change` | C4 |
| 19 | g5 | `irreversible-changes` | chemical change | `def:g5:irreversible-changes:chemical-change` | C4 |
| 20 | g5 | `irreversible-changes` | reversible change | `def:g5:irreversible-changes:reversible` | map |
| 21 | g5 | `raw-materials-and-recycling` | natural material | `def:g5:raw-materials-and-recycling:natural-material` | C5 |
| 22 | g5 | `raw-materials-and-recycling` | manufactured material | `def:g5:raw-materials-and-recycling:natural-material` | C5 |
| 23 | g5 | `raw-materials-and-recycling` | raw material | `def:g5:raw-materials-and-recycling:raw-material` | in-volume, not in map |
| 24 | g5 | `raw-materials-and-recycling` | ore | `def:g5:raw-materials-and-recycling:raw-material` | in-volume, not in map |
| 25 | g5 | `raw-materials-and-recycling` | recycling | `def:g5:raw-materials-and-recycling:recycling` | map |
| 26 | g5 | `raw-materials-and-recycling` | resource | `def:g5:raw-materials-and-recycling:resource` | map |
| 27 | g5 | `raw-materials-and-recycling` | renewable resource | `def:g5:raw-materials-and-recycling:resource` | map |
| 28 | g6 | `pure-substances-and-mixtures` | homogeneous mixture | `def:g6:pure-substances-and-mixtures:homogeneous` | map |
| 29 | g6 | `pure-substances-and-mixtures` | heterogeneous mixture | `def:g6:pure-substances-and-mixtures:homogeneous` | map |
| 30 | g6 | `pure-substances-and-mixtures` | mixture | `def:g6:pure-substances-and-mixtures:mixture` | C2 |
| 31 | g6 | `pure-substances-and-mixtures` | pure substance | `def:g6:pure-substances-and-mixtures:pure-substance` | map |
| 32 | g6 | `pure-substances-and-mixtures` | chemical species | `def:g6:pure-substances-and-mixtures:species` | map |
| 33 | g6 | `solutions-and-solubility` | miscible | `def:g6:solutions-and-solubility:miscible` | map |
| 34 | g6 | `solutions-and-solubility` | immiscible | `def:g6:solutions-and-solubility:miscible` | map |
| 35 | g6 | `solutions-and-solubility` | saturated solution | `def:g6:solutions-and-solubility:saturated` | map |
| 36 | g6 | `solutions-and-solubility` | solubility | `def:g6:solutions-and-solubility:solubility` | map |
| 37 | g6 | `solutions-and-solubility` | solute | `def:g6:solutions-and-solubility:solute` | C1 |
| 38 | g6 | `solutions-and-solubility` | solvent | `def:g6:solutions-and-solubility:solute` | C1 |
| 39 | g6 | `solutions-and-solubility` | aqueous solution | `def:g6:solutions-and-solubility:solute` | C1 |
| 40 | g7 | `identifying-substances` | characteristic test | `def:g7:identifying-substances:characteristic-test` | in-volume, not in map |
| 41 | g7 | `identifying-substances` | reagent | `def:g7:identifying-substances:characteristic-test` | in-volume, not in map |
| 42 | g7 | `identifying-substances` | paper chromatography | `def:g7:identifying-substances:chromatography` | map |
| 43 | g7 | `identifying-substances` | chromatogram | `def:g7:identifying-substances:chromatography` | map |
| 44 | g7 | `atoms-and-molecules` | atom | `def:g7:atoms-and-molecules:atom` | pilot (written) |
| 45 | g7 | `atoms-and-molecules` | chemical formula | `def:g7:atoms-and-molecules:formula` | pilot (written) |
| 46 | g7 | `atoms-and-molecules` | subscript | `def:g7:atoms-and-molecules:formula` | pilot (written) |
| 47 | g7 | `atoms-and-molecules` | molecule | `def:g7:atoms-and-molecules:molecule` | pilot (written) |
| 48 | g7 | `atoms-and-molecules` | symbol of an atom | `def:g7:atoms-and-molecules:symbol` | pilot (written) |
| 49 | g7 | `chemical-reactions` | physical transformation | `def:g7:chemical-reactions:physical-transformation` | C4 |
| 50 | g7 | `chemical-reactions` | reactant | `def:g7:chemical-reactions:reactant` | map |
| 51 | g7 | `chemical-reactions` | product | `def:g7:chemical-reactions:reactant` | map |
| 52 | g7 | `chemical-reactions` | chemical reaction | `def:g7:chemical-reactions:reaction` | C4 |
| 53 | g7 | `chemical-reactions` | word equation | `def:g7:chemical-reactions:word-equation` | in-volume, not in map |
| 54 | g8 | `balanced-equations` | stoichiometric coefficient | `def:g8:balanced-equations:coefficient` | in-volume, not in map |
| 55 | g8 | `balanced-equations` | conservation of mass | `def:g8:balanced-equations:conservation` | map |
| 56 | g8 | `balanced-equations` | chemical equation | `def:g8:balanced-equations:equation` | map |
| 57 | g8 | `balanced-equations` | balanced equation | `def:g8:balanced-equations:equation` | map |
| 58 | g8 | `combustion-and-fuels` | complete combustion | `def:g8:combustion-and-fuels:complete` | C3 |
| 59 | g8 | `combustion-and-fuels` | incomplete combustion | `def:g8:combustion-and-fuels:complete` | C3 |
| 60 | g8 | `combustion-and-fuels` | fossil fuel | `def:g8:combustion-and-fuels:fossil` | in-volume, not in map |
| 61 | g8 | `combustion-and-fuels` | renewable fuel | `def:g8:combustion-and-fuels:fossil` | in-volume, not in map |
| 62 | g8 | `combustion-and-fuels` | greenhouse gas | `def:g8:combustion-and-fuels:greenhouse` | map |
| 63 | g8 | `plastics` | artificial material | `def:g8:plastics:artificial` | C5, C8 |
| 64 | g8 | `plastics` | synthetic material | `def:g8:plastics:artificial` | C5, C8 |
| 65 | g8 | `plastics` | resin identification code | `def:g8:plastics:code` | in-volume, not in map |
| 66 | g8 | `plastics` | plastic | `def:g8:plastics:plastic` | map |
| 67 | g8 | `plastics` | thermoplastic | `def:g8:plastics:thermoplastic` | in-volume, not in map |
| 68 | g8 | `plastics` | thermoset | `def:g8:plastics:thermoplastic` | in-volume, not in map |
| 69 | g9 | `inside-the-atom` | atomic number | `def:g9:inside-the-atom:atomic-number` | map |
| 70 | g9 | `inside-the-atom` | mass number | `def:g9:inside-the-atom:atomic-number` | map |
| 71 | g9 | `inside-the-atom` | chemical element | `def:g9:inside-the-atom:element` | C7 |
| 72 | g9 | `inside-the-atom` | isotopes | `def:g9:inside-the-atom:isotope` | map |
| 73 | g9 | `inside-the-atom` | nucleus | `def:g9:inside-the-atom:nucleus` | map |
| 74 | g9 | `inside-the-atom` | electron | `def:g9:inside-the-atom:nucleus` | map |
| 75 | g9 | `inside-the-atom` | proton | `def:g9:inside-the-atom:proton` | map |
| 76 | g9 | `inside-the-atom` | neutron | `def:g9:inside-the-atom:proton` | map |
| 77 | g9 | `inside-the-atom` | nucleon | `def:g9:inside-the-atom:proton` | map |
| 78 | g9 | `ions` | ion | `def:g9:ions:ion` | map |
| 79 | g9 | `ions` | cation | `def:g9:ions:ion` | map |
| 80 | g9 | `ions` | anion | `def:g9:ions:ion` | map |
| 81 | g9 | `ions` | ionic compound | `def:g9:ions:ionic-compound` | map |
| 82 | g9 | `ions` | precipitate | `def:g9:ions:precipitate` | in-volume, not in map |
| 83 | g9 | `ions` | precipitation | `def:g9:ions:precipitate` | in-volume, not in map |
| 84 | g9 | `acids-bases-ph` | acidic solution | `def:g9:acids-bases-ph:acidic` | map |
| 85 | g9 | `acids-bases-ph` | basic solution | `def:g9:acids-bases-ph:acidic` | map |
| 86 | g9 | `acids-bases-ph` | neutral solution | `def:g9:acids-bases-ph:acidic` | map |
| 87 | g9 | `acids-bases-ph` | pH | `def:g9:acids-bases-ph:ph` | C12 |
| 88 | g9 | `acids-bases-ph` | pH paper | `def:g9:acids-bases-ph:ph-paper` | C11 |
| 89 | g9 | `acids-bases-ph` | pH meter | `def:g9:acids-bases-ph:ph-paper` | C11 |
| 90 | g9 | `metals-acids-corrosion` | corrosion | `def:g9:metals-acids-corrosion:corrosion` | map |
| 91 | g9 | `metals-acids-corrosion` | rust | `def:g9:metals-acids-corrosion:corrosion` | map |
| 92 | g9 | `metals-acids-corrosion` | galvanising | `def:g9:metals-acids-corrosion:galvanising` | in-volume, not in map |
| 93 | g9 | `metals-acids-corrosion` | spectator ion | `def:g9:metals-acids-corrosion:spectator` | in-volume, not in map |
| 94 | g9 | `periodic-table-first-look` | metal | `def:g9:periodic-table-first-look:metal` | map |
| 95 | g9 | `periodic-table-first-look` | non-metal | `def:g9:periodic-table-first-look:metal` | map |
| 96 | g9 | `periodic-table-first-look` | period | `def:g9:periodic-table-first-look:period` | C10 |
| 97 | g9 | `periodic-table-first-look` | group | `def:g9:periodic-table-first-look:period` | C10 |
| 98 | g9 | `periodic-table-first-look` | periodic table | `def:g9:periodic-table-first-look:periodic-table` | map |
| 99 | g9 | `elements-universe-earth` | abundance | `def:g9:elements-universe-earth:abundance` | map |
| 100 | g10 | `chemical-species` | distillation | `def:g10:chemical-species:distillation` | C15 |
| 101 | g10 | `chemical-species` | hydrodistillation | `def:g10:chemical-species:distillation` | C15 |
| 102 | g10 | `chemical-species` | extraction | `def:g10:chemical-species:extraction` | C6 |
| 103 | g10 | `chemical-species` | liquid–liquid extraction | `def:g10:chemical-species:extraction` | C6 |
| 104 | g10 | `chemical-species` | natural species | `def:g10:chemical-species:natural` | C8 |
| 105 | g10 | `chemical-species` | synthetic species | `def:g10:chemical-species:natural` | C8 |
| 106 | g10 | `chemical-species` | retention factor | `def:g10:chemical-species:retention-factor` | map |
| 107 | g10 | `chemical-species` | thin-layer chromatography | `def:g10:chemical-species:tlc` | map |
| 108 | g10 | `chemical-species` | stationary phase | `def:g10:chemical-species:tlc` | map |
| 109 | g10 | `chemical-species` | eluent | `def:g10:chemical-species:tlc` | map |
| 110 | g10 | `electron-shells` | electron configuration | `def:g10:electron-shells:configuration` | map |
| 111 | g10 | `electron-shells` | shell | `def:g10:electron-shells:configuration` | map |
| 112 | g10 | `electron-shells` | subshell | `def:g10:electron-shells:configuration` | map |
| 113 | g10 | `electron-shells` | chemical family | `def:g10:electron-shells:family` | C9 |
| 114 | g10 | `electron-shells` | alkali metals | `def:g10:electron-shells:family` | C9 |
| 115 | g10 | `electron-shells` | halogens | `def:g10:electron-shells:family` | C9 |
| 116 | g10 | `electron-shells` | noble gases | `def:g10:electron-shells:family` | C9 |
| 117 | g10 | `electron-shells` | duet rule | `def:g10:electron-shells:octet` | map |
| 118 | g10 | `electron-shells` | octet rule | `def:g10:electron-shells:octet` | map |
| 119 | g10 | `electron-shells` | valence electrons | `def:g10:electron-shells:valence` | map |
| 120 | g10 | `electron-shells` | core electrons | `def:g10:electron-shells:valence` | map |
| 121 | g10 | `lewis-and-shape` | covalent bond | `def:g10:lewis-and-shape:covalent-bond` | map |
| 122 | g10 | `lewis-and-shape` | Lewis structure | `def:g10:lewis-and-shape:lewis-structure` | map |
| 123 | g10 | `lewis-and-shape` | bonding pair | `def:g10:lewis-and-shape:lone-pair` | in-volume, not in map |
| 124 | g10 | `lewis-and-shape` | lone pair | `def:g10:lewis-and-shape:lone-pair` | in-volume, not in map |
| 125 | g10 | `lewis-and-shape` | double bond | `def:g10:lewis-and-shape:multiple-bond` | in-volume, not in map |
| 126 | g10 | `lewis-and-shape` | triple bond | `def:g10:lewis-and-shape:multiple-bond` | in-volume, not in map |
| 127 | g10 | `the-mole` | amount of substance | `def:g10:the-mole:amount` | map |
| 128 | g10 | `the-mole` | mole | `def:g10:the-mole:amount` | map |
| 129 | g10 | `the-mole` | Avogadro constant | `def:g10:the-mole:avogadro` | map |
| 130 | g10 | `the-mole` | molar mass | `def:g10:the-mole:molar-mass` | in-volume, not in map |
| 131 | g10 | `the-mole` | atomic molar mass | `def:g10:the-mole:molar-mass` | in-volume, not in map |
| 132 | g10 | `the-mole` | molar volume | `def:g10:the-mole:molar-volume` | in-volume, not in map |
| 133 | g10 | `concentration-and-dilution` | dilution | `def:g10:concentration-and-dilution:dilution` | map |
| 134 | g10 | `concentration-and-dilution` | stock solution | `def:g10:concentration-and-dilution:dilution` | map |
| 135 | g10 | `concentration-and-dilution` | dilution factor | `def:g10:concentration-and-dilution:dilution` | map |
| 136 | g10 | `concentration-and-dilution` | mass concentration | `def:g10:concentration-and-dilution:mass-concentration` | map |
| 137 | g10 | `concentration-and-dilution` | molar concentration | `def:g10:concentration-and-dilution:molar-concentration` | map |
| 138 | g10 | `concentration-and-dilution` | standard solution | `def:g10:concentration-and-dilution:standard` | in-volume, not in map |
| 139 | g10 | `concentration-and-dilution` | calibration scale | `def:g10:concentration-and-dilution:standard` | in-volume, not in map |
| 140 | g10 | `reaction-progress-table` | extent of reaction | `def:g10:reaction-progress-table:extent` | map |
| 141 | g10 | `reaction-progress-table` | progress table | `def:g10:reaction-progress-table:extent` | map |
| 142 | g10 | `reaction-progress-table` | limiting reactant | `def:g10:reaction-progress-table:limiting` | map |
| 143 | g10 | `reaction-progress-table` | maximum extent | `def:g10:reaction-progress-table:limiting` | map |
| 144 | g10 | `reaction-progress-table` | total reaction | `def:g10:reaction-progress-table:limiting` | map |
| 145 | g10 | `reaction-progress-table` | stoichiometric mixture | `def:g10:reaction-progress-table:stoichiometric` | in-volume, not in map |
| 146 | g10 | `reaction-progress-table` | chemical system | `def:g10:reaction-progress-table:system` | in-volume, not in map |
| 147 | g10 | `reaction-progress-table` | initial state | `def:g10:reaction-progress-table:system` | in-volume, not in map |
| 148 | g10 | `reaction-progress-table` | final state | `def:g10:reaction-progress-table:system` | in-volume, not in map |
| 149 | g10 | `synthesis-yield` | recrystallisation | `def:g10:synthesis-yield:recrystallisation` | map |
| 150 | g10 | `synthesis-yield` | heating under reflux | `def:g10:synthesis-yield:reflux` | map |
| 151 | g10 | `synthesis-yield` | synthesis | `def:g10:synthesis-yield:synthesis` | in-volume, not in map |
| 152 | g10 | `synthesis-yield` | crude product | `def:g10:synthesis-yield:synthesis` | in-volume, not in map |
| 153 | g10 | `synthesis-yield` | vacuum filtration | `def:g10:synthesis-yield:vacuum-filtration` | in-volume, not in map |
| 154 | g10 | `synthesis-yield` | yield | `def:g10:synthesis-yield:yield` | map |
| 155 | g11 | `absorbance` | absorbance | `def:g11:absorbance:absorbance` | map |
| 156 | g11 | `absorbance` | calibration line | `def:g11:absorbance:calibration-line` | in-volume, not in map |
| 157 | g11 | `absorbance` | complementary colours | `def:g11:absorbance:complementary` | in-volume, not in map |
| 158 | g11 | `absorbance` | molar absorption coefficient | `def:g11:absorbance:epsilon` | in-volume, not in map |
| 159 | g11 | `absorbance` | absorption spectrum | `def:g11:absorbance:spectrum` | in-volume, not in map |
| 160 | g11 | `polarity-and-cohesion` | electronegativity | `def:g11:polarity-and-cohesion:electronegativity` | map |
| 161 | g11 | `polarity-and-cohesion` | hydrogen bond | `def:g11:polarity-and-cohesion:hydrogen-bond` | map |
| 162 | g11 | `polarity-and-cohesion` | molecular solid | `def:g11:polarity-and-cohesion:molecular-solid` | in-volume, not in map |
| 163 | g11 | `polarity-and-cohesion` | polar bond | `def:g11:polarity-and-cohesion:polar-bond` | in-volume, not in map |
| 164 | g11 | `polarity-and-cohesion` | partial charge | `def:g11:polarity-and-cohesion:polar-bond` | in-volume, not in map |
| 165 | g11 | `polarity-and-cohesion` | polar molecule | `def:g11:polarity-and-cohesion:polar-molecule` | map |
| 166 | g11 | `polarity-and-cohesion` | non-polar molecule | `def:g11:polarity-and-cohesion:polar-molecule` | map |
| 167 | g11 | `polarity-and-cohesion` | van der Waals interaction | `def:g11:polarity-and-cohesion:van-der-waals` | map |
| 168 | g11 | `dissolution` | amphiphilic | `def:g11:dissolution:amphiphilic` | map |
| 169 | g11 | `dissolution` | micelle | `def:g11:dissolution:amphiphilic` | map |
| 170 | g11 | `dissolution` | dissociation | `def:g11:dissolution:dissociation` | in-volume, not in map |
| 171 | g11 | `dissolution` | hydrophilic | `def:g11:dissolution:hydrophilic` | in-volume, not in map |
| 172 | g11 | `dissolution` | hydrophobic | `def:g11:dissolution:hydrophilic` | in-volume, not in map |
| 173 | g11 | `dissolution` | solvation | `def:g11:dissolution:solvation` | C6 |
| 174 | g11 | `dissolution` | hydration | `def:g11:dissolution:solvation` | C6 |
| 175 | g11 | `organic-skeletons` | alkane | `def:g11:organic-skeletons:alkane` | C10 |
| 176 | g11 | `organic-skeletons` | alkyl group | `def:g11:organic-skeletons:alkane` | C10 |
| 177 | g11 | `organic-skeletons` | molecular formula | `def:g11:organic-skeletons:formulas` | map |
| 178 | g11 | `organic-skeletons` | structural formula | `def:g11:organic-skeletons:formulas` | map |
| 179 | g11 | `organic-skeletons` | semi-structural formula | `def:g11:organic-skeletons:formulas` | map |
| 180 | g11 | `organic-skeletons` | skeletal formula | `def:g11:organic-skeletons:formulas` | map |
| 181 | g11 | `organic-skeletons` | isomers | `def:g11:organic-skeletons:isomer` | map |
| 182 | g11 | `organic-skeletons` | constitutional isomers | `def:g11:organic-skeletons:isomer` | map |
| 183 | g11 | `organic-skeletons` | organic compound | `def:g11:organic-skeletons:organic` | in-volume, not in map |
| 184 | g11 | `functional-groups` | alcohol | `def:g11:functional-groups:alcohol` | in-volume, not in map |
| 185 | g11 | `functional-groups` | class of an alcohol | `def:g11:functional-groups:alcohol` | in-volume, not in map |
| 186 | g11 | `functional-groups` | amine | `def:g11:functional-groups:amine` | in-volume, not in map |
| 187 | g11 | `functional-groups` | amide | `def:g11:functional-groups:amine` | in-volume, not in map |
| 188 | g11 | `functional-groups` | aldehyde | `def:g11:functional-groups:carbonyl` | in-volume, not in map |
| 189 | g11 | `functional-groups` | ketone | `def:g11:functional-groups:carbonyl` | in-volume, not in map |
| 190 | g11 | `functional-groups` | carboxylic acid | `def:g11:functional-groups:carboxylic-acid` | in-volume, not in map |
| 191 | g11 | `functional-groups` | ester | `def:g11:functional-groups:carboxylic-acid` | in-volume, not in map |
| 192 | g11 | `functional-groups` | functional group | `def:g11:functional-groups:functional-group` | map |
| 193 | g11 | `functional-groups` | halogenoalkane | `def:g11:functional-groups:halogenoalkane` | in-volume, not in map |
| 194 | g11 | `functional-groups` | alkene | `def:g11:functional-groups:halogenoalkane` | in-volume, not in map |
| 195 | g11 | `infrared` | absorption band | `def:g11:infrared:band` | in-volume, not in map |
| 196 | g11 | `infrared` | fingerprint region | `def:g11:infrared:band` | in-volume, not in map |
| 197 | g11 | `infrared` | infrared spectrum | `def:g11:infrared:spectrum` | map |
| 198 | g11 | `infrared` | transmittance | `def:g11:infrared:spectrum` | map |
| 199 | g11 | `infrared` | wavenumber | `def:g11:infrared:wavenumber` | in-volume, not in map |
| 200 | g11 | `redox` | redox couple | `def:g11:redox:couple` | pilot (written) |
| 201 | g11 | `redox` | half-equation | `def:g11:redox:couple` | pilot (written) |
| 202 | g11 | `redox` | oxidant | `def:g11:redox:oxidant` | pilot (written) |
| 203 | g11 | `redox` | reductant | `def:g11:redox:oxidant` | pilot (written) |
| 204 | g11 | `redox` | oxidation | `def:g11:redox:oxidation` | pilot (written) |
| 205 | g11 | `redox` | reduction | `def:g11:redox:oxidation` | pilot (written) |
| 206 | g11 | `redox` | redox reaction | `def:g11:redox:reaction` | pilot (written) |
| 207 | g11 | `titration` | equivalence | `def:g11:titration:equivalence` | map |
| 208 | g11 | `titration` | equivalent volume | `def:g11:titration:equivalence` | map |
| 209 | g11 | `titration` | titration | `def:g11:titration:titration` | map |
| 210 | g11 | `titration` | titrant | `def:g11:titration:titration` | map |
| 211 | g11 | `titration` | titrated solution | `def:g11:titration:titration` | map |
| 212 | g11 | `reaction-energy` | bond energy | `def:g11:reaction-energy:bond-energy` | map |
| 213 | g11 | `reaction-energy` | molar energy of combustion | `def:g11:reaction-energy:combustion-energy` | in-volume, not in map |
| 214 | g11 | `reaction-energy` | exothermic | `def:g11:reaction-energy:exothermic` | map |
| 215 | g11 | `reaction-energy` | endothermic | `def:g11:reaction-energy:exothermic` | map |
| 216 | g12 | `proton-nmr` | equivalent protons | `def:g12:proton-nmr:equivalent` | in-volume, not in map |
| 217 | g12 | `proton-nmr` | integration curve | `def:g12:proton-nmr:integration` | in-volume, not in map |
| 218 | g12 | `proton-nmr` | multiplet | `def:g12:proton-nmr:multiplet` | in-volume, not in map |
| 219 | g12 | `proton-nmr` | n + 1 rule | `def:g12:proton-nmr:multiplet` | in-volume, not in map |
| 220 | g12 | `proton-nmr` | NMR spectrum | `def:g12:proton-nmr:spectrum` | map |
| 221 | g12 | `proton-nmr` | chemical shift | `def:g12:proton-nmr:spectrum` | map |
| 222 | g12 | `stereochemistry` | chiral | `def:g12:stereochemistry:chiral` | map |
| 223 | g12 | `stereochemistry` | asymmetric carbon | `def:g12:stereochemistry:chiral` | map |
| 224 | g12 | `stereochemistry` | conformation | `def:g12:stereochemistry:conformation` | in-volume, not in map |
| 225 | g12 | `stereochemistry` | Cram representation | `def:g12:stereochemistry:cram` | in-volume, not in map |
| 226 | g12 | `stereochemistry` | diastereomers | `def:g12:stereochemistry:diastereomer` | in-volume, not in map |
| 227 | g12 | `stereochemistry` | enantiomers | `def:g12:stereochemistry:enantiomer` | map |
| 228 | g12 | `stereochemistry` | racemic mixture | `def:g12:stereochemistry:enantiomer` | map |
| 229 | g12 | `stereochemistry` | stereoisomers | `def:g12:stereochemistry:stereoisomer` | in-volume, not in map |
| 230 | g12 | `stereochemistry` | Z/E isomers | `def:g12:stereochemistry:z-e` | map |
| 231 | g12 | `curly-arrows` | substitution | `def:g12:curly-arrows:categories` | map |
| 232 | g12 | `curly-arrows` | addition | `def:g12:curly-arrows:categories` | map |
| 233 | g12 | `curly-arrows` | elimination | `def:g12:curly-arrows:categories` | map |
| 234 | g12 | `curly-arrows` | curly arrow | `def:g12:curly-arrows:curly-arrow` | map |
| 235 | g12 | `curly-arrows` | reaction mechanism | `def:g12:curly-arrows:mechanism` | map |
| 236 | g12 | `curly-arrows` | elementary step | `def:g12:curly-arrows:mechanism` | map |
| 237 | g12 | `curly-arrows` | reaction intermediate | `def:g12:curly-arrows:mechanism` | map |
| 238 | g12 | `curly-arrows` | electron-donor site | `def:g12:curly-arrows:site` | in-volume, not in map |
| 239 | g12 | `curly-arrows` | electron-acceptor site | `def:g12:curly-arrows:site` | in-volume, not in map |
| 240 | g12 | `reaction-rates` | first-order reaction | `def:g12:reaction-rates:first-order` | in-volume, not in map |
| 241 | g12 | `reaction-rates` | rate constant | `def:g12:reaction-rates:first-order` | in-volume, not in map |
| 242 | g12 | `reaction-rates` | half-life | `def:g12:reaction-rates:half-life` | map |
| 243 | g12 | `reaction-rates` | kinetic factor | `def:g12:reaction-rates:kinetic-factor` | map |
| 244 | g12 | `reaction-rates` | quenching | `def:g12:reaction-rates:quenching` | in-volume, not in map |
| 245 | g12 | `reaction-rates` | rate of disappearance | `def:g12:reaction-rates:rate` | map |
| 246 | g12 | `reaction-rates` | rate of appearance | `def:g12:reaction-rates:rate` | map |
| 247 | g12 | `catalysis` | catalyst | `def:g12:catalysis:catalyst` | map |
| 248 | g12 | `catalysis` | catalysis | `def:g12:catalysis:catalyst` | map |
| 249 | g12 | `catalysis` | enzyme | `def:g12:catalysis:enzyme` | in-volume, not in map |
| 250 | g12 | `catalysis` | homogeneous catalysis | `def:g12:catalysis:homogeneous` | map |
| 251 | g12 | `catalysis` | heterogeneous catalysis | `def:g12:catalysis:homogeneous` | map |
| 252 | g12 | `catalysis` | selective catalyst | `def:g12:catalysis:selective` | in-volume, not in map |
| 253 | g12 | `equilibrium` | equilibrium constant | `def:g12:equilibrium:constant` | map |
| 254 | g12 | `equilibrium` | equilibrium state | `def:g12:equilibrium:equilibrium-state` | in-volume, not in map |
| 255 | g12 | `equilibrium` | non-total reaction | `def:g12:equilibrium:non-total` | map |
| 256 | g12 | `equilibrium` | final extent ratio | `def:g12:equilibrium:non-total` | map |
| 257 | g12 | `equilibrium` | reaction quotient | `def:g12:equilibrium:quotient` | map |
| 258 | g12 | `ka-and-pka` | Brønsted acid | `def:g12:ka-and-pka:bronsted` | map |
| 259 | g12 | `ka-and-pka` | Brønsted base | `def:g12:ka-and-pka:bronsted` | map |
| 260 | g12 | `ka-and-pka` | acid–base couple | `def:g12:ka-and-pka:bronsted` | map |
| 261 | g12 | `ka-and-pka` | ionic product of water | `def:g12:ka-and-pka:ionic-product` | map |
| 262 | g12 | `ka-and-pka` | acidity constant | `def:g12:ka-and-pka:ka` | map |
| 263 | g12 | `ka-and-pka` | pKa | `def:g12:ka-and-pka:ka` | map |
| 264 | g12 | `ka-and-pka` | oxonium ion | `def:g12:ka-and-pka:oxonium` | in-volume, not in map |
| 265 | g12 | `ka-and-pka` | ampholyte | `def:g12:ka-and-pka:oxonium` | in-volume, not in map |
| 266 | g12 | `ka-and-pka` | strong acid | `def:g12:ka-and-pka:strong-acid` | in-volume, not in map |
| 267 | g12 | `ka-and-pka` | weak acid | `def:g12:ka-and-pka:strong-acid` | in-volume, not in map |
| 268 | g12 | `ka-and-pka` | strong base | `def:g12:ka-and-pka:strong-acid` | in-volume, not in map |
| 269 | g12 | `ka-and-pka` | weak base | `def:g12:ka-and-pka:strong-acid` | in-volume, not in map |
| 270 | g12 | `buffers-predominance` | buffer solution | `def:g12:buffers-predominance:buffer` | map |
| 271 | g12 | `buffers-predominance` | acid–base indicator | `def:g12:buffers-predominance:indicator` | C11 |
| 272 | g12 | `buffers-predominance` | colour-change range | `def:g12:buffers-predominance:indicator` | C11 |
| 273 | g12 | `buffers-predominance` | predominance diagram | `def:g12:buffers-predominance:predominance` | map |
| 274 | g12 | `buffers-predominance` | distribution diagram | `def:g12:buffers-predominance:predominance` | map |
| 275 | g12 | `ph-conductivity-titrations` | conductimetric titration | `def:g12:ph-conductivity-titrations:conductimetric` | map |
| 276 | g12 | `ph-conductivity-titrations` | conductivity | `def:g12:ph-conductivity-titrations:conductivity` | C13 |
| 277 | g12 | `ph-conductivity-titrations` | molar ionic conductivity | `def:g12:ph-conductivity-titrations:conductivity` | C13 |
| 278 | g12 | `ph-conductivity-titrations` | pH-metric titration | `def:g12:ph-conductivity-titrations:ph-metric` | in-volume, not in map |
| 279 | g12 | `ph-conductivity-titrations` | half-equivalence | `def:g12:ph-conductivity-titrations:ph-metric` | in-volume, not in map |
| 280 | g12 | `cells-and-electrolysis` | anode | `def:g12:cells-and-electrolysis:anode` | in-volume, not in map |
| 281 | g12 | `cells-and-electrolysis` | cathode | `def:g12:cells-and-electrolysis:anode` | in-volume, not in map |
| 282 | g12 | `cells-and-electrolysis` | capacity | `def:g12:cells-and-electrolysis:capacity` | in-volume, not in map |
| 283 | g12 | `cells-and-electrolysis` | Faraday constant | `def:g12:cells-and-electrolysis:capacity` | in-volume, not in map |
| 284 | g12 | `cells-and-electrolysis` | electrochemical cell | `def:g12:cells-and-electrolysis:cell` | map |
| 285 | g12 | `cells-and-electrolysis` | half-cell | `def:g12:cells-and-electrolysis:cell` | map |
| 286 | g12 | `cells-and-electrolysis` | salt bridge | `def:g12:cells-and-electrolysis:cell` | map |
| 287 | g12 | `cells-and-electrolysis` | electrolysis | `def:g12:cells-and-electrolysis:electrolysis` | map |
| 288 | g12 | `cells-and-electrolysis` | accumulator | `def:g12:cells-and-electrolysis:electrolysis` | map |
| 289 | g12 | `cells-and-electrolysis` | cell voltage | `def:g12:cells-and-electrolysis:emf` | in-volume, not in map |
| 290 | g12 | `synthesis-strategy` | atom economy | `def:g12:synthesis-strategy:atom-economy` | map |
| 291 | g12 | `synthesis-strategy` | chemoselective reaction | `def:g12:synthesis-strategy:chemoselective` | in-volume, not in map |
| 292 | g12 | `synthesis-strategy` | green chemistry | `def:g12:synthesis-strategy:green-chemistry` | map |
| 293 | g12 | `synthesis-strategy` | protecting group | `def:g12:synthesis-strategy:protecting-group` | map |
| 294 | g12 | `polymers` | addition polymer | `def:g12:polymers:addition-polymer` | in-volume, not in map |
| 295 | g12 | `polymers` | condensation polymer | `def:g12:polymers:addition-polymer` | in-volume, not in map |
| 296 | g12 | `polymers` | polymer | `def:g12:polymers:polymer` | map |
| 297 | g12 | `polymers` | monomer | `def:g12:polymers:polymer` | map |
| 298 | g12 | `polymers` | polymerisation | `def:g12:polymers:polymer` | map |
| 299 | g12 | `polymers` | repeat unit | `def:g12:polymers:repeat-unit` | map |
| 300 | g12 | `polymers` | degree of polymerisation | `def:g12:polymers:repeat-unit` | map |

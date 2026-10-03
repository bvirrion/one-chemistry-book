# Book 3 (University Year 2) — defined terms

One row per term the book will carry as `\emph{term}\index{term}` inside a
`definition` (label `def:b2:<chapter-slug>:<name>`), or — for the named laws
marked "pending ruling" — in the law's own theorem, following Book 2's
precedent (Nernst equation, Markovnikov's rule), unless the sync rules
otherwise (then a one-line definition names the law before the theorem).
Phase A plan, 2026-10-02; revise as chapters land.

Status: **map** — the outline's Years 1–3 table or a Sync S1 ruling gives the
term to this book; **new** — not in the map, first need in the series is here
(earliest-need rule); **re-found** — Book 1 owns it at school level, Book 2
did not define it, this book defines it again rigorously; **contested** —
another university book's outline chapter could claim it (report point 2);
**moved** — placed in a different chapter of this book than the seed row.
Checked against Book 2's real harvest (the perl command of
`SERIES_DEFINITIONS.md`, 2026-10-02) and Book 1's harvest (written grades):
no row below is owned by Book 2; the rows marked contested touch a notion
of Book 4's outline map and await the sync.

| ch | term | label | status |
|---|---|---|---|
| 1 | reaction quantity | `def:b2:reaction-enthalpy:reaction-quantity` | new |
| 1 | reaction enthalpy | `def:b2:reaction-enthalpy:reaction-quantity` | new |
| 1 | standard reaction quantity | `def:b2:reaction-enthalpy:standard-reaction-enthalpy` | new |
| 1 | standard reaction enthalpy | `def:b2:reaction-enthalpy:standard-reaction-enthalpy` | new |
| 1 | exothermic | `def:b2:reaction-enthalpy:exothermic` | re-found (g11 reaction-energy) |
| 1 | endothermic | `def:b2:reaction-enthalpy:exothermic` | re-found (g11 reaction-energy) |
| 1 | athermic | `def:b2:reaction-enthalpy:exothermic` | new |
| 1 | standard reference state | `def:b2:reaction-enthalpy:formation` | new |
| 1 | standard enthalpy of formation | `def:b2:reaction-enthalpy:formation` | map (S1: B3 ch1) |
| 1 | bond dissociation enthalpy | `def:b2:reaction-enthalpy:bond-enthalpy` | re-found (g11 bond energy) |
| 1 | mean bond enthalpy | `def:b2:reaction-enthalpy:bond-enthalpy` | re-found (g11 bond energy) |
| 1 | lattice enthalpy | `def:b2:reaction-enthalpy:lattice-enthalpy` | new — not in the map; earliest need |
| 1 | adiabatic flame temperature | `def:b2:reaction-enthalpy:flame-temperature` | new |
| 1 | Hess's law | `thm:b2:reaction-enthalpy:hess` | map; named law in its theorem (pending ruling) |
| 1 | Kirchhoff's law | `thm:b2:reaction-enthalpy:kirchhoff` | named law in its theorem (pending ruling) |
| 2 | standard molar entropy | `def:b2:reaction-free-energy:standard-entropy` | new |
| 2 | reaction entropy | `def:b2:reaction-free-energy:reaction-entropy` | map |
| 2 | standard reaction entropy | `def:b2:reaction-free-energy:reaction-entropy` | map |
| 2 | Gibbs energy | `def:b2:reaction-free-energy:gibbs-energy` | new |
| 2 | reaction Gibbs energy | `def:b2:reaction-free-energy:reaction-gibbs` | map |
| 2 | standard reaction Gibbs energy | `def:b2:reaction-free-energy:reaction-gibbs` | map |
| 2 | exergonic | `def:b2:reaction-free-energy:exergonic` | new |
| 2 | endergonic | `def:b2:reaction-free-energy:exergonic` | new |
| 2 | Ellingham approximation | `def:b2:reaction-free-energy:ellingham-approximation` | new — not in the map; ch6 recalls |
| 2 | inversion temperature | `def:b2:reaction-free-energy:inversion-temperature` | new |
| 2 | evolution criterion | `thm:b2:reaction-free-energy:evolution` | map; theorem title only, no \index unless ruled |
| 3 | partial molar quantity | `def:b2:chemical-potential:partial-molar` | map |
| 3 | partial molar volume | `def:b2:chemical-potential:partial-molar` | new |
| 3 | chemical potential | `def:b2:chemical-potential:chemical-potential` | map |
| 3 | standard chemical potential | `def:b2:chemical-potential:chemical-potential` | new |
| 3 | ideal mixture | `def:b2:chemical-potential:ideal-mixture` | new |
| 3 | ideal dilute solution | `def:b2:chemical-potential:ideal-mixture` | new |
| 3 | activity coefficient | `def:b2:chemical-potential:activity-coefficient` | new (Year 1 promised it) |
| 3 | ionic strength | `def:b2:chemical-potential:ionic-strength` | new — not in the map |
| 3 | colligative property | `def:b2:chemical-potential:colligative` | new |
| 3 | cryoscopic constant | `def:b2:chemical-potential:colligative` | new |
| 3 | ebullioscopic constant | `def:b2:chemical-potential:colligative` | new |
| 3 | semipermeable membrane | `def:b2:chemical-potential:osmotic-pressure` | new |
| 3 | osmotic pressure | `def:b2:chemical-potential:osmotic-pressure` | new |
| 3 | Raoult's law | `thm:b2:chemical-potential:raoult` | map; named law (pending ruling) |
| 3 | Henry's law | `prop:b2:chemical-potential:henry` | map; named law (pending ruling) |
| 3 | Henry constant | `prop:b2:chemical-potential:henry` | map |
| 4 | independent intensive parameter | `def:b2:equilibrium-shifts:variance` | new |
| 4 | variance | `def:b2:equilibrium-shifts:variance` | map |
| 4 | shift of an equilibrium | `def:b2:equilibrium-shifts:shift` | new (Year 1 left the shift language here) |
| 4 | Le Chatelier's principle | `def:b2:equilibrium-shifts:moderation` | new |
| 4 | single-pass conversion | `def:b2:equilibrium-shifts:single-pass` | new |
| 4 | recycle | `def:b2:equilibrium-shifts:single-pass` | new |
| 4 | purge | `def:b2:equilibrium-shifts:single-pass` | new |
| 4 | van 't Hoff equation | `thm:b2:equilibrium-shifts:vant-hoff` | map; named law (pending ruling) |
| 5 | batch reactor | `def:b2:continuous-reactors:reactors` | new |
| 5 | continuous reactor | `def:b2:continuous-reactors:reactors` | new |
| 5 | continuous stirred-tank reactor | `def:b2:continuous-reactors:reactors` | new |
| 5 | plug-flow reactor | `def:b2:continuous-reactors:reactors` | new |
| 5 | residence time | `def:b2:continuous-reactors:residence-time` | new |
| 5 | conversion | `def:b2:continuous-reactors:conversion` | new (distinct from Year 1's final fractional extent) |
| 5 | selectivity | `def:b2:continuous-reactors:selectivity` | new |
| 5 | adiabatic temperature rise | `def:b2:continuous-reactors:adiabatic-rise` | new |
| 5 | thermal runaway | `def:b2:continuous-reactors:runaway` | new |
| 6 | Ellingham diagram | `def:b2:ellingham:diagram` | new |
| 6 | equilibrium oxygen pressure | `def:b2:ellingham:oxygen-pressure` | new |
| 6 | Boudouard equilibrium | `def:b2:ellingham:boudouard` | new |
| 6 | pyrometallurgy | `def:b2:ellingham:metallurgy` | new |
| 6 | hydrometallurgy | `def:b2:ellingham:metallurgy` | new |
| 6 | roasting | `def:b2:ellingham:metallurgy` | new |
| 6 | leaching | `def:b2:ellingham:metallurgy` | new |
| 6 | cementation | `def:b2:ellingham:metallurgy` | new |
| 6 | aluminothermic reduction | `def:b2:ellingham:aluminothermy` | new |
| 7 | binary diagram | `def:b2:liquid-vapour-diagrams:binary-diagram` | new |
| 7 | isobaric diagram | `def:b2:liquid-vapour-diagrams:binary-diagram` | new |
| 7 | isothermal diagram | `def:b2:liquid-vapour-diagrams:binary-diagram` | new |
| 7 | bubble curve | `def:b2:liquid-vapour-diagrams:bubble-dew` | new |
| 7 | dew curve | `def:b2:liquid-vapour-diagrams:bubble-dew` | new |
| 7 | bubble point | `def:b2:liquid-vapour-diagrams:bubble-dew` | new |
| 7 | dew point | `def:b2:liquid-vapour-diagrams:bubble-dew` | new |
| 7 | azeotrope | `def:b2:liquid-vapour-diagrams:azeotrope` | new (Year 1's list points here) |
| 7 | positive azeotrope | `def:b2:liquid-vapour-diagrams:azeotrope` | new |
| 7 | negative azeotrope | `def:b2:liquid-vapour-diagrams:azeotrope` | new |
| 7 | fractional distillation | `def:b2:liquid-vapour-diagrams:fractional-distillation` | new (Year 1's list points here) |
| 7 | theoretical plate | `def:b2:liquid-vapour-diagrams:fractional-distillation` | new |
| 7 | reflux ratio | `def:b2:liquid-vapour-diagrams:fractional-distillation` | new |
| 7 | miscibility gap | `def:b2:liquid-vapour-diagrams:miscibility-gap` | new |
| 7 | heteroazeotrope | `def:b2:liquid-vapour-diagrams:miscibility-gap` | new |
| 7 | steam distillation | `def:b2:liquid-vapour-diagrams:steam-distillation` | new (distinct from Book 1 hydrodistillation) |
| 7 | lever rule | `thm:b2:liquid-vapour-diagrams:lever` | named law (pending ruling) |
| 8 | thermal analysis | `def:b2:solid-liquid-diagrams:cooling-curve` | new |
| 8 | cooling curve | `def:b2:solid-liquid-diagrams:cooling-curve` | new |
| 8 | liquidus | `def:b2:solid-liquid-diagrams:liquidus` | new |
| 8 | solidus | `def:b2:solid-liquid-diagrams:liquidus` | new |
| 8 | solid solution | `def:b2:solid-liquid-diagrams:solid-solution` | new |
| 8 | eutectic point | `def:b2:solid-liquid-diagrams:eutectic` | new |
| 8 | eutectic mixture | `def:b2:solid-liquid-diagrams:eutectic` | new |
| 8 | defined compound | `def:b2:solid-liquid-diagrams:defined-compound` | new |
| 8 | congruent melting | `def:b2:solid-liquid-diagrams:defined-compound` | new |
| 9 | Faraday constant | `def:b2:cell-thermodynamics:faraday` | re-found (g12 cells-and-electrolysis) |
| 9 | temperature coefficient | `def:b2:cell-thermodynamics:temperature-coefficient` | new |
| 9 | thermodynamic efficiency | `def:b2:cell-thermodynamics:efficiency` | new |
| 9 | concentration cell | `def:b2:cell-thermodynamics:concentration-cell` | map |
| 10 | current–potential curve | `def:b2:current-potential-curves:ie-curve` | map |
| 10 | anodic current | `def:b2:current-potential-curves:ie-curve` | new |
| 10 | cathodic current | `def:b2:current-potential-curves:ie-curve` | new |
| 10 | electroactive species | `def:b2:current-potential-curves:electroactive` | new |
| 10 | working electrode | `def:b2:current-potential-curves:set-up` | new |
| 10 | counter electrode | `def:b2:current-potential-curves:set-up` | new |
| 10 | overpotential | `def:b2:current-potential-curves:overpotential` | map |
| 10 | threshold potential | `def:b2:current-potential-curves:overpotential` | new |
| 10 | fast system | `def:b2:current-potential-curves:fast-slow` | map |
| 10 | slow system | `def:b2:current-potential-curves:fast-slow` | map |
| 10 | diffusion layer | `def:b2:current-potential-curves:limiting-current` | new |
| 10 | limiting current | `def:b2:current-potential-curves:limiting-current` | new |
| 10 | electroactivity window | `def:b2:current-potential-curves:window` | new |
| 10 | solvent wall | `def:b2:current-potential-curves:window` | new |
| 11 | mixed potential | `def:b2:batteries-electrolysis:mixed-potential` | moved here from ch12 (S1 gave it to ch12; earliest need in this book) |
| 11 | primary cell | `def:b2:batteries-electrolysis:battery` | new |
| 11 | accumulator | `def:b2:batteries-electrolysis:battery` | re-found (g12 cells-and-electrolysis) |
| 11 | specific energy | `def:b2:batteries-electrolysis:battery` | new |
| 11 | fuel cell | `def:b2:batteries-electrolysis:fuel-cell` | new |
| 11 | electrolysis | `def:b2:batteries-electrolysis:electrolysis` | re-found (g12 cells-and-electrolysis) |
| 11 | electrolyser | `def:b2:batteries-electrolysis:electrolysis` | new |
| 11 | faradaic efficiency | `def:b2:batteries-electrolysis:faradaic-efficiency` | new |
| 11 | specific energy consumption | `def:b2:batteries-electrolysis:faradaic-efficiency` | new |
| 12 | uniform corrosion | `def:b2:corrosion:uniform` | new |
| 12 | corrosion potential | `def:b2:corrosion:uniform` | new |
| 12 | corrosion current | `def:b2:corrosion:uniform` | new |
| 12 | differential corrosion | `def:b2:corrosion:differential` | S1: B3 ch12 |
| 12 | galvanic corrosion | `def:b2:corrosion:differential` | new |
| 12 | differential aeration | `def:b2:corrosion:differential` | new |
| 12 | passivation | `def:b2:corrosion:passivation` | S1: B3 ch12 (the phenomenon) |
| 12 | passive film | `def:b2:corrosion:passivation` | new |
| 12 | cathodic protection | `def:b2:corrosion:protection` | new |
| 12 | sacrificial anode | `def:b2:corrosion:protection` | new |
| 12 | impressed-current protection | `def:b2:corrosion:protection` | new |
| 13 | wavefunction | `def:b2:atomic-orbitals:wavefunction` | S1: B3 ch13 |
| 13 | probability density | `def:b2:atomic-orbitals:wavefunction` | new |
| 13 | radial part | `def:b2:atomic-orbitals:radial-angular` | S1: B3 ch13 |
| 13 | angular part | `def:b2:atomic-orbitals:radial-angular` | S1: B3 ch13 |
| 13 | radial distribution function | `def:b2:atomic-orbitals:radial-distribution` | S1: B3 ch13 |
| 13 | most probable radius | `def:b2:atomic-orbitals:radial-distribution` | new |
| 13 | nodal surface | `def:b2:atomic-orbitals:node` | S1: B3 ch13 |
| 13 | radial node | `def:b2:atomic-orbitals:node` | new |
| 13 | angular node | `def:b2:atomic-orbitals:node` | new |
| 13 | Slater's rules | `def:b2:atomic-orbitals:slater` | S1: B3 ch13 |
| 13 | orbital energy | `def:b2:atomic-orbitals:orbital-energy` | new |
| 13 | orbital radius | `def:b2:atomic-orbitals:orbital-energy` | new |
| 14 | molecular orbital | `def:b2:diatomic-mos:lcao` | map |
| 14 | LCAO | `def:b2:diatomic-mos:lcao` | map |
| 14 | overlap integral | `def:b2:diatomic-mos:integrals` | new |
| 14 | Coulomb integral | `def:b2:diatomic-mos:integrals` | new |
| 14 | resonance integral | `def:b2:diatomic-mos:integrals` | new |
| 14 | secular determinant | `def:b2:diatomic-mos:integrals` | new |
| 14 | bonding orbital | `def:b2:diatomic-mos:bonding` | map |
| 14 | antibonding orbital | `def:b2:diatomic-mos:bonding` | map |
| 14 | nonbonding orbital | `def:b2:diatomic-mos:bonding` | new |
| 14 | σ orbital | `def:b2:diatomic-mos:sigma-pi` | S1: B3 ch14 (MO sense) |
| 14 | π orbital | `def:b2:diatomic-mos:sigma-pi` | S1: B3 ch14 (MO sense) |
| 14 | bond order | `def:b2:diatomic-mos:bond-order` | map |
| 14 | paramagnetic | `def:b2:diatomic-mos:magnetism` | contested low (Book 4 ch18 magnetism); earliest need |
| 14 | diamagnetic | `def:b2:diatomic-mos:magnetism` | contested low (Book 4 ch18) |
| 15 | fragment | `def:b2:fragment-orbitals:fragment` | map |
| 15 | fragment orbital | `def:b2:fragment-orbitals:fragment` | map |
| 15 | symmetry-adapted combination | `def:b2:fragment-orbitals:symmetry-adapted` | map |
| 15 | photoelectron spectroscopy | `def:b2:fragment-orbitals:photoelectron` | new — not in the map |
| 15 | hyperconjugation | `def:b2:fragment-orbitals:hyperconjugation` | new (Year 1's list points here) |
| 16 | Hückel method | `def:b2:huckel:method` | map |
| 16 | π charge | `def:b2:huckel:indices` | new |
| 16 | π bond index | `def:b2:huckel:indices` | new |
| 16 | delocalisation energy | `def:b2:huckel:delocalisation` | map |
| 16 | aromatic | `def:b2:huckel:aromatic` | map (aromaticity rule) |
| 16 | antiaromatic | `def:b2:huckel:aromatic` | map |
| 16 | Hückel's rule | `thm:b2:huckel:huckel-rule` | map; named law (pending ruling) |
| 17 | HOMO | `def:b2:frontier-orbitals:frontier` | map |
| 17 | LUMO | `def:b2:frontier-orbitals:frontier` | map |
| 17 | frontier orbitals | `def:b2:frontier-orbitals:frontier` | map |
| 17 | charge control | `def:b2:frontier-orbitals:control` | new |
| 17 | orbital control | `def:b2:frontier-orbitals:control` | new |
| 17 | hard nucleophile | `def:b2:frontier-orbitals:hard-soft` | new |
| 17 | soft nucleophile | `def:b2:frontier-orbitals:hard-soft` | new |
| 17 | hard electrophile | `def:b2:frontier-orbitals:hard-soft` | new |
| 17 | soft electrophile | `def:b2:frontier-orbitals:hard-soft` | new |
| 17 | ambident nucleophile | `def:b2:frontier-orbitals:ambident` | new |
| 17 | concerted reaction | `def:b2:frontier-orbitals:concerted` | contested low (Book 4 ch26 pericyclic recalls it) |
| 17 | Diels–Alder reaction | `def:b2:frontier-orbitals:diels-alder` | map |
| 17 | diene | `def:b2:frontier-orbitals:diels-alder` | new |
| 17 | dienophile | `def:b2:frontier-orbitals:diels-alder` | new |
| 17 | endo adduct | `def:b2:frontier-orbitals:endo` | new |
| 17 | exo adduct | `def:b2:frontier-orbitals:endo` | new |
| 17 | endo rule | `def:b2:frontier-orbitals:endo` | new |
| 18 | transition element | `def:b2:coordination-complexes:transition-element` | new |
| 18 | d^n configuration | `def:b2:coordination-complexes:transition-element` | new |
| 18 | denticity | `def:b2:coordination-complexes:denticity` | map (S1) |
| 18 | monodentate ligand | `def:b2:coordination-complexes:denticity` | new |
| 18 | bidentate ligand | `def:b2:coordination-complexes:denticity` | new |
| 18 | bridging ligand | `def:b2:coordination-complexes:denticity` | new |
| 18 | ambidentate ligand | `def:b2:coordination-complexes:denticity` | new |
| 18 | coordination sphere | `def:b2:coordination-complexes:coordination-sphere` | new |
| 18 | fac isomer | `def:b2:coordination-complexes:isomers` | new |
| 18 | mer isomer | `def:b2:coordination-complexes:isomers` | new |
| 18 | linkage isomers | `def:b2:coordination-complexes:isomers` | new |
| 18 | ionisation isomers | `def:b2:coordination-complexes:isomers` | new |
| 18 | valence electron count | `def:b2:coordination-complexes:electron-count` | new |
| 18 | 18-electron rule | `def:b2:coordination-complexes:electron-count` | map (S1) |
| 18 | hapticity | `def:b2:coordination-complexes:hapticity` | contested low (Book 4 ch20 organometallic ligands); earliest need |
| 19 | crystal-field model | `def:b2:ligand-field:crystal-field` | new |
| 19 | crystal-field splitting | `def:b2:ligand-field:crystal-field` | new |
| 19 | high spin | `def:b2:ligand-field:spin` | map |
| 19 | low spin | `def:b2:ligand-field:spin` | map |
| 19 | pairing energy | `def:b2:ligand-field:spin` | new |
| 19 | crystal-field stabilisation energy | `def:b2:ligand-field:cfse` | new |
| 19 | d–d transition | `def:b2:ligand-field:d-d` | new |
| 19 | spectrochemical series | `def:b2:ligand-field:spectrochemical` | map |
| 19 | ligand field theory | `def:b2:ligand-field:ligand-field` | map |
| 19 | π-donor ligand | `def:b2:ligand-field:pi-ligands` | contested (Book 4 ch20 back-bonding) |
| 19 | π-acceptor ligand | `def:b2:ligand-field:pi-ligands` | contested (Book 4 ch20) |
| 19 | back-donation | `def:b2:ligand-field:pi-ligands` | contested (Book 4 ch20 back-bonding); earliest need |
| 20 | coordinatively unsaturated complex | `def:b2:catalytic-cycles:unsaturated` | new |
| 20 | vacant site | `def:b2:catalytic-cycles:unsaturated` | new |
| 20 | ligand exchange | `def:b2:catalytic-cycles:ligand-exchange` | contested low (Book 4 ch19 owns substitution mechanisms) |
| 20 | oxidative addition | `def:b2:catalytic-cycles:oxidative-addition` | map |
| 20 | reductive elimination | `def:b2:catalytic-cycles:oxidative-addition` | map |
| 20 | migratory insertion | `def:b2:catalytic-cycles:insertion` | map |
| 20 | β-hydride elimination | `def:b2:catalytic-cycles:insertion` | new |
| 20 | transmetalation | `def:b2:catalytic-cycles:transmetalation` | new |
| 20 | catalytic cycle | `def:b2:catalytic-cycles:cycle` | new |
| 20 | precatalyst | `def:b2:catalytic-cycles:cycle` | new |
| 20 | turnover number | `def:b2:catalytic-cycles:cycle` | new |
| 20 | turnover frequency | `def:b2:catalytic-cycles:cycle` | new |
| 21 | catalytic hydrogenation | `def:b2:alkene-redox:hydrogenation` | new |
| 21 | hydroboration | `def:b2:alkene-redox:hydroboration` | map |
| 21 | anti-Markovnikov orientation | `def:b2:alkene-redox:hydroboration` | new |
| 21 | epoxide | `def:b2:alkene-redox:epoxide` | new |
| 21 | epoxidation | `def:b2:alkene-redox:epoxide` | map |
| 21 | peroxy acid | `def:b2:alkene-redox:epoxide` | new |
| 21 | dihydroxylation | `def:b2:alkene-redox:dihydroxylation` | new |
| 21 | oxidative cleavage | `def:b2:alkene-redox:cleavage` | map |
| 21 | ozonolysis | `def:b2:alkene-redox:cleavage` | new |
| 22 | arene | `def:b2:aromatic-substitution:arene` | new |
| 22 | electrophilic aromatic substitution | `def:b2:aromatic-substitution:seAr` | new |
| 22 | Wheland intermediate | `def:b2:aromatic-substitution:seAr` | new |
| 22 | Friedel–Crafts alkylation | `def:b2:aromatic-substitution:friedel-crafts` | new |
| 22 | Friedel–Crafts acylation | `def:b2:aromatic-substitution:friedel-crafts` | new |
| 22 | acylium ion | `def:b2:aromatic-substitution:friedel-crafts` | new |
| 22 | activating group | `def:b2:aromatic-substitution:directing` | new |
| 22 | deactivating group | `def:b2:aromatic-substitution:directing` | new |
| 22 | ortho/para director | `def:b2:aromatic-substitution:directing` | new |
| 22 | meta director | `def:b2:aromatic-substitution:directing` | new |
| 23 | primary amine | `def:b2:amines:class` | new |
| 23 | secondary amine | `def:b2:amines:class` | new |
| 23 | tertiary amine | `def:b2:amines:class` | new |
| 23 | quaternary ammonium ion | `def:b2:amines:class` | new |
| 23 | nucleophilic addition | `def:b2:amines:nucleophilic-addition` | new — used undefined in Year 1; earliest definition |
| 23 | hemiaminal | `def:b2:amines:imine` | new |
| 23 | imine | `def:b2:amines:imine` | new (Year 1's list points here) |
| 23 | enamine | `def:b2:amines:imine` | new (Year 1's list points here) |
| 23 | reductive amination | `def:b2:amines:reductive-amination` | new |
| 23 | diazonium ion | `def:b2:amines:diazonium` | new |
| 23 | diazotisation | `def:b2:amines:diazonium` | new |
| 23 | Sandmeyer reaction | `def:b2:amines:diazonium` | new |
| 23 | azo coupling | `def:b2:amines:diazonium` | new |
| 23 | nitrile | `def:b2:amines:nitrile` | new |
| 24 | carboxylic acid derivative | `def:b2:acyl-substitution:derivative` | new |
| 24 | acyl group | `def:b2:acyl-substitution:derivative` | new |
| 24 | acyl chloride | `def:b2:acyl-substitution:derivative` | new |
| 24 | acid anhydride | `def:b2:acyl-substitution:derivative` | new |
| 24 | nucleophilic acyl substitution | `def:b2:acyl-substitution:nas` | new |
| 24 | tetrahedral intermediate | `def:b2:acyl-substitution:nas` | new |
| 24 | esterification | `def:b2:acyl-substitution:esterification` | new |
| 24 | saponification | `def:b2:acyl-substitution:saponification` | new |
| 24 | transesterification | `def:b2:acyl-substitution:transesterification` | new |
| 24 | lactone | `def:b2:acyl-substitution:lactone` | new |
| 24 | lactam | `def:b2:acyl-substitution:lactone` | new |
| 25 | tautomers | `def:b2:enolates-aldol:tautomerism` | new |
| 25 | keto–enol tautomerism | `def:b2:enolates-aldol:tautomerism` | new (Year 1's list points here) |
| 25 | enol | `def:b2:enolates-aldol:tautomerism` | new (Year 1's list points here) |
| 25 | α carbon | `def:b2:enolates-aldol:enolate` | new |
| 25 | α hydrogen | `def:b2:enolates-aldol:enolate` | new |
| 25 | enolate ion | `def:b2:enolates-aldol:enolate` | new |
| 25 | kinetic enolate | `def:b2:enolates-aldol:kinetic-enolate` | new |
| 25 | thermodynamic enolate | `def:b2:enolates-aldol:kinetic-enolate` | new |
| 25 | aldol addition | `def:b2:enolates-aldol:aldol` | new |
| 25 | aldol | `def:b2:enolates-aldol:aldol` | new |
| 25 | aldol condensation | `def:b2:enolates-aldol:aldol` | new |
| 25 | decarboxylation | `def:b2:enolates-aldol:decarboxylation` | new |
| 25 | malonic ester synthesis | `def:b2:enolates-aldol:decarboxylation` | new |
| 25 | Claisen condensation | `def:b2:enolates-aldol:claisen` | new |
| 25 | β-keto ester | `def:b2:enolates-aldol:claisen` | new |
| 25 | haloform reaction | `def:b2:enolates-aldol:haloform` | new |
| 26 | α,β-unsaturated carbonyl compound | `def:b2:conjugate-additions:enone` | new |
| 26 | 1,2-addition | `def:b2:conjugate-additions:addition-modes` | new |
| 26 | conjugate addition | `def:b2:conjugate-additions:addition-modes` | new |
| 26 | Michael addition | `def:b2:conjugate-additions:michael` | new |
| 26 | Michael donor | `def:b2:conjugate-additions:michael` | new |
| 26 | Michael acceptor | `def:b2:conjugate-additions:michael` | new |
| 26 | organocuprate | `def:b2:conjugate-additions:cuprate` | new |
| 26 | annulation | `def:b2:conjugate-additions:robinson` | new |
| 26 | Robinson annulation | `def:b2:conjugate-additions:robinson` | new |
| 27 | phosphonium salt | `def:b2:wittig:ylide` | new |
| 27 | phosphonium ylide | `def:b2:wittig:ylide` | new |
| 27 | stabilised ylide | `def:b2:wittig:ylide` | new |
| 27 | Wittig reaction | `def:b2:wittig:wittig` | new |
| 27 | oxaphosphetane | `def:b2:wittig:wittig` | new |
| 27 | phosphonate | `def:b2:wittig:hwe` | new |
| 27 | Horner–Wadsworth–Emmons reaction | `def:b2:wittig:hwe` | new |
| 28 | retrosynthetic analysis | `def:b2:retrosynthesis:analysis` | map |
| 28 | target molecule | `def:b2:retrosynthesis:analysis` | new |
| 28 | disconnection | `def:b2:retrosynthesis:disconnection` | map |
| 28 | synthon | `def:b2:retrosynthesis:disconnection` | map |
| 28 | synthetic equivalent | `def:b2:retrosynthesis:disconnection` | new |
| 28 | functional-group interconversion | `def:b2:retrosynthesis:fgi` | new |
| 28 | orthogonal protecting groups | `def:b2:retrosynthesis:orthogonal` | contested low (Book 4 ch30 protecting-group economy) |
| 29 | polymer | `def:b2:polymer-synthesis:polymer` | re-found (g12 polymers) |
| 29 | monomer | `def:b2:polymer-synthesis:polymer` | re-found (g12 polymers) |
| 29 | repeat unit | `def:b2:polymer-synthesis:polymer` | re-found (g12 polymers) |
| 29 | degree of polymerisation | `def:b2:polymer-synthesis:polymer` | re-found (g12 polymers) |
| 29 | number-average molar mass | `def:b2:polymer-synthesis:averages` | new |
| 29 | mass-average molar mass | `def:b2:polymer-synthesis:averages` | new |
| 29 | dispersity | `def:b2:polymer-synthesis:averages` | new |
| 29 | step-growth polymerisation | `def:b2:polymer-synthesis:step-chain` | map |
| 29 | chain-growth polymerisation | `def:b2:polymer-synthesis:step-chain` | map |
| 29 | initiation | `def:b2:polymer-synthesis:chain-steps` | contested (Book 4 ch13 chain reaction) |
| 29 | propagation | `def:b2:polymer-synthesis:chain-steps` | contested (Book 4 ch13) |
| 29 | termination | `def:b2:polymer-synthesis:chain-steps` | contested (Book 4 ch13) |
| 29 | radical initiator | `def:b2:polymer-synthesis:chain-steps` | new |
| 29 | kinetic chain length | `def:b2:polymer-synthesis:chain-length` | new |
| 29 | living polymerisation | `def:b2:polymer-synthesis:living` | new |
| 29 | copolymer | `def:b2:polymer-synthesis:copolymer` | new |
| 29 | tacticity | `def:b2:polymer-synthesis:tacticity` | map |
| 29 | isotactic | `def:b2:polymer-synthesis:tacticity` | map |
| 29 | syndiotactic | `def:b2:polymer-synthesis:tacticity` | map |
| 29 | atactic | `def:b2:polymer-synthesis:tacticity` | map |
| 29 | glass transition temperature | `def:b2:polymer-synthesis:transitions` | map |
| 29 | degree of crystallinity | `def:b2:polymer-synthesis:transitions` | new |
| 29 | elastomer | `def:b2:polymer-synthesis:elastomer` | new |
| 29 | Carothers equation | `thm:b2:polymer-synthesis:carothers` | named law (pending ruling) |
| 30 | α-amino acid | `def:b2:biomolecules:amino-acid` | new |
| 30 | side chain | `def:b2:biomolecules:amino-acid` | new |
| 30 | zwitterion | `def:b2:biomolecules:amino-acid` | new |
| 30 | isoelectric point | `def:b2:biomolecules:amino-acid` | new |
| 30 | peptide bond | `def:b2:biomolecules:peptide` | new |
| 30 | peptide | `def:b2:biomolecules:peptide` | new |
| 30 | peptide coupling | `def:b2:biomolecules:peptide` | new |
| 30 | coupling agent | `def:b2:biomolecules:peptide` | new |
| 30 | D/L descriptors | `def:b2:biomolecules:d-l` | new |
| 30 | monosaccharide | `def:b2:biomolecules:sugar` | new |
| 30 | aldose | `def:b2:biomolecules:sugar` | new |
| 30 | ketose | `def:b2:biomolecules:sugar` | new |
| 30 | Haworth projection | `def:b2:biomolecules:anomer` | new |
| 30 | anomeric carbon | `def:b2:biomolecules:anomer` | new |
| 30 | anomers | `def:b2:biomolecules:anomer` | new |
| 30 | mutarotation | `def:b2:biomolecules:anomer` | new |
| 30 | glycoside | `def:b2:biomolecules:glycoside` | new |
| 30 | glycosidic bond | `def:b2:biomolecules:glycoside` | new |
| 30 | reducing sugar | `def:b2:biomolecules:glycoside` | new |
| 30 | fatty acid | `def:b2:biomolecules:lipid` | new |
| 30 | triglyceride | `def:b2:biomolecules:lipid` | new |
| 30 | phospholipid | `def:b2:biomolecules:lipid` | new |
| 30 | nucleobase | `def:b2:biomolecules:nucleotide` | new |
| 30 | nucleoside | `def:b2:biomolecules:nucleotide` | new |
| 30 | nucleotide | `def:b2:biomolecules:nucleotide` | new |
| 30 | phosphodiester bond | `def:b2:biomolecules:nucleotide` | new |
| 31 | chromatography | `def:b2:chromatography:principle` | new |
| 31 | stationary phase | `def:b2:chromatography:principle` | re-found (g10 chemical-species) |
| 31 | mobile phase | `def:b2:chromatography:principle` | new |
| 31 | elution | `def:b2:chromatography:principle` | new |
| 31 | retention time | `def:b2:chromatography:retention` | new |
| 31 | hold-up time | `def:b2:chromatography:retention` | new |
| 31 | retention factor k | `def:b2:chromatography:retention` | contested homonym (Year 1 ch29 owns retention factor = TLC Rf); proposal: harvested as 'retention factor $k$' |
| 31 | plate number | `def:b2:chromatography:plates` | new |
| 31 | plate height | `def:b2:chromatography:plates` | new |
| 31 | selectivity factor | `def:b2:chromatography:separation` | new |
| 31 | resolution | `def:b2:chromatography:separation` | new |
| 31 | gas chromatography | `def:b2:chromatography:techniques` | new |
| 31 | high-performance liquid chromatography | `def:b2:chromatography:techniques` | new |
| 31 | reversed phase | `def:b2:chromatography:techniques` | new |
| 31 | gradient elution | `def:b2:chromatography:techniques` | new |
| 31 | response factor | `def:b2:chromatography:quantitative` | new |
| 31 | internal standard | `def:b2:chromatography:quantitative` | new |
| 32 | mass spectrometry | `def:b2:mass-spec-atomic:spectrum` | new |
| 32 | mass-to-charge ratio | `def:b2:mass-spec-atomic:spectrum` | new |
| 32 | mass spectrum | `def:b2:mass-spec-atomic:spectrum` | new |
| 32 | base peak | `def:b2:mass-spec-atomic:spectrum` | new |
| 32 | molecular ion | `def:b2:mass-spec-atomic:molecular-ion` | map |
| 32 | fragment ion | `def:b2:mass-spec-atomic:molecular-ion` | new |
| 32 | isotope pattern | `def:b2:mass-spec-atomic:isotope-pattern` | new |
| 32 | nitrogen rule | `def:b2:mass-spec-atomic:nitrogen-rule` | new |
| 32 | monoisotopic mass | `def:b2:mass-spec-atomic:exact-mass` | new |
| 32 | high-resolution mass spectrometry | `def:b2:mass-spec-atomic:exact-mass` | new |
| 32 | α-cleavage | `def:b2:mass-spec-atomic:fragmentation` | new |
| 32 | McLafferty rearrangement | `def:b2:mass-spec-atomic:fragmentation` | new |
| 32 | atomic emission spectrometry | `def:b2:mass-spec-atomic:atomic` | new |
| 32 | atomic absorption spectrometry | `def:b2:mass-spec-atomic:atomic` | new |
| 32 | hollow-cathode lamp | `def:b2:mass-spec-atomic:atomic` | new |
| 32 | inductively coupled plasma | `def:b2:mass-spec-atomic:atomic` | new |
| 33 | carbon-13 NMR | `def:b2:structure-determination:c13` | map |
| 33 | broadband decoupling | `def:b2:structure-determination:c13` | new |
| 33 | equivalent carbons | `def:b2:structure-determination:c13` | new |
| 33 | DEPT | `def:b2:structure-determination:dept` | map |
| 33 | quaternary carbon | `def:b2:structure-determination:dept` | new — Year 1 defined primary/secondary/tertiary only |
| 34 | experimental standard deviation | `def:b2:measurement-statistics:dispersion` | new |
| 34 | standard deviation of the mean | `def:b2:measurement-statistics:dispersion` | new |
| 34 | confidence interval | `def:b2:measurement-statistics:confidence` | new |
| 34 | confidence level | `def:b2:measurement-statistics:confidence` | new |
| 34 | Student's coefficient | `def:b2:measurement-statistics:confidence` | new |
| 34 | calibration curve | `def:b2:measurement-statistics:calibration` | re-found (g11 calibration line) |
| 34 | least-squares line | `def:b2:measurement-statistics:calibration` | new |
| 34 | residual | `def:b2:measurement-statistics:calibration` | new |
| 34 | standard-addition method | `def:b2:measurement-statistics:standard-addition` | new |
| 34 | limit of detection | `def:b2:measurement-statistics:limits` | new |
| 34 | limit of quantification | `def:b2:measurement-statistics:limits` | new |
| 34 | trueness | `def:b2:measurement-statistics:validation` | new |
| 34 | precision | `def:b2:measurement-statistics:validation` | new |
| 34 | bias | `def:b2:measurement-statistics:validation` | new |
| 34 | repeatability | `def:b2:measurement-statistics:validation` | new |
| 34 | reproducibility | `def:b2:measurement-statistics:validation` | new |
| 34 | method validation | `def:b2:measurement-statistics:validation` | new |
| 34 | law of propagation of uncertainty | `thm:b2:measurement-statistics:propagation` | named law (pending ruling) |
| 35 | inert atmosphere | `def:b2:lab-techniques-2:inert` | new |
| 35 | work-up | `def:b2:lab-techniques-2:work-up` | new |
| 35 | acid–base extraction | `def:b2:lab-techniques-2:acid-base-extraction` | new |
| 35 | drying agent | `def:b2:lab-techniques-2:drying-agent` | new |
| 35 | flash chromatography | `def:b2:lab-techniques-2:flash` | new |
| 35 | distillation under reduced pressure | `def:b2:lab-techniques-2:reduced-pressure` | new |

**421 terms.**

## Used but not defined (owner elsewhere)

| term | owner | how Book 3 uses it |
|---|---|---|
| standard state, activity, mole fraction, partial pressure, extent, yield, final fractional extent, $Q$, $K^\circ$, equilibrium state, quantitative reaction, phase, intensive/extensive variable | Year 1 (B2 ch7) | recall boxes in ch1–4; the chapters derive the Year-1 laws without redefining the words |
| rate law, order, half-life, Arrhenius law, elementary step, rate-determining step, steady-state approximation, catalyst, homogeneous catalysis, kinetic/thermodynamic control, transition state, Hammond postulate | Year 1 (B2 ch8–9) | ch5, ch17, ch20, ch25–26, ch29 |
| Brønsted acid/base, acidity constant, predominance and distribution diagrams, buffer, polyprotic acid | Year 1 (B2 ch10) | ch23, ch25, ch30, ch35 |
| complex, central atom, ligand, polydentate ligand, chelate, formation constants, coordination number | Year 1 (B2 ch5, ch12) | ch18–20 |
| oxidant, reductant, redox couple, half-equation, oxidation number, electrochemical cell, half-cell, salt bridge, anode, cathode, cell voltage, electrode potential, standard potential, reference electrode, Nernst equation, E–pH diagram, immunity/corrosion/passivation domains, disproportionation | Year 1 (B2 ch13–14) | ch9–12 (the Nernst equation is re-derived in ch9 without a new `\index`) |
| quantum numbers, atomic orbital (as a label), shell, subshell, configuration, screening, effective nuclear charge, unpaired electron, Pauli, Hund, Klechkowski | Year 1 (B2 ch1–2, S1) | ch13–15, ch18–19 |
| Lewis structure, formal charge, resonance structure/hybrid, σ bond, π bond, hybridisation, VSEPR, Lewis acid/base, dative bond, dipole moment | Year 1 (B2 ch3, S1) | ch14–19 |
| stereoisomers, chirality, enantiomers, diastereomers, meso, racemic mixture, CIP rules, Fischer projection, conformation, specific rotation, Biot's law | Year 1 (B2 ch16) | ch18, ch21, ch30, ch35 |
| conjugated system, chromophore, absorbance, chemical shift, coupling, multiplet, integration, $n+1$ rule, wavenumber, fingerprint region, degree of unsaturation | Year 1 (B2 ch17) | ch16, ch25, ch32–33 |
| inductive/mesomeric effects, donor/acceptor group, carbocation, carbanion, radical, carbon class, curly arrow, nucleophile, electrophile, leaving group, SN1/SN2, E1/E2, Zaitsev, regio-/stereo-/chemoselective, stereospecific, Grignard reagent, organometallic compound, polarity inversion, Williamson synthesis, sulfonate ester, acetal, hemiacetal, protecting group, oxidation level, hydride donor, electrophilic addition, Markovnikov's rule, halonium, syn/anti addition, hydration, acetylide | Year 1 (B2 ch18–25) | ch17, ch21–30 |
| hazard, risk, GHS terms, safety data sheet, measurement/standard/expanded/relative uncertainty, type A/B evaluation, normalised deviation, partition coefficient, recrystallisation, retention factor ($R_f$) | Year 1 (B2 ch29) | ch31, ch34, ch35 |
| first and second laws, internal energy, enthalpy, heat capacity, entropy, created entropy, Clapeyron relation, diffusion and Fick's law, the wavefunction as a probability amplitude | physics series | "from physics" in recall boxes (ch1–3, ch10, ch13, ch35) |
| Schrödinger equation (formal), model systems, term symbols, Slater determinants | Book 4 ch1–2 | hydrogen functions `\admitted`, "solved in the Year 3 volume" |
| point group, symmetry operation, symmetry element, character table, irreducible representation | Book 4 ch4–5 | ch15, ch19: symmetry in plain words, orbital names admitted |
| partition function, Boltzmann distribution | Book 4 ch10 | ch2 third-law pointer |
| transition-state theory, activated complex, Eyring equation, kinetic isotope effect | Book 4 ch12 | not used |
| chain reaction, Michaelis–Menten, enzyme kinetics | Book 4 ch13 | ch25 hook, ch29 (steps only, contested) |
| Butler–Volmer, Tafel, cyclic voltammetry, double layer | Book 4 ch15 | ch10 pointer |
| adsorption, physisorption, chemisorption | Book 4 ch16 | ch21 hydrogenation in plain words |
| micelle, surfactant | Book 4 ch17 (university); Book 1 g11 | ch24, ch30 named only |
| Jahn–Teller, Tanabe–Sugano, magnetic susceptibility, spin-only moment, trans effect, inner/outer sphere | Book 4 ch18–19 | ch19 pointer |
| Woodward–Hoffmann rules, pericyclic reaction, cycloaddition (as a class) | Book 4 ch26 | ch17 pointer |
| enantiomeric excess, asymmetric catalysis, organocatalysis | Book 4 ch28 | ch21, ch26, ch35 pointers |
| convergent/linear synthesis, total synthesis | Book 4 ch30 | ch28 plain words |
| E-factor, life-cycle assessment; atom economy | Book 4 ch31; Book 1 g12 | ch27–28 (atom economy recalled) |
| Schlenk line, glovebox, lab notebook, risk assessment | Book 4 ch33 | ch35 pointer |
| ore, corrosion, rust, galvanising, distillation, hydrodistillation, extraction, quenching, heating under reflux, eluent, chromatogram, TLC, thermoplastic, thermoset, isotope, abundance, amine, amide, ester, carboxylic acid, enzyme | Book 1 | used as known (recall where needed) |

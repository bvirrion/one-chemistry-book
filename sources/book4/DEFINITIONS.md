# Book 4 (University Year 3) — defined terms

One row per term the book will carry as `\emph{term}\index{term}` inside a
`definition` (label `def:b3:<chapter-slug>:<name>`), or, for a named law,
in the theorem or proposition that states it (`thm:`/`prop:`/`cor:` rows;
Sync S2 point 2). Phase A plan, 2026-10-02; revise as chapters land (a term
may be demoted to a plain word in Phase B if it proves unnecessary — never
promoted to a term another book owns).

Status: **map** — the outline's Years 1–3 table, the seed rows of
`SERIES_DEFINITIONS.md` or a sync ruling gives the term to Book 4; **new** —
in no map and in no harvest, first need in the series is here (earliest-need
rule; Book 4 is the last volume, so no later book can claim it);
**re-found** — Book 1 owns it at school level, Books 2–3 did not define it;
**contested low** — another book's outline chapter or map touches the same
family of terms (reason given; report point 2); **phrase only** — a
homograph kept apart by defining only the longer phrase.

Checked by script on 2026-10-02 against: Book 2's real harvest (perl command
of `SERIES_DEFINITIONS.md`), Book 1's real harvest (all grades), and Book 3's
frozen map (`sources/book3/DEFINITIONS.md`, Sync S2). **No row below is owned
by Book 2 or Book 3** (the check's output is in `PROGRESS.md`).

| ch | term | label | status |
|---|---|---|---|
| 1 | operator | `def:b3:quantum-model-systems:operator` | new; contested low (Book 3 ch16 uses matrix eigenvalues without defining them) |
| 1 | eigenfunction | `def:b3:quantum-model-systems:operator` | new; contested low (as above) |
| 1 | eigenvalue | `def:b3:quantum-model-systems:operator` | new; contested low (as above) |
| 1 | Hermitian operator | `def:b3:quantum-model-systems:hermitian` | new |
| 1 | expectation value | `def:b3:quantum-model-systems:hermitian` | new |
| 1 | commutator | `def:b3:quantum-model-systems:commutator` | new |
| 1 | Hamiltonian operator | `def:b3:quantum-model-systems:schrodinger` | new |
| 1 | Schrödinger equation | `thm:b3:quantum-model-systems:schrodinger` | map |
| 1 | degenerate levels | `def:b3:quantum-model-systems:degenerate` | new; contested low (as above) |
| 1 | degeneracy | `def:b3:quantum-model-systems:degenerate` | new; contested low (Book 3 ch14 may say "degenerate orbitals" without a definition) |
| 1 | particle in a box | `def:b3:quantum-model-systems:box` | new |
| 1 | free-electron model | `def:b3:quantum-model-systems:box` | new |
| 1 | harmonic oscillator | `def:b3:quantum-model-systems:oscillator` | new |
| 1 | force constant | `def:b3:quantum-model-systems:oscillator` | new |
| 1 | reduced mass | `def:b3:quantum-model-systems:oscillator` | new; contested low (physics uses it; no chemistry book defines it) |
| 1 | zero-point energy | `def:b3:quantum-model-systems:oscillator` | new |
| 1 | ladder operators | `def:b3:quantum-model-systems:ladder` | new |
| 1 | rigid rotor | `def:b3:quantum-model-systems:rotor` | new |
| 1 | spherical harmonics | `def:b3:quantum-model-systems:rotor` | new |
| 1 | tunnelling | `def:b3:quantum-model-systems:tunnelling` | new |
| 1 | transmission probability | `def:b3:quantum-model-systems:tunnelling` | new |
| 2 | spin-orbital | `def:b3:many-electron-atoms:spin-orbital` | new |
| 2 | indistinguishable particles | `def:b3:many-electron-atoms:indistinguishable` | new |
| 2 | antisymmetric wavefunction | `def:b3:many-electron-atoms:indistinguishable` | new |
| 2 | Slater determinant | `def:b3:many-electron-atoms:slater` | new |
| 2 | exchange integral | `def:b3:many-electron-atoms:exchange` | new |
| 2 | singlet state | `def:b3:many-electron-atoms:singlet-triplet` | new |
| 2 | triplet state | `def:b3:many-electron-atoms:singlet-triplet` | new |
| 2 | Russell–Saunders coupling | `def:b3:many-electron-atoms:russell-saunders` | new |
| 2 | total orbital angular momentum quantum number | `def:b3:many-electron-atoms:russell-saunders` | new |
| 2 | total spin quantum number | `def:b3:many-electron-atoms:russell-saunders` | new |
| 2 | total angular momentum quantum number | `def:b3:many-electron-atoms:russell-saunders` | new |
| 2 | spectroscopic term | `def:b3:many-electron-atoms:term` | new; never bare "term" |
| 2 | spin multiplicity | `def:b3:many-electron-atoms:term` | new; phrase kept apart from Book 2 multiplicity (of a cell) |
| 2 | term symbol | `def:b3:many-electron-atoms:term` | new |
| 2 | spin–orbit coupling | `def:b3:many-electron-atoms:spin-orbit` | new |
| 2 | fine structure | `def:b3:many-electron-atoms:spin-orbit` | new |
| 3 | Born–Oppenheimer approximation | `def:b3:computational-chemistry:born-oppenheimer` | new |
| 3 | potential energy surface | `def:b3:computational-chemistry:pes` | new; placed in ch3 (earliest need in this book; ch12 recalls) |
| 3 | stationary point | `def:b3:computational-chemistry:pes` | new |
| 3 | equilibrium geometry | `def:b3:computational-chemistry:pes` | new |
| 3 | geometry optimisation | `def:b3:computational-chemistry:pes` | new |
| 3 | basis set | `def:b3:computational-chemistry:basis` | new |
| 3 | minimal basis set | `def:b3:computational-chemistry:basis` | new |
| 3 | Slater-type orbital | `def:b3:computational-chemistry:basis` | new |
| 3 | Gaussian-type orbital | `def:b3:computational-chemistry:basis` | new |
| 3 | contracted Gaussian function | `def:b3:computational-chemistry:basis` | new |
| 3 | split-valence basis set | `def:b3:computational-chemistry:split-valence` | new |
| 3 | polarisation function | `def:b3:computational-chemistry:split-valence` | new |
| 3 | diffuse function | `def:b3:computational-chemistry:split-valence` | new |
| 3 | Hartree–Fock method | `def:b3:computational-chemistry:hartree-fock` | new |
| 3 | Fock operator | `def:b3:computational-chemistry:hartree-fock` | new |
| 3 | self-consistent field | `def:b3:computational-chemistry:hartree-fock` | new |
| 3 | electron correlation | `def:b3:computational-chemistry:correlation` | new |
| 3 | correlation energy | `def:b3:computational-chemistry:correlation` | new |
| 3 | electron density | `def:b3:computational-chemistry:dft` | new |
| 3 | density-functional theory | `def:b3:computational-chemistry:dft` | new |
| 3 | exchange–correlation functional | `def:b3:computational-chemistry:dft` | new |
| 3 | Kohn–Sham orbitals | `def:b3:computational-chemistry:dft` | new |
| 3 | variational principle | `thm:b3:computational-chemistry:variational` | new |
| 3 | Koopmans' theorem | `thm:b3:computational-chemistry:koopmans` | new |
| 4 | symmetry operation | `def:b3:point-groups:operation` | map |
| 4 | symmetry element | `def:b3:point-groups:operation` | new |
| 4 | proper rotation axis | `def:b3:point-groups:rotation` | new |
| 4 | principal axis | `def:b3:point-groups:rotation` | new |
| 4 | mirror plane | `def:b3:point-groups:mirror` | new |
| 4 | vertical mirror plane | `def:b3:point-groups:mirror` | new |
| 4 | horizontal mirror plane | `def:b3:point-groups:mirror` | new |
| 4 | dihedral mirror plane | `def:b3:point-groups:mirror` | new |
| 4 | centre of inversion | `def:b3:point-groups:inversion` | new |
| 4 | improper rotation axis | `def:b3:point-groups:improper` | new |
| 4 | point group | `def:b3:point-groups:point-group` | map |
| 4 | order of a point group | `def:b3:point-groups:point-group` | new; phrase only (kinetic order is Book 2) |
| 4 | class of symmetry operations | `def:b3:point-groups:class` | new; phrase only (Book 1/2 carbon class) |
| 4 | subgroup | `def:b3:point-groups:class` | new |
| 4 | Schoenflies symbol | `def:b3:point-groups:schoenflies` | new |
| 4 | matrix representation | `def:b3:point-groups:representation` | new |
| 4 | character | `def:b3:point-groups:representation` | new |
| 4 | irreducible representation | `def:b3:point-groups:irrep` | new |
| 4 | character table | `def:b3:point-groups:irrep` | map |
| 4 | Mulliken symbol | `def:b3:point-groups:irrep` | new |
| 5 | reducible representation | `def:b3:group-theory-applied:reducible` | new |
| 5 | totally symmetric representation | `def:b3:group-theory-applied:reducible` | new |
| 5 | direct product | `def:b3:group-theory-applied:direct-product` | new |
| 5 | projection operator | `def:b3:group-theory-applied:projection` | new |
| 5 | normal mode | `def:b3:group-theory-applied:normal-mode` | new |
| 5 | IR active | `def:b3:group-theory-applied:activity` | new |
| 5 | Raman active | `def:b3:group-theory-applied:activity` | new |
| 5 | reduction formula | `thm:b3:group-theory-applied:reduction` | new; phrase only (redox reduction elsewhere) |
| 5 | mutual exclusion rule | `prop:b3:group-theory-applied:mutual-exclusion` | new |
| 6 | rotational constant | `def:b3:rovibrational-spectroscopy:rotational-constant` | new |
| 6 | isotopologue | `def:b3:rovibrational-spectroscopy:rotational-constant` | new |
| 6 | gross selection rule | `def:b3:rovibrational-spectroscopy:selection` | new |
| 6 | specific selection rule | `def:b3:rovibrational-spectroscopy:selection` | new |
| 6 | centrifugal distortion constant | `def:b3:rovibrational-spectroscopy:centrifugal` | new |
| 6 | anharmonicity constant | `def:b3:rovibrational-spectroscopy:anharmonic` | new |
| 6 | fundamental transition | `def:b3:rovibrational-spectroscopy:anharmonic` | new |
| 6 | overtone | `def:b3:rovibrational-spectroscopy:anharmonic` | new |
| 6 | hot band | `def:b3:rovibrational-spectroscopy:anharmonic` | new |
| 6 | Morse potential | `def:b3:rovibrational-spectroscopy:morse` | new |
| 6 | spectroscopic dissociation energy | `def:b3:rovibrational-spectroscopy:dissociation` | new; contested low (Book 3 owns bond dissociation enthalpy, a different quantity) |
| 6 | P branch | `def:b3:rovibrational-spectroscopy:branches` | new |
| 6 | Q branch | `def:b3:rovibrational-spectroscopy:branches` | new |
| 6 | R branch | `def:b3:rovibrational-spectroscopy:branches` | new |
| 6 | band origin | `def:b3:rovibrational-spectroscopy:branches` | new |
| 6 | Raman scattering | `def:b3:rovibrational-spectroscopy:raman` | new |
| 6 | Rayleigh scattering | `def:b3:rovibrational-spectroscopy:raman` | new |
| 6 | Stokes line | `def:b3:rovibrational-spectroscopy:raman` | new |
| 6 | anti-Stokes line | `def:b3:rovibrational-spectroscopy:raman` | new |
| 6 | symmetric top | `def:b3:rovibrational-spectroscopy:rotor-types` | new |
| 6 | asymmetric top | `def:b3:rovibrational-spectroscopy:rotor-types` | new |
| 6 | spherical top | `def:b3:rovibrational-spectroscopy:rotor-types` | new |
| 7 | transition dipole moment | `def:b3:electronic-spectroscopy:transition-dipole` | new |
| 7 | oscillator strength | `def:b3:electronic-spectroscopy:transition-dipole` | new |
| 7 | vibronic transition | `def:b3:electronic-spectroscopy:vibronic` | new |
| 7 | vibronic progression | `def:b3:electronic-spectroscopy:vibronic` | new |
| 7 | Franck–Condon factor | `def:b3:electronic-spectroscopy:vibronic` | new |
| 7 | charge-transfer transition | `def:b3:electronic-spectroscopy:charge-transfer` | new |
| 7 | Jablonski diagram | `def:b3:electronic-spectroscopy:jablonski` | new |
| 7 | vibrational relaxation | `def:b3:electronic-spectroscopy:radiationless` | new |
| 7 | internal conversion | `def:b3:electronic-spectroscopy:radiationless` | new |
| 7 | intersystem crossing | `def:b3:electronic-spectroscopy:radiationless` | new |
| 7 | luminescence | `def:b3:electronic-spectroscopy:luminescence` | new |
| 7 | fluorescence | `def:b3:electronic-spectroscopy:luminescence` | new |
| 7 | phosphorescence | `def:b3:electronic-spectroscopy:luminescence` | new |
| 7 | Stokes shift | `def:b3:electronic-spectroscopy:luminescence` | new |
| 7 | excited-state lifetime | `def:b3:electronic-spectroscopy:lifetime` | new |
| 7 | radiative lifetime | `def:b3:electronic-spectroscopy:lifetime` | new |
| 7 | quantum yield | `def:b3:electronic-spectroscopy:quantum-yield` | new; ch7 owns it, ch14 recalls |
| 7 | fluorescence quantum yield | `def:b3:electronic-spectroscopy:quantum-yield` | new |
| 7 | fluorescence quencher | `def:b3:electronic-spectroscopy:quencher` | new; phrase only (Book 1 quenching, kinetic sense) |
| 7 | dynamic quenching | `def:b3:electronic-spectroscopy:quencher` | new |
| 7 | static quenching | `def:b3:electronic-spectroscopy:quencher` | new |
| 7 | Franck–Condon principle | `thm:b3:electronic-spectroscopy:franck-condon` | new |
| 7 | Laporte rule | `thm:b3:electronic-spectroscopy:laporte` | new |
| 7 | Kasha's rule | `prop:b3:electronic-spectroscopy:kasha` | new |
| 7 | Stern–Volmer equation | `thm:b3:electronic-spectroscopy:stern-volmer` | new |
| 8 | nuclear spin quantum number | `def:b3:advanced-nmr:nuclear-spin` | new |
| 8 | gyromagnetic ratio | `def:b3:advanced-nmr:nuclear-spin` | new |
| 8 | Larmor frequency | `def:b3:advanced-nmr:larmor` | new |
| 8 | net magnetisation | `def:b3:advanced-nmr:magnetisation` | new |
| 8 | rotating frame | `def:b3:advanced-nmr:magnetisation` | new |
| 8 | radiofrequency pulse | `def:b3:advanced-nmr:pulse` | new |
| 8 | flip angle | `def:b3:advanced-nmr:pulse` | new |
| 8 | free induction decay | `def:b3:advanced-nmr:fid` | new |
| 8 | longitudinal relaxation time | `def:b3:advanced-nmr:relaxation` | new; phrase kept apart from ch13 chemical relaxation time |
| 8 | transverse relaxation time | `def:b3:advanced-nmr:relaxation` | new; as above |
| 8 | spin echo | `def:b3:advanced-nmr:echo` | new |
| 8 | nuclear Overhauser effect | `def:b3:advanced-nmr:noe` | new |
| 8 | two-dimensional spectrum | `def:b3:advanced-nmr:two-d` | new |
| 8 | cross peak | `def:b3:advanced-nmr:two-d` | new |
| 8 | diagonal peak | `def:b3:advanced-nmr:two-d` | new |
| 8 | COSY | `def:b3:advanced-nmr:cosy` | new |
| 8 | HSQC | `def:b3:advanced-nmr:hsqc` | new |
| 8 | HMBC | `def:b3:advanced-nmr:hmbc` | new |
| 8 | NOESY | `def:b3:advanced-nmr:noesy` | new |
| 8 | coalescence temperature | `def:b3:advanced-nmr:coalescence` | new |
| 9 | crystal system | `def:b3:x-ray-diffraction:crystal-system` | new |
| 9 | Bravais lattice | `def:b3:x-ray-diffraction:crystal-system` | new |
| 9 | lattice centring | `def:b3:x-ray-diffraction:crystal-system` | new |
| 9 | lattice plane | `def:b3:x-ray-diffraction:miller` | new |
| 9 | Miller indices | `def:b3:x-ray-diffraction:miller` | new |
| 9 | interplanar spacing | `def:b3:x-ray-diffraction:miller` | new |
| 9 | reciprocal lattice | `def:b3:x-ray-diffraction:reciprocal` | map |
| 9 | Ewald sphere | `def:b3:x-ray-diffraction:ewald` | new |
| 9 | atomic scattering factor | `def:b3:x-ray-diffraction:structure-factor` | new |
| 9 | structure factor | `def:b3:x-ray-diffraction:structure-factor` | new |
| 9 | systematic absence | `def:b3:x-ray-diffraction:absence` | new |
| 9 | screw axis | `def:b3:x-ray-diffraction:space-group` | new |
| 9 | glide plane | `def:b3:x-ray-diffraction:space-group` | new |
| 9 | space group | `def:b3:x-ray-diffraction:space-group` | map |
| 9 | asymmetric unit | `def:b3:x-ray-diffraction:space-group` | new |
| 9 | Wyckoff position | `def:b3:x-ray-diffraction:space-group` | new |
| 9 | powder diffraction pattern | `def:b3:x-ray-diffraction:powder` | new |
| 9 | phase problem | `def:b3:x-ray-diffraction:refinement` | new |
| 9 | R factor | `def:b3:x-ray-diffraction:refinement` | new |
| 9 | Bragg's law | `thm:b3:x-ray-diffraction:bragg` | map |
| 10 | microstate | `def:b3:partition-functions:microstate` | new |
| 10 | statistical weight | `def:b3:partition-functions:microstate` | new |
| 10 | Boltzmann distribution | `def:b3:partition-functions:boltzmann` | map |
| 10 | population | `def:b3:partition-functions:boltzmann` | new; homograph risk (ordinary word; STOP outside ch10 if needed) |
| 10 | molecular partition function | `def:b3:partition-functions:partition-function` | map |
| 10 | canonical partition function | `def:b3:partition-functions:canonical` | new |
| 10 | thermal wavelength | `def:b3:partition-functions:thermal-wavelength` | new |
| 10 | symmetry number | `def:b3:partition-functions:symmetry-number` | new |
| 10 | characteristic rotational temperature | `def:b3:partition-functions:characteristic-temperature` | new |
| 10 | characteristic vibrational temperature | `def:b3:partition-functions:characteristic-temperature` | new |
| 10 | statistical entropy | `def:b3:partition-functions:statistical-entropy` | new |
| 10 | Sackur–Tetrode equation | `thm:b3:partition-functions:sackur-tetrode` | new |
| 11 | ortho hydrogen | `def:b3:statistical-thermo-applied:spin-isomers` | new |
| 11 | para hydrogen | `def:b3:statistical-thermo-applied:spin-isomers` | new |
| 11 | residual entropy | `def:b3:statistical-thermo-applied:residual-entropy` | new |
| 11 | equilibrium isotope effect | `def:b3:statistical-thermo-applied:isotope-effect` | new |
| 11 | fractionation factor | `def:b3:statistical-thermo-applied:isotope-effect` | new |
| 11 | δ value | `def:b3:statistical-thermo-applied:isotope-effect` | new |
| 11 | equipartition theorem (named statement, indexed in its owning theorem, S2 point 2) | `thm:b3:statistical-thermo-applied:equipartition` | new |
| 12 | collision cross-section | `def:b3:rate-theories:collision` | new |
| 12 | steric factor | `def:b3:rate-theories:collision` | new |
| 12 | saddle point | `def:b3:rate-theories:saddle` | new |
| 12 | minimum energy path | `def:b3:rate-theories:saddle` | new |
| 12 | activated complex | `def:b3:rate-theories:activated-complex` | map |
| 12 | transition-state theory | `def:b3:rate-theories:tst` | map |
| 12 | transmission coefficient | `def:b3:rate-theories:tst` | new; homograph kept apart from ch1 transmission probability |
| 12 | Gibbs energy of activation | `def:b3:rate-theories:activation` | new |
| 12 | enthalpy of activation | `def:b3:rate-theories:activation` | new |
| 12 | entropy of activation | `def:b3:rate-theories:activation` | new |
| 12 | kinetic isotope effect | `def:b3:rate-theories:kie` | new |
| 12 | primary kinetic isotope effect | `def:b3:rate-theories:kie` | new |
| 12 | secondary kinetic isotope effect | `def:b3:rate-theories:kie` | new |
| 12 | diffusion- controlled reaction | `def:b3:rate-theories:diffusion` | new |
| 12 | activation-controlled reaction | `def:b3:rate-theories:diffusion` | new |
| 12 | cage effect | `def:b3:rate-theories:diffusion` | new |
| 12 | kinetic salt effect | `def:b3:rate-theories:salt` | new |
| 12 | Eyring equation | `thm:b3:rate-theories:eyring` | map |
| 13 | chain reaction | `def:b3:complex-kinetics:chain` | map |
| 13 | chain carrier | `def:b3:complex-kinetics:chain` | new |
| 13 | chain branching | `def:b3:complex-kinetics:branching` | map |
| 13 | explosion limits | `def:b3:complex-kinetics:branching` | map |
| 13 | Lindemann mechanism | `def:b3:complex-kinetics:lindemann` | new |
| 13 | fall-off region | `def:b3:complex-kinetics:lindemann` | new |
| 13 | enzyme | `def:b3:complex-kinetics:enzyme` | re-found (Book 1 g12 catalysis); Books 2–3 do not define it |
| 13 | active site | `def:b3:complex-kinetics:enzyme` | new |
| 13 | enzyme–substrate complex | `def:b3:complex-kinetics:enzyme` | new |
| 13 | Michaelis constant | `def:b3:complex-kinetics:michaelis` | new |
| 13 | maximum rate | `def:b3:complex-kinetics:michaelis` | new |
| 13 | catalytic constant | `def:b3:complex-kinetics:michaelis` | new; Book 3 owns turnover number/frequency of a catalyst |
| 13 | specificity constant | `def:b3:complex-kinetics:michaelis` | new |
| 13 | competitive inhibition | `def:b3:complex-kinetics:inhibition` | new |
| 13 | uncompetitive inhibition | `def:b3:complex-kinetics:inhibition` | new |
| 13 | mixed inhibition | `def:b3:complex-kinetics:inhibition` | new |
| 13 | inhibition constant | `def:b3:complex-kinetics:inhibition` | new |
| 13 | autocatalytic reaction | `def:b3:complex-kinetics:autocatalysis` | new |
| 13 | oscillating reaction | `def:b3:complex-kinetics:oscillating` | new |
| 13 | limit cycle | `def:b3:complex-kinetics:oscillating` | new |
| 13 | relaxation method | `def:b3:complex-kinetics:relaxation` | new |
| 13 | chemical relaxation time | `def:b3:complex-kinetics:relaxation` | new; phrase kept apart from the NMR relaxation times |
| 13 | stopped-flow method | `def:b3:complex-kinetics:fast` | new |
| 13 | flash photolysis | `def:b3:complex-kinetics:fast` | new |
| 13 | Michaelis–Menten equation | `thm:b3:complex-kinetics:michaelis-menten` | map |
| 14 | photon flux | `def:b3:photochemistry:photon-flux` | new |
| 14 | chemical actinometer | `def:b3:photochemistry:photon-flux` | new |
| 14 | photoisomerisation | `def:b3:photochemistry:photoisomerisation` | new |
| 14 | photostationary state | `def:b3:photochemistry:photoisomerisation` | new |
| 14 | photolysis | `def:b3:photochemistry:photolysis` | new |
| 14 | photolysis rate constant | `def:b3:photochemistry:photolysis` | new |
| 14 | Norrish type I reaction | `def:b3:photochemistry:norrish` | new |
| 14 | Norrish type II reaction | `def:b3:photochemistry:norrish` | new |
| 14 | photosensitiser | `def:b3:photochemistry:sensitisation` | new |
| 14 | photosensitisation | `def:b3:photochemistry:sensitisation` | new |
| 14 | triplet energy transfer | `def:b3:photochemistry:sensitisation` | new |
| 14 | singlet oxygen | `def:b3:photochemistry:sensitisation` | new |
| 14 | photoredox catalysis | `def:b3:photochemistry:photoredox` | new |
| 14 | Chapman mechanism | `def:b3:photochemistry:chapman` | new |
| 14 | ozone layer | `def:b3:photochemistry:chapman` | new |
| 14 | ozone depletion | `def:b3:photochemistry:ozone-depletion` | new |
| 14 | reservoir species | `def:b3:photochemistry:ozone-depletion` | new |
| 14 | photochemical smog | `def:b3:photochemistry:smog` | new |
| 14 | Stark–Einstein law | `prop:b3:photochemistry:stark-einstein` | new |
| 15 | electrical double layer | `def:b3:electrode-kinetics:double-layer` | new |
| 15 | Helmholtz layer | `def:b3:electrode-kinetics:double-layer` | new |
| 15 | diffuse layer | `def:b3:electrode-kinetics:double-layer` | new |
| 15 | Debye length | `def:b3:electrode-kinetics:double-layer` | new; ch15 owns it, ch17 recalls |
| 15 | double-layer capacitance | `def:b3:electrode-kinetics:double-layer` | new |
| 15 | exchange current density | `def:b3:electrode-kinetics:exchange` | new |
| 15 | transfer coefficient | `def:b3:electrode-kinetics:exchange` | new |
| 15 | standard rate constant | `def:b3:electrode-kinetics:exchange` | new |
| 15 | charge-transfer resistance | `def:b3:electrode-kinetics:charge-transfer` | new |
| 15 | Tafel slope | `def:b3:electrode-kinetics:charge-transfer` | new |
| 15 | migration | `def:b3:electrode-kinetics:transport` | new |
| 15 | convection | `def:b3:electrode-kinetics:transport` | new |
| 15 | supporting electrolyte | `def:b3:electrode-kinetics:transport` | new |
| 15 | chronoamperometry | `def:b3:electrode-kinetics:chronoamperometry` | new |
| 15 | cyclic voltammetry | `def:b3:electrode-kinetics:cv` | map |
| 15 | voltammogram | `def:b3:electrode-kinetics:cv` | new |
| 15 | peak potential | `def:b3:electrode-kinetics:cv` | new |
| 15 | peak current | `def:b3:electrode-kinetics:cv` | new |
| 15 | electrochemically reversible system | `def:b3:electrode-kinetics:reversibility` | new; contested low (Book 3 owns the phenomenological fast/slow system) |
| 15 | quasi-reversible system | `def:b3:electrode-kinetics:reversibility` | new; contested low (as above) |
| 15 | electrochemically irreversible system | `def:b3:electrode-kinetics:reversibility` | new; contested low (as above) |
| 15 | amperometry | `def:b3:electrode-kinetics:amperometry` | new |
| 15 | biosensor | `def:b3:electrode-kinetics:amperometry` | new |
| 15 | anodic stripping voltammetry | `def:b3:electrode-kinetics:stripping` | new |
| 15 | ion-selective electrode | `def:b3:electrode-kinetics:ise` | new |
| 15 | selectivity coefficient | `def:b3:electrode-kinetics:ise` | new |
| 15 | coulometry | `def:b3:electrode-kinetics:coulometry` | new |
| 15 | Butler–Volmer equation | `thm:b3:electrode-kinetics:butler-volmer` | map |
| 15 | Tafel equation | `cor:b3:electrode-kinetics:tafel` | map |
| 15 | Cottrell equation | `thm:b3:electrode-kinetics:cottrell` | new |
| 15 | Randles–Ševčík equation | `prop:b3:electrode-kinetics:randles-sevcik` | new |
| 15 | Nikolsky equation | `prop:b3:electrode-kinetics:nikolsky` | new |
| 16 | adsorption | `def:b3:surfaces-catalysis:adsorption` | map |
| 16 | adsorbate | `def:b3:surfaces-catalysis:adsorption` | new |
| 16 | adsorbent | `def:b3:surfaces-catalysis:adsorption` | new |
| 16 | desorption | `def:b3:surfaces-catalysis:adsorption` | new |
| 16 | physisorption | `def:b3:surfaces-catalysis:physi-chemi` | map |
| 16 | chemisorption | `def:b3:surfaces-catalysis:physi-chemi` | map |
| 16 | fractional coverage | `def:b3:surfaces-catalysis:coverage` | new |
| 16 | monolayer | `def:b3:surfaces-catalysis:coverage` | new |
| 16 | isosteric enthalpy of adsorption | `def:b3:surfaces-catalysis:isosteric` | new |
| 16 | specific surface area | `def:b3:surfaces-catalysis:surface-area` | new |
| 16 | Langmuir–Hinshelwood mechanism | `def:b3:surfaces-catalysis:mechanisms` | new |
| 16 | Eley–Rideal mechanism | `def:b3:surfaces-catalysis:mechanisms` | new |
| 16 | Sabatier principle | `def:b3:surfaces-catalysis:sabatier` | new |
| 16 | volcano plot | `def:b3:surfaces-catalysis:sabatier` | new |
| 16 | thermal desorption spectroscopy (gate 7 trips on "programme" inside "temperature-programmed") | `def:b3:surfaces-catalysis:tpd` | new |
| 16 | Langmuir isotherm | `thm:b3:surfaces-catalysis:langmuir` | new |
| 16 | BET isotherm | `thm:b3:surfaces-catalysis:bet` | new |
| 17 | surface tension | `def:b3:colloids:surface-tension` | new; contested low (physics uses it; no chemistry book defines it) |
| 17 | contact angle | `def:b3:colloids:wetting` | new |
| 17 | wetting | `def:b3:colloids:wetting` | new |
| 17 | surfactant | `def:b3:colloids:surfactant` | new |
| 17 | anionic surfactant | `def:b3:colloids:surfactant` | new |
| 17 | cationic surfactant | `def:b3:colloids:surfactant` | new |
| 17 | non-ionic surfactant | `def:b3:colloids:surfactant` | new |
| 17 | surface excess concentration | `def:b3:colloids:surface-excess` | new |
| 17 | micelle | `def:b3:colloids:micelle` | re-found (Book 1 g11); map/S1: Book 4 owns the university micelle |
| 17 | critical micelle concentration | `def:b3:colloids:micelle` | new |
| 17 | aggregation number | `def:b3:colloids:micelle` | new |
| 17 | packing parameter | `def:b3:colloids:packing` | new |
| 17 | colloid | `def:b3:colloids:colloid` | new |
| 17 | dispersed phase | `def:b3:colloids:colloid` | new |
| 17 | dispersion medium | `def:b3:colloids:colloid` | new |
| 17 | sol | `def:b3:colloids:colloid` | new; ch17 colloid sense |
| 17 | emulsion | `def:b3:colloids:colloid` | new |
| 17 | foam | `def:b3:colloids:colloid` | new |
| 17 | gel | `def:b3:colloids:colloid` | new; ch17 colloid sense; ch23 sol–gel uses it |
| 17 | aerosol | `def:b3:colloids:colloid` | new |
| 17 | Tyndall effect | `def:b3:colloids:tyndall` | new |
| 17 | zeta potential | `def:b3:colloids:zeta` | new |
| 17 | coagulation | `def:b3:colloids:stability` | new |
| 17 | flocculation | `def:b3:colloids:stability` | new |
| 17 | critical coagulation concentration | `def:b3:colloids:stability` | new |
| 17 | steric stabilisation | `def:b3:colloids:stability` | new |
| 17 | Ostwald ripening | `def:b3:colloids:ripening` | new |
| 17 | hydrophilic–lipophilic balance | `def:b3:colloids:hlb` | new |
| 17 | Young's equation | `thm:b3:colloids:young` | new |
| 17 | Kelvin equation | `thm:b3:colloids:kelvin` | new |
| 17 | Gibbs adsorption isotherm | `thm:b3:colloids:gibbs-adsorption` | new |
| 17 | Schulze–Hardy rule | `prop:b3:colloids:schulze-hardy` | new |
| 18 | ligand-field term | `def:b3:complex-spectra-magnetism:ligand-field-term` | map |
| 18 | correlation diagram | `def:b3:complex-spectra-magnetism:correlation` | map |
| 18 | Racah parameters | `def:b3:complex-spectra-magnetism:racah` | new |
| 18 | Tanabe–Sugano diagram | `def:b3:complex-spectra-magnetism:tanabe-sugano` | map |
| 18 | nephelauxetic effect | `def:b3:complex-spectra-magnetism:nephelauxetic` | new |
| 18 | nephelauxetic ratio | `def:b3:complex-spectra-magnetism:nephelauxetic` | new |
| 18 | vibronic coupling | `def:b3:complex-spectra-magnetism:vibronic-coupling` | new |
| 18 | ligand-to-metal charge transfer | `def:b3:complex-spectra-magnetism:ct` | new |
| 18 | metal-to-ligand charge transfer | `def:b3:complex-spectra-magnetism:ct` | new |
| 18 | magnetic susceptibility | `def:b3:complex-spectra-magnetism:susceptibility` | map |
| 18 | molar susceptibility | `def:b3:complex-spectra-magnetism:susceptibility` | new |
| 18 | Curie constant | `def:b3:complex-spectra-magnetism:curie` | new |
| 18 | effective magnetic moment | `def:b3:complex-spectra-magnetism:moment` | new |
| 18 | spin-only moment | `def:b3:complex-spectra-magnetism:moment` | map |
| 18 | orbital contribution | `def:b3:complex-spectra-magnetism:moment` | new |
| 18 | spin crossover | `def:b3:complex-spectra-magnetism:spin-crossover` | new |
| 18 | ferromagnetism | `def:b3:complex-spectra-magnetism:cooperative` | new |
| 18 | antiferromagnetism | `def:b3:complex-spectra-magnetism:cooperative` | new |
| 18 | Jahn–Teller theorem | `thm:b3:complex-spectra-magnetism:jahn-teller` | map |
| 18 | Curie law | `thm:b3:complex-spectra-magnetism:curie` | new |
| 19 | labile complex | `def:b3:complex-mechanisms:labile` | new |
| 19 | kinetically inert complex | `def:b3:complex-mechanisms:labile` | new; phrase only (Book 3 owns inert atmosphere) |
| 19 | volume of activation | `def:b3:complex-mechanisms:activation-volume` | new |
| 19 | dissociative mechanism | `def:b3:complex-mechanisms:mechanisms` | map |
| 19 | associative mechanism | `def:b3:complex-mechanisms:mechanisms` | map |
| 19 | interchange mechanism | `def:b3:complex-mechanisms:mechanisms` | new |
| 19 | Eigen–Wilkins mechanism | `def:b3:complex-mechanisms:eigen-wilkins` | new |
| 19 | outer-sphere complex | `def:b3:complex-mechanisms:eigen-wilkins` | new |
| 19 | conjugate-base mechanism | `def:b3:complex-mechanisms:conjugate-base` | new |
| 19 | trans effect | `def:b3:complex-mechanisms:trans-effect` | map |
| 19 | trans influence | `def:b3:complex-mechanisms:trans-effect` | new |
| 19 | outer-sphere electron transfer | `def:b3:complex-mechanisms:electron-transfer` | new |
| 19 | inner-sphere electron transfer | `def:b3:complex-mechanisms:electron-transfer` | new |
| 19 | self-exchange reaction | `def:b3:complex-mechanisms:electron-transfer` | new |
| 19 | reorganisation energy | `def:b3:complex-mechanisms:reorganisation` | new |
| 19 | inverted region | `def:b3:complex-mechanisms:inverted` | new |
| 19 | Marcus equation | `thm:b3:complex-mechanisms:marcus` | new |
| 19 | Marcus cross relation | `thm:b3:complex-mechanisms:cross-relation` | new |
| 20 | metal carbonyl | `def:b3:organometallic-bonding:carbonyl` | new |
| 20 | terminal carbonyl | `def:b3:organometallic-bonding:carbonyl` | new |
| 20 | bridging carbonyl | `def:b3:organometallic-bonding:carbonyl` | new |
| 20 | synergic bonding | `def:b3:organometallic-bonding:synergic` | new |
| 20 | Tolman cone angle | `def:b3:organometallic-bonding:tolman` | new |
| 20 | Tolman electronic parameter | `def:b3:organometallic-bonding:tolman` | new |
| 20 | Dewar–Chatt–Duncanson model | `def:b3:organometallic-bonding:dcd` | new |
| 20 | metallacyclopropane | `def:b3:organometallic-bonding:dcd` | new |
| 20 | metallocene | `def:b3:organometallic-bonding:metallocene` | new |
| 20 | sandwich compound | `def:b3:organometallic-bonding:metallocene` | new |
| 20 | carbene | `def:b3:organometallic-bonding:carbene` | new; placed in ch20 (ligand), ch27 recalls (outline lists carbenes in both) |
| 20 | carbene complex | `def:b3:organometallic-bonding:carbene` | new |
| 20 | Fischer carbene | `def:b3:organometallic-bonding:carbene` | new |
| 20 | Schrock carbene | `def:b3:organometallic-bonding:carbene` | new |
| 20 | N-heterocyclic carbene | `def:b3:organometallic-bonding:carbene` | new |
| 20 | carbyne complex | `def:b3:organometallic-bonding:carbyne` | new |
| 20 | δ bond | `def:b3:organometallic-bonding:delta` | new |
| 20 | quadruple bond | `def:b3:organometallic-bonding:delta` | new |
| 20 | isolobal fragments | `def:b3:organometallic-bonding:isolobal` | new |
| 20 | isolobal analogy | `def:b3:organometallic-bonding:isolobal` | new |
| 20 | agostic interaction | `def:b3:organometallic-bonding:agostic` | new |
| 21 | hydroformylation | `def:b3:homogeneous-catalysis:hydroformylation` | new; S2 split (Book 3 reads the cycle, Book 4 owns the process names) |
| 21 | linear-to-branched ratio | `def:b3:homogeneous-catalysis:hydroformylation` | new |
| 21 | carbonylation | `def:b3:homogeneous-catalysis:carbonylation` | new; S2 split |
| 21 | olefin metathesis | `def:b3:homogeneous-catalysis:metathesis` | new |
| 21 | metallacyclobutane | `def:b3:homogeneous-catalysis:metathesis` | new |
| 21 | ring-closing metathesis | `def:b3:homogeneous-catalysis:metathesis` | new |
| 21 | ring-opening metathesis polymerisation | `def:b3:homogeneous-catalysis:metathesis` | new |
| 21 | cross metathesis | `def:b3:homogeneous-catalysis:metathesis` | new |
| 21 | Chauvin mechanism | `def:b3:homogeneous-catalysis:chauvin` | new |
| 21 | cross-coupling reaction | `def:b3:homogeneous-catalysis:cross-coupling` | new; S2 split (as above) |
| 21 | Heck reaction | `def:b3:homogeneous-catalysis:cross-coupling` | new; S2 split |
| 21 | Suzuki–Miyaura coupling | `def:b3:homogeneous-catalysis:cross-coupling` | new; S2 split |
| 21 | Ziegler–Natta catalyst | `def:b3:homogeneous-catalysis:ziegler-natta` | new |
| 21 | Cossee–Arlman mechanism | `def:b3:homogeneous-catalysis:ziegler-natta` | new |
| 21 | single-site catalyst | `def:b3:homogeneous-catalysis:ziegler-natta` | new |
| 22 | energy band | `def:b3:solid-state:band` | new |
| 22 | band gap | `def:b3:solid-state:band` | new |
| 22 | valence band | `def:b3:solid-state:band` | new |
| 22 | conduction band | `def:b3:solid-state:band` | new |
| 22 | density of states | `def:b3:solid-state:fermi` | new |
| 22 | Fermi level | `def:b3:solid-state:fermi` | new |
| 22 | semiconductor | `def:b3:solid-state:classes` | new |
| 22 | insulator | `def:b3:solid-state:classes` | new |
| 22 | intrinsic semiconductor | `def:b3:solid-state:carriers` | new |
| 22 | charge carrier | `def:b3:solid-state:carriers` | new |
| 22 | hole | `def:b3:solid-state:carriers` | new; homograph risk (STOP outside ch22 if needed) |
| 22 | direct band gap | `def:b3:solid-state:gap-types` | new |
| 22 | indirect band gap | `def:b3:solid-state:gap-types` | new |
| 22 | dopant | `def:b3:solid-state:doping` | new |
| 22 | n-type semiconductor | `def:b3:solid-state:doping` | new |
| 22 | p-type semiconductor | `def:b3:solid-state:doping` | new |
| 22 | donor level | `def:b3:solid-state:doping` | new |
| 22 | acceptor level | `def:b3:solid-state:doping` | new |
| 22 | p–n junction | `def:b3:solid-state:junction` | new |
| 22 | point defect | `def:b3:solid-state:defects` | new |
| 22 | Schottky defect | `def:b3:solid-state:defects` | new |
| 22 | Frenkel defect | `def:b3:solid-state:defects` | new |
| 22 | Kröger–Vink notation | `def:b3:solid-state:kroger-vink` | new |
| 22 | colour centre | `def:b3:solid-state:colour-centre` | new |
| 22 | non-stoichiometric compound | `def:b3:solid-state:non-stoichiometric` | new |
| 22 | ionic conductor | `def:b3:solid-state:ionic-conductor` | new |
| 22 | solid electrolyte | `def:b3:solid-state:ionic-conductor` | new |
| 23 | ceramic method | `def:b3:inorganic-materials:ceramic-method` | new |
| 23 | sol–gel process | `def:b3:inorganic-materials:sol-gel` | new |
| 23 | xerogel | `def:b3:inorganic-materials:sol-gel` | new |
| 23 | aerogel | `def:b3:inorganic-materials:sol-gel` | new |
| 23 | hydrothermal synthesis | `def:b3:inorganic-materials:hydrothermal` | new |
| 23 | solvothermal synthesis | `def:b3:inorganic-materials:hydrothermal` | new |
| 23 | chemical vapour deposition | `def:b3:inorganic-materials:cvd` | new |
| 23 | ceramic | `def:b3:inorganic-materials:ceramic` | new |
| 23 | perovskite structure | `def:b3:inorganic-materials:perovskite` | new |
| 23 | tolerance factor | `def:b3:inorganic-materials:perovskite` | new |
| 23 | ferroelectric | `def:b3:inorganic-materials:ferroelectric` | new |
| 23 | oxide glass | `def:b3:inorganic-materials:glass` | new; phrase only (glassware everywhere) |
| 23 | network former | `def:b3:inorganic-materials:glass` | new |
| 23 | network modifier | `def:b3:inorganic-materials:glass` | new |
| 23 | zeolite | `def:b3:inorganic-materials:zeolite` | new |
| 23 | molecular sieve | `def:b3:inorganic-materials:zeolite` | new |
| 23 | shape selectivity | `def:b3:inorganic-materials:zeolite` | new |
| 23 | metal–organic framework | `def:b3:inorganic-materials:mof` | new |
| 23 | secondary building unit | `def:b3:inorganic-materials:mof` | new |
| 23 | reticular synthesis | `def:b3:inorganic-materials:mof` | new |
| 23 | micropore | `def:b3:inorganic-materials:pores` | new |
| 23 | mesopore | `def:b3:inorganic-materials:pores` | new |
| 23 | macropore | `def:b3:inorganic-materials:pores` | new |
| 23 | nanomaterial | `def:b3:inorganic-materials:nano` | new |
| 23 | nanoparticle | `def:b3:inorganic-materials:nano` | new |
| 23 | quantum dot | `def:b3:inorganic-materials:quantum-dot` | new |
| 23 | surface plasmon resonance | `def:b3:inorganic-materials:plasmon` | new |
| 23 | fullerene | `def:b3:inorganic-materials:carbon` | new |
| 23 | carbon nanotube | `def:b3:inorganic-materials:carbon` | new |
| 23 | graphene | `def:b3:inorganic-materials:carbon` | new |
| 23 | Löwenstein's rule | `prop:b3:inorganic-materials:lowenstein` | new |
| 24 | metalloprotein | `def:b3:bioinorganic:metalloprotein` | new |
| 24 | metalloenzyme | `def:b3:bioinorganic:metalloprotein` | new |
| 24 | cofactor | `def:b3:bioinorganic:metalloprotein` | new |
| 24 | hard acid | `def:b3:bioinorganic:hsab` | new; contested low (Book 3 ch17 owns hard/soft nucleophile/electrophile phrases) |
| 24 | soft acid | `def:b3:bioinorganic:hsab` | new; contested low (as above) |
| 24 | hard and soft acid–base principle | `def:b3:bioinorganic:hsab` | new; contested low (as above) |
| 24 | Irving–Williams series | `def:b3:bioinorganic:irving-williams` | new |
| 24 | porphyrin | `def:b3:bioinorganic:haem` | new |
| 24 | haem | `def:b3:bioinorganic:haem` | new |
| 24 | cooperative binding | `def:b3:bioinorganic:cooperativity` | new |
| 24 | Hill coefficient | `def:b3:bioinorganic:cooperativity` | new |
| 24 | entatic state | `def:b3:bioinorganic:entatic` | new |
| 24 | iron–sulfur cluster | `def:b3:bioinorganic:fes` | new |
| 24 | blue copper protein | `def:b3:bioinorganic:blue-copper` | new |
| 24 | oxygen-evolving complex | `def:b3:bioinorganic:oec` | new |
| 24 | metallodrug | `def:b3:bioinorganic:metallodrug` | new |
| 24 | contrast agent | `def:b3:bioinorganic:contrast` | new |
| 24 | relaxivity | `def:b3:bioinorganic:contrast` | new |
| 24 | chelation therapy | `def:b3:bioinorganic:chelation-therapy` | new |
| 24 | Hill equation | `thm:b3:bioinorganic:hill` | new |
| 25 | supramolecular chemistry | `def:b3:supramolecular:supramolecular` | new |
| 25 | host | `def:b3:supramolecular:supramolecular` | new; homograph risk (ordinary word; STOP outside ch25 if needed) |
| 25 | guest | `def:b3:supramolecular:supramolecular` | new; as above |
| 25 | host–guest complex | `def:b3:supramolecular:supramolecular` | new |
| 25 | molecular recognition | `def:b3:supramolecular:recognition` | new |
| 25 | complementarity | `def:b3:supramolecular:recognition` | new |
| 25 | preorganisation | `def:b3:supramolecular:recognition` | new |
| 25 | π stacking | `def:b3:supramolecular:interactions` | new |
| 25 | cation–π interaction | `def:b3:supramolecular:interactions` | new |
| 25 | halogen bond | `def:b3:supramolecular:interactions` | new |
| 25 | hydrophobic effect | `def:b3:supramolecular:interactions` | new |
| 25 | chelate effect | `def:b3:supramolecular:macrocyclic` | new; contested low (no map row; Book 2 ch12 and Book 3 ch18 do not define it) |
| 25 | macrocyclic effect | `def:b3:supramolecular:macrocyclic` | new |
| 25 | crown ether | `def:b3:supramolecular:hosts` | new |
| 25 | cryptand | `def:b3:supramolecular:hosts` | new |
| 25 | cryptate | `def:b3:supramolecular:hosts` | new |
| 25 | cyclodextrin | `def:b3:supramolecular:hosts` | new |
| 25 | calixarene | `def:b3:supramolecular:hosts` | new |
| 25 | isothermal titration calorimetry | `def:b3:supramolecular:itc` | new |
| 25 | Job plot | `def:b3:supramolecular:job` | new |
| 25 | template synthesis | `def:b3:supramolecular:template` | new |
| 25 | self-assembly | `def:b3:supramolecular:self-assembly` | new |
| 25 | mechanically interlocked molecule | `def:b3:supramolecular:interlocked` | new |
| 25 | rotaxane | `def:b3:supramolecular:interlocked` | new |
| 25 | catenane | `def:b3:supramolecular:interlocked` | new |
| 25 | molecular machine | `def:b3:supramolecular:machine` | new |
| 26 | pericyclic reaction | `def:b3:pericyclic:pericyclic` | map |
| 26 | electrocyclic reaction | `def:b3:pericyclic:families` | map |
| 26 | cycloaddition | `def:b3:pericyclic:families` | map |
| 26 | sigmatropic rearrangement | `def:b3:pericyclic:families` | map |
| 26 | cheletropic reaction | `def:b3:pericyclic:families` | new |
| 26 | ene reaction | `def:b3:pericyclic:families` | new |
| 26 | conrotatory | `def:b3:pericyclic:rotation-modes` | new |
| 26 | disrotatory | `def:b3:pericyclic:rotation-modes` | new |
| 26 | suprafacial | `def:b3:pericyclic:faciality` | new |
| 26 | antarafacial | `def:b3:pericyclic:faciality` | new |
| 26 | orbital correlation diagram | `def:b3:pericyclic:orbital-correlation` | new |
| 26 | state correlation diagram | `def:b3:pericyclic:state-correlation` | new |
| 26 | 1,3-dipole | `def:b3:pericyclic:dipolar` | new |
| 26 | 1,3-dipolar cycloaddition | `def:b3:pericyclic:dipolar` | new |
| 26 | Cope rearrangement | `def:b3:pericyclic:cope-claisen` | new |
| 26 | Claisen rearrangement | `def:b3:pericyclic:cope-claisen` | new |
| 26 | aromatic transition state | `def:b3:pericyclic:mobius` | new |
| 26 | Möbius transition state | `def:b3:pericyclic:mobius` | new |
| 26 | Woodward–Hoffmann rules | `thm:b3:pericyclic:woodward-hoffmann` | map |
| 27 | radical clock | `def:b3:radicals-carbenes:radical-clock` | new |
| 27 | exo cyclisation | `def:b3:radicals-carbenes:cyclisation` | new |
| 27 | endo cyclisation | `def:b3:radicals-carbenes:cyclisation` | new |
| 27 | singlet carbene | `def:b3:radicals-carbenes:carbene-states` | new |
| 27 | triplet carbene | `def:b3:radicals-carbenes:carbene-states` | new |
| 27 | carbenoid | `def:b3:radicals-carbenes:carbenoid` | new |
| 27 | cyclopropanation | `def:b3:radicals-carbenes:cyclopropanation` | new |
| 27 | nitrene | `def:b3:radicals-carbenes:nitrene` | new |
| 27 | 1,2-shift | `def:b3:radicals-carbenes:shift` | new |
| 27 | pinacol rearrangement | `def:b3:radicals-carbenes:pinacol` | new |
| 27 | migratory aptitude | `def:b3:radicals-carbenes:migratory` | new |
| 27 | Beckmann rearrangement | `def:b3:radicals-carbenes:beckmann` | new |
| 27 | Baeyer–Villiger oxidation | `def:b3:radicals-carbenes:baeyer` | new |
| 27 | isocyanate | `def:b3:radicals-carbenes:curtius` | new; contested low (not in Book 3 ch23–24 map) |
| 27 | Curtius rearrangement | `def:b3:radicals-carbenes:curtius` | new |
| 27 | Hofmann rearrangement | `def:b3:radicals-carbenes:curtius` | new |
| 27 | ketene | `def:b3:radicals-carbenes:wolff` | new; contested low (not in Book 3 ch24–25 map) |
| 27 | Wolff rearrangement | `def:b3:radicals-carbenes:wolff` | new |
| 27 | Baldwin's rules | `prop:b3:radicals-carbenes:baldwin` | new |
| 28 | enantiomeric excess | `def:b3:asymmetric-synthesis:ee` | new |
| 28 | enantiomeric ratio | `def:b3:asymmetric-synthesis:ee` | new |
| 28 | diastereomeric excess | `def:b3:asymmetric-synthesis:ee` | new |
| 28 | optical purity | `def:b3:asymmetric-synthesis:ee` | new |
| 28 | enantioselective reaction | `def:b3:asymmetric-synthesis:selective` | new |
| 28 | diastereoselective reaction | `def:b3:asymmetric-synthesis:selective` | new |
| 28 | homotopic | `def:b3:asymmetric-synthesis:topicity` | new |
| 28 | enantiotopic | `def:b3:asymmetric-synthesis:topicity` | new |
| 28 | diastereotopic | `def:b3:asymmetric-synthesis:topicity` | new |
| 28 | prochiral | `def:b3:asymmetric-synthesis:faces` | new |
| 28 | Re face | `def:b3:asymmetric-synthesis:faces` | new |
| 28 | Si face | `def:b3:asymmetric-synthesis:faces` | new |
| 28 | Felkin–Anh model | `def:b3:asymmetric-synthesis:felkin` | new |
| 28 | chelation control | `def:b3:asymmetric-synthesis:felkin` | new |
| 28 | chiral pool | `def:b3:asymmetric-synthesis:chiral-pool` | new |
| 28 | chiral auxiliary | `def:b3:asymmetric-synthesis:auxiliary` | new |
| 28 | resolution of a racemate | `def:b3:asymmetric-synthesis:resolution` | new; as above |
| 28 | kinetic resolution | `def:b3:asymmetric-synthesis:resolution` | new; never bare "resolution" (Book 3 ch31 owns chromatographic resolution) |
| 28 | dynamic kinetic resolution | `def:b3:asymmetric-synthesis:resolution` | new |
| 28 | asymmetric catalysis | `def:b3:asymmetric-synthesis:asymmetric-catalysis` | new |
| 28 | chiral ligand | `def:b3:asymmetric-synthesis:asymmetric-catalysis` | new |
| 28 | Sharpless epoxidation | `def:b3:asymmetric-synthesis:sharpless` | new |
| 28 | organocatalysis | `def:b3:asymmetric-synthesis:organocatalysis` | new |
| 28 | enamine catalysis | `def:b3:asymmetric-synthesis:organocatalysis` | new |
| 28 | iminium catalysis | `def:b3:asymmetric-synthesis:organocatalysis` | new |
| 28 | Kagan equation | `thm:b3:asymmetric-synthesis:kagan` | new |
| 29 | heterocycle | `def:b3:heterocycles:heterocycle` | new |
| 29 | heteroaromatic compound | `def:b3:heterocycles:heterocycle` | new |
| 29 | π-excessive heterocycle | `def:b3:heterocycles:pi-character` | new |
| 29 | π-deficient heterocycle | `def:b3:heterocycles:pi-character` | new |
| 29 | nucleophilic aromatic substitution | `def:b3:heterocycles:snar` | new; contested low (not in Book 3 ch22–23 map) |
| 29 | Meisenheimer complex | `def:b3:heterocycles:snar` | new; contested low (as above) |
| 29 | Chichibabin reaction | `def:b3:heterocycles:chichibabin` | new |
| 29 | pyridine N-oxide | `def:b3:heterocycles:n-oxide` | new |
| 29 | Paal–Knorr synthesis | `def:b3:heterocycles:paal-knorr` | new |
| 29 | Hantzsch pyridine synthesis | `def:b3:heterocycles:hantzsch` | new |
| 29 | Fischer indole synthesis | `def:b3:heterocycles:fischer-indole` | new |
| 29 | bioisostere | `def:b3:heterocycles:bioisostere` | new |
| 30 | total synthesis | `def:b3:total-synthesis:total` | new |
| 30 | formal synthesis | `def:b3:total-synthesis:total` | new |
| 30 | semisynthesis | `def:b3:total-synthesis:total` | new |
| 30 | linear synthesis | `def:b3:total-synthesis:architecture` | map |
| 30 | convergent synthesis | `def:b3:total-synthesis:architecture` | map |
| 30 | longest linear sequence | `def:b3:total-synthesis:architecture` | new |
| 30 | overall yield | `def:b3:total-synthesis:architecture` | new |
| 30 | step economy | `def:b3:total-synthesis:economy` | new |
| 30 | protecting-group economy | `def:b3:total-synthesis:economy` | map |
| 30 | ideality | `def:b3:total-synthesis:economy` | new |
| 30 | cascade reaction | `def:b3:total-synthesis:cascade` | new |
| 30 | biomimetic synthesis | `def:b3:total-synthesis:biomimetic` | new |
| 30 | Mannich reaction | `def:b3:total-synthesis:mannich` | new; contested low (not in Book 3 ch23/25 map) |
| 30 | strategic bond | `def:b3:total-synthesis:strategic-bond` | new; contested low (not in Book 3 ch28 map) |
| 31 | green chemistry | `def:b3:green-industrial:green-chemistry` | re-found (Book 1 g12 synthesis-strategy); map |
| 31 | atom economy | `def:b3:green-industrial:atom-economy` | re-found (Book 1 g12 synthesis-strategy); map |
| 31 | E-factor | `def:b3:green-industrial:e-factor` | map |
| 31 | process mass intensity | `def:b3:green-industrial:pmi` | new |
| 31 | reaction mass efficiency | `def:b3:green-industrial:rme` | new |
| 31 | life-cycle assessment | `def:b3:green-industrial:lca` | map |
| 31 | functional unit | `def:b3:green-industrial:lca` | new |
| 31 | system boundary | `def:b3:green-industrial:lca` | new |
| 31 | cradle-to-gate assessment | `def:b3:green-industrial:lca` | new |
| 31 | carbon footprint | `def:b3:green-industrial:carbon-footprint` | new |
| 31 | process intensification | `def:b3:green-industrial:intensification` | new |
| 31 | biocatalysis | `def:b3:green-industrial:biocatalysis` | new |
| 31 | renewable feedstock | `def:b3:green-industrial:feedstock` | new |
| 31 | platform molecule | `def:b3:green-industrial:feedstock` | new |
| 32 | greenhouse gas | `def:b3:environmental-toxicology:greenhouse` | re-found (Book 1 g8 combustion-and-fuels) |
| 32 | global warming potential | `def:b3:environmental-toxicology:greenhouse` | new |
| 32 | particulate matter | `def:b3:environmental-toxicology:pollutants` | new |
| 32 | acid rain | `def:b3:environmental-toxicology:pollutants` | new |
| 32 | alkalinity | `def:b3:environmental-toxicology:alkalinity` | new |
| 32 | ocean acidification | `def:b3:environmental-toxicology:acidification` | new |
| 32 | saturation state | `def:b3:environmental-toxicology:acidification` | new |
| 32 | water hardness | `def:b3:environmental-toxicology:hardness` | new |
| 32 | eutrophication | `def:b3:environmental-toxicology:eutrophication` | new |
| 32 | chemical speciation | `def:b3:environmental-toxicology:speciation` | new |
| 32 | cation exchange capacity | `def:b3:environmental-toxicology:soil` | new |
| 32 | soil–water distribution coefficient | `def:b3:environmental-toxicology:soil` | new; contested low (as above) |
| 32 | organic-carbon partition coefficient | `def:b3:environmental-toxicology:soil` | new; contested low (as above) |
| 32 | octanol–water partition coefficient | `def:b3:environmental-toxicology:kow` | new; contested low (Book 2 owns the generic partition coefficient) |
| 32 | bioconcentration factor | `def:b3:environmental-toxicology:bio` | new |
| 32 | bioaccumulation | `def:b3:environmental-toxicology:bio` | new |
| 32 | biomagnification | `def:b3:environmental-toxicology:bio` | new |
| 32 | persistent organic pollutant | `def:b3:environmental-toxicology:pop` | new |
| 32 | dose–response relationship | `def:b3:environmental-toxicology:dose` | new |
| 32 | median lethal dose | `def:b3:environmental-toxicology:dose` | new |
| 32 | median effective concentration | `def:b3:environmental-toxicology:dose` | new |
| 32 | no-observed-adverse-effect level | `def:b3:environmental-toxicology:dose` | new |
| 32 | lowest-observed-adverse- effect level | `def:b3:environmental-toxicology:dose` | new |
| 32 | acute toxicity | `def:b3:environmental-toxicology:toxicity` | new |
| 32 | chronic toxicity | `def:b3:environmental-toxicology:toxicity` | new |
| 32 | ecotoxicology | `def:b3:environmental-toxicology:ecotoxicology` | new |
| 32 | predicted no-effect concentration | `def:b3:environmental-toxicology:ecotoxicology` | new |
| 32 | predicted environmental concentration | `def:b3:environmental-toxicology:ecotoxicology` | new |
| 32 | risk quotient | `def:b3:environmental-toxicology:ecotoxicology` | new |
| 32 | occupational exposure limit | `def:b3:environmental-toxicology:oel` | new |
| 33 | air-sensitive compound | `def:b3:lab-techniques-3:air-sensitive` | new |
| 33 | pyrophoric substance | `def:b3:lab-techniques-3:air-sensitive` | new |
| 33 | Schlenk line | `def:b3:lab-techniques-3:schlenk` | new |
| 33 | Schlenk flask | `def:b3:lab-techniques-3:schlenk` | new |
| 33 | glovebox | `def:b3:lab-techniques-3:schlenk` | new |
| 33 | cannula transfer | `def:b3:lab-techniques-3:cannula` | new |
| 33 | freeze–pump–thaw degassing | `def:b3:lab-techniques-3:degassing` | new |
| 33 | elemental analysis | `def:b3:lab-techniques-3:elemental` | new; contested low (not in Book 3 ch32/35 map) |
| 33 | quantitative NMR | `def:b3:lab-techniques-3:qnmr` | new; contested low (Book 3 owns internal standard) |
| 33 | significance test | `def:b3:lab-techniques-3:tests` | new |
| 33 | null hypothesis | `def:b3:lab-techniques-3:tests` | new |
| 33 | laboratory notebook | `def:b3:lab-techniques-3:notebook` | new |
| 33 | raw data | `def:b3:lab-techniques-3:notebook` | new |
| 33 | FAIR data | `def:b3:lab-techniques-3:fair` | new |
| 33 | research integrity | `def:b3:lab-techniques-3:integrity` | new |
| 33 | fabrication | `def:b3:lab-techniques-3:integrity` | new |
| 33 | falsification | `def:b3:lab-techniques-3:integrity` | new |
| 33 | plagiarism | `def:b3:lab-techniques-3:integrity` | new |
| 33 | risk assessment | `def:b3:lab-techniques-3:assessment` | new; contested low (Book 2 owns hazard and risk) |
| 33 | hierarchy of controls | `def:b3:lab-techniques-3:assessment` | new |
| 33 | peroxide former | `def:b3:lab-techniques-3:peroxide` | new |
| 33 | primary literature | `def:b3:lab-techniques-3:literature` | new |
| 33 | secondary literature | `def:b3:lab-techniques-3:literature` | new |
| 33 | peer review | `def:b3:lab-techniques-3:literature` | new |
| 33 | supporting information | `def:b3:lab-techniques-3:literature` | new |

Total: 678 terms in 359 labels.

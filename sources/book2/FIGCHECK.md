# Book 2 — per-figure check

One line per figure (`omfigure` / `includegraphics`), checked on its own page
rendered at 130 dpi (`pdftoppm -png -r 130 -f P -l P -singlefile`), for layout
and for chemistry. Page numbers are PDF pages at the time of the check.

| ch | figure | page | layout | chemistry | note |
|---|---|---|---|---|---|
| 1 | AI sodium street lamps | 8 | ok | ok | monochromatic orange lamps; no letters |
| 1 | hydrogen level diagram (figdata hydrogen-levels) | 10 | fixed | ok | n=4,5 label collided with n=3: removed, said in caption; arrows Lyman to 1, Balmer to 2, Paschen to 3 |
| 1 | Balmer line strip (figdata) | 10 | ok | fixed | lines were all red: now red/cyan/blue/violet at 656.5/486.3/434.2/410.3 nm; limit 364.7 |
| 1 | photo Niels Bohr | 10 | ok | ok | PD |
| 1 | Klechkowski diagram | 12 | fixed | ok | arrows crossed the labels: moved to background, white nodes; diagonals n+l = 1..8 in order |
| 1 | quantum boxes N and Cr | 13 | ok | ok | N 2p three up; Cr 3d5 4s1 six unpaired |
| 1 | periodic table by block | 14 | ok | ok | He in s block, widths 2/6/10/14 |
| 2 | periodic table metals/metalloids | 18 | ok | ok | metalloid staircase B, Si, Ge, As, Sb, Te |
| 2 | isoelectronic ions to scale | 19 | fixed | ok | circles O2- and F- touched: spaced; radii 140/133/102/72/54 pm at 0.3 pt/pm |
| 2 | first ionisation energies Z=1-36 (figdata) | 19 | fixed | ok | B, O, S labels sat on the line: moved below; maxima He Ne Ar Kr, minima Li Na K |
| 2 | successive IE of Mg (figdata, log) | 20 | fixed | ok | value labels rounded to 1 decimal: now 7.65/15.04/80.14/109.27 as in text |
| 2 | Pauling EN table (values from ledger) | 21 | ok | ok | F O Cl N shaded in that order of EN |
| 2 | photo Linus Pauling | 22 | ok | ok | PD |
| 3 | Lewis structures HNO3, N2, N2O | 27 | fixed | ok | first draft too small and lone pairs garbled; redrawn with bars (\charge), formal charges N+ and O- |
| 3 | dative bond NH3 + BF3 | 28 | fixed | ok | charges sat on bonds: moved to 45 deg; N+ and B- in the adduct |
| 3 | resonance ozone / benzene / nitrate | 29 | fixed | ok | overlapped text above and caption below: spacing added; central O+ with one lone pair, terminal O- three pairs |
| 3 | sigma and pi overlap | 29 | fixed | ok | the two labels at different heights: aligned |
| 3 | VSEPR gallery (10 shapes) | 30 | fixed | fixed | labels collided at 2.0em: redrawn at 2.6em; SO2 drawn with S=O; XeF4 drawn face on |
| 3 | dipoles of H2O and CO2 | 32 | ok | ok | bond dipoles from O(-) to H(+), resultant along bisector towards H; CO2 arrows towards C cancel |
| 4 | AI gecko on a window | 35 | ok | ok | toe pads flat on glass; no letters |
| 4 | three van der Waals interactions | 36 | fixed | ok | Keesom and Debye labels collided: two-line labels; facing charges opposite in all three |
| 4 | alkane boiling points (figdata) | 36 | ok | ok | monotonic, increments 74 -> 23 degC |
| 4 | water H-bond network + acid dimer | 37 | fixed | fixed | dimer drawn as two disconnected chemfigs: redrawn as a ring with two O-H...O=C bonds; third water moved so the H-bond ends on O |
| 4 | hydride boiling points groups 14-17 (figdata) | 37 | fixed | ok | 'extrapolated' and CH4 labels sat on lines/axis: moved; dashed line from H2S to -79.3 at period 2 |
| 4 | hydration of Na+ and Cl- | 39 | fixed | ok | Cl- label unreadable on green: white; O towards Na+, H towards Cl- |
| 4 | AI salad dressing | 40 | fixed | ok | oil on top; width reduced (portrait image) |
| 4 | amphiphile at surface + micelle | 40 | ok | ok | heads in water, tails in air / inside |
| 5 | AI blacksmith | 45 | ok | ok | glowing orange steel, safety glasses, no letters |
| 5 | close-packed layers A, B, C | 47 | fixed | ok | C letters unreadable: green dots; B in the up-hollows of A |
| 5 | FCC and BCC cells (tikz-3dplot) | 47 | fixed | ok | contact-line labels sat on atoms: moved to caption; face diagonal through a face centre, main diagonal through the body centre |
| 5 | HCP prism | 48 | fixed | ok | a/c labels on atoms: moved to caption; 3 B atoms at c/2 in alternate hollows |
| 5 | photo native copper | 49 | ok | ok | CC0 |
| 5 | octahedral and tetrahedral sites of FCC | 50 | ok | ok | 4 octahedral (centre + 12 edges/4), 8 tetrahedral at (a/4...); one joined to its 4 atoms |
| 6 | radius-ratio number line | 55 | ok | fixed | RbCl mark at 10.26 instead of 12 x 0.84 = 10.08: moved |
| 6 | NaCl and CsCl cells | 55 | fixed | ok | 'NaCl (rock salt)' label under an atom: lowered; Cl- larger than Na+ |
| 6 | photos halite, fluorite, diamond | 56 | ok | ok | CC BY 2.0, credited in captions |
| 6 | ZnS and CaF2 cells | 57 | ok | fixed | F- drawn smaller than Ca2+ although r(F-) 131 > r(Ca2+) 112 pm: sizes swapped; Zn in alternate tetrahedral sites with 4 bonds |
| 6 | diamond cell + graphite layers | 58 | ok | ok | 4 bonds per C; graphite ABAB offset by one bond |
| 6 | photo graphite | 58 | ok | ok | CC BY-SA 4.0 credited |
| 6 | photo Bentley snow crystals | 59 | ok | ok | PD, six-fold |
| 7 | AI hydrogen plant | 62 | ok | ok | industrial scene, no letters visible |
| 7 | Q vs K number line | 65 | ok | ok | forward below K, reverse above |
| 7 | Q(xi) shift + carbonate (figdata) | 67 | fixed | fixed | plots stacked (too wide) and 0.607 on the 0.6 tick: widths/ticks fixed; large-sample curve drawn past K: now stops at K (equilibrium) |
| 8 | AI milk and refrigerator | 71 | ok | ok | no letters |
| 8 | integrated rate laws, 4 panels (figdata) | 73 | ok | ok | linear forms straight; half-lives 10/13.9/20 min marked by the 0.5 line |
| 8 | initial-rate tangent | 74 | fixed | ok | curve ran past xmax and t0 label on the tick: clipped, label removed (caption gives t0) |
| 8 | Arrhenius plot of the medicine (figdata) | 75 | fixed | ok | line ran below the axis and the 25 degC label sat on it: ymin -9, point marked, label moved; slope -Ea/R = -1.02e4 K |
| 8 | photo Svante Arrhenius | 76 | ok | ok | PD |
| 9 | energy profiles one step / two steps (figdata) | 80 | fixed | ok | barrier label crossed the curve, Delta E on 'products', label on the axis: moved, ymin lowered; stationary points exact |
| 9 | consecutive reactions k2 = 0.5 k1 and 20 k1 (figdata) | 82 | fixed | ok | 'A' label on a crossing: moved; B max at k1 t = 1.39; steady state dashed |
| 9 | catalysed vs uncatalysed profile (figdata) | 83 | fixed | ok | labels on the dashed baseline and on the curve end: moved; same Delta E |
| 9 | generic catalytic cycle | 83 | ok | ok | catalyst regenerated, A and B in, P out |
| 9 | AI catalytic converter | 83 | ok | ok | no letters |
| 10 | AI kettle limescale (pending stub) | 87 | - | - | image not generated yet: \IfFileExists stub, check when it lands |
| 10 | distribution diagrams + phosphoric predominance (figdata) | 89 | fixed | ok | labels on curves: legend for phosphoric, ethanoic labels moved; crossings at pKa 4.76 / 2.15, 7.21, 12.34 |
| 10 | pKa ladder | 90 | ok | ok | arrow from CH3COOH (4.76) up to NH3 (9.25), HF placed at 3.16/2 |
| 10 | pH vs pC of ethanoic acid (figdata) | 91 | ok | ok | exact curve on 1/2(pKa+pC) when concentrated, -> 7 dilute |
| 11 | AI limestone cave (stub until batch 2) | 95 | pending | pending | grey box until b1-11-cave lands |
| 11 | AgCl crystal in saturated solution | 96 | ok | ok | Ag+ drawn smaller than Cl-; alternating lattice; arrows dissolution/precipitation |
| 11 | table of pKs | 96 | fixed | ok | empty spacer columns removed; values = test-pinned aqueous-constants |
| 11 | photo silver halides | 97 | ok | ok | white / cream / pale yellow in the right order; CC BY-SA 3.0 |
| 11 | existence domains AgCl (pCl) and AgI (pI) | 99 | ok | ok | boundaries 7.75 and 14.07 for c = 1e-2; solid on the low-pX side |
| 11 | hydroxide thresholds bar chart (figdata) | 100 | fixed | ok | stray marks at bar starts removed (draw=none); Fe3+ < Al3+ < Zn2+ ~ Fe2+ < Mg2+ < Ca2+ |
| 11 | log s vs pH, Zn and Al (figdata) | 101 | fixed | ok | ion labels sat on the curves and panel names on the minima: moved; dotted contributions hidden under solid line: dropped; slopes -2/+2 and -3/+1 |
| 11 | AI limestone cave | 95 | ok | ok | batch 2 image reviewed: stalactites and stalagmites, no letters; stub replaced |
| 10 | AI kettle descaling | 80 | ok | ok | batch 2 image reviewed: scaled kettle, lemon, vinegar; stub replaced |
| 12 | photos Cu(OH)2 and copper ammine | 106 | fixed | ok | caption claimed the hydroxide came from ammonia (unknown): reworded; deep blue over pale precipitate |
| 12 | three complexes (linear, square planar, octahedral) | 107 | fixed | ok | dashed outlines ran through labels: white-filled labels, outline on background layer, figure enlarged |
| 12 | edta and Ca-edta chelate | 107 | fixed | fixed | first draft put the two N trans: redrawn cis (adjacent octahedron corners), five 5-membered rings outward |
| 12 | Cu-NH3 distribution + pL axes (figdata) | 109 | fixed | ok | n labels sat on the peaks: moved above; Ag single boundary 3.61 between dotted logK |
| 13 | Daniell cell | 116 | ok | ok | Zn anode negative, electrons Zn -> Cu in the wire, K+ to cathode, NO3- to anode |
| 13 | standard hydrogen electrode | 116 | fixed | ok | first draft unreadable (labels on the beaker, inlet unclear): redrawn with jacket, inlet arm and leader lines |
| 13 | table of E0 | 117 | ok | ok | values = test-pinned standard-potentials |
| 13 | Nernst photo | 118 | ok | ok | PD, 1889 |
| 13 | potential scale + gamma | 118 | fixed | ok | couples 0.15 V apart overlapped at 1.25 cm/V: 2.6 cm/V; gamma arrows crossed labels: rerouted, text labels dropped |
| 14 | AI ship stern with zinc anodes | 115 | ok | ok | batch 2 image reviewed: grey zinc blocks on a red hull near the propeller; no letters |
| 14 | E-pH diagram of iron (figdata) | 117 | fixed | ok | Fe3+ and Fe(OH)3 labels on the O2 line, Fe(OH)2 on its boundary: moved; slopes -0.177, -0.059; triple points 1.81/0.77 and 6.84 |
| 14 | E-pH diagrams of copper and zinc (figdata) | 118 | fixed | ok | zinc ylabel ran into the copper panel: narrower panels, wider gap; no Cu+ domain; Zn(OH)4 2- sliver above 13.96 marked by arrow |
| 15 | AI teaching lab | 121 | ok | ok | batch 2: goggles, gloves, burette over a flask on a stirrer |
| 15 | pH-metric set-up | 124 | fixed | ok | burette tip floated 2 cm above the beaker: lowered to the rim; electrode wired to the meter |
| 15 | pH-metric curves (figdata) | 124 | fixed | ok | species labels on the curves: moved; jump 3.3-10.7 at +-0.1 mL; half-eq 4.76; eq 8.73; mixture eq at 5 and 10 mL |
| 15 | indicator table | 125 | ok | ok | pKa from the IUPAC dataset, zones pKa +- 1 |
| 15 | potentiometric + conductimetric curves (figdata) | 126 | ok | ok | 0.77 / 1.39 / 1.51 V; conductivity V with minimum 1.15 mS/cm at 10 mL |
| 16 | AI caraway and spearmint | 131 | ok | ok | batch 2: seeds in a bowl, mint sprig; no letters |
| 16 | Newman (staggered, eclipsed), Fischer and Cram of (R)-lactic acid | 132 | fixed | fixed | eclipsed rear H labels sat on front bonds: offset 18 deg, labels outside; Cram drawing first had COOH/CH3 collinear (no chirality readable): redrawn, chirality checked by signed volume = R, same as the Fischer cross |
| 16 | the two carvones | 134 | fixed | fixed | chemfig ring first put the isopropenyl on C4: redrawn in TikZ with explicit coordinates; wedge = (R) checked numerically; CH3 label clashed with name: moved |
| 16 | van 't Hoff photo | 134 | ok | ok | PD, published 1911 |
| 16 | torsion energy of butane and ethane (figdata) | 135 | fixed | ok | conformer labels on the curves: moved to a top row; reproduces the CCCBDB table (16.56/2.83/15.19 kJ/mol) within 0.05 |
| 16 | chair, axial/equatorial, ring flip of methylcyclohexane | 135 | fixed | fixed | figure 36 pt too wide: tightened; flipped chair first showed the methyl axial on the wrong face: substituent moved to the carbon that stays on the right (axial down) |
| 16 | polarimeter | 136 | ok | ok | lamp, polariser, sample, analyser, angle alpha |
| 17 | AI carrots and tomatoes | 141 | ok | ok | batch 2 |
| 17 | colour wheel | 141 | ok | ok | blue opposite orange |
| 17 | IR band table and simulated IR (figdata) | 142 | ok | ok | gas-phase positions from NIST WebBook JCAMP peak search; heights schematic, said so |
| 17 | splitting trees | 143 | fixed | ok | bars overlapped the tree: bars on a baseline below, dotted drops; spacing J = twice each half-split |
| 17 | simulated 1H NMR of ethyl ethanoate and ethanol (figdata) | 143 | fixed | ok | at 400 MHz and 0.8 Hz lines the multiplets were invisible spikes and the singlet clipped: simulated at 90 MHz (field of the measured spectra), normalised |
| 17 | AI NMR spectrometer | 144 | ok | ok | batch 2: magnet, console |
| 17 | problem spectrum of ethyl butanoate (figdata) | 146 | ok | ok | 5 multiplets q/t/sextet/t/t at ledger shifts |
| 18 | pKa bar chart of the halogenated acids | 149 | ok | ok | values from the IUPAC dataset |
| 18 | resonance: ethanoate, phenoxide, amide | 149 | fixed | ok | \chemrel undefined in chemfig 1.6: \schemestart/\arrow{<->}; phenoxide charge para to C=O |
| 18 | geometries of carbocation, radical, carbanion | 150 | fixed | ok | carbanion R label ran into the caption line: labels lowered |
| 18 | curly arrows (heterolysis, proton transfer) | 151 | fixed | ok | chemfig bond naming needs -[@{b}]; second arrow crossed the upper scheme: routed below |
| 19 | SN2 scheme with curly arrows and transition state | 156 | fixed | ok | substrate (S) and product (R) checked by signed volume; nucleophile arrow crossed the H3C label: flattened |
| 19 | SN1 scheme and planar carbocation | 157 | fixed | ok | one-line scheme 36 pt too wide: split in two lines; water attacks both faces |
| 19 | SN2/SN1 energy profiles (figdata) | 157 | ok | ok | schematic, said so; one hump vs two, ionisation highest |
| 19 | comparison table | 158 | ok | ok | |
| 20 | E2 in Newman projection, anti-periplanar, curly arrows | 163 | fixed | fixed | back CH3 first on the same side as the front CH3 (gives Z, caption said E): moved; product drawing first showed the Z alkene: corrected to E |
| 20 | trans-diaxial Cl and H on a chair | 163 | ok | ok | Cl axial up on C1, axial H down on C2 and C6 |
| 20 | E1 scheme | 164 | ok | ok | tertiary cation, proton from a methyl |
| 20 | SN/E orientation table | 165 | ok | ok | |
| 21 | Grignard reagent solvated by two ether molecules | 168 | ok | ok | O->Mg dative bonds, tetrahedral Mg |
| 21 | Grignard apparatus (three-neck flask, condenser, drying tube, addition funnel, stirrer) | 169 | fixed | ok | tested on a scratch page first; right-neck stopper not aligned with the leaning neck: rotated |
| 21 | addition mechanism and work-up | 170 | fixed | ok | \ce{R''} breaks mhchem: math; the C-Mg arrow landed on the R' label: now arrives from the left |
| 21 | Grignard photo | 171 | ok | ok | PD |
| 22 | Williamson mechanism | 176 | fixed | ok | C-I arrow dipped into the caption: turned upward, space added |
| 22 | tosylation scheme | 176 | ok | ok | O-S bond formed, C-O untouched |
| 22 | tosylate retention then SN2 inversion | 177 | ok | ok | (S)-alcohol, (S)-tosylate, (R)-nitrile checked by signed volume (same geometry as ch. 19) |
| 22 | E1 dehydration of 2-methylbutan-2-ol | 177 | fixed | ok | caption touched the scheme: space; Zaitsev product trisubstituted |
| 23 | activation of an aldehyde by acid | 181 | ok | ok | protonated carbonyl and its carbocation resonance form |
| 23 | 5-hydroxypentanal and its cyclic hemiacetal | 182 | fixed | ok | caption touched the OH: space; 6-membered ring with O, OH on C1 |
| 23 | acetal mechanism in two lines | 182 | ok | ok | \ce{R'OH} arrow labels moved to math (mhchem prime trap) |
| 23 | Dean-Stark apparatus | 183 | ok | ok | heating mantle, flask, trap with water lower layer, condenser |
| 24 | AI wine cellar | 187 | ok | ok | batch 2: barrels in a vaulted cellar |
| 24 | oxidation-level ladder of the one-carbon family | 188 | ok | ok | -4, -2, 0, +2, +4 |
| 24 | safety box potassium dichromate | 189 | fixed | ok | six pictograms (Book 1's ghs:K2Cr2O7 row) overflowed at default size: 5 mm |
| 24 | borohydride reduction mechanism | 189 | ok | ok | B-H pair to C, pi pair to O, protonation |
| 24 | hydride chemoselectivity table | 189 | ok | ok | |
| 25 | HBr addition to propene with curly arrows | 193 | ok | ok | proton to CH2, secondary cation, 2-bromopropane |
| 25 | energy profiles via primary/secondary cation (figdata) | 194 | fixed | ok | primary-cation label sat on the dashed curve, reactant label clipped: moved |
| 25 | 1,2-methyl shift | 194 | ok | ok | secondary -> tertiary, chloride capture |
| 25 | bromonium ion and anti opening, meso product | 195 | fixed | fixed | first product drawing was (2R,3R), not meso: C3 wedges swapped, (2R,3S) checked by signed volume |
| 25 | Markovnikov portrait | 196 | ok | ok | PD 1905 |
| 26 | photo Atacama lithium ponds | 199 | ok | ok | NASA, PD; ponds of different colours |
| 26 | photos sodium in oil and flame colours | 200 | ok | ok | flame order Li, Sr, Ca, Na, Ba, B, Cu, Cs, K checked against the Commons description |
| 26 | Solvay flow sheet | 202 | fixed | ok | boxes too close, labels on box edges: spread, small labels; CO2 and NH3 loops, net 2NaCl + CaCO3 -> Na2CO3 + CaCl2; balance gate caught an unbalanced 2NaHCO3 -> Na2CO3 label: arrow in math |
| 26 | AI soda-ash plant | 202 | ok | ok | batch 3: towers, kilns, white stockpiles; no text |
| 26 | lime cycle | 203 | ok | ok | three steps, heat and CO2 in the right places |
| 26 | lithium production bar chart | 203 | ok | ok | USGS MCS 2026 estimates, order by size |
| 27 | AI fertiliser spreading | 207 | ok | ok | batch 3: tractor, white granules, wheat |
| 27 | photos bauxite, borax, quartz, white phosphorus | 208 | ok | ok | licences verified via the Commons API |
| 27 | SiO4 tetrahedron and chain silicate | 209 | ok | ok | chain shares two corners per tetrahedron |
| 27 | Haber-Bosch / Ostwald flow sheet | 209 | fixed | ok | NO label ran into the Pt-Rh box: spread; NO recycled loop |
| 27 | Haber portrait | 210 | ok | ok | Nobel Foundation 1919, PD; transcoded PNG -> JPEG |

### Corrections after the main-session spot-check (272-pp render)

The lines for ch5/ch6 3D cells and the ch14 iron diagram above were marked
clean on label overlaps only; the projected geometry had not been checked.
Rechecked by computing the screen projection of every atom and line, not by eye.

| ch | figure | page | layout | chemistry | note |
|---|---|---|---|---|---|
| 5 | FCC and BCC cells (correction) | 50 | fixed | fixed | old view 70/110: BCC main diagonal projected onto the front-face diagonal and the FCC face diagonal crossed the back-face centre; old omcube dashed the edges at (0,a,0) although the hidden vertex is the origin, and atoms were not drawn back to front. Now view 60/100, omcubeo (edges at the origin dashed), atoms sorted by depth; face diagonal (a,0,0)-(a,a,a) on the front face, main diagonal (a,0,0)-(0,a,a) through the centre, the two clearly distinct |
| 5 | HCP prism (correction) | 51 | fixed | ok | at 60/100 a B atom projected 0.1 units from the hidden bottom vertex at 180 deg (and the other hollow set onto the top vertex at 0 deg): own view 70/113 (min. screen distance 0.64 between any two atoms), omhexprismo hidden edges valid for it, atoms depth-sorted |
| 5 | octahedral and tetrahedral sites (correction) | 53 | fixed | ok | 60/100, depth-sorted; the "(red)"/"(blue)" labels crossed the front bottom corner atoms at the new view: lowered |
| 6 | NaCl and CsCl, ZnS and CaF2, diamond (correction) | 58, 60, 61 | fixed | ok | same view/pic/depth fix; no two sites closer than 0.18 a on screen; Zn/C bonds checked against the four tetrahedral neighbours of each site |
| 14 | E-pH diagram of iron (correction) | 127 | fixed | ok | rotated H2O/H2 label crossed the Fe(OH)2/Fe boundary near pH 12-13: moved to pH 2.2 above the dashed line |
| 10 | weekend-problem solution, answer 16 | - | - | fixed | answer for pH 12.57 now reads "about 12.6" (spot-check) |

| ch | figure | page | layout | chemistry | note |
|---|---|---|---|---|---|
| 28 | photo Kawah Ijen | 223 | ok | ok | CC BY-SA 4.0 (Sémhur), licence via the Commons API; sulfur deposits around the pipes, miners |
| 28 | contact-process flow sheet | 224 | ok | ok | burner -> converter (V2O5) -> absorber -> dilution; acid returned to the absorber; labels clear of arrows |
| 28 | photos chlorine, bromine, iodine | 225 | fixed | ok | at 3.4 cm the iodine photo wrapped to a second line: 2.9 cm, one row; colours match the caption |
| 28 | E° bar chart of the halogen couples (figdata standard-potentials) | 226 | ok | ok | 2.89 / 1.36 / 1.08 / 0.53 V, decreasing down the group |
| 28 | AI swimming pool | 226 | ok | ok | batch 3 image reviewed: pool, lane ropes, comparator kit (pink and yellow tubes); no letters; stub replaced |
| 28 | VSEPR shape table | 227 | ok | ok | SO2 119.5, ClF3 87.5, XeF2 180 from CCCBDB; XeF2 lone pairs equatorial |
| 29 | AI hot filtration (recrystallisation) | 230 | ok | ok | batch 3 image reviewed: goggles, gloves, coat, fluted paper, hot plate, needles in a dish; no letters |
| 29 | GHS pictogram grid (9 \ghs) | 231 | fixed | ok | one-line names made the table 13.7 pt too wide: code and name on two lines; names from the PubChem GHS summary |
| 29 | type A histogram + rectangular density (figdata type-a-uncertainty) | 233 | ok | ok | 20 illustrative readings, mean 12.455, s 0.071 drawn as the arrow; Gaussian area = histogram area (test); rectangular band at +-a/sqrt3 |
| 29 | simple distillation (shared pics) | 236 | fixed | ok | 'water in' label touched the receiver neck: moved left; water in at the low end, bulb level with the side arm, open at the receiver |
| 29 | TLC plate with Rf construction | 237 | fixed | ok | 'baseline' label sat on the d_A arrow: pin from below; Rf 0.30 and 0.65 measured from the baseline, front dashed |
| 29 | photo Kofler bench | 237 | ok | ok | CC BY-SA 3.0 (HBR), licence via the Commons API; reference-substance box visible |
| 29 | photo Abbe refractometer | 238 | ok | ok | CC BY-SA 4.0 (Foreade), PNG transcoded to JPEG on white |

### Phase C full re-check (all figure pages at 90 dpi, projected geometry and labels)

| ch | figure | page | layout | chemistry | note |
|---|---|---|---|---|---|
| 4 | hydride boiling points | 31 | fixed | ok | CH4 label sat on the x-axis corner: x range widened, label left of its point |
| 9 | one-step and two-step profiles | 73 | fixed | ok | "products" label crossed the curve end and the reactants label the start: re-anchored, ymin lowered |
| 10 | ethanoic acid distribution | 82 | fixed | ok | CH3COOH / CH3COO- labels on the crossing curves: moved to the lower corners |
| 11 | zinc and aluminium solubility panels | 94 | fixed | ok | aluminium log s label ran into the zinc panel: narrower panels, wider gap |
| 14 | copper E-pH, Cu2O sliver | 118 | fixed | ok | label straddled the lower Cu2O/Cu line: moved into the Cu domain with an arrow into the sliver |
| 15 | pH-metric titration set-up and curves | 124 | fixed | ok | electrode/stirrer labels floated: arrows to the parts; HCl label off the axis |
| 18 | curly arrows (heterolysis, proton transfer) | 151 | fixed | ok | lower arrow ran into the caption: space added |
| 19 | SN2 scheme, SN1 scheme | 156-157 | fixed | ok | "+" overlapped the curly arrow (spacer instead); SN1 tertiary centres drawn with 90-degree bonds so Br/OH no longer collide with a methyl |
| 20 | E1 scheme | 164 | fixed | ok | same 90-degree layout; space before caption |
| 21, 22, 23, 24, 25 | Grignard, tosylation, acetal, borohydride, rearrangement schemes | 170-194 | fixed | ok | schemes flush on the caption: space added |
| 23 | 5-hydroxypentanal and cyclic hemiacetal | 182 | fixed | fixed | ring had five bonds (open chain drawn): now *6, six-membered with O and the anomeric OH |
| 25 | HBr + propene profiles | 194 | fixed | ok | CH3CH2CH2+ label on the dashed curve: above it with a dotted pointer |
| 29 | GHS grid | 221 | ok | ok | "health hazard" pictogram name no longer term-linked |
| all others | - | - | ok | ok | rechecked: no further overlap, geometry or chemistry defect |

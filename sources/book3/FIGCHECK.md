# Book 3 — per-figure check

One line per figure (`omfigure`, `includegraphics`, history portrait),
checked on its own page rendered at 130 dpi, twice: layout and chemistry
(and projected geometry for 3D drawings). Pages are those of the build of the
check date; the Phase C pass re-checks every line after the term links.

| ch | figure | page | layout | chemistry | note |
|---|---|---|---|---|---|
| 1 | AI camping stove (b2-01-camping-stove) | 8 | ok | ok | blue flame under the pan; no letters (faint engraving on the valve too small to read) |
| 1 | methane enthalpy ladder | 11 | fixed | ok | ΔfH(CH4) label moved above the arrow; tick labels as math minus; levels in proportion (−74.9, −965.2) |
| 1 | Hess portrait (history) | 12 | ok | ok | CC BY-SA 4.0 credit in the box |
| 1 | bond-enthalpy table | 12 | ok | ok | values = thermo-data bonds |
| 1 | Born–Haber cycle NaCl | 13 | fixed | ok | relaid: elements path left, formation and lattice arrows apart; levels to scale; attachment arrow downwards |
| 1 | two-step flame path | 15 | fixed | ok | ΔH1 label off the dashed line; reaction step at T0 then heating |
| 1 | flame-temperature plot | 15 | fixed | ok | ticks every 500 K; intersections marked at 2401 K and 2329 K (= flame-temperature.py) |
| 1 | bomb calorimeter | 16 | ok | ok | bomb, cup, ignition wire, stirrer, thermometer pic, jacket |
| 1 | Berthelot portrait (history) | 17 | ok | ok | PD |
| 2 | AI cold pack (b2-02-cold-pack) | 20 | ok | ok | white pack squeezed, first-aid kit; no letters |
| 2 | zinc S°(T) plot | 21 | ok | ok | S(0)=0, monotone; jumps 10.6 at 692.7 K and 97.7 at 1180.2 K (= standard-entropy.py) |
| 2 | Gibbs portrait (history) | 24 | ok | ok | PD |
| 2 | calcite ΔrH and TΔrS lines | 25 | fixed | ok | Ti label moved off the ticks, region labels clear of the lines; crossing at 1110 K |
| 2 | sign chart 2 × 2 | 25 | ok | ok | four cases consistent with ΔG = ΔH − TΔS |
| 3 | AI salt spreader (b2-03-salt-spreader) | 30 | ok | ok | gritting truck, salt fan from the spinner; no letters |
| 3 | tangent construction (model V_m) | 31 | fixed | ok | model made more curved (−25 x(1−x)); tangent intercepts 14 and 49 = solution 1; labels off the curves |
| 3 | Raoult/Henry pressures (ideal, Margules) | 33 | fixed | ok | Henry slope e^1.1 = 3.00 (dotted), Raoult tangent dashed; p2 label moved below its curve |
| 3 | Raoult portrait (history) | 34 | ok | ok | PD |
| 3 | μ(T) of solid, liquid, solution | 35 | fixed | fixed | slopes were inverted (solid steeper): redrawn with the liquid steeper (S_l > S_s); T_f < T_f* now |
| 3 | osmosis U-tube | 36 | fixed | ok | liquids clipped to the tube; "solution" label off the dotted level line; water arrow towards the membrane |
| 4 | AI ammonia plant (b2-04-ammonia-plant) | 40 | ok | ok | night plant, columns, steam plume; no letters |
| 4 | G(ξ) of N2O4/NO2 | 41 | fixed | fixed | slope labels moved to the caption; the equilibrium dot was at −1.08, the computed minimum is −0.949: moved |
| 4 | van 't Hoff plot NH3 | 42 | fixed | ok | 1000 K label off the axis; dots below the 298-K line at high T (ΔrH more negative) |
| 4 | van 't Hoff portrait (history) | 43 | ok | ok | PD |
| 4 | Q/K shift arrow | 44 | ok | ok | forward when Q < K |
| 4 | Le Chatelier portrait (history) | 44 | ok | ok | CC BY-SA 4.0, printed card caption in the photograph (real document) |
| 4 | x(NH3) vs T at 1, 50, 200, 300 bar | 45 | fixed | ok | labels moved off the curves; 0.253 at 723 K/200 bar = vant-hoff.py |
| 4 | ammonia loop flow sheet | 46 | ok | ok | recycle from separator to compressor; purge on the recycle |
| 4 | Haber and Bosch portraits (history) | 46 | ok | ok | PD |
| 4 | SO2 conversion chart with beds | 47 | fixed | ok | x range widened (curve no longer outside the axis), labels off the lines; X falls with T (exothermic) |
| 5 | AI stirred-tank hall (b2-05-stirred-tanks) | 51 | ok | ok | motors and gearboxes on the vessels; no letters |
| 5 | three ideal reactors | 52 | fixed | ok | inlet/outlet labels moved off the tank walls; slice dV in the tube |
| 5 | conversion vs Damköhler | 54 | fixed | ok | "2.3" label removed (on the tick); 90 % at kτ = ln 10 and 9 (reactors.py) |
| 5 | Levenspiel chart | 54 | fixed | ok | plug-flow label moved out with an arrow; rectangle height 1/r(0.9) = 10 |
| 5 | Semenov diagram | 56 | fixed | ok | cold-state label was clipped; three states 300, 390, 430 K (reactors.py); middle unstable |
| 6 | AI tapping a blast furnace (b2-06-blast-furnace) | 53 | ok | ok | iron runner and suited workers; no letters |
| 6 | Ellingham diagram (13 lines) | 55 | fixed | ok | caption promised a table that did not exist: lines now labelled at the right end with leaders (clip mode individual); Zn and Mg breaks visible; HgO crosses 0 near 734 K; C/CO meets FeO near 1040 K, ZnO near 1216 K (ellingham.py) |
| 6 | thermite photo (PetrS.) | 56 | ok | ok | crucible over the rail joint, credited |
| 6 | Boudouard x(CO) vs T | 57 | fixed | ok | x ticks thinned (1 000 overlapped); CO2 label moved off the y tick and the curve; x = 0.5 near 950 K, 0.92 at 1100 K |
| 6 | blast furnace counter-current scheme | 58 | fixed | ok | charge and top-gas labels collided; tuyere arrow crossed the C + O2 label |
| 6 | Duisburg-Nord photo (Rabich) | 58 | ok | ok | shaft, hot-blast ring, credited |
| 6 | zinc hydrometallurgy flow sheet | 59 | fixed | ok | "cemen-tation" hyphenated inside the box; equations as text (balance gate) |
| 7 | AI copper pot stills (b2-07-pot-stills) | 70 | ok | ok | swan-neck pot stills, condensers behind; no letters |
| 7 | benzene-toluene isobaric + isothermal | 72 | fixed | ok | bubble/dew labels sat on the curves; tie line 0.405/0.626 at 95 °C, bubble 92.1 °C (liquid-vapour.py) |
| 7 | ethanol-water model + negative azeotrope model | 74 | ok | ok | azeotrope dot at 0.881, 77.9 °C (model); max at 0.29, 116.7 °C; both titled "(model)" |
| 7 | plate column scheme + refinery photo | 75 | fixed | ok | condenser label on the box, vapour and condensate on one line: redrawn; merged with the photo (gap) |
| 7 | McCabe staircase at total reflux | 76 | ok | ok | 7 steps from 0.95 to 0.034; equilibrium curve from Raoult |
| 7 | lab fractional distillation (Vigreux) | 77 | ok | ok | shared pics; bulb level with the side arm; water hoses implicit (as Book 2) |
| 7 | heteroazeotrope schematic | 78 | fixed | ok | L1+V label on the dew curve: moved out with a leader; dot enlarged |
| 7 | toluene-water steam distillation | 78 | fixed | ok | "water" label on the curve then under the dotted line: moved; 84.3 °C, ratio 4.1 (liquid-vapour.py) |
| 8 | AI soldering a circuit board (b2-08-soldering) | 75 | ok | ok | iron, wire of solder, fume; no letters |
| 8 | three cooling curves (schematic) | 76 | ok | ok | plateau / break + eutectic plateau / single plateau |
| 8 | Cu-Ni lens | 77 | fixed | ok | 1085 °C label sat on the curve start; formula brackets enlarged; tie line 0.541/0.609 at 1300 °C (solid-liquid.py) |
| 8 | benzene-naphthalene eutectic | 79 | fixed | ok | bottom labels collided with the eutectic line and ticks; region label with leader; E −3.5 °C, 0.133 |
| 8 | Pb-Sn diagram through NIST invariants | 80 | fixed | ok | L+(Sn) touched the liquidus; 18.9/96.6 sat on the dashed solvus; curves between invariants marked schematic in caption |
| 8 | Pb-Sn microstructure (schematic) | 80 | ok | ok | Commons search found no free-licence Pb-Sn micrograph: drawn instead |
| 8 | defined compound AB2 (schematic) | 81 | ok | ok | maximum at 2/3, two eutectics, regions labelled |
| 8 | Bi-Sn ideal vs assessed | 81 | fixed | ok | "assessed eutectic" label crossed the liquidus: moved with a leader; ideal 119.5 °C, assessed 138.8 °C |
| 9 | AI fuel-cell bus (b2-09-fuel-cell-bus) | 85 | ok | ok | roof tanks under fairing, water dripping; no letters or logos |
| 9 | cell as a thermodynamic system (signs) | 86 | ok | ok | work delivered nFU dξ, heat either sign |
| 9 | E°(T) liquid/vapour + efficiency vs Carnot | 88 | ok | ok | 1.229 and 1.185 V at 298 K; liquid falls faster (ΔrS −163 vs −44); crossing with Carnot near 1150 K (cell-thermodynamics.py) |
| 9 | energy bars per mol H2 | 89 | fixed | ok | axis unit sat under the third label: moved below the axis end; 285.8 = 237.1 + 48.7 = 135.1 + 150.7 |
| 9 | Faraday portrait (history box) | 89 | ok | ok | Phillips 1842, PD, credited |
| 9 | silver concentration cell | 90 | ok | ok | shared electrochemistry pics; dilute side anode; 59 mV |
| 10 | AI electroplating line (b2-10-electroplating) | 94 | ok | ok | parts on copper bus bars, PPE (glasses, gloves, apron); no letters |
| 10 | three-electrode set-up | 95 | ok | ok | WE/CE/RE wired to the potentiostat; no current through RE |
| 10 | fast vs slow model curves | 96 | ok | ok | equal-concentration couple; ηa, ηc arrows; same plateaus |
| 10 | diffusion-layer profile | 97 | fixed | ok | "cs = 0" label sat on the δ line: moved right |
| 10 | single-form wave + amperometric line | 98 | fixed | ok | ilim/2 label on the axis: moved; E1/2 at half height |
| 10 | walls of water (model) | 98 | fixed | ok | walls were clipped to fake plateaus (contradicting the text): unclipped with clip mode individual; 0/1.23 labels and H2O→O2 label moved off the axis and dotted line |
| 10 | Heyrovský (history box) | 99 | ok | ok | with dropping-mercury electrode; CC BY-SA 3.0, credited |
| 11 | AI aluminium potroom (b2-11-potroom) | 103 | ok | ok | long row of cells, crane, suited worker; no letters |
| 11 | zinc in acid, mixed potentials (model) | 104 | fixed | ok | y axis sat at E = 0 off the right edge: axis y line left; H+/Zn label crossed the copper curve: moved; −0.82 and −0.74 V (ie-curves.py) |
| 11 | cell operating point (model) | 105 | fixed | ok | "positive electrode" sat on the i axis: moved; U + rI between the two points at ±I |
| 11 | lead-acid accumulator (schematic) | 105 | fixed | ok | ± signs under the electron arrow and ion text over the plates: widened and relabelled |
| 11 | lithium-ion cell (schematic) | 106 | fixed | ok | shuttle labels cut by the separator line and bottom labels colliding: white-filled labels, separator label on top |
| 11 | voltaic pile (history) | 106 | ok | ok | museum pile, CC BY-SA 3.0 credited |
| 11 | zinc electrowinning curves (model) | 107 | ok | ok | Zn plateau before H+ on Zn (≈ −1.1 V), O2 at the anode |
| 11 | membrane chlor-alkali cell (schematic) | 108 | fixed | ok | cathode equation split across lines broke the balance gate: arrow as text |
| 11 | Hall–Héroult cross-section (schematic) | 109 | ok | ok | anodes in the bath, metal pad, cathode block; leaders |
| 11 | Hall and Héroult portraits (history) | 109 | ok | ok | both PD; country names removed from the text (gate 7) |
| 12 | AI rusty riveted bridge (b2-12-rusty-bridge) | 112 | ok | ok | rust streaks from rivets and joints; no letters |
| 12 | Evans diagram, iron in aerated water (model) | 113 | ok | ok | cathodic curve reflected; Ecorr on the O2 plateau |
| 12 | iron coupled to zinc / copper (model) | 114 | ok | ok | Zn shifts to −0.79 (iron protected); Cu doubles the plateau (ie-curves.py) |
| 12 | Evans drop (schematic) | 114 | fixed | ok | labels and equations sat on the rust arcs and O2 arrows: redrawn with labels outside |
| 12 | active-passive-transpassive (model) | 115 | ok | ok | peak, plateau, transpassive rise |
| 12 | copper statue patina | 116 | ok | ok | PD, credited |
| 12 | cathodic protection of a pipe (schematic) | 117 | fixed | ok | "current in the soil" sat on the pipe: moved below |
| 12 | consumed zinc anode on a hull | 117 | ok | ok | CC BY-SA 3.0, credited |
| 12 | scratch in galvanised vs tinned steel | 117 | fixed | ok | too small to read: scaled 1.35 (no pics in it) |
| 13 | Schrödinger (portrait panel) | 121 | ok | ok | Nobel Foundation, PD, credited |
| 13 | radial distributions + R2s, R3s | 123 | fixed | ok | 2s/2p and "3s, 3p" labels on the curves, "node" label on R: moved with a leader; rmax 1, 4, 9 a0; nodes 2, 1.90, 7.10 a0 (atomic-orbitals.py) |
| 13 | dot densities 1s, 2s | 123 | ok | ok | Halton sampling of r R^2 in a plane; 2s node ring dashed at 2 a0 |
| 13 | real orbitals s, p, d (new shared pics) | 124 | ok | ok | omp/omd* lobes, signs, axis letters |
| 13 | Slater constants table | 124 | ok | ok | 0.30 / 0.35 / 0.85 / 1.00 |
| 13 | Z* and radius along period 2 and group 1 | 125 | fixed | ok | "radius" label on the group curve: moved; Z* 1.30→5.85, 2.20 down the group |
| 14 | liquid oxygen deflected by magnets | 129 | ok | ok | low resolution but legible; PD |
| 14 | MO diagrams H2, He2 (modiagram) | 131 | ok | ok | series \setmodiagram defaults; bond orders 1 and 0 |
| 14 | σ/σ*/π/π* lobes (new shared pics) | 131 | ok | ok | facing lobes same colour for bonding, opposite for antibonding (checked sign by sign) |
| 14 | MO diagrams N2 (mixing) and O2 | 132 | fixed | ok | first stacked and overlapping (σ*2s on π; σ2p on π): side by side, 2p raised, levels spread; caption notes modiagram's x axis labels |
| 14 | period-2 diatomics table | 133 | ok | ok | re from WebBook, D0 from JANAF 0 K enthalpies (diatomics.py) |
| 14 | two-level E vs Δ/|β| | 134 | ok | ok | exact vs perturbative; splitting 2|β| at Δ = 0 (two-level.py) |
| 14 | CO valence orbitals (omlevel pics) | 134 | fixed | ok | MO labels sat on the correlation lines: moved left on white |
| 14 | Mulliken and Hund (history) | 135 | ok | ok | CC BY 3.0, credited; order per Commons description |
| 15 | water fragment diagram (omlevel) | 140 | fixed | ok | 1b1 drawn above the O 2p (a nonbonding level must stay at it): moved; long label and ionisation arrow crossed the correlation lines: removed (caption gives 12.62 eV) |
| 15 | methane fragment diagram | 141 | ok | ok | a1 + t2, two filled levels, 1t2 six electrons |
| 15 | ethene π, π*, twisted | 141 | ok | ok | omp lobes; twisted p in-plane, zero overlap |
| 15 | hyperconjugation in a carbocation | 142 | ok | ok | σC–H lobe parallel to the empty p; two-level scheme |
| 16 | butadiene π orbitals, lobes ∝ coefficients | 146 | ok | ok | signs checked orbital by orbital against huckel.py; 0–3 nodes |
| 16 | Frost circles C4H4, C5H5−, C6H6, C7H7+ | 147 | fixed | ok | only the lowest pair of electrons was drawn: filled degenerate pair added for the 6-electron rings |
| 16 | hydrogenation ladder | 148 | fixed | ok | labels on the reference dashes and bars: relaid beside the bars; 118.8, 227.7, 206.0; 150 kJ/mol (dfh:*_g) |
| 16 | Kekulé (history) | 149 | ok | ok | PD 1873 |
| 16 | polyene gap + computed level patterns | 149 | fixed | ok | bottom labels clipped; degenerate pairs merged into one bar: spacing widened |
| 17 | two-orbital interactions, 2 and 4 electrons | 153 | ok | ok | upper level rises more in the 4-electron case |
| 17 | Diels–Alder curly arrows | 154 | fixed | ok | first draft cramped, arrows on the double-bond lines: scaled, atoms numbered, arrows re-routed |
| 17 | HOMO(diene)/LUMO(dienophile) lobes | 155 | ok | ok | ψ2 coefficients ±0.602/±0.372; end lobes in phase |
| 17 | coefficients 1-methoxybutadiene / propenal (model) | 155 | fixed | ok | tick labels sat on the bars (axis in the middle): axis at bottom, zero line, x limits enlarged (huckel.py part c) |
| 17 | endo/exo approaches | 156 | fixed | ok | CH2 label collided with C=O labels: redrawn side view, CH2 bridge on top, carbonyls under (endo) or away (exo) |
| 18 | transition-metal solutions photo | 160 | ok | ok | colours match the description (Co red, dichromate orange, chromate yellow, Ni green, Cu blue, MnO4 violet); PD |
| 18 | chelating ligands en, ox, edta (chemfig) | 161 | fixed | ok | first draft had open rings and a garbled edta: rings with *5( ), edta as condensed skeleton |
| 18 | geometry gallery (shared pics) | 161 | fixed | ok | "trigonal bipyramid" label ran into the next: two lines; tetrahedron re-projected in the pic block |
| 18 | cis/trans, fac/mer, Δ/Λ | 163 | ok | ok | B positions checked: cis L1,L3; trans L1,L2; fac L1,L3,L5 (mutually cis); mer L1,L2,L3 |
| 18 | Werner (history) | 164 | ok | ok | PD |
| 19 | ruby, emerald, copper sulfate photos | 166 | ok | ok | credited in the caption; colours as described |
| 19 | dx2−y2 vs dxy among ligands | 167 | ok | ok | lobes at / between the ligand dots |
| 19 | CFSE vs dn + d6 high/low spin | 169 | fixed | ok | "high spin" label clipped at the top and "low spin" lost under the axis: moved; values from ligand-field.py (−2.4 Δo for low-spin d6) |
| 19 | splittings oct/tet/square planar | 169 | ok | ok | tetrahedral inverted and smaller; dx2−y2 far above in square planar |
| 19 | colour wheel | 170 | ok | ok | complement pairs red–green, orange–blue, yellow–violet |
| 19 | σ-only MO diagram of ML6 | 171 | fixed | ok | ligand donor levels sat at the height of the bonding eg pair and their electrons overlapped: raised and spaced; 1 + 3 + 2 bonding, t2g nonbonding, eg* |
| 19 | π-donor / π-acceptor effects on t2g | 172 | ok | ok | t2g pushed up by a filled π, down by an empty π* |
| 20 | AI pilot plant (b2-20-pilot-plant) | 175 | ok | ok | glass-lined (blue enamel) reactor, sight glass, chemist with glasses and gloves; screen without readable text |
| 20 | gallery of elementary steps | 177 | fixed | ok | first layout in 2×2 with step names overprinting the nodes: one step per row, names under the arrows, reverse steps in grey |
| 20 | Wilkinson hydrogenation cycle | 178 | fixed | ok | in/out arrows crossed the step labels: labels moved inside, arrows outside, precatalyst note in the centre; counts 14/16/18/16 e |
| 20 | Suzuki cycle | 178 | fixed | ok | same relayout; Pd(0) 14 e, Pd(II) 16 e |
| 20 | 2010 laureates photo (history) | 179 | ok | ok | Suzuki, Negishi, Heck left to right per Commons description; CC BY-SA 4.0 |
| 21 | AI epoxy glue (b2-21-epoxy) | 181 | ok | ok | two tubes, stick, card, nitrile gloves, cracked wooden bowl; no text |
| 21 | hydroboration–oxidation of propene | 183 | fixed | ok | intermediate drawn with a spurious H branch and overfull: alkylborane drawn plainly, B on C1, scheme narrowed |
| 21 | epoxidation by a peroxy acid | 184 | fixed | ok | epoxide closing bond struck through "CH": ring syntax with a set base angle |
| 21 | 2,2-dimethyloxirane openings | 184 | fixed | ok | branches written before the atom (invalid chemfig) gave garbled rings: redrawn; OCH3 on CH2 (base) vs on C (acid) |
| 21 | syn/anti butane-2,3-diols | 185 | fixed | ok | the two captions ran together: anti panel moved right, two lines; meso has the mirror plane |
| 21 | ozonolysis of 2-methylbut-2-ene | 185 | fixed | ok | substrate garbled and arrow label on the CH3: redrawn, arrow lengthened; propanone + ethanal |
| 22 | AI indigo vat (b2-22-indigo-vat) | 189 | defect | defect | colour sequence inverted (the part longest in air is yellow-green, the part just out is blue): caption avoids the claim; REGENERATE in batch A with a corrected prompt |
| 22 | model profile substitution vs addition | 190 | fixed | ok | labels on the axis and on the dashed curve: moved outside; first barrier highest, Wheland minimum, aromatic product below (aromatic-profile.py) |
| 22 | nitronium formation + nitration | 191 | fixed | ok | chemfig Wheland lacked the sp3 substituents and misplaced the charge: redrawn with a local TikZ pic (charge at C para to the sp3 carbon, double bonds 1=2, 4=5) |
| 22 | Wheland intermediates, methoxy vs nitro (para) | 192 | fixed | ok | same pic; oxonium structure C=O+ with all octets |
| 22 | Friedel and Crafts (history) | 193 | ok | ok | both PD; Crafts converted PNG to JPEG |
| 23 | AI fish stall with lemons (b2-23-fish-stall) | 205 | ok | ok | whole fish on ice, halved lemons; no text |
| 23 | pKa scale of nitrogen bases | 207 | fixed | ok | four labels near pKa 9–11 overlapped: leaders to a column of labels with values; values from the ledger |
| 23 | imine formation (chemfig) | 208 | ok | ok | hemiaminal then imine, reversible arrows |
| 23 | reactions of a diazonium salt | 209 | ok | ok | six products with reagents on the arrows |
| 24 | AI olive-oil soap bars (b2-24-soap-bars) | 213 | ok | ok | green bars on racks; no stamps or text |
| 24 | saponification mechanism | 214 | fixed | ok | overfull single scheme: split into addition–elimination and the final proton transfer |
| 24 | triglyceride saponification | 215 | fixed | ok | stacked C=O of the three esters overlapped: condensed O–CO–R, product RCOO− Na+ |
| 24 | reactivity ladder | 216 | ok | ok | chloride > anhydride > ester ≈ acid > amide; arrows labelled |
| 24 | Chevreul (history) | 217 | ok | ok | Maurin portrait, PD |
| 25 | keto–enol tautomerism | 220 | fixed | ok | label sat on the equilibrium arrow: arrow lengthened to 2.2 |
| 25 | enolate resonance | 221 | ok | ok | charge on CH2 then O, C=C moved; resonance arrow |
| 25 | aldol of ethanal | 222 | ok | ok | 4 carbons conserved, alkoxide → aldol → but-2-enal, −H2O labelled |
| 25 | Borodin, Claisen (history) | 223 | ok | ok | PD and CC BY-SA 4.0, credited |
| 26 | propenal resonance + Hückel charges/LUMO (figdata huckel d) | 216 | fixed | ok | third structure's C+H2 bond drew as a hyphen: atom rewritten C+H2; charges sum 0, C(O) +0.33 > Cβ +0.23; LUMO Cβ 0.66 largest |
| 26 | MeLi vs Me2CuLi on cyclohexenone | 217 | ok | ok | 1,2-adduct C7H12O tertiary allylic alcohol; 1,4-adduct 3-methylcyclohexanone; ring bonds counted (6) |
| 26 | Michael mechanism (malonate + MVK) | 218 | fixed | ok | (EtOOC)2CH condensed atom overprinted CH2: redrawn as CH with two EtOOC branches; overfull row: atom sep 1.6em; C 11 conserved |
| 26 | Robinson annulation to Wieland–Miescher ketone | 219 | fixed | ok | first nested-ring attempt put CH3 on a non-fusion carbon and C=C on the methyl-bearing fusion (chemfig nests on the NEXT bond): rebuilt and checked with lettered atoms; triketone C11H16O3, ketol, WMK C11H14O2; CH3 moved to 105° off the C=O |
| 26 | Robinson (history) | 220 | ok | ok | PD-Sweden-photo (Nobel 1947), credited |
| 27 | phosphonium salt and ylide | 223 | fixed | ok | Ph3P(+) via \chemabove drew a hyphen bond: charges as superscripts; CH3I + Ph3P → salt, BuLi → ylide ↔ P=C |
| 27 | Wittig through the oxaphosphetane | 224 | fixed | ok | overfull single row: split after the oxaphosphetane; 4-ring P–C–C–O closed with ring hooks |
| 27 | Z from non-stabilised, E from stabilised ylide | 225 | fixed | ok | rows stacked (too wide side by side): caption Left/Right → Top/Bottom; Z: Ph +120°, Et +60° from the C=C axis (same side); E: opposite sides |
| 27 | HWE to ethyl cinnamate | 225 | ok | ok | phosphonate anion between P=O and ester; (E) trans drawn; diethyl phosphate anion |
| 27 | method table (C=C forming reactions) | 226 | fixed | ok | booktabs not loaded: \hline; paragraph spacing after table |
| 28 | retrosynthetic tree (omretro arrows) | 231 | ok | ok | target C10H14O; (a) PhCHO + iPrMgBr, (b) PhMgBr + iPrCHO, FGI ketone ⇐ C6H6 + iPrCOCl; arrows point from target to precursors |
| 28 | synthons and equivalents (table) | 231 | fixed | ok | mhchem leading ^ charges unreadable: synthons written in \mathrm with \overset{+} |
| 28 | two-group disconnection map (table) | 232 | fixed | ok | overfull 8.9 pt: last-column entry shortened; table moved after the argument |
| 28 | overall yield vs steps (figdata overall-yield) | 234 | ok | ok | ρ^n for 0.95/0.90/0.80/0.70; legend colours checked at 300 dpi; 0.9^10 = 35 %, 0.7^10 = 2.8 % |
| 28 | Corey (history) | 234 | ok | ok | CC0 (VRT ticket), credited |
| 29 | Flory distributions + Carothers curve (figdata a, b) | 240 | fixed | ok | two 0.5\linewidth axes wrapped (caption said Left/Right): 0.46; w_x peaks near X_n; X_n = 1/(1-p) |
| 29 | radical polymerisation of styrene (equations) | 241 | fixed | ok | \sim spacing as a relation fixed with {\sim}; benzylic radical on CHPh; dots on the radical carbons; equations instead of fishhook arrows |
| 29 | Poisson vs Flory at X_n = 50 (figdata c) | 242 | ok | ok | Đ 1.02 vs 1.98 match the tests |
| 29 | tacticity of polypropene (chemfig wedges) | 242 | ok | ok | substituents on alternate carbons only; iso all wedges, syndio alternating, atactic irregular |
| 29 | modulus vs temperature (schematic, labelled) | 243 | fixed | ok | "rubbery plateau" and "cross-linked" labels collided: moved apart; transition label off the dotted line |
| 29 | AI pellets and fibres (b2-29) | 243 | ok | ok | reviewed: pellets, spinneret, godet rolls, no text |
| 29 | Carothers (history) | 244 | ok | ok | Commons PD-old (unknown photographer), credited |
| 30 | net charge vs pH + glycine fractions (figdata amino-acid-charge) | 248 | fixed | ok | legend covered the aspartic-acid then the lysine curve: moved above the axes; pI crossings 6.07/2.95/9.9 match the tests; Lys starts at +2, Asp ends at −2 |
| 30 | peptide-bond resonance | 248 | ok | ok | O− and N+ charges, C=N in the second structure |
| 30 | eggs frying (AI b2-30) | 249 | ok | ok | reviewed: whites opaque at the edges, translucent near the yolks, no text |
| 30 | D-glucose Fischer + Haworth α, β | 250 | fixed | ok | columns misaligned (tabular): minipages [c]; Fischer C2 R, C3 L, C4 R, C5 R; Haworth right→down, left→up, C5 CH2OH up; α C1-OH down, β up; C3-OH stub shortened off the back edge |
| 30 | phospholipid bilayer (schematic) | 252 | fixed | ok | gate 3: \foreach {0,...,9} → explicit list; heads out, tails in |
| 30 | A–T and G–C base pairs (chemfig + chemmove) | 252 | fixed | ok | hook closure: a hook after a branch bonded the branch atom (guanine N1–H drew H–C6): hook moved before the branch; Kekulé bonds checked (A: N1=C6, C2=N3, C4=C5, N7=C8; G: C6=O, N3=C2); 2 and 3 H-bonds donor→acceptor |
| 30 | Fischer (history) | 252 | ok | ok | Atelier Victoria c1895, PD-old, credited |
| 22 | indigo vat AI image regenerated (b2-22-indigo-vat-2) | 189 | fixed | ok | the first image had the colours inverted; the new one: just out of the vat yellow-green, longest in air blue; caption explains the oxidation |
| 31 | AI analytical laboratory (b2-31) | 255 | ok | ok | reviewed: LC stacks, solvent bottles, autosampler vials, safety glasses, no brand/text |
| 31 | bands migrating down a column (schematic) | 257 | fixed | ok | bands did not widen between snapshots: widths now grow with the distance travelled; less retained runs ahead |
| 31 | van Deemter curve (figdata chromatogram b) | 258 | fixed | ok | legend covered the H curve: moved outside; minimum (2 mm/s, 30 µm) marked where B/u = Cu |
| 31 | resolution 0.75/1.0/1.5 (figdata a) | 259 | fixed | ok | groupplots library not loaded: three plain axes; valley 27 % at R_s = 1, ~2 % at 1.5 (exercise 11) |
| 31 | GC and HPLC block diagrams | 260 | ok | ok | flow order gas→injector→oven column→detector→data; reservoirs→pump→injector→column→UV→data |
| 31 | Tsvet (history) | 261 | ok | ok | PD-old c1900, credited |
| 31 | problem chromatogram (figdata c, invented data) | 263 | ok | ok | t_M 1.0, theophylline 3.0 (w 0.18), caffeine 3.4 (w 0.20) as in the statement; σ = w/4 |
| 32 | AI fireworks (b2-32) | 265 | ok | ok | reviewed against the ledger lines: caption says yellow = Na atomic D line (589.0/589.6 nm), reds/greens mostly molecular (Sr 460.7, Ba+ 455.4 nm atomic lines are blue) |
| 32 | time-of-flight analyser (schematic) | 266 | fixed | ok | "grids, U" collided with the drift-tube caption: moved above |
| 32 | isotope clusters Cl, Cl2, Br, Br2, ClBr (figdata a) | 267 | fixed | ok | pgfplotsset was local to the first picture (build error): hoisted; zero bars filtered; 100:32, 100:64:10, 100:97, 51:100:49, 77:100:24 from the ledger abundances |
| 32 | EI spectra butan-2-one, 1-bromopropane (figdata b, c, WebBook) | 268 | fixed | ok | labels clipped at the frame: ymax 118, xmax 140; 43 base peaks; 122/124 1:1 |
| 32 | McLafferty of pentan-2-one (chemfig) | 268 | ok | ok | O, C, Cα, Cβ, Cγ, H ring with dotted H···O; products enol radical cation (58) + ethene |
| 32 | AAS spectrometer (schematic) | 269 | fixed | ok | boxes touching and I0→I label on the monochromator: spread out |
| 32 | Aston, Kirchhoff–Bunsen–Roscoe (history) | 270 | ok | ok | PD-Sweden-photo / PD-old; 1862 group photo, Roscoe's collection |
| 32 | problem spectrum, 1-bromo-3-chloropropane (figdata d, WebBook) | 272 | ok | ok | sticks = ledger row ms:bromochloropropane; cluster 14.5:18.6:4.4 matches 3.2:4.2:1 (test) |
| 33 | 13C shift chart (figdata nmr-spectra d) | 275 | ok | ok | measured shifts only (no unsourced ranges): ketone C=O 209, ester C=O 166.5/170.7, aromatic 128–137, C–O 61/66, alkyl < 46; reversed axis |
| 33 | decoupled + DEPT-135/90 of butan-2-one and ethyl benzoate (figdata a, b) | 276 | fixed | ok | first render: axes at 0.48 of a 0.49 minipage (tiny) and arrowed axis lines: width \linewidth, plain lines; signs: CH2 down, C absent, CH only in DEPT-90 |
| 33 | flow chart for unknowns | 276 | ok | ok | MS → DBE → IR → 13C/DEPT → 1H → candidates → check → structure, dashed loop back |
| 33 | problem decoupled spectrum of benzyl ethanoate (figdata c) | 279 | fixed | ok | ymin 0, bottom axis; six lines at the PubChem shifts; 128.24 tallest |
| 34 | AI water-testing laboratory (b2-34) | 280 | ok | ok | reviewed: sample bottles, pipetting with gloves and glasses, ICP-type instrument, no readable text |
| 34 | Student densities + 95 % table (figdata regression c, e) | 282 | ok | ok | table values computed by integrating the density; tests check ν = 1 and 2 against closed forms and monotone approach to 1.96 |
| 34 | lead calibration + residual plot (figdata a, b) | 284 | ok | ok | points on the fitted line; residuals ±0.0013 without pattern, zero line drawn |
| 34 | least-squares Hessian | 284 | fixed | ok | inline smallmatrix unreadable: displayed pmatrix |
| 34 | standard addition (figdata d) | 285 | fixed | ok | middle y axis put the 0.1 label under the line and a/b under the ticks: left axes, x = 0 drawn, a/b above; intercept −3.11 |
| 34 | Gosset (history) | 286 | ok | ok | 1908 photograph, PD-old / PD-US-expired |
| 35 | AI synthesis laboratory (b2-35) | 289 | ok | ok | reviewed: fume hoods, clamped flasks, glasses and gloves, no brand/text |
| 35 | reaction under nitrogen (threeneck, dropfunnel, condenser, thermometer, bubbler pics) | 290 | fixed | ok | first try: thermometer outside the flask and ice cubes over the flask: bulb now on the right-neck axis inside the liquid, cubes outside the bulb; N2 enters through the funnel top, leaves via condenser and bubbler |
| 35 | acid–base separation flow (sepfunnel pic) | 291 | fixed | ok | boxes 2.4 cm hyphenated names and arrow labels touched boxes: 3.0 cm, right column moved; NaHCO3 / NaOH / HCl order with recoveries |
| 35 | flash column, fractions and TLC (chromcolumn, testtube, tlcplate pics) | 293 | fixed | ok | TLC lanes labelled 1–4 against fractions 2,3,5,6 of the caption: relabelled; nonpolar (red) high Rf in early fractions |
| 35 | boiling temperature vs pressure (figdata vacuum-boiling) | 294 | ok | ok | curves through Tb (test); measured 7 and 13 mbar points within 2–3 K, not fitted |

## 130-dpi recheck (2026-10-03, after the main-session sample)

Every figure page (156 pages carrying the 188 figures, plus the problem pages with figures)
rendered on its own at 130 dpi (`pdftoppm -r 130 -f P -l P -singlefile`), read twice
(layout, then chemistry); zooms at 300-400 dpi where a detail was doubtful. Defects found and fixed,
each re-rendered and re-read on its own page:

| ch | figure | PDF p. | defect | fix |
|---|---|---|---|---|
| 5 | Semenov diagram | 61 | "cold, stable" on the blue removal line (main-session sample) | label moved into the empty area with a leader to the point |
| 11 | membrane chlor-alkali cell | 120 | anode half-equation over the anode plate and touching the membrane; cathode text touching the plate (sample) | both half-equations split onto lines, centred in their compartments; Na+ label lifted off the arrow |
| 11 | zinc electrolysis i-E | 120 | "H+ -> H2 on Zn" touching the blue curve (sample); "Zn2+ -> Zn, plateau" crossing the dotted -0.76 line; "0" tick label on the axis | two-line labels moved clear; 0 label offset |
| 1 | flame path diagram | 21 | Delta H1 label overprinted "products, T0" | label above the arrow, smaller, shifted left |
| 1 | flame-temperature curves | 21 | legend's methane entry struck through by the dashed 2657.6 line | legend above the axes in two columns |
| 1 | bomb calorimeter | 22 | "stirrer" leader ended outside the bath, off the rod | leader to the rod |
| 3 | partial molar volumes | 38 | V1 label inside the plot over the tangent | moved outside, left of the axis |
| 3 | chemical potential vs T | 40 | "RT ln x1" overprinted the solid and dashed lines | label below the lines with a leader |
| 4 | shift of an equilibrium | 49 | "before" collided with "forward/backward shift" labels | merged into the ln K tick label "(= ln Q before)" |
| 4 | ammonia loop | 51 | "recycle" label on the line, purge arrow from the loop corner, "fresh N2+3H2" touching the compressor | label above the loop, purge from the top line, longer feed arrow |
| 5 | three ideal reactors | 57 | "Qv, cA,0" touching the tank; "V, cA" overprinted by the stirrer shaft | longer inlet arrow; label beside the shaft on the tank colour |
| 7 | McCabe-Thiele steps | 81 | xD label on the 45-degree line | anchored left of the point |
| 7 | fractional distillation set-up | 82 | heating-mantle leader pointed to the bench; side arm of the head ended in a gap before the condenser | leader to the mantle; joint collar drawn at the junction |
| 8 | Cu-Ni lens | 89 | "1085 degC" over the solidus start | label shifted with a short leader |
| 8 | Pb-Sn diagram | 92 | "18.9" over the (Pb) solvus | moved left |
| 9 | heat bar chart | 101 | "kJ/mol" axis label under the 300 tick | moved to the arrow tip |
| 9 | concentration cell | 102 | voltmeter: red (+) terminal on the anode (-) side (chemistry: pole polarity) | terminal colours swapped: black on the anode, red on the cathode |
| 11 | zinc mixed potential | 116 | "H+ -> H2 on zinc" on the cathodic curve | two-line label in the empty quadrant |
| 13 | radial distributions | 135 | 2p, 2s and 3d labels on their curves | labels moved above their maxima |
| 13 | dot-density clouds | 135 | the two frames had different scales and the 2s cloud overflowed its panel | both axes `scale only axis` at the same size, spaced |
| 14 | CO MO diagram | 146 | MO labels (sigma, pi, "lone pair on C") collided with correlation lines | labels set under their levels, HOMO label shortened |
| 15 | water and methane fragment diagrams | 152-153 | 3a1/1b2 labels and levels overlapping; 1t2/2t2 labels on the lines; "H2 fragment" under a level | water levels spread, labels under levels, fragment name moved |
| 15 | hyperconjugation level scheme | 154 | "empty p" label on the correlation line | label to the left |
| 17 | Diels-Alder curly arrows | 166 | locant "2" on the C1=C2 arrow | moved off |
| 17 | frontier orbitals of diene and dienophile | 167 | chemistry: the LUMO lobes drawn with phases opposite to the HOMO at both ends while the figure says "in phase" | LUMO phases flipped: same sign facing at both ends |
| 19 | colour wheel | 182 | colour names overlapping the wheel | names anchored radially outside |
| 19 | octahedral LF MO diagram | 183 | "t2g (nonbonding)" and "6 bonding" over the correlation lines; Delta_o label on a line | labels under the levels; Delta_o on the other side |
| 20 | Heck cycle | 196 | "alkene binding" on the arc | moved inward |
| 22 | nitration scheme | 203 | chemistry: nitric acid drawn without its formal charges | N+ and O- added |
| 22 | energy profile | 202 | "ArH + E+" on the curve start | moved below the curve |
| 22 | Wheland comparison | 204 | the H/E labels of the methoxy row touched NO2 of the nitro row | rows spaced |
| 23 | pKa ruler | 209 | the four leaders to the 9.26-10.73 labels crossed | leaders re-ordered, uncrossed |
| 29 | radical polymerisation equations | 253 | propagation line: arrow touching the product | thin space after the arrow |
| 32 | 1-bromopropane EI spectrum | 280 | "41" label touching the 43 base-peak stick | label shifted left |
| 34 | standard addition | 297 | "a/b" sat on the dashed line | label under the arrow |

All other figure pages were correct in layout and chemistry on this pass.

# Book 4 — per-figure double check

One line per `omfigure` / `includegraphics`, each checked on its own page at
130 dpi (layout: no label on a label, line or arrow, nothing outside its box,
caption clear; chemistry/physics: arrows, ratios, curves, geometry).

| ch | figure | page | layout | chemistry | note |
|---|---|---|---|---|---|
| 1 | AI dye flasks (b3-01-dyes) | 9 | stub | – | grey stub until batch A lands; review then |
| 1 | box psi_n and densities | 11 | fixed | ok | n = 4 density clipped at ymax: raised to 18.4; n-1 nodes, levels n^2 |
| 1 | cyanine lambda vs j | 12 | fixed | ok | legend covered data: moved right of the axis; values = figdata (147/257/374, 474/603/732) |
| 1 | oscillator levels and psi_v | 13 | fixed | ok | "turning points" label sat on the x axis: moved with a leader; turning points at y = +-1 for v = 0; parities right |
| 1 | rigid-rotor ladder | 15 | fixed | ok | g labels overprinted: rewritten; gaps 2 and 4 = 2(J+1) |
| 1 | hydrogen radial functions | 16 | ok | ok | R20 node at r = 2a; R21(0) = 0 |
| 1 | tunnelling T(E) | 17 | fixed | ok | curves clipped at 1e-2: ymax 0.1; H above D, ratio 58 at E = V0/2 |
| 1 | Schrödinger photo (history box) | 17 | ok | ok | quotation replaced by a paraphrase (not verified verbatim) |
| 2 | p2 ML/MS table | 23 | ok | ok | 15 determinants, 1D + 3P + 1S |
| 2 | carbon configuration/terms/levels + zoom | 24 | fixed | ok | "x10^4" tick scaling removed; zoom inset overlapped the levels column: moved right; levels at ASD values, 3P at its barycentre 29.6 |
| 2 | sodium D doublet | 26 | fixed | ok | emission arrows recoloured (omfluo, downwards); D1 from 2P1/2, D2 from 2P3/2 |
| 2 | helium singlets/triplets | 26 | fixed | ok | 2K arrow sat on the 1s2s 1S label: moved left of the singlet column with a dotted guide; lines 2059 and 1083 nm within families |
| 3 | AI computing cluster (b3-03-cluster) | 30 | stub | – | grey stub until batch A lands |
| 3 | schematic PES contour map | 31 | fixed | ok | "minimum A" label touched the q1 axis: axis lowered; MEP passes through the saddle |
| 3 | STO-3G fit + HeH+ SCF history | 33 | fixed | ok | panels stacked vertically: widths 0.46; SCF energies decrease from above (variational iterates) |
| 3 | SCF flowchart | 35 | fixed | ok | "yes" label moved left of its arrow |
| 3 | H2 RHF curve vs Morse | 35 | fixed | ok | legend covered the guides: moved top-left; guide labels separated; RHF minimum 1.346 a0, rises toward -0.60 Eh at large R |
| 4 | Bentley snowflakes + AI symmetric objects | 41 | stub | ok | photo PD; AI stub until batch A |
| 4 | H2O / NH3 / BF3 symmetry elements | 43 | fixed | ok | BF3 sigma_v drawn thin: now thick mirror lines; NH3 planes through one N-H and bisecting the opposite angle |
| 4 | point-group flowchart | 45 | fixed | ok | cramped: node distances raised |
| 4 | methane in a cube (tikz-3dplot 60/100, omcubeo) | 45 | fixed | ok | first draft had a fifth H at (2,2,2) (wrong tetrahedron): removed; depth-sorted atoms; C3 through H and C; S4/C2 through face centres |
| 4 | stereograms C2v, C3v, D3h | 48 | ok | ok | 4, 6, 12 points = h; mirror lines at the right angles |
| 5 | NH3 hydrogen SALCs (top view) | 53 | ok | ok | a1 (1,1,1), e (2,-1,-1), e (0,1,-1); disc sizes follow coefficients |
| 5 | water MO diagram (xz plane) | 54 | ok | ok | 1b2 nonbonding = O 2p only; correlations by symmetry only |
| 5 | water normal modes | 55 | fixed | ok | bend arrows were not perpendicular to the bonds (wrong mode): redrawn closing the angle; O arrows moved off the atom; nu3 right H moves in along its bond, O right |
| 5 | CO2 synthetic IR/Raman | 56 | fixed | ok | labels clipped and legend on the 2349 band: ymax 1.3, legend right; bands at 667, 2349 (IR), 1333 (Raman) |
| 6 | ALMA antennas photo | 60 | ok | ok | CC BY 4.0 credited at caption end |
| 6 | CO rotational lines 30/300 K | 62 | fixed | ok | legend without line samples: removed, colours in caption; strongest J: caption corrected to 3<-2 at 30 K (was 2<-1) |
| 6 | HCl Morse curve + Birge-Sponer | 63 | ok | ok | levels between Morse turning points; De arrow to 42342 cm-1; BS gaps linear to v = 26 |
| 6 | HCl fundamental band | 64 | fixed | ok | 35/37 doublets invisible at HWHM 1.5: HWHM 0.5, finer grid; no Q branch; R closes up, P spreads |
| 6 | N2 rotational Raman + Raman scheme | 65 | fixed | ok | Rayleigh label clipped under the title: moved to caption; Stokes at positive shift; 6B first, 4B spacing, 2:1 alternation |
| 7 | AI tonic water + fluorite photo | 70 | ok | ok | blue glow, no text; fluorite CC BY 4.0 credited |
| 7 | displaced curves + FC sticks | 72 | fixed | ok | curves ran above the axis (clip off): clipped; labels moved off the curves; legend without samples replaced by colours in caption; vertical arrow from v=0 at fixed R |
| 7 | Jablonski diagram | 73 | fixed | ok | "fluorescence" label crossed by the IC wavy arrow: arrows moved; emission from lowest levels (Kasha); ISC dashed wavy |
| 7 | mirror-image absorption/emission | 73 | ok | ok | symmetric about 0-0 at 25000 cm-1 |
| 7 | quenching decays + Stern-Volmer | 74 | ok | ok | slopes 1/tau; SV slope 50 L/mol |
| 8 | AI MRI room + NMR laboratory photo | 79 | fixed | ok | first photo showed a national flag and an institution's name: replaced by a CC BY 2.0 laboratory view without legible logos |
| 8 | rotating-frame vectors (tikz-3dplot) | 81 | fixed | ok | panels too close (labels collided): spread; misleading rotation arc removed; 90x' takes M from z to +y' (dM/dt = gamma M x B) |
| 8 | FID and its spectrum | 81 | ok | ok | lines at 100/250 Hz, width 1/(pi T2) |
| 8 | inversion recovery and T2 decay | 82 | fixed | ok | legend over the flat T2 tail and the T1 ln2 label on the curve: moved |
| 8 | pulse sequences | 83 | ok | ok | echo after 2 tau |
| 8 | COSY + HSQC/HMBC of ethyl butanoate | 84 | ok | ok | cross peaks only between vicinal protons; HMBC 4.13 and 2.28 ppm to 173.6 ppm |
| 9 | AI: benchtop powder diffractometer | 87 | ok | ok | tube and detector on a goniometer circle around a flat sample; no text or logo |
| 9 | cubic P, I, F cells (tikz-3dplot) | 89 | fixed | ok | cells drifted vertically (shift along the 3D y axis): canvas xshift; labels touched the bottom nodes: lowered; F has the six face centres, I the body centre |
| 9 | Bragg's construction | 90 | ok | ok | parallel rays, the two red segments d sin(theta) on either side of the normal |
| 9 | Ewald construction | 91 | fixed | ok | the circle did NOT pass through the node G = (-1,2) the caption names: radius recomputed (1.625), G label moved off a node |
| 9 | computed powder patterns + Scherrer | 92 | fixed | ok | NaCl/KCl labels sat on the other trace: offset 1.35 and labels to the right; metals data stopped at 90 deg with Cu (311) cut: data to 100; Cu/W labels moved off the peaks; peak positions match Bragg for a = 564.06/629.29 pm, KCl all-odd absent |
| 9 | P2_1/c projection with glyphs | 93 | fixed | ok | glyph pics scaled by x=3cm (giant circles): pics now fixed in cm; signs moved to the right of the circles; 2_1 lines full length; four positions (x,y,z), (-x,1/2+y,1/2-z), (-x,-y,-z), (x,1/2-y,1/2+z) checked |
| 10 | Boltzmann staircase (schematic) | 100 | fixed | ok | J labels computed wrongly from energies: written out; bars re-computed as true populations of the four levels at kT = 2hcB and 10hcB (equal totals), centred on the levels |
| 10 | Boltzmann populations HCl / CO / I2 | 102 | fixed | ok | CO bars (3 x 41) unreadable: joined points; HCl J_max = 3 at 300 K; I2 v = 0 0.64 at 300 K, 0.26 at 1000 K |
| 10 | q_rot exact vs T/theta, q_vib of N2/Cl2/I2 | 103 | fixed | ok | Cl2 and N2 labels collided: moved above their curves; exact sum 1 at low T, parallel to T/theta + 1/3 |
| 10 | table of statistical entropies | 105 | ok | ok | parsed by test_sackur-tetrode against the script |
| 10 | photo: Boltzmann's tomb | 106 | ok | ok | S = k log W visible; CC BY-SA 4.0 credited |
| 11 | AI: liquid-hydrogen storage sphere | 110 | ok | ok | white sphere on legs, pipes, fence; no text or logo |
| 11 | heat capacities N2, Cl2, normal/equilibrium H2 + JANAF points | 112 | fixed | ok | H2 labels sat on the curves: moved; limits 3/2, 5/2, 7/2; equilibrium H2 peak 3.57 at 49 K; JANAF N2/Cl2 points on the curves to 1000 K, Cl2 above 7/2 at 3000 K (anharmonicity, said in caption) |
| 11 | equilibrium ortho/para fractions H2, D2 | 113 | ok | ok | H2 para -> 1/4, D2 ortho -> 2/3; half para near 78 K |
| 11 | ice proton disorder (square network) | 114 | fixed | ok | first random configuration too ordered (whole rows alike): loop-flip Monte Carlo (seed 1, 400 flips), ice rule asserted at every O; drawn larger |
| 11 | log K of I2 = 2I with JANAF points; K(H2+D2=2HD) | 115 | ok | ok | points on the line within 0.02; K -> 4, 3.26 at 298 K |
| 12 | AI: pharmacy shelf | 119 | ok | ok | blank bottles and boxes, blister packs; no readable label |
| 12 | collision cylinder (schematic) | 121 | ok | ok | hit B inside the cylinder radius d, missed B outside |
| 12 | LEPS H + H2 contour map, MEP, saddle | 122 | fixed | ok | valley labels were SWAPPED (x = r_AB small with r_BC large is H_AH_B + H_C): corrected, white-backed; saddle on the diagonal at 0.92 A, MEP joins both valleys at r_e |
| 12 | Eyring plots H/D with 95 % bands | 124 | fixed | ok | bands barely visible: caption says so (1 % scatter); parallel lines, D below H |
| 12 | ZPE energy profile (schematic) | 125 | fixed | ok | levels stuck out of a too shallow well and arrows crossed the curve: well redrawn with smooth plot, levels inside the walls, arrows left of the curve |
| 12 | max primary KIE vs T (C-H, N-H, O-H) | 125 | fixed | ok | labels on the curves and O-H clipped at 200 K: legend, ymax 50, round ticks; zoomed at 400 dpi to confirm legend colours (130 dpi made them look black) |
| 13 | chain cycle (schematic) | 132 | ok | ok | Br -> H with H2, H -> Br with Br2, initiation/termination/inhibition arrows |
| 13 | H2 + Br2 integration vs steady-state law | 132 | fixed | ok | rate ylabel collided with long tick labels: rate x 10^3; agreement < 1 % after t = 30 (test) |
| 13 | Lindemann fall-off | 134 | fixed | ok | k1[M] label sat on the curve: moved; limits k_inf and k1[M], [M]1/2 = k2/km1 |
| 13 | Michaelis-Menten curves + Lineweaver-Burk | 136 | fixed | ok | axis labels of the middle-axis LB panel misplaced/over ticks: nodes; competitive line meets the free one on the 1/v axis, uncompetitive parallel |
| 13 | Brusselator series, limit cycle, Lotka-Volterra orbits | 138 | fixed | ok | Y clipped at 4.6 and legend over the curves; outer trajectory and largest LV orbit clipped, LV orbits not closed (tmax 12 < period): axes enlarged, tmax 20, orbits 0.5/0.3/0.2 |
| 13 | photo: BZ spirals | 138 | ok | ok | CC BY 2.0 credited |
| 13 | T-jump relaxation | 139 | ok | ok | full equation on the exponential; tau = 156 us marked at 1/e |
| 13 | stopped-flow apparatus (schematic) | 139 | fixed | ok | "observation cell" label under the detector arrow: moved above-left |
| 13 | burst trace | 140 | fixed | ok | label on the curve: arrow label; amplitude 1.28 uM, slope 0.2 uM/ms |
| 14 | S0/S1 twist-angle curves (schematic) | 146 | fixed | ok | "E" used for both the axis and the isomer: axis "energy"; relaxation arrows cut through S0: drawn along it; axis label clashed with 180 deg tick |
| 14 | photostationary E/Z switching | 146 | ok | ok | pss 0.80 at 365 nm, 0.16 at 440 nm = formula (test) |
| 14 | Norrish II scheme (chemfig) | 147 | fixed | ok | stray \arrow(@c1--) removed; cyclobutanol OH and CH3 drawn on top of each other: [::+-40]; radical dot moved under C (it sat on the C-OH bond); arrow labels split; 1,2-dimethylcyclobutan-1-ol substituents on adjacent vertices |
| 14 | Cl/ClO cycle and Chapman cycle (schematic) | 149 | fixed | ok | Chapman labels overlapped the arcs: triangle redrawn with separate arcs |
| 14 | O3 build-up (Chapman +/- ClOx) and Leighton line | 149 | ok | ok | ODE limit = analytic steady state (test); 26 ppb at ratio 1.5 |
| 14 | AI: city under smog | 150 | ok | ok | brown haze, no text |
| 14 | photo: ozone hole 1998 | 151 | ok | ok | NASA public domain; date and DU scale are data legends (no logo) |
| 15 | AI: glucose meter | 154 | ok | ok | display blank, test strip with blood drop |
| 15 | double layer (schematic) | 156 | fixed | ok | potential curve drawn over the ions and the metal: separate phi axis below; Helmholtz plane dashed to the axis |
| 15 | Butler-Volmer and Tafel plots | 158 | fixed | ok | middle axes put tick labels and the eta label on the curves: ordinary axes with light zero lines; Tafel slope 118 mV/dec at alpha 0.5 |
| 15 | Cottrell profiles and i vs t^-1/2 | 159 | ok | ok | erf profiles; text corrected to 350 um at 16 s (was 400) |
| 15 | simulated CVs at 4 scan rates + quasi-rev; ip vs sqrt(v) | 160 | fixed | ok | legend over the waves: lower right; first simulation gave dEp 61 mV and ip 2.8 % low (2-point flux): 3-point flux, 600 nodes, Nernst c_O + c_R = c*: dEp 57.7 mV, ip = Randles-Sevcik to 0.01 % |
| 15 | three-electrode cell (schematic) | 161 | fixed | ok | pics in a scaled scope needed [transform shape] (gate); "counter" label on the wires: moved |
| 15 | stripping peaks + standard-addition line | 162 | ok | ok | x-intercept -4.26 = -c0 |
| 16 | photo: SEM of converter honeycomb | 167 | ok | ok | CC BY-SA 4.0 Galadrid; SEM data bar kept (scale bar 1.0 mm), no logo |
| 16 | physisorption/chemisorption curves (schematic) | 168 | fixed | ok | axis label on the curve and a stray tick mark: moved/removed; H + H curve labelled "towards" its asymptote |
| 16 | fcc(111)/(100) sites (schematic) | 168 | ok | ok | atop on an atom, bridge mid-pair, hollows at triangle/square centres (coordinates checked) |
| 16 | Langmuir, BET, BET plot | 171 | fixed | ok | ylabels of the middle and right panels collided with the neighbours: narrower panels, larger shifts; BET line recovers v_m 45.0, c 124 |
| 16 | LH/ER rates | 172 | fixed | ok | legend entries split by commas inside \legend (braces) and legend on the curves: outside right; maxima at K_A p_A = 1 + K_B p_B |
| 16 | volcano (qualitative) | 172 | fixed | ok | labels on the branches: moved under the volcano |
| 16 | AI: ammonia plant | 173 | ok | ok | columns, flare, spheres; no text |
| 17 | AI: mayonnaise | 177 | ok | ok | bowl, whisk, oil jug, egg shells; no text |
| 17 | sessile drop and Young's tensions (schematic) | 179 | fixed | ok | the arc drew a cap LARGER than a hemisphere (theta = 110) while the arrows showed 70: circle centre moved below the solid (theta = 70 = 90 - 20); gamma_SL and theta labels separated |
| 17 | gamma vs log c and kappa vs c with the CMC break | 181 | ok | ok | break at 8.2 mM (ledger SDS); area per molecule 0.6 nm2 |
| 17 | packing shapes (schematic) | 182 | fixed | ok | labels of neighbouring shapes overlapped: spacing widened |
| 17 | photo: sunbeams (Tyndall) | 182 | ok | ok | CC BY-SA 4.0 Kevin c higgins; no text |
| 17 | double layer around a particle (schematic) | 183 | ok | ok | Stern layer, slipping plane, diffuse ions |
| 17 | DLVO V/kT at 1, 10, 50, 200 mM | 183 | ok | ok | barrier 39 kT at 1 mM, 20 at 10, ~0 at 50 (critical 51 mM, test) |
| 17 | Schulze-Hardy ratios (schematic) | 184 | fixed | ok | had no caption: added |
| 18 | photos: ruby and emerald crystals | 188 | fixed | ok | captions under images of different heights misaligned: same height 4.2 cm; CC BY-SA 3.0 Lavinsky |
| 18 | d2 correlation diagram (Book 3 omlevel pics) | 190 | fixed | ok | upper weak-field T1g labelled (P); arrow touched "strong field": shortened; same-symmetry T1g lines do not cross |
| 18 | Tanabe-Sugano d3 and d8 (full diagonalisation) | 191 | fixed | ok | 4A2g/3A2g labels clipped at the axis: moved to the caption; ruby 29.0, emerald 27.1 lines; 4T2 = Delta exactly; 2E flat ~21 B |
| 18 | Jahn-Teller d9 levels + elongated octahedron | 193 | fixed | ok | pics in a picture with a scaled scope need [transform shape] (gate); eg -> a1g (down) + b1g (up), t2g -> eg (down) + b2g (up); 9 electrons, hole in b1g |
| 18 | chi T vs T (Curie, spin crossover), chi vs 1/T | 194 | fixed | ok | labels clipped (top, right): ymax 5.6 and a two-line label at left; T1/2 = 200 K at x = 1/2 (test) |
| 19 | ligand-field activation energies (sigma-only model) | 199 | fixed | ok | ycomb legend showed empty lines and bars below zero hid tick labels: legend replaced by caption colours, ticks at the bottom with a zero line; LS d6 4 Dq, d3/d8 2 Dq (test) |
| 19 | D and A energy profiles (schematic) | 201 | ok | ok | intermediates CN 5 / CN 7 labelled in the wells |
| 19 | trans-effect syntheses (chemfig) | 202 | fixed | ok | the transplatin product was drawn as PtCl(NH3)3 (wrong): Cl-Pt(NH3)(NH3)-Cl; rows spaced; cis product has NH3 on adjacent positions |
| 19 | Taube bridged intermediate (Book 3 omoctahedron pics) | 202 | fixed | ok | metal labels overlapped: anchored left and right; shared ligand position for the Cl bridge |
| 19 | Marcus parabolas and log k vs -dG | 203 | fixed | ok | in-plot labels sat on the dashed curve: removed, colours in the caption; crossing at the reactant minimum for -dG = lambda; maximum at 100 kJ/mol (test) |
| 20 | photo: ferrocene crystals | 209 | ok | ok | CC BY 4.0 Andrea Sella; a second candidate rejected (brand logo on the ruler) |
| 20 | CO sigma donation / pi back-donation (Book 3 omlobe, omp, omdxz) | 210 | fixed | ok | the CO pi* lobe facing the metal lobe had the OPPOSITE sign (no overlap): coefficients swapped, C and O lobes out of phase |
| 20 | Dewar-Chatt-Duncanson (omdxy, omp) | 212 | ok | ok | sigma: two p in phase; pi: out of phase, each matching the facing d lobe |
| 20 | sandwich + metallocene frontier levels | 212 | fixed | ok | electron arrows missing: \foreach variables passed unexpanded to omlevel (\ifx test fails) -> columns written out; nickelocene now one electron in each e1g* (the first draft put both in one orbital) |
| 20 | delta bond of [Re2Cl8]2- (tikz-3dplot) | 213 | fixed | ok | first view flattened lobes and labels sat on them: view 58/25, larger lobes, labels off to the left; lobes between the Cl axes, eclipsed, same signs face to face |
| 20 | isolobal series (schematic) | 214 | ok | ok | 1/2/3 frontier hybrids on both sides |
| 21 | AI b3-21-chemical-plant (opener) | 218 | ok | ok | process plant at dusk, columns and tanks, no legible text or logos |
| 21 | Wilkinson hydrogenation cycle (schematic) | 219 | ok | ok | 14 -> 16 (OA, Rh I -> III) -> 18 -> 16 -> RE back to 14; precatalyst 16 off-cycle |
| 21 | methanol carbonylation cycle (schematic) | 220 | fixed | ok | the two organic steps collided with "migratory insertion" -> moved below the cycle; counts 16/18/16/18 checked |
| 21 | Chauvin mechanism (chemfig) | 221 | fixed | ok | "[M]" read as a chemfig angle (pgfmath "Unknown function M") -> M; ring closed with ? hooks; metallacycle touched caption -> space added; partners swap correctly |
| 21 | Suzuki-Miyaura cycle (schematic) | 222 | fixed | ok | Ar' inside \ce is an mhchem error -> math; OA, transmetalation, RE in order |
| 21 | Cossee-Arlman steps (schematic) | 222 | fixed | ok | first chemfig draft drew a bond to an empty phantom atom -> plain TikZ; vacant site moves to the chain's old side after insertion |
| 21 | Schulz-Flory distribution (pgfplots, figdata) | 223 | fixed | ok | legend and Mn label sat on the mass curve -> label shortened, value in caption; mass fraction peaks at Mn, dashed line at 28 kg/mol |
| 22 | AI b3-22-solar-panels (opener) | 227 | ok | ok | rooftop panels, cell grid plausible, no text |
| 22 | Hückel chain levels and DOS (pgfplots, figdata band-chain) | 228 | ok | ok | levels symmetric about alpha, N = 2 gives alpha +/- beta, band edges at +/-2|beta|, DOS diverges at the edges |
| 22 | band filling metal/semiconductor/insulator (schematic) | 229 | fixed | ok | E_g labels sat on the E_F lines -> moved up the arrows; E_F inside the band for the metal, mid-gap otherwise |
| 22 | intrinsic n_i of Si/Ge and doped-Si regimes (pgfplots, figdata semiconductor-carriers) | 230 | fixed | ok | right panel's y label ran into the left plot and the "intrinsic" note was clipped -> narrower panels, wider gap, note moved; Ge above Si, plateau at 1e15 |
| 22 | donor and acceptor levels (schematic) | 231 | ok | ok | electron promoted from donor level, hole left in valence band; caption says not to scale |
| 22 | photo silicon boule (Wallroth, PD) | 231 | ok | ok | cropped to the boule and cell, label text not legible at print size |
| 22 | Schottky and Frenkel defects (schematic) | 232 | fixed | ok | first draft's "anion" vacancy sat on a cation site (parity) -> moved to (3,2); \par used as a pgfmath macro name -> \pty |
| 22 | zirconia oxygen sensor (schematic) | 235 | fixed | ok | electrolyte too narrow, rotated label crossed the O2- arrow -> wider slab, label horizontal; O2- moves air -> exhaust, reduction on the air side |
| 23 | photo aerogel flower (NASA/JPL, PD) | 238 | ok | ok | slab, flower and flame; no text |
| 23 | sol-gel hydrolysis and condensation (chemfig) | 239 | fixed | ok | second scheme ran into the first and its arrow label touched the species -> space and longer arrows; Si four-coordinate, R generic |
| 23 | AI b3-23-autoclave (hydrothermal) | 240 | ok | ok | steel body, bolted lid with seal, PTFE liner, crystals; no text |
| 23 | perovskite ABO3 cell (tikz-3dplot, omcubeo) | 241 | ok | ok | view 60/100, atoms depth-sorted (0.853x + 0.150y + 0.5z); B at centre, six O at face centres, octahedron edges, A at corners |
| 23 | 2D crystal vs glass network (pgfplots, figdata glass-network) | 242 | ok | ok | test: crystal all 6-rings; glass 6 five- and 6 seven-membered rings, every former 3-coordinate, bonds within 15 %; NBO pairs with Na between |
| 23 | sodalite cage + MOF layer (tikz-3dplot + schematic) | 243 | fixed | ok | hidden edges computed from face normals for view 55/135 (no face within 0.33 of edge-on); Si/Al alternate (bipartite graph); MOF linkers drawn as circles -> hexagons, panel scaled |
| 23 | surface fraction and confinement energy (pgfplots, figdata nanoparticle-size) | 244 | ok | ok | 13/55/147 magic numbers tested; fraction 0.5 near 2.6 nm, 0.21 at 7.8 nm as the caption says; 1/R^2 |
| 23 | graphene chiral vector (schematic) | 245 | fixed | ok | labels sat on the lattice -> white boxes; zigzag along a1, armchair at 30 degrees, C_h = 4a1 + 2a2 drawn to scale |
| 23 | photo Lycurgus cup (Nguyen, CC BY 2.5) | 246 | ok | ok | transmitted-light view, matches caption |
| 24 | photo horseshoe crab (Kaldari, CC0) | 249 | ok | ok | dorsal view of Limulus, no text |
| 24 | haem iron edge-on, deoxy vs oxy (schematic, displacement to scale) | 251 | fixed | ok | Fe label hidden under the porphyrin line in the oxy panel -> moved below; caption said "to scale in the vertical direction" though His and O2 are schematic -> reworded; 0.34 A arrow = 0.51 cm at 1.35 cm/A |
| 24 | O2 saturation curves and Hill plot (pgfplots, figdata oxygen-binding) | 252 | fixed | ok | Hill-plot x label sat on the tick labels (axis lines=middle) -> left axes with a zero line; Hb label moved off the curve; zero crossings at log p50 (-0.43, 0.54), slopes 1 and 2.7 |
| 24 | carbonic anhydrase cycle (schematic) | 253 | ok | ok | Zn-OH2 -> Zn-OH- (-H+) -> Zn-OCO2H- (+CO2) -> back with H2O, -HCO3-; charges consistent |
| 24 | Kok cycle S0-S4 (schematic) | 254 | ok | ok | four photon steps, O2 released S4 -> S0 with 2 H2O bound |
| 24 | cisplatin 1,2-GG cross-link (schematic) | 255 | ok | ok | Pt to N7 of two adjacent G on one strand, two cis NH3 |
| 25 | 18-crown-6 with K+ and [2.2.2]cryptate (schematic) | 261 | fixed | ok | node names with decimals (oa-1.25) broke pgf -> lettered names; 18-ring has 12 C corners and 6 O; cryptand: 3 chains of 2 O between N bridgeheads |
| 25 | titration isotherms and Job plots (pgfplots, figdata binding-titration) | 262 | fixed | ok | legend sat on the K = 1e2 curve with wrong line samples -> direct labels; Job maxima at 0.5 and 1/3 (tested) |
| 25 | cyclodextrin cone with guest (schematic) | 263 | ok | ok | wide rim secondary OH up, narrow rim primary OH down, guest in the cavity |
| 25 | template synthesis of a catenane + rotaxane (schematic) | 264 | fixed | ok | first draft showed two overlapping circles, not interlocked -> over/under crossings drawn with a white gap |
| 26 | AI b3-26-terrace (opener) | 268 | ok | ok | person reading in sunlight, bare arms and legs, no legible text |
| 26 | HOMO lobes of butadiene and hexatriene, con/dis arrows (omp, figdata polyene-mo) | 269 | ok | ok | lobes scaled by the Hückel coefficients (0.60/0.37, 0.52/0.23/0.42); termini opposite (butadiene) and equal (hexatriene); arrows both clockwise vs opposite |
| 26 | orbital correlation diagrams dis/con (omlevel, omcorr) | 271 | fixed | ok | the two panels overlapped (cyclobutene labels on the second panel's butadiene labels) -> narrower panels, wider gap; S/A labels match the tested parities |
| 26 | [4+2] vs [2+2] phase matching (omp) | 272 | ok | ok | facing lobes same colour at both ends for [4+2], one mismatch for [2+2] |
| 26 | Cope and Claisen chair TS (schematic) | 273 | fixed | ok | first drawing was a flat hexagon -> chair from projected 3D coordinates (alternating +-0.25); 3-4 breaking, 1-6 forming, O at 3 for Claisen |
| 26 | vitamin D sequence (schematic on ring B atoms) | 274 | fixed | ok | C9 label hidden under the arrow and the CH2 label -> moved; bonds: 5=6/7=8 -> 10=5/6=7/8=9 -> 19=10/5=6/7=8, H from C19 to C9 |
| 27 | photo pyrethrum daisies (Soramimi, CC BY-SA 4.0) | 277 | ok | ok | Tanacetum flowers, no text |
| 27 | C-H BDE bar chart (pgfplots, figdata bde) | 277 | ok | ok | 439/422/411/405/376 = formula from the ledger rows (tested), order methyl > 1 > 2 > 3 > benzylic |
| 27 | tin hydride chain (schematic) | 278 | fixed | ok | first cycle drew R. -> Bu3SnH as a step (wrong species) -> two-carrier loop Bu3Sn. <-> R. |
| 27 | 5-exo vs 6-endo of the hex-5-enyl radical (schematic) | 279 | fixed | ok | C1-C5 left open (no bond before cyclisation); 5-exo label sat on the 6-endo arrow -> moved; product radical label "CH2." with a stray dot -> .CH2 |
| 27 | radical clock fraction and inverse plot (pgfplots, figdata radical-clock) | 280 | ok | ok | half cyclised at kc/kH = 0.096 M; line through origin, slope kH/kc = 10.4 (tested) |
| 27 | singlet/triplet carbene boxes (\omorbs) | 280 | ok | ok | singlet: pair in sp2, p empty; triplet: one in each, parallel |
| 27 | Skell test (chemfig) | 281 | fixed | ok | first draft drew trans-but-2-ene and a flat cyclopropane -> cis alkene and both methyls on wedges; space before the caption |
| 27 | Beckmann and Baeyer-Villiger ring expansions (chemfig) | 282 | ok | ok | 6-ring oxime -> 7-ring lactam with N-H next to C=O; ketone -> 7-ring lactone with O next to C=O; bond counts checked |
| 28 | AI b3-28-api-plant (opener) | 286 | ok | ok | glass-lined reactors, operator in clean-room suit, no legible text |
| 28 | ee vs ddG and chiral chromatogram (pgfplots, figdata er-ddg) | 287 | fixed | ok | temperature labels sat on the curves -> stacked labels in the empty area; areas 97.5/2.5 integrate to ee 0.95 (tested) |
| 28 | Re/Si faces of acetophenone (schematic) | 288 | fixed | ok | side notes ran into the CH3 label -> moved right; O(1) 90, Ph(2) 210, CH3(3) 330 deg: counterclockwise = Si front |
| 28 | Felkin-Anh Newman projection (schematic) | 289 | ok | ok | L perpendicular (90), S at 210 beside the Nu path at 250, M at 330, O at 0 |
| 28 | kinetic resolution ee vs conversion (pgfplots, figdata kinetic-resolution) | 290 | fixed | ok | curve labels sat on the dashed curves -> legend outside; legend samples checked at 300 dpi (thin look at 130 dpi is antialiasing); Kagan s recovered (tested) |
| 28 | Sharpless mnemonic (schematic) | 291 | ok | ok | CH2OH lower right; L-(+)-DET from below, D-(-)-DET from above |
| 28 | proline enamine aldol TS (schematic) | 292 | fixed | ok | first sketch had stray zero-length bonds and a floating "-H" -> redrawn: pyrrolidine N, enamine C=C, CO2H H-bonded to the aldehyde O, dashed C-C |
| 29 | AI b3-29-coffee (opener) | 297 | ok | ok | cup of coffee and roasted beans, no text |
| 29 | pi systems of pyridine and pyrrole (omp, oblique) | 298 | fixed | ok | first draft: ring path drawn half by a \foreach inside the path, lobes on top of the ring and the lone pair on a p lobe -> lobes first, explicit ring, N at 0 deg with the in-plane lobe outwards; caption no longer names a lobe colour |
| 29 | 1H NMR of pyridine, pyrrole, furan (pgfplots, figdata heterocycle-nmr) | 299 | ok | ok | lines at the ledger shifts, 2:1:2 and 2:2 areas (tested), broad NH of pyrrole |
| 29 | SNAr of 2-chloropyridine with Meisenheimer complex (generated TikZ) | 300 | ok | ok | C2 sp3 with Cl and Nu, minus on N; Kekule rings restored after |
| 29 | Wheland cations of pyrrole C2 vs C3 (generated TikZ) | 300 | fixed | ok | the second structure's charge sat on the first's E label -> wider spacing, charges inside the rings; 3 vs 2 structures, bonds checked one by one |
| 29 | G-C base pair (schematic) | 301 | ok | ok | three H bonds O6...H-N4, N1-H...N3, N2-H...O2 |
| 29 | Fischer indole sequence (chemfig) | 302 | ok | ok | hydrazone -> ene-hydrazine (=CH2) -> 2-methylindole (N-H, C2-CH3, C2=C3); ring bond counts checked |
| 30 | photo Pacific yew bark (JOE BLOWE, CC BY-SA 2.0) | 306 | ok | ok | flaking bark and needles of Taxus brevifolia, no text |
| 30 | overall yield vs steps, linear and convergent (pgfplots, figdata overall-yield) | 307 | ok | ok | 0.9^20 = 12 %, convergent 0.9^(m+1) above linear (tested); legend checked |
| 30 | linear vs convergent route trees (schematic) | 308 | ok | ok | 6 steps LLS 6; 5 steps LLS 3 |
| 30 | Robinson tropinone (schematic) | 309 | fixed | ok | the arrow's lower label ran into the reactants -> moved; bicyclo[3.2.1]: N bridge C1-C5, CH3 on N, C=O at C3, two-carbon bridge broken behind the N-CH3 |
| 30 | Corey PGF2a retrosynthesis (omretro boxes) | 310 | fixed | ok | arrow labels collided with the boxes -> wider spacing, labels below |
| 30 | oseltamivir from shikimic acid (flow) | 310 | fixed | ok | "acetylation, reduction" label sat between boxes -> below the arrow |
| 31 | AI b3-31-biorefinery (opener) | 314 | ok | ok | tanks, column, maize field, wind turbines; no text or logos |
| 31 | AE and minimum E-factor bars (pgfplots, figdata green-metrics) | 316 | ok | ok | 40 / 77 / 25 / 100 % from book molar masses (tested against 206/514.5, 206/266, 44/173.1); E_min = 1/AE - 1 |
| 31 | LCA stages and boundaries (schematic) | 317 | ok | ok | cradle-to-gate encloses extraction and production; cradle-to-grave everything |
| 31 | ammonia loop with recycle and purge (schematic) | 318 | ok | ok | make-up -> mixer -> compressor -> converter -> separator; liquid NH3 out; recycle back to mixer, purge off the recycle |
| 32 | photo algal bloom (USGS/NASA Landsat 8, PD) | 322 | ok | ok | bloom swirls on a lake with farmland; no labels |
| 32 | carbonate fractions and rain pH (pgfplots, figdata carbonate-system) | 324 | ok | ok | crossings at 6.35 and 10.33, rain pH 5.6 at 425.6 ppm (tested) |
| 32 | BOD curve and oxygen sag (pgfplots, figdata bod) | 325 | fixed | ok | L0 label clipped at the top and BOD5 label on the curve -> moved; sag minimum at 2.4 d (tested) |
| 32 | nutrient flows into a lake (schematic) | 326 | fixed | ok | "N, P runoff" label ran into the lake box -> shortened |
| 32 | level-I compartments (schematic) | 327 | ok | ok | each compartment tied to water by its K |
| 32 | dose-response curves with NOAEL/LOAEL (pgfplots, figdata dose-response) | 328 | fixed | ok | n = 6 label on the curves and NOAEL label on its dot -> moved; both curves cross 0.5 at 200 mg/kg (tested); NOAEL 80, LOAEL 160 with the 5 % criterion |
| 33 | AI b3-33-glovebox (opener) | 333 | ok | ok | stainless glovebox with antechamber and gloves, fume hood behind; gloves bulge outwards as under the usual slight overpressure; no text |
| 33 | Schlenk line schematic (rbflask, bubbler pics) | 334 | fixed | ok | "inert gas" label sat on the inlet arrow -> moved; taps join gas and vacuum manifolds, trap before the pump, bubbler on the gas end, side arm into the flask neck |
| 33 | cannula transfer (rbflask, septum pics) | 335 | ok | ok | cannula tip below the liquid in the source, above it in the receiver; gas in to source, vent from receiver |
| 33 | photo Schlenk line (Polimerek, CC BY-SA 3.0) | 336 | ok | ok | glass manifold, taps, tubing, regulator; reagent labels not legible |
| 33 | characterisation workflow (flowchart) | 336 | ok | ok | purity -> formula -> structure -> X-ray -> report; "no" loops back through purification |
| 33 | qNMR spectrum (pgfplots, figdata qnmr) | 337 | fixed | ok | OCH3 label clipped by the axis then on the ferrocene peak -> right of its peak, clip off; areas 10:3:9 x amounts (tested), purity formula recovers 98.0 % |
| 33 | hierarchy of controls (inverted pyramid) | 338 | ok | ok | elimination at the wide top, PPE at the narrow bottom |

## Phase C re-check (2026-10-03, all 405 pages at 72 dpi, suspects at 130-300 dpi)

| ch | figure | page | verdict | fix |
|---|---|---|---|---|
| 7 | tonic water + fluorite photos | 73 | fixed | widths gave different heights, the pair looked misaligned -> both at height 4.6 cm |
| 9 | problem heading | 98 | fixed | heading orphaned (box of exactly one page moved on) -> clearpage + enlargethispage |
| 10-33 | problem headings | -- | fixed | `\section{Problem: <Title>}` was missing from ch10 on (series convention, book_style.md item 8) -> added; ch17 and ch26 orphaned -> clearpage + enlargethispage |
| 13 | stopped-flow apparatus | 140 | fixed | "observation cell" overprinted "mixer", then "stop syringe" -> labels moved |
| 15 | three-electrode cell | 162 | fixed | "counter" label crossed the counter wire -> rotated beside it |
| 16 | volcano plot | 173 | fixed | the two notes touched the rising and falling lines -> lowered |
| 22 | donor/acceptor levels | 231 | fixed | promotion arrows crossed the level labels -> moved left |
| 25 | cyclodextrin | 263 | fixed | guest label sat on the wide rim -> above it |
| 27 | hex-5-enyl cyclisation | 279 | fixed | double radical dot at C1 -> one |
| 28 | Sharpless mnemonic | 291 | fixed | substituents drawn on the wrong carbons (R1 on C3) -> C2 bears R1 and CH2OH, C3 bears R2 and R3; arrows to the C=C midpoint |
| 30 | Corey retrosynthesis | 308 | fixed | boxes ran past the right margin -> two-line boxes |
| all | index | -- | fixed | overfull \vbox in the index (imakeidx multicol) -> \indexspace shrink in the entry file, as Books 1-2 |
| all | layout | -- | fixed | stretched mid-page gaps above unbreakable figures -> \raggedbottom in the entry file, as Book 3 |

## 130-dpi recheck (2026-10-03, main-session request): all 199 figures, each rendered on its own page crop at 130 dpi, checked once for layout and once for chemistry

| ch | figure | page | verdict | fix |
|---|---|---|---|---|
| 6 | N2 rotational Raman + scattering scheme | 69 | fixed | "Rayleigh" label sat between the excitation and Rayleigh arrows -> left of them |
| 7 | Jablonski diagram | 76 | fixed | T1 -> S0 ISC arrow started past the end of the T1 level and its label crossed it -> from the level, label above-left |
| 11 | Cv of N2, Cl2, H2 | 113 | fixed | "N2" label sat on the N2 data points -> above-left |
| 11 | ortho/para fractions | 114 | fixed | "para fraction of H2" label sat on the curve -> moved right |
| 14 | Norrish type II scheme | 148 | fixed | second chemfig line touched the first -> space between schemes |
| 15 | double layer | 157 | fixed | potential drawn as positive for a negatively charged metal -> axis and curve labelled |phi|, caption says the potential is negative; curve made continuous at the Helmholtz plane |
| 15 | Butler-Volmer / Tafel | 160 | fixed | "slope 1/(118 mV)" label sat on two curves -> leader line from clear space |
| 15 | cyclic voltammograms | 161 | fixed | legend covered the cathodic branches at the lower right -> upper left |
| 16 | H2 physisorption/chemisorption | 169 | fixed | "crossing" label sat on the red curve -> leader from clear space |
| 16 | volcano plot | 173 | fixed | side notes touched the lines and the y axis -> above the lines, clear of the axis |
| 17 | zeta-potential particle | 182 | fixed | one diffuse-layer ion overprinted the "slipping plane" leader -> moved |
| 18 | Tanabe-Sugano d3 and d8 (main session's finding) | 192 | fixed | grey curves ran through the 4T1g(P), 4T1g, 4T2g, 2Eg labels and the d8 labels -> labels outside the frame at the height where each curve leaves it (clip mode individual), ruby/emerald labels at the foot of their lines; content re-checked: 4T2g = Delta, 4T1g(F) 50.9 B at 40 B, d8 triplets mirror d3 quartets |
| 18 | Jahn-Teller caption | 194 | fixed | caption printed a macro name ("one of the shared omlevel drawings") -> removed |
| 20 | sigma donation / pi back-donation | 210 | fixed | "M" label of the sigma panel sat on the axis; panel titles touched the labels -> moved |
| 20 | isolobal series | 214 | fixed | "1 frontier orbital(s), 1 electron(s)" -> words, singular/plural right |
| 21 | Cossee-Arlman steps | 222 | fixed | insertion arrow head touched the vacant site; panel 2 alkene too close to M -> panels spaced, space before caption |
| 22 | n_i of Si/Ge | 230 | fixed | "Ge" label on the Ge curve -> above it |
| 23 | perovskite cell | 241 | fixed | legend balls overlapped the corner A ion -> legend moved right |
| 24 | O2 binding / Hill plot | 252 | fixed (caption) | model Hill plot is straight at slope 2.7 for Hb, while the text says real Hb bends to slope 1 at both ends -> caption states it is the model |
| 28 | Sharpless mnemonic | 291 | fixed | frame cut through the R and CH2OH labels -> larger frame, arrows lengthened |
| 32 | dose-response | 328 | fixed | NOAEL label sat on the curve; "n = 6 (red)" -> leader to the 80 mg/kg dot, plain label |
| 33 | characterisation flowchart | 336 | fixed | "yes" overprinted the arrow between touching boxes -> boxes spaced |
| 33 | hierarchy of controls | 338 | fixed | level labels wider than the narrow lower trapezoids ran over their edges -> labels at the right with leaders, effectiveness arrow on the left |
| 13 | stopped-flow apparatus | -- | fixed | syringe/mixer/cell labels touched the drawing -> moved clear |
| 22 | donor and acceptor levels | -- | fixed | ionisation arrows ran into the level labels -> shortened and offset |
| 25 | host-guest complex | -- | fixed | "guest" label overprinted the cavity -> moved outside with a leader |
| 27 | radical scheme | -- | fixed | unpaired-electron dot collided with the atom symbol -> repositioned |
| 30 | Corey retrosynthesis boxes | -- | fixed | box texts touched the frames -> boxes widened |
| 16, 20, 21 | second pass after the table | -- | fixed | volcano "binds too weakly" note moved clear of the line; ch20 panel titles lowered, sigma-panel M moved; ch21 third Cossee-Arlman panel shifted right |
| all others | -- | -- | ok | layout and chemistry both checked; no change |

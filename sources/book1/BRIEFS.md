# Book 1 — chapter briefs (Phase A, 2026-10-02)

Writer: the Book 1 agent of the rolling batch (`sources/BATCH_BOOKS_1-4.md`).
One brief per chapter still to write (46), in outline order; the three pilots
(g2 `mixing-and-dissolving`, g7 `atoms-and-molecules`, g11 `redox`) are listed
only by their definitions, for the map. These briefs are a plan, not a
contract: Phase B may move an example or a figure, but a **definition never
moves to another chapter without a ruling** (see `DEFINITIONS.md`).

Legend for figures: **[S]** schematic (TikZ / chemfig / glassware pics /
pgfplots from inline exact expressions), **[F]** figdata (tested script
`figdata/<year>/<name>.py` → `figdata/out/<year>-<name>.dat`), **[AI]** AI
illustration (everyday / industrial / lab scene only), **[P]** photograph
(Commons, licence verified through the API; candidates checked 2026-10-02
are marked ✓ with their licence).

Definition lines read `` `label` — term; term `` (each term is an
`\emph{term}\index{term}` pair inside that `definition`). Ownership is checked
against the Book 1 map at the end of `OUTLINE.md`; "map ✓" means the map gives
the notion to this chapter, "not in map" means a Book 1-internal term placed
at its first natural use, "contested" points to `DEFINITIONS.md` § Contested.

Page targets (batch calibration, schematics only; illustrated chapters run
longer): grades 1–5 ~7 pp, grades 6–9 ~9 pp, grades 10–12 ~11 pp, solutions
included.

Math guard reminders: whole numbers g1–3; fractions g4+; percentages g6+;
powers g8+; scientific notation g9+; proportionality throughout high school;
derivatives g11+ (a rate written as a derivative only g12); log10/exp only
g12 (g9 pH is qualitative: one unit per tenfold dilution). Atomic weights
printed to 0.1 g/mol (`tools/molar_mass.py`, book column).

---

## Grade 1

### g1 ch1 `materials-around-us` — What Things Are Made Of (~7 pp; 10–11 exos, mostly ★; no problem)

- **Hook:** a child's breakfast table — a wooden spoon, a glass of milk, a
  metal fork, a paper napkin, a plastic bowl, a woollen jumper on the chair:
  many objects, a handful of materials.
- **Recall:** none (first chapter of the series).
- **Sections:** 1. Objects and the materials they are made of; 2. Seven
  common materials (wood, metal, glass, plastic, paper, fabric, stone); 3.
  Properties of materials (hard / soft, transparent / not, attracted by a
  magnet / not, floats / sinks, bends / breaks); 4. Sorting materials (method:
  one question at a time); 5. The right material for the job (window: glass;
  pan: metal; raincoat: plastic; shoes: leather or fabric).
- **Definitions:**
  - `def:g1:materials-around-us:object` — object (map ✓ "material, object")
  - `def:g1:materials-around-us:material` — material (map ✓)
  - `def:g1:materials-around-us:property` — property of a material (not in
    map; Book 1-internal; g6 `pure-substances-and-mixtures` recalls it for
    the "constants that identify a pure substance")
- **Statements:** prop "one object, several materials" (scissors: metal
  blades, plastic handles); method "sorting by one property"; examples for
  each material with everyday objects; remark: magnets attract iron objects,
  not every metal (aluminium cans, copper wire) — physics owns magnetism, used
  as a test only.
- **Boxes:** none (no product hazard at this level; a remark on broken glass
  handled by an adult, no `safety` box).
- **Figures:** [AI] hook table scene; [AI] seven material samples on a white
  table (wood block, metal spoon, glass jar, plastic toy, paper sheet, wool
  scarf, pebble); [AI] three spoons — wooden, metal, plastic; [AI] a magnet
  lifting iron paper clips beside a drink can it does not lift (review: the
  can must stay put); [S] two sorting hoops (Venn) with small drawn object
  icons; [S] table of materials × properties with ticks; [S] a basin of water,
  a wooden block floating and a pebble sunk.
- **Ledger:** none (no numbers about substances).
- **Exercises (10–11):** name the material of objects; odd one out; which
  property makes glass good for windows; sort a list with one question;
  read the hoops figure; an object made of two materials; why a pan handle is
  not metal (★★); choose a material for a boat (★★). Whole numbers only
  ("how many of these 8 objects are made of metal?").

---

## Grade 3

### g3 ch1 `separating-mixtures` — Separating Mixtures (~7 pp; 10–11 exos)

- **Hook:** muddy water from a puddle after a storm, and the clear water
  that comes out of the tap — how is one made into the other?
- **Recall:** mix, dissolve, solution (`ch:g2:mixing-and-dissolving`);
  "what dissolves is still there" (dried-away water leaves the solid).
- **Sections:** 1. Sorting by hand and sieving; 2. Letting settle and
  decanting; 3. Filtering; 4. Evaporating the water away; 5. Which method for
  which mixture — cleaning dirty water step by step (water-treatment plant:
  screens, settling tanks, sand filters, disinfection told).
- **Definitions:**
  - `def:g3:separating-mixtures:sieve` — sieving
  - `def:g3:separating-mixtures:decant` — settling; decanting
  - `def:g3:separating-mixtures:filter` — filtering; filtrate
  - `def:g3:separating-mixtures:evaporate` — evaporating (as a separation:
    the water dries away and the dissolved solid stays; the change of state
    itself is physics)
  (map ✓ "separation methods (decant, filter, evaporate)"; sieving and
  filtrate not in map, placed here.)
- **Statements:** prop "filtering does not remove what is dissolved" (salty
  water passes the filter salty); method "choosing a separation" (decision
  chart: big pieces → sieve; settles → decant; small pieces → filter;
  dissolved → evaporate); example sand + salt + water separated in three
  steps.
- **Boxes:** `inthelab[Filtering muddy water]` (teacher, funnel and paper);
  no safety box.
- **Figures:** [S] sieve over a bowl (gravel kept, sand through); [S]
  decanting: tilted beaker pic pouring the clear water off the settled layer
  into a second beaker; [S] filtration: funnel pic + filter paper + beaker
  pic, filtrate dripping; [S] evaporation in a shallow dish under the sun
  (reuses the pilot's saucer style); [S] water-treatment flow chart (4 boxes
  with arrows); [AI] kitchen sieve with flour; [AI] coffee filter dripping;
  [AI] water-treatment settling tanks (industrial); [AI] gold panning in a
  river (sieving by water).
- **Ledger:** none.
- **Exercises (10–11):** which method for (peas + rice; sand + water; salt +
  water; tea leaves + tea); order the steps for sand + salt + water; read the
  flow chart; why a filter cannot make sea water drinkable (★★); a coffee
  machine is a filter: what is the filtrate? (★★).

---

## Grade 4

### g4 ch1 `air-a-mixture-of-gases` — Air, a Mixture of Gases (~7 pp; 10–11 exos)

- **Hook:** a kite tugging on its string, a sail filling with wind — we
  cannot see air, but it pushes; what is it made of?
- **Recall:** mix (`ch:g2:mixing-and-dissolving`).
- **Sections:** 1. Air is all around us (it takes up space: an upturned
  glass pushed into water stays dry inside — physics owns "air is matter",
  told as an observation); 2. Air is a mixture (about four fifths nitrogen,
  one fifth oxygen, a little argon, carbon dioxide, water vapour); 3. What we
  breathe in and what we breathe out; 4. Oxygen for life and for fire (a
  candle under a jar goes out — teacher; **no "water rises one fifth"
  interpretation**: that classic is wrong, the rise is mostly thermal).
- **Definitions:**
  - `def:g4:air-a-mixture-of-gases:air` — air (the mixture of gases around
    the Earth) (map ✓ "air composition")
  - (breathed-in / breathed-out air: propositions, not terms.)
- **Statements:** prop "composition of dry air" (4/5 nitrogen, 1/5 oxygen,
  the rest about 1 part in 100, mostly argon); prop "breathed-out air"
  (less oxygen, about a hundred times more carbon dioxide); example "100
  balloons of air" (78 nitrogen, 21 oxygen, 1 argon and the rest); remark:
  the names nitrogen, oxygen, carbon dioxide are names of gases; their
  molecules come in grade 7.
- **Boxes:** `inthelab[A candle under a jar]` (teacher; the flame goes out
  when the oxygen it can reach is used up).
- **Figures:** [S] the "100 squares" grid coloured 78 / 21 / 1 (whole
  numbers); [S] bar chart breathed-in vs breathed-out (O₂ 21 → 16, CO₂ 0 →
  4, rounded, ledger); [S] upturned glass pushed into a water trough, paper
  dry inside; [AI] kite day hook; [AI] scuba diver breathing from a tank;
  [AI] candle under a glass jar in a lab, teacher's hands (review: no water
  in the dish, so no misleading rise).
- **Ledger:** `air:N2`, `air:O2`, `air:Ar`, `air:trace` (exist); new
  `air:CO2` (NOAA GML global mean, ppm → %), `air:H2O` (water vapour 0–4 %,
  variable; NASA/NOAA source); `breath:O2`, `breath:CO2` (exist).
- **Exercises (10–11):** fractions of air; "in 100 litres of air, how many
  litres of nitrogen?"; read the bar chart; what changes between air in and
  air out; why a room full of people needs fresh air (★★); why a diver's tank
  holds air, not pure oxygen (told reason: pure oxygen is dangerous under
  pressure) (★★).

### g4 ch2 `what-a-fire-needs` — Burning: What a Fire Needs (~7 pp; 10–11 exos)

- **Hook:** a campfire at dusk: it needs wood, it needs the wind's air, and
  it needs a match to start — and it leaves ash, smoke and warm air behind.
- **Recall:** air composition and oxygen (`ch:g4:air-a-mixture-of-gases`).
- **Sections:** 1. Fuels (wood, paper, candle wax, gas, petrol); 2. The fire
  triangle (fuel, oxygen, heat); 3. Burning makes new substances (ash, smoke,
  carbon dioxide, water — a cold glass held over a candle mists up,
  teacher); 4. Putting a fire out (take away one side: cover it, cool it,
  remove the fuel); 5. Fire safety (pan fires and water, smoke alarms, what
  to do).
- **Definitions:**
  - `def:g4:what-a-fire-needs:fuel` — fuel
  - `def:g4:what-a-fire-needs:fire-triangle` — fire triangle
  - `def:g4:what-a-fire-needs:burning` — burning; combustion (the chemist's
    word; **contested**, see `DEFINITIONS.md` § C3: g8 recalls it and defines
    complete / incomplete combustion)
  (map ✓ "fire triangle, burning makes new substances".)
- **Statements:** prop "a burning makes new substances" (it is not undone:
  ash does not turn back into wood — the word "irreversible" waits for g5);
  method "putting out a fire: which side of the triangle?"; remark "never
  water on a burning pan of oil" (told: the water boils at once and throws
  the burning oil out).
- **Boxes:** `safety{\ghs{GHS02}}` — the flame pictogram on lighter gas
  (butane): flammable; `inthelab[A cold glass over a candle]`.
- **Figures:** [S] fire triangle with three drawn icons (log, O₂ cloud,
  flame); [S] three small triangles, one side crossed out each (blanket /
  water / fuel removed); [S] candle with a cold glass beaker above, droplets
  drawn (beaker pic upside down) and smoke; [AI] campfire hook; [AI] fire
  blanket laid over a pan on a cooker (review: flame out, no water); [AI]
  firefighters spraying water on a burning shed (industrial-everyday); [AI]
  smoke alarm on a ceiling (no letters).
- **Ledger:** `ghs:butane` (PubChem GHS: GHS02, GHS04).
- **Exercises (10–11):** name the three sides; which side does each
  extinguisher remove; why blowing on embers revives them; why a candle under
  a jar goes out (link to ch. 1); identify new substances after burning
  paper; read the triangles figure (★★); why a forest fire is fought by
  cutting a strip of trees (★★).

---

## Grade 5

### g5 ch1 `irreversible-changes` — Changes That Cannot Be Undone (~7 pp; 10–11 exos)

- **Hook:** an egg cracked into a hot pan turns white and firm in seconds;
  no amount of cooling makes it runny and clear again.
- **Recall:** dissolving and getting the solid back
  (`ch:g2:mixing-and-dissolving`); burning makes new substances
  (`ch:g4:what-a-fire-needs`).
- **Sections:** 1. Changes that can be undone (dissolving sugar and drying
  it back; ice melting and freezing again — physics, used as an example
  only); 2. Changes that cannot be undone (cooking an egg, baking a cake,
  burning, rusting, milk turning sour, a cut apple browning); 3. Clues that
  a new substance has appeared (new colour, gas bubbles, new smell, heat or
  light given out, a solid appearing in a liquid); 4. Useful and harmful
  changes (cooking, plaster and cement setting; rust, food going off; how to
  slow them: fridge, paint, oil).
- **Definitions:**
  - `def:g5:irreversible-changes:reversible` — reversible change
  - `def:g5:irreversible-changes:chemical-change` — irreversible change;
    chemical change (map ✓ "chemical change (everyday, irreversible)";
    **contested** with g7 `chemical-reactions`, see § C4)
- **Statements:** prop "in a chemical change new substances appear";
  method "is it a chemical change? look for the clues" (with the warning
  that one clue alone may mislead: boiling water bubbles but makes nothing
  new); example milk turning sour (lumps appear, new smell).
- **Boxes:** `inthelab[Vinegar on baking soda]` (teacher pours vinegar on
  baking soda in a beaker: fizzing, a gas; told, never proposed to do).
- **Figures:** [S] two-column diagram: reversible pairs with ⇄ arrows
  (sugar water ⇄ sugar + water; ice ⇄ water) vs one-way arrows (raw egg →
  cooked egg; wood → ash and smoke); [S] "clue" icons chart (colour, bubbles,
  smell, warmth / light, solid appearing); [AI] egg frying (hook); [AI]
  rusty bicycle chained to a railing; [AI] cake batter and the baked cake;
  [AI] a cut apple browning beside a fresh one; [AI] beaker of vinegar on
  baking soda foaming in a school lab (teacher's gloved hands).
- **Ledger:** none.
- **Exercises (10–11):** reversible or not (8 everyday cases); find the
  clue in a description; why boiling water is not a chemical change though
  it bubbles (★★); which of fridge / paint / oil slows which change; read
  the two-column figure.

### g5 ch2 `raw-materials-and-recycling` — From Raw Materials to Recycling (~7 pp; 10–11 exos)

- **Hook:** an empty drink can tossed into a recycling bin — six weeks
  later it can be back on a shop shelf as a new can.
- **Recall:** object, material (`ch:g1:materials-around-us`); chemical
  change (`ch:g5:irreversible-changes`).
- **Sections:** 1. Natural and manufactured materials (wood, cotton, wool,
  stone vs glass, steel, plastic, paper, concrete); 2. Raw materials: where
  materials come from (trees, ores, crude oil, sand, cotton plants, sheep);
  3. From raw material to object (sand → glass; iron ore → steel; oil →
  plastic; wood → paper) — chemical changes on the way; 4. Sorting and
  recycling (glass, metal, paper, plastic; why: saving raw materials and
  energy); 5. Waste and resources (resources that run out vs renewable ones;
  reduce, reuse, recycle).
- **Definitions:**
  - `def:g5:raw-materials-and-recycling:natural-material` — natural
    material; manufactured material (**contested** with g8 `plastics`,
    § C5: g8 refines manufactured into artificial and synthetic)
  - `def:g5:raw-materials-and-recycling:raw-material` — raw material; ore
    (ore: not in map; placed here, first use)
  - `def:g5:raw-materials-and-recycling:recycling` — recycling (map ✓)
  - `def:g5:raw-materials-and-recycling:resource` — resource; renewable
    resource (map ✓ "recycling, resources")
- **Statements:** prop "recycling saves raw material and energy" (aluminium:
  recycling needs about a twentieth of the energy, ledger); example the
  life of a glass bottle (sand + soda + limestone → glass → bottle → bin →
  cullet → bottle); method "where does this object come from?" (trace back to
  a raw material).
- **Boxes:** `history[Glass, 4500 years old]`? — optional, only with a
  sourced date (Mesopotamian glass); otherwise dropped.
- **Figures:** [S] loop diagram raw material → making → object → waste →
  sorting → recycling → back to making; [S] four labelled sorting bins with
  drawn items (colours neutral, no country's colour code); [P] an ore
  specimen — candidates ✓ `File:Bauxite with unweathered rock core. C 021.jpg`
  (CC BY-SA 2.5), ✓ `File:Hematite.jpg` (CC BY-SA 3.0); [AI] quarry / open-pit
  mine; [AI] glass recycling plant with mounds of green and clear cullet;
  [AI] bales of crushed aluminium cans; [AI] sheep being sheared / cotton
  bolls (natural raw materials).
- **Ledger:** `al:recycle-energy` (energy of recycled vs primary aluminium,
  International Aluminium Institute or USGS); possibly `glass:recycle`
  (qualitative). No other numbers.
- **Exercises (10–11):** natural or manufactured (list); trace an object to
  its raw material; which bin; why recycling aluminium saves energy (read the
  ledger fact as a fraction: 1/20) (★★); renewable or not (wood, oil, sand,
  cotton) (★★).

---

## Grade 6

### g6 ch1 `pure-substances-and-mixtures` — Pure Substances and Mixtures (~9 pp; 12 exos + problem 10–14 q, Parts I–III)

- **Hook:** a bottle of mineral water lists a dozen dissolved substances on
  its label; the water from a laboratory's purifier lists none. Both are
  clear and colourless — which is "pure"?
- **Recall:** mix, solution (`ch:g2:mixing-and-dissolving`); separation
  methods (`ch:g3:separating-mixtures`); properties of materials
  (`ch:g1:materials-around-us`).
- **Sections:** 1. Chemical species and pure substances; 2. Mixtures:
  homogeneous and heterogeneous; 3. Identifying a pure substance by its
  constants (melting temperature, boiling temperature, density — used as
  data, taught in physics); 4. Water, pure and not (pure water, tap water,
  mineral water, sea water; reading a label in mg/L).
- **Definitions:**
  - `def:g6:pure-substances-and-mixtures:species` — chemical species (map ✓)
  - `def:g6:pure-substances-and-mixtures:pure-substance` — pure substance
    (map ✓)
  - `def:g6:pure-substances-and-mixtures:mixture` — mixture (map ✓; distinct
    from g2's verb "mix")
  - `def:g6:pure-substances-and-mixtures:homogeneous` — homogeneous mixture;
    heterogeneous mixture
- **Statements:** prop "a pure substance has a fixed melting and boiling
  temperature; a mixture changes state over a range" (physics fact, used);
  method "identifying a pure substance from its constants" (compare with a
  table); example: salty water boils above 100 °C and keeps rising.
- **Boxes:** `inthelab[Boiling salty water]` (teacher, thermometer readings
  given in a table, no curve).
- **Figures:** [S] classification tree (matter → pure substance / mixture →
  homogeneous / heterogeneous, each leaf with two drawn examples); [S] four
  beaker pics: salt water (homogeneous), oil on water, muddy water, orange
  juice with pulp; [S] a table-figure "constants of five pure substances"
  (no curve); [P] granite ✓ `File:Granite.jpg` (CC BY-SA 2.0 br) as a
  heterogeneous solid; [AI] mineral-water bottle and glass (label blank, no
  text); [AI] orange juice with pulp in a glass.
- **Ledger:** `mp:water`, `bp:water` (definition-level but cited),
  `bp:ethanol`, `mp:ethanol`, `rho:ethanol`, `rho:water`, `mp:NaCl`,
  `mp:Fe` (NIST WebBook / PubChem experimental properties); a sourced
  example mineral-water composition is **not** needed (label values in
  exercises are exercise data).
- **Exercises (12):** classify 8 everyday things; pure or mixture from a
  boiling-temperature table; homogeneous or not; read a label (mg/L,
  percentages allowed); identify a liquid from its constants; why "pure
  orange juice" is not a pure substance (★★); separation chosen for each
  mixture (recall g3) (★★); a percentage of a mixture by mass (★★★).
- **Problem — "Three colourless liquids":** a lab assistant finds three
  unlabelled flasks A, B, C (water, ethanol, salty water). Part I —
  classification from observations; Part II — boiling temperatures and mass
  / volume measurements (density computed as mass ÷ volume, physics
  formula used as known) against a table of constants; Part III — liquid C
  left to dry: the residue. **Named final number: the salt content of C,
  35 g per litre** (ledger `sea:salinity` used to say "as salty as the
  sea"). 12 questions.

### g6 ch2 `solutions-and-solubility` — Solutions and Solubility (~9 pp; 12 exos + problem)

- **Hook:** opening a bottle of fizzy water: a hiss, a rush of bubbles —
  a gas was dissolved in the water all along.
- **Recall:** dissolve, solution (`ch:g2:mixing-and-dissolving`); pure
  substance, mixture, homogeneous (`ch:g6:pure-substances-and-mixtures`);
  evaporating (`ch:g3:separating-mixtures`).
- **Sections:** 1. Solute and solvent (water is not the only solvent:
  ethanol, propanone in nail-varnish remover, white spirit); mass of a
  solution = mass of solvent + mass of solute; 2. Saturation and solubility
  in grams per litre; 3. Miscible and immiscible liquids (oil and water;
  water and alcohol; a vinaigrette); 4. Gases dissolve too (carbon dioxide in
  fizzy drinks and in the oceans; oxygen in water for fish).
- **Definitions:**
  - `def:g6:solutions-and-solubility:solute` — solute; solvent; aqueous
    solution (**contested** § C1: "solution" stays g2's; g6 does not define
    it again)
  - `def:g6:solutions-and-solubility:saturated` — saturated solution
  - `def:g6:solutions-and-solubility:solubility` — solubility (map ✓)
  - `def:g6:solutions-and-solubility:miscible` — miscible; immiscible
    (map ✓)
- **Statements:** prop "mass is conserved when dissolving" (a weighing; not
  the g8 law, which is about reactions); prop "solubility depends on the
  solute, the solvent and the temperature" (told; numbers at 20 °C only);
  method "will it all dissolve?" (compare mass ÷ volume with the
  solubility); example sugar vs salt solubility.
- **Boxes:** `safety{\ghs{GHS02}\ghs{GHS07}}` — propanone (nail-varnish
  remover); `inthelab[Saturating salt water]`.
- **Figures:** [S] solute + solvent → solution with masses (balance drawn
  as a box with no digits; beaker pics); [S] three beakers: dissolved, just
  saturated, excess at the bottom; [S] test tubes: oil/water two layers vs
  ethanol/water one layer; [S] solubility table-figure (NaCl, sugar, CO₂,
  O₂ at 20 °C — a table, not a bar chart: the values span five decades);
  [AI] fizzy-water bottle being opened (no label text); [AI] vinaigrette
  separating in a jar; [AI] fish tank with an air bubbler.
- **Ledger:** `sol:NaCl`, `sol:sucrose`, `sol:CO2`, `sol:O2` (IUPAC–NIST
  Solubility Data / PubChem / USGS dissolved-oxygen tables), `ghs:acetone`.
- **Exercises (12):** solute / solvent in five solutions; can 50 g of salt
  dissolve in 100 mL of water?; saturated or not; miscible or not; why a
  warm fizzy drink goes flat faster (told: solubility of gases falls with
  temperature) (★★); percentages of a solution's mass (★★); read the table
  (★★); a mass balance after evaporation (★★★).
- **Problem — "The cheese-maker's brine":** cheeses are soaked in a
  saturated salt bath. Part I — solute, solvent, saturation; Part II —
  mass of salt to saturate 20 L of water (7.2 kg) and mass of the brine;
  Part III — in summer 5 L of water evaporate from the bath. **Named final
  number: the mass of salt that crystallises, 1.8 kg.** 12 questions.

---

## Grade 7

### g7 ch1 `identifying-substances` — Identifying Substances (~9 pp; 12 exos + problem)

- **Hook:** a forensic chemist receives a crumpled note and a bag of three
  felt-tip pens: which pen wrote it? (Formulas are not yet known: this
  chapter comes before atoms and molecules, so it names substances only.)
- **Recall:** chemical species, pure substance, mixture
  (`ch:g6:pure-substances-and-mixtures`); solubility
  (`ch:g6:solutions-and-solubility`).
- **Sections:** 1. What a characteristic test is (one reagent, one
  observable result, one species); 2. Four classic tests (limewater turns
  milky with carbon dioxide; white anhydrous copper sulfate turns blue with
  water; a glowing splint relights in oxygen; hydrogen burns with a squeaky
  pop); 3. Paper chromatography (dyes of an ink or of sweets' coatings travel
  at different heights); 4. Reading a test bank (a table: test → positive
  result → conclusion; a negative test and a blank).
- **Definitions:**
  - `def:g7:identifying-substances:characteristic-test` — characteristic
    test; reagent (map ✓ "characteristic tests")
  - `def:g7:identifying-substances:chromatography` — paper chromatography;
    chromatogram (map ✓)
  (Map: g9 `ions` recalls the tests and adds precipitation tests; g10
  `chemical-species` owns TLC and Rf.)
- **Statements:** method "running a characteristic test" (sample, reagent,
  observation, conclusion, blank); prop "on a chromatogram, a pure dye gives
  one spot; a mixture of dyes several"; example: the black ink of a pen is
  three dyes.
- **Boxes:** `safety{...}` copper sulfate (anhydrous; PubChem pictograms,
  expected GHS05/GHS07/GHS09 — to verify); `safety` limewater (calcium
  hydroxide); `inthelab[The pop test]` (teacher, tiny test-tube volume only).
- **Figures:** [S] limewater test: testtube pic with delivery tube bubbling
  into a second tube of limewater, before / after; [S] glowing splint at the
  mouth of a test tube; [S] paper chromatography in a beaker (strip as the
  `tlcplate` pic, baseline above the solvent) and the developed chromatogram
  of an ink vs three reference dyes; [S] test-bank table-figure; [P] copper
  sulfate crystals ✓ `File:Copper sulfate.jpg` (CC BY-SA 3.0), plus a
  verified anhydrous-powder photo if one exists (Phase B); [AI] bowl of
  colourful sugar-coated sweets (hook for dyes); [AI] teacher in goggles
  holding a test tube with a glowing splint (lab scene).
- **Ledger:** `ghs:CuSO4`, `ghs:CaOH2`, `ghs:H2` (PubChem). No numbers.
- **Exercises (12):** which test for which species; interpret described
  results; read a chromatogram (how many dyes; which references are in the
  ink); why a blank is run (★★); a test that proves water is present but not
  that a liquid is pure water (★★); design a test sequence for an unknown gas
  (★★★, on paper).
- **Problem — "The forged note":** Part I — chromatograms of the note's
  ink and three pens (drawn in the problem); Part II — the same lab checks
  three gas cylinders with the classic tests; Part III — the test bank,
  conclusions, a false positive. **Named final number: the number of dyes in
  the forger's ink, 3** (and the one matching pen). 12 questions.

### g7 ch3 `chemical-reactions` — Chemical Reactions: Reactants and Products (~9 pp; 12 exos + problem)

- **Hook:** charcoal glowing in a barbecue: after an hour almost nothing is
  left but a little ash. Where has the black carbon gone?
- **Recall:** chemical change (`ch:g5:irreversible-changes`); atom,
  molecule, formula (`ch:g7:atoms-and-molecules`); characteristic tests
  (`ch:g7:identifying-substances`).
- **Sections:** 1. Physical and chemical transformations (changes of state
  and dissolving keep the species; a chemical transformation changes them);
  2. Reactants and products (carbon + oxygen → carbon dioxide, products
  identified by tests); 3. The word equation and its arrow; 4. A reaction is
  a rearrangement of atoms (models: methane + oxygen → carbon dioxide +
  water, with the right numbers of model molecules given; atoms are neither
  created nor destroyed — the mass law and the balancing method are g8's).
- **Definitions:**
  - `def:g7:chemical-reactions:physical-transformation` — physical
    transformation (not in map; Book 1-internal)
  - `def:g7:chemical-reactions:reaction` — chemical reaction (map ✓)
  - `def:g7:chemical-reactions:reactant` — reactant; product (map ✓)
  - `def:g7:chemical-reactions:word-equation` — word equation (not in map)
- **Statements:** prop "in a reaction the atoms are rearranged: the same
  atoms, joined differently" (**boundary with g8**, § C4b); method "writing
  a word equation"; example charcoal burning identified with limewater;
  example steel wool burning in oxygen (teacher) giving iron oxide.
- **Boxes:** `inthelab[Charcoal in a jar of oxygen]` (teacher; limewater
  afterwards).
- **Figures:** [S] ball-and-stick rearrangement: 1 CH₄ + 2 O₂ → 1 CO₂ + 2 H₂O
  before / after with atom counts (atom styles); [S] classification diagram
  physical vs chemical with examples; [S] gas jar of oxygen with a glowing
  charcoal (local drawing; needs the `gasjar` pic, § style needs); [AI]
  barbecue charcoal glowing; [AI] steel wool burning in a lab dish with
  sparks (teacher, goggles).
- **Ledger:** none.
- **Exercises (12):** physical or chemical (8 cases); name reactants and
  products from a description; write word equations; count atoms before and
  after from models; read the model figure; why the mass of ash is less than
  the mass of wood (gases left) (★★); which test identifies each product
  (★★); a reaction drawn with models: find what is wrong (★★★).
- **Problem — "Inside a gas-cooker flame":** methane burns in air. Part I —
  reactants, products, tests (copper sulfate, limewater); Part II — word
  equation, physical vs chemical; Part III — models: "each methane molecule
  needs two oxygen molecules" given; count for 10 methane molecules. **Named
  final number: 20 molecules of water from 10 of methane.** 12 questions.

---

## Grade 8

### g8 ch1 `balanced-equations` — Conservation of Mass and Balanced Equations (~9 pp; 12 exos + problem)

- **Hook:** a log weighs 2 kg; its ash a few tens of grams. Did 2 kg of
  matter vanish? Lavoisier's answer, two centuries ago: weigh everything,
  including the gases.
- **Recall:** reaction, reactant, product, rearrangement of atoms
  (`ch:g7:chemical-reactions`); formula (`ch:g7:atoms-and-molecules`).
- **Sections:** 1. Mass is conserved (closed flask on a balance: vinegar +
  baking soda with a balloon over the neck, teacher; the open flask "loses"
  mass to the escaping gas); 2. Why: atoms are conserved; 3. The chemical
  equation (formulas, arrow, state symbols (s), (l), (g)); 4. Balancing an
  equation (method; stoichiometric coefficients); 5. Reading an equation in
  molecules.
- **Definitions:**
  - `def:g8:balanced-equations:conservation` — conservation of mass (map ✓)
    — stated as a law in a `proposition` right after
  - `def:g8:balanced-equations:equation` — chemical equation; balanced
    equation (map ✓ "balancing")
  - `def:g8:balanced-equations:coefficient` — stoichiometric coefficient
  - `not:g8:balanced-equations:states` — notation (s), (l), (g) (no term)
- **Statements:** prop "Lavoisier's law"; method "balancing an equation"
  (count, fix one element at a time, O and H last, whole numbers, check);
  examples H₂ + O₂; CH₄ + O₂; Fe + O₂ → Fe₂O₃; remark: never change a
  subscript to balance.
- **Boxes:** `history[Lavoisier weighs everything, 1770s–1789]`.
- **Figures:** [S] closed vs open erlenmeyer pic on a drawn balance with a
  balloon; [S] balancing with atom-style models (2 H₂ + O₂ → 2 H₂O, boxes of
  atoms counted); [S] anatomy of an equation (labels on coefficients,
  subscripts, state symbols, arrow); [P] Lavoisier ✓ `File:David - Portrait
  of Monsieur Lavoisier and His Wife.jpg` (PD); [AI] logs and a small heap
  of ash in a fireplace (hook).
- **Ledger:** none (exercise data only); history dates need no row.
- **Exercises (12):** balance 6 equations (two with `% ce-unbalanced-ok`
  skeletons in the questions); mass before / after; read a balance figure;
  explain the open-flask loss (★★); count atoms on both sides (★★); find the
  error in a "balanced" equation (★★★).
- **Problem — "Steel wool in a sealed jar":** steel wool burns in a sealed
  jar on a balance (no change) and in an open dish (gain). Part I —
  observations and the law; Part II — balance 4 Fe + 3 O₂ → 2 Fe₂O₃ and
  3 Fe + 2 O₂ → Fe₃O₄; Part III — mass ratio given ("7 g of iron take 3 g of
  oxygen"), 2.8 g of steel wool. **Named final number: the mass of oxygen
  taken from the jar, 1.2 g.** 12 questions.

### g8 ch2 `combustion-and-fuels` — Combustion: Fuels, Products and Greenhouse Gases (~9 pp; 12 exos + problem)

- **Hook:** a gas boiler in a flat with a blocked flue: a silent, odourless
  gas fills the room. The carbon-monoxide alarm on the wall saves the
  family.
- **Recall:** fire triangle, burning / combustion
  (`ch:g4:what-a-fire-needs`); air composition
  (`ch:g4:air-a-mixture-of-gases`); balanced equations
  (`ch:g8:balanced-equations`).
- **Sections:** 1. Combustion of carbon and of methane (equations, tests);
  2. Complete and incomplete combustion (blue vs yellow flame, soot, carbon
  monoxide); 3. Carbon monoxide, a silent danger (ventilation, detectors,
  never a barbecue indoors); 4. Carbon dioxide and the greenhouse effect
  (the measured rise of CO₂; the greenhouse effect told, its physics is
  physics'); 5. Fossil and renewable fuels (coal, oil, gas vs wood, biogas,
  bioethanol; the carbon they release came from the air how long ago?).
- **Definitions:**
  - `def:g8:combustion-and-fuels:complete` — complete combustion; incomplete
    combustion (map ✓)
  - `def:g8:combustion-and-fuels:greenhouse` — greenhouse gas (map ✓)
  - `def:g8:combustion-and-fuels:fossil` — fossil fuel; renewable fuel (not
    in map explicitly; under "fossil and renewable fuels", owner here)
- **Statements:** prop "complete combustion of a fuel made of C and H gives
  CO₂ and H₂O"; method "writing a combustion equation" (CₓHᵧ + O₂); example
  propane, butane, ethanol; remark CO binds to the blood (told, biology).
- **Boxes:** `safety{\ghs{GHS02}\ghs{GHS04}\ghs{GHS06}\ghs{GHS08}}` carbon
  monoxide (to verify); `safety` methane.
- **Figures:** [F] `co2-record`: annual mean CO₂ at Mauna Loa since 1959
  (NOAA GML file, values in the script with the source line; test: first and
  last points equal their ledger rows, series strictly increasing); [S]
  Bunsen burner with air hole open (blue cone) / closed (yellow flame) —
  needs `bunsen` pic; [S] simple carbon cycle (fuels → CO₂ → plants, fossil
  store with "millions of years"); [AI] gas boiler with CO alarm (no
  letters); [AI] traffic exhaust in winter; [AI] coal power plant; [AI]
  biogas digester on a farm; [AI] soot on a cold spoon held in a yellow
  candle flame (lab scene).
- **Ledger:** `co2:mlo-1959`, `co2:mlo-2024` (NOAA GML annual means),
  `ghs:CO`, `ghs:CH4`; `co2:preindustrial` (~280 ppm, source e.g. NOAA/IPCC
  AR6 WG1 SPM) if quoted.
- **Exercises (12):** equations of complete combustion (carbon, methane,
  propane, butane, ethanol); complete or incomplete from a description; read
  the CO₂ curve (rise per decade, as a percentage); why a yellow flame
  blackens a pan (★★); fossil or renewable (★★); percentage increase since
  1959 (★★★).
- **Problem — "The stove in the tent":** propane camping stove. Part I —
  complete combustion C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O and incomplete 2 C₃H₈ +
  7 O₂ → 6 CO + 8 H₂O; Part II — mass ratio given ("44 g of propane give
  132 g of CO₂"); Part III — why never in a closed tent. **Named final
  number: 1.35 kg of carbon dioxide from one 450 g cartridge.** 12 questions.

### g8 ch3 `plastics` — Plastics and Synthetic Materials (~9 pp; 12 exos + problem)

- **Hook:** the same day: a toothbrush, a water bottle, a raincoat, a
  phone case, a car bumper — all plastics, none existing a hundred and
  twenty years ago.
- **Recall:** natural / manufactured materials, raw materials, recycling
  (`ch:g5:raw-materials-and-recycling`); combustion
  (`ch:g8:combustion-and-fuels`).
- **Sections:** 1. Natural, artificial and synthetic materials; 2. What
  plastics are (made mostly from oil; very long molecules — the word
  "polymer" waits for g12); 3. The main plastics and their uses (PET, HDPE,
  PVC, LDPE, PP, PS; the resin codes 1–7); 4. Thermoplastics and
  thermosets; 5. Plastics in the environment (they last; microplastics;
  collection, recycling rates; burning PVC releases hydrogen chloride).
- **Definitions:**
  - `def:g8:plastics:artificial` — artificial material; synthetic material
    (map ✓ via the outline line; **contested** § C5 with g5)
  - `def:g8:plastics:plastic` — plastic (map ✓ "plastics as materials")
  - `def:g8:plastics:thermoplastic` — thermoplastic; thermoset (not in map;
    g12 `polymers` recalls)
  - `def:g8:plastics:code` — resin identification code (not in map)
- **Statements:** prop "a plastic is shaped when soft"; method "identifying
  a plastic: code, then tests (floats in water? burns how?)" — burning tests
  told, done by nobody outside a lab; example PET bottle to fleece.
- **Boxes:** `history[Bakelite, 1907]`.
- **Figures:** [S] the seven resin-code triangles with abbreviations; [S]
  classification tree natural / artificial / synthetic with examples (cotton
  / viscose / nylon); [S] "a long chain of beads" cartoon labelled as a
  picture, not a model (term deferred to g12); [P] Bakelite telephone ✓
  `File:Bakelittelefon 1947a.jpg` (CC BY-SA 3.0); [AI] row of everyday
  plastic objects; [AI] plastic litter on a beach; [AI] sorting line in a
  recycling plant.
- **Ledger:** `plastics:production` (world production, Mt/yr — OECD Global
  Plastics Outlook 2022), `plastics:recycled` (share recycled, same source),
  `code:resin` (ASTM D7611 codes — names only), densities of PET, PE, PP, PS,
  PVC if the sink–float sorting is kept (source to find; else EXCLUDE and
  drop Part II below).
- **Exercises (12):** natural / artificial / synthetic; code → name → use;
  thermoplastic or thermoset; read the code figure; percentage recycled (★★);
  why PVC must not be burnt in a garden (★★); mass of plastic in a year of
  bottles (★★★).
- **Problem — "The sorting line":** a recycling plant receives mixed
  bottles. Part I — codes and families; Part II — sink–float sorting in
  water (densities given, ledger) (fallback: sorting by code and colour);
  Part III — mass balance of a 1 t bale with a given composition. **Named
  final number: the mass of clean PET flakes from one tonne, 780 kg**
  (exercise composition). 12 questions.

---

## Grade 9

### g9 ch1 `inside-the-atom` — Inside the Atom (~9 pp; 12 exos + problem)

- **Hook:** gold leaf a few hundred atoms thick, a beam of alpha particles,
  and a physicist who said it was "as if you fired a 15-inch shell at a piece
  of tissue paper and it came back and hit you".
- **Recall:** atom, molecule, symbol (`ch:g7:atoms-and-molecules`).
- **Sections:** 1. Nucleus and electrons (the electron's negative charge,
  the atom neutral); 2. Protons and neutrons: atomic number Z, mass number
  A, notation ᴬ_Z X; 3. The chemical element and its isotopes (carbon-12,
  carbon-13; carbon-14 named, its decay is physics); 4. Sizes and masses
  compared (atom ~10⁻¹⁰ m, nucleus ~10⁻¹⁵ m; the mass is in the nucleus);
  5. A short history of the model (Thomson 1897, Rutherford 1911, Bohr 1913
  told, Chadwick 1932).
- **Definitions:**
  - `def:g9:inside-the-atom:nucleus` — nucleus; electron (map ✓)
  - `def:g9:inside-the-atom:proton` — proton; neutron; nucleon
  - `def:g9:inside-the-atom:atomic-number` — atomic number; mass number
    (map ✓ "Z, A")
  - `def:g9:inside-the-atom:element` — chemical element (**contested** § C7
    with g9 `periodic-table-first-look`; claimed here because the definition
    is "all atoms and ions with the same Z")
  - `def:g9:inside-the-atom:isotope` — isotopes (map ✓)
- **Statements:** prop "an atom is neutral: Z electrons"; prop "the mass of
  an atom is almost all in its nucleus" (computed from const:mp, const:me);
  method "reading ᴬ_Z X" (protons, neutrons, electrons); example chlorine-35
  / chlorine-37.
- **Boxes:** `history[Rutherford's gold foil, 1909–1911]`.
- **Figures:** [S] atom drawn not to scale (nucleus + electron cloud) with a
  scale bar remark; [S] the nuclide symbol annotated; [S] gold-foil
  experiment (source, beam, foil, screen, most go straight, few bounce); [S]
  scale comparison: "if the nucleus were a 1 cm marble, the atom would be
  1 km across" (computed from the ledger orders); [S] nuclei of the three
  hydrogen isotopes and of ¹²C / ¹³C (coloured circles); [P] Rutherford ✓
  `File:Ernest Rutherford LOC.jpg` (PD).
- **Ledger:** `const:e`, `const:me`, `const:mp`, `const:mn`, `const:u`,
  `const:a0` (shared, exist); new `r:nucleus` (order of magnitude of nuclear
  radius, e.g. r = 1.2 A^{1/3} fm — source CODATA proton radius or a nuclear
  data page), `iso:C12`, `iso:C13`, `iso:Cl35`, `iso:Cl37`, `iso:H2`
  (CIAAW isotopic compositions).
- **Exercises (12):** protons / neutrons / electrons from ᴬ_Z X (5 nuclides);
  isotopes or not; masses of atoms in scientific notation; nucleus vs atom
  ratio; read the gold-foil figure (★★); why most alpha particles pass
  straight (★★); mass of the electrons of an iron atom as a fraction of its
  mass (★★★).
- **Problem — "Weighing chlorine":** Part I — the two isotopes (Z, A,
  composition); Part II — masses of each atom from nucleon masses
  (1.67 × 10⁻²⁷ kg each, electrons neglected and checked); Part III — 75.8 %
  / 24.2 % abundances (ledger). **Named final number: the average mass of a
  chlorine atom, 5.93 × 10⁻²⁶ kg.** 12 questions.

### g9 ch2 `ions` — Ions and Ionic Solutions (~9 pp; 12 exos + problem)

- **Hook:** a sports drink sold for its "electrolytes" and a glass of
  sugared water: one lights a bulb in a simple circuit, the other does not.
- **Recall:** nucleus, electrons, Z (`ch:g9:inside-the-atom`);
  characteristic tests (`ch:g7:identifying-substances`); solute, solvent
  (`ch:g6:solutions-and-solubility`).
- **Sections:** 1. Atoms that gain or lose electrons (cation, anion;
  monatomic Na⁺, K⁺, Ca²⁺, Mg²⁺, Cl⁻, Cu²⁺, Fe²⁺, Fe³⁺, Zn²⁺, Al³⁺;
  polyatomic SO₄²⁻, NO₃⁻, HO⁻, CO₃²⁻, NH₄⁺); 2. Ionic compounds and their
  formulas (electrically neutral: NaCl, CaCl₂, CuSO₄, FeCl₃, Al₂O₃); the ionic
  solid as a stack of ions (picture, the lattice is Year 1's); 3. Ionic
  solutions conduct electricity (sugar water does not); the state symbol
  (aq); 4. Precipitation tests for ions (sodium hydroxide: Cu²⁺ blue, Fe²⁺
  green, Fe³⁺ rust-brown, Zn²⁺ and Al³⁺ white; silver nitrate: Cl⁻ white,
  darkening in light; flame colours told for Na⁺, K⁺, Cu²⁺ — optional).
- **Definitions:**
  - `def:g9:ions:ion` — ion; cation; anion (map ✓)
  - `def:g9:ions:ionic-compound` — ionic compound (map ✓)
  - `def:g9:ions:precipitate` — precipitate; precipitation (not in map;
    Book 1-internal; Year 1 re-founds precipitation rigorously)
  - `not:g9:ions:aq` — notation (aq) (no term)
- **Statements:** prop "the formula of an ionic compound is neutral";
  method "writing the formula from the ions" (cross the charges, simplify);
  method "testing for an ion" (reagent, colour, conclusion); example
  identifying iron(III) chloride.
- **Boxes:** `safety{\ghs{GHS05}}` sodium hydroxide; silver nitrate
  (`ghs:AgNO3`, exists); `inthelab[Which liquids conduct?]` (teacher, low
  voltage).
- **Figures:** [S] Na atom → Na⁺ ion, Cl atom → Cl⁻ ion (electron counts in
  boxes, not shells: shells are g10); [S] conductivity circuit (battery,
  bulb, two electrodes in a beaker) — `circuitikz` or local symbols; [S] five
  test tubes with coloured precipitates (testtube pics) + the AgCl tube;
  [S] a slice of the NaCl stack (alternating spheres, `aNa`/`aCl` styles);
  [P] halite crystals ✓ `File:Halite-249324.jpg` (CC BY-SA 3.0); [AI] sports
  drink and glass of water on a gym bench (no label text).
- **Ledger:** `ghs:NaOH`, `ghs:AgNO3` (exists); colours are qualitative
  facts (no row; cited from the same PubChem/compound pages in a comment if
  needed).
- **Exercises (12):** charge of an ion from protons / electrons; formulas
  of ionic compounds (8); names ↔ formulas; interpret test results; which
  liquids conduct (★★); count ions in a formula (★★); deduce an unknown salt
  from two tests (★★★).
- **Problem — "The rusty well":** a farmhouse well's water stains the sink
  orange. Part I — tests on a sample (green precipitate turning brown);
  Part II — formulas Fe(OH)₂, Fe(OH)₃, ions, charges; Part III — counting:
  0.30 mg of iron per litre, mass of an iron atom from nucleon count
  (scientific notation). **Named final number: about 3.2 × 10¹⁸ iron ions in
  a litre of well water.** 12 questions. (Optionally compared with a
  drinking-water guideline value — ledger `water:Fe-guideline` if sourced.)

### g9 ch3 `acids-bases-ph` — Acids, Bases and pH (~9 pp; 12 exos + problem)

- **Hook:** lemon juice, vinegar, a bar of soap and a drain cleaner sit on
  the same kitchen shelf; one scale, numbered 0 to 14, sorts them all.
- **Recall:** ions, (aq), formulas of ionic compounds (`ch:g9:ions`).
- **Sections:** 1. Acidic, basic and neutral solutions (H⁺ and HO⁻ ions;
  which outnumbers which); 2. The pH scale (0–14; 7 neutral at 25 °C; the
  lower, the more acidic); measuring it with pH paper and a pH meter; 3.
  Diluting an acid (the pH rises towards 7, about one unit per tenfold
  dilution — qualitative, no log); 4. Everyday acids and bases (vinegar,
  lemon, cola, stomach acid; soap, baking soda, bleach, drain cleaner); 5.
  Safety with corrosive products (pictograms, goggles, acid into water).
- **Definitions:**
  - `def:g9:acids-bases-ph:acidic` — acidic solution; basic solution;
    neutral solution (map ✓ "H⁺, OH⁻")
  - `def:g9:acids-bases-ph:ph` — pH (map ✓ "pH scale"; **contested** § C12:
    g12 adds pH = −log[H₃O⁺] without a second `\emph{pH}\index{pH}`)
  - `def:g9:acids-bases-ph:ph-paper` — pH paper; pH meter (**contested**
    § C11: the term "indicator" is g12's)
- **Statements:** prop "the more H⁺, the lower the pH"; prop "tenfold
  dilution, about one pH unit" (strong acid, told); method "measuring a pH
  with pH paper"; example dilution ladder pH 2 → 3 → 4.
- **Boxes:** `safety{\ghs{GHS05}\ghs{GHS07}}` hydrochloric acid;
  `safety{\ghs{GHS05}}` sodium hydroxide / drain cleaner;
  `inthelab[Diluting an acid]`.
- **Figures:** [S] the pH bar 0–14 coloured, with everyday products placed
  at their ledger values; [S] dilution ladder (beaker pics: 10 mL + 90 mL
  water, etc., with pH); [S] a pH paper strip compared with a colour chart
  (generic, labelled colours); [S] a pH meter and probe in a beaker (needs
  `phprobe` + `meterbox` pics); [AI] kitchen shelf with lemon, vinegar,
  soap (no labels); [AI] red-cabbage juice in a row of glasses from red to
  green (teacher's lab; review the colour order).
- **Ledger:** `ph:lemon`, `ph:vinegar`, `ph:cola`, `ph:seawater`,
  `ph:baking-soda`, `ph:soap`, `ph:bleach`, `ph:stomach`, `ph:drain` (USGS
  Water Science School "pH and Water" chart and/or primary pages; one
  source key), `ghs:HCl`, `ghs:NaOH`.
- **Exercises (12):** acidic / basic / neutral from pH; order products on
  the scale; effect of a tenfold dilution; which ion outnumbers which; read
  the pH bar; why dilution never makes an acid basic (★★); how many tenfold
  dilutions from pH 1 to pH 4 (★★); safety reasoning "acid into water"
  (★★★, told).
- **Problem — "The acid spill":** 1 L of a pH-2 acid is spilt in a lab
  sink. Part I — what pH 2 means; Part II — dilution: volume of water to
  reach pH 5 (three tenfold steps); Part III — why the lab neutralises with
  a base instead (told; neutralisation is a reaction of H⁺ with HO⁻ — named,
  the equation H⁺ + HO⁻ → H₂O written). **Named final number: 999 L of water
  to bring 1 L of the acid to pH 5.** 12 questions.

### g9 ch4 `metals-acids-corrosion` — Metals: Reactions with Acids and Corrosion (~9 pp; 12 exos + problem)

- **Hook:** a ship's hull streaked with rust, a zinc-coated garden gate
  shining after thirty years, a gold ring from an ancient tomb as bright as
  the day it was made.
- **Recall:** ions and their tests (`ch:g9:ions`); acidic solutions, H⁺
  (`ch:g9:acids-bases-ph`); pop test (`ch:g7:identifying-substances`);
  balancing (`ch:g8:balanced-equations`).
- **Sections:** 1. Metals in hydrochloric acid (iron, zinc, aluminium give
  hydrogen and metal ions; copper and gold do not); 2. Writing the equation
  with ions (Fe + 2 H⁺ → Fe²⁺ + H₂; the chloride ions as spectators); 3.
  Corrosion (rust needs oxygen and water; salt speeds it; aluminium's
  protective oxide skin; the copper patina); 4. Protecting metals (paint,
  oil, galvanising, stainless steel, a sacrificial zinc block told
  qualitatively — the electrochemistry is the Year 2 volume's).
- **Definitions:**
  - `def:g9:metals-acids-corrosion:spectator` — spectator ion (not in map)
  - `def:g9:metals-acids-corrosion:corrosion` — corrosion; rust (map ✓
    "corrosion (first look)")
  - `def:g9:metals-acids-corrosion:galvanising` — galvanising (not in map)
  (Must **not** define oxidation / reduction: g11 `redox` owns them and its
  hook re-introduces the word.)
- **Statements:** prop "metal + acid → metal ion + hydrogen" (for Fe, Zn,
  Al; not for Cu, Ag, Au); method "writing the ionic equation" (drop the
  spectators); example 2 Al + 6 H⁺ → 2 Al³⁺ + 3 H₂; prop "rusting needs both
  water and oxygen" (three-nail experiment).
- **Boxes:** `inthelab[Three nails, one week]` (teacher's demonstration
  results described); `safety` hydrochloric acid (from ch. 3) and hydrogen
  (`ghs:H2`).
- **Figures:** [S] three test tubes (iron, zinc, copper in acid) with and
  without bubbles; [S] the three-nail experiment (dry air with drying agent;
  boiled water under oil; water and air) and its result; [S] galvanised
  steel cross-section (zinc layer, scratch, zinc corroding first); [P] copper
  patina ✓ `File:Statue of Liberty 7.jpg` (PD); [AI] rusty ship hull in a
  harbour; [AI] galvanised steel railings.
- **Ledger:** `ghs:HCl`, `ghs:H2` (shared with ch. 3 / g7), `rho:Zn`
  (zinc density, used as data in the problem), `corrosion:cost` (global cost
  of corrosion, NACE IMPACT 2016) if the hook quotes it.
- **Exercises (12):** which metals react with acid; write ionic equations
  (Fe, Zn, Al, Mg); identify spectators; tests on the solution after the
  reaction (Fe²⁺ green); which conditions rust a nail (★★); why aluminium
  windows do not rust away (★★); why a scratched galvanised sheet still does
  not rust (★★★).
- **Problem — "How thick is the zinc?":** a teacher dissolves the zinc
  coat of a galvanised steel square in acid. Part I — reaction and tests;
  Part II — mass of zinc from the mass loss; Part III — thickness from mass,
  area and the density of zinc (data). **Named final number: the thickness
  of the zinc layer, about 85 µm** (exact value fixed with `rho:Zn` in
  Phase B). 12 questions.

### g9 ch5 `periodic-table-first-look` — The Periodic Table: A First Look (~9 pp; 12 exos + problem)

- **Hook:** a classroom wall chart of 118 boxes; in 1869 it had 63, and
  gaps — and a chemist bold enough to describe the elements missing from
  the gaps.
- **Recall:** element, atomic number (`ch:g9:inside-the-atom`); symbols
  (`ch:g7:atoms-and-molecules`); ions (`ch:g9:ions`).
- **Sections:** 1. A table of the elements (ordered by Z; rows are periods,
  columns are groups; 118 known); 2. Metals and non-metals (where they sit;
  properties: shine, conduct, bend vs dull, brittle, many gases); 3. Columns
  that behave alike (lithium, sodium, potassium with water — teacher; the
  unreactive gases of the last column; named families wait for g10); 4.
  Mendeleev's idea (1869: order by atomic weight, columns by properties,
  gaps and predictions — eka-silicon and germanium).
- **Definitions:**
  - `def:g9:periodic-table-first-look:periodic-table` — periodic table
    (map ✓)
  - `def:g9:periodic-table-first-look:period` — period; group (map ✓
    "rows and columns"; **homographs** § C10: STOP "period", "group")
  - `def:g9:periodic-table-first-look:metal` — metal; non-metal
- **Statements:** prop "elements of a column behave alike"; method
  "reading a cell of the table" (Z, symbol, name, atomic weight); example
  sodium vs potassium in water (described).
- **Boxes:** `history[Mendeleev's gaps, 1869–1886]`; `inthelab[Alkali
  metals in water]` (teacher, behind a screen) with `safety` sodium.
- **Figures:** [S] the full periodic table (118 cells, metals / non-metals
  coloured) — needs the `\omperiodictable` macro (§ style needs); [S] the
  first 20 elements enlarged; [S] Mendeleev's prediction table (eka-silicon
  predicted vs germanium measured); [P] Mendeleev ✓ `File:Dmitri Mendeleev
  1890s.jpg` (PD); [P] his table ✓ `File:Mendeleev's periodic table (1869
  year).jpg` (PD, 619 px — check print size) or ✓ `File:Mendelejevs
  periodiska system 1871.png` (PD); [P] element samples (sulfur, copper) —
  CC photos to find in Phase B; [AI] none planned.
- **Ledger:** `aw:` rows (shared) for the problem; `mend:eka-si-aw`,
  `mend:eka-si-rho` (Mendeleev's 1871 predictions), `rho:Ge` (germanium);
  source to find (Mendeleev 1871 translation / a history-of-chemistry
  primary page); `ghs:Na`.
- **Exercises (12):** period and group of an element from Z; metal or
  non-metal; elements of the same column; read the table; why gaps were a
  strength (★★); which element is below sodium (★★); predict a property by
  averaging neighbours (★★★).
- **Problem — "Mendeleev's gap":** Part I — locating Si, Sn, Ga, As around
  the gap; Part II — averaging their atomic weights (shared `aw:` rows):
  (28.1 + 118.7 + 69.7 + 74.9)/4; Part III — germanium discovered 1886,
  comparison. **Named final number: the predicted atomic weight of
  eka-silicon, 72.9** (germanium: 72.6). 12 questions.

### g9 ch6 `elements-universe-earth` — Elements in the Universe and on Earth (~9 pp; 12 exos + problem)

- **Hook:** "We are made of star-stuff": the iron in blood, the calcium in
  bones and the oxygen we breathe were made inside stars that died before
  the Sun was born.
- **Recall:** element (`ch:g9:inside-the-atom`); periodic table
  (`ch:g9:periodic-table-first-look`); air composition
  (`ch:g4:air-a-mixture-of-gases`).
- **Sections:** 1. Elements of the Universe (hydrogen and helium; the rest
  about 2 % by mass); 2. Made in stars (told: H and He from the first
  minutes, heavier elements in stars and their explosions — the physics is
  the physics book's); 3. The Earth: crust, whole Earth, oceans, air; 4.
  The human body (O, C, H, N, Ca, P by mass); 5. The same atoms, recycled
  (atoms are conserved; a carbon atom's journey).
- **Definitions:**
  - `def:g9:elements-universe-earth:abundance` — abundance (mass fraction of
    an element in a body of matter) (map ✓)
- **Statements:** prop "a few elements make up most of each body";
  example "a carbon atom's journey" (rock → CO₂ → leaf → animal → air);
  method "reading an abundance chart".
- **Boxes:** `history[Cecilia Payne and the hydrogen of the stars, 1925]`
  (photo only if a PD/CC portrait is verified).
- **Figures:** [S] four bar charts (Universe, crust, ocean, human body),
  pgfplots with inline ledger coordinates; [S] Earth's layers cross-section
  (crust, mantle, core with their main elements); [S] carbon-atom journey
  loop; [P] Crab Nebula ✓ `File:Crab Nebula.jpg` (PD, NASA) — elements made
  in stars; [AI] coastal cliff with sea and sky (crust, ocean, air in one
  picture).
- **Ledger:** ~25 rows: `ab:univ:H`, `ab:univ:He`, `ab:univ:Z` (Asplund et
  al. 2009 ARA&A); `ab:crust:O`, `:Si`, `:Al`, `:Fe`, `:Ca`, `:Na`, `:Mg`,
  `:K` (a citable crust table — Rudnick & Gao 2003 / USGS; to find);
  `ab:earth:Fe`, `:O`, `:Si`, `:Mg` (McDonough 2003 whole-Earth); `ab:sea:Cl`,
  `:Na`, `:Mg`, `:S` (Millero et al. 2008 reference composition);
  `ab:body:O`, `:C`, `:H`, `:N`, `:Ca`, `:P` (a citable reference to find).
- **Exercises (12):** read each chart; compare crust and whole Earth (iron
  sinks to the core); why the air has no silicon; percentages of a 70 kg
  body; scientific notation of atom counts (★★); which element is common in
  all four charts (★★); mass of calcium in a body (★★★).
- **Problem — "How many atoms am I?":** Part I — read the body chart;
  Part II — mass of an oxygen atom from nucleon count; Part III — counts for
  a 70 kg body. **Named final number: about 1.7 × 10²⁷ oxygen atoms in a
  70 kg body.** 12 questions.

---

## Grade 10

### g10 ch1 `chemical-species` — Chemical Species, Natural and Synthetic (~11 pp; 15 exos 5/6/4 + problem 18–22 q, Parts I–IV)

- **Hook:** vanilla ice cream: the flavour may come from a bean grown on a
  tropical vine, or from a factory — and the molecule that tastes of vanilla
  is the same.
- **Recall:** chemical species, pure substance
  (`ch:g6:pure-substances-and-mixtures`); paper chromatography
  (`ch:g7:identifying-substances`); solubility, miscibility
  (`ch:g6:solutions-and-solubility`); separation methods
  (`ch:g3:separating-mixtures`).
- **Sections:** 1. Natural and synthetic species (vanillin; salicylic acid
  from willow bark to aspirin); 2. Extracting a species (maceration,
  infusion, decoction; distillation and hydrodistillation of lavender;
  liquid–liquid extraction with a separating funnel and the choice of
  solvent from a data table); 3. Thin-layer chromatography (stationary and
  mobile phases, deposits, eluent, revealing under UV or with iodine); 4.
  The retention factor and identification; purity; 5. Identifying a species
  by its physical constants (melting point on a melting-point apparatus,
  boiling point, density).
- **Definitions:**
  - `def:g10:chemical-species:natural` — natural species; synthetic species
    (not in map; § C8 "synthetic material" vs "synthetic species")
  - `def:g10:chemical-species:extraction` — extraction; liquid–liquid
    extraction (map ✓ for g10; **contested** § C6 with g11 `dissolution`)
  - `def:g10:chemical-species:distillation` — distillation;
    hydrodistillation (not in map; § C15)
  - `def:g10:chemical-species:tlc` — thin-layer chromatography; stationary
    phase; eluent (map ✓ "TLC")
  - `def:g10:chemical-species:retention-factor` — retention factor (map ✓)
- **Statements:** method "choosing an extraction solvent" (dissolves the
  species well, immiscible with water, little hazard); method "running a
  TLC"; prop "two species with the same Rf in the same conditions may be
  the same species; different Rf, certainly different"; example lavender oil
  vs linalool reference.
- **Boxes:** `inthelab[A TLC plate]`; `safety` cyclohexane, ethyl
  ethanoate (PubChem); `history[From willow bark to aspirin, 1897]`.
- **Figures:** [S] hydrodistillation set (rbflask + heating mantle + still
  head + thermometer + sloped condenser + receiving erlenmeyer; water in at
  the low end) — needs pics; [S] separating funnel with two layers, labels
  (organic above or below by density, data); [S] TLC tank and developed
  plate with Rf construction; [S] solvent data table-figure; [AI] lavender
  field (hook); [AI] vanilla pods beside a dish of white vanillin crystals;
  [AI] willow tree by a river.
- **Ledger:** `rho:cyclohexane`, `rho:ethyl-acetate`, `rho:dichloromethane`,
  `mp:vanillin`, `mp:aspirin`, `mp:salicylic`, `bp:linalool`,
  `ghs:cyclohexane`, `ghs:ethyl-acetate`, `sol:` qualitative statements
  (PubChem / NIST).
- **Exercises (15):** ★ vocabulary, Rf from a plate, natural or synthetic;
  ★★ choose a solvent from a table, read a TLC of a mixture, identify by
  melting point, order the steps of a hydrodistillation; ★★★ purity from a
  TLC, design an extraction protocol on paper, explain why a synthetic
  vanillin has no "less natural" taste.
- **Problem — "The scent of lavender":** Part I — hydrodistillation
  (apparatus, roles); Part II — extracting the oil from the distillate with
  cyclohexane (data table, layer order); Part III — TLC of the oil against
  linalool and linalyl acetate (Rf computed); Part IV — the oil's mass from
  100 g of flowers (density and volume given). **Named final number: the
  mass of oil from 100 g of flowers, 0.90 g** (exercise data). ~20 questions.

### g10 ch2 `electron-shells` — Electron Shells and the Periodic Table (~11 pp; 15 exos + problem)

- **Hook:** neon tubes glowing red-orange, a halogen lamp, salt on chips:
  why do neon, chlorine and sodium behave so differently although they sit
  side by side in the table?
- **Recall:** nucleus, electrons, Z (`ch:g9:inside-the-atom`); periodic
  table, periods, groups (`ch:g9:periodic-table-first-look`); ions
  (`ch:g9:ions`).
- **Sections:** 1. Electron configuration (shells and subshells 1s, 2s, 2p,
  3s, 3p; filling order up to Z = 18, then 4s for K and Ca); 2. Valence
  electrons; 3. The table rebuilt from configurations (period = outer shell,
  column = valence electrons; s and p blocks named); 4. Families (alkali
  metals, halogens, noble gases); 5. Stable ions and the noble-gas rule
  (duet and octet).
- **Definitions:**
  - `def:g10:electron-shells:configuration` — electron configuration; shell;
    subshell (map ✓; "shell" homograph § C17)
  - `def:g10:electron-shells:valence` — valence electrons; core electrons
    (map ✓ "valence")
  - `def:g10:electron-shells:family` — chemical family; alkali metals;
    halogens; noble gases (not in map as words; outline line "families of
    the periodic table"; **contested** § C9 with g11 `functional-groups`)
  - `def:g10:electron-shells:octet` — duet rule; octet rule (map ✓ "octet")
- **Statements:** method "writing a configuration" (fill in order, at most
  2 / 2 / 6 / 2 / 6); prop "elements of a column have the same number of
  valence electrons"; prop "the noble-gas rule for monatomic ions" (Na⁺,
  Mg²⁺, Al³⁺, O²⁻, F⁻, Cl⁻, S²⁻); remark: the rule has exceptions (iron)
  and its quantum reasons are the Year 1 volume's.
- **Boxes:** `inthelab[Sodium in water]` (teacher, small piece, screen);
  `safety` sodium, chlorine.
- **Figures:** [S] filling-order diagram of subshells (boxes with electron
  counts, no spin arrows); [S] the first three periods with configurations
  in the cells (the periodic-table macro with a "config" key); [S] the
  families highlighted on the full table; [S] Na → Na⁺ and Cl → Cl⁻ with
  configurations; [P] sodium under oil ✓ `File:Na (Sodium).jpg` (CC BY-SA
  3.0); [P] chlorine ampoule ✓ `File:Chlorine ampoule.jpg` (CC BY-SA 3.0);
  [AI] neon tubes bent into abstract curves at night (no letters).
- **Ledger:** `ghs:Na`, `ghs:Cl2`.
- **Exercises (15):** ★ configurations of 5 atoms, valence count, period
  and column; ★★ ions by the noble-gas rule, family from configuration,
  formula of an ionic compound from two elements, read the table figure,
  identify an element from clues; ★★★ explain why helium sits with neon
  though it has 2 valence electrons, an element from its ion's
  configuration, potassium's 4s.
- **Problem — "Ruby, sapphire and corundum":** gems made of aluminium oxide.
  Part I — configurations of Al and O; Part II — their stable ions; Part
  III — the formula Al₂O₃; Part IV — electrons transferred per formula unit
  (6), mass of a formula unit from nucleon counts, per gram. **Named final
  number: about 3.5 × 10²² electrons transferred to make 1 g of corundum.**
  ~19 questions.

### g10 ch3 `lewis-and-shape` — Lewis Structures and the Shape of Molecules (~11 pp; 15 exos + problem)

- **Hook:** carbon dioxide is a straight molecule and water a bent one;
  that one difference is part of why water is a liquid on Earth and carbon
  dioxide a gas.
- **Recall:** valence electrons, duet / octet rules
  (`ch:g10:electron-shells`); molecules and models
  (`ch:g7:atoms-and-molecules`).
- **Sections:** 1. The covalent bond (a shared pair; H forms 1 bond, O 2,
  N 3, C 4, Cl 1); 2. Lewis structures (bonding and lone pairs; method;
  double and triple bonds: O₂, N₂, CO₂, C₂H₄, HCN, methanal); 3. The shape of
  molecules (electron pairs as far apart as possible: linear, bent, trigonal
  planar, tetrahedral, pyramidal); 4. Drawing molecules in space (wedge and
  dash; ball-and-stick and space-filling models).
- **Definitions:**
  - `def:g10:lewis-and-shape:covalent-bond` — covalent bond (map ✓)
  - `def:g10:lewis-and-shape:lone-pair` — bonding pair; lone pair
  - `def:g10:lewis-and-shape:lewis-structure` — Lewis structure (map ✓)
  - `def:g10:lewis-and-shape:multiple-bond` — double bond; triple bond
  - (shape names — linear, bent, tetrahedral… — in a `proposition` table,
    no terms; VSEPR is the Year 1 volume's word)
- **Statements:** method "drawing a Lewis structure" (count valence
  electrons, skeleton, bonds, lone pairs, check octets); prop "the shape
  follows from the number of electron groups around the central atom"
  (admitted at this level; "derived in the Year 1 volume"); examples CH₄,
  NH₃, H₂O, CO₂, C₂H₄; notation wedge / dash.
- **Boxes:** `history[Lewis's shared pair, 1916]` (no portrait: none found
  on Commons).
- **Figures:** [S] Lewis structures table (chemfig `\lewis`); [S]
  ball-and-stick of CH₄, NH₃, H₂O with angles annotated (atom styles,
  perspective); [S] CO₂ linear vs H₂O bent side by side with lone pairs; [S]
  methane in a cube (H at alternate corners) for the problem; [AI] four
  balloons tied at their knots forming a tetrahedron (analogy illustrated,
  not the naming device); [AI] none else.
- **Ledger:** `ang:H2O`, `ang:NH3` (NIST CCCBDB experimental geometries);
  the tetrahedral angle is computed (arccos(−1/3)).
- **Exercises (15):** ★ count bonds per atom, Lewis structures of H₂, HCl,
  H₂O, NH₃, CH₄; ★★ CO₂, N₂, C₂H₄, HCN, methanal, shapes from structures,
  read the angle figure; ★★★ ozone's single Lewis structure (resonance
  avoided: one structure, a remark that the Year 1 volume refines it), an
  isomer pair C₂H₆O, why NH₃'s angle is below 109.5°.
- **Problem — "A molecule in a cube":** designing the carbon balls of a
  molecular model kit. Part I — Lewis structures of CH₄, NH₃, H₂O; Part II —
  predicted shapes; Part III — the cube construction (face diagonal,
  half body diagonal, Pythagoras); Part IV — the half-angle from its sine.
  **Named final number: the angle between two holes of a carbon ball,
  109.5°.** ~19 questions.

### g10 ch4 `the-mole` — The Mole and Molar Mass (~11 pp; 15 exos + problem)

- **Hook:** a bank weighs a bag of coins instead of counting them; chemists
  do the same with atoms, only the bag holds 602 214 076 000 000 000 000 000
  of them.
- **Recall:** masses of atoms in scientific notation
  (`ch:g9:inside-the-atom`); formulas (`ch:g7:atoms-and-molecules`).
- **Sections:** 1. Counting by weighing: the amount of substance and the
  mole (the 2019 definition: exactly N_A entities); 2. The Avogadro
  constant; 3. Molar mass (atomic, from the table; molecular, by adding); 4.
  From mass to amount and back (n = m/M); 5. Gases: the molar volume (from
  physics data; 24.0 L/mol at 20 °C and 1 atm, computed).
- **Definitions:**
  - `def:g10:the-mole:amount` — amount of substance; mole (map ✓;
    "mole" homograph § C17)
  - `def:g10:the-mole:avogadro` — Avogadro constant (map ✓)
  - `def:g10:the-mole:molar-mass` — molar mass; atomic molar mass (map ✓)
  - `def:g10:the-mole:molar-volume` — molar volume (not in map; placed here,
    first use; recalled in g10 `reaction-progress-table`)
- **Statements:** prop n = N / N_A; prop M(molecule) = Σ M(atoms); method
  "from mass to amount"; example a mole of water, of salt, of sugar on a
  bench.
- **Boxes:** `history[Avogadro's hypothesis, 1811]`.
- **Figures:** [S] the triangle mass ↔ amount ↔ number of entities (× M,
  × N_A); [S] one mole each of water, salt, sugar, iron as beaker / heap
  drawings to scale of volume (densities as data); [P] Avogadro ✓
  `File:Avogadro Amedeo.jpg` (PD); [AI] bank teller weighing coins (hook);
  [AI] the silicon sphere of the Avogadro project — **no**: a real object;
  a photograph only if a CC one is verified (Phase B), otherwise omitted.
- **Ledger:** `const:NA`, `const:R` (shared); `ocean:volume` (NOAA),
  `rho:` rows for the to-scale figure (water, NaCl, sucrose, Fe).
- **Exercises (15):** ★ M of 5 molecules, n from m, m from n, N from n;
  ★★ entities in a drop, gas volumes, compare amounts, read the triangle;
  ★★★ atoms in a gold ring, molecules of air in a room, the 1 kg silicon
  sphere's atom count.
- **Problem — "Kelvin's glass of water":** pour a glass of water into the
  sea, wait for it to mix through all the oceans, draw a glass again. Part I
  — M of water, amount in 250 mL; Part II — molecules in the glass; Part
  III — ocean volume (ledger) and molecules of the first glass per litre;
  Part IV — interpretation. **Named final number: about 1600 molecules of
  the first glass in the second.** ~19 questions.

### g10 ch5 `concentration-and-dilution` — Concentration and Dilution (~11 pp; 15 exos + problem)

- **Hook:** a hospital drip bag reads "0.9 % sodium chloride": a nurse
  could make it from salt and water, but only with the right glassware.
- **Recall:** solute, solvent, solubility (`ch:g6:solutions-and-solubility`);
  mole, molar mass (`ch:g10:the-mole`).
- **Sections:** 1. Mass concentration (g/L) — not to be confused with
  solubility, the largest possible one; 2. Molar concentration (mol/L), and
  C_m = c · M; 3. Preparing a solution by dissolving (balance, volumetric
  flask, the mark); 4. Diluting (dilution factor; the amount of solute is
  kept: c₁V₁ = c₂V₂; pipette and volumetric flask); 5. A calibration scale
  (a range of standard solutions compared by colour).
- **Definitions:**
  - `def:g10:concentration-and-dilution:mass-concentration` — mass
    concentration (map ✓ "concentration")
  - `def:g10:concentration-and-dilution:molar-concentration` — molar
    concentration
  - `def:g10:concentration-and-dilution:dilution` — dilution; stock
    solution; dilution factor (map ✓)
  - `def:g10:concentration-and-dilution:standard` — standard solution;
    calibration scale
- **Statements:** prop C_m = c · M; prop "the amount of solute is the same
  before and after a dilution"; method "preparing by dissolving"; method
  "preparing by dilution"; example the drip bag.
- **Boxes:** `inthelab[Filling to the mark]` (meniscus at eye level);
  `safety` copper sulfate (from g7) for the colour scale.
- **Figures:** [S] preparing by dissolving: four steps (balance, funnel,
  volumetric flask half full, filled to the mark) — needs `volflask`, `balance`
  pics; [S] dilution: pipette from the stock beaker → volumetric flask —
  needs `pipette`; [S] colour scale: six test tubes of graded blue and the
  unknown; [S] the meniscus at the mark (eye level vs wrong); [AI] hospital
  drip bag on a stand (no text); [AI] orange squash diluted in a jug (hook,
  everyday).
- **Ledger:** `saline:NaCl` (0.9 %, 9 g/L — a pharmacopoeia / WHO model
  formulary entry), `ghs:CuSO4` (from g7).
- **Exercises (15):** ★ C_m and c from masses and volumes, the mass to weigh,
  dilution factor; ★★ volume of stock to take, glassware choice, read the
  colour scale, convert C_m ↔ c; ★★★ serial dilutions, concentration of each
  ion in a CaCl₂ solution (dissociation told; full treatment g11), error
  from reading the meniscus.
- **Problem — "The drip bag":** Part I — 0.9 % as g/L, mass of salt in a
  500 mL bag; Part II — molar concentration; Part III — preparing it from a
  20 % (200 g/L) ampoule; Part IV — glassware and protocol. **Named final
  number: 22.5 mL of the 20 % ampoule for one 500 mL bag.** ~19 questions.

### g10 ch6 `reaction-progress-table` — The Reaction-Progress Table (~11 pp; 15 exos + problem)

- **Hook:** a car crash: in 30 milliseconds a solid in the steering wheel
  turns into some 60 litres of nitrogen. How much solid is needed?
- **Recall:** balanced equations, coefficients (`ch:g8:balanced-equations`);
  amount, molar mass, molar volume (`ch:g10:the-mole`); concentration
  (`ch:g10:concentration-and-dilution`).
- **Sections:** 1. Describing a chemical system (initial state, final
  state); 2. The extent x and the progress table (method); 3. The limiting
  reactant and the maximum extent x_max; the final state of a total
  reaction; 4. The stoichiometric mixture; 5. Gases and solutions in the
  table (amounts from volumes and concentrations).
- **Definitions:**
  - `def:g10:reaction-progress-table:system` — chemical system; initial
    state; final state (not in map; "system" homograph § C17)
  - `def:g10:reaction-progress-table:extent` — extent of reaction; progress
    table (map ✓)
  - `def:g10:reaction-progress-table:limiting` — limiting reactant; maximum
    extent; total reaction (map ✓; "total reaction" recalled by g12
    `equilibrium`)
  - `def:g10:reaction-progress-table:stoichiometric` — stoichiometric
    mixture
- **Statements:** method "filling a progress table"; method "finding the
  limiting reactant" (solve n_i − ν_i x = 0 for each, smallest x); prop "in
  a stoichiometric mixture all reactants run out together"; example
  magnesium in hydrochloric acid with balloons.
- **Boxes:** `inthelab[Balloons on flasks]` (teacher: fixed acid, growing
  magnesium; balloons grow then stop).
- **Figures:** [S] amounts vs x lines (pgfplots exact expressions) crossing
  zero at x_max; [S] the balloon series (erlenmeyer pics with balloons of
  growing then equal size); [S] the annotated progress table (a tabular
  figure); [AI] airbag deploying in a crash-test lab (industrial scene, no
  dummy text); [AI] none else.
- **Ledger:** `ghs:NaN3`; `const:R` for V_m (computed); airbag volume as
  exercise data ("suppose 60 L").
- **Exercises (15):** ★ fill tables, x_max, limiting reactant (5 short);
  ★★ stoichiometric masses, gas volumes, read the lines figure, two
  reactants in solution, percentages of excess; ★★★ choose initial amounts
  for a stoichiometric mixture, a two-step table, the balloon experiment
  plateau.
- **Problem — "The airbag":** Part I — 2 NaN₃ → 2 Na + 3 N₂ and the
  sodium-removal reaction 10 Na + 2 KNO₃ → K₂O + 5 Na₂O + N₂; Part II —
  progress table of the decomposition; Part III — second table,
  stoichiometric KNO₃; Part IV — nitrogen from both steps for a 60 L bag at
  20 °C. **Named final number: about 102 g of sodium azide.** ~20 questions.

### g10 ch7 `synthesis-yield` — Synthesis: Yield and Purity (~11 pp; 15 exos + problem)

- **Hook:** a tablet of aspirin, the most widely made drug in history, made
  in steel reactors from a substance first found in willow bark.
- **Recall:** extraction, TLC, Rf, melting point (`ch:g10:chemical-species`);
  filtering (`ch:g3:separating-mixtures`); progress table, limiting
  reactant (`ch:g10:reaction-progress-table`).
- **Sections:** 1. The steps of a synthesis (reaction, isolation,
  purification, analysis); 2. Heating under reflux (why and how; water in
  at the bottom of the condenser); 3. Isolating and purifying (vacuum
  filtration, washing, drying; recrystallisation: soluble hot, little
  soluble cold); 4. Analysing the product (melting point, TLC); 5. Yield.
- **Definitions:**
  - `def:g10:synthesis-yield:synthesis` — synthesis; crude product
  - `def:g10:synthesis-yield:reflux` — heating under reflux (map ✓)
  - `def:g10:synthesis-yield:vacuum-filtration` — vacuum filtration (not in
    map; recalls g3 filtering)
  - `def:g10:synthesis-yield:recrystallisation` — recrystallisation (map ✓)
  - `def:g10:synthesis-yield:yield` — yield (map ✓; "yield" homograph
    § C17)
- **Statements:** prop "yield = n(obtained) / n(maximum)"; method "planning
  the steps"; method "recrystallising a solid"; example aspirin from
  salicylic acid and ethanoic anhydride.
- **Boxes:** `inthelab[Making aspirin]`; `safety` ethanoic anhydride,
  salicylic acid (PubChem).
- **Figures:** [S] reflux set (rbflask + condenser + heating mantle; water
  in / out arrows) — needs `heatingmantle`; [S] Büchner filtration (funnel
  + filter flask + vacuum line) — needs `buchner`; [S] recrystallisation in
  four steps; [S] TLC: crude vs recrystallised vs reference; [AI]
  pharmaceutical plant reactor hall (industrial); [AI] aspirin tablets
  blister (no text).
- **Ledger:** `mp:aspirin`, `mp:salicylic` (from ch. 1), `sol:aspirin-cold`,
  `sol:aspirin-hot` (PubChem) if quoted, `rho:acetic-anhydride`,
  `ghs:acetic-anhydride`, `ghs:salicylic`.
- **Exercises (15):** ★ steps in order, role of the condenser, yield from
  masses; ★★ limiting reactant and theoretical mass, recrystallisation
  reasoning, read the TLC, why water enters at the bottom; ★★★ yield
  after losses in two steps, choose a recrystallisation solvent from a
  table, judge purity from a melting point.
- **Problem — "Making aspirin":** Part I — the equation and the roles;
  Part II — progress table (salicylic acid 3.0 g, anhydride 6.0 mL, density
  data), theoretical mass; Part III — crude 3.6 g wet, dried 3.3 g,
  recrystallised 2.7 g; Part IV — melting point and TLC checks. **Named final
  number: the yield of the synthesis, about 69 %** (fixed in Phase B with
  `tools/molar_mass.py`). ~20 questions.

---

## Grade 11

(`07-redox` is the pilot; its definitions: `def:g11:redox:oxidant` —
oxidant, reductant; `def:g11:redox:oxidation` — oxidation, reduction;
`def:g11:redox:couple` — redox couple, half-equation;
`def:g11:redox:reaction` — redox reaction.)

### g11 ch1 `absorbance` — Colour and Absorbance (~11 pp; 15 exos + problem)

- **Hook:** a bright blue sports drink: its colour comes from a few
  milligrams of a dye per litre — how can a laboratory measure so little?
- **Recall:** concentration, dilution, calibration scale
  (`ch:g10:concentration-and-dilution`).
- **Sections:** 1. The colour of a solution (white light, the colours
  absorbed and the colour seen; the colour wheel — wavelengths are physics,
  used as known); 2. The absorption spectrum (A vs λ, λ_max); 3. Absorbance
  and the spectrophotometer (absorbance defined as the reading of the
  instrument, 0 for the solvent, larger the more light is absorbed — **no
  logarithm**: the definition A = log(I₀/I) waits for the grade 12
  reader, a remark points there); 4. The Beer–Lambert law (A = ε ℓ c,
  admitted, "derived in a university volume"); 5. Finding a concentration
  from a calibration line (method).
- **Definitions:**
  - `def:g11:absorbance:complementary` — complementary colours (not in map)
  - `def:g11:absorbance:spectrum` — absorption spectrum
  - `def:g11:absorbance:absorbance` — absorbance (map ✓)
  - `def:g11:absorbance:epsilon` — molar absorption coefficient
  - `def:g11:absorbance:calibration-line` — calibration line
- **Statements:** prop "a solution looks the colour complementary to the
  one it absorbs most"; prop Beer–Lambert (admitted); method "measuring a
  concentration with a calibration line" (λ_max, blank, standards, line,
  read); remark: the law holds for dilute solutions only.
- **Boxes:** `inthelab[Zeroing the spectrophotometer]`.
- **Figures:** [F] `absorbance`: (a) absorption spectrum of the blue dye
  E133 (synthetic Gaussian-sum band at the ledger λ_max) and of potassium
  permanganate; (b) calibration line with five standard points (exact
  proportional values + fixed small offsets, documented as synthetic) —
  test: maximum at the ledger λ_max, line through the origin with slope
  ε ℓ; [S] spectrophotometer principle (lamp → prism → slit → cuvette →
  detector → display) — needs `cuvette` pic; [S] colour wheel with
  complementary pairs; [AI] blue sports drink on a gym bench (no label
  text); [AI] spectrophotometer on a lab bench (no display digits).
- **Ledger:** `lmax:E133` (JECFA / EU specification for Brilliant Blue FCF),
  `eps:E133` (specific absorbance → molar coefficient computed),
  `lmax:KMnO4`, `adi:E133` (EFSA 2010 ADI 6 mg/kg bw/day), `ghs:KMnO4`
  (exists).
- **Exercises (15):** ★ colour seen from colour absorbed, read λ_max, A
  proportional to c; ★★ concentration from a calibration line, choose λ, a
  dilution before measuring, ε from a measurement, read the spectrum; ★★★
  detect a deviation at high concentration, mixture of two dyes at two
  wavelengths, error from a wrong blank.
- **Problem — "The blue of a sports drink":** Part I — colour and
  spectrum; Part II — calibration line from standards; Part III — the
  drink diluted, its absorbance, the dye concentration; Part IV — the
  acceptable daily intake. **Named final number: how many 500 mL bottles a
  30 kg child could drink before reaching the ADI** (value fixed in Phase B
  from the ledger rows). ~20 questions.

### g11 ch2 `polarity-and-cohesion` — Electronegativity, Polarity and Intermolecular Forces (~11 pp; 15 exos + problem)

- **Hook:** a gecko walks up a glass window and hangs by one toe; water,
  a light molecule, boils at 100 °C while heavier hydrogen sulfide is a gas.
  Both stories are about forces between molecules.
- **Recall:** covalent bond, Lewis structures, shapes
  (`ch:g10:lewis-and-shape`); ions, ionic compounds (`ch:g9:ions`).
- **Sections:** 1. Electronegativity (Pauling values; trends across the
  table); 2. Polar bonds and partial charges; polar and non-polar molecules
  (geometry decides: CO₂ vs H₂O; no "dipole moment" term — Year 1's); 3.
  Van der Waals interactions (grow with size); 4. Hydrogen bonds (H on N, O,
  F facing a lone pair of N, O, F); 5. Cohesion of solids (ionic solids,
  molecular solids) and what it explains (melting and boiling
  temperatures).
- **Definitions:**
  - `def:g11:polarity-and-cohesion:electronegativity` — electronegativity
    (map ✓)
  - `def:g11:polarity-and-cohesion:polar-bond` — polar bond; partial charge
  - `def:g11:polarity-and-cohesion:polar-molecule` — polar molecule;
    non-polar molecule (map ✓ "polarity")
  - `def:g11:polarity-and-cohesion:van-der-waals` — van der Waals
    interaction (map ✓ via outline)
  - `def:g11:polarity-and-cohesion:hydrogen-bond` — hydrogen bond (map ✓)
  - `def:g11:polarity-and-cohesion:molecular-solid` — molecular solid
    (not in map)
- **Statements:** prop "a bond between atoms whose electronegativities
  differ is polar"; method "is a molecule polar?" (polar bonds + shape);
  prop "the higher the cohesion, the higher the change-of-state
  temperatures"; example the hydride series.
- **Boxes:** none mandatory; `history[Pauling's scale, 1932]` optional.
- **Figures:** [S] electronegativity table of periods 1–3 (periodic-table
  macro with values, ledger); [S] H₂O with δ⁺ / δ⁻ and the centres of charge;
  CO₂ with cancelling polar bonds; [S] hydrogen bonds between water
  molecules (dashed, angles right); [S] boiling points of the hydrides of
  groups 14–17 vs period (pgfplots, inline ledger points); [P] snowflake ✓
  `File:SnowflakesWilsonBentley.jpg` (PD) — hydrogen-bonded ice;
  [AI] gecko on a glass pane (hook).
- **Ledger:** ~25 rows: `en:H`, `en:C`, `en:N`, `en:O`, `en:F`, `en:Na`,
  `en:Mg`, `en:Al`, `en:Si`, `en:P`, `en:S`, `en:Cl`, `en:Li`, `en:Be`,
  `en:B` (Pauling, PubChem periodic table / a primary compilation);
  `bp:CH4`, `bp:SiH4`, `bp:GeH4`, `bp:SnH4`, `bp:NH3`, `bp:PH3`, `bp:AsH3`,
  `bp:SbH3`, `bp:H2O`, `bp:H2S`, `bp:H2Se`, `bp:H2Te`, `bp:HF`, `bp:HCl`,
  `bp:HBr`, `bp:HI` (NIST WebBook phase-change data).
- **Exercises (15):** ★ which atom is δ⁻, polar bond or not, compare
  electronegativities; ★★ polar molecule or not (CH₂Cl₂, CCl₄, NH₃, CO₂,
  BF₃), H-bond donors, explain a boiling-point order, read the hydride
  chart; ★★★ why ethanol boils far above propane though similar masses,
  why ice floats (told: the open hydrogen-bonded network), predict which
  solid melts higher.
- **Problem — "Why does water boil at 100 °C?":** Part I — Lewis structures
  and polarity of H₂O, H₂S, H₂Se, H₂Te; Part II — hydrogen bonds; Part III —
  the boiling-point trend of the heavier hydrides (ledger), linear
  extrapolation to period 2; Part IV — the gap explained. **Named final
  number: the boiling point water "should" have without hydrogen bonds,
  about −80 °C** (fixed in Phase B from the ledger rows). ~20 questions.

### g11 ch3 `dissolution` — Dissolving Ionic and Molecular Solids (~11 pp; 15 exos + problem)

- **Hook:** a pinch of salt vanishes in water but sits unchanged in
  cooking oil; a greasy pan comes clean with a drop of washing-up liquid.
- **Recall:** solubility, miscibility (`ch:g6:solutions-and-solubility`);
  ions, ionic compounds (`ch:g9:ions`); polarity, hydrogen bonds
  (`ch:g11:polarity-and-cohesion`); extraction
  (`ch:g10:chemical-species`); molar concentration
  (`ch:g10:concentration-and-dilution`).
- **Sections:** 1. Dissolving an ionic solid: dissociation, solvation
  (hydration), dispersion — NaCl(s) → Na⁺(aq) + Cl⁻(aq); 2. Concentrations of
  the ions ([Cl⁻] = 2c for CaCl₂); 3. Polarity and solubility ("like
  dissolves like"; ethanol miscible with water; iodine prefers
  cyclohexane); 4. Liquid–liquid extraction explained (why a solvent
  extracts: polarity; the procedure is recalled from g10); 5. Soaps and
  amphiphilic molecules (head and tail, micelles, how soap removes grease;
  hard water and scum).
- **Definitions:**
  - `def:g11:dissolution:dissociation` — dissociation
  - `def:g11:dissolution:solvation` — solvation; hydration (map ✓
    "solvation")
  - `def:g11:dissolution:hydrophilic` — hydrophilic; hydrophobic
  - `def:g11:dissolution:amphiphilic` — amphiphilic (map ✓ "amphiphiles");
    micelle
  - (no "extraction" here: § C6)
- **Statements:** prop "a polar solvent dissolves polar and ionic species;
  a non-polar one non-polar species"; method "concentration of each ion"
  (from the dissolution equation); example soap: sodium stearate, head
  carboxylate, tail C₁₇.
- **Boxes:** `inthelab[Extracting iodine]`; `safety` iodine, cyclohexane.
- **Figures:** [S] dissolving NaCl: ions leaving the crystal edge, water
  molecules oriented (O towards Na⁺, H towards Cl⁻) — atom styles; [S]
  soap molecule (chemfig skeletal) and its head-and-tail sketch; [S]
  micelle around a grease droplet (cross-section); [S] separating funnel:
  brown aqueous iodine before, violet cyclohexane layer after; [AI]
  washing greasy hands in soapy water; [AI] soap scum ring in a basin of
  hard water.
- **Ledger:** `sol:I2-water` (PubChem), `ghs:I2`, `ghs:cyclohexane` (g10),
  `hardness:classes` (WHO background document, mg/L CaCO₃) if quoted.
- **Exercises (15):** ★ dissolution equations (NaCl, CaCl₂, Na₂SO₄, AlCl₃),
  ion concentrations; ★★ which solvent for which solute, why ethanol mixes
  with water, read the micelle figure, choose an extraction solvent; ★★★
  mass of salt for a given [Cl⁻], why soap fails in sea water (told),
  mixing two salt solutions (ion concentrations after mixing).
- **Problem — "Soap and hard water":** Part I — calcium and magnesium salts
  dissolved in tap water, ion concentrations; Part II — the soap molecule,
  amphiphile, micelle; Part III — scum: 2 C₁₇H₃₅COO⁻ + Ca²⁺ → Ca(C₁₇H₃₅COO)₂
  stoichiometry; Part IV — a 150 L bath of hard water (exercise hardness).
  **Named final number: the mass of soap wasted as scum in one bath**
  (about 0.27 kg for 120 mg/L of Ca²⁺; fixed in Phase B). ~20 questions.

### g11 ch4 `organic-skeletons` — Organic Molecules: Skeletons and Names (~11 pp; 15 exos + problem)

- **Hook:** a disposable lighter holds butane, a camping cartridge in winter
  holds propane — two cousins in a family of molecules made of nothing but
  carbon and hydrogen.
- **Recall:** covalent bonds, Lewis structures, tetrahedral carbon
  (`ch:g10:lewis-and-shape`).
- **Sections:** 1. Formulas of organic molecules (molecular, structural,
  semi-structural, skeletal); 2. Carbon chains (linear, branched, cyclic);
  3. Alkanes and their names (longest chain, numbering, alkyl substituents);
  4. Constitutional isomers (C₄H₁₀, C₅H₁₂); 5. Alkanes from crude oil
  (fractional distillation told: the refinery tower, an industrial scene).
- **Definitions:**
  - `def:g11:organic-skeletons:organic` — organic compound
  - `def:g11:organic-skeletons:formulas` — molecular formula; structural
    formula; semi-structural formula; skeletal formula (map ✓ "skeletal
    formulas"; "chemical formula" stays g7's)
  - `def:g11:organic-skeletons:alkane` — alkane; alkyl group (map ✓
    "alkane names"; "group" homograph § C10)
  - `def:g11:organic-skeletons:isomer` — isomers; constitutional isomers
    (map ✓)
- **Statements:** method "naming an alkane"; method "from a name to a
  skeletal formula"; prop "isomers have the same formula and different
  properties" (pentane isomers' boiling points, ledger).
- **Boxes:** `safety` butane (from g4), pentane (PubChem).
- **Figures:** [S] the four representations of butane and of
  2-methylpropane side by side (chemfig); [S] skeletal formulas of the
  three C₅H₁₂ isomers with boiling points; [S] naming walkthrough (numbered
  chain, circled substituents); [AI] oil refinery towers at dusk; [AI]
  camping stove cartridge in snow (no text).
- **Ledger:** `bp:pentane`, `bp:isopentane`, `bp:neopentane`, `bp:butane`,
  `bp:isobutane`, `bp:propane` (NIST WebBook), `ghs:pentane`.
- **Exercises (15):** ★ formulas between representations, name 3 alkanes,
  count C and H from skeletal formulas; ★★ draw from names, find isomers of
  C₅H₁₂, correct a wrong name, read the boiling-point figure, cyclic vs
  linear formulas; ★★★ isomers of C₆H₁₄ (5), why branched isomers boil
  lower (contact area), name a large branched alkane.
- **Problem — "Lighter gas":** Part I — butane and 2-methylpropane, the
  four representations; Part II — boiling points and winter use (ledger);
  Part III — naming and isomer count; Part IV — the nine isomers of C₇H₁₆,
  drawn and named. **Named final number: 9, the number of constitutional
  isomers of heptane.** ~20 questions.

### g11 ch5 `functional-groups` — Functional Groups and Families (~11 pp; 15 exos + problem)

- **Hook:** vinegar, nail-varnish remover, the smell of pear drops and of
  fish — four smells, four functional groups.
- **Recall:** skeletal formulas, alkane names, isomers
  (`ch:g11:organic-skeletons`); polarity, hydrogen bond
  (`ch:g11:polarity-and-cohesion`).
- **Sections:** 1. Functional groups (hydroxyl, carbonyl, carboxyl, ester,
  amine, amide, halogen, C=C); 2. Alcohols and their class (primary,
  secondary, tertiary); 3. Aldehydes, ketones, carboxylic acids and esters;
  4. Amines, amides, halogenoalkanes, alkenes; 5. Naming (suffix for the
  main group, prefixes for the rest; method).
- **Definitions:**
  - `def:g11:functional-groups:functional-group` — functional group (map ✓)
  - `def:g11:functional-groups:alcohol` — alcohol; class of an alcohol
  - `def:g11:functional-groups:carbonyl` — aldehyde; ketone
  - `def:g11:functional-groups:carboxylic-acid` — carboxylic acid; ester
  - `def:g11:functional-groups:amine` — amine; amide
  - `def:g11:functional-groups:halogenoalkane` — halogenoalkane; alkene
  (map ✓ "functional groups and their names"; the word "family" is used in
  prose only, § C9.)
- **Statements:** method "naming an organic compound with one group";
  table-proposition of groups, families, suffixes, examples; example ethyl
  ethanoate and its acid + alcohol parents.
- **Boxes:** `safety` propanone (`ghs:acetone`, g6); ethanoic acid
  (`ghs:acetic-acid`).
- **Figures:** [S] table of groups with chemfig structures; [S] the class
  of an alcohol (three butanols); [S] ester naming picture (acid part /
  alcohol part); [AI] still life: vinegar bottle, nail-varnish remover,
  pears, a fishmonger's ice (no labels); [AI] perfumer's lab with small
  bottles (lab scene).
- **Ledger:** `ghs:acetic-acid`; no numbers otherwise.
- **Exercises (15):** ★ identify groups in 5 molecules, name simple
  compounds, family from a name; ★★ draw from names, class of alcohols,
  isomers of C₃H₆O (propanal / propanone), ester from acid + alcohol, read
  the table; ★★★ groups in aspirin and paracetamol, isomers with different
  groups (C₂H₆O), name a polyfunctional molecule (main group chosen).
- **Problem — "Fruit flavours":** a flavour chemist builds a banana
  aroma. Part I — groups in candidate molecules; Part II — naming; Part III
  — 3-methylbutyl ethanoate from its acid and alcohol (formulas); Part IV —
  molar masses (`tools/molar_mass.py`) and the identification by M.
  **Named final number: the molar mass of the banana ester, 130.0 g/mol**
  (book weights). ~20 questions.

### g11 ch6 `infrared` — Infrared Spectroscopy (~11 pp; 15 exos + problem)

- **Hook:** a sealed bottle of colourless liquid with a torn label: in two
  minutes an infrared spectrum tells an alcohol from a ketone from an acid.
- **Recall:** functional groups (`ch:g11:functional-groups`); absorption
  spectrum (`ch:g11:absorbance`); hydrogen bonds
  (`ch:g11:polarity-and-cohesion`).
- **Sections:** 1. Bonds vibrate and absorb infrared light (two balls on a
  spring — an illustration); wavenumber σ = 1/λ in cm⁻¹; 2. Reading an IR
  spectrum (transmittance, the reversed axis, bands, the fingerprint
  region); 3. Characteristic bands (O–H free and hydrogen-bonded, N–H, C–H,
  C=O, C=C, C–O; the broad O–H of acids); 4. Identifying functional groups
  (method; ethanol, propanone, ethanoic acid, ethyl ethanoate).
- **Definitions:**
  - `def:g11:infrared:spectrum` — infrared spectrum; transmittance (map ✓
    "IR spectroscopy")
  - `def:g11:infrared:wavenumber` — wavenumber
  - `def:g11:infrared:band` — absorption band; fingerprint region
- **Statements:** prop "each bond type absorbs in a characteristic range"
  (table, ledger ranges); prop "hydrogen bonding broadens and lowers the
  O–H band"; method "reading an IR spectrum" (above 1500 cm⁻¹ first).
- **Boxes:** `inthelab[Recording a spectrum]` (ATR crystal, a drop).
- **Figures:** [F] `infrared`: synthetic spectra of ethanol (liquid), ethanol
  (gas, free O–H), propanone, ethanoic acid, ethyl ethanoate, ethanamine —
  Lorentzian bands at ledger positions; test: minima at ledger positions,
  0 ≤ T ≤ 100, reversed axis consistent; [S] band chart (horizontal bars on
  a wavenumber axis); [S] stretching cartoon (two balls on a spring); [AI]
  FTIR spectrometer on a bench (no screen text).
- **Ledger:** ~15 rows: `ir:OH-free`, `ir:OH-bonded`, `ir:OH-acid`,
  `ir:NH`, `ir:CH`, `ir:CO-ketone`, `ir:CO-ester`, `ir:CO-acid`,
  `ir:CO-aldehyde`, `ir:CC-double`, `ir:CO-single` (ranges: SDBS / NIST
  WebBook spectra of named compounds, one row per compound band used).
- **Exercises (15):** ★ σ ↔ λ, which band means which bond, find the C=O;
  ★★ identify a family from a spectrum (3 spectra), why the acid's O–H is
  broad, gas vs liquid ethanol, choose between isomers C₃H₆O; ★★★ follow
  an oxidation by IR (an O–H vanishes, a C=O appears), ester vs acid with
  the same formula, a spectrum with an impurity.
- **Problem — "Three unlabelled bottles":** Part I — formulas and groups of
  ethanol, propanone, ethanoic acid; Part II — the three spectra matched;
  Part III — isomers sharing a formula and how IR separates them; Part IV —
  converting the strongest band of the ketone to a wavelength. **Named final
  number: the wavelength absorbed by the C=O bond of propanone, about
  5.8 µm** (from the ledger wavenumber). ~20 questions.

### g11 ch8 `titration` — Titration (~11 pp; 15 exos + problem)

- **Hook:** an iron supplement promises 80 mg of iron per tablet. A
  burette, a purple solution and one drop that does not fade check the
  promise. (Honours the pilot's announcement: "This reaction is used in the
  next chapter to measure an amount of iron(II).")
- **Recall:** oxidants, reductants, half-equations, the permanganate–iron(II)
  equation (`ch:g11:redox`); concentration (`ch:g10:concentration-and-
  dilution`); progress table, limiting reactant
  (`ch:g10:reaction-progress-table`).
- **Sections:** 1. Titrating: measuring an amount by a reaction (titrant,
  titrated species; the reaction must be total, fast and unique); 2.
  Equivalence (stoichiometric proportions; the relation n(A)/a = n(B)/b);
  3. Locating equivalence by a colour change (permanganate's own colour;
  iodine and starch); 4. Computing an unknown concentration (method); 5.
  The titration as a measurement (burette reading to 0.05 mL; repeat;
  relative error of a reading — Type A/B uncertainty is the Year 1
  volume's).
- **Definitions:**
  - `def:g11:titration:titration` — titration; titrant; titrated solution
    (map ✓ "colour titration")
  - `def:g11:titration:equivalence` — equivalence; equivalent volume
    (map ✓)
- **Statements:** prop "at equivalence the reactants have been introduced in
  the proportions of the equation"; method "computing c from V_eq"; example
  Fe²⁺ by MnO₄⁻; example vitamin C by iodine with starch.
- **Boxes:** `inthelab[Reading a burette]`; `safety` potassium permanganate
  (`ghs:KMnO4`, exists), iodine (g11 ch3).
- **Figures:** [S] titration set (burette pic on a stand over an erlenmeyer
  on a magnetic stirrer — hotplate pic + stir bar); [S] three flasks:
  before (colourless), at (first pink that stays), after (pink); [S] amounts
  vs added volume (exact lines, pgfplots) crossing at V_eq; [AI] iron
  supplement tablets on a dish (hook, no text); [AI] student at a titration
  bench in goggles (lab scene).
- **Ledger:** `ghs:KMnO4` (exists), `ghs:I2`; supplement content is
  exercise data.
- **Exercises (15):** ★ vocabulary, n from c and V, V_eq read; ★★ c from a
  titration (Fe²⁺, I₂, vitamin C), conditions of a titration reaction, read
  the colour figure, dilution before titrating; ★★★ relative error from the
  burette reading, a titration whose ratio is 2:5, choose the titrant
  concentration to land V_eq near 15 mL.
- **Problem — "Is the iron tablet honest?":** Part I — the two couples and
  the equation (from the pilot); Part II — dissolving a tablet in acid,
  titrating with 0.0200 mol/L permanganate, V_eq = 14.3 mL (exercise data);
  Part III — amount and mass of iron; Part IV — repeatability over three
  tablets, comparison with the label. **Named final number: the mass of iron
  per tablet, about 80 mg** (fixed with the 0.1-rounded M(Fe)). ~20
  questions.

### g11 ch9 `reaction-energy` — The Energy of Reactions: Combustion and Bond Energies (~11 pp; 15 exos + problem)

- **Hook:** a hand warmer that heats up when its seal is broken, a cold
  pack that freezes a sprained ankle, a bus running on hydrogen.
- **Recall:** complete combustion (`ch:g8:combustion-and-fuels`); covalent
  bonds, Lewis structures (`ch:g10:lewis-and-shape`); mole
  (`ch:g10:the-mole`).
- **Sections:** 1. Exothermic and endothermic transformations (heat as known
  from physics); 2. The energy released by a combustion (heating water: the
  physics formula Q = m c ΔT used as known; molar energy of combustion); 3.
  Bond energies (breaking costs, forming gives back; estimating a reaction
  energy from average bond energies); 4. Comparing fuels (energy per mole,
  per kilogram; CO₂ per megajoule; hydrogen, methane, octane, ethanol).
- **Definitions:**
  - `def:g11:reaction-energy:exothermic` — exothermic; endothermic (map ✓)
  - `def:g11:reaction-energy:combustion-energy` — molar energy of
    combustion (not in map; enthalpy is the Year 2 volume's word)
  - `def:g11:reaction-energy:bond-energy` — bond energy (map ✓)
- **Statements:** prop "E_r ≈ Σ E(bonds broken) − Σ E(bonds formed)"
  (sign convention fixed and stated; average values, hence an estimate);
  method "estimating a reaction energy from bond energies"; example methane
  combustion estimate vs measured.
- **Boxes:** `inthelab[Heating water with a spirit burner]` (teacher; the
  losses explained).
- **Figures:** [S] energy diagrams for an exothermic and an endothermic
  reaction (levels, arrow released / taken); [S] the bond-energy cycle for
  CH₄ + 2 O₂ (atoms at the top); [S] spirit burner under a can of water
  with thermometer; [S] bar chart of energy per kilogram of fuels (ledger);
  [AI] hand warmers in gloved hands; [AI] hydrogen bus at a refuelling
  station (no text).
- **Ledger:** ~15 rows: `be:C-H`, `be:C-C`, `be:O=O`, `be:C=O-CO2`,
  `be:O-H`, `be:H-H`, `be:C-O`, `be:N#N`, `be:N-H` (a citable average-bond-
  energy table, e.g. OpenStax Chemistry 2e Table 7.2 — CC BY, from standard
  compilations); `dch:CH4`, `dch:C2H5OH`, `dch:C8H18`, `dch:H2`, `dch:C`
  (NIST WebBook ΔcH° liquid/gas as stated).
- **Exercises (15):** ★ exo or endo from descriptions, energy for n moles,
  read an energy diagram; ★★ estimate E_r from bond energies (H₂ + Cl₂,
  methane, ethanol), energy per kg of two fuels, water heated by a burner,
  read the fuel bar chart; ★★★ efficiency of the spirit-burner experiment,
  CO₂ per MJ, why the estimate differs from the measurement.
- **Problem — "Which fuel for the city bus?":** Part I — combustion
  equations of methane, ethanol, octane, hydrogen; Part II — energy per
  kilogram from the ledger; Part III — the bond-energy estimate for methane
  vs the measured value; Part IV — CO₂ per MJ for each fuel. **Named final
  number: the mass of CO₂ released per megajoule by methane, about 49 g**
  (fixed with `dch:CH4`). ~20 questions.

---

## Grade 12

### g12 ch1 `proton-nmr` — Proton NMR (~11 pp; 15 exos + problem)

- **Hook:** the hospital MRI scanner and the chemist's NMR spectrometer are
  the same physics: hydrogen nuclei in a strong magnet answer a radio
  signal, and each answers according to its neighbours.
- **Recall:** IR spectroscopy (`ch:g11:infrared`); functional groups and
  isomers (`ch:g11:functional-groups`, `ch:g11:organic-skeletons`).
- **Sections:** 1. Protons in a magnetic field (told; the spin physics is
  not taught) — the chemical shift δ in ppm, the TMS reference; 2.
  Equivalent protons (one group, one signal); 3. Integration (step heights
  proportional to proton counts); 4. Multiplicity and the n + 1 rule
  (doublet, triplet, quartet; Pascal intensities; protons on O or N usually
  a singlet); 5. Using IR and NMR together (method; C₃H₆O₂ and C₄H₈O₂
  isomers).
- **Definitions:**
  - `def:g12:proton-nmr:spectrum` — NMR spectrum; chemical shift (map ✓
    "¹H NMR")
  - `def:g12:proton-nmr:equivalent` — equivalent protons
  - `def:g12:proton-nmr:integration` — integration curve ("integration"
    homograph § C17)
  - `def:g12:proton-nmr:multiplet` — multiplet; n + 1 rule (Book 1 owns
    them in-volume; the Year 1 volume re-founds them with coupling
    constants, as the series map allows)
- **Statements:** prop "the shift depends on the neighbouring atoms"
  (table of ranges, ledger); prop "n + 1 rule" (admitted; "explained in the
  Year 1 volume"); method "identifying a molecule from IR + NMR".
- **Boxes:** `inthelab[Preparing an NMR tube]`.
- **Figures:** [F] `proton-nmr`: synthetic spectra of ethanol, ethyl
  ethanoate, propanone, propanoic acid / methyl ethanoate pair, with
  integration curves — test: integral steps ∝ proton counts, multiplet line
  ratios binomial, centres at ledger shifts; [S] shift chart (bands by
  environment); [S] Pascal's triangle and splitting pictures; [AI] MRI
  scanner room (hook, no text); [AI] NMR magnet in a lab (lab scene).
- **Ledger:** ~15 rows `nmr:ethanol-CH3`, `-CH2`, `-OH`; `nmr:etoac-*`;
  `nmr:acetone`; `nmr:propanoic-*`; `nmr:meoac-*` (SDBS, CDCl₃); shift
  ranges (a citable table).
- **Exercises (15):** ★ count groups of equivalent protons, multiplicity of
  a signal, read an integration; ★★ predict a spectrum (ethyl group,
  isopropyl group), match spectra to isomers, read the shift chart, IR + NMR
  identification; ★★★ C₄H₈O₂ isomers, an exchangeable proton, a mixture of
  two compounds.
- **Problem — "The unknown solvent":** a bottle labelled only C₄H₈O₂. Part
  I — possible isomers and groups; Part II — IR (C=O, no broad O–H); Part
  III — the NMR spectrum (singlet 3H, quartet 2H, triplet 3H); Part IV —
  identification as ethyl ethanoate and the integration heights. **Named
  final number: the height of the quartet's integration step, 18 mm out of a
  72 mm total** (exercise data). ~20 questions.

### g12 ch2 `stereochemistry` — Stereochemistry: Chirality and Isomers (~11 pp; 15 exos + problem)

- **Hook:** two molecules made of the same atoms joined in the same order:
  one smells of spearmint, its mirror image of caraway.
- **Recall:** shapes and the wedge-and-dash drawing
  (`ch:g10:lewis-and-shape`); isomers (`ch:g11:organic-skeletons`);
  functional groups (`ch:g11:functional-groups`).
- **Sections:** 1. Representing molecules in space (Cram representation);
  2. Chirality and the asymmetric carbon; enantiomers; racemic mixture; 3.
  Diastereomers (two asymmetric carbons; the meso case); 4. Z/E isomerism of
  double bonds; 5. Conformations (rotation about single bonds; staggered,
  eclipsed); 6 (short). Why it matters: smell, taste, drugs, enzymes.
- **Definitions:**
  - `def:g12:stereochemistry:stereoisomer` — stereoisomers
  - `def:g12:stereochemistry:cram` — Cram representation (Book 1 owns it
    in-volume; the Year 1 volume re-founds it with Newman)
  - `def:g12:stereochemistry:chiral` — chiral; asymmetric carbon (map ✓
    "chirality")
  - `def:g12:stereochemistry:enantiomer` — enantiomers; racemic mixture
    (map ✓)
  - `def:g12:stereochemistry:diastereomer` — diastereomers
  - `def:g12:stereochemistry:z-e` — Z/E isomers (map ✓)
  - `def:g12:stereochemistry:conformation` — conformation
- **Statements:** prop "a molecule with one asymmetric carbon is chiral";
  prop "n asymmetric carbons, at most 2ⁿ stereoisomers"; method "is it
  chiral? look for a mirror plane"; method "Z or E" (higher priority by
  atomic number — the full CIP rules are the Year 1 volume's); example
  lactic acid, but-2-ene, tartaric acid.
- **Boxes:** `history[Pasteur sorts crystals by hand, 1848]`.
- **Figures:** [S] lactic acid enantiomers in Cram, mirror between (chemfig
  with wedges); [S] but-2-ene Z and E; [S] tartaric acid's three
  stereoisomers; [S] ethane conformations (Newman pictures, named as
  pictures); [P] Pasteur ✓ `File:Louis Pasteur, foto av Paul Nadar, Crisco
  edit.jpg` (PD); [P] tartrate crystals ✓ `File:Left ammonium tartrate
  crystals Musée Pasteur Créer le cristal.jpg` (CC BY 4.0, credit in
  caption); [AI] spearmint leaves beside caraway seeds (hook).
- **Ledger:** `mp:tartaric-L`, `mp:tartaric-meso`, `mp:tartaric-rac`
  (PubChem / a primary source); carvone smells qualitative (cited source if
  stated as fact).
- **Exercises (15):** ★ find asymmetric carbons, Z or E, chiral or not;
  ★★ draw enantiomers in Cram, count stereoisomers, enantiomers or
  diastereomers, conformations of butane; ★★★ the meso form, a drug and its
  enantiomer (told), two double bonds Z/E count.
- **Problem — "Pasteur's crystals":** Part I — tartaric acid, its
  asymmetric carbons; Part II — the stereoisomers (L, D, meso); Part III —
  physical properties (melting points, ledger) distinguish diastereomers,
  not enantiomers; Part IV — the racemic mixture sorted by hand. **Named
  final number: the number of stereoisomers of tartaric acid, 3** (not
  2² = 4). ~20 questions.

### g12 ch3 `curly-arrows` — Reaction Mechanisms: Curly Arrows (~11 pp; 15 exos + problem)

- **Hook:** an equation tells where a reaction starts and ends; a mechanism
  tells what happens in between, one electron pair at a time.
- **Recall:** electronegativity, polarity (`ch:g11:polarity-and-cohesion`);
  Lewis structures, lone pairs (`ch:g10:lewis-and-shape`); functional
  groups (`ch:g11:functional-groups`).
- **Sections:** 1. Electron-rich and electron-poor sites (lone pairs, π
  bonds, δ⁻ atoms; δ⁺ atoms); 2. Curly arrows (from a pair to an atom or a
  bond; conventions); 3. Elementary steps and intermediates (the mechanism
  as a series of steps; carbocation intermediate); 4. Three categories:
  substitution, addition, elimination (bromoethane + hydroxide; ethene + HBr;
  dehydration of an alcohol); 5. Changing the chain or the group (a
  reaction modifies the skeleton or only the functional group).
- **Definitions:**
  - `def:g12:curly-arrows:site` — electron-donor site; electron-acceptor
    site (Book 1 words; "nucleophile / electrophile" are the Year 1
    volume's, which re-founds this chapter)
  - `def:g12:curly-arrows:curly-arrow` — curly arrow (map ✓)
  - `def:g12:curly-arrows:mechanism` — reaction mechanism; elementary step;
    reaction intermediate (map ✓ "mechanism categories"; the series map
    lets the Year 1 volume re-found "elementary step")
  - `def:g12:curly-arrows:categories` — substitution; addition; elimination
    (map ✓)
- **Statements:** method "drawing a curly arrow" (start on a pair, end on
  the atom that receives it, check charges); prop "an elementary step's
  arrows conserve charge"; examples as above with full arrows.
- **Boxes:** none.
- **Figures:** [S] δ⁺/δ⁻ map of a carbonyl and of bromoethane; [S] four
  mechanisms with chemfig `@{node}` + `\chemmove` (SN of bromoethane;
  HBr addition in two steps; acid dehydration of ethanol; protonation of
  water as a warm-up); [S] category table (reactants → product schemes);
  [AI] none (abstract chapter) — possibly a chemist at a whiteboard
  **without** writing (low value; skipped unless a chapter needs air).
- **Ledger:** none.
- **Exercises (15):** ★ donor or acceptor sites, category of a reaction,
  complete a curly arrow; ★★ draw arrows of given steps, find the
  intermediate, charges after a step, read a mechanism; ★★★ propose the
  steps of an addition of HCl to propene (two possible carbocations told,
  Markovnikov is the Year 1 volume's word), a mechanism with an error, the
  esterification mechanism skeleton.
- **Problem — "Making bromoethane":** Part I — sites in ethene and HBr;
  Part II — the two-step mechanism with arrows; Part III — category and
  intermediate; Part IV — progress table and yield (10.0 g ethene, 75 %).
  **Named final number: the mass of bromoethane obtained, about 29 g**
  (fixed with `tools/molar_mass.py`). ~20 questions.

### g12 ch4 `reaction-rates` — Reaction Rates (~11 pp; 15 exos + problem)

- **Hook:** milk sours in two days on the counter and in two weeks in the
  fridge; a firework burns in a fraction of a second; a church's limestone
  takes centuries to weather.
- **Recall:** absorbance and Beer–Lambert (`ch:g11:absorbance`);
  concentration (`ch:g10:concentration-and-dilution`); extent
  (`ch:g10:reaction-progress-table`).
- **Sections:** 1. Slow and fast reactions; following a reaction in time
  (sampling and quenching + titration; spectrophotometry; pressure;
  conductivity); 2. Kinetic factors (temperature, concentration, contact
  area; catalysts next chapter); 3. Rates of disappearance and appearance
  (v = −d[A]/dt, read from a tangent); 4. First-order reactions: v = k[A],
  [A] = [A]₀ e^{−kt} (solution of the rate equation checked by derivation);
  5. Half-life (t₁/₂ = ln 2 / k; graphical reading).
- **Definitions:**
  - `def:g12:reaction-rates:kinetic-factor` — kinetic factor (map ✓)
  - `def:g12:reaction-rates:quenching` — quenching
  - `def:g12:reaction-rates:rate` — rate of disappearance; rate of
    appearance (map ✓ "rate")
  - `def:g12:reaction-rates:first-order` — first-order reaction; rate
    constant
  - `def:g12:reaction-rates:half-life` — half-life (map ✓; physics' half-life
    is radioactive decay, prose remark)
- **Statements:** prop [A] = [A]₀ e^{−kt} (proof: it satisfies the
  equation; uniqueness admitted); prop t₁/₂ = ln 2 / k (derived); method
  "rate from a tangent"; method "testing for first order" (ln[A] linear).
- **Boxes:** `inthelab[Quenching a sample]` (ice-cold water).
- **Figures:** [F] `reaction-rates`: (a) [A](t) for one first-order
  reaction at two temperatures, tangent at t = 0, half-lives marked; (b)
  absorbance of a coloured product vs time (iodine appearing) — tests:
  [A](t₁/₂) = [A]₀/2, tangent slope −k[A]₀, ln-linearity; [S] sampling and
  quenching steps; [AI] milk on a kitchen counter vs in a fridge (hook);
  [AI] weathered limestone statue.
- **Ledger:** none required (k values are exercise data); optional real
  example with a source if used.
- **Exercises (15):** ★ kinetic factors, read a half-life, rate from a
  tangent; ★★ first-order test from a table, k from t₁/₂, [A] at time t
  (exp), read the figure, a reaction followed by absorbance; ★★★ time to
  reach 1 %, comparing two temperatures, why quenching works.
- **Problem — "The fading dye":** crystal violet bleached by hydroxide,
  followed by absorbance. Part I — A ∝ [dye]; Part II — the data table and
  the ln-plot; Part III — k and t₁/₂; Part IV — prediction. **Named final
  number: the time for the colour to fall to 1 % of its start, about
  6.6 half-lives** (in minutes from the data, fixed in Phase B). ~20
  questions.

### g12 ch5 `catalysis` — Catalysis (~11 pp; 15 exos + problem)

- **Hook:** hydrogen peroxide poured on a cut keeps quiet in its bottle for
  years and foams within a second on the wound.
- **Recall:** rates and kinetic factors (`ch:g12:reaction-rates`);
  mechanisms and intermediates (`ch:g12:curly-arrows`).
- **Sections:** 1. What a catalyst is (speeds up, is regenerated, absent
  from the equation, does not change the final state); 2. Homogeneous
  catalysis (iodide or iron(III) and hydrogen peroxide, two steps); 3.
  Heterogeneous catalysis (platinum, the catalytic converter, the iron of
  ammonia synthesis); 4. Enzymatic catalysis (catalase; specificity; an
  optimum temperature); 5. Selectivity (ethanol over alumina → ethene, over
  copper → ethanal).
- **Definitions:**
  - `def:g12:catalysis:catalyst` — catalyst; catalysis (map ✓)
  - `def:g12:catalysis:homogeneous` — homogeneous catalysis; heterogeneous
    catalysis (multi-word, no clash with g6's "homogeneous mixture")
  - `def:g12:catalysis:enzyme` — enzyme (biology's word, chemist's angle)
  - `def:g12:catalysis:selective` — selective catalyst
- **Statements:** prop "a catalyst opens a path with a lower energy
  barrier" (profile, admitted); example the two-step iodide mechanism (sum =
  2 H₂O₂ → 2 H₂O + O₂); remark: industry and life run on catalysts.
- **Boxes:** `safety` hydrogen peroxide (PubChem); `history[Haber's
  ammonia, 1909]` with a sourced date and tonnage.
- **Figures:** [F] `catalysis`: (a) energy profiles with and without
  catalyst (two-humped vs one) as analytic smooth curves; (b) O₂ volume vs
  time with and without catalyst, same final value — test: same plateau,
  catalysed curve faster at every t, barrier ordering; [S] catalytic
  converter cross-section (honeycomb, Pt/Rh coat, CO + NO in, CO₂ + N₂ out);
  [S] H₂ on a metal surface (adsorption, reaction, desorption); [AI]
  catalytic converter cut open (industrial); [AI] potato slice fizzing in
  peroxide in a lab dish.
- **Ledger:** `ghs:H2O2`, `haber:conditions` (temperature, pressure range),
  `nh3:production` (USGS Mineral Commodity Summaries, nitrogen),
  `vm:0C` (const:Vm1, shared) for the "volumes" convention.
- **Exercises (15):** ★ catalyst or reactant, type of catalysis, read the
  profile; ★★ two-step mechanism sums, rate with / without catalyst, why
  converters are poisoned by lead (told), enzyme temperature optimum, read
  the kinetic figure; ★★★ selectivity reasoning, the final state unchanged,
  turnover counting.
- **Problem — "The hairdresser's peroxide":** "20-volume" peroxide. Part I —
  the decomposition equation; Part II — what "20 volumes" means and the
  molar concentration (V_m at 0 °C, 1 atm, shared row); Part III —
  catalysed by catalase vs iron(III): curves; Part IV — oxygen released
  by a 100 mL bottle. **Named final number: the concentration of 20-volume
  peroxide, 1.79 mol/L.** ~20 questions.

### g12 ch6 `equilibrium` — Chemical Equilibrium: Quotient and Constant (~11 pp; 15 exos + problem)

- **Hook:** a sealed bottle of fizzy water keeps its gas for months; opened,
  it goes flat in an afternoon. Nothing is wrong with the reaction: it is
  simply allowed to go one way.
- **Recall:** extent, x_max, total reaction (`ch:g10:reaction-progress-
  table`); concentration; kinetic factors (`ch:g12:reaction-rates`).
- **Sections:** 1. Reactions that are not total (x_f < x_max; the final
  extent ratio τ); 2. The equilibrium state (both directions at once,
  dynamic); 3. The reaction quotient Q (concentrations over c°; solids and
  the solvent left out); 4. The equilibrium constant K (Q at equilibrium,
  depends only on temperature); 5. Predicting the direction of change (Q <
  K, Q > K) and shifting it (excess reagent, removing a product).
- **Definitions:**
  - `def:g12:equilibrium:non-total` — non-total reaction; final extent ratio
    (map ✓ "non-total reaction")
  - `def:g12:equilibrium:equilibrium-state` — equilibrium state
  - `def:g12:equilibrium:quotient` — reaction quotient (map ✓ "Q")
  - `def:g12:equilibrium:constant` — equilibrium constant (map ✓ "K")
  - `not:g12:equilibrium:c-standard` — c° (notation, no term)
- **Statements:** prop "Q_eq = K" (admitted: "derived in the Year 2
  volume"); prop "direction of evolution"; method "final state of a
  non-total reaction" (solve K = f(x), quadratic); example esterification
  K ≈ 4.
- **Boxes:** `history[Berthelot and Péan de Saint-Gilles, 1862]`.
- **Figures:** [F] `equilibrium`: extent vs time for esterification from
  acid + alcohol and for hydrolysis from ester + water, both reaching the
  same final composition (rate law with k_f / k_b = K) — test: limit 2/3
  for the equimolar start, the two curves meet; [S] the Q axis with K and
  the arrows of evolution; [AI] sealed and opened fizzy-water bottles
  (no text); [AI] limestone cave with stalactites (equilibria in water —
  told).
- **Ledger:** `K:esterification` (≈ 4; primary or a citable data page).
- **Exercises (15):** ★ Q expressions (4 reactions), τ from x_f and x_max,
  direction from Q vs K; ★★ final state with K (quadratics), effect of an
  excess, read the curves, solid in Q; ★★★ removing water to raise the
  yield, K of the reverse reaction, a mixture that does not move.
- **Problem — "Berthelot's ester":** Part I — the esterification and its
  quotient; Part II — K from Berthelot's equimolar result (2/3); Part III —
  final state with 3 mol of alcohol per mol of acid (quadratic); Part IV —
  removing water. **Named final number: the yield with a threefold excess of
  alcohol, 90 %.** ~20 questions.

### g12 ch7 `ka-and-pka` — Acids and Bases: Ka and pKa (~11 pp; 15 exos + problem)

- **Hook:** an ant bite stings with methanoic acid, a bee's with a different
  mix; "how acidic" turns out to need two numbers, not one.
- **Recall:** H⁺, HO⁻, the qualitative pH scale (`ch:g9:acids-bases-ph`);
  Q and K (`ch:g12:equilibrium`).
- **Sections:** 1. Brønsted acids and bases; acid–base couples; the
  oxonium ion H₃O⁺; ampholytes; 2. The pH, quantitatively: pH =
  −log([H₃O⁺]/c°) (the g9 rule "one unit per tenfold dilution" now
  derived); pH of a strong acid; 3. Autoprotolysis of water, the ionic
  product K_e (pK_e = 14.0 at 25 °C); pH of a strong base; 4. Strong and
  weak acids; the acidity constant K_a and pK_a; 5. Comparing acids on a
  pK_a scale.
- **Definitions:**
  - `def:g12:ka-and-pka:bronsted` — Brønsted acid; Brønsted base;
    acid–base couple (map ✓ "Brønsted")
  - `def:g12:ka-and-pka:oxonium` — oxonium ion; ampholyte
  - `def:g12:ka-and-pka:ph-log` — **no new term**: the quantitative
    definition of pH, inside a `definition` titled "The pH, precisely",
    without `\emph{pH}\index{pH}` (owner stays g9; § C12)
  - `def:g12:ka-and-pka:ionic-product` — ionic product of water (map ✓
    "Ke")
  - `def:g12:ka-and-pka:strong-acid` — strong acid; weak acid; strong base;
    weak base
  - `def:g12:ka-and-pka:ka` — acidity constant; pKa (map ✓)
- **Statements:** prop pH of a strong acid = −log c; prop pH + pOH not used
  (pK_e only); method "pH of a weak acid" (quadratic, then check); prop "the
  smaller the pK_a, the stronger the acid".
- **Boxes:** `history[From Arrhenius to Brønsted, 1887–1923]` with [P]
  Arrhenius ✓ `File:Arrhenius2.jpg` (PD); `safety` methanoic acid.
- **Figures:** [S] the pK_a scale with couples placed (ledger); [S] proton
  transfer with a curly arrow (recall g12 ch3); [S] composition bars strong
  vs weak acid at the same c; [AI] ant on a fingertip / red ant hill (hook);
  [AI] none else.
- **Ledger:** `pKe:25C` (Bandura & Lvov 2006 J. Phys. Chem. Ref. Data);
  `pka:acetic`, `pka:formic`, `pka:NH4`, `pka:H2CO3`, `pka:HCO3`,
  `pka:lactic`, `pka:benzoic`, `pka:ascorbic` (IUPAC Digitized pKa Dataset /
  primary); `ghs:formic-acid`.
- **Exercises (15):** ★ conjugate base / acid, pH of strong acids, [H₃O⁺]
  from pH; ★★ K_a from pH, pH of a weak acid, which acid is stronger, pH of
  a strong base with K_e, read the pK_a scale; ★★★ dilution of a weak acid
  (not one unit per tenfold), ampholyte behaviour, a pH that cannot be
  below 7 for any dilution of an acid (told: water's own ions).
- **Problem — "The ant's sting":** Part I — methanoic acid, its couple and
  its pK_a; Part II — pH of a 0.010 mol/L solution (quadratic); Part III —
  comparison with hydrochloric acid at the same concentration; Part IV —
  neutralising a sting with baking soda (hydrogencarbonate, pK_a values).
  **Named final number: the pH of 0.010 mol/L methanoic acid, 2.9.** ~20
  questions.

### g12 ch8 `buffers-predominance` — Buffers and Predominance Diagrams (~11 pp; 15 exos + problem)

- **Hook:** blood holds its pH between 7.35 and 7.45; a drop below 7.0 is
  life-threatening. A pair of species does the holding.
- **Recall:** K_a, pK_a, couples (`ch:g12:ka-and-pka`); pH (`ch:g9:acids-
  bases-ph`).
- **Sections:** 1. Predominance diagrams (pH < pK_a: the acid predominates;
  pH = pK_a + log([A⁻]/[AH])); 2. Distribution diagrams (fractions vs pH,
  crossing at pK_a; amino acids with two pK_a's); 3. Acid–base indicators
  (HInd / Ind⁻, colour-change range about pK_a ± 1; bromothymol blue,
  phenolphthalein, methyl orange); 4. Buffer solutions (preparation; pH
  barely moves on adding acid, base or water); 5. Buffers in living things
  (blood's CO₂ / HCO₃⁻; the zwitterion of amino acids).
- **Definitions:**
  - `def:g12:buffers-predominance:predominance` — predominance diagram;
    distribution diagram (map ✓)
  - `def:g12:buffers-predominance:indicator` — acid–base indicator;
    colour-change range (map ✓ "indicator"; § C11)
  - `def:g12:buffers-predominance:buffer` — buffer solution (map ✓)
- **Statements:** prop Henderson's relation (derived from K_a); method
  "drawing a predominance diagram"; method "choosing an indicator" (range
  contains the pH to detect — used in ch. 9); method "preparing a buffer".
- **Boxes:** `inthelab[Preparing a buffer at pH 4.8]`.
- **Figures:** [F] `buffers-predominance`: (a) distribution diagram of
  ethanoic acid; (b) of glycine (three species); (c) pH response of water vs
  an ethanoate buffer to added HCl — tests: crossing at pK_a, fractions sum
  to 1, buffer ΔpH < 0.1 over the plotted range; [S] predominance axes for
  four couples; [S] indicator colour bars (ranges from the ledger); [AI]
  blood sample tubes in a rack (lab scene); [AI] swimming pool test kit
  being used (no text).
- **Ledger:** `ph:blood` (range), `pka:H2CO3-blood` (physiological pK′ 6.1,
  a physiology reference), `ind:BBT`, `ind:phenolphthalein`,
  `ind:methyl-orange` (ranges, a vendor technical sheet or IUPAC), glycine
  `pka:gly-1`, `pka:gly-2`.
- **Exercises (15):** ★ predominant species at a pH, read a distribution
  diagram, indicator colour at a pH; ★★ ratio [A⁻]/[AH] at a pH, choose an
  indicator, buffer pH from its recipe, predominance of an amino acid, read
  the response figure; ★★★ buffer capacity reasoning, mix two solutions to
  reach a pH, an indicator with two ranges (thymol blue).
- **Problem — "Blood's buffer":** Part I — the CO₂(aq) / HCO₃⁻ couple and its
  physiological pK′; Part II — predominance at pH 7.4; Part III — the ratio
  by Henderson; Part IV — acidosis: what a fall to 7.1 means for the ratio.
  **Named final number: the hydrogencarbonate-to-carbon-dioxide ratio of
  blood, 20.** ~20 questions.

### g12 ch9 `ph-conductivity-titrations` — Titrations by pH and Conductivity (~11 pp; 15 exos + problem)

- **Hook:** a bottle of vinegar labelled "6 % acidity": a pH meter and a
  burette check the claim in ten minutes.
- **Recall:** titration, equivalence (`ch:g11:titration`); K_a, pK_a
  (`ch:g12:ka-and-pka`); indicators, Henderson (`ch:g12:buffers-
  predominance`); ions conduct (`ch:g9:ions`).
- **Sections:** 1. pH-metric titration: strong acid by strong base; locating
  equivalence by the tangent method and by the derivative dpH/dV; 2. Weak
  acid by strong base: the half-equivalence point, pH = pK_a; 3. Choosing an
  indicator from the curve; 4. Conductivity and conductimetric titration
  (σ = Σ λᵢ[Xᵢ], Kohlrausch's law admitted; slope changes at equivalence;
  the dilution assumption); 5. Which method when.
- **Definitions:**
  - `def:g12:ph-conductivity-titrations:ph-metric` — pH-metric titration;
    half-equivalence (map ✓)
  - `def:g12:ph-conductivity-titrations:conductivity` — conductivity; molar
    ionic conductivity (not in map; § C13: g9 uses "conducts" only)
  - `def:g12:ph-conductivity-titrations:conductimetric` — conductimetric
    titration (map ✓)
- **Statements:** prop "at half-equivalence pH = pK_a" (derived from
  Henderson); prop Kohlrausch (admitted); method "the tangent method";
  method "the derivative method"; method "conductimetric equivalence from
  two lines".
- **Boxes:** `inthelab[Calibrating a pH meter]`; `safety` sodium hydroxide
  (g9).
- **Figures:** [F] `ph-conductivity-titrations`: exact pH curves (HCl by
  NaOH; ethanoic acid by NaOH) from the charge balance, their derivatives,
  and conductimetric curves σ(V) (ledger λ values) — tests: V_eq = C V / C′
  (derivative maximum), pH(V_eq / 2) = pK_a ± 0.05 for the weak acid,
  pH_eq = 7.00 for strong/strong, σ minimum at V_eq for HCl/NaOH; [S]
  pH-metric set (burette, beaker, pH probe, stirrer) — pics; [S]
  conductimetry cell — pic; [S] tangent construction drawn over the
  computed curve (tangent points from the script); [AI] wine-maker's lab
  bench with burette (lab scene, no text).
- **Ledger:** `lambda:H3O`, `lambda:HO`, `lambda:Na`, `lambda:Cl`,
  `lambda:CH3COO` (limiting molar ionic conductivities at 25 °C — a citable
  compilation; **risk**: the usual table is CRC; if no accessible primary is
  found the conductimetric curves are drawn for a stated generic example and
  the real values are EXCLUDED), `pka:acetic` (ch. 7), `rho:vinegar` if
  degrees are mass-based.
- **Exercises (15):** ★ read V_eq on a curve, pK_a at half-equivalence,
  indicator choice; ★★ concentration from a pH-metric titration, the
  derivative method, conductimetric slopes explained by the ions present,
  sketch a curve, read the figure; ★★★ titrating a mixture of strong and
  weak acid (two jumps told), why conductivity falls before equivalence,
  error from a wrongly calibrated pH meter.
- **Problem — "Is the vinegar 6 %?":** Part I — diluting the vinegar ten
  times; Part II — pH-metric titration, V_eq, pK_a at half-equivalence;
  Part III — conductimetric check; Part IV — mass of ethanoic acid per
  100 g of vinegar. **Named final number: the acidity of the vinegar,
  6.0 degrees** (exercise data built to land on the label). ~20 questions.

### g12 ch10 `cells-and-electrolysis` — Electrochemical Cells and Electrolysis (~11 pp; 15 exos + problem)

- **Hook:** a phone dies at 1 % on a winter evening; plugged in, it fills
  again overnight. The same reaction is run forwards in the day and
  backwards at night.
- **Recall:** oxidant, reductant, half-equations, redox reaction
  (`ch:g11:redox`); Q and K, direction of change (`ch:g12:equilibrium`);
  ions conduct (`ch:g9:ions`); mole (`ch:g10:the-mole`).
- **Sections:** 1. A spontaneous redox reaction, split in two: the Daniell
  cell (half-cells, salt bridge, electrodes, the external circuit); anode
  and cathode; 2. The cell voltage (measured; polarity; direction predicted
  by Q vs K — no Nernst, which is the Year 1 volume's); 3. Capacity:
  Q = n(e⁻)·F, the Faraday constant, capacity in A·h; 4. Forcing a reaction:
  electrolysis (water, brine, electroplating, copper refining); 5.
  Batteries, accumulators, fuel cells, electrolysers (lead–acid,
  lithium-ion, hydrogen).
- **Definitions:**
  - `def:g12:cells-and-electrolysis:cell` — electrochemical cell; half-cell;
    salt bridge (map ✓ "cell"; "cell" homograph § C17)
  - `def:g12:cells-and-electrolysis:anode` — anode; cathode
  - `def:g12:cells-and-electrolysis:emf` — cell voltage (open-circuit
    voltage)
  - `def:g12:cells-and-electrolysis:capacity` — capacity; Faraday constant
  - `def:g12:cells-and-electrolysis:electrolysis` — electrolysis; accumulator
    (map ✓)
- **Statements:** prop "in a cell, electrons leave by the anode (oxidation)
  and enter by the cathode (reduction)"; prop "Q = n(e⁻) F"; method
  "describing a cell" (half-equations, polarity, flows); method "mass
  deposited by an electrolysis".
- **Boxes:** `history[Volta's pile, 1800]` with [P] ✓ `File:VoltaBattery.JPG`
  (CC BY-SA 3.0); `inthelab[Electrolysis of water]`.
- **Figures:** [S] Daniell cell (two beakers, Zn and Cu electrodes, salt
  bridge, voltmeter / resistor; electron arrows in the wire, ion arrows in
  the bridge) — `circuitikz` or local symbols, `utube` pic; [S] electrolysis
  of water (U-tube or two inverted tubes, gas volumes 2:1); [S] copper
  refining (impure anode, pure cathode); [AI] phone charging on a bedside
  table; [AI] electrolyser hall of a green-hydrogen plant (industrial).
- **Ledger:** `const:F`, `const:NA`, `const:e` (shared); `emf:Daniell`
  (1.10 V, a citable standard-potential table); `emf:Li-ion` (nominal 3.6–
  3.7 V, a manufacturer datasheet); `emf:alkaline` (1.5 V nominal, datasheet).
- **Exercises (15):** ★ anode / cathode, half-equations at each electrode,
  charge from current and time; ★★ polarity from the direction of electron
  flow, capacity in A·h, mass deposited in electroplating, read the cell
  figure, cell vs electrolyser; ★★★ duration of a cell from the limiting
  electrode, energy stored in a battery, gas volumes in electrolysis.
- **Problem — "The phone battery":** a 4000 mA·h lithium-ion cell. Part I
  — the cell during discharge (simplified couples, lithium ions shuttle,
  one electron each); Part II — the charge 14 400 C, the amount of
  electrons; Part III — the energy stored at 3.7 V; Part IV — recharging as
  an electrolysis. **Named final number: the mass of lithium shuttled in one
  full charge, 1.04 g.** ~20 questions.

### g12 ch11 `synthesis-strategy` — Synthesis Strategy and Green Chemistry (~11 pp; 15 exos + problem)

- **Hook:** the same painkiller made two ways: one route throws away more
  than half of the atoms it buys, the other almost none.
- **Recall:** synthesis steps, yield (`ch:g10:synthesis-yield`); curly
  arrows (`ch:g12:curly-arrows`); catalyst (`ch:g12:catalysis`); Q, K and
  shifting an equilibrium (`ch:g12:equilibrium`).
- **Sections:** 1. Optimising a synthesis (rate: temperature, catalyst,
  concentration; yield: excess reagent, removing a product — a water trap
  told); 2. Selectivity: chemoselective reagents; 3. Protecting groups
  (protect, react, deprotect — an alcohol or an amine); 4. Atom economy
  (computed from the equation); 5. The twelve principles of green chemistry
  (examples: the two ibuprofen routes; water and supercritical CO₂ as
  solvents).
- **Definitions:**
  - `def:g12:synthesis-strategy:chemoselective` — chemoselective reaction
  - `def:g12:synthesis-strategy:protecting-group` — protecting group (map ✓
    via B2's re-found column)
  - `def:g12:synthesis-strategy:atom-economy` — atom economy (map ✓)
  - `def:g12:synthesis-strategy:green-chemistry` — green chemistry (map ✓)
- **Statements:** prop atom economy = M(desired) / Σ M(reactants);
  method "planning a protection"; method "computing an atom economy"; the
  twelve principles as a list (ledger source).
- **Boxes:** `history[Green chemistry, 1998]`.
- **Figures:** [S] protection–reaction–deprotection scheme (chemfig); [S]
  the two ibuprofen routes as step boxes with atom economies; [S] bar chart
  of atom economies (computed); [AI] modern pharmaceutical plant; [AI]
  supercritical-CO₂ extraction vessel (industrial, decaffeination plant).
- **Ledger:** `ibu:boots-ae`, `ibu:bhc-ae` (EPA Presidential Green Chemistry
  Challenge 1997 BHC Company / a citable case study), `green:12` (Anastas &
  Warner 1998 via ACS GCI page).
- **Exercises (15):** ★ atom economy of simple reactions, identify the
  protecting step, which principle; ★★ compare two routes, choose
  conditions to raise yield, chemoselectivity reasoning, read the bar chart,
  waste per kg; ★★★ a three-step route's overall yield and economy, a
  protection scheme for a molecule with two groups, judging a "green" claim.
- **Problem — "Two routes to ibuprofen":** Part I — the overall equations of
  each route (given); Part II — atom economies (molar masses computed);
  Part III — waste per tonne; Part IV — yields and the real-world waste.
  **Named final number: the mass of waste avoided per tonne of ibuprofen by
  the three-step route** (fixed in Phase B). ~20 questions.

### g12 ch12 `polymers` — Polymers (~11 pp; 15 exos + problem)

- **Hook:** a fleece jacket made from 15 plastic bottles; a nylon rope; a
  sheet of paper — three polymers, one made by trees.
- **Recall:** plastics, thermoplastics, thermosets (`ch:g8:plastics`);
  functional groups, esters, amides (`ch:g11:functional-groups`);
  addition (`ch:g12:curly-arrows`).
- **Sections:** 1. Monomers, polymers, repeat unit; degree of
  polymerisation; 2. Addition polymers (polyethene, PVC, polystyrene,
  PTFE); 3. Condensation polymers (PET, nylon-6,6; the small molecule
  released); 4. Structure and properties (chain length, branching, cross-
  links, crystalline and amorphous regions); 5. Natural polymers
  (cellulose, starch, proteins, DNA, natural rubber).
- **Definitions:**
  - `def:g12:polymers:polymer` — polymer; monomer; polymerisation (map ✓)
  - `def:g12:polymers:repeat-unit` — repeat unit; degree of polymerisation
    (map ✓)
  - `def:g12:polymers:addition-polymer` — addition polymer; condensation
    polymer
- **Statements:** prop M(polymer) ≈ n · M(repeat unit); method "finding the
  monomer from a polymer"; examples as above.
- **Boxes:** `history[Carothers and nylon, 1935]` with [P] ✓ `File:Wallace
  Carothers, in the lab.jpg` (PD).
- **Figures:** [S] ethene → polyethene with brackets and n (chemfig); [S]
  PET repeat unit from its two monomers; [S] chain architectures (linear,
  branched, cross-linked; amorphous vs crystalline); [AI] fleece jacket and
  bottles (no labels); [AI] rubber tapping on a plantation tree.
- **Ledger:** none required beyond exercise data; `ghs:` none.
- **Exercises (15):** ★ monomer of a polymer, repeat unit, addition or
  condensation; ★★ degree of polymerisation from M, write a condensation,
  properties from structure, natural or synthetic, read the architecture
  figure; ★★★ nylon from two monomers, mass of water released per kg of
  polymer, cross-linking and recycling.
- **Problem — "From bottle to fleece":** Part I — PET's monomers and repeat
  unit; Part II — degree of polymerisation from a given M; Part III —
  recycling: bottles of 25 g to a 375 g fleece with a given process yield;
  Part IV — chemical recycling back to the monomers (masses). **Named final
  number: the number of 25 g bottles in one fleece, 15** (with an exercise
  yield; fixed in Phase B). ~20 questions.

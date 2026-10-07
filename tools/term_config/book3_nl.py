"""Book 3 (University Chemistry, Year 2) -- nl (Dutch). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_nl.py.

Curated by the nl Book 3 agent (2026-10-06) from this edition's own harvest
(`--terms`: the same 196 targets as English) and the frequency and
chapter-set censuses against the English links -- not translated from
book3_en.py. AMBIG_POLICY stays "drop", as in English: no term is defined
twice.

As in English, a word is linked only once its definition has been met. The
uses AFTER the definition in another sense, each masked below:
  * variantie: the variance of a system (ch. 4, phase rule) / the statistical
    variance (ch. 29 Poisson law, ch. 34 variance of a mean or of a sum);
  * initiatie: radical initiation (ch. 29) / the start of a Grignard
    reaction (ch. 35);
  * selectiviteit: a reactor's selectivity (ch. 5) / chromatographic
    selectivity (ch. 31);
  * resolutie: chromatographic resolution (ch. 31) / spectral resolution
    (ch. 33);
  * retentiefactor: the column's k (ch. 31) / the R_f of a TLC plate;
  * fragment(en): the fragment method (ch. 15) / ozonolysis fragments,
    synthons, mass-spectrum fragments -- STOPped as in English; the welded
    "fragmentorbitaal" keeps its link.
"propagatie" (ch. 29) has no homograph here: this edition writes the
propagation of uncertainty as "voortplanting van onzekerheden" (ch. 34).

Dutch inflects adjectives (-e) and has plurals WORD_TAIL cannot derive
(orbitaal/orbitalen, -zuur/-zuren, patroon/patronen, -aat/-aten,
-eer/-eren); the forms that occur, each a real occurrence of the notion, are
listed in EXTRA. English "aldol reaction" links "aldol"; the welded Dutch
"aldolreactie" is linked whole to the same definition (whose title is
"Aldolreacties"). Losses that cannot be recovered and are left as they are:
"chromatografie" inside welded compounds (gaschromatografie,
vloeistofchromatografie, kolomchromatografie) and "verzeping" inside
"verzepingsgetal", where English links the head word of an open compound.
"""

STOP = {
    # ch. 15's fragment method: the bare word is used later for ozonolysis
    # fragments (ch. 21), synthons (ch. 28) and mass-spectrum fragments
    # (ch. 32-33), exactly as in English.
    "fragment", "fragmenten", "Fragment", "Fragmenten",
}
NO_CAPITAL = set()
EXTRA = {
    # the bare noun of the "Enolates" definition (only "ion" phrase harvested;
    # coordinator, 2026-10-07, as English and Arabic)
    "enolaat": "def:b2:enolates-aldol:enolate",
    "enolaten": "def:b2:enolates-aldol:enolate",
    # inflected adjectives (-e)
    "aromatische": "def:b2:huckel:aromatic",
    "Aromatische": "def:b2:huckel:aromatic",
    "antiaromatische": "def:b2:huckel:aromatic",
    "exotherme": "def:b2:reaction-enthalpy:exothermic",
    "endotherme": "def:b2:reaction-enthalpy:exothermic",
    "isobare diagram": "def:b2:liquid-vapour-diagrams:binary-diagram",
    "isotherme diagram": "def:b2:liquid-vapour-diagrams:binary-diagram",
    "binaire diagrammen": "def:b2:liquid-vapour-diagrams:binary-diagram",
    "Binaire diagrammen": "def:b2:liquid-vapour-diagrams:binary-diagram",
    "gestabiliseerde ylide": "def:b2:wittig:ylide",
    "gestabiliseerde ylides": "def:b2:wittig:ylide",
    "radiale deel": "def:b2:atomic-orbitals:radial-angular",
    "tetraëdrische intermediair": "def:b2:acyl-substitution:nas",
    "primaire amine": "def:b2:amines:class",
    "anomere koolstofatomen": "def:b2:biomolecules:anomer",
    "harde nucleofielen": "def:b2:frontier-orbitals:hard-soft",
    "Harde nucleofielen": "def:b2:frontier-orbitals:hard-soft",
    "zachte nucleofielen": "def:b2:frontier-orbitals:hard-soft",
    "Zachte nucleofielen": "def:b2:frontier-orbitals:hard-soft",
    "harde elektrofielen": "def:b2:frontier-orbitals:hard-soft",
    "elektroactieve deeltje": "def:b2:current-potential-curves:electroactive",
    "elektroactieve deeltjes": "def:b2:current-potential-curves:electroactive",
    # plurals WORD_TAIL cannot derive
    "bindende orbitalen": "def:b2:diatomic-mos:bonding",
    "antibindende orbitalen": "def:b2:diatomic-mos:bonding",
    "niet-bindende orbitalen": "def:b2:diatomic-mos:bonding",
    "molecuulorbitalen": "def:b2:diatomic-mos:lcao",
    "Molecuulorbitalen": "def:b2:diatomic-mos:lcao",
    "fragmentorbitalen": "def:b2:fragment-orbitals:fragment",
    "Fragmentorbitalen": "def:b2:fragment-orbitals:fragment",
    "polymeren": "def:b2:polymer-synthesis:polymer",
    "Polymeren": "def:b2:polymer-synthesis:polymer",
    "repeterende eenheden": "def:b2:polymer-synthesis:polymer",
    "elastomeren": "def:b2:polymer-synthesis:elastomer",
    "Elastomeren": "def:b2:polymer-synthesis:elastomer",
    "chemische potentialen": "def:b2:chemical-potential:chemical-potential",
    "peroxyzuren": "def:b2:alkene-redox:epoxide",
    "Peroxyzuren": "def:b2:alkene-redox:epoxide",
    "diënen": "def:b2:frontier-orbitals:diels-alder",
    "primaire aminen": "def:b2:amines:class",
    "Primaire aminen": "def:b2:amines:class",
    "tertiaire aminen": "def:b2:amines:class",
    "grensstromen": "def:b2:current-potential-curves:limiting-current",
    "coulombintegralen": "def:b2:diatomic-mos:integrals",
    "resonantie-integralen": "def:b2:diatomic-mos:integrals",
    "isotopenpatronen": "def:b2:mass-spec-atomic:isotope-pattern",
    "Isotopenpatronen": "def:b2:mass-spec-atomic:isotope-pattern",
    "organocupraten": "def:b2:conjugate-additions:cuprate",
    "Organocupraten": "def:b2:conjugate-additions:cuprate",
    "fosfoniumylides": "def:b2:wittig:ylide",
    "Fosfoniumylides": "def:b2:wittig:ylide",
    # the welded "aldol reaction" (English links "aldol" inside it)
    "aldolreactie": "def:b2:enolates-aldol:aldol",
    "aldolreacties": "def:b2:enolates-aldol:aldol",
    "Aldolreacties": "def:b2:enolates-aldol:aldol",
    "retro-aldolreactie": "def:b2:enolates-aldol:aldol",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# Multi-word patterns use \s+ between words: a phrase wrapped across a source
# line break must still be protected. A look-ahead anchored on a word that is
# itself a term must allow an optional wrapper: (?:\\omterm\{[^{}]*\}\{)?
EXTRA_PROTECT = [
    # chemfig settings and arrow labels: \arrow{->[label][label]}
    r"\\setchemfig\{[^{}]*\}",
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # pgfplots tick-label lists (every Book 1-2 edition needed this)
    r"[xy]ticklabels=\{[^{}]*\}",
    # statistical variance (ch. 29, 34), not the variance of a system (ch. 4)
    r"\bvariantie(?=\s+\$\\sigma)",
    r"[Vv]ariantie\s+van\s+(?:een\s+(?:som|lineaire)|het\s+gemiddelde)",
    r"som\s+van\s+de\s+varianties",
    r"gemiddelde\s+en\s+de\s+variantie",
    # the start of a Grignard reaction (ch. 35), not radical initiation (ch. 29)
    r"vóór\s+de\s+initiatie",
    r"mislukte\s+initiatie",
    # chromatographic selectivity (ch. 31), not a reactor's selectivity (ch. 5)
    r"Selectiviteit(?=:\s+de\s+factor)",
    r"hefbomen:\s+de\s+selectiviteit",
    # the R_f of a TLC plate, not the column's retention factor k
    r"retentiefactor\s+\$R_f\$",
    # spectral resolution (ch. 33), not the chromatographic resolution (ch. 31)
    r"dan\s+de\s+resolutie",
]

"""Book 2 (University Year 1) -- nl (Dutch). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_nl.py.

Curated by the nl Book 2 agent (2026-10-04) from this edition's own harvest
(`--terms`: the same 169 targets as English) and a census of the harvested
words in their Dutch contexts -- not translated from book2_en.py.
AMBIG_POLICY stays "drop", as in English: no term is defined twice (ch. 17's
NMR shielding is "magnetische afscherming", kept apart from ch. 2's
"afscherming" on purpose).

As in English, a word is linked only once its definition has been met, so a
word defined late in one sense is safe in earlier chapters that use it in
another. Dutch homographs met AFTER their definition, each handled below:
sterk/zwak (acid strength / any strength), groep (of the periodic table / of
atoms), multipliciteit (of a cell / of an NMR signal), hydratatie (of an
alkene / of ions), axiale/equatoriale (cyclohexane bonds / VSEPR positions),
bescherming (protecting group / personal protection), gevaar (the defined
hazard / the signal word), kwantitatief (a reaction / a measurement, a
theory), eindpunt (of a titration / of anything), activiteit (thermodynamic /
optical), katalysator (a catalyst / a car's catalytic converter).

Dutch inflects adjectives (-e) and has irregular plurals that WORD_TAIL
cannot derive (molecuul/moleculen, centrum/centra, -isomeer/-isomeren); the
forms that occur, each a real occurrence of the notion, are listed in EXTRA.
"""

STOP = {
    # bare adjectives: "sterk zuur", "zwakke base" keep their links, but
    # "een sterke binding", "zwakke interacties" must not point at acid
    # strength
    "sterk", "sterke", "zwak", "zwakke",
}
NO_CAPITAL = set()
EXTRA = {
    # plurals and inflected forms of the acid-strength terms
    "sterke zuren": "def:b1:predominant-reaction:strong-acid",
    "sterke zuur": "def:b1:predominant-reaction:strong-acid",
    "zwakke zuren": "def:b1:predominant-reaction:strong-acid",
    "zwakke zuur": "def:b1:predominant-reaction:strong-acid",
    "sterke basen": "def:b1:predominant-reaction:strong-acid",
    "zwakke basen": "def:b1:predominant-reaction:strong-acid",
    # "vrij paar" / "bindend paar" are the everyday short forms of the
    # defined "vrij / bindend elektronenpaar"
    "vrij paar": "def:b1:lewis-resonance-vsepr:lewis",
    "vrije paar": "def:b1:lewis-resonance-vsepr:lewis",
    "vrije paren": "def:b1:lewis-resonance-vsepr:lewis",
    "vrije elektronenparen": "def:b1:lewis-resonance-vsepr:lewis",
    "bindend paar": "def:b1:lewis-resonance-vsepr:lewis",
    "bindende paren": "def:b1:lewis-resonance-vsepr:lewis",
    "bindende elektronenparen": "def:b1:lewis-resonance-vsepr:lewis",
    # predicative / uninflected forms (the index carries "axiale")
    "axiaal": "def:b1:stereochemistry-in-depth:conformations",
    "equatoriaal": "def:b1:stereochemistry-in-depth:conformations",
    # irregular plurals and singulars of the stereochemistry terms
    "enantiomeer": "def:b1:stereochemistry-in-depth:enantiomers",
    "diastereomeer": "def:b1:stereochemistry-in-depth:enantiomers",
    "stereo-isomeer": "def:b1:stereochemistry-in-depth:isomers",
    "chirale": "def:b1:stereochemistry-in-depth:stereocentre",
    "achirale": "def:b1:stereochemistry-in-depth:stereocentre",
    "stereogene centra": "def:b1:stereochemistry-in-depth:stereocentre",
    "stereogene centrum": "def:b1:stereochemistry-in-depth:stereocentre",
    "polaire moleculen": "def:b1:lewis-resonance-vsepr:dipole",
    "polaire molecuul": "def:b1:lewis-resonance-vsepr:dipole",
    # irregular plurals (consonant doubling, -a/-ae, -aal/-alen) and the
    # inflected adjectives of multi-word terms
    "waterstofbruggen": "def:b1:intermolecular-forces-solvents:hbond",
    "resonantiestructuren": "def:b1:lewis-resonance-vsepr:resonance",
    "kristallen": "def:b1:crystals-metals:crystal",
    "ionkristallen": "def:b1:crystals-ionic-covalent:ionic-crystal",
    "covalente kristallen": "def:b1:crystals-ionic-covalent:covalent-crystal",
    "moleculaire kristallen": "def:b1:crystals-ionic-covalent:molecular-crystal",
    "standaardpotentialen": "def:b1:nernst:electrode-potential",
    "elektrodepotentialen": "def:b1:nernst:electrode-potential",
    "subschillen": "def:b1:quantum-numbers:orbital",
    "elektronenschillen": "def:b1:quantum-numbers:orbital",
    "atoomorbitalen": "def:b1:quantum-numbers:orbital",
    "acetalen": "def:b1:acetals-protection:hemiacetal",
    "hemiacetalen": "def:b1:acetals-protection:hemiacetal",
    "oxidatiegetallen": "def:b1:nernst:oxidation-number",
    "substraten": "def:b1:nucleophilic-substitution:substitution",
    "centrale atoom": "def:b1:complexation:complex",
    "ongepaarde elektronen": "def:b1:quantum-numbers:unpaired",
    "polaire oplosmiddelen": "def:b1:intermolecular-forces-solvents:solvent-classes",
    "protische oplosmiddelen": "def:b1:intermolecular-forces-solvents:solvent-classes",
    "aprotische oplosmiddelen": "def:b1:intermolecular-forces-solvents:solvent-classes",
    "gevaren": "def:b1:lab-techniques-1:hazard",
    "bindingsdipolen": "def:b1:lewis-resonance-vsepr:dipole",
    "elementaire stappen": "def:b1:elementary-steps:elementary-step",
    "hydrofiele": "def:b1:intermolecular-forces-solvents:amphiphile",
    "hydrofobe": "def:b1:intermolecular-forces-solvents:amphiphile",
    "amfifiele": "def:b1:intermolecular-forces-solvents:amphiphile",
    "snelheidswetten": "def:b1:rate-laws:order",
    "eenheidscellen": "def:b1:crystals-metals:lattice",
    "dichtste stapelingen": "def:b1:crystals-metals:packings",
    "kubisch vlakgecentreerd": "def:b1:crystals-metals:packings",
    "kubisch ruimtegecentreerd": "def:b1:crystals-metals:packings",
    "radicalen": "def:b1:electronic-effects:intermediates",
    "reactieve intermediairen": "def:b1:electronic-effects:intermediates",
    "antiperiplanaire": "def:b1:elimination:periplanar",
    "synperiplanaire": "def:b1:elimination:periplanar",
    "partiële drukken": "def:b1:extent-q-and-k:composition",
    "grignardreagentia": "def:b1:organomagnesium:organometallic",
    "predominantiediagrammen": "def:b1:predominant-reaction:predominance",
    "verdelingsdiagrammen": "def:b1:predominant-reaction:predominance",
    "chelaten": "def:b1:complexation:chelate",
    "meertandige liganden": "def:b1:complexation:chelate",
    "oxozuren": "def:b1:p-block-13-15:oxoacid",
    "zure oxiden": "def:b1:s-block:oxide-character",
    "basische oxiden": "def:b1:s-block:oxide-character",
    "amfotere oxiden": "def:b1:s-block:oxide-character",
    "multipletten": "def:b1:structure-spectroscopy:coupling",
    "golfgetallen": "def:b1:structure-spectroscopy:wavenumber",
    "chemische verschuivingen": "def:b1:structure-spectroscopy:chemical-shift",
    "potentiaal-pH-diagrammen": "def:b1:e-ph-diagrams:e-ph-diagram",
    "intensieve grootheden": "def:b1:extent-q-and-k:variables",
    "extensieve grootheden": "def:b1:extent-q-and-k:variables",
    "zoutachtige hydriden": "def:b1:s-block:hydride",
    "covalente hydriden": "def:b1:s-block:hydride",
    "metallische hydriden": "def:b1:s-block:hydride",
    "lewiszuren": "def:b1:lewis-resonance-vsepr:lewis-acid",
    "amfotere hydroxiden": "def:b1:precipitation:amphoteric-hydroxide",
    "polyprotische zuren": "def:b1:predominant-reaction:polyprotic",
    "effect van het gemeenschappelijke ion": "def:b1:precipitation:common-ion",
    "brønstedzuur": "def:b1:predominant-reaction:bronsted",
    "zuren volgens Brønsted": "def:b1:predominant-reaction:bronsted",
    "beschermende groepen": "def:b1:acetals-protection:protecting-group",
    "elektrochemische cellen": "def:b1:nernst:cell",
    # synonyms and inflections the definitions themselves give
    "meerwaardig zuur": "def:b1:predominant-reaction:polyprotic",
    "meerwaardige zuren": "def:b1:predominant-reaction:polyprotic",
    "mengbaarheid": "def:b1:intermolecular-forces-solvents:miscibility",
    "mengbare": "def:b1:intermolecular-forces-solvents:miscibility",
    "kubisch vlakgecentreerde": "def:b1:crystals-metals:packings",
    "kubisch ruimtegecentreerde": "def:b1:crystals-metals:packings",
}
DROP = {"sterk", "sterke", "zwak", "zwakke"}
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across
# a source line break must still be protected.
EXTRA_PROTECT = [
    # "groep" is the periodic-table group only before a number (groep 16,
    # groepen 13 tot 15); "een groep atomen", "de groep", "in een groep naar
    # beneden" stay plain, as in English. The two linkable "... groep" terms
    # are excluded by the look-behinds.
    r"(?<!vertrekkende )(?<!beschermende )(?<!Vertrekkende )(?<!Beschermende )"
    r"\b[Gg]roep(?:en)?\b(?!\s*~?\d)",
    # NMR multiplicity of a signal, not the multiplicity of a cell (ch. 17)
    r"\bmultipliciteit(?=\s+van\s+elk\s+signaal)",
    r"\bmultipliciteiten(?=\s+\(aantal)",
    r"\bbenadering,\s+multipliciteiten",
    # hydration of ions, not of an alkene (ch. 28)
    r"\bhydratatie(?=\s+van\s+de\s+kleinere)",
    # VSEPR positions of a trigonal bipyramid, not cyclohexane bonds
    r"\b(?:axiale|equatoriale)(?=\s+posities?)",
    # personal protection in the safety chapter, not a protecting group
    r"\bpersoonlijke\s+bescherming",
    r"\bblootstellingsweg,\s+bescherming",
    r"\ben\s+bescherming(?=,\s+fysische)",
    # the signal word, not the defined hazard
    r"\\emph\{Gevaar\}",
    # "kwantitatief" for a theory or a measurement, not a reaction
    r"\bkwantitatief\s+gemaakt",
    r"\belektronen\s+kwantitatief",
    r"\bkwantitatieve\s+meting",
    # the end of an experiment or of a problem, not of a titration
    r"\beindpunt\s+van\s+het\s+experiment",
    r"\bals\s+eindpunt",
    # optical activity lost (ch. 19), not the thermodynamic activity
    r"\bactiviteit(?=\s+verdwijnt)",
    # a car's catalytic converter (ch. 9 caption)
    r"\bkatalysator\s+van\s+de\s+auto",
    # "niet mengbaar" is immiscible: English does not link "immiscible"
    r"\bniet[-\s]+mengba\w*",
    # a carbon-metal bond (ch. 21), not the metallic bond of ch. 5
    r"\bkoolstof-metaalbinding",
    # key names inside the periodic-table macro's options ("f block=false")
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # pgfplots tick labels are code
    r"[xy]ticklabels=\{[^{}]*\}",
]

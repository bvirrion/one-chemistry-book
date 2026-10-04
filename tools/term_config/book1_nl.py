"""Book 1 (School Chemistry, Grades 1-12) -- nl (Dutch). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_nl.py.

Curated by the nl Book 1 agent (2026-10-04) from this edition's own harvest
(340 terms) and its own frequency and chapter-set censuses against the English
edition. Nothing here is translated from book1_en.py; the English STOP choices
are mirrored only where the Dutch word carries the same everyday sense.

Three Dutch facts drive the curation:
  * lang_nl.WORD_TAIL builds -n/-en/-s plurals only. Plurals with a vowel
    change or a doubled consonant (atoom/atomen, molecuul/moleculen,
    metaal/metalen, cel/cellen, stof/stoffen) and the inflected adjective of a
    multi-word term (een vrij elektronenpaar / de vrije elektronenparen, het
    periodiek systeem / het periodieke systeem) are declared in EXTRA.
  * "zeven" is both the sieving of grade 3 and the number seven;
    "rendement" is both a synthesis yield and the efficiency of a heating;
    "groep" is the periodic-table group only before a number. EXTRA_PROTECT.
  * "oplossing" (solution) is defined in grade 2 but is on nearly every page
    afterwards in its general sense; like the English edition, it is
    stoplisted and its multi-word terms (waterige oplossing, zure oplossing,
    ...) keep their links.
"""

STOP = {
    # everyday words defined in the early grades, used in their everyday sense
    # ever after; their multi-word terms keep their links ("eigenschap van een
    # materiaal", "waterige oplossing", "chemische familie").
    "oplossing", "oplossingen", "materiaal", "materialen", "voorwerp",
    "voorwerpen", "periode", "perioden", "periodes",
    # the atom's symbol in its own chapter; a quantity's symbol (n, M, c)
    # everywhere after. "symbool van een atoom" keeps its link.
    "symbool", "symbolen",
    # reaction categories: "de additie van de titrant", "een substitutie van
    # het ene oplosmiddel door een ander". "additiepolymeer" keeps its link.
    "additie", "substitutie",
    # "de capaciteit van een buffer": only the cell's capacity is defined.
    "capaciteit",
}
NO_CAPITAL = set()
EXTRA = {
    # plurals the tail cannot build (vowel change, doubled consonant, -'s)
    "moleculen": "def:g7:atoms-and-molecules:molecule",
    "metalen": "def:g9:periodic-table-first-look:metal",
    "niet-metalen": "def:g9:periodic-table-first-look:metal",
    "polymeren": "def:g12:polymers:polymer",
    "additiepolymeren": "def:g12:polymers:addition-polymer",
    "condensatiepolymeren": "def:g12:polymers:addition-polymer",
    "alkanen": "def:g11:organic-skeletons:alkane",
    "alkenen": "def:g11:functional-groups:halogenoalkane",
    "halogeenalkanen": "def:g11:functional-groups:halogenoalkane",
    "carbonzuren": "def:g11:functional-groups:carboxylic-acid",
    "brandstoffen": "def:g4:what-a-fire-needs:fuel",
    "kunststoffen": "def:g8:plastics:plastic",
    "grondstoffen": "def:g5:raw-materials-and-recycling:raw-material",
    "hulpbronnen": "def:g5:raw-materials-and-recycling:resource",
    "hernieuwbare hulpbronnen": "def:g5:raw-materials-and-recycling:resource",
    "broeikasgassen": "def:g8:combustion-and-fuels:greenhouse",
    "waterstofbruggen": "def:g11:polarity-and-cohesion:hydrogen-bond",
    "lewisstructuren": "def:g10:lewis-and-shape:lewis-structure",
    "reagentia": "def:g7:identifying-substances:characteristic-test",
    "indices": "def:g7:atoms-and-molecules:formula",
    "elektrochemische cellen": "def:g12:cells-and-electrolysis:cell",
    "halfcellen": "def:g12:cells-and-electrolysis:cell",
    "zoutbruggen": "def:g12:cells-and-electrolysis:cell",
    "accu's": "def:g12:cells-and-electrolysis:electrolysis",
    "molaire massa's": "def:g10:the-mole:molar-mass",
    "absorptiespectra": "def:g11:absorbance:spectrum",
    "infraroodspectra": "def:g11:infrared:spectrum",
    "NMR-spectra": "def:g12:proton-nmr:spectrum",
    "golfgetallen": "def:g11:infrared:wavenumber",
    "multipletten": "def:g12:proton-nmr:multiplet",
    "predominantiediagrammen": "def:g12:buffers-predominance:predominance",
    "verdelingsdiagrammen": "def:g12:buffers-predominance:predominance",
    "voortgangstabellen": "def:g10:reaction-progress-table:extent",
    "elementaire stappen": "def:g12:curly-arrows:mechanism",
    "repeterende eenheden": "def:g12:polymers:repeat-unit",
    # singulars of terms the definitions give in the plural
    "isomeer": "def:g11:organic-skeletons:isomer",
    "structuurisomeer": "def:g11:organic-skeletons:isomer",
    "stereo-isomeer": "def:g12:stereochemistry:stereoisomer",
    "enantiomeer": "def:g12:stereochemistry:enantiomer",
    "diastereomeer": "def:g12:stereochemistry:diastereomer",
    # the inflected adjective (de/het-form, plural) of multi-word terms
    "vrije elektronenparen": "def:g10:lewis-and-shape:lone-pair",
    "vrije elektronenpaar": "def:g10:lewis-and-shape:lone-pair",
    "bindende elektronenparen": "def:g10:lewis-and-shape:lone-pair",
    "bindende elektronenpaar": "def:g10:lewis-and-shape:lone-pair",
    "polaire moleculen": "def:g11:polarity-and-cohesion:polar-molecule",
    "polaire molecuul": "def:g11:polarity-and-cohesion:polar-molecule",
    "apolaire moleculen": "def:g11:polarity-and-cohesion:polar-molecule",
    "apolaire molecuul": "def:g11:polarity-and-cohesion:polar-molecule",
    "moleculaire vaste stoffen": "def:g11:polarity-and-cohesion:molecular-solid",
    "zuivere stoffen": "def:g6:pure-substances-and-mixtures:pure-substance",
    "chemische stoffen": "def:g6:pure-substances-and-mixtures:species",
    "opgeloste stoffen": "def:g6:solutions-and-solubility:solute",
    "natuurlijke stoffen": "def:g10:chemical-species:natural",
    "synthetische stoffen": "def:g10:chemical-species:natural",
    "homogene mengsels": "def:g6:pure-substances-and-mixtures:homogeneous",
    "homogene mengsel": "def:g6:pure-substances-and-mixtures:homogeneous",
    "heterogene mengsels": "def:g6:pure-substances-and-mixtures:homogeneous",
    "heterogene mengsel": "def:g6:pure-substances-and-mixtures:homogeneous",
    "racemische mengsel": "def:g12:stereochemistry:enantiomer",
    "racemische mengsels": "def:g12:stereochemistry:enantiomer",
    "stoichiometrische mengsel": "def:g10:reaction-progress-table:stoichiometric",
    "chemische elementen": "def:g9:inside-the-atom:element",
    "chemische element": "def:g9:inside-the-atom:element",
    "chemische systeem": "def:g10:reaction-progress-table:system",
    "periodieke systeem": "def:g9:periodic-table-first-look:periodic-table",
    "natuurlijke materialen": "def:g5:raw-materials-and-recycling:natural-material",
    "vervaardigde materialen": "def:g5:raw-materials-and-recycling:natural-material",
    "kunstmatige materialen": "def:g8:plastics:artificial",
    "synthetische materialen": "def:g8:plastics:artificial",
    "sterke zuren": "def:g12:ka-and-pka:strong-acid",
    "sterke zuur": "def:g12:ka-and-pka:strong-acid",
    "zwakke zuren": "def:g12:ka-and-pka:strong-acid",
    "zwakke zuur": "def:g12:ka-and-pka:strong-acid",
    "asymmetrische koolstofatomen": "def:g12:stereochemistry:chiral",
    "asymmetrische koolstofatoom": "def:g12:stereochemistry:chiral",
    "molaire volume": "def:g10:the-mole:molar-volume",
    "fossiele brandstoffen": "def:g8:combustion-and-fuels:fossil",
    "hernieuwbare brandstoffen": "def:g8:combustion-and-fuels:fossil",
    # adjectives the definitions give uninflected
    "exotherme": "def:g11:reaction-energy:exothermic",
    "endotherme": "def:g11:reaction-energy:exothermic",
    "chirale": "def:g12:stereochemistry:chiral",
    "chemoselectieve": "def:g12:synthesis-strategy:chemoselective",
    "mengbare": "def:g6:solutions-and-solubility:miscible",
    "niet-mengbare": "def:g6:solutions-and-solubility:miscible",
    "hydrofiele": "def:g11:dissolution:hydrophilic",
    "hydrofobe": "def:g11:dissolution:hydrophilic",
    "amfifiele": "def:g11:dissolution:amphiphilic",
    # the plural of the separable verb of grade 2 ("lost op" is harvested),
    # and the third person of "mengen"
    "lossen op": "def:g2:mixing-and-dissolving:dissolve",
    "mengt": "def:g2:mixing-and-dissolving:mix",
    "oplost": "def:g2:mixing-and-dissolving:dissolve",
    # the verbal noun of burning ("het verbranden van steenkool"); the finite
    # forms (brandt, verbrandt) are left plain, as English leaves "burns"
    "verbranden": "def:g4:what-a-fire-needs:burning",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across a
# source line break must still be protected.
EXTRA_PROTECT = [
    # Coordinator, 2026-10-04 (found by the Indonesian Book 1 agent): the
    # capitalised, colon-led head of g12 solutions/11 exo 1 is the hydration of
    # ETHENE (an addition), not the hydration of ions it linked to.
    r"Hydratatie(?=:)",
    # The isomer letters Z and E are harvested from \emph{Z}/\emph{E}; the
    # Dutch tail (?:e?[ns])? then turns them into the article "een", the
    # conjunction "en", the numeral "zes" and the zinc symbol "Zn" (184 false
    # links in the first uncurated run). Mask those words; the bare letters
    # keep their links.
    r"\b(?:[Ee]en|[Ee]n|[Zz]es|Zn|[Ee]s|[Zz]en)\b",
    # "branden" as a lamp that lights up, and as a corrosive that burns the
    # skin -- not combustion
    r"lampje\s+(?:laten\s+)?branden",
    r"(?:verbranden|branden)(?=\s+(?:de\s+)?huid)",
    r"huid\s+verbranden",
    r"veel\s+erger\s+branden",
    # a conductivity coefficient (lambda_i), not a stoichiometric one
    r"coëfficiënt(?=\s+\$\\lambda)",
    # "groep" is the periodic-table group only before a number (groep 1,
    # groepen 13 tot 18); "karakteristieke groep", "beschermende groep",
    # "een groep atomen" stay plain. The linkable "... groep" terms are
    # excluded by the look-behinds.
    r"(?<!karakteristieke )(?<!beschermende )"
    r"(?<!Karakteristieke )(?<!Beschermende )"
    r"\b[Gg]roep(?:en)?\b(?!\s*~?\d)",
    # "zeven" the number, not the sieving of grade 3 (and "zeven" the plural
    # of "zeef", a sieve, in the grade-3 problem). The look-ahead admits an
    # \omterm wrapper on the next word, or a second --apply links the number
    # once its neighbour has been linked (found: the dry run was not 0).
    r"[Zz]even(?=\s+(?:\\omterm\{[^{}]*\}\{)?(?:gewone|stukjes|moleculen|formules|codes|harsidentificatiecodes|elektronen|O\b))",
    r"er\s+zijn\s+er\s+zeven",
    r"halogenen\}?\s+zeven",
    r"soort\s+zeven",
    # "rendement" as the efficiency of a heating (grade 11), not a yield
    r"rendement\s+van\s+de\s+verwarming",
    r"Rendement(?=\s+\$20\.9)",
    # the hydration of an alkene (an addition), not the hydration of ions
    r"[Hh]ydratatie(?=\s+van\s+etheen)",
    # alcohol the drink, in the breath-test problem
    r"blaastests\s+op\s+alcohol",
    # the data key (first argument) of the infrared chapter's \irpanel
    r"\\irpanel\{[^{}]*\}",
    # chemfig settings: "atom sep=1.5em" is a key
    r"\\setchemfig\{[^{}]*\}",
    # key names inside the periodic-table macro's options
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
]

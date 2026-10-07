"""Book 3 (University Chemistry, Year 2) -- fr (French). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_fr.py.

Curated by the fr Book 3 agent (2026-10-06) from this edition's own harvest
(`--terms`: 427 linkable terms on the same 204 targets as English) and a
census of the linked words in their French contexts -- not translated from
book3_en.py. AMBIG_POLICY stays "drop", as in English: no term is defined
twice.

A word is linked only once its definition has been met, so a word defined
late in one sense is safe in earlier chapters that use it in another (ch. 21's
"traitement réducteur" precedes the definition of ch. 35; ch. 34's water
"traitement" too). The solutions come after every chapter, so every word
there is past its definition. French homographs met AFTER their definition,
each handled below:

- fragment (ch. 15's fragment method / ozonolysis, mass-spectrum and
  structure fragments): the bare word is stoplisted, "orbitale de fragment"
  and "ion fragment" keep their links;
- variance (of a system, ch. 4 / statistical variance, ch. 29 and 34);
- propagation (a chain step, ch. 29 / propagation of uncertainty, ch. 34);
- amorçage (radical initiation, ch. 29 / the start of a Grignard reaction,
  ch. 35);
- sélectivité (of a reactor, ch. 5 / chromatographic selectivity, ch. 31);
- résolution (chromatographic, ch. 31 / the resolving power of a mass
  analyser, high-resolution MS, an NMR resolution, solving a structure);
- résidu (a regression residual, ch. 34 / amino-acid residues and the
  residues of a reaction, in the solutions);
- traitement (the work-up of a reaction, ch. 35 / nothing after it: checked);
- indice(s) de liaison (the diatomic bond order, ch. 14 / ch. 16's Hückel pi
  bond indices): routed or masked in ch. 16; no Hückel-sense use after it.
"""

STOP = {
    # ch. 15's fragment method: the bare word is used later for ozonolysis
    # fragments (ch. 21, 25), synthons (ch. 28), mass-spectrum fragments
    # (ch. 32-33) and pieces of a structure.
    "fragment", "fragments", "Fragment", "Fragments",
}
NO_CAPITAL = set()
# Forms the harvest cannot derive, each a real occurrence of the notion:
# irregular plurals (radial/radiaux, plateau/plateaux), the bare "conversion"
# French uses, as English does, for the defined "taux de conversion" (every
# use after ch. 5 is the conversion of a reactant; "conversion par passage"
# is its own, longer term), and the short forms "nombre de plateaux" and
# "hauteur de plateau" of ch. 31's defined plate number and plate height.
EXTRA = {
    # the bare noun of the "Enolates" definition (only "ion" phrase harvested;
    # coordinator, 2026-10-07, as English and Arabic)
    "énolate": "def:b2:enolates-aldol:enolate",
    "nœuds radiaux": "def:b2:atomic-orbitals:node",
    "plateaux théoriques": "def:b2:liquid-vapour-diagrams:fractional-distillation",
    "conversion": "def:b2:continuous-reactors:conversion",
    "conversions": "def:b2:continuous-reactors:conversion",
    "nombre de plateaux": "def:b2:chromatography:plates",
    "hauteur de plateau": "def:b2:chromatography:plates",
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
    r"\bvariances?\b(?=\s+\$\\sigma)",
    r"[Vv]ariance\s+(?:de\s+la\s+moyenne|d'une\s+(?:somme|combinaison|loi))",
    r"somme\s+des\s+variances",
    r"moyenne\s+et\s+de\s+la\s+variance",
    # propagation of uncertainty (ch. 34), not a chain-propagation step (ch. 29)
    r"[Pp]ropagation(?=\s+des\s+incertitudes)",
    r"règle\s+générale\s+de\s+propagation",
    r"[Ll]oi\s+de\s+propagation",
    # the start of a Grignard reaction (ch. 35), not radical initiation (ch. 29)
    r"avant\s+l'amorçage",
    r"défaut\s+d'amorçage",
    # chromatographic selectivity (ch. 31), not a reactor's selectivity (ch. 5)
    r"Sélectivité(?=~:\s+le\s+facteur)",
    r"leviers~:\s+la\s+sélectivité",
    # resolving power of an analyser, high-resolution MS, an NMR resolution,
    # solving a structure -- not the chromatographic resolution (ch. 31)
    r"[Pp]ouvoirs?\s+de\s+résolution",
    r"haute\s+résolution",
    r"que\s+la\s+résolution",
    r"résolution\s+d'une\s+structure",
    # amino-acid residues and reaction residues, not regression residuals
    r"deux\s+résidus",
    r"dans\s+les\s+résidus",
    # the plates of a distillation column (solutions of ch. 7), not ch. 31's
    # chromatographic plate number
    r"même\s+nombre\s+de\s+plateaux",
    # ch. 16, the Hückel pi bond indices written without "pi" (the method
    # before the definition, the benzene proof): not the diatomic bond order
    # of ch. 14, which "indice de liaison" alone would reach; English writes
    # "bond indices" there and links neither (coordinator, chapter-set census)
    r"charges\s+et\s+les\s+indices\s+de\s+liaison",
    r"tous\s+les\s+indices\s+de\s+liaison\s+sont",
    # "indices de liaison $\pi$" (ch. 16 exercises): the plural with the
    # $\pi$ after the noun cannot reach def:b2:huckel:indices (the masked
    # math breaks the match), so it is masked rather than routed
    r"indices\s+de\s+liaison(?=\s+\$\\pi\$)",
]

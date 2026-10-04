"""Book 2 (University Year 1) -- es (Spanish). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_es.py.

Curated by the es Book 2 agent (2026-10-04) from this edition's own harvest
(`--terms`, 389 linkable terms) and a census of the harvested words in their
Spanish contexts, line by line against the English links -- not translated
from book2_en.py. AMBIG_POLICY stays "drop", as in English: no term is
defined twice.

As in English, a word is linked only once its definition has been met, so a
word defined late in one sense is safe in earlier chapters that use it in
another. Spanish homographs met AFTER their definition, each handled below:
fuerte/débil (acid strength / any strength), grupo (of the periodic table /
of atoms), multiplicidad (of a cell / of an NMR signal), hidratación (of an
alkene / of ions), axial/ecuatorial (cyclohexane bonds / VSEPR positions),
protección (protecting group / personal protection), peligro (the defined
hazard / the GHS08 pictogram's name and the signal word), red (the crystal
lattice / a covalent or hydrogen-bond network), periodo (a row of the table /
an induction period), bloque (the s/p block / a block of zinc), cuantitativa
(a reaction / a measurement, a theory), actividad (thermodynamic / optical).
"""

STOP = set()
# "Red" capitalised is the reduced form of a couple (Ox/Red, ch. 13), never
# the crystal lattice.
NO_CAPITAL = {"red"}
# Forms the harvest cannot derive, each a real occurrence of the notion:
# masculine and plural adjectives (the definition prints the feminine
# "cuantitativa"), the adverb English also links ("quantitatively").
EXTRA = {
    "cuantitativamente": "def:b1:extent-q-and-k:quantitative",
}
# Dropped outright: the bare adjectives. "ácido fuerte", "base débil" keep
# their links as multi-word terms, but "un enlace fuerte", "un nucleófilo
# débil", "el ácido más fuerte", "una constante débil" must not point at
# acid strength, and a stoplist alone still lets the per-chapter map link
# them (the French Book 2 agent's finding, 2026-10-04).
DROP = {"fuerte", "fuertes", "débil", "débiles"}
# Plurals the tail cannot reach (the accent of a final -ón, -ión falls in the
# plural: electrón -> electrones) and the other gender of the adjectives the
# definitions print in one gender only; each kept only if it occurs.
DERIVED = {
    "adición electrófila": ["adiciones electrófilas"],
    "carbanión": ["carbaniones"],
    "carbocatión": ["carbocationes"],
    "configuración": ["configuraciones"],
    "configuración electrónica": ["configuraciones electrónicas"],
    "conformación": ["conformaciones"],
    "conformación alternada": ["conformaciones alternadas"],
    "conformación eclipsada": ["conformaciones eclipsadas"],
    "disolución equivalente": ["disoluciones equivalentes"],
    "disolución tampón": ["disoluciones tampón"],
    "electrón desapareado": ["electrones desapareados"],
    "fracción molar": ["fracciones molares"],
    "fracción másica": ["fracciones másicas"],
    "integración": ["integraciones"],
    "orden global": ["órdenes globales"],
    "interacción de London": ["interacciones de London"],
    "interacción de Keesom": ["interacciones de Keesom"],
    "interacción de Debye": ["interacciones de Debye"],
    "presión parcial": ["presiones parciales"],
    "proyección de Newman": ["proyecciones de Newman"],
    "proyección de Fischer": ["proyecciones de Fischer"],
    "reacción cuantitativa": ["reacciones cuantitativas"],
    "reacción regioselectiva": ["reacciones regioselectivas"],
    "reacción estereoselectiva": ["reacciones estereoselectivas"],
    "reacción estereoespecífica": ["reacciones estereoespecíficas"],
    "rotación específica": ["rotaciones específicas"],
    "semiecuación": ["semiecuaciones"],
    "valoración": ["valoraciones"],
    "valoración directa": ["valoraciones directas"],
    "valoración potenciométrica": ["valoraciones potenciométricas"],
    "hidrófilo": ["hidrófila", "hidrófilas"],
    "hidrófobo": ["hidrófoba", "hidrófobas"],
    "anfífila": ["anfífilo", "anfífilos"],
}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across
# a source line break must still be protected.
EXTRA_PROTECT = [
    # Coordinator, 2026-10-04: the zinc anode blocks of ch. 14 are not the
    # periodic-table block; English now protects the same sites.
    r"bloques?(?=\s+gris)",

    # "grupo" is the periodic-table group only before a number (grupo 16,
    # grupos 13, 14 y 15); "grupo metilo", "grupo OH", "su grupo" stay
    # plain. Spanish puts the modifier after the noun, so the four linkable
    # "grupo ..." terms are excluded by a lookahead.
    r"\b[Gg]rupos?\b(?!\s*~?\d)"
    r"(?!\s+(?:dadore?s?|aceptore?s?|salientes?|protectore?s?)\b)",
    # NMR multiplicity of a signal, not the multiplicity of a cell (ch. 17)
    r"\bmultiplicidad(?:es)?(?=\s+(?:de\s+cada\s+señal|\(número))",
    r"\bmultiplicidades(?=,\s+(?:\\omterm\{[^{}]*\}\{)?integraciones)",
    # hydration of ions, not of an alkene (ch. 28)
    r"\bhidratación(?=\s+de\s+los\s+iones)",
    # VSEPR positions of a trigonal bipyramid, not cyclohexane bonds
    r"\bposiciones\s+ecuatoriales(?=\s+de\s+una\s+bipirámide)",
    # personal protection in the safety chapter, not a protecting group
    r"\bprotección\s+(?:individual|para\s+los\s+ojos)",
    r"\bexposición\s+y\s+protección",
    r"\bvía,\s+protección",
    # an induction period, not a row of the table (ch. 9)
    r"\bperiodos?\s+de\s+inducción",
    # a block of zinc (a sacrificial anode), not the s/p/d/f block
    r"\bbloques?\s+de\s+cinc",
    # "cuantitativa" as a kind of theory or measurement, not a reaction
    r"\bhacen\s+cuantitativa",
    r"\bmedida\s+cuantitativa",
    # optical activity lost, not the thermodynamic activity (ch. 19)
    r"\bpérdida\s+de\s+actividad",
    # the GHS08 pictogram's name and the signal word, not the defined hazard
    r"\bpeligro\s+para\s+la\s+salud",
    r"\\emph\{Peligro\}",
    # key names inside the periodic-table macro's options ("f block=false")
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # "red" is also a network (covalent, of hydrogen bonds in ice, of SiO4
    # tetrahedra), not the crystal lattice of ch. 5
    r"\bred(?=\s+(?:covalente|abierta|está\s+parcialmente|se\s+manifiesta|de\s+\\ce))",
    r"\bred(?=\s+hexagonal\s+de\s+(?:\\omterm\{[^{}]*\}\{)?enlaces)",
    # pgfplots tick labels are code
    r"[xy]ticklabels=\{[^{}]*\}",
]

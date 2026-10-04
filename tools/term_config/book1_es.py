"""Book 1 (School Chemistry, Grades 1-12) -- es (Spanish). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_es.py.

Curated by the es Book 1 agent (2026-10-04) from this edition's own harvest
(`link_defined_terms.py --book 1 --lang es --terms`), never translated from
book1_en.py. The English homograph list was the place to start looking:

  solution  -> es has two words: "disolución" (the mixture, and the act of
               dissolving -- both are the grade-2 definition) and "solución"
               (of an exercise, never a term). en STOPs "solution" and links
               only its multi-word terms; es does the same with "disolución"
               so that the target keeps en's reach and density
               ("disolución acuosa", "disolución tampón"... keep their links).
  group     -> "grupo" is everywhere ("grupo funcional", "grupo ácido",
               "grupo de protones"): masked unless a number follows, as in en.
  period    -> "periodo" is also a period of time, and "periodo de
               semirreacción" is a term of its own: STOP the bare word.
  shell     -> "capa" is mostly a LAYER (a layer of solvent, of zinc, of sand,
               of oil, "capa fina"): masked unless a shell number or
               "externa"/"ocupada"/"completa" follows. en has two words, es one.
  reagent/reactant -> both "reactivo" in es: the harvest finds it twice
               (identifying substances, chemical reactions) and the
               nearest-preceding rule links each chapter to the sense it
               last met. Left to that rule (a reagent IS a reactant of its
               test reaction, so the later chapters' reagent sense lands on a
               true statement). The adjective "reactivo" (reactive) is masked.
  mole      -> "mol" is both the name of the unit (the term) and its symbol in
               running prose ("2/3 mol de éster"); en's term "mole" never
               meets the symbol, so the symbol after a number is masked.
  product, material, object, symbol, addition, substitution, capacity:
               everyday senses, STOP as in en.

es-only work:
  * the singulars of the terms defined in the plural, the other gender of
    the adjectives, and the conjugated verbs of grades 2-4: DERIVED.
"""

STOP = {
    # an atom's symbol in its own chapter; a quantity's symbol ever after.
    # "símbolo de un átomo" keeps its link.
    "símbolo", "símbolos",
    # everyday words used in their everyday sense after their early-grade
    # definition ("un producto de limpieza", "el material de una botella",
    # "un periodo de tiempo"); their multi-word terms keep their links
    # ("disolución acuosa", "propiedad de un material", "periodo de
    # semirreacción").
    "disolución", "disoluciones", "material", "materiales", "objeto",
    "objetos", "producto", "productos", "periodo", "periodos",
    # reaction categories: "la adición del valorante", "la sustitución de un
    # disolvente". "Polímero de adición" keeps its link.
    "adición", "sustitución",
    # "la capacidad de un tampón": only the cell's capacity is defined.
    "capacidad",
}
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {
    # terms defined in the plural, used in the singular
    "isómeros": ["isómero"],
    "isómeros constitucionales": ["isómero constitucional"],
    "estereoisómeros": ["estereoisómero"],
    "diastereoisómeros": ["diastereoisómero"],
    "enantiómeros": ["enantiómero"],
    "miscibles": ["miscible"],
    "inmiscibles": ["inmiscible"],
    "colores complementarios": ["color complementario"],
    # plurals the tail "(?:e?s)?" cannot make: the written accent of "-ión"
    # drops in the plural ("catión" -> "cationes", "reacción" ->
    # "reacciones"); every other plural of the harvest is regular.
    "anión": ["aniones"],
    "catión": ["cationes"],
    "concentración molar": ["concentraciones molares"],
    "concentración en masa": ["concentraciones en masa"],
    "configuración electrónica": ["configuraciones electrónicas"],
    "conformación": ["conformaciones"],
    "disolución acuosa": ["disoluciones acuosas"],
    "disolución ácida": ["disoluciones ácidas"],
    "disolución básica": ["disoluciones básicas"],
    "disolución neutra": ["disoluciones neutras"],
    "disolución saturada": ["disoluciones saturadas"],
    "disolución tampón": ["disoluciones tampón"],
    "disolución patrón": ["disoluciones patrón"],
    "disolución madre": ["disoluciones madre"],
    "ecuación ajustada": ["ecuaciones ajustadas"],
    "ecuación química": ["ecuaciones químicas"],
    "interacción de van der Waals": ["interacciones de van der Waals"],
    "reacción química": ["reacciones químicas"],
    "reacción redox": ["reacciones redox"],
    "reacción total": ["reacciones totales"],
    "reacción no total": ["reacciones no totales"],
    "reacción de primer orden": ["reacciones de primer orden"],
    "semiecuación": ["semiecuaciones"],
    "transformación física": ["transformaciones físicas"],
    "valoración": ["valoraciones"],
    "valoración conductimétrica": ["valoraciones conductimétricas"],
    "valoración pH-métrica": ["valoraciones pH-métricas"],
    "extracción": ["extracciones"],
    "destilación": ["destilaciones"],
    "dilución": ["diluciones"],
    "oxidación": ["oxidaciones"],
    "reducción": ["reducciones"],
    # adjectives defined in one gender, used in the other
    "exotérmica": ["exotérmico", "exotérmicas", "exotérmicos"],
    "endotérmica": ["endotérmico", "endotérmicas", "endotérmicos"],
    "hidrófila": ["hidrófilo", "hidrófilos", "hidrófilas"],
    "hidrófoba": ["hidrófobo", "hidrófobos", "hidrófobas"],
    "anfífilo": ["anfífila", "anfífilos", "anfífilas"],
    "quimioselectiva": ["quimioselectivo"],
    # the verbs of grades 2-4, defined in the infinitive or one person and
    # used conjugated (en links dissolve/dissolves/dissolved, mix/mixes/mixed,
    # burn/burns/burning).
    # (the participle "disuelto" is left out, as en leaves out "dissolved":
    # with it es linked the target 263 times against en's 115.)
    "disolverse": ["disolver", "disuelven", "disolviendo"],
    "evaporación": ["evaporar", "evapora", "evaporan", "evaporando"],
    # the usual word order of the bond is the other one ("un doble enlace")
    "enlace doble": ["doble enlace", "dobles enlaces"],
    "enlace triple": ["triple enlace", "triples enlaces"],
    # the synonym the later chapters use (the definition names it)
    "par no enlazante": ["par libre", "pares libres"],
    # the synonym the later chapters use ("reciclado químico")
    "reciclaje": ["reciclado"],
    "mezclar": ["mezclan", "mezclado", "mezclada", "mezclados",
                "mezcladas"],
    "arder": ["arden", "ardiendo"],
}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped
# across a source line break must still be protected.
EXTRA_PROTECT = [
    # Coordinator, 2026-10-04 (found by the Indonesian Book 1 agent): the
    # capitalised, colon-led head of g12 solutions/11 exo 1 is the hydration of
    # ETHENE (an addition), not the hydration of ions it linked to.
    r"Hidratación(?=:)",
    # "vaso de precipitados" is a BEAKER, not a precipitate (coordinator
    # finding, 2026-10-04). First in the list: the patterns are joined into
    # one alternation, so nothing earlier may take a word of the phrase.
    r"\b[Vv]asos?\s+de\s+precipitados\b",
    # "grupo" is the periodic-table group only before a number (grupo 1,
    # grupos 13 a 18); "grupo funcional", "grupo alquilo", "grupo
    # protector", "grupo ácido", "grupo de protones" stay plain. The linkable
    # "grupo ..." terms follow the word, so they are excluded by lookahead.
    r"\b[Gg]rupos?\b(?!\s*~?\d)(?!\s+(?:funcional|alquilo|protector))",
    # "capa" is an electron shell only before its number or as the outer,
    # occupied or full shell; a layer of solvent, of zinc, of sand stays plain.
    r"\b[Cc]apas?\b(?!\s*~?\d)(?!\s+(?:externa|ocupada|completa))",
    # "mol" after a number or a formula is the unit symbol, not the term
    r"(?:(?<=\d)|(?<=\$)|(?<=\}))(?:\s|~)+mol\b",
    # "Es" (it is) at the head of a question is the E isomer plus the tail
    r"\bEs\b",
    # "reactivo" the ADJECTIVE (reactive), not the reactant/reagent noun:
    # "un grupo reactivo", "¿por qué es tan reactivo?", "no metales de color
    # y reactivos" -- en has "reactive", a different word, and never links it
    # (a lookbehind: the "grupo" mask above has already taken the word)
    r"(?:(?<=grupo )|(?<=grupo\n)|(?<=grupos )|(?<=grupos\n))reactivos?\b",
    r"(?<=\btan )reactivos?\b",
    r"(?<=de color y )reactivos\b",
    # a defined word as one half of a hyphenated compound
    r"ion-litio",
    # the hydration of an alkene (an addition), not the hydration of ions
    r"hidratación(?=\s+del\s+eteno)",
    # the data key (first argument) of the infrared chapter's \irpanel
    r"\\irpanel\{[^{}]*\}",
    # chemfig settings: "atom sep=1.5em" is a key, not the word atom
    r"\\setchemfig\{[^{}]*\}",
    # key names inside the periodic-table macro's options
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
]

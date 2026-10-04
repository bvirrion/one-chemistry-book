"""Book 1 (School Chemistry, Grades 1-12) -- pt (Brazilian Portuguese). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_pt.py.

Curated by the pt Book 1 agent (2026-10-04) from this edition's own harvest
(`link_defined_terms.py --book 1 --lang pt --terms`), never translated from
book1_en.py. The English homograph list was the place to start looking:

  solution  -> "solução" is also the solution of an exercise: STOP, as in en.
  group     -> "grupo" is everywhere ("grupo funcional", "grupo de prótons"):
               masked unless a number follows, as in en.
  period    -> "período" is also a period of time: STOP, as in en.
  shell     -> "camada" is mostly a LAYER here (a layer of solvent, of zinc,
               of sand, "camada delgada"): masked unless a shell number or
               "externa"/"ocupada" follows. en has two words, pt one.
  product, material, object, symbol, addition, substitution, capacity:
               everyday senses, STOP as in en.
  reagent/reactant -> both "reagente" in pt: the harvest finds it twice
               (identifying substances, chemical reactions) and the
               nearest-preceding rule links each chapter to the sense it
               last met. Left to that rule.

pt-only work:
  * "ar" (air) is two letters long, under harvest.py's 3-character floor,
    so it fell to its own chapter only (en links "air" 220 times): EXTRA.
  * Irregular plurals the optional tail "(?:e?s)?" cannot make ("-ção" ->
    "-ções", "-al" -> "-ais", "-el" -> "-eis", "álcool" -> "álcoois") and
    the singulars of the terms defined in the plural: DERIVED.
"""

STOP = {
    # an atom's symbol in its own chapter; a quantity's symbol ever after.
    # "símbolo de um átomo" keeps its link.
    "símbolo", "símbolos",
    # everyday words used in their everyday sense after their early-grade
    # definition ("a solução do exercício", "um produto de limpeza",
    # "o material de uma garrafa", "um período de tempo"); their multi-word
    # terms keep their links ("solução aquosa", "propriedade de um material").
    "solução", "soluções", "material", "objeto", "produto", "produtos",
    "período",
    # reaction categories: "a adição do titulante", "a substituição de um
    # solvente". "Polímero de adição" keeps its link.
    "adição", "substituição",
    # "a capacidade de um tampão": only the cell's capacity is defined.
    "capacidade",
}
NO_CAPITAL = set()
EXTRA = {
    # under the 3-character floor of harvest.py; "ar" has no other sense
    "ar": "def:g4:air-a-mixture-of-gases:air",
}
DROP = set()
DERIVED = {
    # irregular plurals (the tail "(?:e?s)?" makes only regular ones)
    "álcool": ["álcoois"],
    "metal": ["metais"],
    "não metal": ["não metais"],
    "quiral": ["quirais"],
    "combustão": ["combustões"],
    "combustível": ["combustíveis"],
    "combustível fóssil": ["combustíveis fósseis"],
    "combustível renovável": ["combustíveis renováveis"],
    "carga parcial": ["cargas parciais"],
    "concentração em massa": ["concentrações em massa"],
    "concentração molar": ["concentrações molares"],
    "configuração eletrônica": ["configurações eletrônicas"],
    "conformação": ["conformações"],
    "diluição": ["diluições"],
    "equação balanceada": ["equações balanceadas"],
    "equação por extenso": ["equações por extenso"],
    "equação química": ["equações químicas"],
    "extração": ["extrações"],
    "fórmula estrutural": ["fórmulas estruturais"],
    "fórmula estrutural condensada": ["fórmulas estruturais condensadas"],
    "grupo funcional": ["grupos funcionais"],
    "interação de van der Waals": ["interações de van der Waals"],
    "ligação covalente": ["ligações covalentes"],
    "ligação de hidrogênio": ["ligações de hidrogênio"],
    "ligação dupla": ["ligações duplas"],
    "ligação tripla": ["ligações triplas"],
    "ligação polar": ["ligações polares"],
    "material fabricado": ["materiais fabricados"],
    "material natural": ["materiais naturais"],
    "material sintético": ["materiais sintéticos"],
    "material artificial": ["materiais artificiais"],
    "oxidação": ["oxidações"],
    "redução": ["reduções"],
    "reação química": ["reações químicas"],
    "reação de oxirredução": ["reações de oxirredução"],
    "reação de primeira ordem": ["reações de primeira ordem"],
    "reação total": ["reações totais"],
    "reação não total": ["reações não totais"],
    "semirreação": ["semirreações"],
    "solução aquosa": ["soluções aquosas"],
    "solução ácida": ["soluções ácidas"],
    "solução básica": ["soluções básicas"],
    "solução neutra": ["soluções neutras"],
    "solução saturada": ["soluções saturadas"],
    "solução-tampão": ["soluções-tampão"],
    "solução-padrão": ["soluções-padrão"],
    "titulação": ["titulações"],
    "titulação condutométrica": ["titulações condutométricas"],
    "titulação potenciométrica": ["titulações potenciométricas"],
    "transformação física": ["transformações físicas"],
    "transformação química": ["transformações químicas"],
    "transformação reversível": ["transformações reversíveis"],
    "transformação irreversível": ["transformações irreversíveis"],
    # the verbs of grades 2-3, defined in the infinitive and used conjugated
    # (en links mix/mixes/mixed/mixing and evaporate/evaporates). "mistura"
    # itself is the noun of grade 6, "dissolvido" is left to the plain
    # harvest (adding it would double en's count).
    "misturar": ["misturado", "misturada", "misturados", "misturadas",
                 "misture", "misturam", "misturamos", "misturando"],
    "evaporação": ["evapora", "evaporam", "evaporou", "evaporado"],
    # terms defined in the plural, used in the singular
    "isômeros": ["isômero"],
    "isômeros constitucionais": ["isômero constitucional"],
    "estereoisômeros": ["estereoisômero"],
    "diastereoisômeros": ["diastereoisômero"],
    "enantiômeros": ["enantiômero"],
    # adjectives defined in one gender, used in the other
    "exotérmica": ["exotérmico"],
    "endotérmica": ["endotérmico"],
    "anfifílico": ["anfifílica"],
    "quimiosseletiva": ["quimiosseletivo"],
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
    r"Hidratação(?=:)",
    # "grupo" is the periodic-table group only before a number (grupo 1,
    # grupos 13 a 18); "grupo funcional", "grupo alquila", "grupo
    # protetor", "grupo ácido", "grupo de prótons" stay plain. The linkable
    # "grupo ..." terms follow the word, so they are excluded by lookahead.
    r"\b[Gg]rupos?\b(?!\s*~?\d)(?!\s+(?:funciona|alquila|protetor))",
    # "camada" is an electron shell only before its number or as the outer
    # shell; a layer of solvent, of zinc, of sand stays plain.
    r"\b[Cc]amadas?\b(?!\s*~?\d)(?!\s+(?:externa|ocupada|delgada))",
    # "E" is the Z/E isomer only in the stereochemistry sense; as the first
    # word of a sentence it is the conjunction ("E o tempo necessário?"),
    # and the nearest-preceding rule would carry the stereochemistry chapter's
    # link into every later chapter of grade 12.
    r"(?<=[.?!:]\s)E(?=\s+[a-zà-ÿ])",
    # the verb "mistura" (it mixes) shares its spelling with the noun of
    # grade 6: "o etanol se mistura com a água", "mistura ar ao gás"
    r"(?<=\bse\s)mistura\b", r"\bmistura(?=\s+(?:\\omterm\{[^}]*\}\{)?ar\b)",
    # the Daniell cell keeps "cada solução neutra": electrically neutral,
    # not the pH-7 solution of grade 9
    r"(?<=cada\s)solução\s+neutra",
    # a corrosive "queima a pele" (burns the skin), not combustion
    r"queimam?(?=\s+a\s+pele)", r"(?<=pele\sele\s)queima",
    # the honeycomb core of a catalytic converter, not an atomic nucleus
    r"núcleo\s+em\s+colmeia",
    # a spirit burner and a breath test, not the alcohol family
    r"lamparinas?\s+a\s+álcool", r"testes?\s+de\s+álcool",
    # the hydration of an alkene (an addition), not the hydration of ions
    r"hidratação(?=\s+do\s+eteno)",
    # the data key (first argument) of the infrared chapter's \irpanel
    r"\\irpanel\{[^{}]*\}",
    # chemfig settings: "atom sep=1.5em" is a key
    r"\\setchemfig\{[^{}]*\}",
    # key names inside the periodic-table macro's options
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
]

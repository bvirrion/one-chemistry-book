"""Book 4 (University Chemistry, Year 3) -- pt (Brazilian Portuguese). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_pt.py.

Curated by the pt Book 4 agent (2026-10-06) from this edition's own harvest
(`link_defined_terms.py --book 4 --lang pt --terms`: 670 terms harvested,
none defined twice), the per-target frequency census against the English
twin, the chapter-set census, and a reading of every linked context -- not
translated from book4_en.py. AMBIG_POLICY stays "drop", as in English.

A word is linked only once its definition has been met, so a homograph used
before its definition is safe. Homographs met AFTER their definition, each
handled below:

  caráter   -> the character of a representation (ch. 4); the singlet and
               triplet characters mixed by spin-orbit coupling (ch. 7), the odd (u)
               character mixed into d states (ch. 18), the bond-breaking
               character of an interchange (ch. 19), the pi* or d character
               of an orbital (ch. 20) and the s character of a hybrid
               (ch. 29) are masked.
  população -> the Boltzmann population (ch. 10); dense populations of algae
               and a test population (ch. 32) are masked.
  operador  -> the quantum operator (ch. 1); the people who wear goggles at
               a laser or a UV source (ch. 5, 7) and the trained operators of
               a plant (ch. 31 solutions) are masked.
  sol       -> the colloidal sol (ch. 17); the sun ("raios de sol", "luz do
               sol", "ao sol", "Sol, pele") in ch. 17, 26 and their solutions
               is masked.
  migração  -> ionic migration (ch. 15); the migration of a group in a 1,2-
               shift (ch. 27) and one migration of a hydrogen (ch. 26
               solutions) are masked.
  buraco    -> the semiconductor hole (ch. 22); the hole in the middle of a
               porphyrin ring (ch. 24) is masked. (The d-electron "buracos"
               of ch. 18 and the hole of a ferrocene ring in ch. 20 precede
               the definition.)
  indistinguível -> indistinguishable particles (ch. 2); a curve
               "indistinguível da soma" (ch. 10 caption) is masked -- the
               English twin links that occurrence, a wrong-sense link
               reported to the coordinator.

pt-only work: irregular plurals the per-word tail "(?:e?s)?" cannot make
("-ção" -> "-ções", "-al" -> "-ais", "-el" -> "-eis", "-ão" -> "-ões"), each
kept only where the form occurs in this edition; adjectives defined in one
gender and used in the other (conrotatório / conrotatória ...); and the
plural "caracteres" of the group-theory "caráter".
"""

STOP = set()
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {
    # irregular plurals, each present in this edition
    "antarafacial": ["antarafaciais"],
    "suprafacial": ["suprafaciais"],
    "autofunção": ["autofunções", "Autofunções"],
    "caráter": ["caracteres", "Caracteres"],
    "cicloadição": ["cicloadições"],
    "cicloadição 1,3-dipolar": ["cicloadições 1,3-dipolares"],
    "composto sensível ao ar": ["compostos sensíveis ao ar"],
    "constante rotacional": ["constantes rotacionais"],
    "contribuição orbital": ["contribuições orbitais"],
    "defeito pontual": ["defeitos pontuais", "Defeitos pontuais"],
    "eixo helicoidal": ["eixos helicoidais"],
    "emulsão": ["emulsões"],
    "espectro bidimensional": ["espectros bidimensionais"],
    "função de polarização": ["funções de polarização"],
    "função difusa": ["funções difusas"],
    "função de partição molecular": ["funções de partição moleculares"],
    "grupo espacial": ["grupos espaciais"],
    "grupo pontual": ["grupos pontuais", "Grupos pontuais"],
    "integral de troca": ["integrais de troca"],
    "ligação de halogênio": ["ligações de halogênio"],
    "ligação estratégica": ["ligações estratégicas"],
    "matéria-prima renovável": ["matérias-primas renováveis", "Matérias-primas renováveis"],
    "modo normal": ["modos normais"],
    "nanomaterial": ["nanomateriais"],
    "nível aceitador": ["níveis aceitadores"],
    "nível doador": ["níveis doadores"],
    "operação de simetria": ["operações de simetria"],
    "orbital do tipo Slater": ["orbitais do tipo Slater"],
    "pico diagonal": ["picos diagonais"],
    "pião esférico": ["piões esféricos"],
    "pião simétrico": ["piões simétricos"],
    "pião assimétrico": ["piões assimétricos"],
    "plano especular vertical": ["planos especulares verticais"],
    "população": ["populações"],
    "pró-quiral": ["pró-quirais"],
    "razão nefelauxética": ["razões nefelauxéticas"],
    "reação de Mannich": ["reações de Mannich"],
    "reação de acoplamento cruzado": ["reações de acoplamento cruzado"],
    "reação eletrocíclica": ["reações eletrocíclicas"],
    "reação em cadeia": ["reações em cadeia"],
    "reação enantiosseletiva": ["reações enantiosseletivas"],
    "reação oscilante": ["reações oscilantes"],
    "reação pericíclica": ["reações pericíclicas"],
    "representação irredutível": ["representações irredutíveis"],
    "rendimento global": ["rendimentos globais"],
    "entropia residual": ["entropias residuais"],
    "spin-orbital": ["spin-orbitais", "Spin-orbitais"],
    "sol": ["sóis"],
    "tensão superficial": ["tensões superficiais"],
    "lábil": ["lábeis", "Lábeis"],
    # en defines the adjective "isolobal"; the pt definition has the plural
    "isolobais": ["isolobal"],
    # en defines the adjective "indistinguishable"; the pt definition has the plural
    "indistinguíveis": ["indistinguível"],
    # adjectives defined in one gender, used in the other
    "conrotatório": ["conrotatória", "conrotatórias"],
    "disrotatório": ["disrotatória", "disrotatórias"],
    "ativo no IV": ["ativa no IV"],
    "ativo no Raman": ["ativa no Raman"],
}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# Multi-word patterns use \s+ between words: a phrase wrapped across a source
# line break must still be protected. A look-ahead anchored on a word that is
# itself a term must allow an optional wrapper: (?:\\omterm\{[^{}]*\}\{)?
EXTRA_PROTECT = [
    # "indistinguishable" of a symmetry operation (a configuration
    # indistinguishable from the original / from itself, ch. 4): everyday sense,
    # not quantum indistinguishability (coordinator, 2026-10-07, from the hi agent)
    r"indistinguível(?=\s+(?:da\s|de\s+si))",
    # "indistinguível" of an orientation (symmetry number, ch. 10 and sol. 10),
    # not quantum indistinguishability -- as English now protects (coordinator,
    # 2026-10-06)
    r"indistinguíve(?:l|is)(?=\s+da\s+orientação)",
    r"(?<=orientação\s)indistinguível",
    # chemfig settings and arrow labels: \arrow{->[label][label]}
    r"\\setchemfig\{[^{}]*\}",
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # pgfplots tick-label lists (every Book 1-2 edition needed this)
    r"[xy]ticklabels=\{[^{}]*\}",

    # orbital or mechanistic character, not the character of a representation
    r"caráter(?=\s+(?:ímpar|de\s+ruptura|\$|s\b))",
    r"caracteres(?=\s+singleto)",
    # organisms, not Boltzmann populations
    r"populações(?=\s+densas)",
    r"população\s+de\s+teste",
    # people who run an instrument or a plant, not the quantum operator
    r"operadores(?=\s+usam)",
    r"operador(?=\s+trabalha)",
    r"operadores\s+treinados",
    # the sun, not the colloidal sol
    r"(?:[Rr]aios\s+de|luz\s+do|ao)\s+sol\b",
    r"\bSol(?=,\s+pele)",
    # migration of a group or an atom, not ionic migration
    r"migração(?=\s+de\s+um\s+grupo)",
    r"uma\s+migração",
    # the hole of a porphyrin ring, not the semiconductor hole
    r"buraco\s+do\s+anel",
    # a curve indistinguishable from a sum, not indistinguishable particles
    r"indistinguível(?=\s+da\s+soma)",
]

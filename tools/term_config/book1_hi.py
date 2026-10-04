"""Book 1 (School Chemistry, Grades 1-12) -- hi (Hindi). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_hi.py.

Curated by the hi Book 1 agent (2026-10-04) from this edition's own harvest
(`--terms`), an inflection scan of the hi corpus, and a reading of every
flagged term in its Hindi contexts -- not translated from book1_en.py.
AMBIG_POLICY stays "nearest-preceding".

Hindi homographs and drifts found, each handled below:
  * विलयन -- the grade-2 definition is the everyday "solution"; English keeps
    "solution" to its own chapter (STOP), and so does Hindi, so the word is
    not linked from every later page to a grade-2 box. (Hindi has no
    exercise-solution collision -- that one is हल -- but the density
    argument is the same.)
  * मिलाना -- defined as "to mix" in grade 2, but the verb is also "to add"
    (a titrant, a reagent: "मिलाना चाहिए") and "to match" (a note to a pen):
    those three uses are masked below; the infinitive keeps its link in the
    recall boxes that restate the definition. Its finite forms (मिलाने,
    मिलाइए, मिलाया) are nearly all "add" and are not declared.
    The noun "a mix" of grades 2-5 is मिश्रण, which Hindi owns by the
    grade-6 definition (the chemist's mixture); it cannot point at the
    grade-2 box without taking every later मिश्रण with it.
  * सामग्री -- "material" in grade 1, but also "starting material",
    "contents" (प्रारंभिक सामग्री); वस्तु and उत्पाद are everyday words
    after their own chapters, as English rules for object/product.
  * प्रतीक -- the atom's symbol in its own chapter; the symbol of a
    quantity everywhere after ("परमाणु का प्रतीक" keeps its link).
  * धारिता -- the cell's capacity is defined in grade 12 chapter 10, but
    the buffer chapter before it speaks of a buffer's capacity.
  * समूह -- the periodic-table group only before a number (समूह 1, समूह 13
    से 18); "क्रियात्मक समूह", "ऐल्किल समूह", "रक्षी समूह", "अम्ल समूह",
    "समूहों" stay plain or link as their own terms.
  * E, Z -- the bare letters are linked in their own chapter only (the
    chapter-local table, which STOP does not reach), exactly as English links
    them (15 links each side); the protecting group \ce{Z} and the atomic
    number $Z$ are masked as chemistry and mathematics.
  * जलयोजन -- the hydration of ions (grade 11) and, in grade 12 ch. 11, the
    hydration of ethene (an addition): the latter is masked below.
Hindi does not inflect by suffix rules the linker knows (lang_hi.py: no
WORD_TAIL, no DERIVE), so every oblique/plural form the bodies write is
declared in DERIVED, read off the corpus one by one.
"""

STOP = {
    "विलयन", "सामग्री", "वस्तु", "उत्पाद", "प्रतीक", "धारिता",
}
NO_CAPITAL = set()
# "हवा" is the everyday word for air beside वायु; the bodies use both, and
# every हवा in this book is the air (open air, air bubbles, the air of a mill).
EXTRA = {
    "हवा": "def:g4:air-a-mixture-of-gases:air",
}
DROP = set()
DERIVED = {
    # Hindi obliques and plurals, read off THIS edition's corpus (term +
    # ों / एँ / ें / ाएँ / ाओं / ुएँ / ुओं / ियाँ / ियों), each checked as an
    # inflection of the same word -- derivations that are a different word
    # (आयनिक "ionic", एस्टरीकरण "esterification", बहुलकीकरण, अवक्षेपण,
    # निस्यंदन, वर्णलेखन, विलेयता under विलेय, किरैलता, मिश्रणीय under मिश्रण,
    # मोलर under मोल, परमाणवीय, नाभिकीय, जंगल under जंग) are NOT here.
    "अणु": ("अणुओं",),
    "अधातु": ("अधातुएँ", "अधातुओं"),
    "अध्रुवीय अणु": ("अध्रुवीय अणुओं",),
    "अंतिम अवस्था": ("अंतिम अवस्थाएँ",),
    "अपचयोपचय अभिक्रिया": ("अपचयोपचय अभिक्रियाएँ", "अपचयोपचय अभिक्रियाओं"),
    "अपचयोपचय युग्म": ("अपचयोपचय युग्मों",),
    "अप्रतिबिंबरूपी": ("अप्रतिबिंबरूपियों",),
    "अभिकर्मक": ("अभिकर्मकों",),
    "अभिकारक": ("अभिकारकों",),
    "अभिक्रिया क्रियाविधि": ("अभिक्रिया क्रियाविधियाँ", "अभिक्रिया क्रियाविधियों"),
    "अभिलाक्षणिक परीक्षण": ("अभिलाक्षणिक परीक्षणों",),
    "अम्लीय विलयन": ("अम्लीय विलयनों",),
    "अर्ध-आयु": ("अर्ध-आयुओं",),
    "अर्ध-संरचना सूत्र": ("अर्ध-संरचना सूत्रों",),
    "अर्ध-समीकरण": ("अर्ध-समीकरणों",),
    "अवरक्त स्पेक्ट्रम": ("अवरक्त स्पेक्ट्रमों",),
    "अवशोषकता": ("अवशोषकताएँ", "अवशोषकताओं"),
    "अवशोषण स्पेक्ट्रम": ("अवशोषण स्पेक्ट्रमों",),
    "असममित कार्बन": ("असममित कार्बनों",),
    "आंशिक आवेश": ("आंशिक आवेशों",),
    "आण्विक ठोस": ("आण्विक ठोसों",),
    "आण्विक सूत्र": ("आण्विक सूत्रों",),
    "आबंध ऊर्जा": ("आबंध ऊर्जाएँ", "आबंध ऊर्जाओं"),
    "आबंधी युग्म": ("आबंधी युग्मों",),
    "आयन": ("आयनों",),
    "आवर्त": ("आवर्तों",),
    "इलेक्ट्रॉन": ("इलेक्ट्रॉनों",),
    "ईंधन": ("ईंधनों",),
    "उत्कृष्ट गैस": ("उत्कृष्ट गैसों",),
    "उत्प्रेरक": ("उत्प्रेरकों",),
    "ऋणायन": ("ऋणायनों",),
    "धनायन": ("धनायनों",),
    "एंज़ाइम": ("एंज़ाइमों",),
    "एकलक": ("एकलकों",),
    "एकाकी युग्म": ("एकाकी युग्मों",),
    "एस्टर": ("एस्टरों",),
    "ऐमाइड": ("ऐमाइडों",),
    "ऐमीन": ("ऐमीनों",),
    "ऐल्किल समूह": ("ऐल्किल समूहों",),
    "ऐल्केन": ("ऐल्केनों",),
    "ऐल्कोहॉल": ("ऐल्कोहॉलों",),
    "ऐल्डिहाइड": ("ऐल्डिहाइडों",),
    "कीटोन": ("कीटोनों",),
    "कंकाल सूत्र": ("कंकाल सूत्रों",),
    "कार्बनिक यौगिक": ("कार्बनिक यौगिकों",),
    "कार्बोक्सिलिक अम्ल": ("कार्बोक्सिलिक अम्लों",),
    "क्रियात्मक समूह": ("क्रियात्मक समूहों",),
    "क्षार धातु": ("क्षार धातुओं",),
    "क्षारकीय विलयन": ("क्षारकीय विलयनों",),
    "गतिक कारक": ("गतिक कारकों",),
    "ग्रीनहाउस गैस": ("ग्रीनहाउस गैसें", "ग्रीनहाउस गैसों"),
    "घुलता": ("घुलती", "घुलते", "घुलतीं"),
    # "to burn": the intransitive forms mean a fire or a combustion, except a
    # bulb that "जलता है" (lights up), masked in EXTRA_PROTECT; of the
    # transitive forms only those used for burning a fuel are declared --
    # "जलाता/जलाते" also mean a corrosive burning the skin, or lighting a candle.
    "जलना": ("जलने", "जलता", "जलती", "जलते", "जलाने", "जलाया", "जलाई", "जलाए"),
    "घुलना": ("घुलने",),
    "चालकता": ("चालकताओं",),
    "तरंग संख्या": ("तरंग संख्याएँ", "तरंग संख्याओं"),
    "तुल्य प्रोटॉन": ("तुल्य प्रोटॉनों",),
    "त्रिविम समावयवी": ("त्रिविम समावयवियों",),
    "दर्शक आयन": ("दर्शक आयनों",),
    "दुर्बल अम्ल": ("दुर्बल अम्लों",),
    "द्रव्यमान संख्या": ("द्रव्यमान संख्याएँ",),
    "द्रव्यमान सांद्रता": ("द्रव्यमान सांद्रताएँ", "द्रव्यमान सांद्रताओं"),
    "धातु": ("धातुएँ", "धातुओं"),
    "ध्रुवीय अणु": ("ध्रुवीय अणुओं",),
    "ध्रुवीय आबंध": ("ध्रुवीय आबंधों",),
    "नाभिक": ("नाभिकों",),
    "निर्मित सामग्री": ("निर्मित सामग्रियाँ", "निर्मित सामग्रियों"),
    "न्यूक्लिऑन": ("न्यूक्लिऑनों",),
    "न्यूट्रॉन": ("न्यूट्रॉनों",),
    "प्रोटॉन": ("प्रोटॉनों",),
    "परमाणवीय मोलर द्रव्यमान": ("परमाणवीय मोलर द्रव्यमानों",),
    "परमाणु": ("परमाणुओं",),
    "परमाणु मितव्ययिता": ("परमाणु मितव्ययिताएँ", "परमाणु मितव्ययिताओं"),
    "पादांक": ("पादांकों",),
    "पूर्ण अभिक्रिया": ("पूर्ण अभिक्रियाएँ",),
    "प्रगति सारणी": ("प्रगति सारणियाँ",),
    "प्रचुरता": ("प्रचुरताएँ",),
    "प्रतिबिंबरूपी": ("प्रतिबिंबरूपियों",),
    "प्रथम कोटि की अभिक्रिया": ("प्रथम कोटि की अभिक्रियाएँ",),
    "प्राकृतिक सामग्री": ("प्राकृतिक सामग्रियाँ",),
    "प्लास्टिक": ("प्लास्टिकों",),
    "बफ़र विलयन": ("बफ़र विलयनों",),
    "बहुलक": ("बहुलकों",),
    "मानक विलयन": ("मानक विलयनों",),
    "मिश्रण": ("मिश्रणों",),
    "मूल चरण": ("मूल चरणों",),
    "मोलर आयनिक चालकता": ("मोलर आयनिक चालकताओं",),
    "मोलर द्रव्यमान": ("मोलर द्रव्यमानों",),
    "मोलर सांद्रता": ("मोलर सांद्रताएँ",),
    "रक्षी समूह": ("रक्षी समूहों",),
    "रससमीकरणमितीय गुणांक": ("रससमीकरणमितीय गुणांकों",),
    "रासायनिक अभिक्रिया": ("रासायनिक अभिक्रियाएँ", "रासायनिक अभिक्रियाओं"),
    "रासायनिक तत्व": ("रासायनिक तत्वों",),
    "रासायनिक परिवर्तन": ("रासायनिक परिवर्तनों",),
    "लब्धि": ("लब्धियाँ",),
    "लुइस संरचना": ("लुइस संरचनाएँ",),
    "वक्र तीर": ("वक्र तीरों",),
    "वान्डरवाल्स अन्योन्यक्रिया": ("वान्डरवाल्स अन्योन्यक्रियाएँ", "वान्डरवाल्स अन्योन्यक्रियाओं"),
    "विद्युत-ऋणात्मकता": ("विद्युत-ऋणात्मकताएँ", "विद्युत-ऋणात्मकताओं"),
    "विलायक": ("विलायकों",),
    "विलेय": ("विलेयों",),
    "विलेयता": ("विलेयताएँ",),
    "शुद्ध पदार्थ": ("शुद्ध पदार्थों",),
    "संघनन बहुलक": ("संघनन बहुलकों",),
    "संयोजकता इलेक्ट्रॉन": ("संयोजकता इलेक्ट्रॉनों",),
    "संरचना सूत्र": ("संरचना सूत्रों",),
    "संश्लिष्ट सामग्री": ("संश्लिष्ट सामग्रियाँ",),
    "संश्लेषण": ("संश्लेषणों",),
    "संसाधन": ("संसाधनों",),
    "समस्थानिक": ("समस्थानिकों",),
    "समाकलन वक्र": ("समाकलन वक्रों",),
    "समावयवी": ("समावयवियों",),
    "सहसंयोजी आबंध": ("सहसंयोजी आबंधों",),
    "हाइड्रोजन आबंध": ("हाइड्रोजन आबंधों",),
    "हैलोजन": ("हैलोजनों",),
    "NMR स्पेक्ट्रम": ("NMR स्पेक्ट्रमों",),
    "E समावयवी": ("E समावयवियों",),
}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped
# across a source line break must still be protected.
EXTRA_PROTECT = [
    # "समूह" is the periodic-table group only before a number (समूह 1,
    # समूह 13 से 18); a group of atoms, an acid group, a methyl group stay
    # plain. The linkable "... समूह" terms are excluded by lookbehinds.
    r"(?<!क्रियात्मक )(?<!ऐल्किल )(?<!रक्षी )(?<!क्रियात्मक\n)(?<!ऐल्किल\n)(?<!रक्षी\n)समूह(?![\u0900-\u0963\u0966-\u097f])(?!\s*~?\d)",
    # ... and inside the definition of "क्रियात्मक समूह" itself, where the
    # linker skips the self-link and would fall back to the bare "समूह" (the
    # periodic-table sense): the head noun is masked there.
    r"(?<=एक ही क्रियात्मक )समूह(?=\s+वाले)",
    # the hydration of ethene (an addition), not the hydration of ions: the
    # exercise stem and its solution's head "जलयोजन:" (grade 12, ch. 11)
    r"(?<=एथीन के )जलयोजन", r"जलयोजन(?=:)",
    # a bulb that "जलता है" lights up; it does not burn
    r"(?<=बल्ब )जलता", r"(?<=विलयनों के साथ )जलता",
    # मिलाना = "to add" or "to match", not the grade-2 "to mix"
    r"मिलाना(?=\s+(?:चाहिए|या\s+कोई|है।))",
    # pgfplots tick labels are code
    r"[xy]ticklabels=\{[^{}]*\}",
    # the data key (first argument) of the infrared chapter's \irpanel
    r"\\irpanel\{[^{}]*\}",
    # chemfig settings: "atom sep=1.5em" is a key, not a word
    r"\\setchemfig\{[^{}]*\}",
    # key names inside the periodic-table macro's options
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # the key of \polymerdelim
    r"\\polymerdelim\[[^\]]*\]",
]

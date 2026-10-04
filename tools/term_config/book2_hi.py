"""Book 2 (University Year 1) -- hi (Hindi). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_hi.py.

Curated by the hi Book 2 agent (2026-10-04) from this edition's own harvest
(`--terms`: 376 linkable terms, the same 169 targets as English), an
inflection scan of the hi corpus (every term + ों / एँ / ें / ाएँ / ाओं /
ियाँ / ियों, and का -> के inside a term), and a per-target census against
the English links -- not translated from book2_en.py.

Hindi homographs and drifts found, each handled below:
  * प्रबल / दुर्बल -- the bare adjectives are harvested from the strong/weak
    acid definition but also say "a strong bond", "weak interactions", "a
    strong oxidant": STOP, as English stops strong/weak; "प्रबल अम्ल",
    "दुर्बल क्षारक" ... keep their links.
  * समूह -- the periodic-table group only before a number (समूह 1, समूह 13
    से 15); a methyl group, the OH group, the C=O group stay plain. The four
    linkable "... समूह" terms (निर्गामी, रक्षी, दाता, ग्राही) are let through
    by the look-behinds. Its plural is not declared: "समूहों" is never the
    periodic-table sense here.
  * आवर्त -- the period, but also the first word of "आवर्त सारणी" (the
    periodic table), which English ("periodic") never links.
  * उभयधर्मी -- the ampholyte of ch. 10, but Hindi also says उभयधर्मी for
    "amphoteric" (a hydroxide, an oxide, water as a hydride), which English
    keeps apart (ampholyte / amphoteric): those uses are masked; the terms
    "उभयधर्मी हाइड्रॉक्साइड" and "उभयधर्मी ऑक्साइड" keep their own targets.
  * इलेक्ट्रॉन-न्यून -- defined (ch. 3) for the electron-deficient molecule;
    Hindi uses the same word for English "electron-poor" (a carbocation, a
    carbon partner, a reagent), which English does not link.
  * आवरण -- screening (ch. 2); also the solvent screening ion charges
    (ch. 4), the coverage factor (आवरण गुणक), a condenser jacket and the
    heating mantle (ch. 29).
  * बहुकता -- the multiplicity of a cell (ch. 5); the NMR multiplicity of
    ch. 17 is masked, as in English.
  * सक्रियता -- thermodynamic activity; "सक्रियता की हानि" (ch. 19) is the
    optical activity lost, as English masks "loss of activity".
  * अक्षीय / विषुवतीय -- cyclohexane bonds; "... स्थिति(याँ)" are the
    VSEPR positions of a trigonal bipyramid (ch. 28) or a position on a
    ring, masked as English masks "axial/equatorial positions".
  * जलयोजन -- the hydration of an alkene (ch. 25); the hydration energy of
    the halide ions (ch. 28) is masked, as English masks it.
  * स्वास्थ्य संकट -- the GHS08 pictogram's name and the H3xx class, not
    the defined hazard, as English masks "health hazard".
  * ऑक्सीकारक -- the oxidant; as the caption word of the GHS03 pictogram
    ("oxidising") it is a hazard class, masked.
  * विद्युत-ऋणात्मकता -- the hyphenated spelling of Book 1 is the only one
    in the bodies (the run normalised a drift before linking).
EXTRA maps the one Hindi phrasing that cannot carry the term's own words:
"लोप की दर" is the "rate of disappearance" of ch. 19, defined as लोप दर.
"""

STOP = {
    "प्रबल", "दुर्बल",
}
NO_CAPITAL = set()
EXTRA = {
    "लोप की दर": "def:b1:rate-laws:rate",
}
DROP = set()
DERIVED = {
    # Hindi obliques and plurals, read off THIS edition's corpus, each checked
    # as an inflection of the same word.
    "$\\pi$ आबंध": ("$\\pi$ आबंधों",),
    "$\\sigma$ आबंध": ("$\\sigma$ आबंधों",),
    "CIP नियम": ("CIP नियमों",),
    "अंतराकाशी स्थल": ("अंतराकाशी स्थलों",),
    "अंतस्थ ऐल्काइन": ("अंतस्थ ऐल्काइनों",),
    "अनुनादी संरचना": ("अनुनादी संरचनाएँ", "अनुनादी संरचनाओं"),
    "अनुमापन": ("अनुमापनों",),
    "अपचायक": ("अपचायकों",),
    "अभिक्रिया क्रियाविधि": ("अभिक्रिया क्रियाविधियाँ", "अभिक्रिया क्रियाविधियों"),
    "अभिक्रिया दर": ("अभिक्रिया दरों",),
    "अम्लता स्थिरांक": ("अम्लता स्थिरांकों",),
    "अम्लीय ऑक्साइड": ("अम्लीय ऑक्साइडों",),
    "अयुग्मित इलेक्ट्रॉन": ("अयुग्मित इलेक्ट्रॉनों",),
    "अर्ध-आयु": ("अर्ध-आयुओं",),
    "अर्ध-समीकरण": ("अर्ध-समीकरणों",),
    "अर्ध-सेल": ("अर्ध-सेलों",),
    "अवशोषकता": ("अवशोषकताएँ",),
    "अष्टफलकीय स्थल": ("अष्टफलकीय स्थलों",),
    "आंशिक कोटि": ("आंशिक कोटियाँ",),
    "आंशिक दाब": ("आंशिक दाबों",),
    "आण्विक क्रिस्टल": ("आण्विक क्रिस्टलों",),
    "आपेक्षिक अनिश्चितता": ("आपेक्षिक अनिश्चितताएँ",),
    "आबंध द्विध्रुव": ("आबंध द्विध्रुवों",),
    "आबंधी युग्म": ("आबंधी युग्मों",),
    "आयनिक क्रिस्टल": ("आयनिक क्रिस्टलों",),
    "आयनिक त्रिज्या": ("आयनिक त्रिज्याएँ", "आयनिक त्रिज्याओं"),
    "आवर्त": ("आवर्तों",),
    "आवास-क्षमता": ("आवास-क्षमताएँ",),
    "इलेक्ट्रॉन बंधुता": ("इलेक्ट्रॉन बंधुताएँ",),
    "इलेक्ट्रॉनरागी": ("इलेक्ट्रॉनरागियों",),
    "उपकोश": ("उपकोशों",),
    "उपधातु": ("उपधातुएँ",),
    "उपसहसंयोजन संख्या": ("उपसहसंयोजन संख्याएँ",),
    "उपसहसंयोजी आबंध": ("उपसहसंयोजी आबंधों",),
    "ऊर्जा प्रोफ़ाइल": ("ऊर्जा प्रोफ़ाइलों",),
    "ऊर्जा स्तर": ("ऊर्जा स्तरों",),
    "एकाकी युग्म": ("एकाकी युग्मों",),
    "ऐसीटैल": ("ऐसीटैलों",),
    "ऑक्सीकरण संख्या": ("ऑक्सीकरण संख्याएँ", "ऑक्सीकरण संख्याओं"),
    "ऑक्सीकारक": ("ऑक्सीकारकों",),
    "ऑक्सोअम्ल": ("ऑक्सोअम्लों",),
    "औपचारिक आवेश": ("औपचारिक आवेशों",),
    "कार्बऋणायन": ("कार्बऋणायनों",),
    "कार्बधनायन": ("कार्बधनायनों",),
    "कुर्सी": ("कुर्सियाँ", "कुर्सियों"),
    "क्रमिक अनुमापन": ("क्रमिक अनुमापनों",),
    "क्रियाधार": ("क्रियाधारों",),
    "क्रियाशील मध्यवर्ती": ("क्रियाशील मध्यवर्तियों",),
    "क्रिस्टल": ("क्रिस्टलों",),
    "क्रोड इलेक्ट्रॉन": ("क्रोड इलेक्ट्रॉनों",),
    "क्षार धातु": ("क्षार धातुएँ", "क्षार धातुओं"),
    "क्षारीय मृदा धातु": ("क्षारीय मृदा धातुएँ", "क्षारीय मृदा धातुओं"),
    "ग्राही समूह": ("ग्राही समूहों",),
    "ग्रीन्यार अभिकर्मक": ("ग्रीन्यार अभिकर्मकों",),
    "चतुष्फलकीय स्थल": ("चतुष्फलकीय स्थलों",),
    "जल का आयनिक गुणनफल": ("जल के आयनिक गुणनफल",),
    "जल का स्थायित्व क्षेत्र": ("जल के स्थायित्व क्षेत्र",),
    "ज़ैत्सेव का नियम": ("ज़ैत्सेव के नियम",),
    "तरंग संख्या": ("तरंग संख्याओं",),
    "तुल्य प्रोटॉन": ("तुल्य प्रोटॉनों",),
    "तुल्यता": ("तुल्यताएँ", "तुल्यताओं"),
    "त्रिविम समावयवी": ("त्रिविम समावयवियों",),
    "त्रिविमजनक केंद्र": ("त्रिविमजनक केंद्रों",),
    "त्रिविमवरणात्मक अभिक्रिया": ("त्रिविमवरणात्मक अभिक्रियाएँ",),
    "दर नियम": ("दर नियमों",),
    "दर स्थिरांक": ("दर स्थिरांकों",),
    "दुर्बल अम्ल": ("दुर्बल अम्लों",),
    "द्विध्रुव आघूर्ण": ("द्विध्रुव आघूर्णों",),
    "ध्रुवणीयता": ("ध्रुवणीयताओं",),
    "ध्रुवीय अणु": ("ध्रुवीय अणुओं",),
    "ध्रुवीय विलायक": ("ध्रुवीय विलायकों",),
    "नाभिकरागी": ("नाभिकरागियों",),
    "न्यूमैन प्रक्षेप": ("न्यूमैन प्रक्षेपों",),
    "पूर्व-घातांकी गुणक": ("पूर्व-घातांकी गुणकों",),
    "पॉलिंग पैमाना": ("पॉलिंग पैमाने",),
    "प्रतिबिंबरूपी": ("प्रतिबिंबरूपियों",),
    "प्रथम आयनन ऊर्जा": ("प्रथम आयनन ऊर्जाएँ",),
    "प्रबल अम्ल": ("प्रबल अम्लों",),
    "प्रारंभिक दर": ("प्रारंभिक दरों",),
    "प्रावस्था": ("प्रावस्थाएँ",),
    "प्रोटिक विलायक": ("प्रोटिक विलायकों",),
    "बफ़र विलयन": ("बफ़र विलयनों",),
    "बहुक": ("बहुकों",),
    "ब्रॉन्स्टेड अम्ल": ("ब्रॉन्स्टेड अम्लों",),
    "ब्लॉक": ("ब्लॉकों",),
    "मानक अनिश्चितता": ("मानक अनिश्चितताएँ",),
    "मानक विभव": ("मानक विभवों",),
    "मुलिकेन पैमाना": ("मुलिकेन पैमाने",),
    "मूल चरण": ("मूल चरणों",),
    "मोटिफ़": ("मोटिफ़ों",),
    "युग्मन स्थिरांक": ("युग्मन स्थिरांकों",),
    "रससमीकरणमितीय संख्या": ("रससमीकरणमितीय संख्याएँ",),
    "लंदन अन्योन्यक्रिया": ("लंदन अन्योन्यक्रियाएँ", "लंदन अन्योन्यक्रियाओं"),
    "लिगैंड": ("लिगैंडों",),
    "लुइस क्षारक": ("लुइस क्षारकों",),
    "लुइस संरचना": ("लुइस संरचनाएँ", "लुइस संरचनाओं"),
    "लोप दर": ("लोप दरें",),
    "वक्र तीर": ("वक्र तीरों",),
    "वान्डरवाल्स अन्योन्यक्रिया": ("वान्डरवाल्स अन्योन्यक्रियाएँ", "वान्डरवाल्स अन्योन्यक्रियाओं"),
    "विद्युत-ऋणात्मकता": ("विद्युत-ऋणात्मकताएँ", "विद्युत-ऋणात्मकताओं"),
    "विन्यास": ("विन्यासों",),
    "वियोजन स्थिरांक": ("वियोजन स्थिरांकों",),
    "विलेयता": ("विलेयताएँ",),
    "विलेयता गुणनफल": ("विलेयता गुणनफलों",),
    "विस्तारित अनिश्चितता": ("विस्तारित अनिश्चितताएँ",),
    "विस्तीर्ण चर": ("विस्तीर्ण चरों",),
    "संकट": ("संकटों",),
    "संकुल": ("संकुलों",),
    "संक्रमण अवस्था": ("संक्रमण अवस्थाएँ", "संक्रमण अवस्थाओं"),
    "संयोजकता इलेक्ट्रॉन": ("संयोजकता इलेक्ट्रॉनों",),
    "संरूपण": ("संरूपणों",),
    "संहतता": ("संहतताओं",),
    "सक्रियण ऊर्जा": ("सक्रियण ऊर्जाओं",),
    "सक्रियता": ("सक्रियताएँ", "सक्रियताओं"),
    "समग्र कोटि": ("समग्र कोटियों",),
    "समाकलन": ("समाकलनों",),
    "सहसंयोजी आबंध": ("सहसंयोजी आबंधों",),
    "सहसंयोजी त्रिज्या": ("सहसंयोजी त्रिज्याएँ",),
    "सांतरित संरूपण": ("सांतरित संरूपणों",),
    "सावधानी कथन": ("सावधानी कथनों",),
    "सुरक्षा आँकड़ा पत्रक": ("सुरक्षा आँकड़ा पत्रकों",),
    "हाइड्राइड": ("हाइड्राइडों",),
    "हाइड्रोजन आबंध": ("हाइड्रोजन आबंधों",),
    "हैलोजन": ("हैलोजनों",),
}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across
# a source line break must still be protected.
EXTRA_PROTECT = [
    # Coordinator, 2026-10-04: the zinc anode blocks of ch. 14 are not the
    # periodic-table block (and ch. 13/15 adjectival quantitative is not
    # the quantitative reaction); English now protects the same sites.
    r"(?<=ज़िंक के\s)ब्लॉक",
    r"(?<=ज़िंक का\s)ब्लॉक",
    r"(?<=धूसर\s)ब्लॉक",
    r"(?<=विनिमय को\s)मात्रात्मक",
    r"मात्रात्मक(?=\s+मापन)",

    # "समूह" is the periodic-table group only before a number; the four
    # linkable "... समूह" terms are let through by the look-behinds.
    r"(?<!निर्गामी )(?<!रक्षी )(?<!दाता )(?<!ग्राही )"
    r"(?<!निर्गामी\n)(?<!रक्षी\n)(?<!दाता\n)(?<!ग्राही\n)"
    r"समूह(?![\u0900-\u0963\u0966-\u097f])(?!\s*~?\d)",
    # the periodic TABLE, not the period
    r"आवर्त(?=\s+सारणी)",
    # "amphoteric" (a hydroxide, an oxide, water among the hydrides), not
    # the ampholyte of ch. 10
    r"उभयधर्मी(?=\s+(?:पुनर्विलयन|नहीं|के\s+रूप\s+में\s+वर्गीकृत))",
    r"(?<=एक )उभयधर्मी(?=,\s+दूसरा)",
    r"(?<=\\ce\{H2O\} )उभयधर्मी",
    r"उभयधर्मी(?=:\s+\\ce\{Al2O3)",
    # "electron-poor" (a carbocation's carbon, a bond partner, a reagent)
    r"इलेक्ट्रॉन-न्यून(?=\s+(?:कार्बन|भागीदार|अभिकर्मक))",
    # screening by a solvent (ch. 4), the coverage factor, a condenser
    # jacket, the heating mantle (ch. 29)
    r"(?<=उनका )आवरण(?=\s+करते)",
    r"आवरण(?=\s+गुणक)",
    r"आवरण(?=\s+भरा)",
    r"(?<=तापन )आवरण",
    # the NMR multiplicity (ch. 17), not the multiplicity of a cell
    r"बहुकता(?=\s+\(पड़ोसियों)",
    r"(?<=संकेत की )बहुकता",
    r"(?<=विस्थापन, )बहुकता",
    # optical activity lost (ch. 19), not the thermodynamic activity
    r"सक्रियता(?=\s+की\s+हानि)",
    # VSEPR positions, or a position on a ring, not cyclohexane bonds
    r"(?:अक्षीय|विषुवतीय)(?=\s+स्थिति)",
    # hydration energy of the halide ions (ch. 28), not of an alkene
    r"जलयोजन(?=-ऊर्जा)",
    # the GHS08 pictogram's name and the H3xx class
    r"स्वास्थ्य\s+संकट",
    # the GHS03 pictogram's caption word ("oxidising")
    r"(?<=\\footnotesize )ऑक्सीकारक",
    # a sealed distillation apparatus (ch. 29 safety box), not the
    # thermodynamic closed system of ch. 7
    r"बंद\s+निकाय(?=\s+फट)",
    # pgfplots tick labels are code
    r"[xy]ticklabels=\{[^{}]*\}",
    # key names inside the periodic-table macro's options
    r"\\omperiodictable\[[^\]]*\]",
    # chemfig arrow labels: \arrow{->[label][label]}
    r"\\arrow\{(?:[^{}]|\{[^{}]*\})*\}",
    # chemfig settings
    r"\\setchemfig\{[^{}]*\}",
]

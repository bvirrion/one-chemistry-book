"""Book 3 (University Chemistry, Year 2) -- hi (Hindi). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_hi.py.

Curated by the hi Book 3 agent (2026-10-06) from this edition's own harvest
(`--terms`: 413 harvested, 423 linkable), an inflection scan of the hi corpus
(every term + ों / ें / एँ / ाएँ / ाओं / ियाँ / ियों, and का -> के inside a
term), and a per-target and per-chapter census against the English links --
not translated from book3_en.py.

A term is linked only once its definition has been met, so a word defined
late in one sense is safe earlier. Hindi homographs found AFTER their
definition, each handled below:
  * निष्कासन -- the purge of a recycle loop (ch. 4); Hindi uses the same
    word for the removal of a proton or a hydrogen (ch. 22, 25), the removal
    of a protecting group (ch. 30) and the heat-removal line of a CSTR
    (ch. 5), which English calls removal and never links.
  * संचरण -- chain propagation (ch. 29); the propagation of uncertainty
    (ch. 34) is masked, as English masks "propagation of uncertainty".
  * आरंभन -- radical initiation (ch. 29); the initiation of a Grignard
    formation (ch. 35) is masked, as in English.
  * वरणात्मकता -- a reactor's selectivity (ch. 5); the chromatographic
    selectivity lever of ch. 31 is masked, as in English.
  * विभेदन -- the chromatographic resolution (ch. 31); "विभेदन क्षमता"
    (resolving power, ch. 32) and the spectral resolution of ch. 33 are
    masked, as English masks spectral resolution.
  * रूपांतरण -- a reactor's conversion (ch. 5); the eutectic transformation
    of a cooling curve (ch. 8, "गलनक्रांतिक रूपांतरण") is masked.
  * कक्षक ऊर्जा -- an orbital energy (ch. 13); ch. 17's "कक्षक ऊर्जा में
    दूर" is "the orbitals are far apart in energy", subject and noun side by
    side, masked.
  * स्वातंत्र्य कोटि -- the variance of a system (ch. 4); its plural is NOT
    declared, because "स्वातंत्र्य कोटियाँ/कोटियों" in ch. 34 are the
    statistical degrees of freedom, which English never links.
"""

STOP = set()
NO_CAPITAL = set()
EXTRA = {
    # the bare noun of the "Enolates" definition (only "ion" phrase harvested;
    # coordinator, 2026-10-07, as English and Arabic)
    "ईनोलेट": "def:b2:enolates-aldol:enolate",
}
DROP = set()
DERIVED = {
    # Hindi obliques and plurals, read off THIS edition's corpus, each checked
    # as an inflection of the same word in the same sense.
    "$\\alpha$ कार्बन": ("$\\alpha$ कार्बनों",),
    "$\\alpha$ हाइड्रोजन": ("$\\alpha$ हाइड्रोजनों",),
    "$\\pi$ कक्षक": ("$\\pi$ कक्षकों",),
    "$\\pi$-ग्राही लिगैंड": ("$\\pi$-ग्राही लिगैंडों",),
    "अग्रांत कक्षक": ("अग्रांत कक्षकों",),
    "अणुखंड": ("अणुखंडों",),
    "अणुखंड कक्षक": ("अणुखंड कक्षकों",),
    "अधिविभव": ("अधिविभवों",),
    "अनाबंधी कक्षक": ("अनाबंधी कक्षकों",),
    "अभिक्रिया एन्ट्रॉपी": ("अभिक्रिया एन्ट्रॉपियाँ",),
    "अभिक्रिया एन्थैल्पी": ("अभिक्रिया एन्थैल्पियों", "अभिक्रिया एन्थैल्पियाँ"),
    "अभिक्रिया राशि": ("अभिक्रिया राशियाँ",),
    "अभिनति": ("अभिनतियाँ",),
    "अवशिष्ट": ("अवशिष्टों",),
    "आंशिक मोलर आयतन": ("आंशिक मोलर आयतनों",),
    "आंशिक मोलर राशि": ("आंशिक मोलर राशियाँ",),
    "आण्विक कक्षक": ("आण्विक कक्षकों",),
    "आबंध कोटि": ("आबंध कोटियाँ", "आबंध कोटियों"),
    "आबंधी कक्षक": ("आबंधी कक्षकों",),
    "उत्प्रेरकी चक्र": ("उत्प्रेरकी चक्रों",),
    "एकलक": ("एकलकों",),
    "एपॉक्साइड": ("एपॉक्साइडों",),
    "ऐनोमर": ("ऐनोमरों",),
    "ऐनोमरी कार्बन": ("ऐनोमरी कार्बनों",),
    "ऐसिल क्लोराइड": ("ऐसिल क्लोराइडों",),
    "कार्बोक्सिलिक अम्ल व्युत्पन्न": ("कार्बोक्सिलिक अम्ल व्युत्पन्नों",),
    "किरखॉफ़ का नियम": ("किरखॉफ़ के नियम",),
    "कोणीय नोड": ("कोणीय नोडों",),
    "ग्लाइकोसाइडी आबंध": ("ग्लाइकोसाइडी आबंधों",),
    "जालक एन्थैल्पी": ("जालक एन्थैल्पियाँ",),
    "ट्राइग्लिसराइड": ("ट्राइग्लिसराइडों",),
    "ठोस विलयन": ("ठोस विलयनों",),
    "डाइऐज़ोनियम आयन": ("डाइऐज़ोनियम आयनों",),
    "डाईन": ("डाईनों",),
    "तुल्य कार्बन": ("तुल्य कार्बनों",),
    "तृतीयक ऐमीन": ("तृतीयक ऐमीनों",),
    "त्रिज्य नोड": ("त्रिज्य नोडों",),
    "द्विदंतुर लिगैंड": ("द्विदंतुर लिगैंडों",),
    "धारा--विभव वक्र": ("धारा--विभव वक्रों",),
    "नाइट्राइल": ("नाइट्राइलों",),
    "पेप्टाइड आबंध": ("पेप्टाइड आबंधों",),
    "प्रतिआबंधी कक्षक": ("प्रतिआबंधी कक्षकों",),
    "प्रतिधारण काल": ("प्रतिधारण कालों",),
    "फ़ॉस्फ़ोडाइएस्टर आबंध": ("फ़ॉस्फ़ोडाइएस्टर आबंधों",),
    "बलिदानी ऐनोड": ("बलिदानी ऐनोडों",),
    "बहुलक": ("बहुलकों",),
    "मानक अभिक्रिया एन्थैल्पी": ("मानक अभिक्रिया एन्थैल्पियाँ",),
    "मानक मोलर एन्ट्रॉपी": ("मानक मोलर एन्ट्रॉपियाँ",),
    "मानक संभवन एन्थैल्पी": ("मानक संभवन एन्थैल्पियों",),
    "राउल्ट का नियम": ("राउल्ट के नियम",),
    "रासायनिक विभव": ("रासायनिक विभवों",),
    "रूपांतरण": ("रूपांतरणों",),
    "लांबिक रक्षी समूह": ("लांबिक रक्षी समूहों",),
    "ले शातेलिए का सिद्धांत": ("ले शातेलिए के सिद्धांत",),
    "वसा अम्ल": ("वसा अम्लों",),
    "विद्युत-अपघटन": ("विद्युत-अपघटनों",),
    "विभेदन": ("विभेदनों",),
    "विलायक भित्ति": ("विलायक भित्तियाँ",),
    "व्हीलैंड मध्यवर्ती": ("व्हीलैंड मध्यवर्तियों",),
    "शीतलन वक्र": ("शीतलन वक्रों",),
    "सतत रिएक्टर": ("सतत रिएक्टरों",),
    "साम्य का विस्थापन": ("साम्य के विस्थापन",),
    "सिंथॉन": ("सिंथॉनों",),
    "सैद्धांतिक प्लेट": ("सैद्धांतिक प्लेटों",),
    "स्थायीकृत इलाइड": ("स्थायीकृत इलाइडों",),
    "स्लेटर के नियम": ("स्लेटर के नियमों",),
    "हेनरी का नियम": ("हेनरी के नियम",),
}
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

    # removal of a proton / hydrogen / protecting group (ch. 22, 25, 30) and
    # the heat-removal line of a CSTR (ch. 5), not the purge of ch. 4
    r"(?<=का )निष्कासन",
    r"(?<=का\n)निष्कासन",
    r"उसका\s+निष्कासन",
    r"निष्कासन(?=\s+(?:एक\s+सरल|रेखा|से\s+आगे))",
    # propagation of uncertainty (ch. 34), not chain propagation (ch. 29)
    r"(?<=का )संचरण",
    r"(?<=का\n)संचरण",
    r"संचरण(?=\s+नियम)",
    # initiation of a Grignard formation (ch. 35), not radical initiation
    r"आरंभन(?=\s+(?:से\s+पहले|की\s+विफलता))",
    # chromatographic selectivity (ch. 31), not a reactor's selectivity
    r"वरणात्मकता(?=:\s+गुणक)",
    r"(?<=उत्तोलक: )वरणात्मकता",
    # resolving power (ch. 32) and spectral resolution (ch. 33), not the
    # chromatographic resolution of ch. 31
    r"विभेदन(?=\s+क्षमता)",
    r"विभेदन(?=\s+से\s+अधिक\s+निकट)",
    # the eutectic transformation of a cooling curve (ch. 8)
    r"(?<=गलनक्रांतिक )रूपांतरण",
    # "the orbitals are far apart in energy" (ch. 17)
    r"कक्षक\s+ऊर्जा(?=\s+में\s+दूर)",
]

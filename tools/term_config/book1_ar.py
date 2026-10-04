"""Book 1 (School Chemistry, Grades 1-12) -- ar (Arabic). Curation only; the rules live in
tools/termlink/ and the language morphology in tools/term_config/lang_ar.py.

Curated by the ar Book 1 agent (2026-10-04) from this edition's own harvest
(`--terms`) and the frequency and chapter-set censuses against the English
twin -- not translated from book1_en.py. AMBIG_POLICY stays
"nearest-preceding".

Arabic homographs found by the censuses, each handled below: مادة (a
material in grade 1 / matter, substance everywhere after), جسم (an object /
"جسم صلب", a solid / the human body), إضافة (the reaction category / the
ordinary noun "adding"), ترسيب (settling a mixture in grade 3 /
precipitation from grade 9), طبقة (an electron shell / any layer: oil,
oxide, the thin layer of TLC), تفكك (dissociation of an ionic solid /
decomposition), إماهة (hydration of ions / hydration of ethene), معايرة
(a titration / calibrating a pH meter), كاشف (a reagent / an indicator),
رمز (an atom's symbol / any symbol), and the bare letters E and Z.
"""

STOP = {
    # "مادة" is defined in grade 1 as a material ("this cup is made of
    # glass"), and is the word for matter and substance everywhere after
    # ("كمية المادة", "مادة نقية" keep their own multi-word links).
    "مادة", "المادة",
    # "جسم" is the grade-1 object; from grade 6 on it is almost always
    # "جسم صلب" (a solid) or the human body.
    "جسم", "الجسم",
    # the atom's symbol in its own chapter; any other symbol after.
    # "رمز الذرة" keeps its link.
    "رمز",
}
NO_CAPITAL = set()
# Arabic forms most plurals by internal change (broken plurals), which no
# tail rule reaches (lang_ar.py: WORD_TAIL is empty, DERIVE off). The plurals
# this book uses for its most frequent terms are declared here, each pointing
# at the target its singular already reaches; the article and the one-letter
# prefixes are added by HEAD.
EXTRA = {
    "ذرات": "def:g7:atoms-and-molecules:atom",
    "جزيئات": "def:g7:atoms-and-molecules:molecule",
    "أيونات": "def:g9:ions:ion",
    "إلكترونات": "def:g9:inside-the-atom:nucleus",
    "بروتونات": "def:g9:inside-the-atom:proton",
    "نيوترونات": "def:g9:inside-the-atom:proton",
    "فلزات": "def:g9:periodic-table-first-look:metal",
    "إسترات": "def:g11:functional-groups:carboxylic-acid",
    "كحولات": "def:g11:functional-groups:alcohol",
    "بوليمرات": "def:g12:polymers:polymer",
}
DROP = {
    # bare capital letters of the Z/E definition: "متماكب Z" and "متماكب E"
    # keep the target; a lone letter (E133, compound E, spectrum E) is not a
    # term. STOP would fall through to the chapter-local map.
    "E", "Z",
    # the ordinary noun "adding" ("بعد كل إضافة من المحلول المعايِر") swamps
    # the reaction category; "بوليمر إضافة" keeps its own link and the
    # category keeps الاستبدال and الحذف.
    "إضافة", "الإضافة",
    # settling (grade 3) is also reached by الترويق/ترويق; bare ترسيب is
    # precipitation from grade 9 on.
    "ترسيب", "الترسيب",
}
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped
# across a source line break must still be protected.
EXTRA_PROTECT = [
    # Coordinator, 2026-10-04: g12 solutions/11 exo 1 head is the hydration
    # of ETHENE (an addition), not the hydration of ions; same in the
    # exercise statement.
    r"إماهة(?=\s+الإيثين)",
    # calibrating a pH meter is not a titration
    r"معايرة(?=\s+(?:\\omterm\{[^{}]*\}\{)?مقياس)",
    r"(?<=سيئ\s)المعايرة",
    # "ماصة معايرة", "حوجلة معايرة": calibrated (volumetric) glassware
    r"(?<=ماصة\s)معايرة",
    r"(?<=حوجلة\s)معايرة",
    # "طبقة" is an electron shell from grade 10, but also any layer: the
    # liquid layers of an extraction, a sheet of ice, a spongy deposit, a
    # thin catalyst coat.
    r"طبق(?:ة|ات)(?=\s+(?:الهكسان|منفصلة|رقيقة|ثانية|تُصرَّف|الجليد|إسفنجية))",
    r"الطبقة(?=\s+(?:السفلى|العليا))",
    # "مردود التسخين": the efficiency of a heating, not a synthesis yield
    r"مردود(?=\s+التسخين)",
    r"المردود(?=\s+\$20\.9)",
    # "الخام" after crude oil / a crude solid: not the grade-5 ore
    r"(?<=النفط\s)الخام",
    r"(?<=الصلب\s)الخام",
    # the product of a multiplication (grade-10 mole chapter)
    r"الناتج(?=؟)",
    # "الكاشف الضوئي" is a photodetector; and in titration chapters the bare
    # "كاشف" is the indicator, defined only in grade 12, never the reagent
    r"الكاشف(?=\s+الضوئي)",
    r"(?<=حاجة\sإلى\s)كاشف",
    r"(?<=يتغير\sلون\s)الكاشف",
    r"(?<=يوجد\s)كاشف(?=\s+مناسب)",
    # an ionic solution is electrically neutral: not a pH-neutral solution
    r"محلول\s+متعادل(?=:\s*\$2)",
    # "لا يكون له نظير": it has no counterpart, not an isotope
    r"(?<=له\s)نظير",
    # a limestone statue weathered by rain: not the corrosion of a metal
    r"تآكل(?=\s+بفعل)",
    # "تفكك" is the dissociation of an ionic solid only in grade 11/03; the
    # decomposition of limestone, of hydrogen peroxide and radioactive decay
    # are not.
    r"تفكك(?=\s+(?:الحجر|بيروكسيد))",
    r"التفكك(?=\s+(?:الإشعاعي|البطيء))",
    r"(?<=هذا\s)التفكك",
    r"(?<=---\s)التفكك",
    r"(?<=هو\s)التفكك",
    r"(?<=الذي\s)تفكك",
    # hazard statements: "flammable" is not the burning of the fire chapter
    r"للاشتعال",
]

"""Book 2 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-4_ZH.md) before the translation existed, from the
English and French configs' choices; refined at the book's close against the link census (pilot_translation/census.py).
Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han text, so a word that is also part of a common
compound or an everyday verb must be stopped or dropped here. One-character terms are never linked.
"""

# result names are never terms (the French NOT_A_TERM, in Chinese)
NOT_A_TERM = ("定理", "引理", "不等式", "公式", "判据", "准则", "原理", "恒等式", "法则", "定律", "悖论", "问题")

STOP = {
    # homographs linked only in their defining chapter (calibrated at the book's close, 2026-11-18):
    # 屏蔽 is both the electron screening (ch. 2) and the NMR shielding (ch. 17), and steric shielding in ch. 19;
    # 保护 is also the everyday "protect"; 水合 also the hydrated ions of ch. 26/28; 积分 also a calculus integral;
    # 基元 (the crystal motif) also sits in 基元反应
    "屏蔽", "保护", "水合", "积分", "基元",
}
DROP = set()
INDEX_CJK = True    # index-only keys are terms too (harvest.py, physics zh Book 3)
EXTRA = {}          # manual {term: label}, added at the book's close (index-only keys have no space in Chinese)
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = [
    # 构型 is the R/S configuration (stereochemistry) but also a molecule's geometry (几何构型, VSEPR's 构型) and an
    # electron configuration (电子构型, "构型为 ns2np4"): those senses must not link to the isomers definition
    r"电子构型", r"几何构型", r"(?<=所得的)构型", r"(?<=，)构型(?=为\s*\\textit)",
]

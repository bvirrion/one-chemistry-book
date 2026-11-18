"""Book 3 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-4_ZH.md) before the translation existed, from the
English and French configs' choices; refined at the book's close against the link census (pilot_translation/census.py).
Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han text, so a word that is also part of a common
compound or an everyday verb must be stopped or dropped here. One-character terms are never linked.
"""

# result names are never terms (the French NOT_A_TERM, in Chinese)
NOT_A_TERM = ("定理", "引理", "不等式", "公式", "判据", "准则", "原理", "恒等式", "法则", "定律", "悖论", "问题")

STOP = {
    # homographs linked only in their defining chapter (calibrated at the book's close, 2026-11-18):
    # 循环 (the recycle loop of ch. 4) is also every catalytic cycle of ch. 20; 片段 (ch. 15's fragments) is also the
    # mass-spectrum fragments of ch. 32 and the pieces of a synthesis, as English's STOP says; 酰基 alone is the acyl
    # group, not the acyl derivative the definition names
    "循环", "片段", "酰基",
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
    # statistical degrees of freedom (ch. 34), not the variance of a system (ch. 4), as English protects "variance"
    r"(?<=即)自由度(?=。)", r"自由度(?=\s*\$n\s*-)", r"(?<=服从)自由度", r"自由度(?=为\s*2\s*和)",
    r"自由度(?=\s*\$\\nu)", r"自由度(?=为\s*\$n\s*-)", r"自由度(?=是多少)", r"自由度(?=为\s*4）)",
]

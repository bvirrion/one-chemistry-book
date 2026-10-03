#!/usr/bin/env bash
# Chapter-level gates for one year:  bash tools/gates.sh grade-11
# (the build-log gate is separate: see CLAUDE.md). Exit 1 on any failure.
set -u
y=${1:?usage: tools/gates.sh <year>}
d=parts/$y
[ -d "$d" ] || { echo "no such year: $d"; exit 2; }
case $y in
  grade-*)    pfx=g${y#grade-};    book=1 ;;
  bachelor-*) pfx=b${y#bachelor-}; book=$(( ${y#bachelor-} + 1 )) ;;
esac
fail=0
say() { echo "  [$y] $*"; }

# 1. every exo:/pb: label has exactly one solution, in the same order
for f in "$d"/[0-9]*.tex; do
  s="$d/solutions/$(basename "$f")"
  if ! diff -q <(grep -o 'label{\(exo\|pb\):[^}]*}' "$f" | sed 's/label{//;s/}//') \
               <(grep -o 'begin{solution}{[^}]*}' "$s" | sed 's/begin{solution}{//;s/}//') >/dev/null; then
    say "exercise/solution mismatch: $(basename "$f")"; fail=1
  fi
done
# 2. duplicate labels across the whole tree (reported for this year's labels
#    only, so another book's work in progress never fails this year)
dups=$(grep -rho 'label{[^}]*}' parts/ | sort | uniq -d | grep ":$pfx:")
[ -n "$dups" ] && { say "duplicate labels: $dups"; fail=1; }
# 3. typo classes
grep -rn 'end{[a-z]*>' "$d" && { say "\\end{...> typo"; fail=1; }
grep -rn '\.\.\.' "$d" | grep -v '\\dots\|\\foreach\|^\s*%' && { say 'drafty "..." (use \dots)'; fail=1; }
# 4. straight double quotes (use ``...'')
grep -rn '"' "$d"/*.tex "$d"/solutions/*.tex | grep -v '^\S*:\s*%' | grep -v '\\"[a-zA-Z]' \
  && { say 'straight " quote'; fail=1; }
# 5. weekend-problem answers numbered 1..k
python3 tools/check_problem_numbering.py "$d" >/dev/null || { python3 tools/check_problem_numbering.py "$d"; fail=1; }
# 6. every chemical equation balanced
python3 tools/check_ce_balance.py "$d" >/dev/null || { python3 tools/check_ce_balance.py "$d"; fail=1; }
# 6b. glassware pics in a scaled picture must carry [transform shape]
python3 tools/check_pic_scaling.py "$d" >/dev/null || { python3 tools/check_pic_scaling.py "$d"; fail=1; }
# 7. no home experiments, no curriculum or country names in printed text
grep -rniE "at home|try (this|it) yourself|in your kitchen|French|France|coll[eè]ge|lyc[eé]e|terminale|baccalaur|programmes?\b" \
  "$d"/*.tex "$d"/solutions/*.tex | grep -v ':\s*%' && { say "home experiment or curriculum mention (review)"; fail=1; }
# 8. AI images must be JPEG (this year's book)
ls images/book$book/ai/*.png 2>/dev/null && { say "PNG illustrations: transcode to JPEG"; fail=1; }
# 8b. grey stubs (tools/ai_stubs.py) still standing in for AI illustrations:
#     a warning, not a failure -- the book builds, but is not finished
n=$(python3 tools/ai_stubs.py --book $book --list 2>/dev/null | grep -c "images/book$book/ai/$( [ $book = 1 ] && echo "g${y#grade-}-" )")
[ "$n" -gt 0 ] && say "WARNING: $n grey stub illustration(s) still to generate (tools/ai_stubs.py --book $book --list)"
# 9. every % ledger: id has a row; ledger ids unique, sourced and dated
python3 tools/check_ledger.py "$d" >/dev/null || { python3 tools/check_ledger.py "$d"; fail=1; }
# 10. the band's exercise count, star ramp and weekend-problem length
python3 tools/check_exercise_calibration.py "$d" >/dev/null || { python3 tools/check_exercise_calibration.py "$d"; fail=1; }

[ $fail = 0 ] && echo "  [$y] gates OK"
exit $fail

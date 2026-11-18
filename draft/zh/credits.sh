#!/bin/bash
# The four chemistry image-credits pages into Chinese: one Haiku call each, one at a time (a queue "cmd" line).
# Replies go to draft/zh/credits/; the coordinator reads and installs them.
cd /home/bvirrion/repositories/one-course/one-chemistry-book
for f in image-credits image-credits-book2 image-credits-book3 image-credits-book4; do
  { echo "Translate this LaTeX file (the image-credits page of a chemistry textbook) into Simplified Chinese (mainland usage)."
    echo "Keep every LaTeX command, brace, label, URL, file name, licence name (CC BY 4.0, CC BY-SA, public domain stays as the English writes it only inside a licence name), photographer and author names and organisation names exactly as written. Translate the prose and the photo descriptions; Chinese punctuation in Chinese text. Line count and line order must stay the same. Reply with the translated file only, no code fence."
    echo; cat frontmatter/$f.tex; } | timeout 900 claude -p --model claude-haiku-5-5 --effort medium --tools "" > draft/zh/credits/$f.zh.tex 2> draft/zh/credits/$f.err
done

#!/bin/bash
# Chemistry zh trial in a free queue slot (9-call limit): wait until at most 2 physics jobs run, then the two trial
# chapters one after the other with 3 workers, then give the queue back its full list.
Q=../one-physics-book/draft
running() { echo $(( $(grep -c ' started ' $Q/zh-queue.log) - $(grep -c ' done \| NOT CLEAN ' $Q/zh-queue.log) )); }
while [ "$(running)" -gt 2 ]; do sleep 30; done
echo "$(date +%H:%M) slot free ($(running) running)"
cd ../pilot_translation
R=../one-chemistry-book
python3 run.py --repo $R --year grade-11 --lang zh --workers 3 --chapters 07 --book-desc "high school chemistry textbook (grade 11)" > $R/draft/pilot-grade-11-zh/trial.log 2>&1
python3 run.py --repo $R --year grade-11 --lang zh --workers 3 --chapters 07 --book-desc "high school chemistry textbook (grade 11)" >> $R/draft/pilot-grade-11-zh/trial.log 2>&1
python3 run.py --repo $R --year bachelor-1 --lang zh --workers 3 --chapters 03 --book-desc "university chemistry textbook (year 1 of a chemistry bachelor)" > $R/draft/pilot-bachelor-1-zh/trial.log 2>&1
python3 run.py --repo $R --year bachelor-1 --lang zh --workers 3 --chapters 03 --book-desc "university chemistry textbook (year 1 of a chemistry bachelor)" >> $R/draft/pilot-bachelor-1-zh/trial.log 2>&1
cp $Q/zh-queue.list.full $Q/zh-queue.list
echo "$(date +%H:%M) trial done, queue list restored"

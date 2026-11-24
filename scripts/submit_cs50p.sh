#!/bin/sh
# Submits CS50P problems that passed check50 fully (checked 2026-11-24).
set -u

ROOT=$(cd "$(dirname "$0")/.." && pwd)
CS50P="$ROOT/level-0-foundations/01-python/cs50p"
SLUG_PREFIX=cs50/problems/2022/python

# Week 0
cd "$CS50P/week-0-functions/indoor" && submit50 "$SLUG_PREFIX/indoor"; cd -
cd "$CS50P/week-0-functions/playback" && submit50 "$SLUG_PREFIX/playback"; cd -
cd "$CS50P/week-0-functions/faces" && submit50 "$SLUG_PREFIX/faces"; cd -
cd "$CS50P/week-0-functions/einstein" && submit50 "$SLUG_PREFIX/einstein"; cd -
cd "$CS50P/week-0-functions/tip" && submit50 "$SLUG_PREFIX/tip"; cd -

# Week 1
cd "$CS50P/week-1-conditionals/deep" && submit50 "$SLUG_PREFIX/deep"; cd -
cd "$CS50P/week-1-conditionals/meal" && submit50 "$SLUG_PREFIX/meal"; cd -
cd "$CS50P/week-1-conditionals/bank" && submit50 "$SLUG_PREFIX/bank"; cd -
cd "$CS50P/week-1-conditionals/interpreter" && submit50 "$SLUG_PREFIX/interpreter"; cd -
cd "$CS50P/week-1-conditionals/extensions" && submit50 "$SLUG_PREFIX/extensions"; cd -

# Week 2
cd "$CS50P/week-2-loops/camel" && submit50 "$SLUG_PREFIX/camel"; cd -
cd "$CS50P/week-2-loops/coke" && submit50 "$SLUG_PREFIX/coke"; cd -
cd "$CS50P/week-2-loops/twttr" && submit50 "$SLUG_PREFIX/twttr"; cd -
cd "$CS50P/week-2-loops/plates" && submit50 "$SLUG_PREFIX/plates"; cd -
cd "$CS50P/week-2-loops/nutrition" && submit50 "$SLUG_PREFIX/nutrition"; cd -

# Week 3
cd "$CS50P/week-3-exceptions/fuel" && submit50 "$SLUG_PREFIX/fuel"; cd -
cd "$CS50P/week-3-exceptions/taqueria" && submit50 "$SLUG_PREFIX/taqueria"; cd -
cd "$CS50P/week-3-exceptions/grocery" && submit50 "$SLUG_PREFIX/grocery"; cd -
cd "$CS50P/week-3-exceptions/outdated" && submit50 "$SLUG_PREFIX/outdated"; cd -

# Week 4
cd "$CS50P/week-4-libraries/emojize" && submit50 "$SLUG_PREFIX/emojize"; cd -
cd "$CS50P/week-4-libraries/figlet" && submit50 "$SLUG_PREFIX/figlet"; cd -
cd "$CS50P/week-4-libraries/adieu" && submit50 "$SLUG_PREFIX/adieu"; cd -
cd "$CS50P/week-4-libraries/game" && submit50 "$SLUG_PREFIX/game"; cd -
cd "$CS50P/week-4-libraries/professor" && submit50 "$SLUG_PREFIX/professor"; cd -
cd "$CS50P/week-4-libraries/bitcoin" && submit50 "$SLUG_PREFIX/bitcoin"; cd -

# Week 5 (slugs are tests/<name>)
cd "$CS50P/week-5-unit-tests/test_twttr" && submit50 "$SLUG_PREFIX/tests/twttr"; cd -
cd "$CS50P/week-5-unit-tests/test_bank" && submit50 "$SLUG_PREFIX/tests/bank"; cd -
cd "$CS50P/week-5-unit-tests/test_plates" && submit50 "$SLUG_PREFIX/tests/plates"; cd -
cd "$CS50P/week-5-unit-tests/test_fuel" && submit50 "$SLUG_PREFIX/tests/fuel"; cd -

# Week 6
cd "$CS50P/week-6-file-io/lines" && submit50 "$SLUG_PREFIX/lines"; cd -
cd "$CS50P/week-6-file-io/pizza" && submit50 "$SLUG_PREFIX/pizza"; cd -
cd "$CS50P/week-6-file-io/scourgify" && submit50 "$SLUG_PREFIX/scourgify"; cd -
cd "$CS50P/week-6-file-io/shirt" && submit50 "$SLUG_PREFIX/shirt"; cd -

# Week 7
cd "$CS50P/week-7-regex/numb3rs" && submit50 "$SLUG_PREFIX/numb3rs"; cd -
cd "$CS50P/week-7-regex/watch" && submit50 "$SLUG_PREFIX/watch"; cd -
cd "$CS50P/week-7-regex/working" && submit50 "$SLUG_PREFIX/working"; cd -
cd "$CS50P/week-7-regex/um" && submit50 "$SLUG_PREFIX/um"; cd -
cd "$CS50P/week-7-regex/response" && submit50 "$SLUG_PREFIX/response"; cd -

# Week 8
cd "$CS50P/week-8-oop/seasons" && submit50 "$SLUG_PREFIX/seasons"; cd -
cd "$CS50P/week-8-oop/jar" && submit50 "$SLUG_PREFIX/jar"; cd -
cd "$CS50P/week-8-oop/shirtificate" && submit50 "$SLUG_PREFIX/shirtificate"; cd -

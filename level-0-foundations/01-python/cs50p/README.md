# CS50P — Introduction to Programming with Python

My solutions to [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/). One folder per problem, named as in the course, so each folder is what `check50` / `submit50` expects.

| Week | Topic | Problems |
|------|-------|----------|
| 0 | [Functions, Variables](week-0-functions/) | indoor · playback · faces · einstein · tip |
| 1 | [Conditionals](week-1-conditionals/) | deep · bank · extensions · interpreter · meal |
| 2 | [Loops](week-2-loops/) | camel · coke · twttr · plates · ~~nutrition~~ (not done) |
| 3 | [Exceptions](week-3-exceptions/) | fuel · taqueria · grocery · outdated |
| 4 | [Libraries](week-4-libraries/) | emojize · figlet · adieu · game · professor · bitcoin |
| 5 | [Unit Tests](week-5-unit-tests/) | test_twttr · test_bank · test_plates · test_fuel |
| 6 | [File I/O](week-6-file-io/) | lines · pizza · scourgify · shirt |
| 7 | [Regular Expressions](week-7-regex/) | numb3rs · watch · working · um · response |
| 8 | [Object-Oriented Programming](week-8-oop/) | seasons · jar · shirtificate |
| 9 | Final project | Stage 1 of Dubai Property Analytics (separate repo) |

Problems with tests: test_twttr, test_bank, test_plates, test_fuel, numb3rs, working, um, seasons, jar.

## Running

Programs that open files by relative path (`shirt.png`, CSVs) must be run from their own folder:

```sh
cd level-0-foundations/01-python/cs50p/week-6-file-io/shirt
uv run shirt.py before1.jpg after1.jpg
```

`bitcoin` needs a free [CoinCap](https://coincap.io/api-key) key in `COINCAP_API_KEY`.

Tests run from the repo root: `uv run pytest level-0-foundations/01-python/cs50p`.

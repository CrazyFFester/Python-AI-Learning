# CLAUDE.md — Python-AI-Learning

Learning log for Roadmap v3 (AI Engineer → AI Architect). The full plan lives in Obsidian: `04 Databases/AI Dashboard/Roadmap.md`; the README holds only a progress summary.

## Layout

```
level-0-foundations/
├── 01-python/cs50p/week-N-topic/<problem>/   CS50P, one folder per problem, named as in the course
├── 01-python/gaps/NN-topic/                  topics CS50P skipped (decorators, generators, ...)
├── 02-sql/ … 06-probability-statistics/      remaining Level 0 modules
level-1-junior/NN-module/                     created when Level 1 starts
dsa/<pattern>/                                NeetCode 150, created when DSA starts
scripts/submit_cs50p.sh                       submit50 for every CS50P problem (POSIX sh)
```

## CS50P submission

- All 41 problems pass `check50` and were submitted on 2026-11-24 (gradebook 9/10 weeks); only the final project is left.
- Slug is `cs50/problems/2022/python/<folder>`, except Week 5: `test_<name>` folders use `tests/<name>`.
- Run `check50` / `submit50` from the problem's own folder; auth goes over GitHub SSH. Code lands in the private `me50/CrazyFFester` repo, one branch per slug; never edit that repo by hand.
- Keep `scripts/submit_cs50p.sh` in sync when a problem folder is added or renamed.

## Where things go

- Course exercises and drills: `level-N-*/NN-module/<source>/`, one subfolder per source (course, book, problem set), named after it.
- Topics a course skipped: `level-N-*/NN-module/gaps/NN-topic/`.
- DSA problems: `dsa/<pattern>/`.
- Portfolio projects (Dubai Property Analytics and others): separate repos, only linked from the README.
- Theory notes go to Obsidian and definitions/formulas to Anki, never into this repo.
- SQL: one query per `.sql` file, problem link as the first `--` line; LeetCode files named `NNNN-problem-slug.sql`.
- Notebooks: clear outputs before committing unless the plot is the point.

## Code conventions

- Tests sit next to the module they test as `test_*.py`; no `__init__.py`, no `conftest.py` path hacks.
- pytest runs in the default `prepend` import mode, so:
  - test file basenames must be unique across the repo;
  - never name a module after the stdlib (`dataclasses.py`, `typing.py`, `contextlib.py`, `statistics.py`, ...), it shadows the real module.
- Math drills: every hand-written operation is checked against NumPy/scipy in a test (`np.allclose`).
- Don't edit finished CS50P solutions unless asked; they are a record of where I was.

## Environment

- One uv project for the whole repo, Python 3.13. Add dependencies with `uv add`, never pip.
- `uv run pytest` from the root runs everything.
- Programs that open files by relative path (CS50P `shirt`, `pizza`, `scourgify`, `shirtificate`) must be run from their own folder.

## Docs

When a module starts, finishes or the structure changes, update all of: root `README.md` (progress table, layout), `level-N-*/README.md` (module status), the module's own README, and this file.

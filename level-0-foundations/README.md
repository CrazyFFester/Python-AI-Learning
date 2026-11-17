# Level 0 — Foundations refresh

Oct 2026 – mid-Feb 2027, about 15 weeks of Learn slots. Studied at UOWD but faded, so every module stays, with course notes as a fast second pass.

| # | Module | Weeks | Main resource | Status |
|---|--------|-------|---------------|--------|
| 01 | [Python core and tooling](01-python/) | 2 (+2) | [CS50P](01-python/cs50p/) ✅, then [gaps](01-python/gaps/) | 🟨 |
| 02 | [SQL](02-sql/) | 2 | SQLBolt, LeetCode Top SQL 50 | ⬜ |
| 03 | [NumPy, Pandas, plots](03-data-stack/) | 2 | Kaggle Pandas, Kaggle Data Visualization | ⬜ |
| 04 | [Linear algebra](04-linear-algebra/) | 2 | 3Blue1Brown, Essence of Linear Algebra | ⬜ |
| 05 | [Calculus](05-calculus/) | 1 | 3Blue1Brown, Essence of Calculus | ⬜ |
| 06 | [Probability and statistics](06-probability-statistics/) | 4 | StatQuest | ⬜ |

Build slots in this phase go to Dubai Property Analytics (separate repo): stage 1 (DLD data into Postgres, tests) in Nov, stage 2 (EDA notebook) in Dec–Feb.

## Conventions

- Each module folder holds code only: solutions, drills, notebooks. Theory lives in Obsidian, definitions and formulas in Anki.
- One subfolder per source (course, book, problem set), named after it.
- Python modules sit next to their `test_*.py`; `uv run pytest` from the repo root runs everything.

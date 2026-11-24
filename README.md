# Python-AI-Learning

My learning log on the way from Python exercises to **AI Engineer → AI Architect**. Coursework, drills and tests live here; portfolio projects live in their own repos.

**Target:** job-ready as a Junior AI Engineer (Python backend + LLM) in Dubai around graduation, Dec 2027.
**Strategy:** sustainability over speed, depth over breadth, real projects over tutorial demos.
**Main project:** Dubai Property Analytics: Dubai Land Department open data → Postgres → EDA → price model → FastAPI → "ask the market" text-to-SQL assistant (separate repo).

## Progress

| Phase | When | Status |
|-------|------|--------|
| [Level 0 — Foundations refresh](level-0-foundations/) | Oct 2026 – mid-Feb 2027 | 🟨 CS50P problem sets submitted (final project pending), Python gaps in progress |
| Level 1.1 — ML fundamentals | mid-Feb – Apr 2027 | ⬜ |
| Level 1.2 — Backend engineering | May – Jun 2027 | ⬜ |
| Level 1.3 — Deep learning with PyTorch | Summer 2027 (or Sep – Oct) | ⬜ |
| Level 1.4 — LLM engineering | Sep – Nov 2027 | ⬜ |
| Level 1.5 — Low-level C/CUDA project | Summer 2027 or Q1 2028 | ⬜ |
| DSA — NeetCode 150 | All year: 40 by Feb 2027, 100–120 by Dec 2027 | ⬜ |

## Repository layout

```
level-0-foundations/
├── 01-python/
│   ├── cs50p/                    CS50P problem sets, week-N-topic/problem/
│   └── gaps/                     what CS50P skips: decorators, generators, context managers, ...
├── 02-sql/                       SQLBolt, LeetCode Top SQL 50
├── 03-data-stack/                NumPy, Pandas, plots
├── 04-linear-algebra/
├── 05-calculus/
└── 06-probability-statistics/
scripts/
└── submit_cs50p.sh               submit50 for every CS50P problem
pyproject.toml, uv.lock           one uv project for the whole repo (Python 3.13)
```

Planned as they start: `level-1-junior/` (one folder per module) and `dsa/` (NeetCode, one folder per pattern).

### Where things go

| What | Where |
|------|-------|
| Course exercises and drills | `level-N-*/NN-module/<source>/` |
| Topics a course skipped | `level-N-*/NN-module/gaps/` |
| DSA problems | `dsa/<pattern>/` |
| Portfolio projects | Separate repos, linked from here |
| Theory notes | Obsidian, not this repo |
| Definitions and formulas | Anki |

## Running

```sh
uv sync
uv run pytest
uv run pytest level-0-foundations/01-python/cs50p/week-7-regex
```

## Weekly grid

19 pomodoros a week (25/3), about 8 h of focused work: 7 Learn, 6 Build, 5 DSA, 1 Read.

| Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|-----|-----|-----|-----|-----|-----|-----|
| Learn ×3 | Learn ×2, DSA | Build ×2, DSA | Learn ×2, DSA | Build ×3 | Build, DSA ×2, Read | Rest |

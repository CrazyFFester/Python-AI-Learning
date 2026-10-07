# Python-AI-Learning

My learning log on the way from Python exercises to **AI Engineer → AI Architect**. Code lives in this repo, the plan below is what I follow.

**Target:** job-ready as a Junior AI Engineer in Dubai around graduation (Dec 2027).
**Strategy:** sustainability over speed, depth over breadth, real projects over tutorial demos.
**Edge:** RTX 5080 (16 GB) for local training and LLMs, Akein as a real LLM agent, C/C++ and Rust for low-level inference work.

## Weekly grid

19 pomodoros a week (25 min work, 3 min rest), about 8 h of focused work: **7 Learn, 6 Build, 5 DSA, 1 Read**.

| Day | Pomodoros | Slots |
|-----|-----------|-------|
| Mon | 3 | Learn ×3 |
| Tue | 3 | Learn ×2, DSA ×1 |
| Wed | 3 | Build ×2, DSA ×1 |
| Thu | 3 | Learn ×2, DSA ×1 |
| Fri | 3 | Build ×3 |
| Sat | 4 | Build ×1, DSA ×2, Read ×1 |
| Sun | 0 | Rest |

- **Learn:** theory of the current module; formulas and definitions go into Anki.
- **Build:** current project or module practice; code beats notes.
- **DSA:** one problem per slot or a re-solve of a failed one; Saturday is one timed medium plus review.
- **Read:** one paper section or deep blog post per week, three takeaways in Obsidian.

## Timeline

| Phase | When |
|-------|------|
| Level 0 — Foundations refresh | Oct 2026 – Jan 2027 |
| Level 1.1 — ML fundamentals | Feb – Apr 2027 |
| Level 1.2 — Backend engineering | May – Jun 2027 |
| Level 1.3 — Deep learning with PyTorch | Summer 2027 (or Sep – Oct 2027) |
| Level 1.4 — LLM engineering | Sep – Nov 2027 |
| Level 1.5 — Low-level signature project | Summer 2027 or Q1 2028 |
| Junior applications | From Sep 2027 |
| Fully ready | Dec 2027 (intensive summer) / Mar 2028 (internship summer) |

Summer 2027 internship applications run Nov 2026 – Feb 2027.

## Level 0 — Foundations refresh

| Module | Weeks | Main resource |
|--------|-------|---------------|
| Python core and tooling | 2 | Python tutorial, Real Python |
| SQL | 2 | SQLBolt, LeetCode Top SQL 50 |
| NumPy, Pandas, plots | 2 | Kaggle Pandas / Data Visualization |
| Linear algebra | 2 | 3Blue1Brown, Essence of Linear Algebra |
| Calculus | 1 | 3Blue1Brown, Essence of Calculus |
| Probability and statistics | 4 | StatQuest |

Build: polish the Akein and ETMBot repos (README, demo GIF, run instructions), plus an EDA notebook on Dota 2 matches from the OpenDota API.

## Level 1 — Junior AI Engineer

Entry role: Python backend with LLM features.

1. **ML fundamentals** (12 weeks) — Géron, *Hands-On ML with Scikit-Learn and PyTorch*. Project 1: classical ML on Dota 2 data.
2. **Backend engineering** (8 weeks) — FastAPI, Postgres, Redis, auth, tracing, Docker, CI. Build: Akein's backend core as a standalone service.
3. **Deep learning with PyTorch** — Karpathy, *Neural Networks: Zero to Hero*. Project 2: ETMBot upgrade with W&B tracking, ablations, model card, Gradio demo.
4. **LLM engineering** (10 weeks) — Hugging Face LLM Course, tool calling, RAG, agents and MCP, evals in CI, tracing, prompt-injection defenses. Project 3: Akein as the flagship.
5. **Low-level signature project** — a CUDA kernel benchmarked against PyTorch, or int4/int8 quantization with perplexity and speed measured; then one small PR to llama.cpp.
6. **DSA** (all year) — NeetCode 150; 40 problems by Feb 2027, 100–120 by Dec 2027.
7. **Interviews and job search** (all year) — 5–10 mock interviews, one-page CV, pinned GitHub, GITEX Global networking.

### Junior readiness checklist

- [ ] Akein is deployed and its core (agent loop, tools, retrieval) is my own code
- [ ] Akein answers from a real client's knowledge base
- [ ] Akein has an eval set tracking accuracy, p95 latency and cost per conversation
- [ ] Akein has prompt-injection defenses, tracing, CI with evals and ADRs
- [ ] Dota 2 ML project and upgraded ETMBot are on GitHub with writeups
- [ ] One low-level C/CUDA project with benchmarks
- [ ] Can build, test and deploy FastAPI + Postgres + Redis with CI
- [ ] 100+ DSA problems solved by pattern
- [ ] SQL is comfortable: joins, window functions, indexes
- [ ] Can explain data leakage, cross-validation, metric choice, embeddings, attention, KV cache, RAG failure modes, prompt injection
- [ ] 5–10 mock interviews done; CV and pinned GitHub ready

## Level 2 — Middle AI Engineer

About 1.5–2 years after the first job: advanced ML (XGBoost, Optuna, SHAP), production RAG, QLoRA fine-tuning and vLLM serving, MLOps, cloud, system design, and one production-grade end-to-end project.

## Level 3 — Senior to AI Architect

About 5–7 years in total: production excellence (SRE), distributed training, architecture at scale (design docs, ADRs, cost modeling, security), one or two specializations, and mentoring.

## Repository layout

```
Pre-Junior/python/   early Python exercises (1.py – 12.py)
```

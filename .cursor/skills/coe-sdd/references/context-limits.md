# context-limits — Token Budget

## Targets

| Threshold | Action |
|-----------|--------|
| < 40k tokens | Normal operation |
| 40k–60k tokens | 🟡 Warn: suggest unloading unused docs |
| > 60k tokens | 🔴 Alert: load only what the current task requires; archive STATE entries if needed |

## What Adds Up

Heavy artifacts: ARCHITECTURE.md (can be 5k+), CONSTITUTION.md (3–8k), multiple spec/plan files, brownfield docs loaded simultaneously.

## Minimum Context by Command

| Command | Load | Never load simultaneously |
|---------|------|--------------------------|
| `coe-sdd-resume` | PROJECT.md + ROADMAP.md + STATE.md | Multiple feature specs |
| `coe-sdd-plan MN` | + CONSTITUTION.md + spec/plan/tasks of the current feature (`MN-{feature-slug}`) | Other feature specs |
| `coe-sdd-implement MN` | + tasks.md of the current feature folder + TESTING.md + CONVENTIONS.md | tasks from other features; ARCHITECTURE.md (unless task references it) |
| Brownfield | ARCHITECTURE.md + CONCERNS.md (on demand) | Full feature specs |

## Archiving STATE.md

When STATE.md approaches 10k tokens:
1. Move entries older than 60 days to `.specs/project/STATE-archive-YYYY-MM.md`
2. Keep a one-line summary of archived content in STATE.md:
   ```
   [Archived 2026-04-01] 12 decisions, 3 blockers (resolved) → STATE-archive-2026-04.md
   ```

## Sub-Agent Context Budget

Each sub-agent for task implementation receives only:
- Task definition (~500 tokens)
- CONVENTIONS.md + TESTING.md (~2–4k tokens)
- Relevant spec section (~1–3k tokens)

Total per sub-agent: target `<10k tokens` input.

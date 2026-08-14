# analyze — Cross-Artifact Consistency Check

## When Triggered

Explicitly only:
`"analyze M1"`, `"check consistency"`, `"validate before implement"`, `"analisar artefatos"`, `"tem gaps na cobertura?"`

Or at the end of `coe-sdd-plan` when the user explicitly requests it.

**This check is read-only. It does not create or modify files. Results are delivered as a message only.**

## What It Checks

| Check | What |
|-------|------|
| **Coverage gaps** | FR-* in spec.md without corresponding task in tasks.md |
| **Duplicate tasks** | Overlapping tasks addressing the same requirement |
| **Terminology inconsistency** | Terms in tasks.md that don't match GLOSSARY or spec.md |
| **Constitution alignment** | Tasks that may violate Core Principles |
| **Data model ↔ spec** | Entities in data-model.md not referenced in spec or tasks |
| **Contracts ↔ plan** | API contracts not reflected in plan.md or tasks.md |
| **Test coverage** | Tasks without Tests or Gate columns filled |
| **Story points missing** | Product US in spec.md without a story point value |
| **Story points off-scale** | SP value not in the Fibonacci scale (`1\|2\|3\|5\|8\|13\|21`) |
| **Story points drift** | SP echoed in tasks.md phase header doesn't match spec.md US value |
| **Story points rollup** | plan.md Story Points table total doesn't match sum in spec.md |

## Severity Classification

- **CRITICAL** — blocks `coe-sdd-implement` until resolved (missing FR coverage, constitution violation, product US without story points)
- **MEDIUM** — significant gap; surface with suggested remediation (off-scale SP, SP drift between tasks.md and spec.md)
- **LOW** — minor inconsistency; informational only (plan.md rollup mismatch)

## Output Format

```
## Analyze Report: MN — [milestone name]

### CRITICAL (blocks implement)
- [finding]: [location] — [suggested action]

### MEDIUM
- [finding]: [location] — [suggested action]

### LOW
- [finding]: [location]

### Summary
Coverage: X/Y requirements have tasks.
Constitution: aligned / N violations.
Tests: X/Y tasks have gate commands defined.
Story points: X total (P1: Y).
```

CRITICAL findings block `coe-sdd-implement` until the user resolves them and re-runs analyze (or explicitly acknowledges the risk).

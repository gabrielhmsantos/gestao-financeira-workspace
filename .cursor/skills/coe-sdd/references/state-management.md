# STATE.md — Persistent Memory

## Structure

```markdown
## Decisions (AD-NNN)
## Active Blockers (B-NNN)
## Deferred Ideas
## Lessons Learned
```

## Entry Formats

**Decision:**
```
**AD-001** [YYYY-MM-DD] [MN] Decision title
Rationale: why this was chosen.
Alternatives: option A (rejected: reason); option B (rejected: reason).
```

**Blocker:**
```
**B-001** [YYYY-MM-DD] [MN] Blocker description
Impact: what is blocked.
Resolution: [open | resolved YYYY-MM-DD — how]
```

**Deferred Idea:**
```
- [YYYY-MM-DD] Idea description — deferred because: reason. Revisit: condition/milestone.
```

**Spec Deviation:**
```
**SD-001** [YYYY-MM-DD] [MN/T-ID] What deviated from spec.
Reason: technical constraint / discovery / user decision.
Status: [open — spec update pending | closed — spec updated]
```

**Constitution Violation (justified):**
```
**AD-NNN** [YYYY-MM-DD] CONSTITUTION VIOLATION — [principle name]
Context: what triggered the violation.
Justification: why the exception is acceptable.
Mitigation: how risk is managed.
```

## Limits

- Target: `<10k tokens`
- Archive entries older than 60 days to `.specs/project/STATE-archive-YYYY-MM.md`
- Keep one-line summary of archived entries:
  ```
  [Archived 2026-04-01] 12 decisions, 3 blockers (resolved) → STATE-archive-2026-04.md
  ```

## When to Update

| Event | Update |
|-------|--------|
| `coe-sdd-plan MN` completes | Add AD-NNN for key decisions |
| Constitution violation detected | Add AD-NNN: CONSTITUTION VIOLATION + justification |
| Spec deviation found | Add SD-NNN |
| Blocker identified | Add B-NNN |
| Milestone completes | Add lessons learned; close resolved blockers |
| Out-of-order planning confirmed | Add AD-NNN noting risk |

## coe-sdd-status Output

When `"status"`, `"onde estamos"`, or `"show roadmap"` is triggered:
load ROADMAP.md + STATE.md and report:
- Milestone statuses (emoji + name + brief note)
- Open blockers (B-NNN)
- Last 3 decisions (AD-NNN)
- Next planned action

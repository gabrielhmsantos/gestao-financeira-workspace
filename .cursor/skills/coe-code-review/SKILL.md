---
name: coe-code-review
description: >-
  Two-axis code review (Spec × Standards) of coe-sdd work against feature
  artifacts and project standards. Resolves scope from a Jira issue key, Phase,
  or T-ID — and after implement, infers Jira issue/Phase/T-IDs from the session
  and git so the engineer need not re-enter the Jira project. Works greenfield
  and brownfield. Use when finishing a Phase/Subtask, or when the user asks for
  "code review", "revise essa phase", "review T007", "review PROJ-123", or
  "/coe-code-review".
---

# coe-code-review — Spec × Standards gate for coe-sdd

Review completed implementation against coe-sdd artifacts before marking tasks
`[x]` or closing a Jira Subtask. Hybrid of Matt-style two-axis review and a
post-review fix gate.

**Core principle:** Spec fidelity and coding standards are separate axes — never
merge or rerank findings across them.

## Triggers

- Explicit `/coe-code-review` or skill attach
- "code review", "revise essa phase", "review T007", "review PROJ-123"
- After implementing a Phase / Jira Subtask / set of `T00x`

## Hard rules

1. **Pin the git range before spawning reviewers.** Confirm refs resolve
   (`git rev-parse`) and the diff is non-empty. Bad ref or empty diff → STOP.
2. **Prefer** `BASE_SHA..HEAD_SHA` (work session). If the user only asks for
   branch vs main: `origin/main...HEAD` — Spec scope stays limited to the
   resolved Phase / T-IDs.
3. **Crafted context only** for sub-agents — never pass the parent session
   history.
4. Spawn **two** `generalPurpose` sub-agents **in parallel** (Spec + Standards).
5. After the report: fix **Critical** immediately; fix **Important** before
   marking `[x]` / closing the Subtask; note **Minor** for later. Push back
   with evidence if the reviewer is wrong.
6. **Greenfield and brownfield.** Never require `.specs/codebase/`. Use the
   Standards cascade below.
7. After Assessment, if a **Jira issue key is known** (explicit **or inferred**),
   post a short comment via Atlassian MCP (`addCommentToJiraIssue`). **Never**
   transition status. Never ask the user for the Jira **project** key — it is
   embedded in the issue key (`PROJ-123`).

## Default scope

**Phase** (`## Phase N` in `tasks.md` / Jira Subtask) — all `T00x` in that
phase. Also accepts an explicit `T00x` list or a feature folder. Not
whole-milestone by default.

## Workflow

```
Progress:
- [ ] 1. Resolve scope — infer Jira/Phase/T-IDs if omitted (see resolve-scope.md)
- [ ] 2. Pin BASE_SHA / HEAD_SHA; verify non-empty diff
- [ ] 3. Load Spec artifacts + Standards sources (cascade)
- [ ] 4. Spawn Spec + Standards sub-agents in parallel
- [ ] 5. Aggregate under ## Spec / ## Standards + Assessment
- [ ] 6. Act on Critical / Important
- [ ] 7. Optional Jira comment (if issue key known — explicit or inferred)
```

### 1. Resolve scope

Follow [resolve-scope.md](references/resolve-scope.md).

**After implement in the same session:** the user should be able to say only
`/coe-code-review` or "faz o code-review". **Infer** Jira issue, Phase, and
T-IDs — do **not** ask for Jira project or issue key unless inference fails.

Order:

0. **Infer** Jira key + work scope from session / git / STATE (see resolve-scope)
1. Explicit Jira issue key (if given) → feature folder + Phase / US / T-IDs
2. `T00x` → Phase + US in `tasks.md`
3. Explicit `.specs/features/{MN}-*` path + Phase name
4. Ambiguous after inference → ask only for the missing piece (T-ID / Phase /
   issue key) — never ask for "projeto Jira" alone

### 2. Pin git range

```bash
git rev-parse {BASE_SHA} {HEAD_SHA}
# Session work (preferred):
git diff --stat {BASE_SHA}..{HEAD_SHA}
git log --oneline {BASE_SHA}..{HEAD_SHA}
# Branch vs main (only if user asks):
# git diff --stat origin/main...HEAD
```

If the user did not give `BASE_SHA`, ask for it (or the commit before their
work). Do not invent a range.

### 3. Load sources

**Spec axis** — scoped `tasks.md` (Phase / T-IDs) + matching US/FR from
`spec.md`; `plan.md` / `contracts/` / `data-model.md` only if the Phase
references them; always `.specs/project/CONSTITUTION.md` for binding rules
touched by the change.

**Standards cascade** (list every path actually found in the Standards prompt):

1. If present: `.specs/codebase/CONVENTIONS.md` + `TESTING.md`
2. Else: `.specs/project/CONSTITUTION.md` + `.specs/foundation/STACK.md` +
   relevant bits of feature `plan.md`
3. Always: Fowler smell baseline (inlined in [reviewer-standards.md](reviewer-standards.md))
4. Skip anything tooling already enforces; repo docs override smells

Record which tier applied: `codebase` | `constitution+stack` | `baseline-only`.

### 4. Spawn sub-agents

Fill and dispatch in **one** message (two Task / Agent calls):

- Spec → [reviewer-spec.md](reviewer-spec.md)
- Standards → [reviewer-standards.md](reviewer-standards.md)

### 5. Aggregate

Present reports under `## Spec` and `## Standards` (verbatim or lightly
cleaned). Do **not** merge findings across axes.

Then:

```markdown
## Assessment
**Ready to close?** Yes | With fixes | No
**Blockers:** Critical N · Important N
**Worst Spec:** …
**Worst Standards:** …
**Standards sources used:** codebase | constitution+stack | baseline-only
**Next:** ordered fix list
```

Map sub-agent findings into severities for the gate:

| Severity | Meaning |
|----------|---------|
| Critical | Bugs, security, data-loss, broken Done-when / Gate |
| Important | Missing FR/US pieces, Constitution breaches, architecture gaps |
| Minor | Style, polish, optional improvements |

### 6. Act

- Critical → fix now
- Important → fix before `[x]` / Subtask Done
- Minor → note only (STATE or leave for later)
- If reviewer wrong → push back with code/tests, then proceed

### 7. Jira comment (conditional)

When an issue key is **known** (user typed it **or** step 0 inferred it). Short
body: Assessment + Critical/Important bullets. No status transition. If no key
could be inferred, skip the comment — Spec/Standards review still runs.

## Out of scope (v1)

- Hard gate inside `coe-sdd-implement`
- Jira status transitions
- Milestone-wide review as default
- Generating or requiring `.specs/codebase/`

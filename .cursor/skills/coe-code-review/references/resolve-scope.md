# Resolve scope — Jira / T-ID / Phase → coe-sdd artifacts

Used by `coe-code-review` before loading Spec sources or spawning reviewers.

## Inputs (resolve in order)

| Priority | Input | How to resolve |
|----------|--------|----------------|
| 0 | **Infer** (post-implement) | Session + git + STATE/HANDOFF — see below |
| 1 | Jira issue key (`PROJ-123`) | `getJiraIssue` → parse summary/description/parent |
| 2 | Task id(s) (`T007`, `T004 T005`) | Search `tasks.md` under `.specs/features/` |
| 3 | Feature path + Phase | e.g. `.specs/features/M0-bootstrap` + `Phase 3` |
| 4 | Ambiguous | Ask only for the missing piece — **never** ask for Jira project alone; **never guess** the feature folder |

Default review unit: **Phase** (all `T00x` under that `## Phase N` header).
Narrow to an explicit `T00x` list when the user names them.

**Jira project:** never required as a separate input. The project key is the
prefix of the issue key (`ABC-42` → project `ABC`). Infer the **issue key**;
MCP calls use that key only.

## 0. Infer after implementation (default when user omits keys)

When the user runs `/coe-code-review` (or equivalent) **without** naming a Jira
key / project / T-ID — typical right after `coe-sdd-implement` — the
**orchestrator** (not the reviewer sub-agents) must infer before asking:

### 0a. Jira issue key (try in order; stop at first solid hit)

1. **Same conversation** — issue key already mentioned when the engineer pulled
   or started the task (`PROJ-123`, link to Jira, "suba a Subtask X"). Reuse it.
2. **Git branch name** — `git branch --show-current`; match `\b[A-Z][A-Z0-9]+-\d+\b`.
3. **Recent commits in the review range** (or last ~15 on the branch) —
   `git log --oneline`; same issue-key regex in subjects/bodies.
4. **STATE.md / HANDOFF.md** — `Current Work`, handoff fields, or any stored
   issue key for the active milestone.
5. **Optional JQL assist** — only if Phase/US/`[MN]` already known from steps
   below: `searchJiraIssuesUsingJql` for Subtasks whose summary contains the
   Phase title and `[MN]` (or label `MN`). If **exactly one** hit → use it. If
   zero or many → do not guess; continue without Jira or ask for the issue key.

If still unknown: proceed with Spec/Standards **without** Jira comment; ask for
the issue key **only if** the user wanted a Jira comment or status follow-up.

### 0b. Work scope (Phase / T-IDs) when omitted

1. **Same conversation** — T-IDs or Phase just implemented.
2. **tasks.md** — recently checked `[x]` lines in the active feature folder
   (from STATE `Current Work` / ROADMAP in-progress / conversation). Prefer the
   Phase that contains those T-IDs.
3. **Commit messages** — `feat(M0-bootstrap): …` / `T00x` mentions → folder + tasks.
4. Still ambiguous → ask for Phase or T-ID list (not Jira project).

### 0c. After inference

If an issue key was inferred, continue as **§1 From Jira issue** (validate with
`getJiraIssue` and align Phase/T-IDs). Prefer inferred T-IDs/Phase from 0b when
they are more precise than a broad Subtask match.

## 1. From Jira issue

1. Call Atlassian MCP `getJiraIssue` for the key.
2. Extract milestone id from summary/labels/description: `[M0]`, `[M1]`, … or label `M0`.
3. Glob `.specs/features/{MN}-*/` that have both `spec.md` and `tasks.md`.
   - One folder → use it.
   - Several folders → match feature slug from issue text / parent Epic / História;
     if still ambiguous, list folders and ask.
4. Map issue type to scope:
   - **Subtask** → treat as a Phase: match `## Phase N: …` in `tasks.md` using
     Phase title tokens from the issue summary (e.g. `Phase 3`, US title fragment).
   - **História / Story** → if the user asked to review the whole story, take all
     Phases tagged with that US; otherwise ask which Phase.
   - **Epic** → STOP and ask for a Subtask, Phase, or `T00x` (milestone-wide is
     out of default scope).
5. Collect every `- [ ] T00x` / `- [x] T00x` under the matched Phase until the next
   `## Phase` header (or EOF).

## 2. From T-ID

1. `rg -n "T00N"` under `.specs/features/` (prefer `tasks.md`).
2. Open the matching `tasks.md`. The enclosing `## Phase …` is the Phase scope
   unless the user listed only specific T-IDs — then scope = those lines only.
3. Read `[US-N]` / `[INFRA]` on the task line for Spec US mapping.

## 3. From explicit path + Phase

1. Require folder under `.specs/features/` with `tasks.md`.
2. Match `## Phase N` (number and/or title substring).
3. Collect T-IDs as in step 1.5.

## Artifact load list (for Spec axis)

Always load (scoped excerpts preferred over full files when large):

| Artifact | When |
|----------|------|
| Feature `tasks.md` | Always — Phase / T-ID blocks only |
| Feature `spec.md` | Always — matching US + related FR/BR / Out of scope |
| `.specs/project/CONSTITUTION.md` | Always — principles touched by the change |
| Feature `plan.md` | If Phase / tasks reference structure, stack, or constitution check |
| `contracts/*` | If Phase / tasks / US mention APIs or contracts |
| `data-model.md` | If Phase / tasks mention entities / schema |
| `quickstart.md` | Only if Phase is validation / E2E oriented |

## Standards source discovery (for Standards axis)

Check existence; do not invent content:

```
.specs/codebase/CONVENTIONS.md
.specs/codebase/TESTING.md
.specs/project/CONSTITUTION.md
.specs/foundation/STACK.md
.specs/features/{folder}/plan.md
```

Tier label for Assessment:

- Both codebase docs present → `codebase`
- Else Constitution and/or STACK (and optional plan) → `constitution+stack`
- Else only smell baseline will apply → `baseline-only`

## Output of this step (pass to orchestrator)

Return a short scope block:

```markdown
**Feature folder:** `.specs/features/{MN}-{slug}/`
**Milestone:** MN
**Phase:** Phase N — Title (or n/a)
**T-IDs:** T004, T005, …
**US tags:** US1 | INFRA | …
**Jira key:** PROJ-123 | none
**Jira key source:** explicit | inferred-session | inferred-branch | inferred-commits | inferred-state | inferred-jql | none
**Spec paths:** …
**Standards paths:** …
**Standards tier:** codebase | constitution+stack | baseline-only
```

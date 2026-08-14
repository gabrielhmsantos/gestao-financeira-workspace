# coe-sdd-implement — Execute Tasks

## Pre-checks

1. Resolve the feature folder:
   - If a `feature-name` is provided: load `tasks.md` from `.specs/features/{MN}-{feature-slug}/`
   - Milestone with `### Features` and no feature-name specified: list PLANNED features for MN and ask which to implement
   - Scope-only milestone (no `### Features`): load `tasks.md` from the single milestone folder (`.specs/features/{MN}-{milestone-slug}/`) directly

2. Require workspace rule + layout + Git (from `coe-sdd-init`):
   - Load the IDE context file (Cursor: `.cursor/rules/coe-sdd-rule.mdc`; else `CLAUDE.md` / `AGENTS.md`)
   - Require **Workspace layout** (A|B|C) and **`## Git`** (pattern + default type)
   - If missing → stop: `"Execute coe-sdd-init first."`
   - Do **not** re-ask or rewrite the Git pattern here

3. Resolve target **code repository** for this feature/tasks:
   - Use the code-repositories map in the IDE rule (and PROJECT.md Workspace layout)
   - If the task's code root is not listed → stop:
     `"Atualize a rule e PROJECT.md com o novo repositório (layout A|B|C) e tente de novo."`

4. Ensure feature branch **inside the target code repository** (not the control repo):
   - `feature-folder` = basename of the resolved feature folder (e.g. `M1-authentication-session`)
   - `type` = default type from the rule (`feat` unless the user overrides for this invocation only — override does not rewrite the rule)
   - `BRANCH` = apply Git pattern (default `{type}/{feature-folder}` → e.g. `feat/M1-authentication-session`)
   - Algorithm (run with cwd = code repo root):
     1. Not a git repo / git unavailable → warn and continue (still apply the branch-name guard below if git becomes available mid-session)
     2. Already on `BRANCH` → noop
     3. Branch exists → `git checkout BRANCH`
     4. Branch missing → create from default branch (`main` / `master` / remote default) — not from another feature branch — then stay on `BRANCH`
     5. Dirty working tree blocks checkout → stop; do not start tasks
   - **Branch pattern guard (mandatory before any task work):**
     - After ensure, read `git branch --show-current` in the code repo
     - Current branch MUST equal the resolved `BRANCH` (and thus match the rule's Git pattern)
     - **Never** implement on environment or integration branches, including but not limited to: `main`, `master`, `develop`, `prod`, `production`, `hml`, `homolog`, `staging`, `release`, `trunk`
     - If current branch is an environment branch or otherwise does **not** match the Git pattern → stop:
       `"Implementação bloqueada: branch atual '{current}' não segue o padrão Git do projeto ({pattern}). Faça checkout/crie '{BRANCH}' e tente de novo."`
     - Do not auto-commit or edit application code until this guard passes

5. Check for incomplete tasks from previous milestones — block if found, unless user confirms

6. If a specific task ID is provided (e.g., `T005`): jump directly to that task after verifying its dependencies are met

## Execution Loop

For each task (or a specific T-ID if provided):

1. Read task definition: `What / Where / Depends / Req / Tests / Gate / Done when`
2. Implement — guided by spec.md, plan.md, data-model.md, contracts/. No code inline in the skill.
   - Application code changes land in the **code repository**; specs/docs updates land in the **control repository**
3. Run gate command (e.g., `pnpm test guards`, `pnpm build`) in the code repo as appropriate
4. Verify "Done when" criteria
5. Run `/coe-code-review` for the Phase or `T00x` set just completed — **required before commit** when application code changed. Assessment must be `Ready to close? Yes` (Critical/Important fixed).
6. Mark `[x]` in tasks.md (control repo)
7. Atomic commit in the repo that owns the change; subject follows `coe-commit-pr-rule` (`type(scope): imperative summary`)

## Parallel Tasks `[P]`

Tasks marked `[P]` with no mutual dependencies can be delegated to sub-agents simultaneously.
Each sub-agent receives:
- Its specific task definition
- CONVENTIONS.md + TESTING.md
- Relevant spec context
- Target code repo path + feature branch name already ensured

Each sub-agent returns: Status · Files changed · Gate result · SPEC_DEVIATION markers.

## Failure Handling

| Failure | Action |
|---------|--------|
| Missing rule / layout / Git | Stop: `"Execute coe-sdd-init first."` |
| Code repo not in map | Stop: update rule + PROJECT.md, then retry |
| Branch checkout blocked (dirty tree) | Stop on pre-check; do not start tasks |
| Current branch ≠ resolved `BRANCH` / outside Git pattern / env branch (`main`, `master`, `prod`, `hml`, …) | Stop: blocked message above; do not start tasks |
| Gate fails | Stop on task, report error, suggest debug approach. No auto-fix attempt. |
| Dependency not satisfied | Stop and identify the blocking task. |
| Spec deviation detected | Mark `SD-NNN: SPEC_DEVIATION` in STATE.md with reason; continue; user decides whether to update spec. |

## Milestone Completion

After all tasks are marked `[x]`:
1. Update ROADMAP.md:
   - Milestone with Features: mark the implemented feature as `COMPLETED`; mark the milestone itself `✅ done` only when all its features are COMPLETED
   - Scope-only milestone: mark the milestone `✅ done` directly
2. Update STATE.md:
   - Add lessons learned
   - Note any `SD-NNN` spec deviations
   - Close any blockers resolved during implementation

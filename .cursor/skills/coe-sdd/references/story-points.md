# story-points — Estimating User Stories

## When to Apply

During `coe-sdd-plan` FASE 1 (Spec), right after each User Story is drafted, before the ambiguity scan.

## What Story Points Measure

Story points (SP) estimate **relative effort** — not hours, not complexity alone. Effort combines three factors (CUE):

| Factor | Question |
|--------|----------|
| **Complexity** | How technically hard is it (validations, rules, edge cases, interactions between fields)? |
| **Uncertainty / risk** | How unclear is the requirement? How fragile/unknown is the code touched? |
| **Effort (volume)** | How much concrete work is there to do, end to end (incl. tests to satisfy Definition of Done)? |

SP are **unit-less and relative**: a 5-point US is roughly twice a 3-point US and about half an 8-point US. Never equate a point value to a fixed number of hours.

## Scale

Fibonacci: `1, 2, 3, 5, 8, 13, 21`.

The growing gaps between numbers reflect that larger, less-understood work carries more uncertainty — don't debate `6` vs `7`; choose between `5` and `8`.

| SP | Typical shape |
|----|---------------|
| 1–2 | Trivial CRUD, single field/flag, no new integration |
| 3 | Standard CRUD or UI flow with validation, no new integration |
| 5 | New integration (auth, external service) or moderate cross-file change |
| 8 | Multiple integrations, non-trivial state machine, or notable unknowns |
| 13 | Large scope with real uncertainty — candidate for split |
| 21 | Too big — always split before tasks are generated |

## Split Rule

**SP ≥ 13** → before generating `tasks.md`, propose splitting the User Story into two or more independently testable/deliverable stories. Proceed unsplit only if the user explicitly confirms after seeing the proposed split.

## Estimating in the Pipeline

1. Read this file once per `coe-sdd-plan` run (FASE 1).
2. For each User Story, weigh the three CUE factors against the table above and assign the closest Fibonacci value.
3. If SP ≥ 8, add a one-sentence rationale under the US (what drives the size — new integration, unclear requirement, large surface area).
4. If SP ≥ 13, trigger the Split Rule above.
5. Never estimate SP for `INFRA` tasks, Phase 1/2 (Setup/Foundational), or Polish/cross-cutting work — these are not product User Stories.
6. Record the value directly in `spec.md` under each US (`**Story points:** [N]`). This is the single source of truth — `plan.md` and `tasks.md` only echo it.

## Anti-Patterns

- Converting SP to hours (`1 SP = X hours`) or back.
- Assigning SP to individual tasks (`T00x`) instead of the parent US.
- Comparing velocity or SP scales across different teams/projects.
- Assigning SP to `INFRA` work or cross-cutting polish.
- Treating SP as a productivity metric for individuals.

## Jira Mapping

Aligned with `coe-jira-integration`:

- SDD Milestone → Jira **Epic** (identity via Epic + `[MN]` in summary/labels; no SP rollup at Epic level).
- `US-N` in `spec.md` → Jira **Story** / História, carries the SP value; summary includes milestone + feature slug.
- `## Phase N` in `tasks.md` → Jira **Sub-task**, no SP field; `T00x` lines stay as checklist in the Subtask description (not issues).

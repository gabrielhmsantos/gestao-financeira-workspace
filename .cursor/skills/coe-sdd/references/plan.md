# coe-sdd-plan — Plan Feature

**Trigger:** `coe-sdd-plan MN` or `coe-sdd-plan MN feature-name`

## Pre-checks

1. `ROADMAP.md` exists? → if not: `"Execute coe-sdd-init first."`
2. Milestone dependencies complete?
   - Example: M1 depends on M0 → if M0 status ≠ `✅ done`, warn and request confirmation
   - If user confirms out-of-order planning: record `AD-NNN: antecipated planning of MN — risk of incomplete deps` in STATE.md
3. Scope resolution — check ROADMAP.md for MN:
   - Milestone **with** `### Features`:
     - If `feature-name` provided: verify it exists under MN → if not found, list available features and stop
     - If no `feature-name` provided: list the features defined under MN and ask the user which one to plan
   - Milestone **without** `### Features` (scope-only): plan the milestone as a single unit directly — no feature selection needed; output folder slug derived from the milestone name
4. Foundation available? → load the four files from `.specs/foundation/`

## Planning Unit

Each `coe-sdd-plan` invocation produces **exactly one output folder** under `.specs/features/`:

- Milestone with `### Features` → one folder per feature: `.specs/features/{MN}-{feature-slug}/`
- Milestone without `### Features` (scope-only) → one folder for the whole milestone: `.specs/features/{MN}-{milestone-slug}/`

**Folder naming:** `{MN}-` prefix is mandatory. Slug in kebab-case derived from the feature name (or milestone name for scope-only). Examples: `M1-authentication-session`, `M0-bootstrap`.

**Anti-pattern — never do this:** creating a single folder (e.g. `M1-auth-access-control/`) that consolidates multiple entries listed under `### Features` of the same milestone.

## Artifact Selection First

Before generating any artifact: evaluate which conditional artifacts apply (see [artifact-selection.md](artifact-selection.md)).
Announce what will be generated and what will be omitted — with justification. Ask for confirmation.

---

### FASE 0 — Research

Generate `research.md` when:
- A significant technical decision must be made (new library, architectural pattern, integration approach)
- Spec has `[NEEDS CLARIFICATION]` markers on technical points

Format of each decision in `research.md`:
```
## Decision: [topic]
**Chosen:** [option]
**Rationale:** [why]
**Alternatives rejected:** [option A — reason; option B — reason]
```

---

### FASE 1 — Spec

1. Read `.specs/_templates/spec-template.md`
2. Generate `spec.md` filling feature-level placeholders:
   - User stories P1/P2 with Given/When/Then acceptance scenarios
   - FR-* references (traceable to foundation RF-*)
   - BR-* references
   - Edge cases
   - Out of scope
3. Read [story-points.md](story-points.md) and assign a Fibonacci story point (`1|2|3|5|8|13|21`) to each product User Story:
   - SP ≥ 8 → add a one-sentence rationale under the US
   - SP ≥ 13 → propose a split into smaller US before continuing; proceed unsplit only with explicit user confirmation
   - `INFRA` work and Polish/cross-cutting items get no SP
4. Run **ambiguity scan** across 10 categories (see [clarify.md](clarify.md)):
   - High/Critical ambiguities → trigger clarify loop (up to 5 questions, one at a time)
   - No ambiguities → proceed without interruption
5. Generate `checklists/requirements.md` from checklist template (max 1 fix iteration)

---

### FASE 2 — Design

1. **Constitution Check (pre-design):**
   Verify milestone scope aligns with Core Principles.
   Violation → document as `AD-NNN: CONSTITUTION VIOLATION` in STATE.md; must be justified before proceeding.

2. Read `.specs/_templates/plan-template.md`
3. Generate `plan.md`:
   - Summary (feature + technical approach)
   - Story Points table — echo SP per US from `spec.md` (spec.md is the source of truth; never re-estimate here)
   - Technical context (stack, deps, storage, testing, constraints)
   - Constitution Check section (pre + post results)
   - Project structure (docs + source code layout)

4. Generate `data-model.md` if new or changed entities / tables / schema:
   - Entities with fields, types, validations
   - Enums with values (using project domain language convention from foundation)
   - State transitions (if applicable)
   - Relationships

5. Generate `contracts/` if the milestone exposes an interface to the outside:
   - Scope: internal or public API, CLI commands, event schemas, UI contracts
   - Use OpenAPI 3.0 format for HTTP APIs; use appropriate contract format for other types
   - Skip only if the milestone is purely internal (build scripts, config changes, migrations with no interface change)

6. Generate `context.md` only if `discuss` was explicitly triggered
   (architectural/UX gray areas debated with user — distinct from clarify, which is automatic)

7. **Constitution Check (post-design):**
   Verify data-model, contracts, and plan don't introduce violations.
   Same handling: violation = block + STATE.md entry + justification required.

---

### FASE 3 — Tasks

1. Read `.specs/_templates/tasks-template.md`
2. Generate `tasks.md` (unified format):
   - Header (milestone, status, depends on, foundation refs, tests policy)
   - Execution graph (dependency diagram)
   - Each User Story phase header echoes its SP from `spec.md` — never invent or re-estimate SP per task
   - Task table: `Task | O que fazer | Onde | Depende | Req | Tests | Gate`
   - "Done when" section for critical tasks
   - Execution order + parallelizable tasks + MVP scope
3. Generate `quickstart.md` if non-trivial E2E or manual validation is needed:
   - Prerequisites, setup commands, test/run commands, expected outcomes

---

### FASE 4 — State Update

1. STATE.md: add `AD-NNN` for relevant architectural decisions made during planning
2. ROADMAP.md:
   - Milestone with Features: update the feature's status from `NOT STARTED` → `PLANNED` and add a link to its folder (e.g. `PLAN ✅ → .specs/features/M1-authentication-session/`)
   - Scope-only milestone: mark the milestone block as `PLANNED` with a link to the folder

---

### Gate Opcional: Analyze

Trigger explicitly: `"analyze M1"`, `"check consistency"`, `"validate before implement"`
See [analyze.md](analyze.md).

CRITICAL issues from analyze → block `coe-sdd-implement` until resolved.

---

## Out-of-Order Protection

```
⚠️  MN depends on M(N-1) (status: not started).
    Are you sure you want to plan [feature-name] in MN now? (yes/no)
```

- Yes → record AD-NNN in STATE.md and proceed
- No → stop

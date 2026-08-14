# CONSTITUTION.md — Generation and Amendment

## Generation (coe-sdd-init)

Read `coe-sdd/templates/constitution-template.md` (base template from the skill).
Fill all `[ALL_CAPS]` placeholders with content extracted from foundation files.
**No placeholder may remain unfilled** — use `TODO(<FIELD>)` only if information is genuinely unavailable.

### Required Sections

| Section | Content |
|---------|---------|
| **Core Principles** | Principles MUST with name, non-negotiable rules, explicit rationale (derived from BR-*/PRD). Each: declarative, testable, no vague "should" — use MUST/SHOULD with justification |
| **Technology & Architecture Constraints** | Table per layer (frontend, backend, storage, infra, observability) + mandatory patterns (entity fields, soft delete, audit_logs, pagination, monetary formats, enums, code language) |
| **Development Workflow & Quality Gates** | Spec→plan→tasks flow, test expectations (unit/integration/e2e per scope), review gate checklist (foundation alignment, RBAC, audit, glossary, MVP scope) |
| **Governance** | Authority hierarchy, amendment process (semver MAJOR/MINOR/PATCH), Sync Impact Report |

### Authority Hierarchy (record in constitution)

```
1. CONSTITUTION.md
2. .specs/foundation/ (PRD, BUSINESS-RULES, GLOSSARY, STACK)
3. .specs/features/MN-{feature-slug}/ (specs, plans, tasks per feature, grouped by milestone in ROADMAP.md)
4. Project code
```

### Sync Impact Report

Add as HTML comment at the top of CONSTITUTION.md:

```html
<!--
SYNC IMPACT REPORT
Version: 1.0.0
Date: YYYY-MM-DD
Principles added: [list]
Templates affected: spec-template ✅ | plan-template ✅ | tasks-template ✅ | checklist-template ✅
TODOs: [field — reason, or "none"]
-->
```

### Validation Before Saving

- All principles: MUST/SHOULD declarative, testable
- Dates: ISO format (YYYY-MM-DD)
- No `[ALL_CAPS]` tokens remaining (except inside code blocks)
- No vague "should try to" language

## Amendment (coe-sdd-init --amend)

Triggered when the agent detects:
`"adicionar novo princípio"`, `"mudamos o stack"`, `"amend project rules"`, `"esse princípio precisa mudar"`

### Semver Rules

| Type | When | Bump |
|------|------|------|
| MAJOR | Removal or incompatible redefinition of principle | 1.0.0 → 2.0.0 |
| MINOR | New principle or section added | 1.0.0 → 1.1.0 |
| PATCH | Clarification, typo, non-semantic refinement | 1.0.0 → 1.0.1 |

### Amendment Steps

1. Update `CONSTITUTION.md` (increment semver in version field and Sync Impact Report)
2. Generate new Sync Impact Report (list changed principles, affected templates)
3. Update `.specs/_templates/*.md` for affected templates
4. Warn which milestones generated before this amendment may need revision — do not auto-modify generated milestone artifacts

## Constitution Check (in coe-sdd-plan)

Run at two points in every `coe-sdd-plan MN`:

| Point | What to check |
|-------|---------------|
| **Pre-design (Fase 0)** | Milestone scope aligns with Core Principles |
| **Post-design (Fase 2)** | data-model, contracts, and plan don't introduce violations |

**Violation handling:**
- Violation detected → error documented in STATE.md as `AD-NNN: CONSTITUTION VIOLATION — [principle] — [justification]`
- Blocks progress until user provides justification
- Justified → document exception and proceed

---
name: coe-jira-integration
description: >-
  Sync coe-sdd milestone specs to Jira (Epic → User Stories → Phase Subtasks),
  filling Story Points and SSG. Use when the user asks to send a milestone to
  Jira ("envie M0 para o Jira", "sync M1 Jira", "criar backlog no Jira",
  "coe-jira-integration"). Always discovers and validates the SSG field ID
  before creating any issues. Milestone identity is the Epic issue + [MN]
  in summaries/labels (no custom field).
---

# coe-jira-integration — Spec milestone → Jira backlog

Push a planned milestone (all `.specs/features/{MN}-*/` folders) into Jira with a fixed hierarchy and mandatory SSG field discovery.

## Hard rules

1. **Never call `createJiraIssue` until the SSG field is identified and shown to the user.** Also resolve Story Points when available on História.
2. User Story → Jira **História** (or Story). **Phase** (`## Phase N` in `tasks.md`) → **Subtask**. `T00x` lines → checklist in the Subtask description — **never** separate issues.
3. Story Points live **only on the US**, never on Subtasks or INFRA. Source of truth: `spec.md` (`**Story points:** N`).
4. Do not hardcode `customfield_*` IDs across sites. Discover via create-meta every run.
5. If SSG cannot be uniquely resolved → **STOP**, report candidates, ask the user. Do not create.

## Triggers

- "Envie MN para o Jira"
- "Sync M1 / create backlog no Jira"
- Explicit `/coe-jira-integration` or skill attach

## Inputs (resolve in order)

| Input | Where |
|-------|--------|
| Milestone id | User message (`M0`, `M1`, …) |
| Spec artifacts | **All** folders `.specs/features/{MN}-*/` that have both `spec.md` and `tasks.md` (required). If none → STOP. |
| Optional feature slug | If the user names one feature, sync **only** that folder; still attach issues to the **single** Epic for the milestone |
| SSG value | DAS / project docs (`SSG123456` → numeric part if field is number) or ask user |
| Jira project | User key, else `getVisibleJiraProjects` (prefer non-example project) |

Optional: `plan.md`, ROADMAP row for Epic summary/description.

**Milestone in Jira** = the Epic issue type + `[MN]` in summaries/labels. Do not discover or fill a custom field for the SDD milestone id.

## Workflow

Copy and track:

```
Progress:
- [ ] 1. Load all MN-* feature folders (or the one named feature)
- [ ] 2. Resolve cloudId + project key
- [ ] 3. Discover issue types
- [ ] 4. FIELD GATE — identify SSG (+ SP)
- [ ] 5. Present field map + backlog plan — wait for confirm if SSG ambiguous
- [ ] 6. Create or reuse Epic for the milestone
- [ ] 7. Create US (História) under Epic (all folders / selected feature)
- [ ] 8. Create Phase Subtasks under each US
- [ ] 9. Create INFRA parent + Phase Subtasks (if any)
- [ ] 10. Verify SSG (+ SP) on one US; summarize links
```

### 1. Load artifacts

Glob `.specs/features/{MN}-*/`. For each folder with `spec.md` + `tasks.md`, read both.

**Feature slug:** folder name without the `{MN}-` prefix (e.g. `M1-tenant-provisioning` → `tenant-provisioning`; scope-only `M0-bootstrap` → `bootstrap`).

Build the tree:

| Spec | Jira |
|------|------|
| Milestone (ROADMAP title) | **1 Epic** for the whole milestone |
| Each product US in each `spec.md` | **História** under that Epic |
| INFRA / Setup / Foundational / Polish phases per folder | **1 Tarefa INFRA per feature** (if those phases exist) |
| Each `## Phase …` tied to a US | **Subtask** of that História |
| Each INFRA-class `## Phase …` | **Subtask** of that feature’s INFRA Tarefa |

**Phase detection:** headers `## Phase N: …` in `tasks.md`. Collect every `T00x` in that section until the next Phase header (or end). Those `T00x` become a checklist in the Subtask description — not issues.

Feature does **not** become an Epic.

### 2–3. Jira context

1. `getAccessibleAtlassianResources` → `cloudId`
2. `getVisibleJiraProjects` (`action: create`) → project key
3. `getJiraProjectIssueTypesMetadata` → resolve type names:

| Role | Prefer (PT/EN) |
|------|----------------|
| Epic | Epic |
| User Story | História / Story |
| Infra parent | Tarefa / Task |
| Phase | Subtask / Sub-task |

**Reuse Epic:** before create, search JQL for an existing Epic with summary starting `[MN]` (and/or label `MN`). Reuse if found; otherwise create.

### 4. FIELD GATE (mandatory before create)

Follow [field-discovery.md](references/field-discovery.md).

Using Atlassian MCP:

1. `getJiraIssueTypeMetaWithFields` on **História/Story** and **Epic** with `requiredFieldsOnly: false`.
2. Match **SSG** by field **name** (and schema) — see discovery doc.
3. Resolve Story Points field (recommended; fill on every US).

**Gate checklist — all required before any create:**

```
Field gate:
- [ ] SSG fieldId + name + schema.type identified
- [ ] SP fieldId identified (or explicit note: unavailable on this issue type)
- [ ] Value coercion plan recorded (number vs string vs option id)
```

Present to the user **before creating**:

```
Campos identificados (projeto KEY):
| Papel        | Nome exibido           | fieldId            | Tipo   | Valor a gravar |
|--------------|------------------------|--------------------|--------|----------------|
| SSG          | Projeto SSG            | customfield_#####  | number | 123456         |
| Story Points | Story point estimate   | customfield_#####  | number | (por US)       |
```

If SSG is missing or ambiguous → **stop**. Do not invent labels as substitutes for SSG.

### 5. Confirm backlog shape

Show planned Epic / US (+ SP) / Phase Subtask counts (per feature). Proceed when SSG is clear (user already asked to send → create after a clear field table). If multiple SSG candidates, wait for user pick.

### 6–9. Create order

Always: **Epic → parents (US / INFRA) → Phase Subtasks**.

Set via `additional_fields` on create (and `editJiraIssue` if create ignores a field):

| Issue | parent | SP | SSG |
|-------|--------|----|-----|
| Epic | — | no | yes |
| História (US) | Epic | yes (from spec) | yes |
| Tarefa (INFRA) | Epic | no | yes |
| Subtask (Phase) | US or INFRA | no | no* |

\*Skip SSG on Subtasks unless the project requires them.

**Summaries:**

- Epic: `[MN] <ROADMAP title>`
- US: `[MN] <feature-slug> / US-0N — <title>`
- INFRA: `[MN] <feature-slug> / INFRA`
- Subtask: `Phase N — <phase title>` (e.g. `Phase 1 — Setup`)

**Descriptions:**

- US: story + acceptance from `spec.md` + path to feature folder
- Subtask: phase purpose + checklist of `T00x` (What / Where / Depends / Gate / FR from `tasks.md`)

Labels (optional): `MN`, `<feature-slug>`, `US-0N` / `INFRA`.

### 10. Verify + summarize

`getJiraIssue` on one US with SSG and SP fieldIds. Confirm values.

Return:

- Epic link
- Each US with SP + Phase Subtask keys (grouped by feature)
- INFRA + Phase Subtasks
- Field map used (fieldId + values)

## MCP tools

Prefer Atlassian MCP: `getAccessibleAtlassianResources`, `getVisibleJiraProjects`, `getJiraProjectIssueTypesMetadata`, `getJiraIssueTypeMetaWithFields`, `createJiraIssue`, `editJiraIssue`, `getJiraIssue`, `searchJiraIssuesUsingJql`.

Call `GetMcpTools` for the Atlassian server before first create in the session.

## Anti-patterns

- Creating issues before the SSG (+ SP) field table is resolved
- Hardcoding field IDs from a previous project/site
- Putting SP on Subtasks or INFRA
- Mapping `T00x` as Subtasks or top-level Stories
- Creating one Epic per Feature (Epic is always the milestone)
- Discovering or filling a custom field for the SDD milestone id
- Skipping INFRA phases silently (include under INFRA parent)
- Syncing only one feature folder when the user asked for the whole milestone (without them naming a feature)
- Creating when no `{MN}-*` folder has both `spec.md` and `tasks.md`

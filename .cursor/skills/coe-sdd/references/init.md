# coe-sdd-init — Initialize Project

## Mode detection (first)

Determine **greenfield** vs **brownfield** before any foundation gate.

**Brownfield** if any of:

- Explicit intent: `"map this codebase"`, `"analyze existing code"`, `"temos um projeto existente"`, `"quero mapear antes de inicializar"`, `"quero mapear antes de planejar"`, `"brownfield"`
- Heuristic: application code exists in the workspace (e.g. `package.json`, `src/`, or a code repo under layout shapes A/B/C) **and** `.specs/project/PROJECT.md` does **not** exist yet

Otherwise → **greenfield**.

Announce the chosen mode to the user before continuing.

## Brownfield path (no foundation gate)

If mode is brownfield:

1. Run [brownfield.md](brownfield.md) **first** — produce `.specs/codebase/` (required docs). Does **not** require `.specs/foundation/`.
2. Skip the greenfield foundation pre-condition entirely.
3. Continue with Steps 1–9 below using **brownfield sources** (see Step 1).
4. After layout (steps 7–9), seed the code-repositories map from discovered roots under the chosen layout — still without asking for folder names.
5. If foundation files exist (full or partial), use them only to **enrich** PROJECT / ROADMAP / CONSTITUTION. Never generate foundation in init (`foundation-docs` owns that).

## Greenfield path (foundation required)

If mode is greenfield:

`.specs/foundation/` must contain all four canonical files:
`PRD.md` · `BUSINESS-RULES.md` · `GLOSSARY.md` · `STACK.md`

If any is missing: alert the user and stop. Do not generate foundation files — they are external input (use `foundation-docs` if the user wants them created).

Then continue with Steps 1–9 using foundation as the primary source.

## Steps

**1. Read primary sources**

- **Greenfield:** load all four foundation files. Extract vision, goals, users, stack, milestones, BR-*, RF-*, glossary, constraints.
- **Brownfield:** load `.specs/codebase/` (STACK, ARCHITECTURE, CONVENTIONS, TESTING, plus optionals). Also load secondary docs when present: README, `AGENTS.md`, `CLAUDE.md`, legacy `specs/`, package manifests. If any foundation files exist, load them as enrichment only.

**2. Generate `.specs/project/PROJECT.md`**

Read `coe-sdd/templates/project-template.md`.
Fill `[ALL_CAPS]` placeholders from the primary sources of the active mode.
Leave **Workspace layout** placeholders for step 8 (or fill after layout is chosen — see step 8).
Do NOT invent a product narrative that contradicts observed code/docs.
Size limit: 2,000 tokens.

**3. Generate `.specs/project/ROADMAP.md`**

Read `coe-sdd/templates/roadmap-template.md`.
Fill placeholders from primary sources.
Greenfield: include M0 (bootstrap).
Brownfield: omit M0 or mark `✅ done` if infra already exists (see [brownfield.md](brownfield.md) — M0 rules).
Size limit: 3,000 tokens.

**4. Generate `.specs/project/CONSTITUTION.md`**

Full constitution — not a lightweight version.
See [constitution.md](constitution.md) for the complete generation process.
Brownfield: ground principles in observed CONVENTIONS / ARCHITECTURE / TESTING; do not require foundation.

**5. Initialize `.specs/project/STATE.md`**

Read `coe-sdd/templates/state-template.md`.
Initialize with empty sections — no AD-NNN, B-NNN, or L-NNN entries yet.
Set `Last Updated` to today's date. Set `Current Work` to `"Project initialization"`.

**6. Generate `.specs/_templates/`**

Read feature/project base templates from the skill (`spec-template.md`,
`plan-template.md`, `tasks-template.md`, `data-model-template.md`,
`checklist-template.md`). **Do not** copy:
- `codebase-*-template.md` — brownfield-only sources for [brownfield.md](brownfield.md) → `.specs/codebase/`
- `coe-sdd-rule-template.md` — IDE rule only (step 9); not copied into `.specs/_templates/`

Fill project-level placeholders from primary sources + CONSTITUTION:
- Stack (from foundation STACK or codebase STACK)
- Project conventions (from BUSINESS-RULES / CONVENTIONS / STACK)
- Constitution principles
- Canonical glossary terms when available (omit or mark TBD if brownfield has no glossary)

Leave milestone-level placeholders intact:
`[FEATURE_NAME]`, `[MILESTONE]`, `[DEPENDS_ON]`, `[ENTITIES]`, `[DATE]`, `[CODE_STRUCTURE]`, `[FOUNDATION_REFS]`

Write to `.specs/_templates/`:
- `spec-template.md`
- `plan-template.md`
- `tasks-template.md`
- `data-model-template.md`
- `checklist-template.md`

> After this step, all subsequent **plan/feature** commands read `.specs/_templates/` —
> never the skill's `templates/` folder directly. Brownfield mapping still reads
> `codebase-*-template.md` from the skill. IDE rule generation (step 9) still reads
> `coe-sdd-rule-template.md` from the skill.

**7. Choose workspace layout (control + code repos)**

Invariant: this workspace is the **control repository** (specs / SDD). Application code lives in separate **code repositories**.

Present the Modelo Operacional layouts and ask the user to pick **only** A, B, or C — do **not** ask for real folder names:

| Code | Name | Shape |
|------|------|--------|
| **A** | Submodule at root | `workspace/<app>/` |
| **B** | Grouping folder | `workspace/repositories/{frontend,backend,libs}/` |
| **C** | By domain | `workspace/repositories/{produto-a,produto-b}/` |

Wait for the user's choice before continuing.

**8. Document layout in PROJECT.md + confirm Git pattern**

Update the **Workspace layout** section in `.specs/project/PROJECT.md`:
- Record adopted layout code + name
- Include the maintenance note (update PROJECT.md + IDE rule as soon as repos are known/discovered; again before implement on new ones)
- Optionally list code repos already present on disk under the chosen shape; do not interview the user for names

Propose feature-branch naming (aligned with `coe-commit-pr-rule` types):

- Pattern: `{type}/{feature-folder}`
- Default type: `feat`

Ask the user to confirm (or provide an alternate pattern / default type). Do **not** create any git branch.

**9. Generate IDE context file (rule)**

Detect IDE/agent and generate the context file from `coe-sdd/templates/coe-sdd-rule-template.md`.
See [workspace-rule.md](workspace-rule.md).

Fill layout + Git placeholders from steps 7–8. Include any known code-repo rows; omit empty placeholder rows.

## Output

```
.specs/project/
├── PROJECT.md          ← includes Workspace layout (A|B|C)
├── ROADMAP.md
├── CONSTITUTION.md
└── STATE.md

.specs/codebase/        ← brownfield only (from brownfield.md)
├── STACK.md · ARCHITECTURE.md · CONVENTIONS.md · TESTING.md
└── … optional

.specs/_templates/
├── spec-template.md
├── plan-template.md
├── tasks-template.md
├── data-model-template.md
└── checklist-template.md
```

Plus IDE context file generated from the skill rule template (see workspace-rule.md) — **not** installed from the product ZIP as the source of truth (init regenerates/overwrites with layout + Git).

## Order Protection

After init, `coe-sdd-plan MN` that runs before ROADMAP.md exists must fail with:
> `"Execute coe-sdd-init first."`

`coe-sdd-implement` that runs without an IDE rule containing layout + `## Git` must fail with the same message (see [implement.md](implement.md)).

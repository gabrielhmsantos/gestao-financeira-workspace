# coe-sdd-init --brownfield — Codebase Mapping

## Foundation

**Does not require** `.specs/foundation/` (`PRD.md`, `BUSINESS-RULES.md`, `GLOSSARY.md`, `STACK.md`).

Init in brownfield mode must **not** stop for missing foundation. Mapping the codebase is enough to proceed to PROJECT / ROADMAP / CONSTITUTION. Generating foundation remains the job of the separate `foundation-docs` skill — never invent foundation files here.

If foundation files already exist (full or partial), init may **enrich** project artifacts with them after mapping; still do not require them to start.

## When Activated

The agent detects brownfield intent:

- `"map this codebase"`, `"analyze existing code"`
- `"temos um projeto existente"`, `"quero mapear antes de planejar"`, `"quero mapear antes de inicializar"`
- `"brownfield"` as standalone intent

Or via **heuristic** from [init.md](init.md): application code present and `.specs/project/PROJECT.md` missing.

Can be triggered as part of `coe-sdd-init` (always first on the brownfield path) or as a standalone step before initialization.

## Handoff to init

After required codebase docs exist under `.specs/codebase/`:

1. Return to [init.md](init.md) Steps 1–9 (brownfield sources).
2. Primary input = `.specs/codebase/` plus secondary sources below.
3. Init may complete layout + Git + IDE rule without foundation.

## Secondary sources (accepted)

Use when present to enrich mapping and later PROJECT / ROADMAP / CONSTITUTION — do not require all of them:

- `README.md` / `README` at workspace or code-repo roots
- `AGENTS.md`, `CLAUDE.md`, Cursor project rules
- Legacy Speckit / docs trees (e.g. `specs/` outside `.specs/`)
- Package manifests (`package.json`, lockfiles, `pyproject.toml`, etc.)
- Existing CI / build configs (gate commands for TESTING.md)

## Source templates (bundled)

Read structure from the skill templates — same idea as foundation-docs. Do **not**
invent ad-hoc doc shapes.

| Output (`.specs/codebase/`) | Template |
|-----------------------------|----------|
| `STACK.md` (required) | `coe-sdd/templates/codebase-stack-template.md` |
| `ARCHITECTURE.md` (required) | `coe-sdd/templates/codebase-architecture-template.md` |
| `CONVENTIONS.md` (required) | `coe-sdd/templates/codebase-conventions-template.md` |
| `TESTING.md` (required) | `coe-sdd/templates/codebase-testing-template.md` |
| `STRUCTURE.md` (optional) | `coe-sdd/templates/codebase-structure-template.md` |
| `INTEGRATIONS.md` (optional) | `coe-sdd/templates/codebase-integrations-template.md` |
| `CONCERNS.md` (optional) | `coe-sdd/templates/codebase-concerns-template.md` |

For each doc written:

1. Read the matching template.
2. Replace every `[placeholder]` with observed facts from the codebase.
3. Remove unused optional sections and HTML guidance comments.
4. Never leave placeholders or template comments in the final file.

These `codebase-*-template.md` files are **brownfield-only** — never copy them into
`.specs/_templates/`.

## Output: `.specs/codebase/`

| Document | Content | Required |
|----------|---------|----------|
| `STACK.md` | Languages, frameworks, observed versions | Yes |
| `ARCHITECTURE.md` | Folder structure, patterns, modules, layers | Yes |
| `CONVENTIONS.md` | Naming, patterns, formatting, import style | Yes |
| `TESTING.md` | How to test, gate commands, current coverage | Yes |
| `STRUCTURE.md` | Relevant folder tree | Optional |
| `INTEGRATIONS.md` | External services, existing contracts | Optional |
| `CONCERNS.md` | Technical debt, fragile areas, risks | Optional |

Generate all 4 required docs. Generate optional ones only if significant content is found
(otherwise omit the file entirely — do not write an empty stub).

## codenavi Integration

- **If `codenavi` is installed:** delegate code exploration to it; consume output to fill codebase docs
- **If not installed:** use native tools (`rg`, glob, AST inspection) with graceful degradation

## Depth Adaptation

Scale exploration depth to codebase size:
- Small (<20 files): complete analysis
- Medium (20–200 files): focus on `src/`, `apps/`, `packages/` (skip build artifacts, lock files)
- Large (200+ files): sample representative modules; flag areas needing deeper inspection in `CONCERNS.md`

## Impact on Subsequent coe-sdd-plan

After brownfield mapping, every `coe-sdd-plan MN` automatically loads `TESTING.md` and `CONVENTIONS.md`,
ensuring tasks follow observed project patterns.

## M0 in Brownfield

When generating ROADMAP.md after brownfield:
- Infrastructure (CI, DB, scaffold) already exists → M0 status = `✅ done`
- Partial infrastructure → M0 status = `🔄 in progress` with note on what's missing
- No infrastructure → M0 status = `⬜ not started` as usual

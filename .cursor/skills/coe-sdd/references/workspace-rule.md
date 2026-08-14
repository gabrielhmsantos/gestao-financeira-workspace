# workspace-rule — IDE Context File

After layout + Git are confirmed in `coe-sdd-init`, generate the IDE context file from the skill template — **do not** ship a pre-filled rule in the product bundle.

## Detection Table

| IDE / Agent | File to create |
|-------------|----------------|
| Cursor | `.cursor/rules/coe-sdd-rule.mdc` |
| Claude (claude.ai, API) | `CLAUDE.md` |
| Codex, Antigravity, others | `AGENTS.md` |

## Detection Logic

1. Check for `.cursor/` directory → Cursor
2. Check for existing `CLAUDE.md` or Claude-specific markers → Claude
3. Default → `AGENTS.md` (most broadly compatible)

If uncertain, create `AGENTS.md`.

## Source Template

Read `coe-sdd/templates/coe-sdd-rule-template.md`.

Fill placeholders from the init session:

| Placeholder | Source |
|-------------|--------|
| `[LAYOUT_CODE]` | `A`, `B`, or `C` (user choice) |
| `[LAYOUT_NAME]` | Submodule at root / Grouping folder / By domain |
| `[GIT_PATTERN]` | Confirmed pattern (default `{type}/{feature-folder}`) |
| `[DEFAULT_TYPE]` | Confirmed default type (default `feat`) |
| `[CODE_REPO_PATH]` / `[STACK]` / `[RESPONSIBILITY]` | Optional rows for repos already on disk under the layout; omit empty rows — **do not ask the user for folder names** |

Preserve the mandatory **Maintenance** paragraph and the **Git** section from the template.

### Cursor (`.mdc`)

Write the filled template as-is (keep YAML frontmatter: `description`, `alwaysApply: true`).

### Claude / AGENTS.md

Omit the YAML frontmatter; keep the markdown body. Title may stay `# coe-sdd — Project Context`.

## Required Content (all variants)

The generated file MUST:

- Instruct the agent to use the `coe-sdd` skill for all spec-driven work
- Point to `.specs/` as the canonical output root
- Reference `.specs/project/PROJECT.md`, `ROADMAP.md`, `STATE.md`, and `CONSTITUTION.md`
- State that this workspace is the **control repository**
- Record adopted layout **A | B | C** and the code-repositories map
- Include the maintenance rule (update rule + PROJECT.md as soon as repos are known/discovered; again before implement on new ones)
- Include `## Git` with pattern and default type
- **Never** reference a specific feature, milestone, or sprint

## When Porting to Another Repository

Detect the environment again and create/update the correct file for the new control repo.
Do not carry over the file from a previous repository without re-running layout + Git confirmation.

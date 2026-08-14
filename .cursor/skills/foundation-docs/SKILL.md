---
name: foundation-docs
description: Fills the four SDD foundation docs (PRD, GLOSSARY, BUSINESS-RULES, STACK) in .specs/foundation/ from an input document and/or a grill-style interview. Self-contained — bundles its own templates, so it does not depend on .specs/foundation/templates/ existing. Use when the user asks to "preencher foundation", "gerar PRD/STACK/GLOSSARY/BUSINESS-RULES", "documentar a fundação do projeto", "fill foundation docs", or to bootstrap the foundation layer before spec-driven development.
disable-model-invocation: true
license: CC-BY-4.0
metadata:
  version: 1.0.0
---

# Foundation Docs

Generate or update the four SDD foundation docs from an input document and/or an
interview. Operates as the "layer 0" before feature-level spec-driven work.

Output language follows the bundled templates (pt-BR). Keep all four docs in the
same language and vocabulary.

## What it produces

Writes to `.specs/foundation/` (relative to the project root):

- `PRD.md`
- `GLOSSARY.md`
- `BUSINESS-RULES.md`
- `STACK.md`

## Source templates (bundled)

Read the structure from the templates inside this skill, not from the project:

- `templates/PRD.template.md`
- `templates/GLOSSARY.template.md`
- `templates/BUSINESS-RULES.template.md`
- `templates/STACK.template.md`

Each output doc is the corresponding template with every `[placeholder]` replaced
by real content and unused optional sections removed. Never leave placeholders or
HTML guidance comments in the final docs.

## Hard gate

Do NOT write any final doc until all three are true:

1. Context explored (input doc parsed and/or codebase checked).
2. Gaps, ambiguities, and conflicts resolved through the interview.
3. A summary of all four docs presented and the user approved it.

## Interview style

Adopted from grill-me, grill-with-docs, and brainstorming:

- One question at a time, each with a recommended answer.
- Explore the input doc / codebase to answer a question instead of asking, whenever the answer already exists.
- Sharpen ambiguous or overloaded terms on the spot and propagate the agreed term into the GLOSSARY immediately.
- When the user uses a term that conflicts with an already-agreed term, call it out before continuing.

## Workflow

Copy this checklist and track progress:

```
Foundation Progress:
- [ ] Phase 1: Detect state (existing docs + input doc)
- [ ] Phase 2: Parse input (pre-fill drafts, mark gaps)
- [ ] Phase 3: Interview by doc (PRD -> GLOSSARY -> BUSINESS-RULES -> STACK)
- [ ] Phase 4: Cross-doc consistency pass
- [ ] Phase 5: Approval + write
```

### Phase 1: Detect state

- Check whether any of the four docs already exist in `.specs/foundation/`.
  - If they exist, ask the user which mode to use: **create from scratch**, **update incrementally**, or **abort**. Never overwrite silently.
- Determine whether the user provided an input document (file path, pasted text, or a linked doc). Record `has_input = yes/no`.

### Phase 2: Parse input (only if `has_input = yes`)

Follow [references/input-parsing.md](references/input-parsing.md): extract content,
pre-fill a draft for each of the four docs, and tag every section as
`[preenchido]`, `[lacuna]`, or `[conflito]`. With no input doc, start from empty
drafts based on the templates.

### Phase 3: Interview by doc

Follow [references/interview-guide.md](references/interview-guide.md). Go in domain
dependency order — **PRD -> GLOSSARY -> BUSINESS-RULES -> STACK** — asking only
about `[lacuna]` and `[conflito]` sections (ask everything when there is no input
doc). Apply the interview style above.

### Phase 4: Cross-doc consistency pass

Follow [references/validation.md](references/validation.md). Verify terms, roles,
RF/BR IDs, statuses, and that STACK does not contradict the PRD non-functional
requirements. Resolve every failure (ask or adjust) before Phase 5.

### Phase 5: Approval + write

Present a concise summary of all four docs (sections filled, key decisions, terms
sharpened). After the user approves, write the four files to `.specs/foundation/`,
replacing template placeholders and removing unused optional sections and guidance
comments.

## Out of scope (YAGNI)

- No automatic handoff to other SDD phases or skills.
- No generation of `.specs/project/` or `.specs/codebase/` docs.
- No silent overwrite and no automatic backups.

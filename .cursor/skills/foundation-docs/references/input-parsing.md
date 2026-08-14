# Input Parsing

How to turn an input document into pre-filled drafts of the four foundation docs.

## Accepted input

- A file path in the repo (read it).
- Pasted text in the conversation.
- A linked/attached doc the user provides.

If multiple inputs are given, merge them; on conflict, mark the section `[conflito]`
and resolve it in the interview.

## Process

1. Read the full input once and build a mental map of its content.
2. For each of the four docs, walk the template section by section and try to fill
   each section from the input.
3. Tag every section with exactly one status:
   - `[preenchido]` — confidently filled from the input; do not re-ask.
   - `[lacuna]` — missing or too vague; must be covered in the interview.
   - `[conflito]` — the input states contradictory things, or contradicts another doc.
4. Do not invent facts. If the input implies but does not state something, treat it
   as `[lacuna]` with a recommended answer rather than `[preenchido]`.

## Mapping hints

- Product summary, problem, goal, audience -> PRD top sections.
- Roles / personas / "quem usa" -> PRD `Usuários` AND GLOSSARY roles (keep identical).
- Feature lists, "must have" / "nice to have" -> PRD `Escopo do MVP` / `Fora do escopo`.
- Numbered/explicit system behaviors -> PRD `Requisitos funcionais macro` (assign RF IDs).
- Security, privacy, performance, audit, logging notes -> PRD `Requisitos não funcionais`.
- Domain nouns and their definitions -> GLOSSARY terms; flag synonyms under `Evitar usar`.
- "The system must / must not", invariants, lifecycle, status flows -> BUSINESS-RULES (assign BR IDs).
- Any technology choice (language, framework, DB, infra, integrations) -> STACK.
- Explicit "do not change / fixed" constraints -> STACK `Restrições para o SDD`.

## Output of this phase

A draft per doc with every section tagged, plus a short list of `[lacuna]` and
`[conflito]` items that drives the interview in
[interview-guide.md](interview-guide.md).

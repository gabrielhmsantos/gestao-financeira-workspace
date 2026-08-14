# Cross-Doc Validation

Run this pass after the interview and before writing the final docs. For each check
that fails, either ask the user or adjust the draft, then re-check.

## Checklist

```
Consistency Pass:
- [ ] Roles match between PRD "Usuários" and GLOSSARY
- [ ] Domain terms used in PRD/BUSINESS-RULES are defined in GLOSSARY
- [ ] Banned synonyms (GLOSSARY "Evitar usar") are not used elsewhere
- [ ] Official statuses match between GLOSSARY and BUSINESS-RULES BR-007
- [ ] RF IDs are sequential (RF-001..RF-NNN), no gaps or duplicates
- [ ] BR IDs are sequential (BR-001..BR-NNN), no gaps or duplicates
- [ ] STACK does not contradict PRD non-functional requirements
- [ ] STACK "Padrões obrigatórios" cover audit/archiving rules referenced by BUSINESS-RULES
- [ ] No placeholders ([...]) or guidance HTML comments remain
- [ ] Only one language used across all four docs
```

## Detail per check

- **Roles** — every role in PRD `Usuários` has a GLOSSARY entry with the same name, and vice versa.
- **Terms** — scan PRD and BUSINESS-RULES for domain nouns; each significant one is defined in the GLOSSARY. Add missing definitions or remove orphan terms.
- **Banned synonyms** — words listed under `Evitar usar` must not appear in any doc; replace with the canonical term.
- **Statuses** — the status list in GLOSSARY equals the status list in BR-007, and every transition in BR-007 uses only those statuses.
- **RF/BR IDs** — contiguous numbering starting at 001, no gaps, no duplicates; each is testable and independent.
- **STACK vs PRD non-functional** — e.g. if PRD requires audit, STACK must define where audit events live; if PRD requires pagination, STACK must list it; auth/authorization choices must satisfy PRD security.
- **Cleanliness** — no remaining `[placeholder]`, no `<!-- ... -->` guidance comments, unused optional sections removed.

## Resolution

- Prefer adjusting drafts for mechanical issues (renumbering IDs, replacing synonyms, removing comments).
- Ask the user only for genuine decisions (a missing status, a contradictory rule, an undefined-but-needed term), one question at a time with a recommended answer.

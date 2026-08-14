# clarify — Ambiguity Scan and Resolution

## When Triggered

**Automatically** during `coe-sdd-plan` Fase 1 (after initial spec.md draft), when High or Critical ambiguities are detected.

**Explicitly:**
`"clarify the spec"`, `"a spec tem ambiguidades"`, `"preciso esclarecer antes de planejar"`, `"quero revisar as dúvidas da spec"`

## Ambiguity Scan

Scan spec.md across 10 categories:

| Category | What to look for |
|----------|-----------------|
| Domain | Undefined business terms, missing BR-* references |
| UX / behavior | Unclear user flows, undefined states or transitions |
| Non-functional | Missing performance targets, undefined SLAs |
| Edge cases | Unhandled boundary conditions |
| Integration | Undefined external service contracts or error modes |
| Auth / RBAC | Undefined role permissions for new operations |
| Data | Ambiguous entity attributes, missing constraints |
| Error handling | Undefined error states or messages |
| Performance | Undefined load or latency expectations |
| i18n / locale | Undefined language, timezone, or currency behavior |

**Classify each finding:**
- **Critical** — cannot proceed without resolution (impacts core behavior or design)
- **High** — significant ambiguity (impacts design or test strategy)
- **Medium** — notable but resolvable with a reasonable assumption
- **Low** — minor; document assumption and proceed

## Clarify Loop

For Critical and High items:
1. Surface at most **5 questions**, **one at a time**
2. Wait for user response before next question
3. Integrate each answer directly into `spec.md`:
   - Update the relevant section with the resolved information
   - Add entry in `## Clarifications` section:

```markdown
## Clarifications

- **CL-001** [YYYY-MM-DD]: [original question] → [answer integrated]
- **CL-002** [YYYY-MM-DD]: [original question] → [answer integrated]
```

For Medium/Low: document assumption in `## Assumptions` section of spec.md. No interruption.

## Output

- Updated `spec.md` with:
  - Resolved ambiguities integrated into the relevant sections
  - `## Clarifications` section with CL-NNN entries
  - `## Assumptions` section for Medium/Low items
- No separate file generated — clarifications live in spec.md

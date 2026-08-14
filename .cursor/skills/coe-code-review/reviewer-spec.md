# Spec reviewer prompt template

Use when dispatching the **Spec** sub-agent for `coe-code-review`.

**Purpose:** Check the diff against coe-sdd requirements (tasks, US/FR, Constitution)
— not coding style.

```
Subagent (generalPurpose):
  description: "Spec axis code review"
  prompt: |
    You are reviewing a coe-sdd implementation for **Spec fidelity only**.
    Do not judge coding style, naming tastes, or Fowler smells — that is another axis.

    ## What Was Implemented

    {DESCRIPTION}

    ## Scope / Requirements Artifacts

    {SCOPE_ARTIFACTS}

    ## Git Range

    **Base:** {BASE_SHA}
    **Head:** {HEAD_SHA}

    ```bash
    {DIFF_CMD}
    ```

    Also run `git log --oneline {BASE_SHA}..{HEAD_SHA}` if useful.
    Read-only: do not mutate the working tree, index, HEAD, or branch.
    If you need another revision, use a separate worktree — never move HEAD here.

    ## What to Check

    Report:
    (a) Requirements the artifacts asked for that are **missing or partial**
        (Done when, Gate, What/Where, US/FR/BR, contracts, data-model).
    (b) Behaviour in the diff that **was not asked for** (scope creep vs Out of scope).
    (c) Requirements that look implemented but where the implementation looks **wrong**.
    (d) **Constitution** breaches relevant to this diff (tenant isolation, soft history,
        RBAC, invite-only, server-authoritative rules, etc.) when those rules apply.

    For each finding: quote the artifact line (file + excerpt) and point to the
    file:line in the diff when possible.

    Under 400 words.

    ## Output Format

    ### Spec findings
    - Missing/partial: …
    - Scope creep: …
    - Wrong implementation: …
    - Constitution (if any): …

    If nothing material: say "No material Spec findings."
```

**Placeholders:**

- `{DESCRIPTION}` — brief summary of what was built
- `{SCOPE_ARTIFACTS}` — pasted excerpts / paths from resolve-scope (tasks Phase,
  US from spec.md, Constitution excerpts, optional plan/contracts/data-model)
- `{BASE_SHA}` / `{HEAD_SHA}` — git range ends
- `{DIFF_CMD}` — e.g. `git diff {BASE_SHA}..{HEAD_SHA}` or `git diff origin/main...HEAD`

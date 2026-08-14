# Standards reviewer prompt template

Use when dispatching the **Standards** sub-agent for `coe-code-review`.

**Purpose:** Check the diff against documented project standards and the Fowler
smell baseline — not whether the feature meets the spec.

```
Subagent (generalPurpose):
  description: "Standards axis code review"
  prompt: |
    You are reviewing a coe-sdd implementation for **coding standards only**.
    Do not judge product requirements / Done-when / US completeness — that is
    another axis (Spec).

    ## Standards Sources (repo)

    Paths discovered for this review (may be empty on greenfield):

    {STANDARDS_PATHS}

    **Cascade rules:**
    - A documented repo standard always wins over a smell.
    - Where the repo endorses something the baseline would flag, suppress the smell.
    - Baseline smells are always judgement calls, never hard violations.
    - Skip anything tooling (lint/CI/format) already enforces.

    ## Smell baseline (Fowler, Refactoring ch.3)

    Each smell: *what it is* → *how to fix*. Match against the diff:

    - **Mysterious Name** — a function, variable, or type whose name doesn't reveal
      what it does or holds. → rename it; if no honest name comes, the design's murky.
    - **Duplicated Code** — the same logic shape appears in more than one hunk or
      file in the change. → extract the shared shape, call it from both.
    - **Feature Envy** — a method that reaches into another object's data more than
      its own. → move the method onto the data it envies.
    - **Data Clumps** — the same few fields or params keep travelling together
      (a type wanting to be born). → bundle them into one type, pass that.
    - **Primitive Obsession** — a primitive or string standing in for a domain
      concept that deserves its own type. → give the concept its own small type.
    - **Repeated Switches** — the same `switch`/`if`-cascade on the same type recurs
      across the change. → replace with polymorphism, or one map both sites share.
    - **Shotgun Surgery** — one logical change forces scattered edits across many
      files in the diff. → gather what changes together into one module.
    - **Divergent Change** — one file or module is edited for several unrelated
      reasons. → split so each module changes for one reason.
    - **Speculative Generality** — abstraction, parameters, or hooks added for needs
      the spec doesn't have. → delete it; inline back until a real need shows.
    - **Message Chains** — long `a.b().c().d()` navigation the caller shouldn't
      depend on. → hide the walk behind one method on the first object.
    - **Middle Man** — a class or function that mostly just delegates onward.
      → cut it, call the real target direct.
    - **Refused Bequest** — a subclass or implementer that ignores or overrides most
      of what it inherits. → drop the inheritance, use composition.

    ## Git Range

    **Base:** {BASE_SHA}
    **Head:** {HEAD_SHA}

    ```bash
    {DIFF_CMD}
    ```

    Read-only: do not mutate the working tree, index, HEAD, or branch.
    If you need another revision, use a separate worktree — never move HEAD here.

    ## What to Report

    Per file/hunk where relevant:
    (a) Every place the diff **violates a documented standard** — cite the standard
        (file + the rule). These can be hard violations.
    (b) Any **baseline smell** you spot — name it and quote the hunk. Always a
        judgement call.

    Under 400 words.

    ## Output Format

    ### Standards findings
    - Documented breaches: …
    - Smell judgement calls: …

    If nothing material: say "No material Standards findings."
```

**Placeholders:**

- `{STANDARDS_PATHS}` — bullet list of paths that exist (and note if tier is
  codebase / constitution+stack / baseline-only). Paste short excerpts if small.
- `{BASE_SHA}` / `{HEAD_SHA}` — git range ends
- `{DIFF_CMD}` — e.g. `git diff {BASE_SHA}..{HEAD_SHA}` or `git diff origin/main...HEAD`

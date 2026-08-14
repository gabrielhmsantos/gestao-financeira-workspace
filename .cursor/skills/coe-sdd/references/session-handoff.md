# Session Handoff — Pause & Resume

## coe-sdd-pause

**Trigger:** `"pause work"`, `"end session"`, `"vou parar por aqui"`

Generate `.specs/project/HANDOFF.md`:

```markdown
# Session Handoff

**Date:** [YYYY-MM-DD HH:MM]
**Milestone in progress:** [MN — name]
**Last completed task:** [T-ID — description]
**Next task:** [T-ID — description]
**Active blockers:** [B-NNN list or "none"]
**STATE.md summary:** [key recent decisions/deviations in 3–5 bullets]
**Context to load on resume:** [specific files beyond the base set, if any]
```

Also update STATE.md with any pending lessons or deferred ideas from the session.

## coe-sdd-resume

**Trigger:** `"resume work"`, `"continue"`, `"voltando ao projeto"`

1. Load HANDOFF.md + STATE.md + ROADMAP.md
2. Report current state in one message:
   - Active milestone and its status
   - Last completed task
   - Next task to execute
   - Open blockers
   - Critical recent decisions (last 3 AD-NNN)
3. Ask: `"Ready to continue from [next task]? (yes / or specify a different starting point)"`

## coe-sdd-status

**Trigger:** `"status"`, `"onde estamos"`, `"show roadmap"`, `"qual o progresso"`

Load ROADMAP.md + STATE.md. Report:
- All milestone statuses (emoji + name + brief note)
- Open blockers (B-NNN)
- Last 3 decisions (AD-NNN)
- Next planned action

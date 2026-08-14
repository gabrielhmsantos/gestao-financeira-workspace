# Field discovery — SSG and Story Points

Run on every sync. Never reuse IDs from memory alone.

## How to fetch

```
getJiraIssueTypeMetaWithFields(
  cloudId,
  projectIdOrKey,
  issueTypeId,          // História/Story AND Epic
  requiredFieldsOnly: false
)
```

Inspect each field’s `name`, `fieldId`, `schema.type`, `schema.custom`, and `allowedValues` (if any).

If create-meta omits a known field, cross-check with:

```
searchJiraIssuesUsingJql(..., fields: ["*all"])
getJiraIssue(..., fields: ["*all"])  // names/schema in expand when present
```

## SSG field

**Role:** project/solution code (e.g. SSG123456).

**Name match (case-insensitive), first unique hit wins:**

1. Exact / contains: `Projeto SSG`, `SSG`, `Código SSG`, `SSG Code`
2. Avoid: fields that are clearly Epic Name, Rank, Sprint, Story Points

**Typical schemas:**

| schema.type | How to write value |
|-------------|--------------------|
| `number` / float | Digits only from `SSG123456` → `123456` |
| `string` | Prefer full `SSG123456` unless project convention is digits-only |
| `option` | Match `allowedValues[].value` (exact or contains SSG code) → set `{ "id": "..." }` |

**Value source order:** DAS / `.specs/das/*` → PROJECT.md → ask user.

If **no** SSG field exists in create-meta for História **and** Epic:

1. STOP create
2. Tell the user the field is missing on the project
3. List closest name candidates (if any)
4. Ask them to add the field or point to the correct `customfield_*`

Do not invent a substitute (labels-only) unless the user explicitly says to proceed without SSG.

## Story Points (recommended)

**Name match:**

1. `Story point estimate`, `Story Points`, `Story points`, `Estimativa de pontos da história`, `SP`

**Schema:** usually `number` (`jsw-story-points`).

Set only on User Story (História). Fibonacci from `spec.md`.

If missing on História create-meta but present on existing issues, still try `additional_fields` / `editJiraIssue` with that fieldId.

## Ambiguity

| Situation | Action |
|-----------|--------|
| 0 matches for SSG | STOP + report |
| 2+ matches for SSG | List candidates; ask user to pick fieldId |
| Name match but wrong type | Show schema; ask how to coerce or pick alternate |
| Field on Epic only / História only | Prefer História for US; set SSG on Epic too when available |
| SP unavailable on História | Note explicitly; proceed with SSG only |

## Coercion cheat sheet

```
SSG123456 + number field  → 123456
SSG123456 + string field  → "SSG123456" (or digits if user/docs say so)
SP 5                      → 5
```

## Example (illustrative — rediscover each run)

On one GHMS Dev site the map was:

| Role | Name | fieldId |
|------|------|---------|
| SSG | Projeto SSG | `customfield_10170` |
| Story Points | Story point estimate | `customfield_10016` |

Treat the table above as a hint only. Re-run discovery every sync.

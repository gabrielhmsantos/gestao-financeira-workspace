# Interview Guide

Question bank for the foundation interview, anchored to the real sections of each
bundled template. Go in domain dependency order: **PRD -> GLOSSARY ->
BUSINESS-RULES -> STACK**.

## Cadence rules

- Ask **one question at a time** and wait for the answer before the next.
- Every question carries a **recommended answer** (your best guess given context).
- **Skip** any question already answered by the input doc (section tagged `[preenchido]`).
- Ask only about `[lacuna]` and `[conflito]` sections when an input doc exists; ask everything when there is none.
- **Sharpen terms inline.** When a term is vague, overloaded, or conflicting, resolve it now and write the agreed definition into the GLOSSARY draft immediately.
- **Explore instead of asking** when the answer is discoverable in the input doc or the codebase.

## PRD

Cover, in order:

1. **Produto** — name, one-line definition, who uses it vs. who interacts indirectly.
2. **Problema** — current pain, lost control, rework or risk.
3. **Objetivo** — the single main outcome the system enables.
4. **Público-alvo** — segments / org types / operational context.
5. **Usuários** — official roles for the MVP (one subsection each). These roles are canonical and must match the GLOSSARY.
6. **Escopo do MVP** vs **Fora do escopo** — force explicit exclusions.
7. **Capacidades principais** — one per functional domain.
8. **Requisitos funcionais macro** — assign `RF-001..RF-NNN`, each independent and testable.
9. **Requisitos não funcionais** — Segurança, Privacidade, Performance, Auditoria, Observabilidade (add others only if needed).
10. **Critérios de sucesso** — observable outcomes per user profile.

## GLOSSARY

Derive terms from the PRD; do not invent a parallel vocabulary.

1. **Entidade/conceito raiz** (org, tenant, etc.).
2. **Usuário** and each **papel** — must match PRD "Usuários".
3. **Entidade principal de negócio** + `Evitar usar` (ambiguous synonyms to ban).
4. **Entidade de processo** (atendimento, pedido, ticket, etc.).
5. **Responsável** — which records a user can be assigned to.
6. **Campo de estado / Status** — list the official statuses (must match BR-007).
7. **Classificador** (etiqueta, tag, categoria) + official examples.
8. **Unidade de trabalho, Notificação, Agenda, Visão agregada** — only if in scope.
9. **Arquivar** and **Auditoria** — operational meaning.

## BUSINESS-RULES

Use IDs `BR-NNN`, imperative titles, testable descriptions. Probe each area:

1. Uniqueness / data consistency within a scope.
2. History preservation (what must never be hard-deleted).
3. Archiving and its effect on related records.
4. Status lifecycle and allowed transitions (BR-007 — must match GLOSSARY statuses).
5. Partial immutability after a terminal state.
6. Cancellation / closure metadata (reason, responsible, date).
7. Auditable critical actions.
8. Permissions on reports / aggregated views (by role or ownership).
9. Domain / compliance limits (what the system explicitly does not decide).

## STACK

Fill only what exists in the MVP; remove non-applicable lines/sections.

1. **Modelo de repositório** — monorepo / multi-repo / other.
2. **Linguagem principal**.
3. **Frontend** — interface type, framework, styling, forms, client validation, remote state, routing, build (duplicate the block per client surface if web + mobile).
4. **Backend** — runtime, framework, API style, data format, validation, auth, authorization, contract docs, persistence.
5. **Banco de dados** — engine, access layer, identifiers, dates/timezone.
6. **Cache e filas** — remove if unused.
7. **Infraestrutura** — containers, runtime env, proxy/gateway, managed services, deploy model.
8. **Observabilidade** — server logs, client logs, metrics/tracing, healthcheck.
9. **Padrões obrigatórios** — entity field conventions, archiving, where critical rules live, validation boundary, API error format, pagination, audit events. Must align with PRD non-functional requirements and BUSINESS-RULES.
10. **Integrações do MVP** — confirmed only.
11. **Restrições para o SDD** — what later SDD phases must not change.

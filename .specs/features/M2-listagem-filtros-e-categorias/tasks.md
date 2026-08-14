---
description: "Tasks M2 — Listagem, filtros e categorias"
---

# Tasks: Listagem, filtros e categorias

**Marco:** M2 | **Status:** planejado | **Depende de:** M2-cadastro-e-ciclo-de-vida-da-despesa
**Foundation:** RF-005 · RF-009 · BR-010

## Grafo de execução

```
T001 → T002 → T003 → T004 → T005
```

---

## Fase 2–3

- [ ] T001 [INFRA] Query listExpenses (userId, archivedAt null, filtros, paginação) em `apps/web/src/server/queries/expenses.ts`
- [ ] T002 [US2] Expor catálogo (const + opcional action/route) labels pt-BR — SP 2 — em `apps/web/src/lib/domain/categories.ts`
- [ ] T003 [US1] UI `/despesas` com filtros período/categoria + paginação — SP 5 — em `apps/web/src/app/(app)/despesas/`
- [ ] T004 [US1] Testes integration filtros/paginação/isolamento em `apps/web/tests/`
- [ ] T005 [US1] E2E listagem + filtros em `apps/web/tests/e2e/`

## Resumo das tasks

| Task | US | O que fazer | Onde | Depende | Req | Tests | Gate |
|------|----|-------------|------|---------|-----|-------|------|
| **T001** | INFRA | query list | `server/queries/expenses.ts` | ciclo vida | FR-001–003,005,006 | integration | `npm test` |
| **T002** | US2 | catálogo UI/API | `lib/domain/categories.ts` | — | FR-004 | unit | `npm test` |
| **T003** | US1 | página listagem | `app/(app)/despesas/` | T001,T002 | FR-001–005 | e2e | `npx playwright test` |
| **T004** | US1 | testes integration | `tests/` | T001 | FR-001–006 | integration | `npm test` |
| **T005** | US1 | E2E | `tests/e2e/` | T003 | FR-001–004 | e2e | `npx playwright test` |

## Notas

- Branch: `feat/M2-listagem-filtros-e-categorias`
- Sem data-model novo (reusa Despesa)

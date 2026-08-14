---
description: "Tasks M3 — Resumo por período"
---

# Tasks: Resumo por período

**Marco:** M3 | **Status:** planejado | **Depende de:** M2 (ciclo de vida + listagem)
**Foundation:** RF-008 · BR-009 · BR-012 · BR-013

## Grafo de execução

```
T001 → T002 → T003 → T004 → T005
```

---

- [ ] T001 [INFRA] Query/agregação `getExpenseSummary` em `apps/web/src/server/queries/expense-summary.ts`
- [ ] T002 [US1] Server Action/loader + validação de período — SP 5 — em `apps/web/src/server/`
- [ ] T003 [US2] UI `/resumo` com total em evidência + breakdown — SP 2 — em `apps/web/src/app/(app)/resumo/`
- [ ] T004 [US1] Testes unit/integration (zero division, arquivadas excluídas, isolamento) em `apps/web/tests/`
- [ ] T005 [US1] E2E presets mês atual/anterior/personalizado em `apps/web/tests/e2e/`

## Resumo das tasks

| Task | US | O que fazer | Onde | Depende | Req | Tests | Gate |
|------|----|-------------|------|---------|-----|-------|------|
| **T001** | INFRA | aggregate summary | `queries/expense-summary.ts` | M2 | FR-001–003,005 | integration | `npm test` |
| **T002** | US1 | action/loader período | `src/server/` | T001 | FR-004 | integration | `npm test` |
| **T003** | US2 | UI resumo | `app/(app)/resumo/` | T002 | FR-001–006 | e2e | `npx playwright test` |
| **T004** | US1 | testes cálculo | `tests/` | T001 | FR-001–005 | unit | `npm test` |
| **T005** | US1 | E2E | `tests/e2e/` | T003 | FR-004 | e2e | `npx playwright test` |

## Notas

- Branch: `feat/M3-resumo-por-periodo`
- Sem gráficos; sem recomendações

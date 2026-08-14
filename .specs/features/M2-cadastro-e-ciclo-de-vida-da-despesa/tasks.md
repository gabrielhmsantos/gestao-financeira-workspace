---
description: "Tasks M2 — Cadastro e ciclo de vida da despesa"
---

# Tasks: Cadastro e ciclo de vida da despesa

**Marco:** M2 | **Status:** planejado | **Depende de:** M1 (auth + isolamento)
**Foundation:** RF-004 · RF-006 · RF-007 · BR-004–008 · BR-010 · BR-011

## Grafo de execução

```
T001 → T002 → T003 → T004 → T005
         ├──→ T006 [P] → T007
         └──→ T008 [P] → T009
T007,T009 → T010
```

---

## Fase 1–2: Fundação

- [ ] T001 [INFRA] Model `Expense` + migration + índices `(user_id)` em `apps/web/prisma/`
- [ ] T002 [INFRA] Catálogo de Categorias + Zod expense em `apps/web/src/lib/`
- [ ] T003 [INFRA] Extender auditoria `EXPENSE_*` em `apps/web/src/server/audit.ts`

---

## Fase 3: US-01 — Cadastrar (P1) — SP 5

- [ ] T004 [US1] Server Action create com ownership em `apps/web/src/server/actions/expenses.ts`
- [ ] T005 [US1] UI formulário nova Despesa em `apps/web/src/app/(app)/despesas/nova/`

---

## Fase 4: US-02 — Editar (P1) — SP 3

- [ ] T006 [P] [US2] Action update (só Ativa, só dono) em `apps/web/src/server/actions/expenses.ts`
- [ ] T007 [US2] UI edição em `apps/web/src/app/(app)/despesas/[id]/edit/`

---

## Fase 5: US-03 — Arquivar (P1) — SP 3

- [ ] T008 [P] [US3] Action archive (`archived_at`) em `apps/web/src/server/actions/expenses.ts`
- [ ] T009 [US3] Controle UI de arquivar + confirmação simples

---

## Fase 6: Polish

- [ ] T010 [US1] Testes integration + E2E create/edit/archive + cross-user 404 em `apps/web/tests/`

---

## Resumo das tasks

| Task | US | O que fazer | Onde | Depende | Req | Tests | Gate |
|------|----|-------------|------|---------|-----|-------|------|
| **T001** | INFRA | Schema Expense | `prisma/` | M1 | FR-001 | build | `npx prisma migrate deploy` |
| **T002** | INFRA | Catálogo + Zod | `src/lib/` | T001 | FR-001,007 | unit | `npm test` |
| **T003** | INFRA | Audit EXPENSE_* | `src/server/audit.ts` | T001 | FR-006 | unit | `npm test` |
| **T004** | US1 | create action | `actions/expenses.ts` | T002,T003 | FR-001,002 | integration | `npm test` |
| **T005** | US1 | UI nova | `despesas/nova/` | T004 | FR-001 | e2e | `npx playwright test` |
| **T006** [P] | US2 | update action | `actions/expenses.ts` | T004 | FR-003,005 | integration | `npm test` |
| **T007** | US2 | UI edit | `despesas/[id]/edit/` | T006 | FR-003 | e2e | `npx playwright test` |
| **T008** [P] | US3 | archive action | `actions/expenses.ts` | T004 | FR-004 | integration | `npm test` |
| **T009** | US3 | UI arquivar | UI despesas | T008 | FR-004 | e2e | `npx playwright test` |
| **T010** | US1 | suite E2E/integration | `tests/` | T005,T007,T009 | FR-* | e2e | `npx playwright test` |

## Notas

- Branch: `feat/M2-cadastro-e-ciclo-de-vida-da-despesa`
- Listagem filtrada: feature irmã

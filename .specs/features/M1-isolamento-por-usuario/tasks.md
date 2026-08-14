---
description: "Tasks M1 — Isolamento por usuário"
---

# Tasks: Isolamento por usuário

**Marco:** M1 | **Status:** planejado | **Depende de:** M1-autenticacao-e-sessao
**Foundation:** RF-003 · BR-003 · BR-012
**Política de testes:** integration two-user obrigatória; E2E smoke

## Grafo de execução

```
T001 → T002 → T003 → T004 → T005 → T006
```

---

## Fase 1–2: Fundação

- [ ] T001 [INFRA] Implementar `requireUser` + erros Unauthorized/NotFound em `apps/web/src/server/auth/`
- [ ] T002 [INFRA] Implementar `assertOwnership` + helper de `where` por userId em `apps/web/src/server/auth/ownership.ts`
- [ ] T003 [INFRA] Middleware/proxy protegendo rotas autenticadas em `apps/web/src/middleware.ts`

**✅ Checkpoint:** Visitante não acessa área autenticada.

---

## Fase 3: US-01 — Acessar apenas os próprios dados (P1)

**Story points:** 5

- [ ] T004 [US1] Suite integration two-user (A não lê/muta recurso de B → 404) em `apps/web/tests/integration/isolation.test.ts`
- [ ] T005 [US1] E2E smoke: usuário autenticado não vê dados de outro (via fixture) em `apps/web/tests/e2e/isolation.spec.ts`

**T004 Done when:**
- Dois usuários reais no DB de teste
- Tentativa cross-user falha com 404
- Agregação/lista filtra por `userId`

---

## Fase 4: US-02 — Padrão reutilizável (P1)

**Story points:** 3

- [ ] T006 [US2] Documentar padrão no README da lib + exemplo de Server Action template em `apps/web/src/server/auth/README.md` (ou equivalente)

**✅ Checkpoint:** M2 pode copiar o padrão sem redesenhar auth.

---

## Resumo das tasks

| Task | US | O que fazer | Onde | Depende | Req | Tests | Gate |
|------|----|-------------|------|---------|-----|-------|------|
| **T001** | INFRA | requireUser | `src/server/auth/` | auth feature | FR-004 | unit | `npm test` |
| **T002** | INFRA | assertOwnership | `src/server/auth/ownership.ts` | T001 | FR-001,002 | unit | `npm test` |
| **T003** | INFRA | middleware rotas | `src/middleware.ts` | T001 | FR-004 | e2e | `npx playwright test` |
| **T004** | US1 | testes two-user | `tests/integration/` | T002 | FR-001–003,006 | integration | `npm test` |
| **T005** | US1 | E2E isolamento | `tests/e2e/` | T003,T004 | FR-006 | e2e | `npx playwright test` |
| **T006** | US2 | docs padrão M2 | `src/server/auth/` | T002 | FR-005 | none | file exists |

## Notas

- Branch: `feat/M1-isolamento-por-usuario`
- Não implementar CRUD de Despesa aqui

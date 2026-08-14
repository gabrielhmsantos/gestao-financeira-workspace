# Plano: Cadastro e ciclo de vida da despesa

**Marco:** M2 | **Status:** planejado | **Spec:** [spec.md](./spec.md)
**Criado em:** 2026-08-14

---

## Resumo

Persistir Despesa com ownership, catálogo fixo, valor em centavos, ciclo Ativa→Arquivada via `archived_at`, Server Actions validadas, auditoria e UI de formulário create/edit/archive — sem listagem filtrada (feature irmã).

## Story points

| US | Título | Prioridade | SP |
|----|--------|------------|-----|
| US-01 | Cadastrar Despesa | P1 | 5 |
| US-02 | Editar Despesa ativa | P1 | 3 |
| US-03 | Arquivar Despesa | P1 | 3 |
| **Total (P1 / Todos)** | | | **11 / 11** |

## Contexto técnico

| Aspecto | Valor |
|---------|-------|
| Dependências | Prisma, Zod, helpers M1 ownership, shadcn forms |
| Armazenamento | `Despesa.amount_cents`, `archived_at` |
| Testes | unit validators · integration CRUD · E2E create/edit/archive |

## Checagem da constituição

| Princípio | Status | Notas |
|-----------|--------|-------|
| Isolamento | ✅ | user_id + helpers |
| Auth | ✅ | requireUser |
| Arquivamento | ✅ | archived_at |
| Catálogo fixo | ✅ | enum |
| Validação servidor | ✅ | Zod |
| Auditoria | ✅ | EXPENSE_* |
| Sem decisões financeiras | ✅ | |

**Violações:** nenhuma

## Código-fonte (alvo)

```
apps/web/prisma/schema.prisma          # model Expense
apps/web/src/lib/domain/categories.ts
apps/web/src/lib/validators/expense.ts
apps/web/src/server/actions/expenses.ts
apps/web/src/app/(app)/despesas/nova/
apps/web/src/app/(app)/despesas/[id]/edit/
```

## Decisões técnicas

| Decisão | Escolhido | Justificativa |
|---------|-----------|---------------|
| Dinheiro | centavos int | precisão |
| Status | archived_at | BR-007/008 |
| Categoria | enum fixo | BR-010 |

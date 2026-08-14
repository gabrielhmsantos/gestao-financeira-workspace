# Plano: Listagem, filtros e categorias

**Marco:** M2 | **Status:** planejado | **Spec:** [spec.md](./spec.md)
**Criado em:** 2026-08-14

---

## Resumo

Listagem paginada de Despesas Ativas do proprietário com filtros de período e categoria, reutilizando o catálogo fixo compartilhado — sem alterar o ciclo de vida.

## Story points

| US | Título | Prioridade | SP |
|----|--------|------------|-----|
| US-01 | Listar Despesas ativas com filtros | P1 | 5 |
| US-02 | Exibir catálogo fixo de Categorias | P1 | 2 |
| **Total (P1 / Todos)** | | | **7 / 7** |

## Contexto técnico

| Aspecto | Valor |
|---------|-------|
| Query | Prisma `findMany` + `count` com `userId`, `archivedAt: null`, filtros |
| UI | `/despesas` com controles de filtro shadcn |
| Testes | integration filtros · E2E listagem |

## Checagem da constituição

| Princípio | Status | Notas |
|-----------|--------|-------|
| Isolamento | ✅ | filtro userId |
| Arquivamento | ✅ | só ativas |
| Catálogo fixo | ✅ | RF-009 |
| Demais | ✅ | |

**Violações:** nenhuma

## Código-fonte

```
apps/web/src/server/queries/expenses.ts
apps/web/src/app/(app)/despesas/page.tsx
apps/web/src/components/expenses/expense-filters.tsx
apps/web/src/lib/domain/categories.ts   # compartilhado
```

## Decisões técnicas

| Decisão | Escolhido | Justificativa |
|---------|-----------|---------------|
| Paginação | offset page=20 | MVP |
| Período | from/to inclusivos | RF-005 |
| Ordenação | date DESC | usabilidade |

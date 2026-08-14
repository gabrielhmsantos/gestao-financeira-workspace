# Plano: Resumo por período

**Marco:** M3 | **Status:** planejado | **Spec:** [spec.md](./spec.md)
**Criado em:** 2026-08-14

---

## Resumo

Calcular e exibir Resumo de despesas no servidor (total, quantidade, participação por categoria) para Ativas do usuário no período (padrão mês atual), sem gráficos nem recomendações financeiras.

## Story points

| US | Título | Prioridade | SP |
|----|--------|------------|-----|
| US-01 | Consultar Resumo de despesas no período | P1 | 5 |
| US-02 | Destacar total do período | P1 | 2 |
| **Total (P1 / Todos)** | | | **7 / 7** |

## Contexto técnico

| Aspecto | Valor |
|---------|-------|
| Agregação | Prisma groupBy / aggregate filtrando userId + archivedAt null + date range |
| UI | `/resumo` — total em evidência, tabela/lista de categorias |
| Testes | unit % · integration agregação · E2E período |

## Checagem da constituição

| Princípio | Status | Notas |
|-----------|--------|-------|
| Isolamento / BR-012 | ✅ | |
| Arquivamento | ✅ | só ativas |
| BR-013 | ✅ | só números |
| Demais | ✅ | |

**Violações:** nenhuma

## Código-fonte

```
apps/web/src/server/queries/expense-summary.ts
apps/web/src/app/(app)/resumo/page.tsx
apps/web/src/components/summary/
apps/web/tests/e2e/summary.spec.ts
```

## Decisões técnicas

| Decisão | Escolhido | Justificativa |
|---------|-----------|---------------|
| Cálculo | servidor | BR-009 |
| % | 1 decimal | clareza |
| Default | mês atual | RF-008 |

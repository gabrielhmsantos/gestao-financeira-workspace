# Research: Resumo por período

**Marco:** M3 | **Feature:** Resumo por período
**Criado em:** 2026-08-14

---

## Decision: Cálculo no servidor

**Chosen:** Agregação no servidor (Prisma `groupBy` / SQL) sobre Despesas Ativas do usuário no período; UI só exibe
**Rationale:** BR-009 · BR-012 · validação servidor; evita inconsistência client-side.
**Alternatives rejected:**
- Somar no client a partir da listagem — frágil com paginação
- Materialized view — overkill MVP

---

## Decision: Participação percentual

**Chosen:** Percentual = `(totalCategoria / totalGeral) * 100` com **1 casa decimal**; se totalGeral = 0, categorias com 0% e total 0
**Rationale:** RF-008; UX clara sem gráficos (fora de escopo).
**Alternatives rejected:**
- Arredondamento que some ≠ 100 sem regra — documentar possível residual de arredondamento
- Gráficos — fora do MVP

---

## Decision: Período padrão

**Chosen:** **Mês civil atual** no fuso de exibição definido (premissa: America/Sao_Paulo para bounds de UI; storage date-only)
**Rationale:** PRD/RF-008.

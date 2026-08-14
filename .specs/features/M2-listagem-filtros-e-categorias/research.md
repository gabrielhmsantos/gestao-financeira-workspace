# Research: Listagem, filtros e categorias

**Marco:** M2 | **Feature:** Listagem, filtros e categorias
**Criado em:** 2026-08-14

---

## Decision: Paginação

**Chosen:** Cursor ou offset com **page size default 20** (máx. 50)
**Rationale:** Constituição exige listagens paginadas/limitadas; volume pessoal não exige cursor sofisticado — offset OK no MVP.
**Alternatives rejected:**
- Sem limite — risco de payload grande
- Infinite scroll complexo — overkill MVP

---

## Decision: Filtro de período

**Chosen:** `from` + `to` (date inclusivos) na query; UI com atalhos mês atual / mês anterior / personalizado (personalizado nesta feature; resumo M3 reutiliza)
**Rationale:** RF-005; glossário Período.
**Alternatives rejected:**
- Só mês fixo sem range — insuficiente para RF-005

---

## Decision: Exibição de categorias

**Chosen:** Módulo compartilhado `categories.ts` (labels pt-BR) usado em filtros e formulários
**Rationale:** RF-009 · BR-010; uma fonte de verdade.

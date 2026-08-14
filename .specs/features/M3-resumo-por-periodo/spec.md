# Spec: Resumo por período

**Marco:** M3 | **Status:** planejado | **Depende de:** M2-listagem-filtros-e-categorias
**Refs da foundation:** RF-008 · BR-009 · BR-012 · BR-013
**Criado em:** 2026-08-14

---

## Contexto do projeto (fix)

- **Produto:** Controle de Despesas — registro e resumo de despesas pessoais autenticadas
- **Stack:** Next.js (App Router) + React + TypeScript + Tailwind/shadcn · SQLite · Playwright
- **Código:** `apps/web` (layout B — pasta agrupadora `apps/`)
- **Glossário canônico:** Usuário, Despesa, Categoria, Status (Ativa/Arquivada), Resumo de despesas, Período, Arquivar, Auditoria — evitar Gasto/Lançamento/Transação como sinônimo de registro
- **Princípios:** isolamento por proprietário; auth obrigatória; arquivamento sem exclusão física; catálogo fixo; validação no servidor; auditoria; sem decisões financeiras além do cálculo

---

## Cenários de usuário

### US-01 — Consultar Resumo de despesas no período (P1)

Como Usuário autenticado, quero ver o Resumo de despesas (total, quantidade, total e participação por Categoria) no período selecionado, para acompanhar meu consumo sem recomendações financeiras.

**Story points:** 5

**Cenários de aceitação:**

1. **Dado** Despesas Ativas no mês atual, **Quando** abro o resumo sem escolher período, **Então** o padrão é o **mês atual** e os totais refletem só minhas Ativas nesse intervalo
2. **Dado** seleção de mês anterior ou período personalizado, **Quando** consulto, **Então** total, quantidade e breakdown por categoria são recalculados (BR-009)
3. **Dado** Despesas Arquivadas no período, **Quando** o resumo é calculado, **Então** elas **não** entram
4. **Dado** outro usuário com Despesas, **Quando** vejo meu resumo, **Então** nenhum valor dele aparece (BR-012)
5. **Dado** o resumo exibido, **Quando** inspeciono a UI, **Então** não há recomendações/orçamento/investimento (BR-013) — apenas números de acompanhamento

---

### US-02 — Destacar total do período (P1)

Como Usuário, quero identificar facilmente o total gasto no período, para cumprir a usabilidade do PRD.

**Story points:** 2

**Cenários de aceitação:**

1. **Dado** resumo carregado, **Quando** olho a página, **Então** o total geral está visualmente em evidência (hierarquia tipográfica), com quantidade e participação por categoria acessíveis
2. **Dado** período sem Despesas, **Quando** abro o resumo, **Então** total 0, quantidade 0, categorias a 0% (ou lista vazia de breakdown)

---

## Requisitos funcionais

| ID | Requisito | Ref foundation | Prioridade |
|----|-----------|----------------|------------|
| FR-001 | Calcular total gasto (centavos→BRL) no período para Ativas do usuário | RF-008 · BR-009 | P1 |
| FR-002 | Calcular quantidade de Despesas Ativas no período | RF-008 | P1 |
| FR-003 | Calcular total e participação % por Categoria | RF-008 | P1 |
| FR-004 | Período padrão = mês atual; opções mês anterior e personalizado | RF-008 · Glossário | P1 |
| FR-005 | Restringir agregação ao usuário autenticado | BR-012 | P1 |
| FR-006 | Não oferecer decisões/recomendações financeiras | BR-013 | P1 |

## Casos de borda

- Total zero — percentuais zero; sem divisão por zero
- Arredondamento de % — 1 casa decimal; residual aceitável
- Período personalizado inválido (`from` > `to`) — 400
- Categorias sem gasto no período — omitir ou mostrar 0 (premissa: **omitir** do breakdown)

## Fora de escopo

- Gráficos
- Comparativo multi-mês automático, metas, orçamento
- Exportação
- Incluir Arquivadas

## Esclarecimentos

## Premissas

- Fuso para “mês atual”: **America/Sao_Paulo** nos bounds da UI
- Breakdown: **omitir** categorias com total 0
- Percentual: **1 casa decimal**
- Rota UI: `/resumo`

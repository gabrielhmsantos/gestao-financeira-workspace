# Spec: Listagem, filtros e categorias

**Marco:** M2 | **Status:** planejado | **Depende de:** M2-cadastro-e-ciclo-de-vida-da-despesa
**Refs da foundation:** RF-005 · RF-009 · BR-010 · BR-003
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

### US-01 — Listar Despesas ativas com filtros (P1)

Como Usuário autenticado, quero listar minhas Despesas **Ativas** filtrando por período e categoria, para encontrar registros do dia a dia.

**Story points:** 5

**Cenários de aceitação:**

1. **Dado** Despesas Ativas e Arquivadas próprias, **Quando** abro a listagem sem filtro especial, **Então** vejo apenas Ativas (paginadas)
2. **Dado** filtro de período (`from`/`to`), **Quando** aplico, **Então** só Despesas Ativas com `date` no intervalo aparecem
3. **Dado** filtro de categoria do catálogo, **Quando** aplico, **Então** a lista restringe a essa Categoria
4. **Dado** Despesas de outro usuário, **Quando** listo, **Então** nenhuma delas aparece

---

### US-02 — Exibir catálogo fixo de Categorias (P1)

Como Usuário, quero ver as Categorias oficiais do MVP em filtros (e consistentes com o cadastro), para classificar e filtrar corretamente.

**Story points:** 2

**Cenários de aceitação:**

1. **Dado** a UI de filtro/cadastro, **Quando** abro o seletor de Categoria, **Então** vejo exatamente: Alimentação, Transporte, Moradia, Saúde, Lazer, Educação, Outros
2. **Dado** tentativa de categoria customizada via API, **Quando** o servidor valida, **Então** rejeita (BR-010)

---

## Requisitos funcionais

| ID | Requisito | Ref foundation | Prioridade |
|----|-----------|----------------|------------|
| FR-001 | Listar Despesas Ativas do usuário autenticado | RF-005 · BR-003 | P1 |
| FR-002 | Filtrar por período (from/to) | RF-005 | P1 |
| FR-003 | Filtrar por categoria do catálogo | RF-005 · BR-010 | P1 |
| FR-004 | Exibir catálogo fixo de Categorias (RF-009) | RF-009 · BR-010 | P1 |
| FR-005 | Paginar ou limitar a listagem | RNF Performance · Constituição | P1 |
| FR-006 | Excluir Arquivadas da listagem ativa | BR-008 | P1 |

## Casos de borda

- Período com `from` > `to` — rejeitar validação
- Sem resultados — lista vazia (não erro)
- Página além do total — lista vazia ou última página (premissa: lista vazia)
- Categoria “todas” — omitir filtro de categoria

## Fora de escopo

- Resumo agregado (M3)
- Exportação, busca full-text, ordenação avançada multi-coluna (ordenação default: date desc)
- Desarquivar / listar arquivadas (opcional futuro)
- Criar categorias

## Esclarecimentos

## Premissas

- Ordenação default: **`date` DESC**, depois `created_at` DESC
- Page size default: **20**
- Atalhos de período na UI: mês atual e mês anterior (personalizado via inputs de data)
- Labels de categoria em **pt-BR**

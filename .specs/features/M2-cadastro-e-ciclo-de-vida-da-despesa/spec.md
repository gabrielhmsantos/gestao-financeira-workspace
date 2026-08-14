# Spec: Cadastro e ciclo de vida da despesa

**Marco:** M2 | **Status:** planejado | **Depende de:** M1-autenticacao-e-sessao · M1-isolamento-por-usuario
**Refs da foundation:** RF-004 · RF-006 · RF-007 · BR-004 · BR-005 · BR-006 · BR-007 · BR-008 · BR-010 · BR-011
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

### US-01 — Cadastrar Despesa (P1)

Como Usuário autenticado, quero cadastrar uma Despesa com descrição, valor > 0, data e Categoria do catálogo, para registrar um gasto pessoal.

**Story points:** 5

**Cenários de aceitação:**

1. **Dado** usuário autenticado e dados válidos, **Quando** cadastra a Despesa, **Então** ela nasce **Ativa**, vinculada ao seu `user_id`, e aparece como própria
2. **Dado** valor ≤ 0 ou campos obrigatórios ausentes / categoria inválida, **Quando** submete, **Então** o servidor rejeita sem persistir
3. **Dado** cadastro bem-sucedido, **Quando** a auditoria é consultada, **Então** há evento de criação de Despesa (BR-011)

---

### US-02 — Editar Despesa ativa (P1)

Como Usuário, quero editar descrição, valor, data e categoria de uma Despesa **Ativa** minha, para corrigir registros.

**Story points:** 3

**Cenários de aceitação:**

1. **Dado** Despesa Ativa própria, **Quando** edito campos válidos, **Então** alterações persistem e geram auditoria
2. **Dado** Despesa de outro usuário ou inexistente, **Quando** tento editar, **Então** recebo 404
3. **Dado** Despesa Arquivada, **Quando** tento editar, **Então** a operação é rejeitada

---

### US-03 — Arquivar Despesa (P1)

Como Usuário, quero Arquivar uma Despesa Ativa minha, para removê-la da operação sem exclusão física.

**Story points:** 3

**Cenários de aceitação:**

1. **Dado** Despesa Ativa própria, **Quando** Arquivo, **Então** `archived_at` é preenchido (status Arquivada) e ela deixa de ser mutável como ativa
2. **Dado** Despesa já Arquivada, **Quando** tento arquivar de novo, **Então** operação é no-op seguro ou erro idempotente documentado
3. **Dado** arquivamento, **Quando** auditoria é consultada, **Então** há evento de arquivamento; não há DELETE físico

---

## Requisitos funcionais

| ID | Requisito | Ref foundation | Prioridade |
|----|-----------|----------------|------------|
| FR-001 | Cadastrar Despesa com descrição, valor > 0, data e categoria do catálogo | RF-004 · BR-004 · BR-005 · BR-010 | P1 |
| FR-002 | Vincular Despesa ao usuário autenticado (ownership) | BR-006 · RF-003 | P1 |
| FR-003 | Editar Despesa Ativa do proprietário | RF-006 · BR-006 | P1 |
| FR-004 | Arquivar Despesa (Ativa → Arquivada) sem exclusão física | RF-007 · BR-007 · BR-008 | P1 |
| FR-005 | Rejeitar edição de Despesa Arquivada | BR-007 | P1 |
| FR-006 | Auditar criação, edição e arquivamento | BR-011 | P1 |
| FR-007 | Validar no servidor todos os inputs | Constituição | P1 |

## Casos de borda

- Valor com centavos (ex.: 10,99) — persistir em centavos
- Data futura — permitida no MVP (premissa)
- Categoria fora do catálogo — rejeitar
- Tentativa de enviar `userId` no body — ignorar
- Arquivar recurso de outro — 404

## Fora de escopo

- Listagem com filtros e UI de catálogo (feature **Listagem, filtros e categorias**)
- Resumo (M3)
- Parcelamento, recorrência, anexos, exclusão física, desarquivar
- Criação de categorias pelo usuário

## Esclarecimentos

## Premissas

- Moeda: **BRL**; armazenamento em **centavos**
- Data da Despesa: **date** (dia) armazenada de forma consistente (UTC midnight ou date-only string ISO)
- Datas futuras: **permitidas**
- Idempotência de arquivar já arquivada: **409 ou 204 no-op** — escolher **409** com mensagem clara
- UI mínima de formulário create/edit nesta feature; listagem rica na feature irmã

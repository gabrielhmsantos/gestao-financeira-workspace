# Roadmap

**Marco atual:** M1 — Autenticação e isolamento
**Status:** M0 ✅ done — próximo: `coe-sdd-implement M1-autenticacao-e-sessao`

---

## M0 — Bootstrap

**Objetivo:** Tornar a aplicação Next.js full-stack executável localmente (scaffold, SQLite, lint/testes, health) em `apps/web`
**Dependências:** —
**Status:** ✅ done → [`.specs/features/M0-bootstrap/`](../features/M0-bootstrap/)

**Escopo:**

- Scaffold Next.js (App Router) + TypeScript + Tailwind + shadcn/ui em `apps/web`
- Persistência SQLite com camada de acesso e primeira migration/schema base
- Configuração de ambiente (env), lint, formatação e runner de testes
- Playwright (E2E) e verificação simples de disponibilidade (health)
- Estrutura de pastas alinhada ao STACK (UI + Server Actions/Route Handlers)

---

## M1 — Autenticação e isolamento

**Objetivo:** Usuário cria conta, autentica-se e acessa apenas os próprios dados
**Alvo:** Pessoa física consegue entrar no sistema com segurança e privacidade dos próprios registros
**Dependências:** M0

### Features

**Autenticação e sessão** - PLANNED ✅ → [`.specs/features/M1-autenticacao-e-sessao/`](../features/M1-autenticacao-e-sessao/)

- RF-001 Criar conta com nome, e-mail e senha, rejeitando e-mail já cadastrado
- RF-002 Autenticar com e-mail/senha e encerrar sessão (logout)
- BR-001 Exigir conta autenticada para acessar dados pessoais
- BR-002 Garantir unicidade de e-mail no cadastro
- BR-011 Auditar criação de conta e falhas relevantes de login

**Isolamento por usuário** - PLANNED ✅ → [`.specs/features/M1-isolamento-por-usuario/`](../features/M1-isolamento-por-usuario/)

- RF-003 Isolar dados por usuário em consultas e mutações
- BR-003 Isolar dados por proprietário
- BR-012 Restringir visão agregada ao próprio usuário

---

## M2 — Gestão de despesas

**Objetivo:** Usuário registra, consulta, edita e arquiva despesas classificadas pelo catálogo fixo
**Alvo:** Controle operacional do dia a dia de gastos pessoais com filtros por período e categoria
**Dependências:** M1

### Features

**Cadastro e ciclo de vida da despesa** - PLANNED ✅ → [`.specs/features/M2-cadastro-e-ciclo-de-vida-da-despesa/`](../features/M2-cadastro-e-ciclo-de-vida-da-despesa/)

- RF-004 Cadastrar despesa com descrição, valor > 0, data e categoria do catálogo
- RF-006 Editar despesa ativa do proprietário
- RF-007 Arquivar despesa (exclusão operacional)
- BR-004 Exigir campos obrigatórios da despesa
- BR-005 Exigir valor positivo
- BR-006 Restringir mutação ao proprietário
- BR-007 Controlar ciclo de vida Ativa → Arquivada
- BR-008 Arquivar em vez de excluir fisicamente
- BR-011 Auditar criação, edição e arquivamento de despesa

**Listagem, filtros e categorias** - PLANNED ✅ → [`.specs/features/M2-listagem-filtros-e-categorias/`](../features/M2-listagem-filtros-e-categorias/)

- RF-005 Listar despesas ativas com filtro por período e categoria
- RF-009 Exibir categorias fixas do MVP
- BR-010 Usar apenas categorias do catálogo fixo

---

## M3 — Resumo de despesas

**Objetivo:** Usuário acompanha total gasto e distribuição por categoria no período selecionado
**Alvo:** Visibilidade numérica rápida do consumo pessoal no mês atual, mês anterior ou período personalizado
**Dependências:** M2

### Features

**Resumo por período** - PLANNED ✅ → [`.specs/features/M3-resumo-por-periodo/`](../features/M3-resumo-por-periodo/)

- RF-008 Consultar resumo (total, quantidade, total e participação por categoria) no período selecionado
- BR-009 Calcular resumo apenas no período e sobre despesas ativas
- BR-012 Restringir visão agregada ao próprio usuário
- BR-013 Não decidir além do cálculo de acompanhamento

---

## Considerações futuras

- Controle de receitas, contas bancárias, cartões e parcelamento
- Despesas recorrentes, orçamento mensal e metas financeiras
- Importação de extratos / Open Finance e investimentos
- Compartilhamento de conta, multi-papel e painel administrativo
- Categorias criadas pelo usuário e gráficos no resumo
- Alteração de senha in-app, e-mail/notificações, exportação e IA
- Aplicativo mobile

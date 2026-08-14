# Controle de Despesas

**Visão:** Aplicação web simples para pessoas físicas registrarem despesas pessoais e acompanharem um resumo dos gastos por período e categoria, com isolamento total por usuário autenticado.
**Para:** Pessoas físicas que desejam controle individual e simples de gastos pessoais (sem compartilhamento familiar ou empresarial).
**Resolve:** Falta de registro único e filtrável de despesas, que impede saber quanto foi gasto em um período e quais categorias concentram os gastos.
**Refs da foundation:** PRD.md · BUSINESS-RULES.md · GLOSSARY.md · STACK.md

---

## Objetivos

- Permitir criar conta, login/logout e operar apenas sobre os próprios dados, sem workaround
- Permitir cadastrar, editar, arquivar e filtrar despesas por período e categoria
- Exibir resumo correto (total, quantidade, distribuição por categoria) no período selecionado, com mês atual como padrão
- Manter specs SDD implementáveis sem redefinir o produto

## Stack tecnológica

**Núcleo:**

- Frontend: Next.js (App Router) + React + TypeScript + Tailwind CSS + shadcn/ui
- Backend: Next.js (Server Actions e/ou Route Handlers) na mesma aplicação
- Banco de dados: SQLite
- Runtime: Node.js + TypeScript

**Dependências-chave:** autenticação com e-mail/senha e hash (ex.: Auth.js ou equivalente), ORM/query builder compatível com SQLite, Playwright (E2E), validação de schema no servidor

## Escopo

**O MVP inclui:**

- Criação de conta (nome, e-mail, senha) com e-mail único
- Login e logout; acesso autenticado a dados pessoais
- Cadastro, listagem com filtros, edição e arquivamento de despesas
- Categorias fixas do catálogo MVP
- Resumo numérico por período (padrão: mês atual) com total, quantidade e participação por categoria
- Isolamento de dados por usuário; auditoria de ações críticas

**Explicitamente fora de escopo:**

- Receitas, contas bancárias, cartões, parcelamento, recorrência, orçamento, metas
- Importação de extratos, Open Finance, investimentos, compartilhamento de conta
- Mobile nativo, painel admin, multi-papel, categorias criadas pelo usuário
- Gráficos no resumo, alteração de senha in-app, e-mail/notificações, exportação, IA

## Restrições

- Técnicas: TypeScript obrigatório; Next.js + React no frontend; SQLite como banco; aplicação única full-stack (sem microsserviços no MVP)
- Produto: um único papel (Usuário); sem visão cross-user; exclusão operacional via arquivamento

## Layout do workspace

**Repositório de controle:** este workspace (specs / SDD em `.specs/`).

**Layout adotado:** `B` — Pasta agrupadora (`apps/` como pasta de organização dos submódulos)

| Código | Nome | Forma |
|--------|------|--------|
| A | Submódulo na raiz | `workspace/<app>/` |
| B | Pasta agrupadora | `workspace/apps/{web,...}/` (neste projeto: `apps/` em vez de `repositories/`) |
| C | Por domínio | `workspace/repositories/{produto-a,produto-b}/` |

**Repositórios de código** (atualizar quando novos repos aparecerem sob o layout):

| Path | Stack | Responsabilidade |
|------|-------|------------------|
| `apps/web` | Next.js + React + TypeScript + SQLite | Aplicação web full-stack (UI, Server Actions/Route Handlers, persistência, E2E) |

**Manutenção:** Mantenha a tabela de repositórios de código atualizada. Assim que módulos/repos sob o layout adotado forem conhecidos ou descobertos, atualize esta seção **e** a rule da IDE (`coe-sdd-rule.mdc` / `CLAUDE.md` / `AGENTS.md`) com path, stack e responsabilidade. Quando novos repos aparecerem depois, atualize de novo antes do `coe-sdd-implement` neles.

**Rule da IDE:** gerada pelo `coe-sdd-init` a partir do template `coe-sdd-rule-template.md` (layout + Git). Não é a fonte da verdade só pelo ZIP do produto.

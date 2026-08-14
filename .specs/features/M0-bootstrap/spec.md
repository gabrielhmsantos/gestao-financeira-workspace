# Spec: Bootstrap

**Marco:** M0 | **Status:** planejado | **Depende de:** —
**Refs da foundation:** STACK.md · PRD.md (contexto de produto) · CONSTITUTION (padrões técnicos)
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

<!-- M0 é marco de infraestrutura: histórias orientadas à executabilidade local do sistema. -->

### US-01 — Aplicação Next.js executável localmente (P1)

Como desenvolvedor, quero um scaffold Next.js (App Router) com TypeScript, Tailwind e shadcn/ui em `apps/web`, para iniciar o produto sobre a stack canônica sem improvisar estrutura.

**Story points:** 8

**Rationale (≥8):** Greenfield completo (scaffold, UI kit, estrutura de pastas, env) em repositório quase vazio.

**Cenários de aceitação:**

1. **Dado** o repositório `apps/web` sem app Next.js, **Quando** o bootstrap é concluído, **Então** `npm run dev` sobe a aplicação App Router em TypeScript com Tailwind disponível
2. **Dado** a aplicação configurada, **Quando** a estrutura de pastas é inspecionada, **Então** há separação clara para UI (App Router) e camada de servidor (Server Actions e/ou Route Handlers) alinhada ao STACK
3. **Dado** shadcn/ui inicializado, **Quando** um componente base é referenciado, **Então** o design system está utilizável sem configuração adicional ad hoc

---

### US-02 — Persistência SQLite com migration base (P1)

Como desenvolvedor, quero SQLite com Prisma, camada de acesso e primeira migration, para que marcos seguintes persistam entidades sem reinventar o acesso a dados.

**Story points:** 5

**Cenários de aceitação:**

1. **Dado** a aplicação bootstrapada, **Quando** as migrations são aplicadas, **Então** o arquivo/banco SQLite é criado conforme env e o schema Prisma está versionado
2. **Dado** a camada de acesso configurada, **Quando** um smoke de conectividade é executado (teste ou script), **Então** a conexão com SQLite sucede
3. **Dado** o schema base do M0, **Quando** o modelo é revisado, **Então** não há entidades de domínio de produto (Usuário/Despesa) — apenas infraestrutura pronta para M1+

---

### US-03 — Health check e toolchain de qualidade (P1)

Como desenvolvedor, quero lint, formatação, Vitest, Playwright e um endpoint de health, para validar disponibilidade e qualidade mínima antes das features de produto.

**Story points:** 5

**Cenários de aceitação:**

1. **Dado** a app em execução, **Quando** `GET /api/health` é chamado, **Então** responde 200 com JSON indicando disponibilidade (e, se aplicável, status da dependência de banco)
2. **Dado** o projeto configurado, **Quando** lint e formatação são executados, **Então** os comandos concluem com sucesso na base limpa
3. **Dado** Vitest e Playwright configurados, **Quando** os suites smoke são executados, **Então** há pelo menos um teste unitário/integration de sanidade e um E2E que verifica o health (ou home + health)

---

## Requisitos funcionais

| ID | Requisito | Ref foundation | Prioridade |
|----|-----------|----------------|------------|
| FR-001 | O sistema DEVE ser uma aplicação Next.js App Router + React + TypeScript em `apps/web` | STACK | P1 |
| FR-002 | O sistema DEVE usar Tailwind CSS e shadcn/ui como base de UI | STACK | P1 |
| FR-003 | O sistema DEVE persistir em SQLite via Prisma, com migration inicial versionada | STACK · Constituição (armazenamento) | P1 |
| FR-004 | O sistema DEVE expor verificação de disponibilidade via `GET /api/health` | STACK (healthcheck) | P1 |
| FR-005 | O sistema DEVE ter lint, formatação e runner de testes unit/integration (Vitest) | STACK · Constituição (quality gates) | P1 |
| FR-006 | O sistema DEVE ter Playwright configurado com smoke E2E mínimo | STACK | P1 |
| FR-007 | O sistema DEVE documentar variáveis de ambiente necessárias (ex.: URL/path do SQLite) | STACK | P1 |

## Casos de borda

- O que acontece quando o arquivo SQLite ou diretório de dados não existe na primeira execução? (migration/create deve criar)
- Como o health se comporta se o banco estiver inacessível? (responder degradado ou 503 — ver premissas)
- O que acontece se `npm install` falhar por lock/node incompatível? (documentar versão de Node no README/quickstart)

## Fora de escopo

- Autenticação, sessão, criação de conta (M1)
- Entidades Usuário, Despesa, Categoria, Auditoria de domínio (M1/M2)
- Resumo, filtros de despesas, UI de produto além de página placeholder
- Deploy em produção, Docker obrigatório, CI remoto (pode ser preparado depois)
- Microsserviços, mobile, integrações externas

## Esclarecimentos

<!-- Nenhum Critical/High — defaults documentados em Premissas. -->

## Premissas

- Gerenciador de pacotes: **npm**
- ORM: **Prisma** + SQLite; schema M0 **sem** entidades de domínio
- Health: `GET /api/health`; se DB falhar, resposta **503** (ou 200 com `status: degraded`) — preferência: **503** quando checagem de DB estiver habilitada
- Porta local padrão: **3000**
- Node.js LTS compatível com a versão estável atual do Next.js no momento da implementação
- Idioma da UI placeholder: pt-BR
- Auth.js e entidades de produto ficam para M1+

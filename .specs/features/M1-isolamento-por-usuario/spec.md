# Spec: Isolamento por usuário

**Marco:** M1 | **Status:** planejado | **Depende de:** M1-autenticacao-e-sessao
**Refs da foundation:** RF-003 · BR-003 · BR-012
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

### US-01 — Acessar apenas os próprios dados (P1)

Como Usuário autenticado, quero que o sistema restrinja consultas e mutações ao meu `userId`, para que nenhum outro usuário veja ou altere minhas informações.

**Story points:** 5

**Cenários de aceitação:**

1. **Dado** dois usuários A e B autenticáveis, **Quando** A solicita um recurso pertencente a B (via id), **Então** recebe 404 (ou equivalente) e nenhum dado de B é retornado
2. **Dado** usuário A autenticado, **Quando** lista recursos próprios, **Então** apenas registros com `user_id = A` aparecem
3. **Dado** visitante não autenticado, **Quando** tenta acessar APIs/ações de dados pessoais, **Então** é rejeitado (401/redirect) sem payload de dados
4. **Dado** visão agregada (stub de resumo ou query agregada de teste), **Quando** A consulta, **Então** somente dados de A entram no cálculo (BR-012)

---

### US-02 — Padrão reutilizável de ownership para M2+ (P1)

Como desenvolvedor do produto, quero helpers e testes de isolamento documentados, para que cadastro/listagem/resumo de Despesa reutilizem o mesmo enforcement.

**Story points:** 3

**Cenários de aceitação:**

1. **Dado** o módulo `requireUser` / `assertOwnership`, **Quando** uma Server Action omite o filtro de usuário, **Então** testes de integração falham (contrato de qualidade)
2. **Dado** a documentação/quickstart, **Quando** o implementador de M2 segue o padrão, **Então** consegue aplicar `userId` em queries de Despesa sem novo design de auth

---

## Requisitos funcionais

| ID | Requisito | Ref foundation | Prioridade |
|----|-----------|----------------|------------|
| FR-001 | O sistema DEVE restringir toda consulta de dados pessoais ao usuário autenticado | RF-003 · BR-003 | P1 |
| FR-002 | O sistema DEVE restringir toda mutação ao proprietário do recurso | RF-003 · BR-003 | P1 |
| FR-003 | O sistema DEVE restringir visões agregadas ao próprio usuário | BR-012 | P1 |
| FR-004 | O sistema DEVE negar acesso a visitantes em rotas/ações de dados pessoais | BR-001 | P1 |
| FR-005 | O sistema DEVE expor helpers de servidor para ownership reutilizáveis em M2+ | RF-003 | P1 |
| FR-006 | O sistema DEVE cobrir isolamento com testes automation (integration/E2E) | Constituição (gates) | P1 |

## Casos de borda

- ID de recurso inexistente vs de outro usuário — ambos 404
- Sessão expirada no meio de mutação — 401
- Tentativa de forjar `userId` no body — servidor ignora e usa sessão
- Query sem `where userId` — deve ser impossível via API pública (só via helpers)

## Fora de escopo

- CRUD completo de Despesa (M2)
- Resumo de produto (M3)
- Admin cross-user, papéis, compartilhamento
- Row Level Security nativa do banco

## Esclarecimentos

## Premissas

- Recurso cross-user: resposta **404**
- Fixture de teste: entidade mínima `OwnedExample` **ou** uso de `AuditEvent`/`User` profile read — preferência: tabela/helper de teste `OwnedResource` apenas se necessário; senão testar via leitura de perfil + audit do próprio usuário e suite que simula query indevida
- Middleware protege rotas de app autenticadas; Server Actions chamam `requireUser()` sempre
- M2 DEVE importar os mesmos helpers (nota em plan/tasks)

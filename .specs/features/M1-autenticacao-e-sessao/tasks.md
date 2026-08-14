---
description: "Tasks M1 — Autenticação e sessão"
---

# Tasks: Autenticação e sessão

**Marco:** M1 | **Status:** planejado | **Depende de:** M0-bootstrap
**Foundation:** RF-001 · RF-002 · BR-001 · BR-002 · BR-011
**Política de testes:** Vitest + Playwright E2E fluxos de auth

## Convenções de path

- **App:** `apps/web/`

---

## Grafo de execução

```
T001 → T002 → T003 → T004
T004 → T005 → T006 → T007
T004 → T008 [P] → T009
T007,T009 → T010 → T011
```

---

## Fase 1: Setup

- [ ] T001 [INFRA] Estender `prisma/schema.prisma` com Usuário + AuditEvent e migration em `apps/web/prisma/`

**✅ Checkpoint:** migrate aplica; client tipado.

---

## Fase 2: Fundação

- [ ] T002 [INFRA] Configurar Auth.js (Credentials) + secrets env em `apps/web/src/lib/auth.ts`
- [ ] T003 [INFRA] Schemas Zod de register/login em `apps/web/src/lib/validators/auth.ts`
- [ ] T004 [INFRA] Serviço de auditoria (`USER_REGISTERED`, `LOGIN_FAILED`) em `apps/web/src/server/audit.ts`

**✅ Checkpoint:** Auth.js inicializa; validators cobertos por unit.

---

## Fase 3: User Story 1 — Criar conta (P1) 🎯 MVP

**Story points:** 5

- [ ] T005 [US1] Server Action/register com hash bcrypt + unicidade e-mail em `apps/web/src/server/actions/auth.ts`
- [ ] T006 [US1] UI `/cadastro` (shadcn) em `apps/web/src/app/(auth)/cadastro/`
- [ ] T007 [US1] Testes integration cadastro (sucesso, 409 e-mail, validação) em `apps/web/tests/`

**T005 Done when:**
- Conta persistida com `password_hash`
- E-mail duplicado rejeitado
- AuditEvent `USER_REGISTERED` criado
- Sessão iniciada após sucesso (premissa)

**✅ Checkpoint:** Cadastro E2E/manual via quickstart.

---

## Fase 4: User Story 2 — Login e logout (P1)

**Story points:** 5

- [ ] T008 [P] [US2] Login Credentials + logout + proteção básica de rotas autenticadas em `apps/web/src/`
- [ ] T009 [US2] UI `/login` + controle de sessão na shell em `apps/web/src/app/(auth)/login/`
- [ ] T010 [US2] Testes integration/E2E login falha/sucesso e logout em `apps/web/tests/`
- [ ] T011 [US2] Playwright E2E jornada cadastro → logout → login em `apps/web/tests/e2e/`

**T008 Done when:**
- Credenciais inválidas → 401 genérico + `LOGIN_FAILED`
- Logout limpa sessão
- Rota protegida redireciona visitante

**✅ Checkpoint:** US-01 e US-02 independentes e cobertas.

---

## Resumo das tasks

| Task | US | O que fazer | Onde | Depende | Req | Tests | Gate |
|------|----|-------------|------|---------|-----|-------|------|
| **T001** | INFRA | Schema User + AuditEvent | `apps/web/prisma/` | M0 | FR-001 | build | `npx prisma migrate deploy` |
| **T002** | INFRA | Auth.js Credentials | `apps/web/src/lib/auth.ts` | T001 | FR-004 | build | `npm run build` |
| **T003** | INFRA | Validators Zod | `apps/web/src/lib/validators/auth.ts` | T001 | FR-008 | unit | `npm test` |
| **T004** | INFRA | Auditoria | `apps/web/src/server/audit.ts` | T001 | FR-007 | unit | `npm test` |
| **T005** | US1 | Register action | `apps/web/src/server/actions/auth.ts` | T002–T004 | FR-001–003,007 | integration | `npm test` |
| **T006** | US1 | UI cadastro | `apps/web/src/app/(auth)/cadastro/` | T005 | FR-001 | e2e | `npx playwright test` |
| **T007** | US1 | Testes cadastro | `apps/web/tests/` | T005 | FR-002 | integration | `npm test` |
| **T008** [P] | US2 | Login/logout/guards | `apps/web/src/` | T002,T004 | FR-004–006 | integration | `npm test` |
| **T009** | US2 | UI login | `apps/web/src/app/(auth)/login/` | T008 | FR-004 | e2e | `npx playwright test` |
| **T010** | US2 | Testes login/logout | `apps/web/tests/` | T008 | FR-005,007 | integration | `npm test` |
| **T011** | US2 | E2E jornada auth | `apps/web/tests/e2e/` | T006,T009 | FR-001–006 | e2e | `npx playwright test` |

---

## Escopo MVP

T001–T011 (P1 completo desta feature).

## Notas

- Branch: `feat/M1-autenticacao-e-sessao` (ou `feat/M1-autenticacao-e-isolamento` se o time unificar o marco — preferir pasta da feature)
- Padrão AD-002: `feat/{milestone-name}` → `feat/M1-autenticacao-e-sessao` alinhado à pasta

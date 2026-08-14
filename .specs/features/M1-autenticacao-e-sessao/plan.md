# Plano: Autenticação e sessão

**Marco:** M1 | **Status:** planejado | **Spec:** [spec.md](./spec.md)
**Criado em:** 2026-08-14

---

## Resumo

Implementar criação de conta, login/logout com Auth.js (Credentials) + Prisma/SQLite, hash bcrypt, sessão em cookie HTTP-only, validação server-side, auditoria de registro e falhas de login, e UI pt-BR em `/cadastro` e `/login`. Isolamento fino de despesas fica na feature irmã.

## Story points

| US | Título | Prioridade | SP |
|----|--------|------------|-----|
| US-01 | Criar conta | P1 | 5 |
| US-02 | Login e logout | P1 | 5 |
| **Total (P1 / Todos)** | | | **10 / 10** |

## Contexto técnico

| Aspecto | Valor |
|---------|-------|
| Linguagem / Versão | TypeScript · Next.js App Router |
| Dependências principais | Auth.js v5, bcrypt, Zod (ou equivalente), Prisma, shadcn/ui |
| Armazenamento | SQLite — models Usuário + AuditEvent |
| Testes | Vitest unit/integration · Playwright E2E cadastro/login/logout |
| Plataforma-alvo | `apps/web` |
| Restrições | Sem OAuth; sem e-mail transacional; senha só hash |

## Checagem da constituição

### Pré-design (Fase 0)

| Princípio | Status | Notas |
|-----------|--------|-------|
| Isolamento por proprietário | ✅ alinhado | Prep via userId na sessão; queries de Despesa na feature Isolamento |
| Autenticação obrigatória | ✅ alinhado | Núcleo desta feature |
| Arquivamento sem exclusão física | ✅ alinhado | N/A |
| Catálogo fixo de categorias | ✅ alinhado | N/A |
| Validação no servidor como fonte da verdade | ✅ alinhado | Zod/schema no servidor |
| Auditoria de ações críticas | ✅ alinhado | USER_REGISTERED + LOGIN_FAILED |
| Escopo MVP sem decisões financeiras | ✅ alinhado | |

### Pós-design (Fase 2)

| Artefato | Princípio | Status | Notas |
|----------|-----------|--------|-------|
| data-model | Auth + auditoria | ✅ | password_hash; sem texto claro |
| contracts | Auth obrigatória | ✅ | 401 em credenciais inválidas |

**Violações:** nenhuma

## Estrutura do projeto

### Docs (esta feature)

```
.specs/features/M1-autenticacao-e-sessao/
├── spec.md · plan.md · tasks.md · data-model.md · research.md
├── contracts/auth-api.yaml · quickstart.md
└── checklists/requirements.md
```

### Código-fonte

```
apps/web/
├── prisma/schema.prisma          # User, AuditEvent
├── src/app/(auth)/login/
├── src/app/(auth)/cadastro/
├── src/app/api/auth/[...nextauth]/
├── src/lib/auth.ts
├── src/lib/validators/auth.ts
├── src/server/actions/auth.ts
└── tests/e2e/auth.spec.ts
```

## Decisões técnicas

| Decisão | Escolhido | Justificativa | Alternativas rejeitadas |
|---------|-----------|---------------|-------------------------|
| Auth | Auth.js Credentials | STACK | Lucia; IdP externo |
| Sessão | JWT cookie HTTP-only | Simplicidade MVP | Session table obrigatória |
| Hash | bcrypt | RNF | Hash fraco |
| API | Server Actions + Auth.js | Full-stack Next | REST-only |

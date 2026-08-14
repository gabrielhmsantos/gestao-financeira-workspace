# Plano: Isolamento por usuário

**Marco:** M1 | **Status:** planejado | **Spec:** [spec.md](./spec.md)
**Criado em:** 2026-08-14

---

## Resumo

Entregar enforcement de isolamento: `requireUser`, queries com `userId`, middleware de rotas, política 404 cross-user, testes de não-vazamento e padrão documentado para M2/M3 — sem CRUD de Despesa.

## Story points

| US | Título | Prioridade | SP |
|----|--------|------------|-----|
| US-01 | Acessar apenas os próprios dados | P1 | 5 |
| US-02 | Padrão reutilizável de ownership | P1 | 3 |
| **Total (P1 / Todos)** | | | **8 / 8** |

## Contexto técnico

| Aspecto | Valor |
|---------|-------|
| Dependências | Auth.js sessão (feature auth), Prisma |
| Testes | Integration two-user + E2E smoke acesso negado |
| Código | `apps/web/src/server/auth/`, `middleware.ts` |

## Checagem da constituição

### Pré-design

| Princípio | Status | Notas |
|-----------|--------|-------|
| Isolamento por proprietário | ✅ alinhado | Núcleo |
| Autenticação obrigatória | ✅ alinhado | requireUser |
| Demais | ✅ alinhado | N/A ou preservados |

### Pós-design

| Artefato | Princípio | Status | Notas |
|----------|-----------|--------|-------|
| data-model | Isolamento | ✅ | Convenção `user_id` |
| contracts | Isolamento | ✅ | 401/404 |

**Violações:** nenhuma

## Estrutura do projeto

### Docs

```
.specs/features/M1-isolamento-por-usuario/
├── spec.md · plan.md · tasks.md · research.md · data-model.md
├── contracts/ownership.md · quickstart.md
└── checklists/requirements.md
```

### Código

```
apps/web/src/server/auth/require-user.ts
apps/web/src/server/auth/ownership.ts
apps/web/src/middleware.ts
apps/web/tests/integration/isolation.test.ts
```

## Decisões técnicas

| Decisão | Escolhido | Justificativa | Alternativas |
|---------|-----------|---------------|--------------|
| Enforcement | Helpers + middleware | Constituição | Só UI |
| Cross-user | 404 | Privacidade | 403 |
| Despesa | Adiada M2 | ROADMAP | CRUD em M1 |

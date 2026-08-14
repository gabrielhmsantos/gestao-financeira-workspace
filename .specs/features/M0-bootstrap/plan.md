# Plano: Bootstrap

**Marco:** M0 | **Status:** planejado | **Spec:** [spec.md](./spec.md)
**Criado em:** 2026-08-14

---

## Resumo

Tornar `apps/web` uma aplicação Next.js full-stack executável localmente: scaffold App Router + TypeScript + Tailwind + shadcn/ui, Prisma/SQLite com migration baseline, toolchain (lint, format, Vitest, Playwright) e `GET /api/health`. Domínio de produto fica para M1+.

## Story points

| US | Título | Prioridade | SP |
|----|--------|------------|-----|
| US-01 | Aplicação Next.js executável localmente | P1 | 8 |
| US-02 | Persistência SQLite com migration base | P1 | 5 |
| US-03 | Health check e toolchain de qualidade | P1 | 5 |
| **Total (P1 / Todos)** | | | **18 / 18** |

## Contexto técnico

| Aspecto | Valor |
|---------|-------|
| Linguagem / Versão | TypeScript · Node.js LTS · Next.js (App Router) + React |
| Dependências principais | Tailwind CSS, shadcn/ui, Prisma, Vitest, Playwright, ESLint, Prettier (ou formatter alinhado ao Next) |
| Armazenamento | SQLite via Prisma (schema sem entidades de domínio no M0) |
| Testes | Vitest (unit/integration) · Playwright (E2E smoke health) |
| Plataforma-alvo | Web — repositório `apps/web` |
| Metas de performance | N/A no M0 (página placeholder + health) |
| Restrições | Sem microsserviços; sem auth/domínio de produto; TypeScript obrigatório |

## Checagem da constituição

### Pré-design (Fase 0)

| Princípio | Status | Notas |
|-----------|--------|-------|
| Isolamento por proprietário | ✅ alinhado | Sem dados de usuário no M0 |
| Autenticação obrigatória | ✅ alinhado | Auth adiada para M1; M0 não expõe dados pessoais |
| Arquivamento sem exclusão física | ✅ alinhado | Sem Despesa no M0 |
| Catálogo fixo de categorias | ✅ alinhado | Sem categorias no M0 |
| Validação no servidor como fonte da verdade | ✅ alinhado | Health e configs no servidor; padrão estabelecido para M1+ |
| Auditoria de ações críticas | ✅ alinhado | Sem ações críticas de domínio no M0 |
| Escopo MVP sem decisões financeiras | ✅ alinhado | Bootstrap apenas |

### Pós-design (Fase 2)

| Artefato | Princípio | Status | Notas |
|----------|-----------|--------|-------|
| data-model | Padrões de entidade | ✅ | Schema vazio de domínio; padrões aplicam-se em M1/M2 |
| contracts | Escopo MVP | ✅ | Apenas health; sem decisões financeiras |

**Violações:** nenhuma

## Estrutura do projeto

### Docs (esta feature)

```
.specs/features/M0-bootstrap/
├── spec.md
├── plan.md              ← este arquivo
├── tasks.md
├── data-model.md
├── research.md
├── contracts/
│   └── health-api.yaml
├── quickstart.md
└── checklists/
    └── requirements.md
```

### Código-fonte

```
apps/web/
├── prisma/
│   ├── schema.prisma
│   └── migrations/
├── src/                 # ou app/ na raiz conforme create-next-app
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── api/health/route.ts
│   ├── components/ui/   # shadcn
│   └── lib/
│       ├── db.ts        # Prisma client
│       └── utils.ts
├── tests/               # ou __tests__ / e2e/
│   ├── unit/
│   └── e2e/
├── .env.example
├── package.json
├── vitest.config.ts
└── playwright.config.ts
```

## Decisões técnicas

| Decisão | Escolhido | Justificativa | Alternativas rejeitadas |
|---------|-----------|---------------|-------------------------|
| ORM | Prisma + SQLite | Migrations + tipagem maduras no ecossistema Next | Drizzle; SQL cru |
| Testes unit | Vitest | ESM/TS rápido | Jest |
| Pacotes | npm | Alinhado ao STACK | pnpm/yarn |
| Health | `GET /api/health` | Probe HTTP estável | Página HTML |
| Schema M0 | Sem domínio | Evita antecipar M1/M2 | Criar User/Expense cedo |

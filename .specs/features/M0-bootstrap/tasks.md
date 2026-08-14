---
description: "Tasks M0 — Bootstrap da aplicação Next.js full-stack em apps/web"
---

# Tasks: Bootstrap

**Marco:** M0 | **Status:** concluído | **Depende de:** —
**Foundation:** STACK.md · CONSTITUTION (padrões técnicos)
**Política de testes:** Vitest unit/integration + Playwright E2E smoke; gates concretos por task

## Formato: `- [ ] T-ID [P?] [US-N] Descrição no path`

- **[P]**: paralelizável
- **[US-N]**: user story ou `INFRA`
- **Tests**: `none` | `build` | `unit` | `integration` | `e2e`
- **Gate**: comando que deve passar antes de marcar `[x]`

## Convenções de path

- **App full-stack:** `apps/web/`

---

## Grafo de execução

```
T001 → T002 → T003
         ├──→ T004 [P]
         └──→ T005 [P]
T003 → T006 → T007 → T008
T004,T005 → T009 [P]
T007,T008,T009 → T010 → T011 → T012
```

---

## Fase 1: Setup (infraestrutura compartilhada)

**Objetivo:** Scaffold Next.js e toolchain base em `apps/web`.

- [x] T001 [INFRA] Substituir placeholder e criar app Next.js (App Router) + TypeScript em `apps/web/`
- [x] T002 [INFRA] Configurar Tailwind CSS e inicializar shadcn/ui em `apps/web/`
- [x] T003 [INFRA] Definir estrutura de pastas (app, components, lib) e página placeholder pt-BR em `apps/web/src/app/` (ou `app/`)

**✅ Checkpoint:** `npm run dev` sobe a app com Tailwind/shadcn utilizáveis.

---

## Fase 2: Fundação (pré-requisitos bloqueantes)

**Objetivo:** Env, qualidade e persistência antes das US de verificação.

- [x] T004 [P] [INFRA] Configurar ESLint + Prettier (ou formatter do Next) e scripts `lint`/`format` em `apps/web/`
- [x] T005 [P] [INFRA] Criar `.env.example` com `DATABASE_URL` (SQLite) e documentar Node em `apps/web/README.md`
- [x] T006 [INFRA] Adicionar Prisma + SQLite, `schema.prisma` sem models de domínio e client em `apps/web/src/lib/db.ts`
- [x] T007 [INFRA] Criar e aplicar migration baseline em `apps/web/prisma/migrations/`

**✅ Checkpoint:** `npx prisma migrate deploy` (ou `dev`) aplica sem erro; client conecta.

---

## Fase 3: User Story 1 — Aplicação Next.js executável localmente (P1) 🎯 MVP

**Objetivo:** Confirmar stack canônica executável e estrutura alinhada ao STACK.
**Story points:** 8
**Teste independente:** `npm run build` e `npm run dev` com UI base.

- [x] T008 [US1] Garantir layout/página inicial e imports shadcn de sanidade em `apps/web/src/app/` e `apps/web/src/components/`

**T008 Done when:**
- Build de produção conclui sem erro
- Página inicial renderiza em pt-BR
- Pelo menos um componente shadcn é referenciado sem erro de resolução

**✅ Checkpoint:** US-01 verificável via build + dev.

---

## Fase 4: User Story 2 — Persistência SQLite com migration base (P1)

**Objetivo:** Camada de acesso pronta para M1+.
**Story points:** 5
**Teste independente:** teste de conectividade Prisma.

- [x] T009 [P] [US2] Implementar smoke de conectividade Prisma (Vitest integration) em `apps/web/tests/` (ou equivalente)

**T009 Done when:**
- Suite sobe DB de teste/arquivo temp ou usa env de teste
- Asserção de `$queryRaw`/`SELECT 1` (ou equivalente) passa
- Schema permanece sem User/Despesa

**✅ Checkpoint:** US-02 coberta por teste de integração.

---

## Fase 5: User Story 3 — Health check e toolchain de qualidade (P1)

**Objetivo:** Health + Vitest + Playwright smoke.
**Story points:** 5
**Teste independente:** curl/fetch health + e2e.

- [x] T010 [US3] Implementar `GET /api/health` conforme `contracts/health-api.yaml` em `apps/web/src/app/api/health/route.ts`
- [x] T011 [US3] Configurar Vitest + teste unitário mínimo (ex.: util ou parser de health) em `apps/web/`
- [x] T012 [US3] Configurar Playwright e E2E smoke que acessa `/api/health` (status 200) em `apps/web/`

**T010 Done when:**
- 200 + JSON `{ status, timestamp }` com DB up
- 503 (ou contrato acordado) quando checagem de DB falha em teste controlado

**T012 Done when:**
- `npx playwright test` (smoke) passa contra app local ou webServer do Playwright

**✅ Checkpoint:** US-03 completa; M0 validável via quickstart.

---

## Resumo das tasks

| Task | US | O que fazer | Onde | Depende | Req | Tests | Gate |
|------|----|-------------|------|---------|-----|-------|------|
| **T001** | INFRA | Scaffold Next.js + TS | `apps/web/` | — | FR-001 | build | `npm run build` |
| **T002** | INFRA | Tailwind + shadcn | `apps/web/` | T001 | FR-002 | build | `npm run build` |
| **T003** | INFRA | Estrutura pastas + placeholder | `apps/web/src/app/` | T002 | FR-001 | build | `npm run build` |
| **T004** [P] | INFRA | ESLint + format | `apps/web/` | T001 | FR-005 | none | `npm run lint` |
| **T005** [P] | INFRA | `.env.example` + README Node | `apps/web/` | T001 | FR-007 | none | `test -f .env.example` / equivalente Win |
| **T006** | INFRA | Prisma client + schema vazio domínio | `apps/web/prisma/`, `src/lib/db.ts` | T003,T005 | FR-003 | build | `npx prisma validate` |
| **T007** | INFRA | Migration baseline | `apps/web/prisma/migrations/` | T006 | FR-003 | integration | `npx prisma migrate deploy` |
| **T008** | US1 | UI sanidade shadcn + home | `apps/web/src/app/` | T003 | FR-001,FR-002 | build | `npm run build` |
| **T009** [P] | US2 | Smoke conectividade DB | `apps/web/tests/` | T007 | FR-003 | integration | `npm test` (Vitest) |
| **T010** | US3 | Route Handler health | `apps/web/src/app/api/health/route.ts` | T007 | FR-004 | integration | `npm test` / request health |
| **T011** | US3 | Vitest + unit mínimo | `apps/web/` | T004 | FR-005 | unit | `npm test` |
| **T012** | US3 | Playwright smoke health | `apps/web/` | T010,T011 | FR-006 | e2e | `npx playwright test` |

---

## Escopo MVP

Tasks T001–T012 (todas P1) constituem o M0 completo.

## Estratégia de implementação

1. Fase 1 Setup → app sobe
2. Fase 2 Fundação → Prisma migrate
3. US1 → build/UI
4. US2 → teste DB
5. US3 → health + E2E
6. Validar `quickstart.md`

## Notas

- Branch no repo de código: `feat/M0-bootstrap` (padrão AD-002)
- Commits no `apps/web`: `feat(M0-bootstrap): …`
- Não criar entidades Usuário/Despesa neste marco
- Glossário: não introduzir sinônimos proibidos em textos de UI placeholder

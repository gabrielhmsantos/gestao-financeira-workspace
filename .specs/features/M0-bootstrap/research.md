# Research: Bootstrap

**Marco:** M0 | **Status:** concluído
**Criado em:** 2026-08-14

---

## Decision: ORM / query builder para SQLite

**Chosen:** Prisma + SQLite
**Rationale:** Ecossistema maduro com Next.js/TypeScript, migrations versionadas (`prisma migrate`), tipagem gerada e caminho curto para UUID/`created_at`/`updated_at` exigidos pela constituição. Adequado ao MVP single-app sem microsserviços.
**Alternatives rejected:**
- Drizzle ORM — excelente DX SQL-first, porém menos “opiniado” em migrations para o time no bootstrap; pode ser revisitado se Prisma pesar no runtime
- better-sqlite3 cru / SQL manual — sem tipagem de schema e migrations padronizadas no MVP

---

## Decision: Runner de testes unit/integration

**Chosen:** Vitest
**Rationale:** Rápido, nativo ESM/TypeScript, alinhado a projetos Next.js modernos; cobre unit e integration sem acoplar ao Jest legado.
**Alternatives rejected:**
- Jest — padrão amplamente conhecido, porém setup mais pesado com App Router/ESM
- Apenas Playwright — insuficiente para lógica de domínio e camada de persistência (constituição exige unit/integration)

---

## Decision: Gerenciador de pacotes

**Chosen:** npm
**Rationale:** Compatível com Next.js e STACK (“npm ou equivalente”); evita divergência no workspace enquanto há um único app em `apps/web`.
**Alternatives rejected:**
- pnpm / yarn — válidos, mas sem necessidade no MVP e aumentam atrito de onboarding

---

## Decision: Endpoint de health

**Chosen:** Route Handler `GET /api/health` (JSON)
**Rationale:** Verificação simples de disponibilidade exigida pelo ROADMAP/STACK; Route Handler é o contrato HTTP estável sem acoplar a Server Actions.
**Alternatives rejected:**
- Página HTML `/health` — menos útil para probes e automação
- Health só no E2E sem rota — não atende verificação de disponibilidade da app

---

## Decision: Escopo de schema no M0

**Chosen:** Schema Prisma inicial **sem** entidades de domínio (Usuário, Despesa); apenas infraestrutura de migration + conectividade validável
**Rationale:** Domínio de autenticação e despesas pertence a M1/M2; M0 entrega executabilidade e persistência pronta, não o modelo de negócio.
**Alternatives rejected:**
- Criar `User`/`Expense` já no M0 — antecipa escopo e mistura bootstrap com features de produto
- Sem migration alguma — deixa SQLite “solto” e atrasa o padrão obrigatório de timestamps/UUID

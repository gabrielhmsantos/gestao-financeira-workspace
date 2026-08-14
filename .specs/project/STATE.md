# Estado

**Última atualização:** 2026-08-14
**Trabalho atual:** M0-bootstrap concluído em `apps/web` (`feat/M0-bootstrap`). Próximo: `coe-sdd-implement M1-autenticacao-e-sessao`.

---

## Decisões (AD-NNN)

### AD-001: Layout B com pasta `apps/` (2026-08-14)

**Decisão:** Layout B (pasta agrupadora); submódulos de código sob `apps/` (ex.: `apps/web`).
**Motivo:** Submódulo web já instalado em `apps/web`; `apps/` é a pasta de organização do workspace.
**Foundation:** STACK (aplicação única Next.js full-stack)
**Trade-off:** Forma canônica do template B usa `repositories/`; neste projeto a pasta agrupadora é `apps/`.
**Impacto:** `coe-sdd-implement` e mapa de repos apontam para `apps/web`.

### AD-002: Padrão Git `feat/{milestone-name}` (2026-08-14)

**Decisão:** Feature branches no repo de código seguem `feat/{milestone-name}` (tipo default `feat`).
**Motivo:** Preferência do time; alinhado ao marco (ex.: `feat/M0-bootstrap`).
**Foundation:** —
**Trade-off:** Diferente do default do skill (`feat/{feature-folder}`); com várias features no mesmo marco, a branch é por marco.
**Impacto:** Rule IDE e implement usam este padrão; branches só em `apps/web`.

### AD-003: Prisma + Vitest + health `/api/health` no M0 (2026-08-14)

**Decisão:** Bootstrap usa Prisma/SQLite (schema sem domínio), Vitest, npm e `GET /api/health`; Auth.js e entidades de produto ficam para M1+.
**Motivo:** Entregar executabilidade e persistência sem antecipar escopo de autenticação/despesas.
**Foundation:** STACK.md
**Trade-off:** Troca futura de ORM exigiria migração de schema; aceitável no MVP.
**Impacto:** `M0-bootstrap` e implementação em `apps/web`.

### AD-004: Planejamento antecipado M1–M3 antes de M0 done (2026-08-14)

**Decisão:** Planejar M1–M3 com M0 apenas `PLANNED` (não `✅ done`), em fila sequencial autorizada pelo usuário.
**Motivo:** Usuário pediu planejamento de todos os marcos, um a um, sem nova aprovação entre itens.
**Foundation:** —
**Trade-off:** Specs de M1+ assumem stack/decisões do M0; se o implement de M0 divergir, planos posteriores podem precisar de ajuste.
**Impacto:** ROADMAP marca features `PLANNED` antes da implementação de dependências.

### AD-005: Auth.js Credentials + bcrypt + JWT cookie (2026-08-14)

**Decisão:** M1 auth usa Auth.js (Credentials), bcrypt e sessão JWT em cookie HTTP-only.
**Motivo:** Alinhado ao STACK; MVP sem IdP externo.
**Foundation:** STACK · RF-001/002
**Trade-off:** Sessões em DB ficam de fora no MVP.
**Impacto:** `M1-autenticacao-e-sessao`.

### AD-006: Despesa em centavos + `archived_at` (2026-08-14)

**Decisão:** `amount_cents` (int > 0); status via `archived_at` nullable.
**Motivo:** Precisão monetária e BR-007/008.
**Foundation:** CONSTITUTION · BUSINESS-RULES
**Trade-off:** Conversão BRL na UI obrigatória.
**Impacto:** M2/M3 queries e contratos.

### AD-007: Cross-user retorna 404 (2026-08-14)

**Decisão:** Recurso de outro usuário ou inexistente → 404 (não 403).
**Motivo:** Privacidade (não enumerar IDs).
**Foundation:** RF-003 · BR-003
**Impacto:** Helpers de ownership e testes M1/M2.

---

## Bloqueios ativos (B-NNN)

<!-- Remova a entrada quando o bloqueio for resolvido. -->

---

## Lições aprendidas (L-NNN)

### L-001: Playwright webServer precisa de build (2026-08-14)

Em checkout limpo, `npm run start` sozinho falha no smoke E2E. Configurar `webServer.command` como `npm run build && npm run start` (ou equivalente) para o gate T012/quickstart.

### L-002: Vitest não deve incluir specs Playwright (2026-08-14)

`tests/e2e/*.spec.ts` conflitam com Vitest se o include for amplo demais. Restringir Vitest a `tests/unit` e `tests/integration`.

---

## Ideias adiadas

<!-- Scope creep capturado aqui para manter as features focadas.
     Nunca apague — são candidatas a marcos futuros. -->

---

## Todos

- [x] Planejar M0 (`coe-sdd-plan M0`) → `.specs/features/M0-bootstrap/`
- [x] Planejar M1 Autenticação e sessão → `.specs/features/M1-autenticacao-e-sessao/`
- [x] Planejar M1 Isolamento por usuário → `.specs/features/M1-isolamento-por-usuario/`
- [x] Planejar M2 Cadastro e ciclo de vida da despesa → `.specs/features/M2-cadastro-e-ciclo-de-vida-da-despesa/`
- [x] Planejar M2 Listagem, filtros e categorias → `.specs/features/M2-listagem-filtros-e-categorias/`
- [x] Planejar M3 Resumo por período → `.specs/features/M3-resumo-por-periodo/`
- [x] Implementar M0 (`coe-sdd-implement M0-bootstrap`)
- [ ] Implementar M1-autenticacao-e-sessao
- [ ] Implementar M1-isolamento-por-usuario

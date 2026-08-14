# Research: Isolamento por usuário

**Marco:** M1 | **Feature:** Isolamento por usuário
**Criado em:** 2026-08-14

---

## Decision: Camada de enforcement de ownership

**Chosen:** Helpers de servidor obrigatórios (`requireUser()` + queries sempre filtradas por `userId`) + middleware/proxy de rotas autenticadas
**Rationale:** Constituição exige ownership em toda consulta/mutação; centralizar evita vazamento por Route Handler/Server Action esquecido.
**Alternatives rejected:**
- Filtro só na UI — inseguro
- RLS no SQLite — suporte limitado/não idiomático com Prisma no MVP

---

## Decision: Comportamento cross-user

**Chosen:** Recursos de outro usuário → **404** (não 403), para não confirmar existência
**Rationale:** Privacidade; alinhado a apps multi-tenant lógicos por userId.
**Alternatives rejected:**
- 403 explícito — revela que o id existe
- Exceção genérica sem status HTTP claro — dificulta testes

---

## Decision: Escopo sem entidade Despesa ainda

**Chosen:** Entregar **framework de isolamento** + testes com recurso stub/fixture (ou tabela mínima de teste) e contratos de acesso; wiring completo em despesas no M2 reutiliza os helpers
**Rationale:** ROADMAP lista Isolamento em M1 (RF-003) antes de M2; não antecipar CRUD de Despesa, mas garantir padrão testável.
**Alternatives rejected:**
- Adiar RF-003 inteiro para M2 — contradiz ROADMAP
- Implementar Despesa completa em M1 — invade M2

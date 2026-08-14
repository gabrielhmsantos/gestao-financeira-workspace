# Estado

**Última atualização:** 2026-08-14
**Trabalho atual:** Init concluído — próximo: `coe-sdd-plan M0`

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

---

## Bloqueios ativos (B-NNN)

<!-- Remova a entrada quando o bloqueio for resolvido. -->

---

## Lições aprendidas (L-NNN)

---

## Ideias adiadas

<!-- Scope creep capturado aqui para manter as features focadas.
     Nunca apague — são candidatas a marcos futuros. -->

---

## Todos

- [ ] Planejar M0 (`coe-sdd-plan M0`)

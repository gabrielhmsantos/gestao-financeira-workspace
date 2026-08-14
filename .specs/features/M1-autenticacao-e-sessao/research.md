# Research: Autenticação e sessão

**Marco:** M1 | **Feature:** Autenticação e sessão
**Criado em:** 2026-08-14

---

## Decision: Biblioteca de autenticação

**Chosen:** Auth.js (NextAuth v5) com Credentials provider (e-mail/senha)
**Rationale:** Citado no STACK; integração nativa com App Router, sessão gerenciada na app, sem provedor OAuth obrigatório no MVP.
**Alternatives rejected:**
- Lucia / implementação manual de cookies — mais controle, mais superfície de erro no MVP
- Clerk/Auth0 — integração externa fora do escopo MVP (STACK: sem serviços gerenciados obrigatórios)

---

## Decision: Estratégia de sessão

**Chosen:** Sessão em cookie HTTP-only (strategy JWT ou database session do Auth.js — preferência **JWT em cookie** no MVP para reduzir tabelas; revisável se auditoria de sessão exigir DB)
**Rationale:** Simplicidade operacional com SQLite single-node; cookie HTTP-only atende RNF de segurança básica.
**Alternatives rejected:**
- Session table obrigatória desde o dia 1 — útil, porém aumenta escopo do M1 sem RF explícito de “listar sessões”
- Token bearer mobile — não há app mobile no MVP

---

## Decision: Hash de senha

**Chosen:** bcrypt (ou argon2 via API estável do runtime) — **bcrypt** como default
**Rationale:** Amplamente suportado; senha nunca em texto claro (constituição / RNF).
**Alternatives rejected:**
- scrypt manual — correto, porém menos ergonomia pronta no ecossistema Auth.js credentials
- Hash fraco (MD5/SHA sem salt) — proibido

---

## Decision: Superfície de API

**Chosen:** Server Actions para cadastro/login/logout + rotas Auth.js necessárias; UI em `/cadastro`, `/login`
**Rationale:** Alinha ao modelo full-stack Next.js; contratos documentam inputs/outputs sem forçar REST público.
**Alternatives rejected:**
- Apenas Route Handlers REST — válido, mas Server Actions cobrem o MVP com menos boilerplate de client fetch

# Modelo de dados: Bootstrap

**Marco:** M0 | **Status:** planejado
**Refs da foundation:** STACK.md · CONSTITUTION (padrões de entidade — aplicáveis a partir de M1)

---

## Escopo do schema no M0

O M0 estabelece **infraestrutura de persistência** (Prisma + SQLite + migrations), **sem** entidades de domínio do produto.

Entidades de negócio entram nos marcos seguintes:

| Entidade | Marco |
|----------|-------|
| Usuário (+ credenciais/sessão conforme auth) | M1 |
| Auditoria (eventos críticos) | M1 (mínimo) / M2 (despesas) |
| Despesa | M2 |
| Categoria (catálogo fixo — enum/const, não CRUD) | M2 |

---

## Entidades

Nenhuma entidade de domínio neste marco.

### Infraestrutura (não-domínio)

| Artefato | Descrição |
|----------|-----------|
| `prisma/schema.prisma` | Datasource SQLite + generator client; models de domínio ausentes no M0 |
| `prisma/migrations/` | Primeira migration “baseline” (schema vazio de domínio ou apenas metadados internos do Prisma) |
| Client Prisma | Singleton/acesso compartilhado para Server Actions e Route Handlers |

---

## Enums

Nenhum enum de domínio no M0. Catálogo de Categorias e Status da Despesa serão definidos em M2 (e refletidos no glossário).

---

## Transições de estado

Não se aplica (sem Despesa neste marco).

---

## Validações

| Artefato | Regra | Mensagem de erro |
|----------|-------|------------------|
| `DATABASE_URL` / path SQLite | Obrigatório em runtime de persistência | Configuração de banco ausente ou inválida |
| Conexão Prisma | Deve abrir com sucesso após migrate | Falha de conectividade com SQLite |

---

## Notas

- Padrões obrigatórios da constituição (`id` UUID, `created_at`/`updated_at`, `archived_at` em Despesa) **não** são materializados no M0; o plano de M1/M2 DEVE aplicá-los na criação das entidades
- Soft delete / audit log: fora do M0
- Smoke de conectividade (teste ou health) valida que a base está acessível após migrate

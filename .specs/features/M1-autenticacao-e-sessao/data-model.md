# Modelo de dados: Autenticação e sessão

**Marco:** M1 | **Status:** planejado
**Refs da foundation:** RF-001 · RF-002 · BR-002 · BR-011 · STACK · CONSTITUTION

---

## Entidades

### Usuário

| Campo | Tipo | Nullable | Default | Validação |
|-------|------|----------|---------|-----------|
| `id` | UUID | Não | auto | — |
| `name` | string | Não | — | não vazio; trim |
| `email` | string | Não | — | e-mail válido; único; normalizado lowercase |
| `password_hash` | string | Não | — | hash bcrypt (nunca texto claro) |
| `created_at` | timestamp UTC | Não | now() | — |
| `updated_at` | timestamp UTC | Não | now() | — |

**Relacionamentos:**
- terá muitas `Despesa` (M2)
- terá muitos `AuditEvent` (esta feature)

**Notas:** Sem `archived_at` — Usuário não usa arquivamento no MVP.

---

### AuditEvent

| Campo | Tipo | Nullable | Default | Validação |
|-------|------|----------|---------|-----------|
| `id` | UUID | Não | auto | — |
| `user_id` | UUID | Sim | — | nulo em falha de login sem usuário resolvido |
| `action` | string/enum | Não | — | ver enum |
| `entity_type` | string | Sim | — | ex.: `user` |
| `entity_id` | UUID | Sim | — | id do registro afetado |
| `metadata` | JSON/string | Sim | — | sem senha; pode incluir e-mail tentado (cuidado PII) |
| `created_at` | timestamp UTC | Não | now() | — |
| `updated_at` | timestamp UTC | Não | now() | — |

**Relacionamentos:**
- opcionalmente pertence a `Usuário` via `user_id`

---

## Enums

### AuditAction (subset M1)

| Valor | Significado |
|-------|-------------|
| `USER_REGISTERED` | Criação de conta |
| `LOGIN_FAILED` | Falha relevante de login |
| `LOGIN_SUCCEEDED` | Opcional (log); não obrigatório por BR-011 |

---

## Transições de estado

Não se aplica a Usuário no MVP (sem estados Ativa/Arquivada para conta).

---

## Validações

| Entidade.campo | Regra | Mensagem de erro |
|----------------|-------|------------------|
| Usuário.email | único global (BR-002) | E-mail já cadastrado |
| Usuário.email | formato e-mail | E-mail inválido |
| Usuário.name | obrigatório, não vazio | Nome obrigatório |
| Usuário.password | min 8 caracteres (antes do hash) | Senha deve ter ao menos 8 caracteres |
| Login | credenciais válidas | Credenciais inválidas |

---

## Notas

- Sessão Auth.js: cookie HTTP-only; sem expor `password_hash` em qualquer DTO
- Índices: único em `email`
- Extensão M2: ações `EXPENSE_*` no mesmo `AuditEvent`

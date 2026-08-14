# Modelo de dados: Isolamento por usuário

**Marco:** M1 | **Status:** planejado
**Refs da foundation:** RF-003 · BR-003 · BR-012

---

## Entidades

Sem nova entidade de produto obrigatória. Reusa `Usuário` de M1-autenticação.

### Convenção de ownership (obrigatória para entidades futuras)

Toda entidade de dados pessoais DEVE incluir:

| Campo | Tipo | Nullable | Validação |
|-------|------|----------|-----------|
| `user_id` | UUID | Não | FK → Usuário.id; sempre igual ao autenticado em writes |

Índice recomendado: `(user_id, …)` conforme queries.

### OwnedResource (opcional — apenas se necessário para testes)

| Campo | Tipo | Nullable | Default | Validação |
|-------|------|----------|---------|-----------|
| `id` | UUID | Não | auto | — |
| `user_id` | UUID | Não | — | ownership |
| `label` | string | Não | — | — |
| `created_at` | timestamp UTC | Não | now() | — |
| `updated_at` | timestamp UTC | Não | now() | — |

**Nota:** Preferir não persistir stub em produção; se criado, restringir a ambiente de teste ou remover após suite M2.

---

## Enums

Nenhum novo.

---

## Transições de estado

Não se aplica.

---

## Validações

| Regra | Mensagem / comportamento |
|-------|---------------------------|
| Ausência de sessão | 401 / redirect login |
| `user_id` do recurso ≠ sessão | 404 |
| Body com `userId` forjado | ignorado; usa sessão |

---

## Notas

- Despesa (M2) herdará `user_id` + `archived_at`
- Resumo (M3) agrega somente com filtro de `user_id`

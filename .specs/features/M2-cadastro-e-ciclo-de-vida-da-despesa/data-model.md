# Modelo de dados: Cadastro e ciclo de vida da despesa

**Marco:** M2 | **Status:** planejado
**Refs da foundation:** RF-004 · RF-006 · RF-007 · BR-004–008 · BR-010 · BR-011 · CONSTITUTION

---

## Entidades

### Despesa

| Campo | Tipo | Nullable | Default | Validação |
|-------|------|----------|---------|-----------|
| `id` | UUID | Não | auto | — |
| `user_id` | UUID | Não | — | FK Usuário; ownership |
| `description` | string | Não | — | não vazia; trim; max razoável (ex. 200) |
| `amount_cents` | int | Não | — | > 0 |
| `date` | date | Não | — | obrigatória |
| `category` | enum/string | Não | — | catálogo fixo |
| `archived_at` | timestamp UTC | Sim | null | null = Ativa |
| `created_at` | timestamp UTC | Não | now() | — |
| `updated_at` | timestamp UTC | Não | now() | — |

**Relacionamentos:**
- pertence a `Usuário` via `user_id`

**Status derivado:**
- Ativa ⇔ `archived_at IS NULL`
- Arquivada ⇔ `archived_at IS NOT NULL`

---

## Enums

### Categoria (catálogo fixo)

| Valor | Significado |
|-------|-------------|
| `ALIMENTACAO` | Alimentação |
| `TRANSPORTE` | Transporte |
| `MORADIA` | Moradia |
| `SAUDE` | Saúde |
| `LAZER` | Lazer |
| `EDUCACAO` | Educação |
| `OUTROS` | Outros |

### AuditAction (extensão)

| Valor | Significado |
|-------|-------------|
| `EXPENSE_CREATED` | Criação de Despesa |
| `EXPENSE_UPDATED` | Edição de Despesa |
| `EXPENSE_ARCHIVED` | Arquivamento de Despesa |

---

## Transições de estado

```
[nova] → Ativa → Arquivada
```

| De | Evento | Para | Guarda |
|----|--------|------|--------|
| — | cadastrar | Ativa | autenticado; campos válidos |
| Ativa | editar | Ativa | proprietário; validação |
| Ativa | arquivar | Arquivada | proprietário |
| Arquivada | editar/arquivar | — | rejeitado |

---

## Validações

| Entidade.campo | Regra | Mensagem de erro |
|----------------|-------|------------------|
| Despesa.description | obrigatória | Descrição obrigatória |
| Despesa.amount_cents | > 0 | Valor deve ser maior que zero |
| Despesa.date | obrigatória | Data obrigatória |
| Despesa.category | ∈ catálogo | Categoria inválida |
| Despesa (edit) | Ativa | Despesa arquivada não pode ser editada |

---

## Notas

- Listagens ativas e resumos **ignoram** `archived_at NOT NULL` (features seguintes)
- Sem exclusão física no MVP

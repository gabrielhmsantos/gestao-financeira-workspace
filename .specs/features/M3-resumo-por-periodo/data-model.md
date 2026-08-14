# Modelo de dados: Resumo por período

**Marco:** M3 | **Status:** planejado
**Refs da foundation:** RF-008 · BR-009 · BR-012

---

## Entidades

Nenhuma tabela nova. O **Resumo de despesas** é um **read model** calculado a partir de `Despesa`.

### ResumoDeDespesas (read model — não persistido)

| Campo | Tipo | Nullable | Validação |
|-------|------|----------|-----------|
| `from` | date | Não | bound do período |
| `to` | date | Não | ≥ from |
| `totalAmountCents` | int | Não | ≥ 0 |
| `expenseCount` | int | Não | ≥ 0 |
| `byCategory` | array | Não | ver item |

### ItemPorCategoria

| Campo | Tipo | Validação |
|-------|------|-----------|
| `category` | enum catálogo | — |
| `totalAmountCents` | int ≥ 0 | — |
| `percentage` | number | 1 casa decimal; 0 se total geral 0 |

---

## Enums

Reusa Categoria do M2.

---

## Transições de estado

Não se aplica.

---

## Validações

| Regra | Comportamento |
|-------|---------------|
| Só `archived_at IS NULL` | BR-009 |
| Só `user_id` da sessão | BR-012 |
| `date` ∈ [from, to] | inclusivo |
| from ≤ to | 400 se inválido |

---

## Notas

- Não persistir resumo materializado no MVP
- Sem gráficos / recomendações

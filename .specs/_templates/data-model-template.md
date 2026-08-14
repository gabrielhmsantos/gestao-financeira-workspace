# Modelo de dados: [FEATURE_NAME]

**Marco:** [MILESTONE] | **Status:** rascunho
**Refs da foundation:** [FOUNDATION_REFS]

---

## Entidades

### [NomeDaEntidade]

<!-- Use a linguagem de domínio do projeto nos nomes de campo: Usuário, Despesa, Categoria, Status (Ativa/Arquivada), Resumo de despesas, Período, Arquivar, Auditoria -->

| Campo | Tipo | Nullable | Default | Validação |
|-------|------|----------|---------|-----------|
| `id` | UUID (ou equivalente não sequencial) | Não | auto | — |
| `[campo]` | [tipo] | [Sim/Não] | [default/—] | [regra] |
| `created_at` | timestamp UTC | Não | now() | — |
| `updated_at` | timestamp UTC | Não | now() | — |

**Relacionamentos:**
- pertence a `[Entidade]` via `[foreign_key]`
- tem muitos `[Entidade]`

---

<!-- Adicione mais entidades conforme necessário. Despesa DEVE incluir archived_at (ou equivalente) quando no escopo. -->

## Enums

### [NomeDoEnum]

<!-- Valores canônicos: Status Ativa|Arquivada; Categorias Alimentação|Transporte|Moradia|Saúde|Lazer|Educação|Outros -->

| Valor | Significado |
|-------|-------------|
| [VALUE_1] | [descrição] |
| [VALUE_2] | [descrição] |

---

## Transições de estado

<!-- Só se a entidade tiver ciclo de vida. Omita a seção se não se aplicar. -->

```
[inicial] → [STATE_A] → [STATE_B] → [terminal]
                ↓
           [STATE_C]
```

| De | Evento | Para | Guarda |
|----|--------|------|--------|
| Ativa | arquivar | Arquivada | proprietário autenticado; despesa ativa |

---

## Validações

| Entidade.campo | Regra | Mensagem de erro |
|----------------|-------|------------------|
| [Entidade.campo] | [regra] | [mensagem] |

---

## Notas

- Campos monetários: valor da Despesa > 0; representação consistente (detalhar no plano)
- Soft delete: Despesa via arquivamento (`archived_at`); sem exclusão física imediata no MVP
- Audit log: ações críticas de BR-011 (conta, login falho relevante, CRUD operacional de despesa)

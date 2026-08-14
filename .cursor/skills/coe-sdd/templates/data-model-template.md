# Modelo de dados: [FEATURE_NAME]

**Marco:** [MILESTONE] | **Status:** rascunho
**Refs da foundation:** [FOUNDATION_REFS]

---

## Entidades

### [NomeDaEntidade]

<!-- Use a linguagem de domínio do projeto nos nomes de campo: [DOMAIN_LANGUAGE] -->

| Campo | Tipo | Nullable | Default | Validação |
|-------|------|----------|---------|-----------|
| `id` | [PK_TYPE] | Não | auto | — |
| `[campo]` | [tipo] | [Sim/Não] | [default/—] | [regra] |
| `created_at` | [TIMESTAMP_TYPE] | Não | now() | — |
| `updated_at` | [TIMESTAMP_TYPE] | Não | now() | — |

**Relacionamentos:**
- pertence a `[Entidade]` via `[foreign_key]`
- tem muitos `[Entidade]`

---

<!-- Adicione mais entidades conforme necessário -->

## Enums

### [NomeDoEnum]

<!-- Use a linguagem de domínio do projeto nos valores: [ENUM_CONVENTION] -->

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
| [STATE_A] | [evento] | [STATE_B] | [condição] |

---

## Validações

| Entidade.campo | Regra | Mensagem de erro |
|----------------|-------|------------------|
| [Entidade.campo] | [regra] | [mensagem] |

---

## Notas

- Campos monetários: [MONETARY_RULE]
- Soft delete: [SOFT_DELETE_RULE]
- Audit log: [AUDIT_LOG_RULE]

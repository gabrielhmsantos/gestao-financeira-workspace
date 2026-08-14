# Research: Cadastro e ciclo de vida da despesa

**Marco:** M2 | **Feature:** Cadastro e ciclo de vida da despesa
**Criado em:** 2026-08-14

---

## Decision: Representação monetária

**Chosen:** Inteiro em **centavos** (`amount_cents: Int`) no banco; UI formata BRL
**Rationale:** Evita erro de ponto flutuante; alinhado à constituição (“decimal/centavos — detalhar no plano”).
**Alternatives rejected:**
- `Decimal`/`Float` — risco de arredondamento
- String monetária no DB — dificulta agregações

---

## Decision: Arquivamento

**Chosen:** Campo `archived_at` (UTC nullable); status derivado Ativa (`null`) / Arquivada (não nulo). Sem DELETE físico no MVP.
**Rationale:** BR-007, BR-008, constituição.
**Alternatives rejected:**
- Flag booleana sem timestamp — perde rastreabilidade
- Hard delete — proibido

---

## Decision: Categoria no model

**Chosen:** Enum/string persistida com valores do catálogo fixo (validação servidor); seed não necessário se enum fechado
**Rationale:** BR-010; feature de listagem também usa o catálogo — mesma fonte (`categories.ts`)
**Alternatives rejected:**
- Tabela `categories` editável — fora do MVP

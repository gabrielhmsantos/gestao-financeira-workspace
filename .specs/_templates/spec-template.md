# Spec: [FEATURE_NAME]

**Marco:** [MILESTONE] | **Status:** rascunho | **Depende de:** [DEPENDS_ON]
**Refs da foundation:** [FOUNDATION_REFS]
**Criado em:** [DATE]

---

## Contexto do projeto (fix)

- **Produto:** Controle de Despesas — registro e resumo de despesas pessoais autenticadas
- **Stack:** Next.js (App Router) + React + TypeScript + Tailwind/shadcn · SQLite · Playwright
- **Código:** `apps/web` (layout B — pasta agrupadora `apps/`)
- **Glossário canônico:** Usuário, Despesa, Categoria, Status (Ativa/Arquivada), Resumo de despesas, Período, Arquivar, Auditoria — evitar Gasto/Lançamento/Transação como sinônimo de registro
- **Princípios:** isolamento por proprietário; auth obrigatória; arquivamento sem exclusão física; catálogo fixo; validação no servidor; auditoria; sem decisões financeiras além do cálculo

---

## Cenários de usuário

<!-- P1 = obrigatório no MVP; P2 = próxima iteração; P3 = futuro -->
<!-- Story points: toda US de produto DEVE ter valor Fibonacci (1|2|3|5|8|13|21) — ver references/story-points.md. SP ≥13 → dividir antes de gerar tasks.md. -->

### [US-01] — [Título breve] (P1)

[Descreva a jornada do usuário em linguagem simples]

**Story points:** [N] <!-- Fibonacci: 1|2|3|5|8|13|21 -->

**Cenários de aceitação:**

1. **Dado** [estado inicial], **Quando** [ação], **Então** [resultado esperado]
2. **Dado** [estado inicial], **Quando** [ação], **Então** [resultado esperado]

---

### [US-02] — [Título breve] (P2)

[Descreva a jornada do usuário em linguagem simples]

**Story points:** [N] <!-- Fibonacci: 1|2|3|5|8|13|21 -->

**Cenários de aceitação:**

1. **Dado** [estado inicial], **Quando** [ação], **Então** [resultado esperado]

---

<!-- Adicione mais user stories conforme necessário. Cada uma independentemente testável e entregável. -->

## Requisitos funcionais

<!-- Mapeie cada FR às refs RF-* ou BR-* da foundation. Marque itens pouco claros com [NEEDS CLARIFICATION]. -->

| ID | Requisito | Ref foundation | Prioridade |
|----|-----------|----------------|------------|
| FR-001 | O sistema DEVE [capacidade] | RF-[N] | P1 |
| FR-002 | O sistema DEVE [capacidade] | BR-[N] | P1 |
| FR-003 | [NEEDS CLARIFICATION: descrição] | — | P1 |

## Casos de borda

- O que acontece quando [condição de contorno]?
- Como o sistema trata [cenário de erro]?
- [CASOS_DE_BORDA_DO_DOMÍNIO]

## Fora de escopo

- [Capacidade explicitamente excluída 1]
- [Capacidade explicitamente excluída 2]

## Esclarecimentos

<!-- Preenchido pelo loop de clarify (entradas CL-NNN). Não remova a seção mesmo se vazia. -->

## Premissas

<!-- Defaults razoáveis escolhidos quando a spec não especificava. Preenchido pelo clarify para achados Medium/Low. -->

- [Premissa sobre usuários-alvo ou ambiente]

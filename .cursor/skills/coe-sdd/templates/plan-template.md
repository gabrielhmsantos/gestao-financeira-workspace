# Plano: [FEATURE_NAME]

**Marco:** [MILESTONE] | **Status:** rascunho | **Spec:** [link para spec.md]
**Criado em:** [DATE]

---

## Resumo

[Um parágrafo: requisito principal + abordagem técnica escolhida]

## Story points

<!-- Ecoados de spec.md — spec.md é a fonte da verdade. Não reestime aqui. -->

| US | Título | Prioridade | SP |
|----|--------|------------|-----|
| US-01 | [título] | P1 | [N] |
| US-02 | [título] | P2 | [N] |
| **Total (P1 / Todos)** | | | **[N] / [N]** |

## Contexto técnico

| Aspecto | Valor |
|---------|-------|
| Linguagem / Versão | [TECH_STACK] |
| Dependências principais | [DEPENDENCIES] |
| Armazenamento | [STORAGE] |
| Testes | [TESTING_FRAMEWORK] |
| Plataforma-alvo | [PLATFORM] |
| Metas de performance | [PERF_GOALS] |
| Restrições | [CONSTRAINTS] |

## Checagem da constituição

### Pré-design (Fase 0)

| Princípio | Status | Notas |
|-----------|--------|-------|
| [NOME_PRINCIPIO_1] | ✅ alinhado / ⚠️ violação | [nota] |
| [NOME_PRINCIPIO_2] | ✅ alinhado / ⚠️ violação | [nota] |

### Pós-design (Fase 2)

<!-- Preenchido após data-model e estrutura do plano definidos -->

| Artefato | Princípio | Status | Notas |
|----------|-----------|--------|-------|
| data-model | [NOME_PRINCIPIO] | ✅ / ⚠️ | [nota] |
| contracts | [NOME_PRINCIPIO] | ✅ / ⚠️ | [nota] |

**Violações:** [nenhuma / AD-NNN documentado em STATE.md]

## Estrutura do projeto

### Docs (esta feature)

```
<!-- FEATURE_SLUG = {MN}-{kebab-case} ex.: M1-authentication-session, M0-bootstrap -->
.specs/features/[FEATURE_SLUG]/
├── spec.md
├── plan.md              ← este arquivo
├── tasks.md
├── data-model.md        (se aplicável)
├── research.md          (se aplicável)
├── contracts/           (se aplicável)
├── context.md           (se aplicável)
├── quickstart.md        (se aplicável)
└── checklists/
    └── requirements.md
```

### Código-fonte

```
[CODE_STRUCTURE]
```

## Decisões técnicas

<!-- De research.md se aplicável. Omita a seção se não houver decisões relevantes. -->

| Decisão | Escolhido | Justificativa | Alternativas rejeitadas |
|---------|-----------|---------------|-------------------------|
| [tópico] | [opção] | [por quê] | [opção A — motivo] |

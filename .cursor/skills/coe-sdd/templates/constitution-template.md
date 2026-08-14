<!--
RELATÓRIO DE IMPACTO DE SYNC
Versão: [CONSTITUTION_VERSION]
Data: [RATIFICATION_DATE]
Princípios adicionados: [PRINCIPLES_LIST]
Templates afetados: spec-template ⬜ | plan-template ⬜ | tasks-template ⬜ | checklist-template ⬜
TODOs: [TODOS_LIST]
-->

# [NOME_DO_PROJETO] — Constituição

**Versão**: [CONSTITUTION_VERSION] | **Ratificada**: [RATIFICATION_DATE] | **Última emenda**: [RATIFICATION_DATE]

---

## Hierarquia de autoridade

```
1. CONSTITUTION.md (este arquivo)
2. .specs/foundation/ (PRD, BUSINESS-RULES, GLOSSARY, STACK)
3. .specs/features/MN-{feature-slug}/ (specs, planos, tasks por feature, agrupados por marco no ROADMAP.md)
4. Código do projeto
```

---

## Princípios centrais

<!-- Cada princípio: MUST/SHOULD declarativo, testável, sem "deveria tentar" vago, racional explícito derivado de BR-*/PRD -->

### [NOME_PRINCIPIO_1]

[REGRAS_PRINCIPIO_1]
<!-- Formato: "O sistema DEVE [regra]. [Entidade] DEVE [regra]. Proibido [anti-padrão]." -->

**Racional**: [RACIONAL_PRINCIPIO_1]
<!-- Por que este princípio existe — vincule a BR-* ou requisito de negócio -->

---

### [NOME_PRINCIPIO_2]

[REGRAS_PRINCIPIO_2]

**Racional**: [RACIONAL_PRINCIPIO_2]

---

### [NOME_PRINCIPIO_3]

[REGRAS_PRINCIPIO_3]

**Racional**: [RACIONAL_PRINCIPIO_3]

---

<!-- Adicione mais princípios conforme necessário. Cada um deve ser inegociável, testável e rastreável à foundation. -->

---

## Restrições de tecnologia e arquitetura

| Camada | Tecnologia | Padrões obrigatórios |
|--------|------------|----------------------|
| Frontend | [FRONTEND_STACK] | [FRONTEND_PATTERNS] |
| Backend | [BACKEND_STACK] | [BACKEND_PATTERNS] |
| Armazenamento | [STORAGE_STACK] | [STORAGE_PATTERNS] |
| Infra | [INFRA_STACK] | [INFRA_PATTERNS] |
| Observabilidade | [OBS_STACK] | [OBS_PATTERNS] |

### Padrões universais de entidade

Todas as entidades persistentes DEVEM incluir:
- `id` — chave primária ([PK_TYPE])
- `created_at` — timestamp ([TIMESTAMP_TYPE])
- `updated_at` — timestamp ([TIMESTAMP_TYPE])
- [SOFT_DELETE_FIELD] — flag de soft delete (sem deletes físicos para [ENTITY_TYPES])

### Padrões obrigatórios

| Padrão | Regra |
|--------|-------|
| Soft delete | [SOFT_DELETE_RULE] |
| Audit log | [AUDIT_LOG_RULE] |
| Paginação | [PAGINATION_RULE] |
| Valores monetários | [MONETARY_RULE] |
| Enums | [ENUM_CONVENTION] |
| Linguagem de código | [CODE_LANGUAGE] |
| Linguagem de domínio | [DOMAIN_LANGUAGE] |

---

## Fluxo de desenvolvimento e quality gates

### Fluxo Spec-Driven

Todas as features DEVEM seguir: `coe-sdd-plan` → `coe-sdd-implement`. Seleção de artefatos por necessidade, não por tamanho estimado de escopo.
Sem implementação sem task em tasks.md. Sem task sem comando de gate.

### Expectativas de teste

| Escopo | Unit | Integration | E2E |
|--------|------|-------------|-----|
| Lógica de negócio | DEVE | — | — |
| Endpoints de API | DEVE | DEVE | — |
| Fluxos voltados ao usuário (P1) | — | DEVE | DEVE |
| Infraestrutura | — | DEVE | — |

### Checklist do gate de review

Antes de marcar qualquer marco `✅ done`:
- [ ] Todos os FR-* em spec.md têm tasks correspondentes marcadas `[x]`
- [ ] Todos os comandos de gate passam
- [ ] Regras de RBAC aplicadas a todos os novos endpoints (se aplicável)
- [ ] Entradas de audit_log criadas para operações que alteram estado (se aplicável)
- [ ] Terminologia canônica usada de forma consistente (sem sinônimos para termos do glossário)
- [ ] Todas as tasks P1 concluídas; itens P2 adiados documentados em STATE.md

---

## Governança

### Processo de emenda

| Tipo de mudança | Bump Semver | Obrigatório |
|-----------------|-------------|-------------|
| Remover ou redefinir princípio de forma incompatível | MAJOR (X.0.0) | Justificativa + nota de migração |
| Adicionar novo princípio ou seção | MINOR (X.Y.0) | Relatório de Impacto de Sync |
| Esclarecer, corrigir typo, refinamento não semântico | PATCH (X.Y.Z) | Relatório de Impacto de Sync atualizado |

Gatilhos de emenda: `"adicionar novo princípio"`, `"mudamos o stack"`, `"amend project rules"`.
Após emenda: atualize os templates afetados em `.specs/_templates/`; avise quais marcos podem precisar de revisão.

### Tratamento de violações

Violação da constituição detectada durante `coe-sdd-plan`:
1. Documente como `AD-NNN: CONSTITUTION VIOLATION — [princípio] — [justificativa]` em STATE.md
2. Bloqueie o progresso até o usuário fornecer justificativa explícita
3. Exceção justificada: anotada inline no artefato relevante

### Imutabilidade da foundation

Arquivos em `.specs/foundation/` são **input somente leitura**. Esta skill NUNCA DEVE escrever ou modificar arquivos da foundation.

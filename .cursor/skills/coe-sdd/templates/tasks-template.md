---
description: "Lista unificada de tasks — estrutura por fase/story (Speckit) + tabela resumo com colunas Req/Tests/Gate (TLC). Gerada pelo coe-sdd-plan. Substitua todas as tasks de exemplo pelas tasks reais derivadas de spec.md, plan.md, data-model.md e contracts/."
---

# Tasks: [FEATURE_NAME]

**Marco:** [MILESTONE] | **Status:** rascunho | **Depende de:** [DEPENDS_ON]
**Foundation:** [FOUNDATION_REFS]
**Política de testes:** conforme `.specs/codebase/TESTING.md`

## Formato: `- [ ] T-ID [P?] [US-N] Descrição no path`

- **[P]**: paralelizável — arquivos diferentes, sem dependências mútuas
- **[US-N]**: user story à qual a task pertence (US1, US2… ou `INFRA` para setup/fundação)
- **Tests**: `none` | `build` | `unit` | `integration` | `e2e`
- **Gate**: comando de shell concreto que deve passar antes de marcar `[x]`

> Toda task DEVE pertencer a uma US. Use `INFRA` para tasks das Fases 1/2 que são infraestrutura compartilhada sem US de produto. Isso mapeia limpo para Jira: cada valor US único vira uma Story sob o Epic do marco.

> **Story points** vivem na User Story, não em tasks individuais. Cada cabeçalho de fase de User Story ecoa o SP de `spec.md` (fonte da verdade) — nunca invente ou reestime SP por task. Fases `INFRA` e trabalho de polish/transversal não carregam SP.

## Convenções de path

<!-- Atualize com base na estrutura de plan.md -->

- **Monorepo**: `apps/web/src/`, `apps/api/src/`, `packages/shared/src/`
- **Projeto único**: `src/`, `tests/` na raiz do repositório
- **App web**: `backend/src/`, `frontend/src/`

---

## Grafo de execução

```
[TASK_GRAPH]
```

<!--
Exemplo:
T001 → T002 → T003 ──→ T004 [P]
              ├──→ T005 [P]
              └──→ T006 [P]
T004,T005,T006 → T007 (integration)
T007 → T008 (e2e)
-->

---

<!--
============================================================================
IMPORTANTE: As tasks abaixo são EXEMPLOS apenas para ilustração.

Substitua pelas tasks reais derivadas de:
- User stories de spec.md (prioridades P1, P2, P3)
- Estrutura técnica de plan.md
- Entidades e enums de data-model.md
- Endpoints de contracts/

Organize por Fase → User Story para que cada story possa ser:
- Implementada de forma independente
- Testada de forma independente
- Entregue como incremento de MVP

NÃO mantenha estas tasks de exemplo no tasks.md gerado.
============================================================================
-->

---

## Fase 1: Setup (infraestrutura compartilhada)

**Objetivo**: Inicialização do projeto e estrutura base.

- [ ] T001 [INFRA] Criar estrutura do projeto conforme plan.md em `[path raiz]`
- [ ] T002 [P] [INFRA] Configurar lint e formatação em `[arquivos de config]`
- [ ] T003 [P] [INFRA] Configurar ambiente e secrets em `[path de env]`

**✅ Checkpoint**: Estrutura base pronta — trabalho de fundação pode começar.

---

## Fase 2: Fundação (pré-requisitos bloqueantes)

**Objetivo**: Infraestrutura central que DEVE estar completa antes de qualquer user story.

**⚠️ CRÍTICO**: Nenhum trabalho de user story começa até esta fase estar completa.

- [ ] T004 [INFRA] Schema do banco + migrations em `[path do schema]`
- [ ] T005 [P] [INFRA] Framework de auth / RBAC em `[path de auth]`
- [ ] T006 [P] [INFRA] Entidades base / tipos compartilhados em `[path shared]`
- [ ] T007 [INFRA] Tratamento de erros e logging em `[path de middleware]`

**✅ Checkpoint**: Fundação pronta — implementação de user stories pode começar em paralelo.

---

## Fase 3: User Story 1 — [Título] (P1) 🎯 MVP

**Objetivo**: [O que esta story entrega]
**Story points**: [N] <!-- ecoado de spec.md US-01 -->
**Teste independente**: [Como verificar que esta story funciona sozinha]

- [ ] T008 [P] [US1] Criar model [Entity] em `[path]`
- [ ] T009 [P] [US1] Criar [entidade relacionada] em `[path]`
- [ ] T010 [US1] Implementar [serviço/caso de uso] em `[path]` (depende de T008, T009)
- [ ] T011 [US1] Implementar [endpoint de API ou fluxo de UI] em `[path]`
- [ ] T012 [US1] Adicionar validação e tratamento de erros em `[path]`

**T011 Done when:**
- [critério 1 — ex.: "Retorna 200 + payload esperado"]
- [critério 2 — ex.: "Input inválido retorna 422 com erro estruturado"]
- [critério 3 — ex.: "Acesso não autorizado retorna 401"]

**✅ Checkpoint**: User Story 1 totalmente funcional e independentemente testável.

---

## Fase 4: User Story 2 — [Título] (P2)

**Objetivo**: [O que esta story entrega]
**Story points**: [N] <!-- ecoado de spec.md US-02 -->
**Teste independente**: [Como verificar que esta story funciona sozinha]

- [ ] T013 [P] [US2] Criar [entidade ou estender existente] em `[path]`
- [ ] T014 [US2] Implementar [serviço/caso de uso] em `[path]`
- [ ] T015 [US2] Implementar [endpoint de API ou fluxo de UI] em `[path]`
- [ ] T016 [US2] Integrar com componentes da US1 se necessário em `[path]`

**✅ Checkpoint**: User Stories 1 E 2 independentemente funcionais.

---

[Adicione mais blocos Fase N: User Story N seguindo o mesmo padrão]

---

## Fase N: Polish e preocupações transversais

**Objetivo**: Melhorias que atravessam várias user stories.

- [ ] TXXX [P] Atualizações de documentação em `docs/`
- [ ] TXXX Validação E2E / quickstart
- [ ] TXXX [P] Endurecimento de performance e segurança

---

## Resumo das tasks

| Task | US | O que fazer | Onde | Depende | Req | Tests | Gate |
|------|----|-------------|------|---------|-----|-------|------|
| **T001** | INFRA | [Criar estrutura do projeto] | `[path]` | — | — | build | `[comando]` |
| **T004** | INFRA | [Schema + migrations] | `[path]` | T001 | FR-001 | build | `[cmd migrate]` |
| **T005** [P] | INFRA | [Auth / RBAC] | `[path]` | T004 | FR-002 | unit | `[cmd test]` |
| **T008** [P] | US1 | [Criar model da entidade] | `[path]` | T004 | FR-003 | unit | `[cmd test]` |
| **T009** [P] | US1 | [Criar entidade relacionada] | `[path]` | T004 | FR-003 | unit | `[cmd test]` |
| **T010** | US1 | [Implementar serviço] | `[path]` | T008,T009 | FR-003 | unit | `[cmd test]` |
| **T011** | US1 | [Endpoint ou fluxo de UI] | `[path]` | T010 | FR-003 | integration | `[cmd test]` |
| **T013** [P] | US2 | [Criar entidade] | `[path]` | T004 | FR-004 | unit | `[cmd test]` |
| **T015** | US2 | [Endpoint ou fluxo de UI] | `[path]` | T014 | FR-004 | integration | `[cmd test]` |

---

## Escopo MVP

Tasks T001–T012 (Fase 1 + Fase 2 + User Story 1) constituem o MVP.
Fases 4+ são P2 e podem ser adiadas.

## Estratégia de implementação

### MVP primeiro (somente User Story 1)

1. Completar Fase 1: Setup
2. Completar Fase 2: Fundação (**bloqueia todas as stories**)
3. Completar Fase 3: User Story 1
4. **PARAR e VALIDAR**: testar User Story 1 de forma independente
5. Deploy / demo se estiver pronto

### Entrega incremental

1. Setup + Fundação → fundação pronta
2. User Story 1 → testar de forma independente → deploy (MVP!)
3. User Story 2 → testar de forma independente → deploy
4. Cada story agrega valor sem quebrar as anteriores

---

## Notas

- Tasks `[P]` = arquivos diferentes, sem dependências mútuas — execute em paralelo
- Label `[US-N]` mapeia a task à user story (rastreabilidade até spec.md)
- Story points são definidos uma vez por US em `spec.md` e ecoados em cada cabeçalho de fase — ver `references/story-points.md`
- O comando de gate DEVE passar antes de marcar `[x]`
- Commit após cada task: `feat(MN-slug): descrição da task`
- Pare em qualquer checkpoint para validar de forma independente antes de continuar

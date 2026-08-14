<!--
RELATÓRIO DE IMPACTO DE SYNC
Versão: 1.0.0
Data: 2026-08-14
Princípios adicionados: Isolamento por proprietário; Autenticação obrigatória; Arquivamento sem exclusão física; Catálogo fixo de categorias; Validação no servidor; Auditoria de ações críticas; Escopo MVP sem decisões financeiras
Templates afetados: spec-template ✅ | plan-template ✅ | tasks-template ✅ | checklist-template ✅
TODOs: none
-->

# Controle de Despesas — Constituição

**Versão**: 1.0.0 | **Ratificada**: 2026-08-14 | **Última emenda**: 2026-08-14

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

### Isolamento por proprietário

O sistema DEVE garantir que cada usuário consulte, edite e arquive apenas as próprias despesas e informações. Toda consulta e mutação DEVE restringir-se ao usuário autenticado. Proibido exposição cross-user ou papéis com visão global no MVP.

**Racional**: RF-003, BR-003, BR-006, BR-012 — privacidade e ownership são não negociáveis no produto individual.

---

### Autenticação obrigatória

O acesso a despesas, listagens e resumos DEVE exigir usuário autenticado. Visitantes NÃO DEVEM visualizar dados pessoais. Senhas DEVEM ser armazenadas apenas como hash. Sessão ou token DEVE expirar conforme política definida na implementação.

**Racional**: RF-001, RF-002, BR-001, BR-002 e RNFs de segurança — conta com e-mail único é a porta de entrada do MVP.

---

### Arquivamento sem exclusão física

A exclusão operacional de despesa DEVE ser arquivamento (`Ativa` → `Arquivada`). Despesas arquivadas NÃO DEVEM aparecer em listagens ativas nem entrar em totais e resumos. Proibido exclusão física imediata no MVP e retorno de Arquivada para Ativa.

**Racional**: RF-007, BR-007, BR-008 — rastreabilidade e histórico preservados sem soft-delete genérico ambíguo.

---

### Catálogo fixo de categorias

Toda despesa DEVE usar uma categoria do catálogo oficial do MVP: Alimentação, Transporte, Moradia, Saúde, Lazer, Educação, Outros. O usuário NÃO DEVE criar, editar ou remover categorias no MVP.

**Racional**: RF-009, BR-010 — classificação estável para filtros e resumo sem gestão de taxonomia.

---

### Validação no servidor como fonte da verdade

O servidor DEVE validar todos os inputs (cadastro, login, despesa). Validação no client é complementar. Despesa DEVE ter descrição, valor > 0, data e categoria; registros incompletos ou inválidos NÃO DEVEM ser persistidos. Regras críticas de negócio e autorização por ownership DEVEM viver no servidor.

**Racional**: BR-004, BR-005, STACK — client não é autoridade de segurança ou integridade.

---

### Auditoria de ações críticas

O sistema DEVE registrar auditoria para: criação de conta; login com falha relevante (quando aplicável); criação, edição e arquivamento de despesa — com usuário, ação, data/hora e identificador do registro quando aplicável.

**Racional**: BR-011 e RNF de auditoria — rastreabilidade operacional mínima do MVP.

---

### Escopo MVP sem decisões financeiras

O sistema DEVE registrar e agregar despesas; NÃO DEVE recomendar investimentos, definir orçamento, importar extratos ou tomar decisões financeiras em nome do usuário. Proibido expandir o MVP para capacidades listadas como fora de escopo no PRD sem emenda explícita.

**Racional**: BR-013 e escopo do PRD — evita scope creep e mantém o produto como acompanhamento, não assessoria.

---

## Restrições de tecnologia e arquitetura

| Camada | Tecnologia | Padrões obrigatórios |
|--------|------------|----------------------|
| Frontend | Next.js (App Router) + React + TypeScript + Tailwind + shadcn/ui | UI simples; validação local complementar; dados via Server Actions/fetch da própria app |
| Backend | Next.js Server Actions e/ou Route Handlers (Node.js + TypeScript) | Validação server-side; ownership por recurso; erros em formato consistente; sem microsserviços |
| Armazenamento | SQLite + ORM/query builder compatível | UUID (ou equivalente não sequencial); datas em UTC; `archived_at` para despesas |
| Infra | Ambiente simples (Docker opcional) | Single tenant lógico por instalação; dados isolados por usuário na mesma base |
| Observabilidade | Logs estruturados no servidor | Correlação de requisição quando possível; falhas de auth e persistência registráveis |

### Padrões universais de entidade

Todas as entidades persistentes DEVEM incluir:
- `id` — chave primária (UUID ou equivalente não sequencial)
- `created_at` — timestamp (UTC)
- `updated_at` — timestamp (UTC)
- `archived_at` (ou equivalente) — apenas para Despesa; listagens ativas e resumos ignoram arquivadas

### Padrões obrigatórios

| Padrão | Regra |
|--------|-------|
| Soft delete | Despesa: arquivamento via `archived_at`; sem exclusão física imediata no MVP |
| Audit log | Auditoria nas ações críticas de BR-011 |
| Paginação | Listagens de despesas paginadas ou limitadas |
| Valores monetários | Valor da despesa > 0; representação consistente (ex.: decimal/centavos — detalhar no plano da feature) |
| Enums | Status: Ativa, Arquivada; Categorias: catálogo fixo do glossário |
| Linguagem de código | TypeScript |
| Linguagem de domínio | Termos canônicos do GLOSSARY (Despesa, Categoria, Resumo de despesas, Arquivar — evitar Gasto/Lançamento/Transação como sinônimo de registro) |

---

## Fluxo de desenvolvimento e quality gates

### Fluxo Spec-Driven

Todas as features DEVEM seguir: `coe-sdd-plan` → `coe-sdd-implement`. Seleção de artefatos por necessidade, não por tamanho estimado de escopo.
Sem implementação sem task em tasks.md. Sem task sem comando de gate.

### Expectativas de teste

| Escopo | Unit | Integration | E2E |
|--------|------|-------------|-----|
| Lógica de negócio | DEVE | — | — |
| Endpoints / Server Actions | DEVE | DEVE | — |
| Fluxos voltados ao usuário (P1) | — | DEVE | DEVE (Playwright) |
| Infraestrutura | — | DEVE | — |

### Checklist do gate de review

Antes de marcar qualquer marco `✅ done`:
- [ ] Todos os FR-* em spec.md têm tasks correspondentes marcadas `[x]`
- [ ] Todos os comandos de gate passam
- [ ] Ownership / isolamento aplicados a todas as novas operações de dados
- [ ] Entradas de auditoria criadas para operações que alteram estado (quando aplicável)
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

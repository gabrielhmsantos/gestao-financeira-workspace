# [NOME_DO_PROJETO]

**Visão:** [1–2 frases descrevendo o que o produto é e faz]
**Para:** [usuários-alvo]
**Resolve:** [problema central abordado]
**Refs da foundation:** PRD.md · BUSINESS-RULES.md · GLOSSARY.md · STACK.md

---

## Objetivos

<!-- Cada objetivo deve ter métrica de sucesso mensurável. -->
- [Objetivo principal — ex.: "Reduzir o tempo de agendamento em X%"]
- [Objetivo secundário — ex.: "Zero perda de dados em registros críticos"]

## Stack tecnológica

**Núcleo:**

- Frontend: [framework + versão]
- Backend: [framework + versão]
- Banco de dados: [nome]
- Runtime: [nome + versão]

**Dependências-chave:** [3–5 bibliotecas/frameworks críticos — ex.: Prisma, JWT, S3 SDK]

## Escopo

**O MVP inclui:**

<!-- Liste apenas capacidades que serão construídas no MVP. -->
- [Capacidade principal 1]
- [Capacidade principal 2]
- [Capacidade principal 3]

**Explicitamente fora de escopo:**

<!-- Seja preciso — exclusões vagas geram scope creep. -->
- [O que NÃO será construído e por quê]
- [O que NÃO será construído e por quê]

## Restrições

<!-- Preencha apenas o que realmente se aplica. Remova os demais. -->
- Técnicas: [se aplicável — ex.: "deve rodar na instância PostgreSQL existente"]
- Prazo: [se aplicável — ex.: "MVP até Q3 2026"]
- Recursos: [se aplicável — ex.: "2 engenheiros, sem QA dedicado"]

## Layout do workspace

<!-- Índice obrigatório do projeto (Modelo Operacional). Preenchido pelo coe-sdd-init — o usuário escolhe só A|B|C, não nomes de pastas. -->

**Repositório de controle:** este workspace (specs / SDD em `.specs/`).

**Layout adotado:** `[LAYOUT_CODE]` — `[LAYOUT_NAME]`

| Código | Nome | Forma |
|--------|------|--------|
| A | Submódulo na raiz | `workspace/<app>/` |
| B | Pasta agrupadora | `workspace/repositories/{frontend,backend,libs}/` |
| C | Por domínio | `workspace/repositories/{produto-a,produto-b}/` |

**Repositórios de código** (atualizar quando novos repos aparecerem sob o layout):

| Path | Stack | Responsabilidade |
|------|-------|------------------|
| [CODE_REPO_PATH] | [STACK] | [RESPONSIBILITY] |

**Manutenção:** Mantenha a tabela de repositórios de código atualizada. Assim que módulos/repos sob o layout adotado forem conhecidos ou descobertos, atualize esta seção **e** a rule da IDE (`coe-sdd-rule.mdc` / `CLAUDE.md` / `AGENTS.md`) com path, stack e responsabilidade. Quando novos repos aparecerem depois, atualize de novo antes do `coe-sdd-implement` neles.

**Rule da IDE:** gerada pelo `coe-sdd-init` a partir do template `coe-sdd-rule-template.md` (layout + Git). Não é a fonte da verdade só pelo ZIP do produto.

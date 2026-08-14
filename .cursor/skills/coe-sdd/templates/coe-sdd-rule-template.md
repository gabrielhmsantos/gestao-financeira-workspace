---
description: contexto de desenvolvimento spec-driven coe-sdd
alwaysApply: true
---

# coe-sdd — Contexto do projeto

Este projeto usa a skill **coe-sdd** para desenvolvimento orientado a especificações.

Este workspace é o **repositório de controle** (specs, roadmap, decisões). O código de aplicação vive em repositórios de código separados, sob o layout de workspace abaixo.

## Specs

Raiz canônica das specs: `.specs/`
Contexto do projeto (índice): `.specs/project/PROJECT.md`
Governança (vinculante): `.specs/project/CONSTITUTION.md`
Roadmap: `.specs/project/ROADMAP.md`
Estado / memória: `.specs/project/STATE.md`
Templates: `.specs/_templates/`
Foundation (input somente leitura): `.specs/foundation/`

Quando o usuário pedir para planejar, implementar ou gerir features, leia e siga a skill `coe-sdd`.
Planeje e implemente marco a marco (`coe-sdd-plan MN` → `coe-sdd-implement MN`).

Nunca modifique `.specs/foundation/` — é input externo, somente leitura.
Sempre respeite a CONSTITUIÇÃO.

**Idioma dos artefatos:** pt-BR (corpo e headings dos docs gerados a partir dos templates).

## Layout do workspace

**Layout adotado:** `[LAYOUT_CODE]` — `[LAYOUT_NAME]`

| Código | Nome | Forma |
|--------|------|--------|
| A | Submódulo na raiz | `workspace/<app>/` |
| B | Pasta agrupadora | `workspace/repositories/{frontend,backend,libs}/` |
| C | Por domínio | `workspace/repositories/{produto-a,produto-b}/` |

Documentado no índice do projeto: `.specs/project/PROJECT.md` (seção Layout do workspace).

### Mapa de repositórios de código

<!-- Paths relativos à raiz do workspace de controle. Preencha quando os repos existirem; remova linhas vazias. -->

| Path | Stack | Responsabilidade |
|------|-------|------------------|
| [CODE_REPO_PATH] | [STACK] | [RESPONSIBILITY] |

**Manutenção (obrigatória):** Mantenha o **Mapa de repositórios de código** (e a seção correspondente em `.specs/project/PROJECT.md`) atualizado.

- Assim que você **souber** ou **descobrir** módulos/repositórios de código sob o layout adotado (init, brownfield, plan, inspeção de disco, mensagem do usuário, etc.), atualize esta rule e o `PROJECT.md` com path, stack e responsabilidade — não espere o `coe-sdd-implement`.
- Quando **novos** repositórios de código aparecerem depois sob o mesmo layout, atualize de novo **antes** de rodar `coe-sdd-implement` neles.
- Nunca deixe repos conhecidos como placeholders (`[CODE_REPO_PATH]`) depois que o path for conhecido.

## Git

Feature branches (`coe-sdd-implement` apenas — não durante plan ou init):

- Padrão: `[GIT_PATTERN]`
- Tipo default: `[DEFAULT_TYPE]`
- `feature-folder` = basename sob `.specs/features/` (ex.: `M1-authentication-session`)
- Vocabulário de types alinhado aos types de commit em `coe-commit-pr-rule` (`feat`, `fix`, `docs`, `refactor`, `chore`, `test`, `perf`, `ci`, `build`, `style`)

Crie e alterne feature branches só dentro do **repositório de código** alvo da task — nunca use o repo de controle para branches de código de aplicação.

O `coe-sdd-implement` DEVE recusar trabalho de aplicação a menos que o repo de código já esteja numa branch que siga este padrão (nunca em `main`, `master`, `prod`, `hml` ou outras branches de ambiente/integração).

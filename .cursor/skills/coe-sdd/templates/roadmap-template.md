# Roadmap

**Marco atual:** [NOME_DO_PRIMEIRO_MARCO]
**Status:** Planejamento

---

<!-- Padrão de marco só-escopo (sem seção ### Features):
     Use **Escopo:** com bullets do que o marco cobre.
     coe-sdd-plan cria uma única pasta para o marco inteiro: .specs/features/{MN}-{slug}/
     M0 é o caso mais comum; qualquer marco sem ### Features segue o mesmo padrão.
     Brownfield: omita M0 ou marque ✅ done se a infra já existir. -->
## M0 — Bootstrap

**Objetivo:** [Scaffold, CI, conexão de BD, env — tornar o projeto executável]
**Dependências:** —

**Escopo:**

- [bullet de infra — ex.: setup monorepo, Docker Compose]
- [bullet de infra — ex.: Prisma + primeira migration]
- [bullet de infra — ex.: endpoint de healthcheck]
- [bullet de infra — ex.: lint, formatação, test runner]

---

<!-- Repita o bloco abaixo para cada marco.
     REGRAS PARA FEATURES:
     - Nomes DEVEM ser capacidades voltadas ao usuário (ex.: "Autenticação e Sessão", "RBAC", "Gestão de Pacientes").
     - NUNCA use nomes genéricos como "Backend", "API", "Services" ou "Camada de Banco".
     - Agrupe 2–5 itens RF-*/BR-* relacionados sob cada nome de feature.
     - Cada feature deve ser planejável de forma independente via coe-sdd-plan MN feature-name.
     REGRAS PARA BULLETS:
     - UM bullet por item RF-* ou BR-* — nunca agrupe várias refs num único bullet.
     - Comece cada bullet com o identificador: "RF-XXX descrição" ou "BR-XXX descrição". -->
## [NOME_M1]

**Objetivo:** [O que torna este marco entregável — uma frase]
**Alvo:** [Quem se beneficia e qual o resultado entregável — voltado ao usuário, não técnico]
**Dependências:** M0

### Features

**[NOME_FEATURE_1]** - NOT STARTED

- RF-XXX [descrição da capacidade — uma frase]
- BR-XXX [regra de negócio aplicada — uma frase]

**[NOME_FEATURE_2]** - NOT STARTED

- RF-XXX [descrição da capacidade — uma frase]
- RF-XXX [descrição da capacidade — uma frase]
- BR-XXX [regra de negócio aplicada — uma frase]

**[NOME_FEATURE_3]** - NOT STARTED

- RF-XXX [descrição da capacidade — uma frase]

---

<!-- Adicione um bloco ## por marco seguindo a mesma estrutura.
     VALORES DE STATUS (não use outros):
     - NOT STARTED: intenção no roadmap — pasta .specs/features/ ainda não existe
     - PLANNED:     coe-sdd-plan rodou — pasta + spec/plan/tasks criados
                    Inclua link após o status: PLAN ✅ → .specs/features/M1-authentication-session/
                    Exemplo só-escopo:         PLAN ✅ → .specs/features/M0-bootstrap/
     - COMPLETED:   coe-sdd-implement concluído — código entregue e verificado -->

---

## Considerações futuras

<!-- Itens explicitamente fora de escopo no PRD. Não invente — extraia da foundation. -->
- [Capacidade futura potencial da seção fora de escopo do PRD]
- [Capacidade futura potencial da seção fora de escopo do PRD]

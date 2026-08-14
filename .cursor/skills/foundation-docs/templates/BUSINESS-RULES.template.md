# BUSINESS-RULES

<!-- Cada regra usa ID BR-NNN, título imperativo e descrição clara. Regras devem ser testáveis e rastreáveis nas specs de feature. -->

## BR-001 — [Título da regra]

[Descrição da regra de negócio em 1–3 frases.]

[Consequência ou restrição derivada, se houver.]

## BR-002 — [Título da regra]

[Descrição da regra de negócio.]

[Lista de valores ou papéis oficiais, se aplicável:]

- [Valor ou papel 1]
- [Valor ou papel 2]
- [Valor ou papel N]

## BR-003 — [Título da regra]

[Descrição da regra de negócio.]

[Condições ou exceções explícitas, ex.: status que dispensam a regra.]

## BR-004 — [Título da regra — unicidade ou consistência de dados]

[Regra sobre duplicidade, integridade ou consistência dentro de um escopo (tenant, organização, etc.).]

## BR-005 — [Título da regra — preservação de histórico]

[O que não pode ser apagado em operação normal e por quê.]

## BR-006 — [Título da regra — arquivamento]

[Como arquivamento afeta registros relacionados e o histórico.]

## BR-007 — [Título da regra — fluxo de status ou ciclo de vida]

Status oficiais:

- [Status 1]
- [Status 2]
- [Status N]

Transições permitidas:

- [Status A] → [Status B]
- [Status B] → [Status C]
- [Status A] → [Status D]

<!-- Use diagrama ou tabela se o fluxo for complexo. -->

## BR-008 — [Título da regra — imutabilidade parcial]

[O que pode e o que não pode ser alterado após um estado terminal ou conclusão.]

## BR-009 — [Título da regra — cancelamento ou encerramento]

[Metadados obrigatórios ao cancelar ou encerrar um registro: motivo, responsável, data, etc.]

## BR-010 — [Título da regra — auditoria]

Devem gerar auditoria:

- [Ação crítica 1]
- [Ação crítica 2]
- [Ação crítica N]

## BR-011 — [Título da regra — permissões em relatórios ou visões agregadas]

[Quem vê o quê: escopo por papel ou por ownership.]

## BR-012 — [Título da regra — limite de domínio ou compliance]

[O que o sistema faz e explicitamente não faz — ex.: não toma decisões de domínio regulado.]

<!-- Adicione BR-NNN conforme novas regras forem identificadas. Mantenha IDs estáveis após publicação. -->

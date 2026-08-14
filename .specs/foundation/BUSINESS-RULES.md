# BUSINESS-RULES

## BR-001 — Exigir conta autenticada

Todo acesso a despesas, listagens e resumos exige usuário autenticado. Visitantes não autenticados não visualizam dados pessoais.

## BR-002 — Garantir unicidade de e-mail

O e-mail de cadastro deve ser único em todo o sistema. Tentativas de cadastro com e-mail já existente devem ser rejeitadas.

## BR-003 — Isolar dados por proprietário

Usuários não podem consultar, editar ou arquivar despesas de outros usuários. Toda consulta e mutação deve restringir-se às despesas do usuário autenticado.

## BR-004 — Exigir campos obrigatórios da despesa

Toda despesa deve possuir descrição, valor, data e categoria. Registros incompletos não podem ser persistidos.

## BR-005 — Exigir valor positivo

O valor da despesa deve ser maior que zero. Valores zero ou negativos são inválidos.

## BR-006 — Restringir mutação ao proprietário

Apenas o usuário proprietário da despesa pode editá-la ou arquivá-la.

## BR-007 — Controlar ciclo de vida da despesa

Status oficiais:

- Ativa
- Arquivada

Transições permitidas:

- Ativa → Arquivada

Despesas novas nascem como Ativa. Não há retorno de Arquivada para Ativa no MVP.

## BR-008 — Arquivar em vez de excluir fisicamente

A exclusão operacional de uma despesa é feita por arquivamento. Despesas arquivadas são preservadas no histórico e não são consideradas em listagens ativas, totais e resumos.

## BR-009 — Calcular resumo apenas no período e sobre ativas

Os valores do resumo devem ser calculados exclusivamente a partir das despesas ativas do usuário autenticado cuja data esteja no período selecionado.

## BR-010 — Usar apenas categorias do catálogo fixo

A categoria de uma despesa deve pertencer ao catálogo oficial do MVP:

- Alimentação
- Transporte
- Moradia
- Saúde
- Lazer
- Educação
- Outros

O usuário não cria, edita nem remove categorias no MVP.

## BR-011 — Auditar ações críticas

Devem gerar auditoria:

- Criação de conta
- Login com falha relevante (quando aplicável à política de logs)
- Criação de despesa
- Edição de despesa
- Arquivamento de despesa

## BR-012 — Restringir visão agregada ao próprio usuário

O resumo de despesas e demais visões agregadas exibem apenas dados do usuário autenticado. Não há papéis com visão cross-user no MVP.

## BR-013 — Não decidir além do cálculo de acompanhamento

O sistema registra e agrega despesas; não recomenda investimentos, não define orçamento, não importa extratos e não toma decisões financeiras em nome do usuário.

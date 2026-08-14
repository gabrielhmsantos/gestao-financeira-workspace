# GLOSSARY

## Controle de Despesas

Aplicação web de uso individual para registro e acompanhamento de despesas pessoais por período e categoria.

## Usuário

Pessoa física com conta autenticada no sistema. No MVP, é o único papel e possui acesso exclusivo aos próprios dados.

## Despesa

Registro de um gasto pessoal do usuário, contendo descrição, valor, data e categoria. É a entidade principal de negócio do produto.

### Evitar usar

- Gasto (como sinônimo de registro persistido)
- Lançamento
- Transação
- Movimentação

## Categoria

Classificador fixo que agrupa despesas para filtros e resumo. No MVP o catálogo é definido pelo sistema; o usuário não cria categorias.

Exemplos oficiais do MVP:

- Alimentação
- Transporte
- Moradia
- Saúde
- Lazer
- Educação
- Outros

## Status da despesa

Estado operacional de uma despesa na operação ativa versus arquivada.

Status oficiais do MVP:

- Ativa
- Arquivada

## Resumo de despesas

Visão agregada numérica das despesas ativas do usuário em um período: total gasto, quantidade de despesas, total por categoria e participação percentual de cada categoria no total.

## Período

Intervalo de datas usado para filtrar listagens e calcular o resumo. Opções do MVP: mês atual (padrão), mês anterior e período personalizado.

## Arquivar

Remoção da despesa da operação ativa sem exclusão física imediata. Despesa arquivada não aparece na listagem ativa nem entra nos totais e resumos.

## Auditoria

Registro de ações relevantes executadas por usuários no sistema (ex.: criação de conta, mutações de despesa), com metadados suficientes para rastreabilidade.

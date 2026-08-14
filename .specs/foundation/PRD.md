# PRD

## Produto

**Controle de Despesas** é uma aplicação web simples para pessoas físicas registrarem despesas pessoais e acompanharem um resumo dos gastos por período e categoria.

Cada usuário autentica-se e interage apenas com os próprios dados. Não há perfis administrativos nem compartilhamento de conta na primeira versão.

## Problema

Hoje, o acompanhamento de gastos pessoais costuma ocorrer em planilhas, aplicativos de notas ou sem qualquer registro estruturado. Isso dificulta saber quanto foi gasto em um período e quais categorias concentram a maior parte das despesas. Sem um registro único e filtrável, o usuário perde visibilidade e controle sobre o próprio consumo.

## Objetivo

Permitir que o usuário crie uma conta, registre e mantenha suas despesas classificadas por categoria, consulte-as com filtros e acompanhe o total gasto e a distribuição por categoria em um período selecionado — de forma rastreável e restrita aos próprios dados.

## Público-alvo

- Pessoas físicas que desejam controle simples de gastos pessoais
- Usuários individuais (sem compartilhamento familiar ou empresarial)
- Contexto de uso pessoal, sem necessidade de sistemas financeiros complexos

## Usuários

### Usuário

Pessoa física autenticada que cria conta, registra e mantém suas próprias despesas, consulta listagens com filtros e acompanha o resumo de gastos. Possui acesso exclusivo aos próprios registros; não há outros papéis no MVP.

## Escopo do MVP

- Criação de conta com nome, e-mail e senha
- Login e logout
- Cadastro, consulta, edição e exclusão (arquivamento) de despesas
- Classificação de despesas por categorias fixas
- Filtro de despesas por período e por categoria
- Resumo numérico: total no período, quantidade de despesas, total e participação por categoria
- Período padrão ao acessar o resumo: mês atual
- Isolamento total de dados por usuário

## Fora do escopo do MVP

- Controle de receitas
- Contas bancárias
- Cartões de crédito
- Parcelamento de despesas
- Despesas recorrentes
- Orçamento mensal
- Metas financeiras
- Importação de extratos
- Integração bancária / Open Finance
- Controle de investimentos
- Compartilhamento de conta entre usuários
- Controle financeiro empresarial
- Aplicativo mobile
- Painel administrativo
- Diferentes perfis ou níveis de permissão
- Criação de categorias pelo usuário
- Gráficos no resumo
- Alteração de senha dentro da aplicação
- Notificações
- Envio de e-mails
- Exportação de relatórios
- Inteligência artificial

## Capacidades principais

### Autenticação

Permitir que o usuário crie conta com nome, e-mail e senha, realize login e logout, e acesse apenas as próprias informações. O e-mail de cadastro é único.

### Gestão de despesas

Permitir cadastrar, consultar, editar e arquivar despesas pessoais com descrição, valor, data e categoria (do catálogo fixo), com filtros por período e categoria.

### Resumo de despesas

Apresentar visão numérica agregada das despesas ativas do usuário no período selecionado: total gasto, quantidade de registros, totais e participação percentual por categoria. Período padrão: mês atual; opções incluem mês anterior e período personalizado.

## Requisitos funcionais macro

### RF-001 — Criar conta

O sistema deve permitir criar uma conta informando nome, e-mail e senha, rejeitando e-mail já cadastrado.

### RF-002 — Autenticar e encerrar sessão

O sistema deve permitir login com e-mail e senha e logout, exigindo autenticação para acessar dados pessoais.

### RF-003 — Isolar dados por usuário

O sistema deve garantir que cada usuário visualize, consulte e altere apenas as próprias despesas e informações.

### RF-004 — Cadastrar despesa

O sistema deve permitir cadastrar uma despesa vinculada ao usuário autenticado, com descrição, valor maior que zero, data e categoria do catálogo fixo.

### RF-005 — Listar e filtrar despesas

O sistema deve listar as despesas ativas do usuário autenticado, com filtro por período e por categoria.

### RF-006 — Editar despesa

O sistema deve permitir que o proprietário edite descrição, valor, data e categoria de uma despesa ativa de sua titularidade.

### RF-007 — Arquivar despesa

O sistema deve permitir que o proprietário arquive uma despesa; despesas arquivadas não aparecem na listagem ativa nem entram nos totais e resumos.

### RF-008 — Consultar resumo por período

O sistema deve calcular e exibir, para o período selecionado (padrão: mês atual), o total gasto, a quantidade de despesas ativas e o total e a participação percentual por categoria, usando apenas despesas ativas do usuário autenticado.

### RF-009 — Exibir categorias fixas

O sistema deve disponibilizar o catálogo fixo de categorias do MVP para classificação de despesas: Alimentação, Transporte, Moradia, Saúde, Lazer, Educação e Outros.

## Requisitos não funcionais

### Segurança

- Acesso a informações pessoais exige autenticação
- Cada usuário acessa somente os próprios registros
- Senhas não são armazenadas em formato legível (hash)
- Sessão ou token deve expirar conforme política definida na implementação

### Privacidade

- Dados de despesas e perfil são visíveis apenas ao próprio usuário
- Remoção operacional de despesa ocorre por arquivamento (exclusão lógica), sem exclusão física imediata no MVP

### Performance

- Listagens de despesas devem ser paginadas ou limitadas de forma adequada ao volume de uso pessoal
- Listagem e resumo devem carregar de forma adequada para volume típico de uso individual

### Usabilidade

- Interface simples e objetiva
- Cadastro de despesa com poucos campos e fluxo rápido
- Total gasto no período selecionado facilmente identificável

### Auditoria

- Ações críticas devem ser registráveis: criação de conta, login (sucesso/falha relevante), criação, edição e arquivamento de despesa, com usuário, ação, data/hora e identificador do registro quando aplicável

### Observabilidade

- Logs estruturados no servidor para erros e falhas relevantes
- Falhas de autenticação e de persistência devem ser registradas de forma correlacionável

## Critérios de sucesso

- Usuário consegue criar conta e realizar login sem workaround
- Cada usuário acessa apenas os próprios dados
- Usuário consegue cadastrar, editar e arquivar despesas e consultá-las com filtros por período e categoria
- Sistema calcula corretamente o total gasto e a distribuição por categoria no período
- Operação básica é realizável sem treinamento
- Specs geradas pelo SDD são implementáveis sem redefinir o produto

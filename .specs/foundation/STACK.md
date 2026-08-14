# STACK

## Modelo de repositório

O projeto será criado como **aplicação única** em repositório Git (Next.js full-stack).

Compõe o repositório: interface web, camada de servidor (Server Actions / Route Handlers), acesso ao banco SQLite e testes end-to-end. Sem microsserviços no MVP.

## Linguagem principal

- TypeScript

## Frontend

- **Tipo de interface:** web
- **Framework ou plataforma:** Next.js com React
- **Linguagem:** TypeScript
- **Estilização / design system:** Tailwind CSS com componentes baseados em shadcn/ui
- **Formulários e entrada de dados:** formulários React alinhados ao padrão do projeto (campos de despesa e cadastro/login)
- **Validação no client:** validação local dos campos obrigatórios; servidor é a fonte da verdade
- **Estado e dados remotos:** dados via Server Actions / fetch ao backend da própria aplicação Next.js
- **Roteamento e navegação:** App Router do Next.js
- **Build e dependências:** toolchain Node.js / npm ou equivalente compatível com Next.js

## Backend

- **Runtime / linguagem:** Node.js com TypeScript
- **Framework ou arquitetura:** Next.js (Server Actions e/ou Route Handlers) na mesma aplicação
- **Estilo de API:** REST leve via Route Handlers e/ou Server Actions
- **Formato de troca de dados:** JSON
- **Validação de entrada:** validação no servidor (schema ou camada equivalente) para todos os inputs
- **Autenticação:** e-mail e senha com hash; sessão ou token gerenciado pela aplicação (ex.: Auth.js / solução equivalente no ecossistema Next.js)
- **Autorização:** ownership por recurso (cada despesa pertence a um usuário); sem RBAC multi-papel no MVP
- **Documentação de contrato:** contratos internos da aplicação; OpenAPI opcional se Route Handlers forem expostos de forma estável
- **Persistência e acesso a dados:** camada de acesso sobre SQLite (ORM ou query builder a definir na implementação, desde que compatível)

## Banco de dados

- **Banco principal:** SQLite
- **Camada de acesso:** ORM ou query builder compatível com SQLite e TypeScript
- **Identificadores:** UUID (ou equivalente não sequencial exposto)
- **Datas e timezone:** armazenamento em UTC; exibição conforme fuso do usuário ou política definida na implementação

## Infraestrutura

- **Containers / empacotamento:** opcional (Docker) se útil ao deploy; não obrigatório para desenvolvimento local
- **Ambiente de execução:** ambiente simples adequado ao escopo reduzido (local e hospedagem a detalhar em doc técnica posterior)
- **Proxy / gateway:** conforme hospedagem escolhida; não há API Gateway dedicado no MVP
- **Serviços gerenciados:** nenhum obrigatório além do runtime da aplicação e arquivo/volume do SQLite
- **Modelo de deploy:** single tenant lógico por instalação; dados isolados por usuário na mesma base

## Observabilidade

- **Logs do servidor:** logs estruturados com correlação de requisição quando possível
- **Logs do client:** captura de erros relevantes da interface conforme padrão do Next.js
- **Métricas e tracing:** não obrigatórios no MVP
- **Healthcheck:** endpoint ou verificação simples de disponibilidade da aplicação, se exigido pelo ambiente de deploy

## Testes

- **Testes end-to-end:** Playwright
- **Versionamento:** Git

## Padrões obrigatórios

- Entidades persistem `id`, `created_at` e `updated_at`
- Despesas usam `archived_at` (ou equivalente) para arquivamento; listagens ativas e resumos ignoram arquivadas
- Exclusão operacional de despesa é arquivamento; sem exclusão física imediata no MVP
- Regras críticas de negócio e autorização por ownership vivem no servidor
- Validação no client é complementar; validação no servidor é obrigatória
- Respostas de erro de API/Server Actions com formato consistente
- Listagens de despesas paginadas ou limitadas
- Eventos de auditoria nas ações críticas definidas em BUSINESS-RULES

## Integrações do MVP

Nenhuma integração externa confirmada para o MVP (sem e-mail, banco, Open Finance ou provedores de notificação).

## Restrições para o SDD

- Não propor outra linguagem principal que não TypeScript
- Não trocar o frontend principal (Next.js + React) nem o banco principal (SQLite) no MVP
- Não criar microsserviços nem aplicativo mobile no MVP
- Não introduzir compartilhamento de conta, multi-papel ou painel administrativo no MVP
- Gerar specs compatíveis com aplicação web full-stack Next.js e uso individual autenticado

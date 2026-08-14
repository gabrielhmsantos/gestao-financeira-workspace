# STACK

## Modelo de repositório

O projeto será criado como **[monorepo | multi-repo | outro]**.

[Descreva o que compõe o repositório: aplicações, serviços, workers, bibliotecas compartilhadas, etc.]

## Linguagem principal

- [Linguagem(s) e versão(ões), se relevante]

<!-- Use esta seção quando houver uma linguagem dominante. Para stacks poliglota, detalhe por camada nas seções abaixo. -->

## Frontend

<!-- Preencha apenas o que existir no MVP. Remova linhas não aplicáveis.
     Um único client (ex.: só web): preencha esta seção normalmente.
     Web + mobile (ou outros clients): duplique o bloco ## Frontend inteiro — um por superfície — ou descreva cada client inline nos campos (ex.: "Web: Next.js | Mobile: Flutter").
     Contratos compartilhados (API, auth, schemas, design tokens) ficam no Backend ou em Padrões obrigatórios. -->

- **Tipo de interface:** [web | mobile nativo | mobile híbrido | desktop | CLI | outro]
- **Framework ou plataforma:** [ferramenta principal de UI ou renderização]
- **Linguagem:** [se diferente da linguagem principal]
- **Estilização / design system:** [CSS, biblioteca de componentes, tokens, etc.]
- **Formulários e entrada de dados:** [biblioteca ou abordagem para forms e máscaras]
- **Validação no client:** [biblioteca ou mecanismo de validação local]
- **Estado e dados remotos:** [cache, requisições, sincronização com API]
- **Roteamento e navegação:** [se aplicável]
- **Build e dependências:** [gerenciador de pacotes, bundler, toolchain]

## Backend

- **Runtime / linguagem:** [ex.: JVM, .NET, Node, Python, Go, Ruby]
- **Framework ou arquitetura:** [web framework, microsserviço mínimo, serverless, etc.]
- **Estilo de API:** [REST | GraphQL | gRPC | RPC interno | eventos | outro]
- **Formato de troca de dados:** [JSON | Protobuf | XML | outro]
- **Validação de entrada:** [biblioteca, schema ou camada de validação]
- **Autenticação:** [sessão, JWT, OAuth, API key, SSO, etc.]
- **Autorização:** [RBAC, ABAC, ACL, políticas por recurso, etc.]
- **Documentação de contrato:** [OpenAPI, GraphQL schema, protobuf, etc.]
- **Persistência e acesso a dados:** [ORM, query builder, driver nativo, repositórios]

## Banco de dados

- **Banco principal:** [relacional, documento, key-value, etc.]
- **Camada de acesso:** [ORM, query builder, SQL direto, driver]
- **Identificadores:** [UUID, ULID, sequencial, composto]
- **Datas e timezone:** [política de armazenamento, ex.: UTC no banco]

## Cache e filas

- **Cache:** [Redis, Memcached, in-memory, CDN, etc.]
- **Filas / mensageria:** [RabbitMQ, SQS, Kafka, Redis Streams, etc.]
- **Worker / processamento assíncrono:** [runtime, fila consumida, scheduler]

<!-- Remova esta seção se o MVP não usar cache ou processamento assíncrono. -->

## Infraestrutura

- **Containers / empacotamento:** [Docker, imagens, etc.]
- **Ambiente de execução:** [VPS, cloud, on-premise, PaaS]
- **Proxy / gateway:** [Nginx, Traefik, API Gateway, load balancer]
- **Serviços gerenciados:** [banco, cache, filas, storage, etc.]
- **Modelo de deploy:** [single tenant, multi-tenant, por cliente, etc.]

## Observabilidade

- **Logs do servidor:** [formato, destino, correlação]
- **Logs do client:** [como erros da interface são capturados e reportados]
- **Métricas e tracing:** [se aplicável]
- **Healthcheck:** [endpoint, probe ou mecanismo de verificação]

## Padrões obrigatórios

- [Convenção de campos em entidades, ex.: id, created_at, updated_at]
- [Convenção de arquivamento, ex.: archived_at]
- [Política de exclusão vs. arquivamento]
- [Onde regras críticas devem viver — ex.: camada de servidor]
- [Fronteira de validação entre client e servidor]
- [Formato de resposta de API e tratamento de erros]
- [Paginação em listagens]
- [Eventos de auditoria em alterações críticas]

## Integrações do MVP

- [Integração 1]: [provedor e protocolo]
- [Integração 2]: [provedor e protocolo]

<!-- Liste apenas integrações confirmadas para o MVP. -->

## Restrições para o SDD

- [Restrição 1 — ex.: não propor outra stack]
- [Restrição 2 — ex.: não trocar banco ou framework principal]
- [Restrição 3 — ex.: não criar microserviços]
- [Restrição 4 — ex.: modelo de implantação fixo]
- [Restrição 5 — ex.: gerar specs compatíveis com o contexto de deploy]

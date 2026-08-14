# STACK (observado)

**Mapeado em:** [DATE]
**Raiz do código:** [CODE_ROOT]

<!-- Stack observada no repositório existente.
     NÃO copie a STACK.md da foundation às cegas — documente o que o código realmente usa.
     Remova seções não usadas. Nunca deixe [placeholders] no .specs/codebase/STACK.md final. -->

## Linguagens e runtimes

- **Linguagem(ns) principal(is):** [LANGUAGE + VERSION]
- **Runtime(s):** [ex.: Node 20, JVM 21, .NET 8]

## Layout de pacotes / workspace

- **Modelo:** [monorepo | multi-repo | pacote único]
- **Ferramentas:** [pnpm workspaces | npm | yarn | Maven | Cargo | …]
- **Apps / pacotes observados:** [lista com paths]

## Frontend (se existir)

- **Framework:** [ex.: Next.js App Router]
- **UI / estilo:** [Tailwind, CSS modules, …]
- **Estado / data fetching:** […]
- **Validação no client:** […]

<!-- Remova esta seção se não houver frontend. -->

## Backend (se existir)

- **Framework:** [ex.: Fastify, Nest, Spring]
- **Estilo de API:** [REST | GraphQL | …]
- **Validação:** [Zod, class-validator, …]
- **Auth (observada):** […]

<!-- Remova esta seção se não houver backend. -->

## Armazenamento de dados

- **BD principal:** [Postgres, …]
- **ORM / camada de acesso:** [Drizzle, Prisma, …]
- **Migrations:** [ferramenta + local]
- **Cache / filas (se houver):** […]

## Build, lint, format

- **Build:** [comandos / ferramenta]
- **Lint / format:** [ESLint, Prettier, Biome, …]
- **Typecheck:** […]

## Deploy / runtime (observado)

- **Como roda hoje:** [Docker, PaaS, scripts, …]
- **Padrão de env / config:** [.env, arquivos de config, …]

## Bibliotecas relevantes

| Área | Biblioteca | Onde observada |
|------|------------|----------------|
| [área] | [pkg] | [path] |

## Divergência da STACK da foundation (se houver)

- [ITEM]: foundation diz X; o codebase usa Y — [path de origem]

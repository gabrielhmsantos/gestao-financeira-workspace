# TESTING (observado)

**Mapeado em:** [DATE]
**Raiz do código:** [CODE_ROOT]

<!-- Documente como este repo realmente testa e quais comandos de gate devem passar.
     coe-sdd-plan / tasks.md devem ecoar os comandos de gate deste arquivo.
     Nunca deixe [placeholders] no .specs/codebase/TESTING.md final. -->

## Política (como praticada)

- **Unit:** [o que recebe testes unitários]
- **Integration:** [o que recebe testes de integração]
- **E2E:** [o que recebe E2E; ferramenta]
- **Explicitamente não testado hoje:** […]

## Ferramentas

| Camada | Ferramenta | Path de config |
|--------|------------|----------------|
| Unit | [Vitest, Jest, …] | [path] |
| Integration | […] | [path] |
| E2E | [Playwright, Cypress, …] | [path] |

## Onde os testes moram

- [padrão + paths de exemplo]

## Comandos de gate

<!-- Comandos de shell concretos que devem passar antes de marcar tasks como feitas. -->

| Propósito | Comando |
|-----------|---------|
| Typecheck / build | `[cmd]` |
| Unit | `[cmd]` |
| Integration | `[cmd]` |
| E2E (se usado como gate) | `[cmd]` |
| Lint | `[cmd]` |

## Fixtures / BD de teste

- **Abordagem:** [in-memory, docker, BD de teste compartilhado, mocks]
- **Setup / teardown:** [path ou script]

## Expectativas de cobertura (se houver)

- [Limiar observado ou “nenhum enforced”]

## Lacunas

- [Cobertura faltante de que tasks futuras devem estar cientes]

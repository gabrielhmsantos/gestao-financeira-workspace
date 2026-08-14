# CONVENTIONS (observado)

**Mapeado em:** [DATE]
**Raiz do código:** [CODE_ROOT]

<!-- Extraia naming e estilo de 5–10 arquivos representativos — observado, não aspiracional.
     Nunca deixe [placeholders] no .specs/codebase/CONVENTIONS.md final. -->

## Naming

- **Arquivos:** [padrão + exemplos]
- **Funções / métodos:** [padrão + exemplos]
- **Tipos / interfaces:** [padrão + exemplos]
- **Variáveis / constantes:** [padrão + exemplos]
- **Tabelas / colunas de BD:** [padrão + exemplos, se aplicável]
- **Rotas / recursos de API:** [padrão + exemplos]

## Imports e fronteiras de módulo

- **Ordem de import / alias:** [ex.: `@intranet/db`, relativo dentro do pacote]
- **Imports cross-package permitidos:** [regras observadas]
- **Acoplamento proibido (se enforced):** […]

## Organização de arquivos / pastas

- **Dentro de uma feature / módulo:** [padrão de layout]
- **Co-localização de testes:** [ao lado | `__tests__` | `tests/`]

## Tratamento de erros

- **Formato lançado / retornado:** [ex.: ErrorEnvelope `{ error: { code, message } }`]
- **Onde definido:** [path]
- **Logging em falha:** […]

## Tipos e validação

- **Fonte da verdade dos schemas:** [path]
- **Tipos compartilhados vs locais do app:** […]

## Formatação / lint (observado)

- **Formatter:** [ferramenta + path de config]
- **Linter:** [ferramenta + path de config]
- **Regras notáveis que o codebase realmente segue:** […]

## Exemplos (apenas ponteiros)

- [convenção]: `[path:symbol]` ou `file` (L10-25)
- [convenção]: […]

# ARCHITECTURE (observado)

**Mapeado em:** [DATE]
**Raiz do código:** [CODE_ROOT]

<!-- Documente padrões arquiteturais e fluxo de dados como existem no repo.
     Prefira nomes concretos de módulos e paths a diagramas abstratos sozinhos.
     Nunca deixe [placeholders] no .specs/codebase/ARCHITECTURE.md final. -->

## Estilo

- **Estilo geral:** [em camadas | modular monolith | microservices | hexagonal | …]
- **Regras de fronteira (observadas):** [ex.: API é dona do Zod; web não importa db]

## Módulos / pacotes principais

| Módulo | Path | Responsabilidade |
|--------|------|------------------|
| [nome] | [path] | [o que possui] |

## Fluxo de request / dados

<!-- Descreva o caminho feliz de uma escrita típica e de uma leitura típica. -->

1. [Ponto de entrada — ex.: rota HTTP / ação de UI]
2. [Próxima camada]
3. [Persistência / chamada externa]
4. [Resposta / efeitos colaterais]

## Preocupações transversais

- **AuthN / AuthZ:** [onde é aplicado]
- **Erros / envelopes:** [padrão + path]
- **Logging / correlação:** […]
- **Multi-tenancy (se houver):** [como o tenant é escopado]

## Padrões em uso

- [Padrão]: [onde — ex.: repository em packages/db]
- [Padrão]: […]

## Anti-padrões / hotspots de acoplamento

- [Observação]: [path] — [por que importa para o trabalho futuro]

<!-- Dívida sistêmica vai para CONCERNS.md; mantenha esta seção curta. -->

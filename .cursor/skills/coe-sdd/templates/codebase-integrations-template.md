# INTEGRATIONS (observado)

**Mapeado em:** [DATE]
**Raiz do código:** [CODE_ROOT]

<!-- Doc brownfield opcional. Omita o arquivo inteiro se não houver integrações
     externas relevantes. Prefira evidência de código/config a docs de marketing.
     Nunca deixe [placeholders] no .specs/codebase/INTEGRATIONS.md final. -->

## Serviços externos

| Serviço | Propósito | Client / path do SDK | Config / secrets |
|---------|-----------|----------------------|------------------|
| [nome] | […] | [path] | [chaves de env — só nomes] |

## Entrada (inbound)

- **Webhooks:** [paths de endpoint + verificação]
- **Callbacks / redirects OAuth:** […]

## Saída (outbound)

- **Clients HTTP:** [base URLs da config — sem secrets]
- **Filas / eventos publicados:** […]

## Contratos

- **OpenAPI / schemas no repo:** [paths]
- **Compartilhados com consumidores:** […]

## Modos de falha (tratamento observado)

- [Serviço]: [timeout / retry / fallback — path]

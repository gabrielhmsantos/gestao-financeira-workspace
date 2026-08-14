---
name: das-creator
description: Gera um DAS (Documento de Arquitetura de Solução) em Markdown, documento que descreve como uma demanda/projeto será resolvido arquiteturalmente — escopo, jornadas, sistemas impactados e desenho da solução, com diagramas Mermaid embutidos. Use quando o usuário pedir para "gerar DAS", "criar DAS", "das-creator", "documento de arquitetura de solução", ou pedir um DAS para um projeto ou feature.
disable-model-invocation: true
metadata:
  version: 1.1.0
---

# das-creator

Gera um DAS em Markdown a partir do contexto disponível (input do usuário e/ou
`.specs/foundation/`), preenchendo [`templates/DAS.template.md`](templates/DAS.template.md).
Diagramas usam Mermaid embutido no próprio arquivo, seguindo o guide autocontido
[`references/diagrams.md`](references/diagrams.md). Esta skill é autônoma: não
depende de nenhum arquivo ou skill fora deste diretório.

## O que é um DAS

Um DAS é o documento de arquitetura de solução: descreve, para uma demanda ou
projeto, o escopo de negócio, as jornadas/fluxos envolvidos, os sistemas
impactados e o desenho técnico da solução (nível de contexto e de container).
Não é um documento de implementação detalhada — é a ponte entre a visão de
negócio e a integração entre sistemas.

## O que produz

Um único arquivo `.specs/das/<nome>.md` (cria a pasta se não existir). Sem pasta
`diagrams/`, sem PNG — os diagramas ficam embutidos como blocos ` ```mermaid ` no
próprio Markdown.

## Estrutura do documento

Segue [`templates/DAS.template.md`](templates/DAS.template.md) e o mapa de
seções em [`references/structure.md`](references/structure.md):

1. Título H1: `DAS <identificador> - PROJETO <nome do projeto>`
2. Histórico do documento
3. Projetos que referenciam este documento
4. 1. Visão do Escopo
5. 2. Visão da Solução (por jornada, com diagrama de contexto)
6. 3. Considerações (3.1 Pontos de atenção / 3.2 Dependências)
7. 4. Descrição do impacto
8. 5. Desenho da solução (por jornada, com diagrama de container/sequência)
9. 6. Mapeamento de Recursos Sistêmicos
10. 7. Documentos relacionados
11. 8. Anexos
12. 9. Links Relacionados

## Workflow

Copie este checklist e acompanhe o progresso:

```
DAS Progress:
- [ ] Fase 1: Resolver origem do contexto
- [ ] Fase 2: Extrair conteúdo e identificar gaps
- [ ] Fase 3: Entrevista pontual (só gaps)
- [ ] Fase 4: Outline (título, nome do arquivo, jornadas) + aprovação
- [ ] Fase 5: Gerar diagramas Mermaid
- [ ] Fase 6: Escrever .specs/das/<nome>.md
```

### Fase 1: Resolver origem do contexto

- Se o usuário informou uma origem explícita (documento, texto colado,
  identificador de projeto/ticket, link, etc.), use-a como fonte primária.
- Caso o usuário **não** informe nenhuma origem, leia `.specs/foundation/`:
  `PRD.md`, `GLOSSARY.md`, `BUSINESS-RULES.md`, `STACK.md`. Se essa pasta não
  existir ou estiver vazia, avise o usuário e pergunte a origem antes de continuar.

### Fase 2: Extrair conteúdo e identificar gaps

Extraia da origem, seguindo os campos descritos em
[`references/structure.md`](references/structure.md):

- Identificador do projeto/demanda (ex.: PTI/ticket) e nome da feature/release.
- Escopo (público-alvo, tipos de solicitação/pedido, prioridades, o que
  entra/não entra).
- Jornadas (uma por fluxo relevante), cada uma com: breve descrição, sistemas
  envolvidos, e o impacto por sistema (Impactos Mapeados).
- Pontos de atenção e dependências (projeto, arquiteto responsável, descrição).
- Sistemas/componentes impactados (IC) e o tipo de impacto (novo, alterado,
  reuso).
- Recursos sistêmicos usados/alterados (tecnologia, ambiente, responsável de
  desenvolvimento/sustentação/produção).

Marque cada bloco acima como preenchido ou lacuna. Não invente dados — jornadas,
sistemas ou responsáveis sem base na origem ficam como lacuna.

### Fase 3: Entrevista pontual

Pergunte **apenas** sobre lacunas, uma pergunta por vez, com uma sugestão quando
fizer sentido (ex.: nome do arquivo, próxima versão do documento). Não repita
perguntas cuja resposta já esteja na origem.

### Fase 4: Outline + aprovação

Antes de escrever o arquivo final, apresente ao usuário:

- Título H1 proposto.
- Nome de arquivo proposto (ver [Naming do arquivo](#naming-do-arquivo)).
- Lista das jornadas identificadas (uma linha cada).
- Lacunas que ficarão marcadas como "Não informado" no documento, se houver.

Só prossiga para a Fase 5 depois que o usuário aprovar ou pedir ajustes (repita a
Fase 4 até aprovação). Nunca grave o arquivo antes desse gate.

### Fase 5: Gerar diagramas Mermaid

Siga [`references/diagrams.md`](references/diagrams.md) para os padrões e
exemplos de cada tipo de diagrama: para cada jornada, gere um diagrama de
Contexto em §2 e um diagrama de Container (e, se houver troca de
mensagens/API entre sistemas, também um de Sequência, incluindo caminho de
erro/compensação quando houver ponto de atenção conhecido) em §5. Use
[`references/symbols.md`](references/symbols.md) para escolher os símbolos
semânticos de cada nó e aplique `classDef` de alto contraste conforme
`diagrams.md`. Um diagrama = um conceito — não acumule múltiplos conceitos em
um único diagrama.

### Fase 6: Escrever o arquivo

Preencha [`templates/DAS.template.md`](templates/DAS.template.md) substituindo
todo `<<placeholder>>` por conteúdo real e removendo os comentários HTML de
orientação. Onde uma seção do template for inaplicável ao caso (ex.:
"Projetos que referenciam este documento" sem nenhum), mantenha o heading e
escreva "Não aplicável" — não remova a seção. Grave em `.specs/das/<nome>.md`,
criando a pasta se necessário.

### Exportar para PDF (sob demanda)

Não faz parte do fluxo padrão acima — as Fases 1-6 sempre produzem apenas o
`.md`. Só execute este passo se o usuário pedir explicitamente um PDF do
documento gerado. Use [`scripts/das_to_pdf.py`](scripts/das_to_pdf.py):

```bash
python .agents/skills/das-creator/scripts/das_to_pdf.py .specs/das/<nome>.md
```

O script renderiza os diagramas Mermaid e gera `.specs/das/<nome>.pdf` ao lado
do `.md`. Detalhes, pré-requisitos e troubleshooting em
[`references/pdf-export.md`](references/pdf-export.md).

## Naming do arquivo

- Prefixo `DAS-`.
- Inclua o identificador do projeto/demanda se conhecido (ex.: `PTI1234`, um
  código de ticket, ou qualquer identificador que a origem fornecer).
- Slug kebab-case do nome da feature/release (sem espaços, acentos ou
  caracteres inválidos de sistema de arquivos).
- Exemplo: `DAS-PTI1234-alertas-multicanal-release-01.md`.
- Se o usuário fornecer um nome de arquivo explícito, use-o em vez do gerado.
- Nunca use literalmente `DAS.md` como nome de saída.

## Fora de escopo (YAGNI)

- Publicação em wiki/Confluence ou geração de links reais para ferramentas de
  arquitetura externas.
- Geração de documentos técnicos de integração detalhados (fora do nível de
  arquitetura de solução).
- Exportação para PNG/SVG isolado dos diagramas ou validação via `mmdc` fora
  do contexto do PDF — os diagramas ficam embutidos como Mermaid no Markdown
  por padrão. PDF do documento completo é suportado sob demanda via
  [`scripts/das_to_pdf.py`](scripts/das_to_pdf.py) (ver seção acima); outros
  formatos (DOCX, wiki) continuam fora de escopo.
- Handoff automático para outras skills ou pipelines.

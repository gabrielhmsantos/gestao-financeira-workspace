# Estrutura do DAS — mapa de seções, campos e guidance

Referência autocontida das seções, tabelas e textos-guia do modelo de DAS. Use
ao preencher [`templates/DAS.template.md`](../templates/DAS.template.md); não
é necessário nenhum arquivo externo a este diretório.

## Cabeçalho

- **H1:** `DAS <identificador> - PROJETO <Nome do Projeto>`
  - O identificador (ex.: "PTI 1234") é o código do projeto/demanda que a
    origem fornecer; se não houver, use o nome curto do projeto.
- Logo abaixo do H1, sem heading próprio: uma linha com o identificador e o
  nome do projeto repetidos (linha de subtítulo, útil quando o H1 fica muito
  longo). Pode ser omitida se o H1 já for suficientemente descritivo.

## Histórico do documento

Tabela: `Data | Versão | Autor | Nota Revisão`.

- Data no formato `DD Mon AAAA` (ex.: `08 Jan 2026`).
- Versão evolui de forma incremental: `0.001` (versão inicial) → `0.01`,
  `0.02`, ... até uma versão promovida (ex.: `1.0`).
- Nota Revisão é uma frase curta descrevendo a mudança daquela versão (ex.:
  "Versão inicial.", "Ajuste no fluxo de integração.").
- Ao gerar um DAS novo, use apenas uma linha: `0.001` / "Versão inicial." com a
  data atual, salvo se o usuário fornecer histórico anterior.

## Projetos que referenciam este documento

Tabela: `Projeto/PTI | Nome do Projeto | Gerente do Projeto | Data da Solicitação | Tipo de Relacionamento`.

Uso: quando outro projeto reaproveita esta solução, registre aqui qual
projeto está indicando a opção de reuso. Normalmente vazia em documentos
novos — mantenha o heading e a tabela com uma linha "Não aplicável" se não
houver dado.

## 1. Visão do Escopo

Texto livre indicando a finalidade/propósito do documento — o porquê da
elaboração desta solução. Cobrir, quando aplicável:

- Interpretação da visão de negócio em visão sistêmica (o que precisa ser
  desenvolvido por TI).
- Objetivo a ser alcançado com a entrega da solução.
- Contexto de entrega (restrições de orçamento e prazo).
- Condições que limitam a validade da solução (prazo, atualização
  tecnológica, obsolescência dos sistemas envolvidos).

Não é seção com tabela.

## 2. Visão da Solução

Desdobramento da solução por jornadas, épicos e funcionalidades, sempre
baseado em um observador/ator. Uma subseção `2.N Jornada N: <nome>` por
jornada, cada uma com:

1. **Breve Descrição da Jornada** — texto livre explicando gatilho →
   processamento → resultado.
2. **Diagrama de Contexto** — diagrama Mermaid nível C1/Context embutido (ver
   [`diagrams.md`](diagrams.md)), evidenciando o impacto principal em
   integração/TI.
3. **Container de Referência** — link ou nome do processo/container que a
   jornada usa (pode ser reaproveitado entre jornadas).
4. **Impactos Mapeados** — tabela `Sistema | Processo | Impacto | Descrição`
   com os sistemas e impactos mapeados conforme o diagrama de contexto.
   - Valores comuns de Impacto: "Desenvolvimento e Testes", "Teste".

## 3. Considerações

Objetivo: mapear observações relevantes para a elaboração do documento.

### 3.1 Pontos de atenção

Tabela: `Ponto | Descrição`. Temas que mereçam atenção do time e da
organização (ex.: tempo de resposta dos sistemas envolvidos, sistemas sem
equipe de manutenção ativa, sistemas departamentais). "Ponto" normalmente
referencia uma jornada (ex.: "Jornada 2").

### 3.2 Dependências

Tabela: `PTI | Projeto | Arquiteto de soluções | Descrição da dependência`.
Registra iniciativas em curso, planejadas, não iniciadas ou concluídas que
criam dependências funcionais/técnicas com a solução em questão. Vazia se não
houver dependências conhecidas.

## 4. Descrição do impacto

Tabela: `Sistema | IC (Item de Configuração) | Tipo de Impacto`. Lista os
sistemas que precisam ser customizados, configurados ou parametrizados e que
requerem alocação de recursos para análise — consolida, em nível de sistema,
o que a seção 2 já detalhou por jornada.

## 5. Desenho da solução

Detalhamento de cada jornada que gere impacto no desenvolvimento de sistemas,
no nível de Contêiner (Nível 2). Espelha a seção 2: uma subseção `5.N Jornada N: <nome>`
por jornada, na mesma ordem e com o mesmo número N, cada uma com:

- **Contexto de Referência** — link ou nome do contexto correspondente da
  seção 2.
- **Diagrama Container** — diagrama Mermaid nível C2/Container embutido (ver
  [`diagrams.md`](diagrams.md)).
- Se a jornada envolver troca de mensagens/API entre sistemas, adicionar
  também um diagrama de sequência.

## 6. Mapeamento de Recursos Sistêmicos

Tabela: `Item | Tecnologia | Descrição do Recurso | Reuso/Novo/Alterado | Ambiente | Responsável Desenvolvimento | Responsável Sustentação | Responsável Produção`.
Uso conjunto entre arquitetura de solução e arquitetura de integração, para
manter o documento alinhado com a especificação de desenvolvimento.

## 7. Documentos relacionados

Lista de documentos DAS anteriores com relação direta com a solução sendo
desenhada (link ou caminho do arquivo).

## 8. Anexos

Lista de documentos anexos que refletem ou influenciam a solução.

## 9. Links Relacionados

Lista de links para conteúdos relacionados com a solução ou projeto.

## Regras gerais

- Nunca remover uma seção do template, mesmo vazia — todas as 9 seções +
  histórico + projetos referenciados devem estar presentes.
- Numeração de subseções (2.N, 5.N) deve ser consistente entre a Visão da
  Solução e o Desenho da solução: a jornada N em 2.N é a mesma jornada N em
  5.N.
- Nomes de sistemas devem ser os nomes reais fornecidos pelo usuário/origem —
  nunca inventar siglas de sistema.

<!--
Template DAS (Documento de Arquitetura de Solução). Espelha a estrutura, os
campos e os textos-guia do modelo de referência desta skill. Substitua todo
<<placeholder>> por conteúdo real e remova os comentários HTML de orientação.
Mantenha todos os headings mesmo quando a seção for "Não aplicável" — não
remova seções para preservar a estrutura do documento.
-->

# DAS <<identificador>> - PROJETO <<Nome do Projeto>>

<!--
Sumário (opcional): a maioria dos visualizadores de Markdown gera um índice
automaticamente a partir dos headings; inclua um sumário manual apenas se o
destino de publicação não suportar isso.
-->

## Histórico do documento

| Data | Versão | Autor | Nota Revisão |
|------|--------|-------|---------------|
| <<DD Mon AAAA>> | <<0.001>> | <<Autor>> | <<Versão inicial.>> |

## Projetos que referenciam este documento

<!--
Utilizar este quadro em situações de reuso, onde nos campos abaixo deverá ser
informado o projeto atual o qual está sendo indicado a opção de reuso da
solução existente.
-->

| Projeto/PTI | Nome do Projeto | Gerente do Projeto | Data da Solicitação | Tipo de Relacionamento |
|---|---|---|---|---|
| <<Projeto/PTI>> | <<Nome do Projeto>> | <<Gerente do Projeto>> | <<DD Mon AAAA>> | <<Tipo de Relacionamento>> |

## 1. Visão do Escopo

<!--
Neste tópico o arquiteto deverá indicar qual a finalidade ou propósito deste
documento (o porquê da elaboração desta solução). Temas principais a serem
abordados:
- Interpretação da visão de negócio em visão sistêmica: o que precisa ser
  desenvolvido por TI;
- Qual o objetivo a ser alcançado com a entrega desta solução;
- Em qual contexto a solução está sendo entregue, incluindo restrições sobre
  orçamento e prazo;
- Condições que permitem a validade da solução (prazo, atualização
  tecnológica, obsolescência dos sistemas envolvidos).
-->

<<Descrever a proposta do projeto e o escopo (público-alvo, tipo de
solicitação/pedido coberto, prioridade/fase, se houver)>>

## 2. Visão da Solução

<!--
Neste tópico o arquiteto deverá indicar como se pretende atender a demanda
solicitada. Deve ser feito um desdobramento da solução por jornadas, épicos e
funcionalidades. É através desta visão geral que os diagramas deverão ser
apresentados. Temas principais a serem considerados:
- Inserir diagramas nível C1 - Contexto;
- Definir a visão sempre baseada em um observador ou ator, o qual permita
  apresentar um comportamento sistêmico;
- Evidenciar o impacto principal em TI (integração) e, principalmente, onde
  haverá desenvolvimento sistêmico.

Repita o bloco 2.N abaixo para cada jornada identificada.
-->

### 2.<<N>> Jornada <<N>>: <<Nome da Jornada>>

**Breve Descrição da Jornada:**

<<Descrição da Jornada>>

**Diagrama de Contexto:**

```mermaid
<<Diagrama C4 Context relacionado com a jornada — ver references/diagrams.md>>
```

**Container de Referência:** <<link ou nome do container>>

**Impactos Mapeados:**

| Sistema | Processo | Impacto | Descrição |
|---|---|---|---|
| <<Sistema>> | <<Processo>> | <<Desenvolvimento e Testes / Teste / N/A>> | <<Descrição do impacto>> |

## 3. Considerações

<!-- O objetivo deste tópico é mapear observações relevantes para a elaboração do documento. -->

### 3.1 Pontos de atenção

<!--
Trata-se de temas relevantes que mereçam atenção do time e da própria
organização. Exemplo: tempo de resposta dos sistemas envolvidos; sistemas sem
equipes de manutenção ou desenvolvimento em atividade; sistemas considerados
departamentais; etc.
-->

| Ponto | Descrição |
|---|---|
| <<Jornada N>> | <<Descrição do ponto de atenção>> |

### 3.2 Dependências

<!--
Investigar se existe alguma iniciativa em curso ou planejada que afeta a
solução que está sendo desenhada, incluindo iniciativas que ainda não
começaram ou concluíram e que criam dependências funcionais e técnicas com a
solução em questão.
-->

| PTI | Projeto | Arquiteto de soluções | Descrição da dependência |
|---|---|---|---|
| <<PTI>> | <<Projeto>> | <<Arquiteto>> | <<Descrição>> |

## 4. Descrição do impacto

<!--
Neste tópico o arquiteto de soluções deverá informar os sistemas impactados
pela solução a ser adotada. Entende-se como impacto o sistema que deverá ser
customizado, configurado ou parametrizado e que tenha necessidade de
alocação de recursos para análise.
-->

| Sistema | IC (Item de Configuração) | Tipo de Impacto |
|---|---|---|
| <<Sistema>> | <<IC>> | <<Novo/Alterado/Reuso>> |

## 5. Desenho da solução

<!--
Neste tópico o arquiteto de soluções deverá apresentar de forma detalhada
cada jornada que corresponda a um desenho de solução que gere impacto no
desenvolvimento de sistemas. O nível de Contêiner (Nível 2) deve ser
considerado nesta fase.

Repita o bloco 5.N abaixo para cada jornada da seção 2, na mesma ordem e com
o mesmo número N.
-->

### 5.<<N>> Jornada <<N>>: <<Nome da Jornada>>

**Contexto de Referência:** <<link ou nome do contexto>>

**Diagrama Container:**

```mermaid
<<Diagrama C4 Container relacionado com a jornada — ver references/diagrams.md>>
```

<!-- Se a jornada envolver troca de mensagens/API entre sistemas, inclua também um diagrama de sequência. -->

```mermaid
<<Diagrama de sequência, quando aplicável — ver references/diagrams.md>>
```

## 6. Mapeamento de Recursos Sistêmicos

<!--
Este bloco é de uso conjunto entre o arquiteto de soluções e o arquiteto de
integração. O objetivo deste mapeamento é deixar o documento de soluções
alinhado e sincronizado com a especificação para desenvolvimento.
-->

| Item | Tecnologia | Descrição do Recurso | Reuso/Novo/Alterado | Ambiente | Responsável Desenvolvimento | Responsável Sustentação | Responsável Produção |
|---|---|---|---|---|---|---|---|
| <<Item>> | <<Tecnologia>> | <<Descrição>> | <<Reuso/Novo/Alterado>> | <<Ambiente>> | <<Responsável>> | <<Responsável>> | <<Responsável>> |

## 7. Documentos relacionados

<!--
Utilizar este tópico para referenciar documentos (DAS) anteriores que possuem
relação direta com a solução que está sendo desenhada. Inclua o link ou o
caminho do arquivo.
-->

- <<Documento relacionado 1>>

## 8. Anexos

<!-- Incluir como anexo (ou referência a) todos os documentos que refletem ou influenciam na respectiva solução. -->

- <<Anexo 1>>

## 9. Links Relacionados

<!-- Incluir links para todos os conteúdos relacionados com a solução ou projeto. -->

- <<Link 1>>

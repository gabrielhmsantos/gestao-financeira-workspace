# Guia de diagramas Mermaid para o DAS

Guia autocontido para os diagramas embutidos no DAS. Não depende de nenhum
arquivo fora deste diretório. Para os símbolos usados nos exemplos abaixo, veja
[`symbols.md`](symbols.md).

## Quando usar cada tipo

| Seção do DAS | Campo | Diagrama | Quando |
|---|---|---|---|
| §2 Visão da Solução (por jornada) | "Diagrama de Contexto" | C4 Context / Nível C1 (flowchart) | Sempre — um por jornada |
| §5 Desenho da solução (por jornada) | "Diagrama Container" | C4 Container / Nível C2 (flowchart) | Sempre — um por jornada, refinando o Context correspondente |
| §5 Desenho da solução (adicional) | — | Sequência (sequenceDiagram) | Quando a jornada envolve troca explícita de mensagens/eventos/API entre dois ou mais sistemas |

Regra: **um diagrama = um conceito**. Nunca combine Context e Container da
mesma jornada no mesmo bloco Mermaid — são blocos separados em §2 e §5, ligados
pelos campos "Container de Referência" (em §2) e "Contexto de Referência" (em
§5).

## C4 Context (nível §2)

Mostra a jornada como processo: o sistema em foco, os atores que interagem com
ele e os sistemas externos dos quais ele depende — sem detalhar componentes
internos.

**Inclua:**
- O sistema da jornada (uma única caixa, dentro de uma fronteira/subgraph).
- Atores/personas que interagem com o sistema.
- Sistemas externos dos quais o sistema depende.
- Relacionamentos e protocolos/canais usados em cada seta.

```mermaid
flowchart TB
    Ator([👤 Ator/Cliente])
    Operador([👤 Operador/Administrador])

    subgraph "Fronteira do sistema"
        Sistema[⚙️ Sistema principal da jornada]
    end

    Externo1[🌐 Sistema externo 1]
    Externo2[📧 Sistema externo 2]
    Externo3[📊 Sistema externo 3]

    Ator -->|"Aciona a jornada<br/>Consulta status"| Sistema
    Operador -->|"Administra/configura<br/>Consulta relatórios"| Sistema

    Sistema -->|"Integração/consulta<br/>REST/HTTPS"| Externo1
    Sistema -->|"Notificação/evento<br/>SMTP"| Externo2
    Sistema -->|"Registra métricas"| Externo3

    Externo1 -->|"Retorno/callback"| Sistema

    classDef ator fill:#FFE66D,stroke:#F08C00,color:#000
    classDef principal fill:#4ECDC4,stroke:#0B7285,color:#fff
    classDef externo fill:#A8DADC,stroke:#1864AB,color:#000

    class Ator,Operador ator
    class Sistema principal
    class Externo1,Externo2,Externo3 externo
```

**Características-chave:**
- Uma única caixa para o sistema em foco.
- Fronteira do sistema explícita (`subgraph`).
- Todos os atores e sistemas externos relevantes aparecem.
- Protocolos/canais de comunicação rotulados nas setas.
- Nem todo Context precisa dos três sistemas externos do exemplo — use quantos
  a jornada realmente tiver (mínimo um: o próprio ator).

## C4 Container (nível §5)

Refina o Context correspondente mostrando os componentes/serviços internos do
sistema principal da jornada: aplicações, serviços de backend, bancos de
dados, cache e integrações com sistemas externos.

**Inclua:**
- Aplicações web/mobile que iniciam a jornada.
- Serviços de backend (API, serviço de negócio, workers).
- Bancos de dados e cache.
- Fila de mensagens/eventos, se a jornada usar mensageria assíncrona.
- Tecnologia de cada container (linguagem/framework, porta, protocolo).

```mermaid
flowchart TB
    Ator([👤 Ator/Cliente<br/>Web/Mobile])

    subgraph SistemaPrincipal["Sistema principal da jornada"]
        direction TB

        API[🚪 API/Gateway<br/>Tecnologia X<br/>Porta 443]

        subgraph "Serviços"
            ServicoA[⚙️ Serviço de negócio<br/>Tecnologia Y]
        end

        Dados[(💾 Base de dados<br/>Tecnologia Z)]
        Cache[(⚡ Cache<br/>Redis)]
    end

    Externo1[📬 Sistema externo 1]

    Ator -->|"HTTPS"| API
    API -->|"Roteia requisição"| ServicoA
    ServicoA --> Dados
    ServicoA --> Cache
    ServicoA -->|"Integração/evento<br/>REST/AMQP"| Externo1

    classDef gateway fill:#F38181,stroke:#C92A2A,color:#fff
    classDef servico fill:#4ECDC4,stroke:#0B7285,color:#fff
    classDef dados fill:#A8DADC,stroke:#1864AB,color:#000
    classDef externo fill:#D4A5A5,stroke:#7D4E57,color:#fff

    class API gateway
    class ServicoA servico
    class Dados,Cache dados
    class Externo1 externo
```

**Rótulos de tecnologia:** sempre inclua, quando conhecido:
- Linguagem/framework do serviço.
- Porta (se relevante para integração).
- Tecnologia do banco/cache.
- Protocolo de comunicação (REST, AMQP, SOAP, etc.).

## Sequência (nível §5, quando aplicável)

Use quando for necessário mostrar a ordem temporal das chamadas entre
sistemas — especialmente jornadas com API síncrona, mensageria assíncrona, ou
um ponto de atenção conhecido (conflito, retry, indisponibilidade).

### Elementos básicos

Participantes aparecem como linhas de vida verticais:

```mermaid
sequenceDiagram
    participant Cliente as 👤 Cliente
    participant Frontend as 🌐 Frontend
    participant SistemaA as ⚙️ Sistema A
    participant Dados as 💾 Base de dados

    Cliente->>Frontend: Aciona ação
    Frontend->>SistemaA: Envia requisição
    SistemaA->>Dados: Grava registro
    Dados-->>SistemaA: Sucesso
    SistemaA-->>Frontend: Confirmação
    Frontend-->>Cliente: Exibe confirmação
```

**Tipos de participante:**

| Símbolo | Tipo | Exemplo |
|---|---|---|
| 👤 | Pessoa/ator | Cliente, Operador |
| 🌐 | Web/frontend | App web, navegador, app mobile |
| ⚙️ | Serviço/backend | API, microsserviço |
| 💾 | Base de dados | PostgreSQL, MongoDB, Redis |
| 📬 | Fila de mensagens | RabbitMQ, Kafka, SQS |
| 🔐 | Serviço de autenticação | OAuth, Auth0, Keycloak |
| 🚪 | Gateway | API Gateway, Load Balancer |

**Tipos de mensagem** — síncrona, assíncrona e chamada interna:

```mermaid
sequenceDiagram
    participant A as ⚙️ Sistema A
    participant B as ⚙️ Sistema B

    Note over A,B: Chamada síncrona
    A->>B: Requisição síncrona (seta sólida)
    B-->>A: Resposta (seta pontilhada)

    Note over A,B: Mensagem assíncrona
    A--)B: Mensagem assíncrona (seta aberta)

    Note over A,B: Chamada interna
    A->>A: Chamada de método interno
```

**Caixas de ativação** — mostram quando um participante está processando
ativamente. Todo `+` que abre uma ativação precisa de um `-` correspondente
que a fecha na mesma linha de vida:

```mermaid
sequenceDiagram
    participant Cliente as 👤 Cliente
    participant SistemaA as ⚙️ Sistema A
    participant Dados as 💾 Base de dados

    Cliente->>+SistemaA: Consulta dados
    Note over SistemaA: Sistema A está ativo
    SistemaA->>+Dados: Consulta registro
    Note over Dados: Base de dados está ativa
    Dados-->>-SistemaA: Resultado
    Note over SistemaA: Sistema A ainda ativo
    SistemaA-->>-Cliente: Resposta + dados
    Note over Cliente,SistemaA: Ambos voltam a ficar ociosos
```

**Indicar síncrono vs. assíncrono** — use estilos de seta diferentes:

- **Seta sólida `->>`:** síncrono (espera resposta).
- **Seta aberta `--)`:** assíncrono (dispara e não espera).
- **Seta pontilhada `-->>`:** retorno/resposta.

```mermaid
sequenceDiagram
    participant SistemaA as ⚙️ Sistema A
    participant Fila as 📬 Fila
    participant Worker as ⚙️ Worker

    SistemaA->>Fila: Chamada síncrona (espera ACK)
    Fila-->>SistemaA: ACK
    Fila--)Worker: Entrega assíncrona (sem espera)
```

### Caminho feliz

```mermaid
sequenceDiagram
    actor Cliente as 👤 Cliente
    participant Frontend as 🌐 Frontend
    participant SistemaA as ⚙️ Sistema A
    participant Dados as 💾 Base de dados

    Cliente->>Frontend: Preenche e envia formulário
    Frontend->>+SistemaA: Aciona a jornada<br/>{dados de entrada}
    Note over SistemaA: Valida a requisição

    SistemaA->>SistemaA: Valida regras de negócio
    SistemaA->>+Dados: Verifica existência do registro
    Dados-->>-SistemaA: Não existe

    SistemaA->>+Dados: Grava novo registro
    Dados-->>-SistemaA: {id gerado}

    SistemaA-->>-Frontend: Sucesso<br/>{id, dados confirmados}
    Frontend->>Cliente: Exibe confirmação
```

### Caminho de erro/compensação

Use quando a jornada tiver um ponto de atenção conhecido (ligue ao campo
"Pontos de atenção" em §3.1 do DAS) — conflito de concorrência, validação que
pode falhar, ou indisponibilidade de um sistema externo:

```mermaid
sequenceDiagram
    participant Cliente as 👤 Cliente
    participant SistemaA as ⚙️ Sistema A
    participant SistemaB as 💾 Sistema B

    Cliente->>+SistemaA: Atualiza registro<br/>{dados, versão: 5}
    Note over SistemaA: Cliente envia a versão atual

    SistemaA->>+SistemaB: Atualiza registro<br/>SE versão = 5
    Note over SistemaB: Só atualiza se a versão bater

    alt Versão confere (sem conflito)
        SistemaB-->>-SistemaA: Registro atualizado
        SistemaA-->>-Cliente: Sucesso<br/>{registro, nova versão}

    else Versão não confere (conflito)
        SistemaB-->>SistemaA: Nenhuma linha afetada
        SistemaA-->>Cliente: Erro — recurso alterado por outro processo
        Note over Cliente: Cliente deve buscar<br/>a versão mais recente e tentar novamente
    end
```

## Regras obrigatórias

- **Alto contraste:** todo `classDef` deve incluir a propriedade `color:`
  explícita. Fundo claro → texto escuro; fundo escuro → texto claro.
- **IDs sem espaços:** use camelCase ou PascalCase nos IDs dos nós (ex.:
  `SistemaPrincipal`, não `Sistema Principal`).
- **Rótulos com caracteres especiais:** envolva em aspas duplas quando a label
  tiver parênteses, vírgulas ou dois-pontos (ex.: `A["Processo (principal)"]`).
- **Nunca use `;` em texto de mensagem/`Note` de `sequenceDiagram`:** mesmo
  fora de colchetes, `;` é interpretado como separador de statement e quebra o
  diagrama. Use vírgula, travessão ou ponto no lugar (veja
  [Erros comuns](#erros-comuns)).
- **Símbolos semânticos (Unicode):** use para reforçar o tipo de nó — veja o
  guia completo em [`symbols.md`](symbols.md).
- **Nomes reais:** substitua os nomes genéricos do exemplo (Sistema A, Sistema
  externo 1, etc.) pelos nomes reais fornecidos pela origem do DAS.

## Erros comuns

### Palavras reservadas como identificador

Palavras como `end`, `style`, `class`, `subgraph`, `click`, `graph`,
`default`, `classDef`, `linkStyle`, `call` quebram o parser quando usadas sem
aspas como ID de nó.

Incorreto:
```mermaid
flowchart TD
    start --> end
    call --> style
```

Correto:
```mermaid
flowchart TD
    start --> "end"
    "call" --> "style"
```

### Caracteres especiais não escapados

Aspas duplas, parênteses, colchetes, chaves, barra invertida, dois-pontos,
vírgula, `#`, `%` e `@` em rótulos precisam estar entre aspas duplas.

Incorreto:
```mermaid
flowchart TD
    A[Diz "olá"]
    B[Objeto(x,y)]
```

Correto:
```mermaid
flowchart TD
    A["Diz #34;olá#34;"]
    B["Objeto(x,y)"]
```

Regra prática: quando tiver dúvida, envolva o rótulo inteiro em aspas duplas.

### Ponto-e-vírgula em texto de mensagem/Note (sequenceDiagram)

Em `sequenceDiagram`, `;` funciona como separador de statement — igual a uma
quebra de linha — **mesmo dentro do texto de uma mensagem ou `Note`**, e mesmo
sem colchetes. Envolver em aspas não resolve (o texto de mensagem/Note não é
um label entre colchetes). O parser corta a linha no `;` e o restante do texto
sobra como um statement inválido, geralmente com erro `... got 'NEWLINE'` uma
ou duas linhas depois do `;` real.

Incorreto:
```mermaid
sequenceDiagram
    participant A as ⚙️ Sistema A
    A->>A: Nada
    Note over A: Motivo opcional; sem reabertura no MVP
```

Correto (evite `;` no texto — troque por vírgula, travessão ou ponto):
```mermaid
sequenceDiagram
    participant A as ⚙️ Sistema A
    A->>A: Nada
    Note over A: Motivo opcional, sem reabertura no MVP
```

Alternativa (se o `;` for indispensável no texto): use a entidade `#59;` em
vez do caractere literal, ex.: `Note over A: Motivo#59; sem reabertura`. Na
prática, prefira reescrever a frase sem `;` — é mais legível.

### Sintaxe inválida de classDef

`classDef` não aceita chaves `{}` nem ponto-e-vírgula — apenas pares
`propriedade:valor` separados por vírgula ou espaço.

Incorreto:
```mermaid
flowchart TD
    classDef minhaClasse {
        fill: #ff0000;
        stroke: #333;
    }
```

Correto:
```mermaid
flowchart TD
    classDef minhaClasse fill:#ff0000,stroke:#333,color:#fff
```

### Ativação (+/-) sem pareamento

Cada `+` que abre uma caixa de ativação (`->>+Participante`) precisa de um `-`
correspondente que a fecha (`-->>-Participante`) mais adiante na mesma linha
de vida. Ativação aberta sem fechamento (ou fechada sem ter sido aberta) quebra
o diagrama ou deixa a caixa "vazando" visualmente até o fim.

Incorreto:
```mermaid
sequenceDiagram
    Cliente->>+SistemaA: Requisição
    SistemaA-->>Cliente: Resposta
```

Correto:
```mermaid
sequenceDiagram
    Cliente->>+SistemaA: Requisição
    SistemaA-->>-Cliente: Resposta
```

## Fora do padrão deste DAS

- Não gerar arquivos `.mmd` separados nem pasta `diagrams/` como parte do
  fluxo padrão — os diagramas ficam embutidos como blocos ` ```mermaid ` no
  próprio `.md`.
- Exportar o documento completo para PDF é suportado sob demanda via
  [`../scripts/das_to_pdf.py`](../scripts/das_to_pdf.py) (que internamente usa
  `mmdc` para renderizar cada diagrama) — ver
  [`pdf-export.md`](pdf-export.md). Não é um passo automático das Fases 1-6;
  só roda se o usuário pedir explicitamente um PDF.

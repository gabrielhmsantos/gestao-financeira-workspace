# Exportar o DAS para PDF

Guia autocontido para [`scripts/das_to_pdf.py`](../scripts/das_to_pdf.py), o
script que converte o `.md` do DAS (com diagramas Mermaid embutidos) em PDF.
Essa exportação é **sob demanda** — só é executada se o usuário pedir
explicitamente um PDF; não faz parte do fluxo padrão de geração do DAS.

## Como funciona

1. Renderiza **todos** os blocos ` ```mermaid ` do markdown para SVG em uma
   única chamada de `mmdc` (`@mermaid-js/mermaid-cli`, modo nativo de
   Markdown: `-i doc.md -o doc.md -a diagrams/`) — isso abre **um único**
   navegador Chrome/Chromium para todos os diagramas, e o próprio `mmdc` já
   devolve uma cópia do markdown com os blocos Mermaid substituídos por
   referências de imagem para os SVGs gerados.
2. Converte essa cópia para PDF com `md-to-pdf`, aplicando
   [`assets/pdf-style.css`](../assets/pdf-style.css) por padrão.
3. Limpa o diretório temporário — só o `.pdf` final permanece no destino.

Nenhum arquivo intermediário (`.svg`, markdown temporário) é deixado ao lado
do `.md` original, a menos que `--keep-temp` seja usado.

Para os passos 1 e 2, o script prefere binários instalados **globalmente**
(`mmdc`/`md-to-pdf` no PATH) e só cai para `npx --yes <pacote>` como
fallback — ver "Instalação recomendada" abaixo.

> **Nota de design:** uma versão anterior deste script chamava `mmdc` uma vez
> *por diagrama* (um `puppeteer.launch()` por bloco Mermaid). Isso multiplicava
> por N o risco de um launch de Chrome lento/travado sob carga do sistema,
> antivírus escaneando o processo, etc. — foi a causa raiz de travamentos
> observados em produção mesmo com o binário global instalado. O modo nativo
> de Markdown do `mmdc` (usado hoje) resolve isso abrindo o navegador uma
> única vez para todos os diagramas do documento.

## Instalação recomendada (uma vez por máquina)

```bash
npm install -g @mermaid-js/mermaid-cli md-to-pdf
```

Isso evita que cada execução do script dependa do `npx` resolver a árvore de
dependências pela rede (lento e, em redes corporativas restritas, pode travar
por minutos). Com os binários globais instalados, o pipeline completo (~15
diagramas) roda em cerca de 15-20 segundos. Sem eles, o script ainda funciona
via `npx`, mas a primeira chamada pode ser bem mais lenta.

## Pré-requisitos

- **Node.js >= 18** no PATH. Verifique com `node --version`.
- **`mmdc` e `md-to-pdf` instalados globalmente** (recomendado, ver acima) ou
  **`npm`/`npx` no PATH** como fallback.
- **Internet** só é necessária (a) na primeira vez que `npx` busca um pacote
  que não está instalado globalmente, ou (b) se nenhum Chrome/Edge local for
  encontrado (veja abaixo) e o Puppeteer precisar baixar seu próprio Chromium
  (~300MB, uma única vez).
- **Um navegador Chrome/Edge/Chromium instalado é opcional, mas recomendado**:
  o script detecta automaticamente uma instalação existente (Windows: Chrome
  ou Edge em `Program Files`; macOS/Linux: `google-chrome`, `chromium`,
  `microsoft-edge` no PATH ou nos caminhos padrão de instalação) e a reusa via
  `executablePath` do Puppeteer, evitando o download de um Chromium dedicado.
  **Sem um Chrome/Edge local detectado, o Puppeteer do `md-to-pdf` pode ficar
  travado indefinidamente tentando localizar/baixar um Chromium em redes
  restritas** (sem erro nem timeout visível) — instale um navegador local ou
  informe um caminho com `--chrome-path` para evitar esse cenário.

## Uso

```bash
# Básico — gera DAS-foo.pdf ao lado de DAS-foo.md
python .agents/skills/das-creator/scripts/das_to_pdf.py .specs/das/DAS-foo.md

# Caminho de saída customizado
python .agents/skills/das-creator/scripts/das_to_pdf.py .specs/das/DAS-foo.md --output out/DAS-foo.pdf

# Tema escuro nos diagramas
python .agents/skills/das-creator/scripts/das_to_pdf.py .specs/das/DAS-foo.md --theme dark

# Forçar um executável de navegador específico
python .agents/skills/das-creator/scripts/das_to_pdf.py .specs/das/DAS-foo.md --chrome-path "/usr/bin/chromium"

# Manter o diretório temporário (diagramas .svg + markdown intermediário) para depuração
python .agents/skills/das-creator/scripts/das_to_pdf.py .specs/das/DAS-foo.md --keep-temp
```

## Troubleshooting

**`ERROR: Node.js not found on PATH`**
Instale o Node.js e garanta que está no PATH da sessão atual.

**Primeira execução demorada, ou travada sem erro**
Se `mmdc`/`md-to-pdf` não estiverem instalados globalmente, o script usa
`npx --yes <pacote>`, que resolve a árvore de dependências pela rede a cada
chamada — em redes corporativas restritas isso pode demorar minutos ou até
travar sem erro visível (o processo Node fica parado, sem gerar processo de
Chrome, sem consumir CPU). Resolva instalando os binários globalmente:

```bash
npm install -g @mermaid-js/mermaid-cli md-to-pdf
```

O script detecta e usa esses binários automaticamente na próxima execução
(sem precisar de `npx`).

**`mmdc failed rendering diagrams`**
Normalmente é um erro de sintaxe Mermaid em algum bloco do documento — confira
contra [`diagrams.md`](diagrams.md) (seção "Erros comuns") antes de tentar de
novo. A mensagem de erro do `mmdc` costuma indicar a linha do markdown
original onde o bloco problemático começa.

**Comando `mmdc`/`md-to-pdf` trava sem erro, sem gerar processo de Chrome**
Verifique se algum arquivo de configuração JSON passado com `-p`/
`--config-file` não tem um BOM (byte order mark) no início — isso faz o
`JSON.parse` do Node falhar ou, em alguns casos, o processo ficar esperando
indefinidamente. O próprio script sempre escreve esses arquivos sem BOM; esse
problema só aparece se você gerar o config manualmente (ex.: via
`Set-Content -Encoding utf8` no PowerShell, que adiciona BOM por padrão —
use `-Encoding ascii` ou `[System.IO.File]::WriteAllText(...)` para testes
manuais).

**PDF gerado sem os diagramas**
Confira se `mmdc` realmente gerou os `.svg` (`--keep-temp` + olhar a pasta
`diagrams/`, que também contém o markdown intermediário já com as referências
de imagem).

**Diagrama cortado no meio, entre duas páginas**
Isso é o que [`assets/pdf-style.css`](../assets/pdf-style.css) evita por
padrão: a regra `img { max-height: 230mm; ... }` garante que nenhum diagrama
seja mais alto do que uma página A4 imprimível, para que ele sempre caiba
inteiro numa página nova em vez de ser cortado no meio quando não há espaço
suficiente na página atual. Se você estiver usando um `--stylesheet`
customizado sem essa regra, ou um `pdf_options.format` diferente de A4, ajuste
o `max-height` do seu CSS de acordo (altura da página menos as margens
configuradas em `convert_to_pdf`).

**Diagrama muito largo e com texto pequeno**
Diagramas muito largos (muitos nós lado a lado, ou `sequenceDiagram` com
muitos participantes) são reduzidos para caber na largura da página
(`max-width: 100%`), o que pode deixar o texto pequeno. Nesses casos, considere
reescrever o diagrama com orientação `LR`→`TB` ou quebrá-lo em mais de um
diagrama.

**Nenhum Chrome/Edge encontrado**
O script avisa e deixa o Puppeteer baixar seu próprio Chromium (requer
internet, ~300MB, uma única vez). Para evitar isso, instale o Google Chrome
ou o Microsoft Edge, ou informe manualmente o caminho de um Chromium existente
com `--chrome-path`.

## Fora de escopo

- Capa, cabeçalho/rodapé com marca, numeração de página customizada — o PDF
  sai com estilo neutro de leitura ([`pdf-style.css`](../assets/pdf-style.css)).
- Outros formatos de saída (DOCX, HTML standalone, PPTX).
- Instalação automática de `mmdc`/`md-to-pdf` — o script detecta e reusa
  instalações globais existentes, mas nunca instala pacotes globais por
  conta própria; isso é uma ação manual e única do usuário (ver "Instalação
  recomendada" acima).

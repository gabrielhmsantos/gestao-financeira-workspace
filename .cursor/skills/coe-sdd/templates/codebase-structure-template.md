# STRUCTURE (observado)

**Mapeado em:** [DATE]
**Raiz do código:** [CODE_ROOT]

<!-- Doc brownfield opcional. Omita o arquivo inteiro se a árvore for trivial.
     Mostre só paths relevantes — ignore node_modules, dist, ruído de lockfile.
     Nunca deixe [placeholders] no .specs/codebase/STRUCTURE.md final. -->

## Árvore (relevante)

```
[CODE_ROOT]/
├── [dir]/          # [papel]
│   └── …
├── [dir]/
└── …
```

## Cola de paths

| Path | Papel |
|------|-------|
| [path] | [o que vive aqui] |

## Pontos de entrada

- **Web / UI:** [path]
- **API / server:** [path]
- **Workers / jobs:** [path ou n/a]
- **CLI / scripts:** [path ou n/a]

## Áreas geradas / ignoradas

- [paths que agentes não devem tratar como fonte da verdade]

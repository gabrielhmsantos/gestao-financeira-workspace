# Quickstart: Bootstrap (M0)

**Marco:** M0 | **Código:** `apps/web`

---

## Pré-requisitos

- Node.js LTS compatível com a versão do Next.js escolhida no scaffold
- npm
- Git (submódulo `apps/web` inicializado)

## Setup

```bash
cd apps/web
cp .env.example .env
npm install
npx prisma migrate deploy
```

## Desenvolvimento

```bash
npm run dev
```

Abrir [http://localhost:3000](http://localhost:3000) — página placeholder em pt-BR.

## Health

```bash
curl -s http://localhost:3000/api/health
```

Esperado: HTTP 200 e JSON com `status: "ok"` e `timestamp` UTC.

## Qualidade

```bash
npm run lint
npm test
npx playwright test
```

Esperado: lint limpo na base; Vitest verde (inclui smoke DB); Playwright smoke do health verde.

## Build

```bash
npm run build
```

Esperado: build de produção sem erro.

## Critério de aceite manual do marco

- [ ] App sobe com `npm run dev`
- [ ] Health 200
- [ ] Migration baseline aplicada; sem models Usuário/Despesa
- [ ] Lint + Vitest + Playwright smoke passam

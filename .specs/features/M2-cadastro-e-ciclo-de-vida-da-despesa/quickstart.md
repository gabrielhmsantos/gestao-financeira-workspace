# Quickstart: Cadastro e ciclo de vida da despesa (M2)

```bash
cd apps/web
npx prisma migrate deploy
npm run dev
```

1. Login → `/despesas/nova`
2. Cadastrar Despesa válida (categoria do catálogo, valor > 0)
3. Editar campos
4. Arquivar — confirmar que não há DELETE no banco (`archived_at` preenchido)
5. Tentar editar arquivada — rejeitado

```bash
npm test
npx playwright test
```

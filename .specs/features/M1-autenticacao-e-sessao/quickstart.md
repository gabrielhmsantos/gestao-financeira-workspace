# Quickstart: Autenticação e sessão (M1)

## Pré-requisitos

- M0 concluído (`npm run dev`, Prisma, health OK)
- Migration M1 aplicada

```bash
cd apps/web
npx prisma migrate deploy
npm run dev
```

## Jornada manual

1. Abrir `/cadastro` — criar conta (nome, e-mail novo, senha ≥8)
2. Confirmar sessão iniciada (área autenticada acessível)
3. Logout — áreas protegidas bloqueadas
4. `/login` com credenciais corretas — acesso restaurado
5. Login com senha errada — mensagem genérica; sem vazamento de `password_hash`

## Testes

```bash
npm test
npx playwright test
```

## Aceite

- [ ] E-mail duplicado rejeitado
- [ ] Senha nunca legível no banco
- [ ] Audit de registro e falha de login presentes

# Quickstart: Isolamento por usuário (M1)

## Pré-requisitos

- Features M0 + Autenticação e sessão implementadas

## Validação

1. Criar usuários A e B
2. Autenticar como A; obter id de recurso de B (fixture/teste)
3. Tentar ler/mutar como A → **404**
4. Listar como A → só itens de A
5. Logout → áreas de dados inacessíveis

```bash
cd apps/web
npm test -- isolation
npx playwright test isolation
```

## Aceite

- [ ] Sem vazamento cross-user
- [ ] Helpers documentados para M2

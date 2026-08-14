# Contrato de ownership (UI/Server)

**Feature:** M1-isolamento-por-usuario
**Tipo:** contrato interno (não HTTP OpenAPI completo)

---

## requireUser()

- **Entrada:** sessão Auth.js corrente
- **Saída:** `{ id, email, name }` do Usuário autenticado
- **Erro:** se ausente/expirada → `UnauthorizedError` (mapeado a 401 ou redirect `/login`)

## assertOwnership(resourceUserId, actorUserId)

- **Precondição:** ambos UUIDs
- **Comportamento:** se diferentes → `NotFoundError` (404)
- **Proibido:** retornar o recurso do outro usuário

## Regras para Server Actions / queries

1. Obter `user` via `requireUser()` no início
2. Em `create`: setar `user_id` **somente** de `user.id` (ignorar body)
3. Em `find/update/archive`: `where: { id, userId: user.id }`
4. Em agregações: sempre `where: { userId: user.id, ... }`

## Rotas (middleware)

| Padrão | Visitante | Autenticado |
|--------|-----------|-------------|
| `/login`, `/cadastro`, `/api/health`, `/api/auth/*` | permitido | permitido |
| Demais rotas de app de dados | redirect `/login` | permitido |

## Códigos

| Situação | Código |
|----------|--------|
| Sem sessão | 401 / redirect |
| Recurso de outro / inexistente | 404 |
| Validação de input | 400 |

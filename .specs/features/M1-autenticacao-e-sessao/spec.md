# Spec: Autenticação e sessão

**Marco:** M1 | **Status:** planejado | **Depende de:** M0-bootstrap
**Refs da foundation:** RF-001 · RF-002 · BR-001 · BR-002 · BR-011 · STACK (auth)
**Criado em:** 2026-08-14

---

## Contexto do projeto (fix)

- **Produto:** Controle de Despesas — registro e resumo de despesas pessoais autenticadas
- **Stack:** Next.js (App Router) + React + TypeScript + Tailwind/shadcn · SQLite · Playwright
- **Código:** `apps/web` (layout B — pasta agrupadora `apps/`)
- **Glossário canônico:** Usuário, Despesa, Categoria, Status (Ativa/Arquivada), Resumo de despesas, Período, Arquivar, Auditoria — evitar Gasto/Lançamento/Transação como sinônimo de registro
- **Princípios:** isolamento por proprietário; auth obrigatória; arquivamento sem exclusão física; catálogo fixo; validação no servidor; auditoria; sem decisões financeiras além do cálculo

---

## Cenários de usuário

### US-01 — Criar conta (P1)

Como pessoa física, quero criar conta com nome, e-mail e senha, para acessar o Controle de Despesas com identidade própria.

**Story points:** 5

**Cenários de aceitação:**

1. **Dado** e-mail ainda não cadastrado e dados válidos (nome, e-mail, senha), **Quando** submeto o cadastro, **Então** a conta é criada, a senha é armazenada apenas como hash e sou autenticado (ou direcionado ao login conforme premissa)
2. **Dado** e-mail já existente, **Quando** tento cadastrar, **Então** o sistema rejeita com erro claro e não cria segunda conta
3. **Dado** campos obrigatórios ausentes ou inválidos, **Quando** submeto, **Então** a validação no servidor impede persistência
4. **Dado** cadastro bem-sucedido, **Quando** a auditoria é consultada, **Então** existe registro de criação de conta (BR-011)

---

### US-02 — Login e logout (P1)

Como Usuário, quero autenticar com e-mail/senha e encerrar a sessão, para acessar dados pessoais com segurança e sair quando desejar.

**Story points:** 5

**Cenários de aceitação:**

1. **Dado** conta existente e credenciais corretas, **Quando** faço login, **Então** obtenho sessão autenticada e acesso às áreas protegidas
2. **Dado** credenciais incorretas, **Quando** tento login, **Então** o acesso é negado e falha relevante é auditável/logável (BR-011)
3. **Dado** sessão ativa, **Quando** faço logout, **Então** a sessão encerra e dados pessoais deixam de ser acessíveis sem novo login
4. **Dado** visitante não autenticado, **Quando** acesso rota de dados pessoais, **Então** sou bloqueado/redirecionado (BR-001) — gate mínimo nesta feature; reforço em Isolamento

---

## Requisitos funcionais

| ID | Requisito | Ref foundation | Prioridade |
|----|-----------|----------------|------------|
| FR-001 | O sistema DEVE permitir criar conta com nome, e-mail e senha | RF-001 | P1 |
| FR-002 | O sistema DEVE rejeitar e-mail já cadastrado | RF-001 · BR-002 | P1 |
| FR-003 | O sistema DEVE armazenar senha apenas como hash | RNF Segurança · Constituição | P1 |
| FR-004 | O sistema DEVE autenticar com e-mail e senha e estabelecer sessão | RF-002 | P1 |
| FR-005 | O sistema DEVE permitir logout e invalidar a sessão corrente | RF-002 | P1 |
| FR-006 | O sistema DEVE exigir autenticação para acessar dados pessoais | BR-001 | P1 |
| FR-007 | O sistema DEVE auditar criação de conta e falhas relevantes de login | BR-011 | P1 |
| FR-008 | O sistema DEVE validar inputs de cadastro/login no servidor | Constituição · STACK | P1 |

## Casos de borda

- E-mail com casing diferente (ex.: `A@b.com` vs `a@b.com`) — normalizar para unicidade?
- Senha abaixo do comprimento mínimo — rejeitar
- Login com conta inexistente vs senha errada — mensagem genérica (não enumerar usuários)
- Sessão expirada ao acessar área protegida — redirecionar ao login
- Tentativa de cadastro com payload manipulado no client — servidor rejeita

## Fora de escopo

- OAuth / magic link / 2FA
- Alteração de senha in-app, reset por e-mail, verificação de e-mail
- Isolamento completo de consultas de Despesa (feature **Isolamento por usuário**)
- Multi-papel, admin, compartilhamento de conta
- Despesas e resumo

## Esclarecimentos

## Premissas

- Após cadastro bem-sucedido: **iniciar sessão automaticamente** (melhor UX MVP)
- E-mail armazenado e comparado em **forma normalizada** (trim + lowercase)
- Comprimento mínimo de senha: **8 caracteres** (sem complexidade extra obrigatória no MVP)
- Mensagens de erro de login: **genéricas** (“Credenciais inválidas”)
- TTL de sessão: **padrão Auth.js / 30 dias** renovável por uso (ajustável via env)
- Auditoria de login: registrar **falhas** (e opcionalmente sucessos em log estruturado; BR-011 exige falha relevante)
- UI em pt-BR; rotas `/cadastro` e `/login`

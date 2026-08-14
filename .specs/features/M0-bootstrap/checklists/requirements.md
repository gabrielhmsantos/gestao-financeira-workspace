# Checklist de requisitos: Bootstrap

**Marco:** M0 | **Criado em:** 2026-08-14
**Spec:** `.specs/features/M0-bootstrap/spec.md`

---

## Qualidade do conteúdo

- [x] CHK001 Todas as user stories têm cenários de aceitação Dado/Quando/Então
- [x] CHK002 Prioridades P1/P2 atribuídas a todas as user stories
- [x] CHK003 Cada user story é independentemente testável e entregável
- [x] CHK004 Casos de borda documentados (contornos, cenários de erro)
- [x] CHK005 Fora de escopo listado explicitamente

## Completude dos requisitos

- [x] CHK006 Todos os FR-* rastreáveis a RF-* ou BR-* da foundation (STACK/Constituição)
- [x] CHK007 Nenhum marcador `[NEEDS CLARIFICATION]` restante (ou premissa documentada)
- [x] CHK008 Entidades-chave definidas se a feature envolve mudanças de dados (schema base sem domínio — explícito)
- [x] CHK009 Requisitos não funcionais especificados (toolchain, health, env)

## Alinhamento à constituição

- [x] CHK010 Conformidade com os Princípios Centrais verificada (sem violações silenciosas)
- [x] CHK011 Ownership / isolamento tratados para todas as novas operações de dados (N/A — sem dados de usuário)
- [x] CHK012 Requisitos de auditoria tratados para operações que alteram estado (N/A no M0; adiado M1+)
- [x] CHK013 Terminologia canônica usada (Despesa, Categoria, Arquivar — sem sinônimos proibidos do glossário)

## Prontidão da feature

- [x] CHK014 Ambiguidades resolvidas via clarify ou documentadas como premissas
- [x] CHK015 Dependências de outros marcos ou serviços externos identificadas (nenhuma)
- [x] CHK016 Escopo MVP definido explicitamente (P1 = obrigatório no marco, P2 = próxima iteração)
- [x] CHK017 Critérios de sucesso mensuráveis e agnósticos de tecnologia
- [x] CHK018 Toda user story de produto tem story point Fibonacci (1|2|3|5|8|13|21)
- [x] CHK019 Nenhuma user story com SP ≥13 permanece sem divisão sem justificativa documentada

## Notas

- US-01 SP 8 com rationale documentada (greenfield)
- Código-alvo: `apps/web`

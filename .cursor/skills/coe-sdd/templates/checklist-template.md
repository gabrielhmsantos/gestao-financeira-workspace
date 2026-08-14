# Checklist de requisitos: [FEATURE_NAME]

**Marco:** [MILESTONE] | **Criado em:** [DATE]
**Spec:** `.specs/features/[FEATURE_SLUG]/spec.md`
<!-- FEATURE_SLUG = {MN}-{kebab-case} ex.: M1-authentication-session -->

---

## Qualidade do conteúdo

- [ ] CHK001 Todas as user stories têm cenários de aceitação Dado/Quando/Então
- [ ] CHK002 Prioridades P1/P2 atribuídas a todas as user stories
- [ ] CHK003 Cada user story é independentemente testável e entregável
- [ ] CHK004 Casos de borda documentados (contornos, cenários de erro)
- [ ] CHK005 Fora de escopo listado explicitamente

## Completude dos requisitos

- [ ] CHK006 Todos os FR-* rastreáveis a RF-* ou BR-* da foundation
- [ ] CHK007 Nenhum marcador `[NEEDS CLARIFICATION]` restante (ou premissa documentada)
- [ ] CHK008 Entidades-chave definidas se a feature envolve mudanças de dados
- [ ] CHK009 Requisitos não funcionais especificados (performance, segurança, escala)

## Alinhamento à constituição

- [ ] CHK010 Conformidade com os Princípios Centrais verificada (sem violações silenciosas)
- [ ] CHK011 RBAC / controle de acesso tratado para todas as novas operações
- [ ] CHK012 Requisitos de audit log tratados para operações que alteram estado
- [ ] CHK013 Terminologia canônica usada (sem sinônimos para termos do glossário)

## Prontidão da feature

- [ ] CHK014 Ambiguidades resolvidas via clarify ou documentadas como premissas
- [ ] CHK015 Dependências de outros marcos ou serviços externos identificadas
- [ ] CHK016 Escopo MVP definido explicitamente (P1 = obrigatório no marco, P2 = próxima iteração)
- [ ] CHK017 Critérios de sucesso mensuráveis e agnósticos de tecnologia
- [ ] CHK018 Toda user story de produto tem story point Fibonacci (1|2|3|5|8|13|21)
- [ ] CHK019 Nenhuma user story com SP ≥13 permanece sem divisão sem justificativa documentada

## Notas

- Marque itens `[x]` quando concluídos
- Adicione comentários inline para achados
- Itens falhando: uma iteração de correção em spec.md, depois reexecute o checklist

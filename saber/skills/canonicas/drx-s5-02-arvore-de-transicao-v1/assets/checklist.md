# Checklist: Árvore de Transição

**Objetivo:** Padronizar a construção da Árvore de Transição para transformar a injeção em ações práticas, garantir que a mudança ocorra de forma lógica e ordenada, evitar implementação caótica e conectar ação a efeito intermediário a resultado sistêmico
**Responsável:** Consultor, Cliente
**Frequência:** por evento

---

## Antes de Começar
- [ ] Injeção validada na FRT
- [ ] Obstáculos tratados na PRT (se necessário)

---

## Execução
- [ ] Posicionar a injeção - começar pela condição validada- [ ] Identificar primeira ação necessária perguntando qual é o primeiro movimento que precisa acontecer para isso se tornar possível- [ ] Definir efeito intermediário perguntando se essa ação acontecer, o que passa a ser possível que antes não era- [ ] Continuar a cadeia repetindo o ciclo: Ação > Efeito > Nova condição > Próxima ação- [ ] Testar a lógica perguntando para cada passo se isso não acontecer o próximo passo ainda é possível- [ ] Validar completude perguntando se essa sequência garante que a injeção se torne realidade
---

## Verificação Final
- [ ] Sequência lógica de ações
- [ ] Relação clara entre ações e efeitos
- [ ] Plano estruturado por impacto
- [ ] Base para cronograma e priorização
- [ ] Diagrama ou tabela com Ação, Efeito intermediário e Nova condição
- [ ] ⚠️ Verificar: Ausência de ferramentas definidas em todos os passos reduz rastreabilidade e padronização da execução
- [ ] ⚠️ Verificar: Processo altamente dependente de julgamento consultivo qualificado — risco de variação de qualidade entre consultores
- [ ] ⚠️ Verificar: Nenhum condicional explícito mapeado, o que pode gerar ambiguidade em situações de bloqueio ou revisão da injeção
- [ ] ⚠️ Verificar: A validação de completude (passo 6) é subjetiva e sem critério mensurável definido
- [ ] ⚠️ Verificar: Dependência de artefatos externos (FRT e PRT) sem protocolo de handoff formalizado

---
slug: drx-s6-02-board-final-apresentacao-nbo-v1
description: "name: Board Final — Apresentação e NBO"
name: Board Final — Apresentação e NBO
status: draft-v1

---

# Board Final — Apresentação da Entrega Final & NBO

## Descrição
Conduz a apresentação final do DR-X ao cliente, entregando formalmente o documento completo, validando o plano de ação e apresentando a **NBO (Next Best Offer)** para manter o relacionamento e a execução pós-diagnóstico. É a última etapa do ciclo DR-X.

Ativar quando o Documento de Entrega Final estiver pronto e a reunião de encerramento estiver agendada.

## Quando Usar
- Triggers: "board final", "apresentação final", "NBO", "próximos passos comerciais", "encerrar DR-X"
- **NÃO usar quando:**
  1. O Documento de Entrega Final ainda não foi compilado/revisado
  2. O decisor do cliente não estará presente — sem ele, NBO não fecha
  3. Quick Wins do Board 1 ainda não têm status registrado

## Inputs Necessários
1. **Documento de Entrega Final** completo e revisado (output de `drx-s6-01-elaboracao-entrega-final-v1`)
2. **Master Contexto** atualizado com decisões do Board 1
3. **Registro formal do Board 1** (Quick Wins aprovados, validações, ajustes)
4. **Forecast** (`drx-s5-04-forecast-financeiro-v1`)
5. **Matriz de Expansão** (`drx-s5-05-matriz-de-expansao-v1`)
6. **Cronograma de Implementação** (`drx-s5-03-cronograma-90-dias-v1`)

## Processo de Execução

### 1. Preparar a pauta (1h30 a 2h)

| Bloco | Duração | Objetivo |
|---|---|---|
| Abertura | 5 min | Reestabelecer contexto, alinhar expectativas da reunião |
| Diagnóstico | 15-20 min | Apresentar sistema atual + trava dominante |
| Estratégia | 15-20 min | ICP, PUV, CVBA, Fluxo de Estratégia |
| Plano de Ação | 15-20 min | Injeção, PRT, Árvore de Transição, Cronograma |
| Projeções | 10 min | Forecast + Matriz de Expansão |
| Quick Wins | 5-10 min | Status dos Quick Wins do Board 1 |
| NBO | 10-15 min | Apresentação da próxima oferta |
| Fechamento | 5 min | Próximos passos, decisão do cliente |

### 2. Preparar a NBO (Next Best Offer)
Estruturar a oferta de continuidade com base em Cronograma, Forecast, Matriz de Expansão e travas diagnosticadas:

- **Problema endereçado** — qual dor ou oportunidade a NBO resolve
- **Escopo proposto** — o que está incluído
- **Formato** — consultoria contínua, implementação, sprint, etc.
- **Duração sugerida** — tempo estimado de execução
- **Resultado esperado** — conectado ao Forecast (retorno projetado)
- **Investimento** — valor proposto

**Regra:** NBO deve ser personalizada. **Nunca** apresentar catálogo genérico de serviços. Ela nasce dos dados do DR-X.

### 3. Conduzir o Board Final
Seguir a pauta do Bloco 1:
- Conectar cada seção com decisões validadas no Board 1
- Mostrar progressão lógica (diagnóstico → estratégia → plano → projeção)
- Destacar Quick Wins implementados com evidência
- Ser direto nas recomendações
- Na NBO: mostrar que ela nasce dos dados; conectar investimento ao retorno projetado; dar espaço para cliente perguntar

### 4. Registrar decisões imediatamente após a reunião
- **Entrega aceita:** Sim / Com ressalvas / Pendências
- **Plano de ação validado:** Sim / Não
- **NBO:** aceita / em consideração / recusada / contraproposta
- **Pendências** registradas
- **Feedback do cliente** capturado

### 5. Formalizar entrega e encerrar ciclo
- Enviar Documento de Entrega Final ao cliente formalmente
- Se NBO aceita: iniciar onboarding
- Se em consideração: definir prazo de follow-up (máximo 7 dias)
- Se recusada: registrar motivo e manter relacionamento
- Atualizar Master Contexto com status final de encerramento

## Outputs Esperados
- Board Final conduzido e documentado
- Documento de Entrega Final entregue formalmente
- NBO apresentada (com status registrado)
- Registro de decisões do Board Final
- Master Contexto atualizado com status de encerramento
- Ciclo DR-X formalmente encerrado

## Exceções
- **Cliente cancela ou adia o Board Final:** reagendar em até 5 dias úteis. Se ultrapassar, enviar documento por escrito e agendar call reduzida para NBO
- **Cliente rejeita parte do diagnóstico no Board Final:** registrar pontos contestados. Se forem fundamentais (ex.: injeção), ajustar plano — não forçar validação
- **Cliente aceita entrega mas recusa NBO:** encerrar com profissionalismo. Manter relacionamento para retorno futuro
- **Decisor ausente:** apresentar para os presentes, mas não fechar NBO sem decisor. Agendar follow-up em até 3 dias úteis

## Riscos
- ⚠️ Ausência do decisor compromete fechamento da NBO — risco de ciclo não encerrado formalmente
- ⚠️ NBO genérica ou mal conectada aos dados reduz drasticamente taxa de conversão
- ⚠️ Rejeição parcial do diagnóstico sem protocolo claro gera conflito relacional
- ⚠️ Follow-up não executado em 7 dias em NBO "em consideração" → perda da oportunidade
- ⚠️ Sem ferramenta definida para registro pós-reunião → perda de informações críticas

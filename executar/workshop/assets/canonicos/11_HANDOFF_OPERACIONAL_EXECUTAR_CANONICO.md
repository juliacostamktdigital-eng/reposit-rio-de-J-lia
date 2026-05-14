# Handoff Operacional Executar Canônico
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + canônico original sem skill merge dedicada.  
**Decisão de merge:** sem skill dedicada; mantido como entrada EXECUTAR e pré-requisito dos playbooks estratégicos.


Status: v1 alinhado ao processo SABER TO BE  
Escopo: entrada operacional do cliente no processo EXECUTAR  
Objetivo: transformar os insumos vindos de vendas e Growth Class em um pacote de handoff validado, suficiente para o time EXECUTAR iniciar planning sem pedir o mesmo contexto de novo.

## 1. Princípio

O handoff operacional não é uma reunião de apresentação. Ele é a transferência auditável de contexto entre venda, boas-vindas e operação.

No começo do EXECUTAR, os assets recebidos são:

- plano de ROI;
- transcrição da call de vendas;
- transcrição da Growth Class / call de boas-vindas.

Esses três insumos precisam virar um pacote operacional validado. O time não deve depender de memória do closer, print solto no WhatsApp ou repetição do cliente no kickoff.

## 2. Entradas obrigatórias

### 2.1 Plano de ROI

Deve conter ou permitir extrair:

- produto contratado;
- escopo vendido;
- investimento;
- expectativa de retorno;
- metas prometidas ou simuladas;
- premissas usadas no cálculo;
- horizonte de tempo;
- canais/produtos considerados;
- restrições e observações do closer;
- divergências entre cenário provável, otimista e conservador.

Critério:

```text
O plano de ROI precisa deixar claro o que foi prometido, em quais premissas essa promessa depende e quais riscos podem quebrar a expectativa.
```

### 2.2 Transcrição da call de vendas

Deve ser usada para extrair:

- dores declaradas pelo cliente;
- objetivo que motivou a compra;
- objeções levantadas;
- promessas feitas em call;
- restrições de escopo;
- urgências e prazos mencionados;
- stakeholders e decisores;
- critérios de sucesso percebidos pelo cliente;
- riscos de desalinhamento;
- dúvidas que ficaram em aberto.

### 2.3 Transcrição da Growth Class / boas-vindas

Deve ser usada para extrair:

- entendimento do cliente sobre o que comprou;
- expectativas pós-venda;
- dúvidas sobre escopo e próximos passos;
- desvios entre o que foi vendido e o que foi entendido;
- maturidade percebida do cliente;
- tom da relação;
- riscos de churn M0;
- pendências de informação;
- próximos passos acordados.

## 3. Saída canônica

O pacote de handoff operacional deve gerar um documento único com:

- resumo executivo da conta;
- produto/escopo contratado;
- links para plano de ROI e transcrições;
- síntese da call de vendas;
- síntese da Growth Class;
- promessas e expectativas;
- premissas críticas;
- riscos e red flags;
- divergências venda vs. entendimento do cliente;
- perguntas abertas;
- stakeholders;
- próximos passos;
- dono interno;
- status de completude.

## 4. Análise de desvio

Comparar explicitamente:

| Eixo | Call de vendas | Growth Class | Risco |
| --- | --- | --- | --- |
| Escopo | O que foi vendido | O que o cliente entendeu | Baixo/Médio/Alto |
| Resultado esperado | Promessa/premissa | Expectativa verbalizada | Baixo/Médio/Alto |
| Prazo | O que foi sinalizado | O que o cliente espera | Baixo/Médio/Alto |
| Responsabilidades | O que depende da V4 | O que depende do cliente | Baixo/Médio/Alto |
| Próximo passo | O que vendas indicou | O que boas-vindas confirmou | Baixo/Médio/Alto |

Se houver desvio médio ou alto, o handoff não está completo até que o coordenador/account registre ação corretiva.

## 5. Fluxo operacional recomendado

```text
Contrato/fechamento -> Plano de ROI + transcrição da venda
Growth Class -> transcrição + análise de desvios
IA compila pacote de handoff
Coordenador/Gerente revisa de forma supervisionada
Squad/Account recebe pacote validado
Planning inicia com escopo, risco e próximos passos claros
```

## 6. Campos do documento de handoff

```text
# Handoff Operacional EXECUTAR

Cliente:
Produto contratado:
Data do fechamento:
Data da Growth Class:
Squad/Responsável:

## Links dos insumos
Plano de ROI:
Transcrição da call de vendas:
Transcrição da Growth Class:

## Resumo executivo

## Escopo contratado

## Premissas do Plano de ROI

## Promessas e expectativas

## Dores e objetivos declarados

## Stakeholders

## Riscos e red flags

## Divergências venda vs. boas-vindas

## Pendências

## Próximos passos

## Decisão do responsável
```

## 7. Automação AI-native

O processo ideal é:

- IA recebe plano de ROI e transcrições;
- IA extrai entidades, promessas, riscos e dúvidas;
- IA compara call de vendas vs. Growth Class;
- IA gera pacote de handoff;
- coordenador/gerente valida, corrige e aprova;
- sistema registra completude e notifica o squad;
- planning usa o pacote como fonte de verdade inicial.

O humano não deve compilar do zero. O humano deve validar, corrigir e decidir.

## 8. Critério N2

Handoff operacional está N2 quando:

- plano de ROI está anexado;
- transcrição da call de vendas está anexada;
- transcrição da Growth Class está anexada;
- síntese operacional foi gerada;
- análise de desvio foi feita;
- riscos e pendências estão registrados;
- responsável interno revisou;
- próximo passo está claro para o time EXECUTAR.

## 9. Critério N3

Handoff operacional está N3 quando:

- desvios recorrentes viram feedback para vendas;
- promessas problemáticas são classificadas por tipo;
- risco de churn M0 é monitorado;
- tempo de handoff é medido;
- completude do pacote é medida;
- aprendizados melhoram o roteiro de vendas e Growth Class;
- o planejamento EXECUTAR usa o handoff sem precisar recoletar contexto.

## 10. Métricas

- tempo contrato/fechamento -> pacote de handoff completo;
- completude do pacote;
- número de pendências por handoff;
- número de desvios venda vs. Growth Class;
- severidade média dos desvios;
- retrabalho no planning por falta de contexto;
- churn ou risco M0 associado a desalinhamento inicial.

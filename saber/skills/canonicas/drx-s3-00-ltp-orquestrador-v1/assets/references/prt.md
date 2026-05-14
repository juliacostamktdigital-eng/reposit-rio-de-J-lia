# Prerequisite Tree (PrT) — Referência de Construção

## O que é

O Prerequisite Tree é uma ferramenta de **lógica de necessidade** que transforma as injections validadas na FRT em um plano de implementação sequenciado. Responde "Como causar a mudança?" identificando obstáculos e criando Intermediate Objectives (IOs) para superá-los.

Dettmer consolida o Prerequisite Tree original de Goldratt com o Transition Tree, criando uma ferramenta única mais prática.

## Estrutura

```
                [OBJETIVO FINAL]
                      ↑
             [IO: Condição/Ação N]
              (Supera Obstáculo N)
                      ↑
             [IO: Condição/Ação 3]
              (Supera Obstáculo 3)
                      ↑
        ┌─────────────┴──────────────┐
  [IO: Cond./Ação 1]          [IO: Cond./Ação 2]
   (Supera Obst. 1)           (Supera Obst. 2)
```

Leitura: "Para alcançar [Objetivo], precisamos de [IO N], porque [Obstáculo N] nos impede."

## Conceitos Fundamentais

### Objetivo
- Vem da FRT: é uma injection ou conjunto de injections a implementar
- Deve ser uma condição específica e verificável
- Pode haver múltiplos PrTs para diferentes injections

### Obstáculos
- Condições que impedem a realização de cada IO ou do Objetivo
- Sempre formulados como **condições** (estados), não como ações
- "A equipe não tem competência em X" (condição) — não "Treinar a equipe" (ação)
- Obstáculos são superados, não obliterados — a abordagem é pragmática

### Intermediate Objectives (IOs)
- Condições ou ações que, ao serem realizadas, superam os obstáculos
- Cada IO é pareado com um obstáculo: "Para [IO], precisamos superar [Obstáculo]"
- IOs podem ser condições ("A equipe está treinada") ou ações ("Realizar workshop de capacitação")
- Dettmer prefere condições porque são mais verificáveis

### Sequence Dependency
- Alguns IOs dependem de outros (IO 3 só pode ser feito depois de IO 1 e IO 2)
- Outros são paralelos (IO 1 e IO 2 podem ser feitos simultaneamente)
- O PrT captura ambas as relações

## Procedimento de Construção (10 passos)

### Passo 1: Determinar o Objetivo
- Selecione a injection (ou grupo de injections) da FRT
- Formule como condição verificável no futuro
- "O novo processo de qualificação de leads está implementado e operacional"

### Passo 2: Identificar Todos os Intermediate Objectives
- Antes de pensar em obstáculos, liste TUDO que precisa estar em vigor para o Objetivo ser alcançado
- Pense em: recursos, competências, aprovações, infraestrutura, alinhamento, comunicação
- Seja exaustivo — é mais fácil remover IOs desnecessários do que descobrir que faltou um

### Passo 3: Surfacear Todos os Obstáculos Possíveis
Para cada IO, pergunte: "O que impede isso de existir/acontecer HOJE?"
- Obstáculos podem ser:
  - **Físicos:** falta de recurso, ferramenta, infraestrutura
  - **Políticos:** falta de aprovação, regulação, compliance
  - **De conhecimento:** falta de competência, informação, dados
  - **Comportamentais:** resistência, hábitos, cultura
  - **De tempo:** dependência de eventos, prazos, janelas
- Envolver outras pessoas na identificação de obstáculos melhora a qualidade e gera buy-in

### Passo 4: Organizar IOs e Obstáculos
- Pareie cada IO com seu(s) obstáculo(s)
- Um IO pode superar múltiplos obstáculos
- Um obstáculo pode requerer múltiplos IOs para ser superado

### Passo 5: Sequenciar os IOs Dentro de Cada Branch
- Identifique dependências: "IO 3 só pode ser feito depois de IO 1"
- Identifique paralelismos: "IO 1 e IO 2 podem ser feitos simultaneamente"
- Teste: "Posso fazer IO 3 sem ter completado IO 1?" Se não → dependência

### Passo 6: Conectar os IOs
- Construa a árvore de baixo para cima
- IOs independentes ficam na base (podem ser feitos primeiro)
- IOs dependentes ficam acima de seus pré-requisitos
- O Objetivo fica no topo

### Passo 7: Superar os Obstáculos
Para cada obstáculo, formule a estratégia de superação:
- Pode ser uma ação direta
- Pode ser uma condição a ser criada
- Pode ser uma negociação ou alinhamento
- O objetivo é SUPERAR, não ELIMINAR — ser pragmático

### Passo 8: Integrar as Branches
- Se há múltiplas branches paralelas, identifique pontos de convergência
- Branches podem se unir quando IOs de diferentes caminhos são necessários juntos

### Passo 9: Conectar o Corpo da Árvore ao Objetivo
- Verifique se o topo da árvore (últimos IOs) realmente leva ao Objetivo
- Pergunte: "Se todos estes IOs estão satisfeitos, o Objetivo é alcançado?"

### Passo 10: Escrutinar a Árvore Inteira
Aplique as CLR relevantes:
- **Entity Existence:** cada IO e obstáculo é real?
- **Cause Sufficiency:** os IOs são suficientes para superar cada obstáculo?
- **Additional Cause:** faltam IOs para algum obstáculo?
- **IO-Obstacle Validity Test:** "Em que medida [Obstáculo] impede [IO]?" — se não impede, remova

## IO-Obstacle Validity Test

Para cada par IO-Obstáculo:
1. "[Obstáculo] realmente impede a realização de [IO]?"
2. "[IO] realmente supera [Obstáculo]?"
3. Se a resposta para qualquer um é "não", o par é inválido

## Integração com Critical Chain Project Management

Dettmer sugere que, uma vez construído o PrT, a implementação pode ser gerida como um projeto usando CCPM (Critical Chain Project Management):
- IOs se tornam tarefas do projeto
- Dependências do PrT definem a sequência
- Paralelismos do PrT definem o que pode ser feito simultaneamente
- O caminho mais longo define a Critical Chain
- Buffers protegem contra variação

## Framework de 3 Fases para Gestão da Mudança

1. **Fase de Preparação:** comunicar a visão, alinhar liderança, definir comportamentos desejados
2. **Fase de Implementação:** executar os IOs do PrT, monitorar progress, ajustar conforme necessário
3. **Fase de Sustentação:** reforçar novos comportamentos, medir resultados, celebrar conquistas

## Armadilhas Comuns

1. **Obstáculos genéricos:** "Falta de budget" é genérico demais — especifique: "Não há aprovação para investimento de R$X em Y"
2. **IOs que são ações, não condições:** Prefira "A equipe domina o processo X" ao invés de "Treinar a equipe em X"
3. **Ignorar obstáculos comportamentais:** Resistência humana é frequentemente o maior obstáculo e o mais ignorado
4. **Sequência sem justificativa:** Se não há dependência real, permita paralelismo — reduz o tempo total
5. **PrT sem dono:** Cada IO deve ter um responsável e um prazo estimado

## Transição para a Fase Seguinte (Gestão da Mudança)

O PrT fornece o "o quê" e "em que ordem". A Fase 6 (Gestão da Mudança) endereça:
- **Quem** vai resistir e por quê
- **Como** criar commitment (não apenas compliance)
- **Como** sustentar a mudança após implementação
- Abordagem comportamental: definir comportamentos, reforçar, medir

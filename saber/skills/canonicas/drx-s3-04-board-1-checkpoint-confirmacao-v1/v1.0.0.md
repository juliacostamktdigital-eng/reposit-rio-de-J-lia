---
slug: drx-s3-04-board-1-checkpoint-confirmacao-v1
name: drx-s3-04-board-1-checkpoint-confirmacao-v1
description: "Apresentar ao cliente os resultados do diagnóstico e da análise lógica (LTP), validar a direção estratégica antes de avançar para o Posicionamento Estratégico, e identificar Quick Wins que podem ser implementados imediatamente enquanto o..."
---

# Checkpoint de Confirmação (Board 1)

## Descrição
Apresentar ao cliente os resultados do diagnóstico e da análise lógica (LTP), validar a direção estratégica antes de avançar para o Posicionamento Estratégico, e identificar Quick Wins que podem ser implementados imediatamente enquanto o planejamento estratégico avança.
Ativar quando dr-x, board de decisão, diagnóstico, validação com cliente, quick wins, ltp, semana 3 for necessário.

## Quando Usar
- Trigger: "DR-X", "Board de decisão", "Diagnóstico", "Validação com cliente", "Quick Wins", "LTP", "Semana 3"
- NÃO usar quando: Passo 4 (condução do Board 1) exige presença humana e leitura de dinâmica interpessoal — não automatizável; Validação ou rejeição do diagnóstico pelo cliente gera bifurcação que impacta toda a continuidade do projeto; Quick Wins identificados pela IA podem não refletir restrições operacionais reais do cliente; Atualização do arquivos de context/ com informações coletadas verbalmente no comitê depende de registro humano fiel
## Inputs Necessários
Solicitar antes de iniciar. Se faltar algum, perguntar antes de prosseguir:

1. **context/business.md** — modelo de negócio, revenue streams, capacidade
   **context/gtm.md** — canais, funil, ICP, ciclo de vendas, mercado
   **context/constraints.md** — restrições, UDEs, diagnóstico de trava
   **DECISIONS.md** — decisões estratégicas e questões abertas
2. **Árvore de Objetivos (IO Map) (context-arvore-de-objetivos + checklist)**
3. **Sizing de Mercado (TAM/SAM/SOM)**
4. **Estudo de Concorrentes (output da skill de Estudo de Concorrentes)**
5. **Análise de Tendências (context-analise-de-tendencias)**
6. **Mapeamento do Fluxo de Receita (context-fluxo-receita)**
7. **Diagnóstico das 7 Travas (contexts e checklists das travas 1-7)**
8. **Definição de Maturidade Digital (context-definicao-de-maturidade-digital)**
9. **CRT — Árvore da Realidade Atual (output da skill-ltp-crt)**
10. **Nuvem do Conflito (output da skill-ltp-nuvem, se aplicável)**
11. **FRT — Árvore de Realidade Futura (context-arvore-de-realidade-futura-frt)**
12. **Injeção definida (resultado da FRT)**

## Processo de Execução

### 1. Compilar diagnóstico reunindo os outputs das Semanas 2 e 3 em uma narrativa coerente, organizado em 3 blocos: Bloco 1 (Onde estamos) - visão geral do negócio, maturidade digital atual, fluxo de receita, sizing de mercado; Bloco 2 (O que encontramos) - diagnóstico das 7 travas, landscape competitivo, tendências relevantes; Bloco 3 (Lógica do sistema) - CRT, Nuvem, Injeção, FRT
- Ferramenta: *arquivos de context/, outputs das skills de diagnóstico*
### 2. Identificar Quick Wins a partir do diagnóstico, selecionando ações de implementação rápida (1-2 semanas) que não dependem do planejamento estratégico completo, geram resultado visível, reforçam credibilidade e endereçam travas de baixa complexidade. Aplicar critérios: esforço baixo, impacto perceptível, independência. Listar entre 2 e 5 Quick Wins com ação, resultado esperado e prazo.
- Ferramenta: *Diagnóstico compilado*
### 3. Montar apresentação do Board 1 estruturada com: 1) Contexto (resumo do negócio e objetivos do DR-X); 2) Diagnóstico (principais achados); 3) Lógica (CRT → Injeção → FRT, versão simplificada); 4) Quick Wins (ações imediatas propostas); 5) Próximos passos (fase de Posicionamento Estratégico)
- Ferramenta: *Compilação de diagnóstico, Quick Wins identificados*
### 4. Conduzir o Board 1 apresentando ao cliente e registrando: validações do cliente, divergências ou objeções levantadas, Quick Wins aprovados para execução imediata, aprovação para seguir para Posicionamento Estratégico
- Ferramenta: *Apresentação do Board 1*
### 5. Registrar decisões do Board 1 documentando: se diagnóstico foi validado (Sim/Não/Com ressalvas), quais Quick Wins foram aprovados com responsável e prazo, ajustes necessários antes de avançar, atualizar arquivos de context/ com informações novas coletadas no comitê
- Ferramenta: *arquivos de context/*
## Formato de Saída
- Apresentação do Board 1 (documento/slides)
- Lista de Quick Wins aprovados com prazos
- Registro de validação do diagnóstico pelo cliente
- arquivos de context/ atualizado
- Aprovação para avançar à fase de Posicionamento Estratégico

## Exceções e Fallbacks
- Cliente não valida o diagnóstico: registrar as objeções específicas, revisar os pontos contestados com dados antes de avançar, não prosseguir para Semana 4 sem validação mínima da CRT e injeção
- Nenhum Quick Win identificado: registrar que o diagnóstico não revelou ações de baixo esforço, isso é válido — nem todo sistema tem ganhos rápidos acessíveis
- Cliente solicita mudança de escopo: documentar a solicitação e avaliar impacto no cronograma do DR-X antes de aceitar

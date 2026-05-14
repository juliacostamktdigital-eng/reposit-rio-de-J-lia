---
slug: drx-s2-04-analise-de-tendencias-v1
name: drx-s2-04-analise-de-tendencias-v1
description: "Conduz a análise de tendências do segmento e mapeamento de oportunidades de mercado em modo Copilot: a IA lidera a estruturação das dimensões de análise, processa os sinais fornecidos pelo consultor, propõe a classificação de impacto por..."
---

# Skill: Análise de Tendências do Segmento e Oportunidades de Mercado (DR-X)

## Descrição
Conduz a análise de tendências do segmento e mapeamento de oportunidades de mercado em modo Copilot: a IA lidera a estruturação das dimensões de análise, processa os sinais fornecidos pelo consultor, propõe a classificação de impacto por tendência com justificativa e redige as oportunidades e alavancas de crescimento priorizadas. O consultor fornece os sinais de mercado observados, os insumos do estudo de concorrentes e valida os outputs em cada etapa.

## Quando Usar
- Triggers: "Análise de tendências", "Tendências do segmento", "Oportunidades de mercado", "Mapear tendências para [cliente]", "Alavancas de crescimento"
- **Pré-requisitos:**
  - Arquivos `context/` do cliente com status `[VALIDADO]` devem estar disponíveis
  - Sizing de mercado (SAM/SOM) realizado — oportunidades precisam ser conectadas ao mercado dimensionado
  - Estudo de concorrentes disponível como insumo
- **NÃO usar** se os arquivos `context/` não existirem — executar `skill-pipeline-extracao` primeiro
- **NÃO usar** se o ICP não estiver definido — tendências sem ICP claro geram análise genérica sem valor estratégico
- **Posição no DR-X:** executar após Sizing de Mercado e Estudo de Concorrentes, antes da Árvore de Objetivos e do diagnóstico de Travas

---

## Inputs de Partida

Antes de perguntar qualquer coisa ao consultor, **ler os arquivos `context/`** do cliente e extrair:
- Segmento e ICP prioritário definidos (`context/gtm.md`)
- SAM/SOM calculados — referência para conectar oportunidades ao mercado real (`context/gtm.md`)
- Resultados do estudo de concorrentes (sinais competitivos já identificados)
- UDEs relacionadas a demanda, posicionamento ou mercado
- Restrições do sistema mencionadas — capacidade operacional, modelo de venda, recursos (`context/business.md`)

Registrar internamente o que já se sabe e **não coletar novamente o que já está nos arquivos `context/`**.

---

## Processo de Execução

### Step 0 — Leitura do Contexto

1. Ler os arquivos `context/business.md` e `context/gtm.md`
2. Mapear:
   - Segmento, ICP e mercado já dimensionado (`context/gtm.md`)
   - Concorrentes identificados e movimentos competitivos observados
   - UDEs relacionadas a demanda, geração de oportunidades ou posicionamento
   - Restrições operacionais e estratégicas do sistema (`context/business.md`)
3. Apresentar resumo ao consultor:

> *"Com base nos arquivos context/, já sei que: [resumo do segmento, ICP, SAM/SOM, concorrentes identificados e restrições relevantes]. Vou estruturar a análise de tendências em 5 dimensões. Seguindo para o Step 1."*

---

### Step 1 — Coleta de Sinais de Mercado (Batch)

Solicitar **em uma única mensagem batch** os sinais nas 5 dimensões de tendência. Adaptar ao que já está no Master Contexto — não coletar o que já foi informado.

**Perguntar de uma vez:**

> *Preciso das seguintes informações para mapear as tendências relevantes do segmento. Forneça o que tiver — dado parcial é melhor que nada:*
>
> **Dimensão 1 — Econômica:**
> *1. Como está o ciclo econômico do setor? O orçamento dos clientes está em expansão, contração ou estável?*
> *2. Existe pressão por eficiência ou redução de custos que esteja mudando como os clientes tomam decisões de compra?*
> *3. Há alguma mudança macroeconômica recente (juros, câmbio, crédito) que esteja impactando diretamente o ICP?*
>
> **Dimensão 2 — Tecnológica:**
> *4. Quais tecnologias estão sendo adotadas pelos clientes ou concorrentes do segmento (IA, automação, plataformas, ferramentas específicas)?*
> *5. Existe alguma tecnologia emergente que ainda não chegou ao segmento mas já está impactando mercados adjacentes?*
> *6. O cliente percebe alguma mudança tecnológica que sua operação ainda não acompanhou?*
>
> **Dimensão 3 — Comportamental:**
> *7. Como o comportamento de compra do ICP mudou nos últimos 1–2 anos? (canal, processo de decisão, tempo de ciclo)*
> *8. Existem novas expectativas dos clientes em relação ao produto/serviço ou à experiência de compra?*
> *9. Há sinais de mudança de hábito que ainda não se traduziram em demanda explícita?*
>
> **Dimensão 4 — Regulatória:**
> *10. Existem normas, certificações ou mudanças regulatórias recentes (ou anunciadas) que afetam o segmento?*
> *11. Alguma barreira regulatória está criando oportunidade para quem se adaptar antes dos concorrentes?*
>
> **Dimensão 5 — Competitiva:**
> *12. Existem novos entrantes no segmento com proposta de valor diferente? Quem?*
> *13. Algum player estabelecido está se reposicionando, saindo do mercado ou sendo adquirido?*
> *14. Onde os concorrentes estão falhando em responder às tendências acima?*

**Após receber os dados:** avançar para o Step 2 sem pedir mais informações nesta etapa.

---

### Step 2 — Mapa de Tendências com Classificação de Impacto

Com base nos sinais coletados, estruturar o mapa de tendências e propor a classificação de impacto. **A IA propõe — o consultor valida.** Nunca pedir ao consultor que classifique o impacto.

**Critérios de classificação de impacto:**

| Nível | Critério |
|---|---|
| **Alto** | Altera o volume de demanda, muda o processo de decisão do ICP ou redefine a estrutura competitiva do segmento num horizonte de 12–24 meses |
| **Médio** | Impacta operações ou posicionamento mas não altera o modelo de negócio nem a dinâmica competitiva de forma estrutural |
| **Baixo** | Sinal real mas com impacto periférico ou horizonte muito longo — relevante monitorar, não agir agora |

Apresentar ao consultor:

```
| Tendência | Dimensão | Impacto Proposto | Justificativa | Base de Evidência |
|---|---|---|---|---|
| [tendência] | [dimensão] | Alto / Médio / Baixo | [por quê] | [sinal que sustenta] |
```

Perguntar: *"Essa leitura está coerente com o que você observou? Algum ajuste no impacto ou tendência faltando antes de avançar?"*

---

### Step 3 — Mapeamento de Oportunidades

Com base nas tendências de impacto Alto e Médio, identificar oportunidades derivadas. Para cada oportunidade, verificar se existe conexão com o SAM/SOM já definido.

**Categorias de oportunidade a verificar:**

| Categoria | Pergunta orientadora |
|---|---|
| Dores emergentes | Qual novo problema está surgindo no ICP que ainda não tem solução no mercado? |
| Mudança no comportamento de compra | Como o cliente quer comprar/consumir de forma diferente? O negócio consegue entregar assim? |
| Ineficiências criadas por novos contextos | O que está ficando mais difícil para o ICP por causa das tendências identificadas? |
| Lacunas competitivas | Onde os concorrentes estão lentos ou ausentes na resposta às tendências? |

**Regra:** oportunidades sem conexão com SAM/SOM são especulações estratégicas — registrar com nota de baixa confiança.

Apresentar oportunidades identificadas e perguntar: *"Alguma oportunidade óbvia que não apareceu aqui? Alguma que você vê como inviável dado o que sabe do cliente?"*

---

### Step 4 — Análise de Alavancas de Crescimento (Lente TOC)

Para cada oportunidade validada, avaliar viabilidade estratégica usando lente TOC:

| Critério | Pergunta | Pontuação |
|---|---|---|
| Potencial de throughput | Capturar essa oportunidade aumenta a taxa de geração de receita do sistema? | Alto / Médio / Baixo |
| Aderência às competências | O negócio tem (ou consegue desenvolver rapidamente) o que é necessário para capturar? | Alta / Média / Baixa |
| Complexidade de execução | Quantos recursos, mudanças ou etapas são necessários para capturar? | Baixa / Média / Alta |
| Dependência de recursos inexistentes | A captura exige capacidades que o sistema não possui e não consegue adquirir no horizonte relevante? | Sim / Não |

**Regra de descarte:** oportunidades com "Sim" em dependência de recursos inexistentes ou com potencial de throughput Baixo devem ser descartadas desta análise — registrar como oportunidades de longo prazo.

---

### Step 5 — Priorização Estratégica

Com base nos Steps 2, 3 e 4, propor a lista priorizada de oportunidades. **A IA propõe a ordem — o consultor confirma ou ajusta.**

**Critérios de priorização (em ordem de peso):**
1. Impacto no resultado (throughput potencial)
2. Velocidade de captura (complexidade de execução)
3. Risco estratégico (dependências e exposição competitiva)

Apresentar:

```
| Prioridade | Oportunidade | Tendência-Origem | Throughput | Velocidade | Risco | Próximo Passo Sugerido |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
```

Perguntar: *"Essa priorização reflete a realidade do cliente? Algum reordenamento necessário antes de finalizar?"*

---

## Regras Operacionais

- **Nunca perguntar um sinal de cada vez** — todas as perguntas de uma mesma dimensão vão em uma única mensagem batch
- **Nunca delegar a classificação de impacto ao consultor** — a IA propõe com justificativa, o consultor confirma ou ajusta
- **Nunca avançar de step sem apresentar resultado e receber confirmação** do consultor
- **Sempre ler os arquivos `context/` antes de perguntar qualquer coisa** — não coletar o que já está disponível
- **Conectar todas as oportunidades ao SAM/SOM definido** — oportunidades fora do mercado dimensionado são sinalizadas como especulativas
- **Usar lente TOC na análise de alavancas** — oportunidades que violam restrições críticas do sistema são descartadas, não priorizadas

---

## Fallbacks

| Situação | O que fazer |
|---|---|
| Estudo de concorrentes não disponível | Prosseguir sem dimensão competitiva. Registrar como lacuna no output final e recomendar execução do estudo antes de usar a análise para decisões estratégicas. |
| SAM/SOM não calculados | Bloquear o skill. Orientar a executar `skill-sizing-mercado` antes de prosseguir — sem mercado dimensionado, oportunidades não podem ser priorizadas com rigor. |
| Mercado em colapso ou crise aguda | Adaptar foco para tendências de sobrevivência e consolidação. Sinalizar que a análise de oportunidades tem horizonte mais curto e premissas mais conservadoras. |
| Ausência de dados setoriais | Registrar como limitação no output. Usar sinais observacionais do consultor com nota explícita de baixa confiança. Recomendar fontes secundárias (associações setoriais, relatórios públicos). |
| Cliente em segmento muito nichado | Buscar tendências em mercados adjacentes como proxy. Registrar a extrapolação como premissa explícita. |
| Consultor sem acesso a dados internos de performance do cliente | Avaliar impacto das tendências com base no perfil do ICP — não exige dados internos do cliente para esta análise. |

---

## Formato de Saída Obrigatório

```markdown
# Análise de Tendências e Oportunidades de Mercado — [Nome do Cliente]

> **Status:** `[AGUARDANDO VALIDAÇÃO DO CONSULTOR]`
> **Data:** [data de execução]
> **Fontes:** context/business.md + context/gtm.md + dados fornecidos pelo consultor em [data]
> **Limitações registradas:** [listar dados ausentes ou estimados com baixa confiança]

---

## Mapa de Tendências

| Tendência | Dimensão | Impacto | Justificativa | Base de Evidência |
|---|---|---|---|---|
| | Econômica / Tecnológica / Comportamental / Regulatória / Competitiva | Alto / Médio / Baixo | | |

---

## Oportunidades Identificadas

| Oportunidade | Tendência-Origem | Categoria | Conexão SAM/SOM |
|---|---|---|---|
| | | Dor emergente / Mudança de comportamento / Ineficiência / Lacuna competitiva | Dentro do SAM / Especulativa |

---

## Análise de Alavancas de Crescimento

| Oportunidade | Throughput Potencial | Aderência | Complexidade | Dependência Bloqueante | Decisão |
|---|---|---|---|---|---|
| | Alto / Médio / Baixo | Alta / Média / Baixa | Baixa / Média / Alta | Sim / Não | Priorizar / Descartar / Monitorar |

---

## Oportunidades Priorizadas

| # | Oportunidade | Tendência-Origem | Throughput | Velocidade | Risco | Próximo Passo |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

---

## Hipóteses de Crescimento

*Hipóteses derivadas das oportunidades priorizadas, já ancoradas nas restrições do sistema:*

1. **[Hipótese 1]** — Se [oportunidade], então [crescimento esperado], desde que [restrição/condição do sistema].
2. **[Hipótese 2]** — ...
3. **[Hipótese 3]** — ...

---

## Conexão com o Diagnóstico de Travas

*Quais tendências e oportunidades amplificam ou são amplificadas pelas Travas já identificadas:*

| Trava | Como a tendência/oportunidade se conecta |
|---|---|
| Trava 7 — Exposição | |
| Trava 6 — Atenção | |
| Trava 5 — Interesse | |
| Trava 4 — Qualificação | |
| Trava 3 — Compromisso | |
| Trava 2 — Decisão | |
| Trava 1 — Retenção | |

*Registrar apenas as Travas efetivamente impactadas.*
```

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/analise-de-tendencias.md`
- Se o diretório não existir, criá-lo.
- Se não tiver permissão de escrita, exibir o conteúdo no chat para o consultor salvar manualmente.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output.

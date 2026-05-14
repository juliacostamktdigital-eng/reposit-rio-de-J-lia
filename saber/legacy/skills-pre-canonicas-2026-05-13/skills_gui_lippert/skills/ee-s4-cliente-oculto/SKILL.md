---
name: ee-s4-cliente-oculto
version: "1.1.0"
description: "Simulacao de cliente oculto: cria perfil de comprador ficticio, operador executa no canal real, IA analisa a conversa e gera relatorio com nota 0-10. Use quando o operador disser 'cliente oculto', 'mystery shopping', 'testar atendimento', 'simular compra', ou apos o diagnostico comercial."
changelog:
  - version: "1.0.0"
    date: "2026-01-01"
    notes: "Versao inicial."
  - version: "1.1.0"
    date: "2026-05-07"
    notes: "Output alterado de .json para .md. Estrutura do relatorio fixada com secoes obrigatorias. Adicionada dupla verificacao de timestamps obrigatoria antes de classificar C1. Instrucao explicita: timestamps sao legíveis nos prints — nunca declarar [nao disponivel] sem tentar ler todas as mensagens visiveis."
dependencies:
  - ee-s4-diagnostico-comercial
outputs: ["ee-s4-cliente-oculto.md"]
week: 4
estimated_time: "1.5h"
---

# Cliente Oculto IA

Voce e um especialista em avaliacao de experiencia de compra e mystery shopping. Vai criar um cenario de simulacao realista para testar o atendimento comercial do cliente e, apos a execucao pelo operador, analisar a conversa gerando um relatorio detalhado com nota e recomendacoes.

> **IMPORTANCIA:** Este teste revela a realidade do atendimento — nao o que o cliente diz que faz, mas o que realmente acontece. O resultado alimenta diretamente os scripts do SDR IA.

## Dados necessários

1. `client.json` (seção `briefing`) — NOME_CLIENTE, PRODUTO_SERVICO, CANAL_CONTATO
2. `outputs/ee-s1-persona-icp.json` — RESUMO_ICP, perfil demografico, comportamento
3. `outputs/ee-s4-diagnostico-comercial.json` — objecoes mapeadas, gargalos, SLA
4. `client.json` (seção `connectors`) — dados adicionais de canais

Confirme com o operador:

> Vamos criar e executar um cliente oculto para {NOME_CLIENTE}.
> Canal principal: {CANAL — WhatsApp / formulario / email / Instagram DM}
> Correto? IMPORTANTE: voce (operador) vai executar a simulacao manualmente. Eu crio o roteiro e depois analiso.

---

## Geração

Gere o output COMPLETO de uma vez: perfil do comprador + script da simulação. Use os dados de `client.json` (briefing) e outputs de skills dependentes em `outputs/`.

Consulte `references/criterios-avaliacao-ee-s4-cliente-oculto.md` para os criterios de avaliação.

### Perfil do comprador simulado

- Nome fictício, contexto plausível e específico
- Urgência (alta/média/baixa) com motivo
- Budget declarado (como/quando mencionar)
- Objeção principal (alinhada ao diagnóstico)
- Nível de conhecimento do produto

### Script da simulação

**Mensagem de abertura:** como o ICP real enviaria
**Mensagens de acompanhamento:** se não houver resposta (30min, 2h)
**4 perguntas para fazer ao longo da conversa:** cada uma testando uma dimensão (conhecimento do produto, objeção de preço, urgência/follow-up, personalização)
**Comportamento do comprador:** atraso de resposta, cautela, objeção de preço na proposta, "vou pensar" para testar follow-up

Apresente ao operador e peça validação de que é realista.

### Execução (MANUAL pelo operador)

> **ATENCAO: Esta etapa e MANUAL.** Voce (operador) executa a simulação seguindo o roteiro.
>
> **Instrucoes:**
> 1. Use numero/conta que NÃO esteja associado a V4 ou ao seu nome
> 2. Siga o roteiro mas adapte naturalmente
> 3. Anote tempos exatos de cada resposta
> 4. Documente TODA a conversa (print ou cópia)
> 5. NÃO revele que é teste
> 6. Se pedirem dados sensíveis, invente dados fictícios
>
> Cole aqui o histórico completo com horários quando terminar.

Aguarde o operador executar e colar o histórico.

### Análise da conversa e relatório

Após receber o histórico (prints ou texto colado), execute a **dupla verificação de timestamps** antes de qualquer avaliação:

> **VERIFICAÇÃO OBRIGATÓRIA DE TIMESTAMPS — faça antes de classificar C1:**
> 1. Percorra TODAS as mensagens visíveis nos prints/histórico em busca de timestamps (formato HH:MM).
> 2. Identifique: (a) timestamp da primeira mensagem do lead, (b) timestamp da primeira resposta automática, (c) timestamp da primeira resposta humana.
> 3. Calcule o intervalo em minutos entre (a) e (c).
> 4. Somente declare `[não disponível]` se, após percorrer todos os inputs, nenhum timestamp for visível. **Nunca declare [não disponível] sem realizar esta varredura explicitamente.**
> 5. Se os prints forem screenshots de WhatsApp, os timestamps estão nos balões de mensagem — leia os dígitos com atenção, especialmente para não confundir "11:07" com "11:37".

Após a verificação, gere o relatório **diretamente no arquivo** `clientes/{slug}/outputs/ee-s4-cliente-oculto.md`. Não apresente como texto de resposta antes de salvar.

---

#### Estrutura obrigatória do .md

```
# Cliente Oculto — {NOME_CLIENTE}

> Data de execução: ...
> Canal testado: ...
> Produto simulado: ...
> Fontes: [lista dos inputs utilizados]
> Dados não visíveis nos inputs sinalizados como [não disponível].

---

## Nota Geral: X/10 — CLASSIFICAÇÃO

> Resumo de 2 linhas: o que sustenta a nota.

---

## Avaliação por Critério

### C1 — Tempo de Primeira Resposta
Peso: 20% · Nota: X/10
[timestamp lead] → [timestamp bot] → [timestamp humano] = X minutos
Evidência: screenshot ou trecho com horário.

### C2 ... C7 (mesma estrutura)

---

## Cálculo da Nota

| Critério | Peso | Nota | Contribuição |
...
| TOTAL | % avaliado | — | X,XX |

> Nota ajustada e critério de arredondamento.

---

## Pontos Fortes
(com evidência específica + timestamp ou trecho)

## Pontos Críticos
(em ordem de impacto: problema + impacto estimado)

---

## Limitações desta Análise
(apenas limitações reais — nunca incluir "timestamps não legíveis" se foram lidos)
```

---

**Nota geral: X/10** (EXCELENTE 9-10 / BOM 7-8 / REGULAR 5-6 / RUIM 3-4 / CRITICO 0-2)

Para cada critério: nota 0-10 + observação + evidência (trecho ou timestamp da conversa). Se timestamp foi lido, incluí-lo explicitamente na evidência.

## Auto-validação

Antes de salvar, verifique:

- [ ] Timestamps de C1 foram lidos e documentados com os valores exatos (HH:MM)?
- [ ] Nenhum `[não disponível]` foi declarado sem varredura explícita dos inputs?
- [ ] Mencionou o cliente pelo nome?
- [ ] Usou dados reais — nenhum número inventado?
- [ ] Critérios de avaliação têm evidência específica (trecho ou timestamp)?
- [ ] Seção "Limitações" não repete algo que foi avaliado com sucesso?

Se falhou em qualquer item → corrija antes de salvar.

## Finalização

Salve em `clientes/{slug}/outputs/ee-s4-cliente-oculto.md`.

Atualize `client.json`: progress.skills → completed, version++, append em history[].

Informe ao operador:
- "Cliente oculto concluido. Nota: {X}/10. Pontos criticos: {lista resumida}."
- Pergunte: "O relatorio reflete o que voce observou? Algum detalhe que interpretei errado?"
- Sugira: `/ee-s5-scripts-sdr` (criar scripts que corrigem os problemas encontrados)

**NOTA:** O relatório pode ser compartilhado com o cliente como evidência do valor do SDR IA. O contraste "antes vs depois" é poderoso.

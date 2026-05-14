---
name: diagnostico-social-media
description: "Diagnóstico do Instagram com foco em Bio, Destaques e Posts Fixados como funil de conversão, benchmarking vs 3 concorrentes, e nova bio sugerida. Produto Saber — diagnostica sem redesenhar. Use quando o operador disser 'diagnosticar Instagram', 'auditoria de redes sociais', 'diagnóstico de social media', ou ao iniciar o POP 5.3."
dependencies:
  - definicao-icp-b2b
  - estudo-concorrentes
tools: []
outputs: ["diagnostico-social-media.json"]
week: 3
estimated_time: "2h"
ucm: "1 e 2"
multimodal: true
---

# Diagnóstico de Social Media — Instagram como Nova Landing Page

Você é um especialista em estratégia de social media com foco em conversão para PMEs brasileiras. Vai diagnosticar o perfil do Instagram do cliente com foco em Bio, Destaques e Posts Fixados — a "estática permanente" que o tráfego pago vai encontrar.

> **PRINCÍPIO ESTRATÉGICO:** "O perfil do Instagram é a nova Landing Page. Se o tráfego leva ao perfil e encontra uma casa desarrumada, a conversão cai." O foco é a ESTÁTICA — o que funciona 24h/7d independentemente de frequência de posts.
>
> **ANTI-PADRÃO:** Tratar social media apenas como vitrine estética. Toda sugestão deve ter viés comercial. "Mudar destaque para levar ao WhatsApp" > "capas mais bonitas".
>
> **PRODUTO SABER:** Esta skill diagnostica — não executa. Gera recomendações mas não redesenha a bio, não cria novas capas, não produz conteúdo.

## Dados necessários

1. `client.json` (briefing) — NOME_CLIENTE, SEGMENTO, URL_INSTAGRAM
2. `outputs/definicao-icp-b2b.json` ou `outputs/definicao-persona-b2c.json` — ICP para avaliar alinhamento
3. `outputs/estudo-concorrentes.json` — concorrentes para benchmarking

Solicite ao operador:
> "Para o diagnóstico de social media, preciso:
> 1. **URL do Instagram** do {NOME_CLIENTE}
> 2. **Screenshots:** perfil completo (bio + 9 posts do feed) + capas dos destaques + 3 posts fixados (se houver)
> 3. **Instagram de 3 concorrentes** que considera referência (para benchmarking)
> 4. Qual é o objetivo principal do Instagram agora? (gerar leads / vender / educar / construir autoridade)"

> **Atenção multimodal:** Você pode analisar screenshots do perfil. Peça prints ao operador.

---

## Geração

Gere o output COMPLETO após receber os dados.

### CHECK INICIAL — Informações Básicas

| Item | Dados atuais |
|------|-------------|
| @usuario | {handle} |
| Tipo de conta | Personal / Creator / Business |
| Seguidores | {n} |
| Seguindo | {n} |
| Posts | {n} |
| Link na bio | {URL ou "sem link"} |
| Ferramenta de link | {Linktree / página própria / WhatsApp direto / sem link} |

---

## SEÇÃO 1: Diagnóstico da Bio

A bio é o "above the fold" do Instagram. Um visitante do ICP deve entender o que a empresa faz em 5 segundos.

### Análise da Bio Atual

**Bio atual (transcrição):**
```
{texto exato da bio como aparece}
```

**Checklist de elementos:**

| Elemento | Status | Avaliação |
|----------|--------|-----------|
| Foto de perfil legível (logo/rosto em escala pequena) | ✅/❌/⚠️ | {análise} |
| Nome do perfil tem palavra-chave do nicho | ✅/❌/⚠️ | {análise} |
| Descrição diz O QUÊ e PARA QUEM | ✅/❌/⚠️ | {análise} |
| Há uma promessa/benefício (não apenas descrição de serviço) | ✅/❌/⚠️ | {análise} |
| CTA claro na bio | ✅/❌/⚠️ | {análise} |
| Link ativo e funcionando | ✅/❌/⚠️ | {análise} |
| Emojis usados com moderação e propósito | ✅/❌/⚠️ | {análise} |

**Teste dos 5 segundos:** Um visitante do ICP entende o que a empresa faz e por que deve contatar em 5 segundos?
- Resultado: {Sim / Parcialmente / Não}
- Justificativa: {análise específica}

**Nova bio sugerida:**
```
{bio reformulada com: palavra-chave no nome / promessa clara / CTA específico / link}
```
Explicação da lógica: {por que cada elemento foi escolhido}

---

## SEÇÃO 2: Diagnóstico dos Destaques (Stories Highlights)

Destaques funcionam como o "menu de navegação" do site — o ICP usa para entender a empresa antes de comprar.

**Destaques existentes:**

| Destaque | Capa | Conteúdo | Avaliação | Score |
|----------|------|----------|-----------|-------|
| {nome} | {qualidade da capa} | {descrição resumida} | {análise} | /5 |

**Destaques AUSENTES que deveriam existir:**

| Destaque faltante | Por que é crítico | Conteúdo sugerido |
|-------------------|------------------|-------------------|
| "Depoimentos/Cases" | Prova social é o principal gatilho de confiança para o ICP | {stories com resultados, fotos de clientes, prints de mensagens} |
| "Quem Somos" | ICP precisa entender o nível de expertise antes de contatar | {história da empresa, equipe, certificações, tempo de mercado} |
| "Serviços/Como funciona" | Reduz fricção: ICP não precisa entrar em contato para entender o que é vendido | {explicação visual do produto/processo} |
| {outros conforme ICP} | {justificativa} | {conteúdo} |

**Avaliação de capas:**
- Seguem identidade visual? {Sim/Parcialmente/Não}
- São legíveis em miniatura (70×70px)? {Sim/Não}
- Sugestão: {se há capas problemáticas}

---

## SEÇÃO 3: Diagnóstico dos Posts Fixados (Top 3 do Feed)

Posts fixados são o "primeiro contato". Estrutura ideal: 1) Pitch de Autoridade/Vendas, 2) Prova Social Matadora, 3) Isca Digital ou Oferta.

**Posts fixados atualmente:**

| Posição | Tipo de post | Objetivo percebido | Score | Recomendação |
|---------|-------------|-------------------|-------|--------------|
| #1 (topo) | {imagem/vídeo/carrossel} | {o que comunica} | /5 | {manter/substituir por X} |
| #2 | {tipo} | {objetivo} | /5 | {recomendação} |
| #3 | {tipo} | {objetivo} | /5 | {recomendação} |

**Se não há posts fixados:** erro crítico — qualquer post aleatório aparece no topo. Prioridade alta para fixar.

**Sugestão de posts a fixar:**
1. Fixado #1: {tipo + tema + por que nesta posição}
2. Fixado #2: {tipo + tema}
3. Fixado #3: {tipo + tema}

---

## SEÇÃO 4: Benchmarking vs 3 Concorrentes

Para cada concorrente, analisar os mesmos 3 componentes:

| Concorrente | Bio score | Destaques score | Fixados score | Diferencial principal | Gap vs {NOME_CLIENTE} |
|-------------|----------|----------------|--------------|----------------------|----------------------|
| {nome} | /5 | /5 | /5 | {o que fazem bem} | {onde supera o cliente} |

**Frequência de postagem comparada:**

| Conta | Posts/semana | Formatos | Engajamento estimado |
|-------|-------------|---------|---------------------|
| {NOME_CLIENTE} | {n} | {tipos} | {baixo/médio/alto} |
| {Concorrente A} | {n} | {tipos} | {nível} |

**Insights do benchmark:**
- O que os concorrentes fazem que o {NOME_CLIENTE} deveria considerar: {análise}
- O que nenhum concorrente faz (oportunidade): {análise}

---

## RESUMO EXECUTIVO

**Score geral do perfil:** {X}/15 (Bio {x}/5 + Destaques {x}/5 + Fixados {x}/5)

**Escala:**
- 13-15: Perfil bem preparado para receber tráfego pago
- 9-12: Ajustes pontuais necessários antes de escalar tráfego
- 5-8: Reconstrução significativa da estática necessária
- < 5: Tráfego pago enviado para este perfil está sendo desperdiçado

**Top 3 gaps prioritários:**
1. {gap com maior impacto imediato} — impacto estimado: {%} de melhoria em conversão orgânica}
2. {segundo gap}
3. {terceiro gap}

**Custo da inação:** enviar tráfego pago para um perfil sem {principal gap} = perda estimada de {X}% dos visitantes que poderiam converter.

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Os 3 componentes (Bio/Destaques/Fixados) foram analisados como seções separadas?
- [ ] A nova bio sugerida foi escrita (não apenas criticada a atual)?
- [ ] Destaques faltantes têm conteúdo sugerido (não apenas "falta destaques")?
- [ ] Benchmarking de 3 concorrentes está completo?
- [ ] Todas as recomendações têm viés comercial (não apenas estético)?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

- "O diagnóstico da bio reflete o que um visitante novo percebe ao chegar no perfil?"
- "Os destaques ausentes fazem sentido para o que o ICP busca antes de contatar?"
- "Os posts fixados atuais — você escolheu eles intencionalmente ou estão lá por padrão?"
- "O benchmark com os concorrentes — algum que você considera referência e que não estava na lista?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/diagnostico-social-media.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Sugira próximas skills:
   - `/plano-de-acao-5w2h` (POP 5.4 — transformar diagnóstico em plano de ação de criativos)
   - "Diagnóstico de Social Media concluído. Score: {X}/15. Top gap: {gap principal}. Nova bio sugerida: '{bio}'."

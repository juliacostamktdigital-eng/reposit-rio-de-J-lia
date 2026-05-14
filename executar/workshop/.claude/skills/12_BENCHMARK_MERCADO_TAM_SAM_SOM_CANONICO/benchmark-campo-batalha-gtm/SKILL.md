---
name: benchmark-campo-batalha-gtm
description: Mapeia campo de batalha GTM com concorrentes, evidências de mídia e jornada, voz do cliente, padrões dominantes, ruído de mercado, gaps ranqueados, riscos com janela temporal, conflitos internos da marca, ativos de PR sub-aproveitados e implicações para assets v1 antes de DEOC, plano de mídia e criativos. Use após handoff e diagnóstico GTM, quando precisar de baseline copiável e diferenciação com lastro.
---

# Benchmark Campo Batalha GTM

## Quando Usar

Use na etapa de inteligência de mercado **antes** de consolidar DEOC, plano de mídia, briefing criativo ou LP.

O benchmark não substitui TAM/SAM/SOM, mapa 2x2, SWOT específica ou beachhead quando N2 exige esses blocos; ele prepara o terreno e alimenta essas decisões.

Não use como pesquisa infinita ou coleção de exemplos bonitos. Se o achado não muda DEOC, oferta, plano de mídia, criativo, LP ou backlog, ele deve ficar fora do output principal.

## Princípio

Benchmark sem evidência ou sem ligação com decisão vira teatro: **cada achado relevante precisa de lastro** (link, print, data quando couber, nota de fonte).

Antes de executar, a operação deve saber responder:

- qual mercado se tenta capturar;
- quem disputa a mesma atenção;
- quais mensagens estão saturadas;
- onde há brecha de diferenciação;
- qual amostra de concorrentes é válida;
- como o público-alvo fala da categoria (voz do cliente);
- o que a marca diz vs. o que o dono e o mercado percebem (conflitos internos).

## Fronteira Com Skills Irmãs (mesmo playbook 12)

Para evitar invasão de fronteira, esta skill **não produz**:

- TAM/SAM/SOM detalhado → escopo de `sizing-mercado-tam-sam-som`. Aqui só entra **contexto macro mínimo** (tamanho, crescimento, tendências) para situar o leitor.
- Mapa competitivo 2x2 com decisão estratégica e SWOT específica do cliente → escopo de `posicionamento-competitivo-beachhead`. Aqui só entra **matriz de atributos cruzada** (presença/ausência por player) e quatro dimensões por concorrente (forte / fraco / gap / ameaça) — sem rotular como SWOT.
- Backlog de hipóteses testáveis com métrica → escopo de `benchmark-para-backlog-growth`. As oportunidades aqui são ranqueadas (P1/P2/P3) mas não viram hipóteses formais.

## Inputs Mínimos

- handoff EXECUTAR e contexto do cliente;
- segmento, produto foco, ticket, geografia;
- **se o cliente tem múltiplas unidades, registrar cada uma e seu papel** (expansão / manter / transição) — restringir o benchmark a só uma unidade tira lastro de qualquer recomendação que valha pra marca-toda;
- ICP ou persona preliminar;
- lista inicial de concorrentes (tipicamente 3 a 10) e/ou keywords de descoberta;
- canais de interesse e objetivo de aquisição;
- **fontes para voz do cliente**: reviews em portais (Google Maps, Tripadvisor, BaresSP, equivalente do segmento), comentários em redes sociais, transcrições da call de vendas, fóruns relevantes.

## Fluxo De Trabalho

1. Definir escopo e pergunta de negócio que o benchmark precisa destravar.
2. Selecionar amostra: diretos, substitutos e referências fortes do setor (evitar irrelevante).
3. Coletar evidências por player (ordem recomendada): biblioteca de anúncios → busca/SERP e LPs → redes → reviews → oferta e prova.
4. **Capturar voz do cliente** em capítulo dedicado: termos do público-alvo, termos da marca-cliente que ressoam, críticas reputacionais dos concorrentes (que viram munição), dores não resolvidas (categoria mental vazia), critérios de compra ponderados.
5. **Detectar conflitos internos da marca**: comparar bio/claims atuais do cliente com a autocrítica do dono e a percepção do mercado. Onde houver descolamento, registrar antes da S2 com proposta de resolução.
6. **Mapear ativos de PR sub-aproveitados**: cobertura espontânea, prêmios, depoimentos institucionais já existentes que não estão sendo usados.
7. Consolidar padrões que se repetem no setor (5 a 15 bullets acionáveis).
8. Listar **ruído de mercado** (promessas saturadas).
9. Montar matriz de atributos (atributo × player) e tabela de evidência por concorrente com 4 dimensões (forte / fraco / gap / ameaça) + brand awareness percebido.
10. Converter em decisões: baseline a adotar vs. onde diferenciar vs. riscos a mitigar — **ranquear oportunidades em P1/P2/P3** (medalhas 🥇🥈🥉) e **etiquetar riscos com janela temporal** (S1/S2/contínuo).
11. Registrar implicações por consumer skill downstream (DEOC, mídia, LP, criativos, próximos testes) com sub-headers explícitos.
12. **Visita de cliente-oculto nos top-3 concorrentes** antes de fechar o pacote (calibração in loco do que está em mídia paga vs. realidade da operação) — registrar como ação operacional pré-DEOC.
13. Registrar todas as fontes/URLs no final, agrupadas por categoria (macro / concorrentes / voz do cliente). Hipóteses sem lastro viram pergunta ou backlog, não conclusão.

## Output Esperado

- versionamento do documento (`versão`, `data`, `próxima revisão`);
- sumário executivo (3 a 5 bullets de tese acionável);
- contexto do cliente + contexto macro mínimo (tamanho, crescimento, tendências, sazonalidade);
- voz do cliente como capítulo dedicado;
- amostra de concorrentes com motivo de inclusão;
- tabela de evidências por player com 4 dimensões + brand awareness;
- matriz de atributos cruzada (atributo × player);
- 5 a 15 bullets de padrões dominantes;
- ruído de mercado listado;
- conflitos internos da marca + resolução proposta;
- ativos de PR sub-aproveitados + uso recomendado;
- oportunidades ranqueadas (🥇 P1, 🥈 P2, 🥉 P3);
- riscos com janela temporal (S1 / S2 / contínuo);
- baseline vs. diferenciação;
- implicações em sub-headers por consumer skill;
- bloco de fontes agrupadas por categoria.

Use `templates/benchmark-gtm.md` como referência de estrutura.
Use `templates/benchmark-gtm.json` com o script para gerar Markdown a partir de dados estruturados.

## Script Utilitário

```bash
python3 scripts/build_benchmark_gtm.py templates/benchmark-gtm.json --md /tmp/benchmark-gtm.md
```

O script é retrocompatível: campos opcionais ausentes não quebram a renderização. Oportunidades são reordenadas por prioridade (P1 → P2 → P3); riscos são reordenados por janela temporal (S1 → S2 → contínuo).

## Definition Of Done

- Versão, data e próxima revisão estão preenchidas no cabeçalho.
- Sumário executivo com 3 a 5 bullets de tese acionável.
- Contexto macro mínimo registrado (sem invadir TAM/SAM/SOM).
- Voz do cliente preenchida com pelo menos termos do público + 1 dor não resolvida + critérios de compra.
- Amostra e critérios de escolha estão documentados; cobre todas as unidades relevantes da marca-cliente.
- Cada concorrente tem 4 dimensões (forte / fraco / gap / ameaça) e brand awareness percebido.
- Síntese de padrões em 5 a 15 bullets acionáveis.
- Conflitos internos da marca, se houver, registrados com resolução proposta.
- Oportunidades ranqueadas em P1/P2/P3; pelo menos 1 P1 com implicação concreta.
- Riscos têm janela temporal (S1 / S2 / contínuo).
- Implicações cobrem DEOC, mídia, LP, criativos e próximos testes em sub-headers.
- Cliente-oculto top-3 está agendado ou registrado como pendência operacional pré-DEOC.
- Todas as afirmações citadas no documento aparecem no bloco `Fontes` com URL ou nota.

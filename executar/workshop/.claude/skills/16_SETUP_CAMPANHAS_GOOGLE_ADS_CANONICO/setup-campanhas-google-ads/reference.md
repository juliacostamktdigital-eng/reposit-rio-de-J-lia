# Referência — Setup Google Ads (playbook 16)

Fonte: **`16_SETUP_CAMPANHAS_GOOGLE_ADS_CANONICO.md`**. Não substitui políticas atuais do Google Ads, GA4 nem parecer jurídico (marca concorrente, criativos).

## 1. Princípio (Seção 1)

Antes de rodar mídia: conta/faturamento; tag/GA4/GTM; conversões; públicos/listas; estrutura sem fragmentar dados; termos, URLs e assets alinhados à oferta; UTMs e IDs; planilha backup e CRM para reconciliar lead e qualidade.

## 2. Links oficiais / citados (Seção 2)

- [Performance Max — documentação](https://support.google.com/google-ads/answer/10724896)
- [SA360 — nota relacionada](https://support.google.com/sa360/answer/12368425)

## 3. Inputs (Seção 3)

DEOC; plano de mídia; LP; contrato; taxonomia; backup; CRM/SLA; keywords/temas; negativas iniciais; assets quando PMax/YouTube/Display; acessos Ads, GA4, GTM, Search Console quando aplicável.

## 4. Checklist de conta (Seção 4)

Conta correta; faturamento ativo; permissões; auto-tagging avaliado; GA4 vinculado quando aplicável; GTM publicado; tag Google instalada; conversões principais configuradas; enhanced conversions quando possível; importação offline planejada para MQL/SQL/venda quando houver CRM; listas remarketing elegíveis; Customer Match preparado quando houver base; UTMs preservadas até CRM e backup.

## 5. Conversões (Seção 5)

**Mínimas citadas:** formulário; clique/envio WhatsApp quando for conversão real; ligação qualificada quando aplicável; MQL importado; SQL/oportunidade importado; venda/receita quando houver ciclo e dado.

**Regra:** otimizar a conversão **mais profunda com volume suficiente**; sem volume — começar lead/formulário, qualidade na planilha growth, importar MQL/SQL com consistência; separar principais vs secundárias/observação.

## 6. GTM e parâmetros (Seção 6)

Validar: `gclid`; `gbraid`/`wbraid` quando aplicável; UTMs; `v4_client_id`, `v4_campaign_id`, `v4_adgroup_id`, `v4_creative_id`, `v4_test_id`; campos hidden; envio backup e CRM. **Não publicar sem testar submissão real de lead.**

## 7. Search (Seção 7)

**Quando:** demanda ativa (problema, solução, categoria, concorrente se permitido, marca para defesa/captura).

**Estrutura:** Campanha 1 não-marca (grupos problema, solução/categoria, comparativos, segmento/persona); Campanha 2 marca separada; Campanha 3 concorrentes só se permitido/estratégico.

**Keywords:** alta intenção; frase/exata no início; ampla só com conversão e negativas maduras; **negativas desde o dia 1.**

## 8–9. PMax e Display (Seções 8–9)

**PMax quando:** conversão bem configurada; assets suficientes; audience signal relevante; budget para aprendizado; objetivo de expandir além de Search.

**Evitar no início:** conversão não validada; LP sem preservação de dados; sem asset decente; budget muito baixo; necessidade de controle granular imediato; sem sinais mínimos.

**PMax estrutura:** 1 campanha aquisição; asset groups oferta principal, segmento/persona, dor/caso — em geral **2 a 5 grupos**, não muitos no início.

**Audience signals:** Customer Match, visitantes site, leads/MQLs, termos alta intenção, URLs referência, in-market, GA4 — **não sobrecarregar**; começar pelos mais fortes.

**Assets PMax:** headlines curtas/longas, descrições, imagens quadradas/horizontais/verticais quando possível, logo, vídeo próprio preferível (evitar só auto-gerado).

**Display:** só com função clara no plano; targeting, exclusões anti-ICP, placements/apps bloqueados, brand safety, frequência, janela remarketing, criativos por formato, métrica de leitura. Não como “sobra de verba”.

## 10. Nomenclatura (Seção 10)

**Campanha:** `{campaign_id} | {tipo_campanha} | {objetivo} | {movimento} | {slug}`

**Grupo / asset group:** `{adgroup_id} | {intencao} | {temperatura} | {tipo} | {slug}`

**Asset/anúncio:** `{creative_id} | {formato} | {hook} | {persona} | {slug} | {versao}`

## 11. Negativas (Seção 11)

Exemplos: vagas/emprego; grátis/free; curso/aula; PDF/modelo quando indesejado; termos irrelevantes; regiões fora do escopo; marca própria em não-marca quando a leitura exige aquisição pura. Revisar buscas na primeira semana e cadência semanal no início.

## 12. Orçamento (Seção 12)

Não fragmentar demais; período mínimo de aprendizado; evitar mudanças grandes antes da janela de leitura; ajustar gradualmente; tCPA/tROAS com histórico suficiente; maximizar conversões para volume inicial; importar offline para qualidade. PMax: não alterar diariamente sem evidência.

## 13. Estrutura inicial (Seção 13)

**Mínimo leadgen:** 1 Search não-marca; 1 Search marca se necessário; remarketing/Display/YouTube só com público e objetivo; PMax só se conversões/assets/sinais adequados.

**Maturidade:** Search por intenção; marca separada; PMax com asset groups por oferta/segmento; remarketing próprio; import offline MQL/SQL/venda.

## 14. Checklist pré go-live (Seção 14)

Conversões testadas; enhanced conversions avaliadas; UTMs e IDs aplicados; lead teste na backup; CRM recebeu ou será conciliado; Search com negativas iniciais; PMax com assets suficientes; audience signals configurados; Search clusters/negativas/RSAs conferidos quando aplicável; PMax asset groups, URL expansion, brand controls e metas conferidos quando aplicável; Display placements/apps, frequência, exclusões e brand safety quando aplicável; URLs finais conferidas; orçamento, lances e datas; hipótese na planilha growth; change log preparado.

## 15. N2 (Seção 15)

Conta/faturamento; GTM/tag/conversões OK; UTMs e IDs aplicados; estrutura Search/PMax documentada; públicos/listas/sinais configurados; backup captura lead teste; hipótese e leitura registrados.

## 16. N3 (Seção 16)

MQL/SQL/venda via importação offline; revisão de termos e negativas em cadência; performance de assets alimenta criativos; consolidação/separação PMax/Search por dados; orçamento com qualidade comercial, não só CPL.

## 17. O que evitar (Seção 17)

Sem conversão testada; PMax sem asset decente; PMax sem audience signal; misturar marca e não-marca sem leitura separada; otimizar clique quando objetivo é lead qualificado; não importar qualidade offline; Search sem negativas; alterar budget/lance todo dia; lead sem backup; avaliar só por CPL sem MQL/SQL.

# Referência — QA go-live Meta (playbook 15)

Fonte: **`15_SETUP_CAMPANHAS_META_ADS_CANONICO.md`**. Uso: conferência final antes de verba; não substitui políticas da Meta nem validação legal de criativo/LP.

## Mapa: grupos do checklist ↔ seções

| Grupo no JSON | Seções / tema |
|---------------|----------------|
| `principio` | 1 — perguntas que a conta precisa responder antes do ar |
| `conta` | 4 — BM, conta, pagamento, página, IG, domínio, pixel, CAPI, permissões, backup, CRM |
| `eventos` | 5 — profundidade do evento vs volume; eventos testados / priorizados |
| `publicos_estrutura` | 6–8, 7.3–7.5 — temperatura separada, exclusões, ordem de magnitude de conjuntos (evitar 12+ sem motivo), coerência com objetivo |
| `nomenclatura_ids` | 10 — `campaign_id`, `adgroup_id`, `creative_id` na taxonomia |
| `criativos` |11 — 3–5 anúncios por conjunto, variação real, hipótese por criativo |
| `orcamento` |12 — fragmentação, mínimo por conjunto, CBO vs ABO |
| `go_live` |13 — checklist explícito pré ativação |
| `n2_complemento` |14 — itens N2 não redundantes com 13 (`v4_*`, públicos padrão criados, subtipos) |
| `subtipos` |14 + 9 — lead nativo, conversão site, engajamento: checklist específico obrigatório **quando aplicável** |
| `anti_padroes` |16 — qualquer detecção tende a bloquear go-live |

## Lista espelhada — Seção 13 (go-live)

Reprodução fiel do canônico para auditoria:

1. campanha criada com ID  
2. conjuntos criados com ID  
3. anúncios criados com ID  
4. público e temperatura corretos  
5. exclusões aplicadas  
6. pixel/eventos testados  
7. UTMs aplicadas  
8. planilha backup testada  
9. CRM/handoff testado  
10. criativos aprovados  
11. matriz de testes registrada  
12. campos e perguntas do lead nativo conferidos **quando aplicável**  
13. regra de criação/uso de públicos de engajamento e vídeo definida **quando aplicável**  
14. orçamento e datas conferidos  
15. hipótese registrada na planilha de growth  
16. change log preparado para mudanças de estrutura, público, criativo, evento ou orçamento  

## Seção 16 — anti-padrões (lista para o JSON)

Trechos do canônico usados como flags `detectado`:

- campanha sem ID  
- criativo sem ID  
- público quente e frio misturados sem intenção  
- 12+ conjuntos com pouca verba  
- muitos interesses pequenos sem volume  
- remarketing sem exclusão de convertidos  
- criativos genéricos que não segmentam pelo próprio conteúdo  
- pixel/evento não testado  
- lead sem planilha backup  
- otimizar só por CPL sem qualidade comercial  
- lead nativo sem SLA ou sem perguntas mínimas  
- conversão no site sem evento validado  
- engajamento usado indefinidamente sem ponte para remarketing/performance  

## Status por item

- **`ok`** — verificado.  
- **`gap`** — falha ou risco inaceitável para o movimento atual.  
- **`n.a.`** — não se aplica (ex.: item 12 quando não há lead nativo **e** nenhum formulário nativo no escopo).  

Itens sem status preenchido são tratados como **incompletos** na geração do relatório.

No arquivo JSON, `checklist[].status` aceita textos equivalentes a **ok**, **gap** e **n.a.** (via normalização no script). Em `anti_padroes[]`, use o booleano **`detectado`**.

## Links externos (Seção 2 do canônico)

- [Como escolher públicos no Meta Ads](https://pedrosobral.com.br/blog/c/introducao-ao-trafego-pago/como-escolher-publicos-no-meta-ads)  
- [Público certo no Meta Ads em 2025](https://pedrosobral.com.br/blog/c/introducao-ao-trafego-pago/como-anunciar-para-o-publico-certo-no-meta-ads-em-2025)  
- [3 tipos de campanha](https://pedrosobral.com.br/blog/c/introducao-ao-trafego-pago/os-3-tipos-de-campanha-que-todo-gestor-de-trafego-precisa-dominar-no-meta-ads)  
- [Guia campanhas Meta 2026](https://pedrosobral.com.br/blog/c/estrategias-de-trafego-pago/como-criar-campanhas-no-meta-ads-em-2026-o-guia-completo-para-anunciar-no-instagram-facebook-e-whatsapp)  

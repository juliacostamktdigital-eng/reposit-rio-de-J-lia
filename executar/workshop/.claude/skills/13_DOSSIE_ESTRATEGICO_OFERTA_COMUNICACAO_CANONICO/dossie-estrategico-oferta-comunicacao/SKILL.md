---
name: dossie-estrategico-oferta-comunicacao
description: Produz ou consolida o Dossiê Estratégico de Oferta e Comunicação (DEOC) como fonte única entre diagnóstico/benchmark e execução, cobrindo resumo estratégico, oferta e mecanismo, ICP/anti-ICP, problemas, alternativas, proposta de valor, narrativa, claims e matriz de tradução para mídia, criativo, LP, vendas e tracking. Inclui esqueleto Dunford de 5 elementos (POV → Alternatives → Perfect World → Differentiated Value → Proof), pirâmide emocional explícita (Feature → Vantagem → Benefício Funcional → Benefício Emocional com slot de prova obrigatório) e PUV em 3 versões (completa, headline 5s, one-liner 2s). Use após handoff, diagnóstico GTM, benchmark, TAM/SAM/SOM e beachhead e antes de plano de mídia, briefing criativo, LP, roteiros e scripts comerciais.
---

# Dossiê Estratégico Oferta Comunicação (DEOC)

## Quando Usar

Use quando precisar da **fonte canônica** que substitui a lógica paralela de UCM e DCC: uma narrativa e oferta **auditáveis** que descem até mídia, LP, criativo e vendas sem reinventar promessa.

## Camada De Redação UCM/DCC

Use a referência `executar-ai/workshop/skills/02-documento-comunicacao-ucm-dcc.md` como reforço de redação do DEOC quando o problema for clareza narrativa: ICP/anti-ICP operacional, persona, promessa, provas, objeções, CTA, proposta única de valor e regras de consistência. Não crie um documento paralelo se o DEOC já existe; incorpore esses blocos na seção correspondente do DEOC e registre a mudança no changelog.

## Pré-requisitos (playbook)

**Depois de:** handoff EXECUTAR, diagnóstico GTM, benchmark (mercado, concorrentes, TAM/SAM/SOM), discovery mínimo.

**Antes de:** plano de mídia, briefing criativo, LP, roteiros, campanhas, scripts comerciais.

## Pergunta Que O DEOC Responde

```text
O que vendemos, para quem, por que alguém deveria se importar, contra quais alternativas competimos e como isso vira comunicação executável?
```

## Workflow

1. Colete inputs obrigatórios listados em `reference.md` (Seção 4 do canônico).
2. Preencha na ordem canônica: resumo estratégico → oferta e mecanismo → ICP/personas e anti-ICP → problemas → alternativas → proposta de valor → inimigo/tese/narrativa → claims → tradução para execução.
3. **Esqueleto Dunford-style**: organize o DEOC em 5 elementos canônicos — (a) **POV/Insight nomeado** (a tese contraintuitiva que nomeia a categoria); (b) **Alternatives mapeadas como approaches** (não só concorrentes — o conjunto de caminhos que o ICP considera, incluindo "não fazer nada"); (c) **Perfect World** à la Raskin (o estado futuro que a oferta torna possível); (d) **Differentiated Value** (o que só essa oferta entrega); (e) **Proof por differentiator** (cada valor diferenciado tem prova explícita ou vira pendente).
4. **PUV em 3 versões obrigatórias**: (i) completa — 1 frase longa com ICP + problema + mecanismo + resultado; (ii) headline 5s — manchete enxuta pra LP/ad; (iii) one-liner 2s — pitch de elevador. **Teste de qualidade Dunford**: compreensível em <5s? menciona ICP? promete resultado concreto? memorável?
5. **Pirâmide emocional explícita**: para cada feature relevante, traduza Feature → Vantagem → Benefício Funcional → Benefício Emocional, com **slot de prova obrigatório por benefício emocional**. Sem prova, o benefício emocional fica como **claim pendente** (não vai pra copy nem pra vendas).
6. Garanta **oferta dizível**, **escopo explícito**, **provas mínimas** e **limites da promessa**.
7. Codifique as **regras de comunicação**: núcleo que não muda, variações permitidas por canal/cohort e usos em anúncios, LP, vendas e CRM.
8. Separe **claims permitidos**, **proibidos** e **pendentes** (com prova a obter).
9. Valide aderência a N2 com o script de auditoria antes de declarar pronto.
10. Versione mudanças por ciclo quando evoluir para N3 (changelog).

## Outputs

- **Output dual**: (i) **Executivo** — versão de 2-3 páginas pra C-level com PUV (3 versões), POV, Differentiated Value, Perfect World e prova-âncora; (ii) **Playbook técnico** — DEOC completo na ordem canônica para os times de mídia, criativo, LP e vendas. O DEOC inteiro é grande demais pra leitura executiva; o executivo serve de capa.
- matriz de tradução para plano de mídia, briefing, LP, copy, vendas e tracking;
- lista de gaps N2 quando o script apontar lacunas.

Use `templates/deoc.md` para redação manual guiada.
Use `templates/deoc.json` com o script para gerar o Markdown estruturado a partir de dados já extraídos.

## Scripts

```bash
python3 scripts/build_deoc.py templates/deoc.json --md /tmp/deoc.md
python3 scripts/build_deoc.py templates/deoc.json --audit
```

## Definition Of Done (N2 mínimo)

O DEOC só conta como N2 se integrar oferta, público, problema, concorrência e narrativa; tiver proposta de valor clara; ICP e anti-ICP operacionais; claims governados; regras de consistência de comunicação; e tradução explícita para execução. Detalhes e checklist em `reference.md` (Seções 6 e 7 do canônico).

Legado: playbooks `04_DCC` e `10_UCM` são contexto de apoio; **fonte operacional** é este DEOC.

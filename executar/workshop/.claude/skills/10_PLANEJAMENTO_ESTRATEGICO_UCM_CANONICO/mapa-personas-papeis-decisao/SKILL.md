---
name: mapa-personas-papeis-decisao
description: Mapeia personas e papéis de decisão em B2B, B2C ou alto envolvimento, detalhando dores, desejos, medos, objeções, linguagem, provas, CTA e canais prováveis. Inclui Champion identification metodológica (Mobilizer types — Go-Getter/Teacher/Skeptic — vs Talker/Blocker, sinais comportamentais, Champion test MEDDPICC), Detractor explícito (quem perde se a compra acontece), reality test do comitê (organograma assumido vs comitê real, Forrester 2026: 13 stakeholders + 9 influenciadores externos) e princípio de relevância de grupo (mensagem coletiva +20% consenso vs personalização individual −59%). Use em UCM, DEOC, planejamento de campanha, copy, LP, mídia, criativos e handoff comercial.
---

# Mapa Personas Papéis Decisão

## Quando Usar

Use quando a comunicação precisa separar quem sofre o problema, quem compra, quem paga, quem bloqueia e quem influencia.

Use especialmente para:

- definir ICP/personas;
- orientar copy e LP;
- separar mensagens por etapa;
- ajustar plano de mídia;
- preparar abordagem comercial;
- mapear comitê de compra.

## Inputs

- discovery;
- CRM;
- feedback de vendas;
- benchmark;
- segmento;
- oferta;
- UCM/DEOC;
- histórico de leads.

## Papéis B2B

- champion/promotor interno;
- decisor econômico;
- blocker técnico;
- usuário final;
- influenciador;
- jurídico/compliance;
- detractor (quem PERDE se a compra acontece — perde poder, visibilidade, orçamento ou status). Mapear estratégia de neutralização explícita.

## Identificação Metodológica do Champion

Champion não é "quem sente mais dor" — é reação comportamental ao insight. Distinguir:

- **Mobilizer (vai mobilizar)**:
  - Go-Getter: motivado por melhoria, age cedo;
  - Teacher: gosta de ensinar internamente, vende a ideia;
  - Skeptic: cético saudável, valida tecnicamente, vira aliado forte se convencido.
- **Talker (não move)**: simpático, dá feedback positivo, mas não mobiliza.
- **Blocker**: silenciosamente bloqueia.

Sinais comportamentais positivos do Champion: skepticism saudável, perguntas provocativas, vontade de mobilizar pares, acesso interno real, crédito a ganhar com a aprovação.

Champion test MEDDPICC (operacional): "posso contar com você pra preparar slides pro decisor?", "topa marcar a reunião com o financeiro?". Se topa, é Champion; se foge, é Talker.

Mobilizer não é título — é reação ao insight.

## Papéis B2C Ou Alto Envolvimento

- comprador;
- usuário/beneficiário;
- influenciador familiar;
- pagador;
- pessoa que sofre julgamento social.

## Workflow

1. Liste personas relevantes para a compra.
2. Defina o papel de cada uma na decisão (incluindo Detractor explícito).
3. Para cada persona, registre:
   - rotina;
   - dores;
   - desejos;
   - medos;
   - objeções;
   - linguagem;
   - provas que convencem;
   - CTA adequado;
   - canal provável.
4. Aplique Champion test (MEDDPICC) para classificar candidatos a Champion como Mobilizer (Go-Getter / Teacher / Skeptic), Talker ou Blocker — nomeie nominalmente quem é qual.
5. Reality test do comitê: pergunte "esse comitê é REAL ou organograma assumido? Que sinal externo confirma cada papel?". Single-threading (1 só contato real) é razão #1 de deals slip — exija ≥2 sinais comportamentais por papel.
6. Identifique conflitos entre papéis e a estratégia de neutralização do Detractor.
7. Traduza cada persona para:
   - copy;
   - LP;
   - mídia;
   - criativos;
   - vendas;
   - tracking.

## Output Esperado

- mapa de personas;
- papéis de decisão;
- dores e objeções por papel;
- provas necessárias;
- CTAs e canais prováveis;
- matriz de tradução para ativos.

Use `templates/personas-papeis.md`.
Use `templates/personas-papeis.json` com o script para gerar Markdown/CSV.

## Script Utilitário

```bash
python3 scripts/build_persona_decision_map.py templates/personas-papeis.json --md /tmp/personas.md --csv /tmp/personas.csv
```

## Definition Of Done

- Cada persona tem papel claro na decisão (Champion, Economic Buyer, User, Influenciador, Blocker, Detractor, Compliance).
- Champion está classificado como Mobilizer (Go-Getter / Teacher / Skeptic) e passou no Champion test MEDDPICC.
- Detractor está nominalmente identificado com estratégia de neutralização.
- Reality test do comitê passou: cada papel tem ≥2 sinais comportamentais externos (não é organograma assumido).
- Dores e objeções não são genéricas.
- Há prova associada ao que convence cada papel.
- CTA e canal mudam quando o papel muda.
- Output gera mensagem de relevância de grupo (Forrester 2025: +20% consenso) que apoia o comitê fazendo sense-making — não bombardeia com versões 1-a-1 (-59% consenso).
- Saída orienta campanha e venda.

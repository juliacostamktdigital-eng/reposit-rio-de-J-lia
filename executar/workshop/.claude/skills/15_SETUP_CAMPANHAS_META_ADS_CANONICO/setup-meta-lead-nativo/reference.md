# Referência — Lead nativo Meta Ads (playbook 15)

Fonte primária: **`15_SETUP_CAMPANHAS_META_ADS_CANONICO.md`**. Complemento operacional: **`assets/legacy/merge/skills/10-1-meta-lead-nativo.md`**. Esta referência **não** substitui políticas atuais da Meta nem parecer jurídico/privacidade.

## 1. Onde o lead nativo se encaixa no canônico

- **Seção 9 — Captação de leads:** objetivo é coletar contato qualificado. O canônico **separa** formulário nativo, LP/formulário externo e WhatsApp/mensagem porque cada destino altera qualidade, fricção, tracking e SLA.
- **Seção 9 — Usar captação de leads quando:** oferta clara; LP/formulário pronto (no caso nativo, o “formulário” é o Instant Form); CRM/SLA existe; planilha backup ativa; **formulário nativo tem perguntas suficientes** para intenção/qualificação **sem matar volume**; **SLA de follow-up aceito antes de ativar** lead nativo.

## 2. Eventos e pixel (Seção 5) — leadgen

Mínimos citados:

- `PageView`;
- `ViewContent` ou equivalente de visita qualificada;
- **`Lead` no envio do formulário**;
- evento customizado para `MQL` quando houver integração;
- evento customizado/offline para `SQL`, oportunidade ou venda quando houver volume e CRM.

**Regra:** otimizar o mais profundo possível **sem matar volume**. Sem volume: começar com `Lead` ou evento de formulário; qualidade comercial na planilha de growth; evoluir depois.

## 3. Públicos úteis para lead nativo (Seções 6–7)

Além dos frios/mornos/quentes gerais:

- **Morno relacionado a formulário:** “aberturas de formulário sem envio” (canônico lista como público morno) — remarketing para quem abriu e não concluiu.

Manter **temperaturas separadas** e **exclusões** (ex.: remarketing de novo lead exclui quem já converteu no formulário, quando o objetivo for aquisição de novo contato).

## 4. Estrutura e criativos (Seções 8, 11, 12)

- Seguir a estrutura inicial e limites de conjuntos do playbook (evitar fragmentação excessiva).
- **3 a 5 anúncios por conjunto** com hipótese de leitura; evitar peças quase idênticas.
- Orçamento: CBO vs ABO conforme necessidade de controle por público/teste (Seção 12).

## 5. Go-live (Seção 13) — itens específicos lead nativo

- **Campos e perguntas do lead nativo conferidos quando aplicável.**

Demais itens do checklist global (IDs, público, exclusões, pixel, UTMs, backup, CRM, criativos, matriz, orçamento, hipótese, changelog) continuam obrigatórios.

## 6. N2 (Seção 14)

Setup Meta N2 inclui:

- **Subtipos lead nativo, conversão e engajamento têm checklist específico quando usados.**

Ou seja: preencher o checklist desta skill além do setup genérico.

## 7. O que evitar (Seção 16) — trechos diretos para lead nativo

- **lead sem planilha backup;**
- **otimizar só por CPL sem qualidade comercial;**
- **lead nativo sem SLA ou sem perguntas mínimas.**

## 8. Síntese legada (skill 10-1)

Objetivo legado: estruturar Lead Nativo para **volume com lead correto** e handoff auditável.

Passos reforçados no merge:

1. Temperatura e objetivo (prospecção vs remarketing).
2. Lead Form: caminhos “volume vs maior intenção” conforme capacidade de atendimento.
3. Matriz de testes (não testar tudo junto).
4. Estrutura com exclusões anti-ICP e remarketing quando couber.
5. **Repasse + SLA** — o que acontece quando entra um lead.

**Componentes críticos para iterar (legado):** qualidade do formulário vs volume cego; SLA e registro; exclusões; matriz de testes; distribuição de criativos por função.

## 9. Mapa rápido: nativo vs outros destinos (Seção 9)

| Destino | Implicação resumida |
| --- | --- |
| Formulário nativo | Menos fricção que LP em alguns casos; qualidade depende de perguntas + SLA; tracking centrado em Lead/MQL no CRM |
| LP / formulário externo | Mais controle de página e mensagem; UTMs na LP; depende de pixel no site |
| WhatsApp / mensagem | Outro SLA e outro fluxo de conversão; não misturar critérios de qualidade “como se fosse” o mesmo lead de form longo |

## 10. Formato dos arrays no `meta-lead-nativo.json` (script)

- `lead_form.campos_padrao`: strings, ex. `"email"`, `"full_name"`.
- `lead_form.campos_custom`: objetos `campo`, `obrigatorio` (boolean), `criterio_mql` (texto).
- `lead_form.perguntas_qualificacao`: objetos `pergunta`, `tipo_resposta`, `criterio_mql`.
- `origem_rastreio.campaign_ids` e `campos_crm_obrigatorios`: listas de strings.

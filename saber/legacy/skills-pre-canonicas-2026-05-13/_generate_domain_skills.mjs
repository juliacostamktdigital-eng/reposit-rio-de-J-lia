import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = __dirname;
const BUNDLE_REF =
  "No monorepo V4OS Colli&Co: `src/data/saber-bpmn.bundle.json` (jornada, estágios, tipos A/S/H/M).";
const PLAN_REF =
  "Planejamento: `V4OS Colli&Co/Plans/Execution/saber-tobe-bpmn-app/Paperclip-planejamento-skills.md`.";

function skillMd(name, description, body) {
  const desc = description.replace(/\n/g, " ").trim();
  return `---
name: ${name}
description: >
  ${desc}
---

# ${name}

${body}

## Coordenação Paperclip

Quando o run estiver no **pool OPS** acoplado ao Paperclip: use a skill \`paperclip\` (ficheiro \`paperclip/SKILL.md\` nesta pasta) para checkout, comentários, anexos, status e header \`X-Paperclip-Run-Id\`. Trabalho de **domínio** (texto, análise, rascunhos) faz-se aqui; **governança do quadro** faz-se via API Paperclip conforme essa skill.

## Dados e processo canônicos

- ${BUNDLE_REF}
- ${PLAN_REF}

## Tipos de passo (A / S / H / M)

Alinhar saídas ao painel do bundle (\`task_types\`) e às colunas do issue (Briefing → Execução → **Aprovar entrega** quando for gate humano).
`;
}

const SKILLS = [
  [
    "saber_bpmn_context",
    `Injeta trecho do processo BPMN/jornada relevante à etapa do pedido (GC, KO, CX, …). Use no pré-run ou quando o orquestrador precisar do que é permitido na etapa.`,
    `## Escopo

Orquestrador ou agente carrega o **estágio OPS ou vendas** atual (ex.: \`gc\`, \`ko\`, \`bm\`) e produz um resumo operacional: objetivos da fase, entradas/saídas esperadas do bundle, e restrições para o run.

## Instruções

1. Identificar \`stage_id\` do issue (rótulo, template ou metadado).
2. Ler em \`saber-bpmn.bundle.json\` o objeto \`stages.<stage_id>\` (título, inputs, outputs, gateway, steps).
3. Entregar markdown curto: título da fase, lista de passos com IDs (ex. GC.02), e nota de **gate humano** quando o passo for tipo revisão (\`s\`/\`S\`).

## Saída

Bloco markdown pronto para colar na descrição do issue, em documento \`plan\`, ou no contexto do run.`,
  ],
  [
    "saber_context_pack_validate",
    `Valida pacote mínimo do pedido (ticker, links, refs POP) antes de run B2 pesado. Use na coluna Preparação ou checklist do issue.`,
    `## Pacote mínimo

Verificar presença e formato razoável de:

- \`ticker\` (código projeto Saber)
- Links: grupo/chat, pasta Drive ou equivalente, gravação/transcrição se houver
- Instruções do Coord / operador
- Referências POP ou IDs de passos quando a etapa exigir

## Instruções

1. Listar campos obrigatórios do template do issue.
2. Para cada um, OK / ausente / ambíguo.
3. Se faltar algo crítico: não iniciar síntese pesada; pedir completar no comentário (via skill \`paperclip\`).

## Saída

Checklist tabular + uma frase de **go/no-go** para o run.`,
  ],
  [
    "saber_run_artifact_version",
    `Convenção de versionamento de artefatos anexados ao issue e comentários pós-run. Use após cada run ou re-run pós-reprovação.`,
    `## Convenção

- Versão semântica leve: \`v0.1\`, \`v0.2\`, … até aprovação.
- Toda entrega em comentário: título com versão + data (ISO).
- Reprovação: incrementar minor; mencionar o comentário que motivou a revisão.

## Instruções

1. Detectar última versão no thread.
2. Propor próxima versão e nome sugerido do anexo (slug + ticker).
3. Lembrar \`X-Paperclip-Run-Id\` em mutações.

## Saída

Texto curto para colar no topo do comentário com artefato.`,
  ],
  [
    "saber_gate_comment_templates",
    `Textos mínimos para aprovar ou reprovar com rastreio ao gate B3. Use para humanos no quadro ou agente assistente de comentário.`,
    `## Aprovar (exemplo)

"Aprovo entrega **vX.Y** para envio ao cliente. Gate B3 OK. Próximo passo: …"

## Reprovar (exemplo)

"Reprovo **vX.Y**: ajustar [ponto]. Ref: comentário [link/id]. Manter em revisão."

## Instruções

Substituir colchetes; sempre referenciar versão do artefato e próxima ação clara.`,
  ],
  [
    "saber_session_extract",
    `Extrai de transcrição ou notas: objetivos, decisões, riscos, próximos passos e perguntas abertas, com referência a timestamp/turno quando existir. MVP OPS — eficiência consultor.`,
    `## Entrada

Transcrição ou notas brutas (issue, anexo ou documento).

## Saída

1. **Objetivos** acordados
2. **Decisões** (bullet, quem/decisão)
3. **Riscos** e dependências
4. **Próximos passos** acionáveis
5. **Abertos** / perguntas
6. Quando houver tempo ou turno na fonte, cite entre parênteses.

## Notas

Rascunho para revisão humana; não substitui POP nem evidências formais.`,
  ],
  [
    "saber_gc_client_pack",
    `Pacote cliente pós-handoff OPS: comunicação ao cliente (convite, DMD, próximos passos) e relatório curto desvios promessa × expectativa. Agrega GC.02 + GC.05 num único run; GC.04 fora se ASR manual.`,
    `## Entrada

Manifest/handoff resumido, ROI, transcrição ou notas da GC, instruções do Coord.

## Saída

**(a)** Texto ao cliente (tom profissional, pt-BR) com convite/links/DMD e próximos passos.
**(b)** Relatório interno curto: promessa (vendas) vs briefing/ROI; riscos de handoff; hipóteses marcadas como tal.

## Gate

Saída **não** é oficial para cliente sem aprovação no quadro (gate S).`,
  ],
  [
    "gtm_lead_brief",
    `Monta briefing do lead a partir de CRM + pesquisa leve. Funil GTM — fora do Paperclip OPS.`,
    `## Mapeamento: Q.02

## Entrada → saída

\`lead_id\` e campos CRM → texto/tabular para prospecção.

## Instruções

Resumir fit, contexto, próximo passo sugerido; citar fontes da pesquisa leve.`,
  ],
  [
    "gtm_spiced_extract",
    `Extrai framework SPICED estruturado da transcrição (pós-vínculo). Funil GTM.`,
    `## Mapeamento: Q.07

## Saída

Rascunho \`SPICED_v1\` em seções claras; marcar incertezas.`,
  ],
  [
    "gtm_call_quality_score",
    `Rubrica opcional: score e flags de qualidade de call para Cap. Funil GTM.`,
    `## Mapeamento: Q.16 (opcional)

## Saída

Score, bullets de feedback, flags (ex.: próximos passos fracos).`,
  ],
  [
    "gtm_commercial_package",
    `Ensabla pacote comercial: SPICED + histórico + notas num pacote único (Drive/Chat). Funil GTM.`,
    `## Mapeamento: P.01

## Saída

Índice do pacote + onde cada peça vive; nada sensível em claro fora dos canais aprovados.`,
  ],
  [
    "gtm_deck_roi_draft",
    `Deck + narrativa + ROI rascunho + sugestão Service Cart. Funil GTM.`,
    `## Mapeamento: P.02

## Saída

Estrutura de slides ou outline, narrativa, ROI em premissas explícitas; alinhamento a SKUs como sugestão.`,
  ],
  [
    "gtm_post_call_sales",
    `Pós-call comercial: objeções, próximos passos, valores falados. Funil GTM.`,
    `## Mapeamento: P.05

## Saída

Resumo acionável para follow-up; separar fato inferido.`,
  ],
  [
    "gtm_followup_sequence",
    `Sequência de e-mails/mensagens em rascunho a partir de objeções e contexto. Funil GTM.`,
    `## Mapeamento: P.08a

## Saída

2–4 mensagens com assunto, corpo, CTA; tom alinhado à marca.`,
  ],
  [
    "gtm_contract_draft",
    `Minuta de contrato a partir de proposta/Service Cart. Funil GTM.`,
    `## Mapeamento: C.01

## Saída

Rascunho estruturado; avisar revisão jurídica humana obrigatória.`,
  ],
  [
    "gtm_contract_consistency_check",
    `Checa consistência de valores, SKU e prazo vs JSON portfólio. Funil GTM.`,
    `## Mapeamento: C.02

## Saída

Lista de issues/discrepâncias; severidade; sem alterar sistema de registro sozinho.`,
  ],
  [
    "gtm_handoff_manifest",
    `Compila manifest.json + checksums na pasta do ticker. Passagem H1.`,
    `## Mapeamento: H1.01

## Saída

Manifesto com lista de artefatos C.07, hashes se disponíveis, metadados para OPS.`,
  ],
  [
    "ops_gc_kit",
    `Gera convite, link DMD, material pré-GC; prepara anexos ao pedido. OPS GC — GC.02.`,
    `## Mapeamento: GC.02

## Saída

Textos de convite, checklist pré-GC, links DMD; comentário Paperclip com anexos quando aplicável.

## Gate

Coord se política (S).`,
  ],
  [
    "ops_gc_deviation_analysis",
    `Análise promessa (vendas) vs briefing/ROI; riscos de handoff. OPS GC — GC.05.`,
    `## Mapeamento: GC.05

## Entrada

\`bpmns\`/bundle + transcrição ou notas.

## Saída

Tabela desvio × evidência; riscos; recomendações ao Coord.`,
  ],
  [
    "ops_dmd_reminders",
    `Lembretes e registro de status DMD quando não for só forms nativos. OPS GC — GC.07.`,
    `## Mapeamento: GC.07

## Saída

Rascunho de mensagens de lembrete + estado (enviado/pendente); integração real depende de conector (D4).`,
  ],
  [
    "ops_project_scaffold",
    `Scaffold de projeto: pastas Drive, checklist, links Ekyte quando houver automação. OPS KO — KO.01.`,
    `## Mapeamento: KO.01

## Saída

Lista de artefatos/pastas + links; partes manuais marcadas (M).`,
  ],
  [
    "ops_kickoff_prep",
    `Roteiro e PPT estrutural v0 a partir de ROI e outputs GC. OPS KO — KO.02.`,
    `## Mapeamento: KO.02

## Saída

Agenda, slides outline, perguntas obrigatórias; e-show B1 revisado.`,
  ],
  [
    "ops_post_kickoff_extract",
    `Pós-kickoff: objetivos, riscos, decisões, backlog com rastreio à transcrição. OPS KO — KO.05.`,
    `## Mapeamento: KO.05

## Saída

Mesma estrutura que sessão extract, amarrada a itens de backlog rastreáveis.`,
  ],
  [
    "ops_backlog_merge_suggest",
    `Sugere merge de template + itens de backlog; Coord valida. OPS KO — KO.06.`,
    `## Mapeamento: KO.06

## Saída

Diff sugerido em markdown; conflitos explícitos; **sem** aplicar sem humano.`,
  ],
  [
    "ops_context_compiler",
    `Documento mestre + mapa de lacunas com citações a timestamps. OPS CX — CX.03.`,
    `## Mapeamento: CX.03

## Saída

Doc único + seção lacunas; citações \`(hh:mm:ss)\` quando houver mídia.`,
  ],
  [
    "ops_context_diff",
    `Diff assistido entre versão IA e manual. OPS CX — CX.04.`,
    `## Mapeamento: CX.04

## Saída

Tabela parágrafo × status (igual/divergente/incerto); suporte a gate S.`,
  ],
  [
    "ops_canonical_publish",
    `Registra URI canônica + versão no pacote ticker quando automatizável. OPS CX — CX.07.`,
    `## Mapeamento: CX.07

## Saída

Registro proposto (URI, versão, data); passos manuais se API indisponível.`,
  ],
  [
    "ops_research_grid",
    `Sub-runs de pesquisa (demografia, TAM/SAM/SOM, concorrentes) com citações. OPS BM — BM.02.`,
    `## Mapeamento: BM.02

## Saída

Grid estruturado + fontes; hipóteses sem fonte marcadas.`,
  ],
  [
    "ops_benchmark_draft",
    `Draft de benchmark em schema-alvo; sem template usar draft β e flag schema_missing. OPS BM — BM.03.`,
    `## Mapeamento: BM.03

## Saída

Documento/PPT rascunho; frontmatter ou cabeçalho com \`schema_version\` ou \`schema_missing\`.`,
  ],
  [
    "ops_claim_coverage_check",
    `Marca afirmações sem fonte como hipótese; relatório de cobertura. OPS BM — BM.04.`,
    `## Mapeamento: BM.04

## Saída

Lista de claims × tipo (citado/hipótese) + métrica de cobertura.`,
  ],
  [
    "ops_benchmark_refine",
    `Refinamento curto do benchmark a partir de feedback do cliente. OPS BM — BM.06.`,
    `## Mapeamento: BM.06

## Saída

Changelog curto + seções atualizadas; runs curtos iterativos.`,
  ],
  [
    "ops_pop_evidence_run",
    `Roteiros POP com anexo de evidências (screenshots, checklist). OPS DG — DG.02.`,
    `## Mapeamento: DG.02

## Saída

Um pacote por POP ou lote definido; checklist de evidência cumprida/pendente.`,
  ],
  [
    "ops_diag_package_v1",
    `Documento de diagnóstico + PPT + plano de ação rascunho. OPS DG — DG.04.`,
    `## Mapeamento: DG.04

## Saída

Três camadas alinhadas: narrativa executiva, detalhe analítico, plano rascunho.`,
  ],
  [
    "ops_csat_trigger",
    `Disparo ou processamento CSAT quando integrado. OPS DG — DG.09.`,
    `## Mapeamento: DG.09

## Saída

Texto de convite CSAT + registro; depende de integração (D4).`,
  ],
  [
    "ops_solution_hypotheses",
    `Hipóteses de solução amarradas a SKUs + manual de soluções. OPS PS — PS.02.`,
    `## Mapeamento: PS.02

## Saída

Matriz hipótese × SKU × risco; flag \`manual_ausente\` se aplicável.`,
  ],
  [
    "ops_implementation_design",
    `Fases, dependências e riscos de implementação. OPS PS — PS.03.`,
    `## Mapeamento: PS.03

## Saída

Diagrama ou lista ordenada fases + dependências + riscos mitigados.`,
  ],
  [
    "ops_pricing_package",
    `Pacote de precificação vs tabela/API; interromper se API indisponível. OPS PS — PS.04.`,
    `## Mapeamento: PS.04

## Saída

Tabela de preço proposta + validações; **parar** e escalar humano se API/tabela ausente (gate).`,
  ],
  [
    "ops_client_proposal_deck",
    `PPT unificado para cliente + anexos. OPS PS — PS.07.`,
    `## Mapeamento: PS.07

## Saída

Outline completo + notas de orador; lista de anexos obrigatórios.`,
  ],
  [
    "ops_contract_generate",
    `Gera contrato quando integrado ao Service Cart; senão fluxo manual/upload. OPS N — N.04.`,
    `## Mapeamento: N.04

## Saída

Rascunho ou instruções de upload; tipo M sem integração.`,
  ],
  [
    "ops_esign_monitor",
    `Monitora assinatura e follow-ups se conector existir. OPS N — N.06.`,
    `## Mapeamento: N.06

## Saída

Status timeline + próximos lembretes; degradar a checklist se sem conector.`,
  ],
  [
    "ops_compile_handoff_executar",
    `Compila ROI + contrato + transcrições + decisões em manifest e rascunho de handoff Executar. OPS H2 — H2.01.`,
    `## Mapeamento: H2.01

## Saída

Pacote único indexado + narrativa de handoff; ligação a fila Executar fora deste repo quando aplicável.`,
  ],
  [
    "ops_notebooklm_handoff",
    `Consolida NotebookLM + links (API ou checklist assistido). OPS H2 — H2.07.`,
    `## Mapeamento: H2.07

## Saída

Lista de links, resumo sintético, gaps; sem API usar checklist manual.`,
  ],
];

for (const [name, desc, body] of SKILLS) {
  const dir = path.join(ROOT, name);
  fs.mkdirSync(dir, { recursive: true });
  const file = path.join(dir, "SKILL.md");
  fs.writeFileSync(file, skillMd(name, desc, body), "utf8");
  console.log("wrote", file);
}

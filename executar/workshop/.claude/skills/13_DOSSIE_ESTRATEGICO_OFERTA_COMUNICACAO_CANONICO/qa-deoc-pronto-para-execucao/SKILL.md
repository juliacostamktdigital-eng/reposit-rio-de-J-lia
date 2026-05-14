---
name: qa-deoc-pronto-para-execucao
description: Audita um DEOC contra os critérios N2 e N3 do playbook 13, cobertura das seções 5.1–5.9, aplicabilidade prática (seção 3) e anti-padrões (seção 8); produz decisão pronto / condicional / não pronto, gaps priorizados, riscos e revisão de claims pendentes. Use antes de aprovar investimento em mídia, produção de criativos, LP em escala ou go-live de campanhas.
---

# QA — DEOC pronto para execução

## Fonte canônica

Playbook **`13_DOSSIE_ESTRATEGICO_OFERTA_COMUNICACAO_CANONICO.md`**, em especial:

- **Seção 6** — Critério N2 (obrigatório para “pronto” na maioria dos casos).
- **Seção 7** — Critério N3 (elevação de rigor; opcional para primeiro ciclo, recomendado para escala).
- **Seção 3** — Implementação real (mídia, LP, criativo, CRM, vendas precisam conseguir aplicar).
- **Seção 8** — O que evitar (sinais de veto ou retrabalho).

## Quando usar

**Depois de:** DEOC redigido ou gerado; idealmente com matriz de tradução (`traducao-deoc-para-assets`) ou seção 5.9 preenchida no próprio DEOC.

**Antes de:** aprovação formal de plano de mídia, briefings em massa, produção de LP ou ativação de campanhas.

**Entradas típicas:** artefato(s) do DEOC, benchmark, diagnóstico GTM, materiais de apoio, restrições legais/compliance, e opcionalmente saída do `build_deoc.py --audit` da skill `dossie-estrategico-oferta-comunicacao`.

## Decisões possíveis

| Resultado | Significado |
|-----------|-------------|
| **Pronto** | Critérios N2 atendidos; sem bloqueio material; tradução executável; riscos aceitos e registrados. |
| **Condicional** | N2 quase completo; gaps menores com owner e prazo; execução pode começar só em escopo limitado (ex.: um canal ou teste). |
| **Não pronto** | Falha em critério N2 material, anti-padrão grave da seção 8 ou impossibilidade de executar sem inventar promessa. |

## Workflow

1. Abra o DEOC e a matriz 5.9 (ou artefato de tradução equivalente).
2. Preencha o checklist em `templates/checklist-qa-deoc.md` **ou** edite `templates/checklist-qa-deoc.json`.
3. Marque cada item N2 como **ok**, **gap** ou **n.a.** (não aplicável — com justificativa).
4. Avalie itens N3 se o cliente exige rigor ampliado ou já está em escala.
5. Verifique **anti-padrões** da seção 8: qualquer ocorrência documentada vira gap ou risco.
6. Responda ao bloco **implementação** (seção 3): times conseguiriam executar só com esse documento?
7. Rode o script para consolidar contagem e gerar relatório Markdown.
8. Registre **decisão**, **revisor** e **próximos passos**; liste claims pendentes que ainda entram em copy pública.

## Outputs

- Checklist preenchido (Markdown ou JSON).
- Relatório de QA (opcionalmente gerado por script).
- Lista priorizada de gaps e riscos bloqueantes.
- Registro explícito de claims pendentes e condicionantes de “pronto”.

## Artefatos

- `reference.md` — critérios copiados/adaptados do canônico e guia de severidade.
- `templates/checklist-qa-deoc.md`
- `templates/checklist-qa-deoc.json`
- `scripts/evaluate_qa_deoc.py`

## Scripts

```bash
python3 scripts/evaluate_qa_deoc.py templates/checklist-qa-deoc.json --audit
python3 scripts/evaluate_qa_deoc.py templates/checklist-qa-deoc.json --md ./relatorio-qa-deoc.md
```

O `--audit` lista itens N2 incompletos ou em gap e sugere um resultado **pronto / condicional / não pronto / incompleto** com base apenas nos campos obrigatórios. A decisão final permanece humana.

## Observação

Esta skill **não** substitui revisão jurídica ou compliance; integra risco de comunicação e aderência ao playbook 13.

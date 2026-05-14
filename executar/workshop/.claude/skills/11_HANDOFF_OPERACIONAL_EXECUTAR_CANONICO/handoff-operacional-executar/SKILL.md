---
name: handoff-operacional-executar
description: Compila plano de ROI, transcrição da call de vendas e transcrição da Growth Class em pacote de handoff operacional EXECUTAR auditável para o squad iniciar planning sem recoletar contexto. Use no pós-fechamento, antes do planning EXECUTAR ou quando faltarem insumos validados entre venda, boas-vindas e operação.
---

# Handoff Operacional Executar

## Quando Usar

Use quando o cliente entrou no fluxo EXECUTAR e os insumos de venda e boas-vindas precisam virar documento único validado.

Situações típicas:

- fechamento concluído e falta pacote para o time;
- planning não pode depender de memória do closer ou prints soltos;
- precisa registrar promessas, premissas, riscos e pendências;
- handoff precisa atingir critério N2 antes de avançar.

## Inputs Obrigatórios

- plano de ROI;
- transcrição da call de vendas;
- transcrição da Growth Class ou call de boas-vindas;
- contrato ou escopo quando disponível;
- links dos insumos.

## Workflow

1. Confirme que os três insumos existem e estão acessíveis.
2. Extraia do plano de ROI: produto, escopo, investimento, metas, premissas, horizonte, restrições, divergências de cenários.
3. Extraia da call de vendas: dores, objetivo da compra, objeções, promessas, urgências, stakeholders, critérios de sucesso, riscos, dúvidas abertas.
4. Extraia da Growth Class: entendimento do cliente, expectativas, desvios vs. venda, maturidade, tom, risco churn M0, pendências, próximos passos acordados.
5. Preencha o documento canônico com resumo, escopo, sínteses, promessas, premissas críticas, riscos, divergências, pendências, stakeholders, próximos passos, dono e status de completude.
6. Rode análise de desvio (eixo a eixo) com `analise-desvios-venda-boas-vindas` ou incorpore a matriz no pacote.
7. Validação humana: coordenador/account revisa, corrige e decide antes do squad consumir como fonte da verdade.

## Output Esperado

- documento único de handoff operacional;
- links para insumos;
- sínteses objetivas;
- riscos e pendências explícitos;
- próximos passos claros;
- status de completude e decisão do responsável.

Use `templates/handoff-executar.md` para preenchimento manual.
Use `templates/handoff-executar.json` com o script para gerar Markdown a partir de dados estruturados.

## Script Utilitário

```bash
python3 scripts/build_handoff_executar.py templates/handoff-executar.json --md /tmp/handoff-executar.md
```

## Definition Of Done

- Plano de ROI, transcrição de vendas e Growth Class estão referenciados.
- Síntese operacional e análise de desvio constam no pacote ou estão anexadas.
- Riscos e pendências estão registrados.
- Responsável interno registra revisão e próximo passo para o EXECUTAR.

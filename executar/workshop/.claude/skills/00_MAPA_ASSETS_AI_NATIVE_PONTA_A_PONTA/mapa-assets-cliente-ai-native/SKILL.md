---
name: mapa-assets-cliente-ai-native
description: Mapeia os assets necessários para operar um cliente no Marketing OS ponta a ponta, identificando gaps, donos, dependências e critérios N2/N3. Use no onboarding, planning, auditoria de conta, decisão de pacote v1 ou quando o usuário pedir mapa de assets, inventário operacional, maturidade AI-native ou checklist ponta a ponta.
---

# Mapa Assets Cliente AI-Native

## Quando Usar

Use quando precisar:

- transformar contexto bruto de cliente em mapa operacional de assets;
- decidir quais assets entram no primeiro ciclo;
- auditar se uma conta tem base N2/N3 suficiente;
- encontrar gaps antes de plano de mídia, DEOC, LP, criativos, setup ou go-live;
- preparar handoff entre estratégia, execução, tracking, vendas e aprendizado.

Nao use para:

- escrever cada asset especialista em profundidade;
- substituir playbooks de mídia, tracking, CRM, LP, criativo ou benchmark;
- criar uma lista genérica sem dono, evidência e decisão.

## Inputs Necessários

Colete o máximo possível:

- handoff operacional, contrato/escopo e promessas comerciais;
- discovery, transcrições, diagnóstico, benchmark e DEOC, quando existirem;
- inventário de assets atuais do cliente;
- stack de mídia, LP, CRM, tracking, planilhas e dashboards;
- status de campanhas, criativos, leads, feedback comercial e aprendizados;
- responsáveis internos, aprovadores do cliente, riscos e restrições.

Se algum input crítico faltar, registre como gap. Nao invente maturidade.

## Workflow

1. Defina o objetivo do mapa: onboarding, auditoria, pacote v1, go-live ou próximo ciclo.
2. Classifique o cliente nas 14 etapas da jornada ponta a ponta descritas em `reference.md`.
3. Para cada etapa, liste assets obrigatórios, existentes, faltantes, evidências e donos.
4. Separe gaps por tipo: estratégia, mídia, criativo, conversão, tracking, CRM, vendas, dados, governança ou aprendizado.
5. Decida o pacote v1: o que precisa existir agora, o que fica fora do ciclo e o que depende do cliente.
6. Atribua prioridade e severidade:
   - `bloqueador`: impede execução, tracking ou handoff confiável;
   - `alto`: gera risco relevante de falso aprendizado ou retrabalho;
   - `medio`: reduz qualidade, mas nao bloqueia o ciclo;
   - `baixo`: melhoria futura.
7. Gere plano de ação com dono, dependencia, prazo e definition of done.
8. Valide N2/N3 usando os criterios em `reference.md`.

## Output Esperado

Produza:

- mapa executivo da situacao atual;
- matriz de assets por etapa;
- lista de gaps priorizados;
- pacote v1 recomendado;
- assets fora do ciclo e motivo;
- riscos de falso N2/N3;
- proximas acoes com dono, evidencia esperada e prazo.

Use `templates/mapa-assets-cliente.md` para documentos em Markdown.
Use `templates/matriz-assets.json` como schema de entrada para automacoes.

## Script Utilitário

Para converter uma matriz JSON de assets para CSV e Markdown:

```bash
python scripts/build_asset_matrix.py templates/matriz-assets.json --csv /tmp/matriz-assets.csv --md /tmp/matriz-assets.md
```

O script espera um JSON com uma lista `assets`. Cada item deve conter pelo menos `etapa`, `asset`, `status`, `prioridade`, `dono` e `dod`.

## Definition Of Done

- Todas as etapas relevantes foram avaliadas.
- Cada asset critico tem status, evidencia, dono e proxima acao.
- Gaps bloqueadores estao separados de melhorias.
- O pacote v1 esta claro e nao tenta resolver tudo de uma vez.
- N2/N3 foram avaliados com evidencia, nao por percepcao.
- O output consegue alimentar playbooks especialistas sem recoletar contexto.

## Armadilhas

- Tratar lista de documentos como processo implementado.
- Marcar N2 sem evidencia de execucao.
- Ignorar CRM, SLA, tracking e planilha backup.
- Criar um pacote v1 grande demais para a capacidade real.
- Nao separar dependencia do cliente de pendencia interna.
- Chamar qualquer aprendizado de N3 sem decisao registrada e rebrief.

## Referencias

- Playbook canonico: `assets/canonicos/00_MAPA_ASSETS_AI_NATIVE_PONTA_A_PONTA.md`
- Detalhamento: `reference.md`
- Template: `templates/mapa-assets-cliente.md`
- Schema: `templates/matriz-assets.json`

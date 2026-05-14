# Referência — Conversão no site Meta Ads (playbook 15)

Fonte primária: **`15_SETUP_CAMPANHAS_META_ADS_CANONICO.md`**. Complemento: **`assets/legacy/merge/skills/10-2-meta-conversao.md`**. Não substitui documentação oficial da Meta nem checklist jurídico da LP.

## 1. Definição no canônico (Seção 9 — Venda/conversão)

**Objetivo:** compra, agendamento, oportunidade ou venda — em síntese, conversão rastreada **no site** quando o ambiente está maduro.

**Usar quando:**

- **evento de conversão está validado;**
- **há volume suficiente;**
- **ciclo e valor justificam otimização mais profunda.**

Se o volume ainda não existe, o canônico não proíbe campanha de performance, mas a **Seção 5** orienta: evento de otimização o mais profundo **possível sem matar volume**; pode-se começar mais raso e qualificar na planilha de growth.

## 2. Eventos e pixel (Seção 5)

Mínimos citados para contexto lead/e-commerce:

- `PageView`; `ViewContent` ou equivalente; `Lead` no envio do formulário;
- `MQL` custom quando houver integração; `SQL`/offline quando houver volume e CRM.

**Regra central:** otimizar o **mais profundo possível sem matar volume**; sem volume, não forçar evento profundo só pela teoria.

Para **conversão no site**, o evento escolhido na interface da campanha deve ser o que o funil define como “sucesso rastreável” **e** que a Meta recebe de forma consistente (pixel e/ou CAPI).

## 3. Checklist de conta (Seção 4) — recortes relevantes

- pixel instalado; CAPI quando possível; eventos testados; priorização quando aplicável;
- **UTMs preservadas na LP/formulário**;
- planilha backup / CRM — especialmente quando a conversão é **lead via formulário na LP** (alinha ao N2 geral: lead teste).

## 4. Públicos (Seções 6–8)

Exemplos úteis para conversão:

- **Mornos:** visitantes do **site 30D**; visitantes **LP/site** em estruturas de remarketing do canônico;
- **Quentes:** visitantes LP 7D/14D, leads capturados, comportamentos de intenção conforme o caso.

**Seção 16:** remarketing **sem** exclusão de convertidos é citada como problema — aplicar exclusões coerentes ao evento de conversão.

## 5. Go-live global (Seção 13) + específico

Itens sempre válidos: IDs campanha/conjunto/anúncio; público/temperatura; exclusões; **pixel/eventos testados**; **UTMs**; backup; CRM quando houver lead; criativos; matriz; orçamento; hipótese; changelog.

Para este subtipo, o checklist em `meta-conversao-site.md` cobre **evento validado**, URLs, CAPI e prova de disparo.

## 6. N2 (Seção 14)

Inclui explicitamente:

- **subtipos lead nativo, conversão e engajamento têm checklist específico quando usados.**

Ou seja: além do `estrutura-campanha-meta`, este pacote deve estar preenchido quando a campanha for otimizada para conversão no domínio.

## 7. O que evitar (Seção 16) — conversão

- **pixel/evento não testado;**
- **conversão no site sem evento validado.**

## 8. Síntese legada (10-2)

Passos legados que permanecem válidos:

1. Fixar evento de conversão (funil) e validar tracking mínimo.
2. Separar prospecting vs remarketing quando aplicável.
3. Matriz de testes (público vs criativo vs oferta).
4. Ad sets, exclusões, criativos por hipótese.
5. Registrar decisões / change log.

**Riscos legados:** otimizar para **evento errado**; misturar temperaturas; matriz fraca.

## 9. Formato dos campos no `meta-conversao-site.json`

- `evento_otimizacao.eventos_suporte`: lista de strings (PageView, ViewContent, etc.) que alimentam diagnóstico, não necessariamente todos otimizados.
- `teste_p2p`: booleans para disparo testado na Meta; `backup_ok` / `crm_ok` **obrigatórios na auditoria** quando `tipo_conversao` indica captura de lead na LP (`lead_form_lp` ou similar).
- `publicos.linhas`: objetos com `audience`, `temperatura`, `uso`.
- `campanhas_resumo.linhas`: objetos com `campaign_id`, `objetivo_meta`, `notas`.

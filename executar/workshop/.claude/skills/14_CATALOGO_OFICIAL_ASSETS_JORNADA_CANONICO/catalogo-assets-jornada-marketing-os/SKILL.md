---
name: catalogo-assets-jornada-marketing-os
description: Consulta o catálogo oficial de assets da jornada Marketing OS (playbook 14), classifica obrigatoriedade (obrigatório, condicional, suporte, evidência, legado) e, com contexto opcional, lista assets aplicáveis ao cohort/canal/maturidade. Use para decisão de pacote, auditoria N2, evitar bullshit documental e alinhar o time ao que é ou não asset canônico.
---

# Catálogo de assets — jornada Marketing OS

## Fonte canônica

Playbook **`14_CATALOGO_OFICIAL_ASSETS_JORNADA_CANONICO.md`**. Este catálogo é **transversal**: não é etapa operacional da jornada, é **referência normativa** para o que pode ou deve existir.

## Duas formas de consulta

1. **Humana:** `reference.md` reproduz o catálogo completo (tabelas e regras de leitura, seções 13 e 14 do canônico).
2. **Máquina / filtro:** `data/catalogo_assets.json` replica os itens com `gatilhos_condicionais` opcionais; `scripts/listar_assets_aplicaveis.py` combina o JSON com `templates/contexto-catalogo.json` para gerar uma lista aplicável ao seu contexto.

## Regra de leitura (Seção 1)

Nem todo asset é obrigatório para toda conta. Classificações:

| Classificação | Definição |
| --- | --- |
| Obrigatório | Sem ele, a jornada não roda ou não pode ser auditada como N2. |
| Condicional | Necessário só para certos cohorts, canais, mercados, tickets ou maturidades. |
| Suporte | Ajuda operação, governança ou aprendizado; não é entrega principal. |
| Evidência | Prova de que uma etapa foi executada ou que um componente existe. |
| Legado | Exemplo anterior incorporado por um asset mais completo. |

Detalhes e critério “anti-bullshit” (Seção 14) em `reference.md`.

## Inputs

- Contexto do cliente: jornada, canal (Meta / Google / Search), maturidade, cohort, etapa atual.
- Catálogo oficial (este repositório: JSON + referência).

## Outputs

- Lista de assets **aplicáveis agora** vs **revisar manualmente** vs **suporte / evidência / legado**.
- Justificativa por item quando o script marcar exclusão por gatilho.

## Workflow

1. Leia a **Regra de leitura** e o **critério Seção 14** em `reference.md`.
2. (Opcional) Preencha `templates/contexto-catalogo.json` com booleans de canal, vendas, integração, etc.
3. Rode `python3 scripts/listar_assets_aplicaveis.py --context templates/contexto-catalogo.json --md ./aplicacao.md`.
4. Para auditoria N2 / pacote v1, use também `decisor-pacote-assets-v1` e `controle-duplicacao-assets` quando existirem no repositório.
5. Registre no dossiê do cliente: quais linhas do catálogo foram **explicitamente postergadas** e por quê.

## Templates

- `templates/aplicacao-catalogo.md` — registro manual da aplicação do catálogo a um cliente.
- `templates/contexto-catalogo.json` — parâmetros para o script.

## Scripts

```bash
python3 scripts/listar_assets_aplicaveis.py --resumo
python3 scripts/listar_assets_aplicaveis.py --context templates/contexto-catalogo.json --audit
python3 scripts/listar_assets_aplicaveis.py --context templates/contexto-catalogo.json --md ./saida.md
```

## Observação (Seção 13 do canônico)

O playbook lista alguns itens como “fora da jornada principal” por serem meta-regras de leitura; na prática **notação N1/N2/N3** e **este catálogo** continuam **obrigatórios como transversais**. A interpretação está detalhada em `reference.md`.

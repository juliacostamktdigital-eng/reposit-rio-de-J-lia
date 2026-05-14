# Referência — Display / remarketing Google (playbook 16 + legado 13)

## 1. Texto canônico — Estrutura Display (§9)

Usar Display quando o **Plano de Mídia** definir **função clara**: alcance qualificado, remarketing, contextual, sustentação de awareness ou recuperação de intenção. A estrutura deve declarar:

- **targeting**
- **exclusões anti-ICP**
- **placements/apps bloqueados**
- **brand safety**
- **frequência**
- **janela de remarketing**
- **criativos por formato**
- **métrica de leitura**

Display **não** deve entrar como **sobra de verba** nem como “barato para aparecer”. **Sem** exclusões, frequência e brand safety, gera **falso aprendizado** e tráfego de baixa qualidade.

## 2. Setup mínimo leadgen (§13)

Uma campanha remarketing/**Display**/YouTube **apenas se houver público e objetivo**. Com maturidade: remarketing com **audiência e mensagem própria**.

## 3. Go-live (§14)

Quando Display aplicável:

- **Display** com **placements/apps, frequência, exclusões e brand safety** conferidos.

## 4. Nomenclatura (§10)

Mesmo padrão geral:

**Campanha:** `{campaign_id} | {tipo_campanha} | {objetivo} | {movimento} | {slug}`  

Exemplo conceitual: `... | display | ... | remarketing | ...`

**Grupo:** `{adgroup_id} | {intencao} | {temperatura} | {tipo} | {slug}`

**Criativo:** `{creative_id} | {formato} | {hook} | {persona} | {slug} | {versao}`

## 5. Orçamento (§12)

Evitar fragmentação excessiva; aprendizado mínimo; mudanças graduais; não ajustar budget/lance todo dia sem evidência (§17 eco).

## 6. Legado 13 — síntese

**Quando usar:** plano define Display (awareness ou remarketing); reforço para público aquecido. **Não usar:** “tráfego barato” sem função.

**Crítico:** função no funil; exclusões e brand safety; audiência coerente com ICP; frequência.

**DoD legado:** função documentada; targeting + exclusões; criativos linkados; guardrails placements/frequência.

## 7. JSON — chaves principais

- `funcao_funil.tipo` e `descricao`
- `compromisso_nao_sobra_verba`: confirmação explícita
- `exclusoes`: listas `anti_icp`, `placements_apps_bloqueados`
- `brand_safety`, `frequencia`, `janela_remarketing`, `metrica_leitura`
- `campanhas[].grupos[]`: targeting, criativos
- `pre_go_live_display`

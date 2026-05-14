# Referência — Iteração por performance ↔ playbook 20

## Vereditos (`veredito`)

| Valor | Significado |
|--------|-------------|
| `manter` | Receita validada; próximo ciclo pode reutilizar com pouca mudança |
| `alterar` | Mecânismo ou template precisa ajuste; hipótese refinada |
| `descontinuar` | Tipo ou variante não paga o custo de produção/leitura no contexto atual |
| `pausar` | Esperar mais dados, sazonalidade ou dependência (LP/oferta) |
| `expandir` | Escalar para mais peças/canais; duplicar racionalmente |
| `inconclusivo` | Dados insuficientes ou conflitantes — não mudar banco sem nova rodada |

## Métricas por contexto

Escolha **uma primária** por linha, alinhada ao objetivo do tipo (funil + canal):

- Topo frio: CTR, thumbstop, hook rate, CPC, qualidade do clique
- Meio: taxa de lead, CPL, qualidade MQL (se rastreado)
- Quente: ROAS, CAC assist, conversão remarketing

Registre **período** e **volume** (impressões/cliques/conversões) para evitar decisão em amostra mínima.

## Encadeamento com o banco

1. Esta skill produz `change_log_sugerido[]`.
2. **Copiar** para `banco-tipos-criativos` → `change_log_catalogo` (mesmos campos: `data`, `autor`, `tipo_id`, `resumo`, `motivo`).
3. Editar o objeto do tipo em `tipos[]`: `hipotese`, `componentes_obrigatorios`, `variacoes`, `dod_checklist`, `versao_tipo`.
4. Rodar `build_banco_tipos.py --audit` até DoD.

## KPI § Gerenciado (lembrete)

- **Impacto por tipo:** usar `analise[].metrica_primaria` + valor observado vs esperado.
- **Taxa iteração tipo→mudança→resultado:** contar ciclos com `change_log_sugerido` aplicado e resultado na próxima rodada (governança fora do JSON, se necessário).

## Relação com outras skills

| Skill | Papel |
|-------|--------|
| `selecao-pack-criativo-ciclo` | Pack que originou o teste (link em `meta.link_pack`) |
| `briefing-criativo-video-first` | Novos briefs após `alterar` / `expandir` |
| `roteiro-criativo-performance` | Novas variações estruturadas |

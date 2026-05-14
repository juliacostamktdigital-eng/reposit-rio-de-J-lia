# Referência — Banco de tipos ↔ playbook 20

## Taxonomia mínima (passo 1 do canônico)

Eixo **formato × temperatura × objetivo** (cada tipo deve ser classificável nos três).

| Eixo | Valores usuais |
|------|----------------|
| Formato | estático, vídeo, carrossel, outro |
| Temperatura | frio, morno, quente (remarketing) |
| Objetivo no funil | ex.: clique qualificado, lead, reativação, fechamento — alinhar ao plano de mídia e DEOC |

## Componentes críticos (iteração)

- Objetivo por tipo claro (**função no funil**).
- Template **enxuto** (componentes obrigatórios), não receita vaga.
- Variações que testam **hipótese**, não só estética.
- Referências de benchmark **vinculadas** (evidência).
- **DoD** consistente (conformidade + qualidade).

## Gerenciado — o que registrar

| Exigência canônica | Onde no JSON |
|--------------------|--------------|
| Change log por tipo | `change_log_catalogo[]` com `tipo_id` |
| Link / id de campanhas onde foi usado | `tipos[].campanhas_onde_usado[]` |
| Revisão mensal por canal/segmento | `meta.cadencia_revisao` + prática de governança |
| KPI (tipos usados; impacto; iteração tipo→mudança→resultado) | planilha/BI externa; aqui manter rastreio mínimo em `campanhas_onde_usado` e notas em `meta` |

## IDs de tipo

Sugestão: `TIPO-001`, `TIPO-002`, … estáveis no tempo; mudanças substantivas incrementam `versao_tipo` e geram entrada no change log.

## Relação com outras skills

| Skill | Uso do banco |
|--------|----------------|
| `selecao-pack-criativo-ciclo` | Seleciona subconjunto e quantidades a partir deste catálogo |
| `briefing-criativo-video-first` | Brief puxa `tipo_id` / hipótese / template |
| `roteiro-criativo-performance` | Estrutura de cena alinhada ao template do tipo |
| `iteracao-tipo-criativo-por-performance` | Atualiza tipos e change log com base em performance |

## Arquivo canônico de template (repo)

`assets/canonicos/templates/tipo-criativo.md` — mantido alinhado à cópia em `.claude/skills/20_BANCO_TIPOS_CRIATIVOS_CANONICO/banco-tipos-criativos/templates/tipo-criativo.md`.

## `change_log_catalogo[]` (JSON)

Cada entrada (mudança no catálogo ou em um tipo):

| Campo | Uso |
|-------|-----|
| `data` | ISO |
| `autor` | Quem registrou |
| `tipo_id` | `TIPO-xxx` afetado (ou `CATALOGO` para baseline taxonomia) |
| `resumo` | O que mudou |
| `motivo` | Por quê (obrigatório no playbook) |

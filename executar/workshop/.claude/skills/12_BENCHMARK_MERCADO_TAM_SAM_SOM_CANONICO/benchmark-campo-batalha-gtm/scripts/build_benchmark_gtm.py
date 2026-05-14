#!/usr/bin/env python3
"""Gera Markdown do benchmark campo de batalha GTM a partir de JSON.

Compatível com JSONs antigos (campos extras opcionais). Renderiza:
- cabeçalho com versionamento (versao/data/proxima_revisao)
- sumário executivo
- contexto + contexto macro
- voz do cliente (capítulo dedicado)
- amostra de concorrentes
- tabela de concorrentes com 4 dimensões + brand awareness
- matriz de atributos cruzada
- padrões dominantes
- ruído de mercado
- conflitos internos da marca
- ativos de PR sub-aproveitados
- oportunidades ranqueadas (medalhas / prioridade)
- riscos com janela temporal de mitigação
- baseline vs. diferenciação
- implicações em sub-headers por consumer skill
- fontes agrupadas por categoria
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def esc(text: Any) -> str:
    return str(text or "").replace("|", "\\|").replace("\n", " ")


def section(title: str, level: int = 2) -> list[str]:
    return [f"{'#' * level} {title}", ""]


def kv_line(label: str, value: Any) -> str:
    return f"- **{label}:** {value}" if value not in (None, "", []) else f"- **{label}:** —"


def render_sumario_executivo(items: list[Any]) -> list[str]:
    if not items:
        return []
    lines = section("Sumário Executivo")
    for item in items:
        lines.append(f"- {item}")
    lines.append("")
    return lines


def render_contexto(ctx: dict[str, Any]) -> list[str]:
    lines = section("Contexto")
    lines += [
        kv_line("Cliente", ctx.get("cliente", "")),
        kv_line("Segmento", ctx.get("segmento", "")),
        kv_line("Geografia", ctx.get("geografia", "")),
        kv_line("Produto foco", ctx.get("produto_foco", "")),
        kv_line("Ticket", ctx.get("ticket", "")),
        kv_line("ICP", ctx.get("icp", "")),
        kv_line("Canais", ", ".join(ctx.get("canais") or [])),
        kv_line("Objetivo", ctx.get("objetivo_aquisicao", "")),
    ]
    multi = ctx.get("geografia_multi_unidade") or []
    if multi:
        lines += ["", "**Multi-unidade:**", ""]
        for u in multi:
            if isinstance(u, dict):
                lines.append(f"- {u.get('unidade', '')} — papel: {u.get('papel', '')}")
    lines.append("")
    return lines


def render_contexto_macro(macro: dict[str, Any]) -> list[str]:
    if not macro:
        return []
    lines = section("Contexto Macro")
    lines.append("Visão de setor mínima para situar o leitor (TAM/SAM/SOM detalhado fica em `sizing-mercado-tam-sam-som`):")
    lines.append("")
    lines += [
        kv_line("Tamanho do mercado", macro.get("tamanho_mercado", "")),
        kv_line("Crescimento / CAGR", macro.get("crescimento", "")),
    ]
    tend = macro.get("tendencias") or []
    if tend:
        lines += ["- **Tendências relevantes:**"]
        for t in tend:
            lines.append(f"  - {t}")
    lines += [
        kv_line("Sazonalidade", macro.get("sazonalidade", "")),
        kv_line("Regulatório / tecnológico", macro.get("regulatorio_tecnologico", "")),
    ]
    if macro.get("fonte_macro"):
        lines.append(kv_line("Fonte macro", macro.get("fonte_macro")))
    lines.append("")
    return lines


def render_voz_cliente(voz: dict[str, Any]) -> list[str]:
    if not voz:
        return []
    lines = section("Voz Do Cliente")
    lines.append("Capítulo dedicado — extraído de reviews, fóruns, comentários, transcrições, redes sociais.")
    lines.append("")

    termos_pub = voz.get("termos_publico_alvo") or []
    if termos_pub:
        lines.append("**Termos do público-alvo:**")
        lines.append("")
        for t in termos_pub:
            lines.append(f"- {t}")
        lines.append("")

    termos_marca = voz.get("termos_marca_ressoam") or []
    if termos_marca:
        lines.append("**Termos da marca que ressoam:**")
        lines.append("")
        for t in termos_marca:
            lines.append(f"- {t}")
        lines.append("")

    criticas = voz.get("criticas_concorrentes") or []
    if criticas:
        lines.append("**Críticas reputacionais dos concorrentes:**")
        lines.append("")
        lines.append("| Concorrente | Crítica recorrente | Ângulo estratégico |")
        lines.append("| --- | --- | --- |")
        for c in criticas:
            if isinstance(c, dict):
                # aceitar tanto 'angulo_estrategico' quanto 'ângulo_estrategico'
                ang = c.get("angulo_estrategico") or c.get("ângulo_estrategico", "")
                lines.append(f"| {esc(c.get('concorrente'))} | {esc(c.get('critica'))} | {esc(ang)} |")
        lines.append("")

    dores = voz.get("dores_nao_resolvidas") or []
    if dores:
        lines.append("**Dores não resolvidas (categoria mental vazia):**")
        lines.append("")
        for d in dores:
            lines.append(f"- {d}")
        lines.append("")

    criterios = voz.get("criterios_compra_ponderados") or []
    if criterios:
        lines.append("**Critérios de compra ponderados:**")
        lines.append("")
        lines.append("| Critério | Peso percebido |")
        lines.append("| --- | --- |")
        for c in criterios:
            if isinstance(c, dict):
                lines.append(f"| {esc(c.get('criterio'))} | {esc(c.get('peso_percebido'))} |")
        lines.append("")

    if voz.get("fontes_voz"):
        lines.append(kv_line("Fontes desta seção", voz.get("fontes_voz")))
        lines.append("")

    return lines


def render_concorrentes(concs: list[dict[str, Any]]) -> list[str]:
    lines = section("Concorrentes")
    lines.append("| Player | Tipo | Anuncia | Brand awareness | Formato | Mensagem | Forte | Fraco | Gap | Ameaça | Evidência |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for c in concs:
        if not isinstance(c, dict):
            continue
        # retro-compat: 'fortes'/'fracos' (string) → 'forte'/'fraco'
        forte = c.get("forte") or c.get("fortes", "")
        fraco = c.get("fraco") or c.get("fracos", "")
        lines.append(
            "| {player} | {tipo} | {anuncia} | {ba} | {fmt} | {msg} | {forte} | {fraco} | {gap} | {ameaca} | {ev} |".format(
                player=esc(c.get("player")),
                tipo=esc(c.get("tipo")),
                anuncia="sim" if c.get("anuncia") else "nao",
                ba=esc(c.get("brand_awareness", "—")),
                fmt=esc(c.get("formato")),
                msg=esc(c.get("mensagem")),
                forte=esc(forte),
                fraco=esc(fraco),
                gap=esc(c.get("gap")),
                ameaca=esc(c.get("ameaca", "—")),
                ev=esc(c.get("evidencia")),
            )
        )
    lines.append("")
    return lines


def render_matriz_atributos(matriz: dict[str, Any]) -> list[str]:
    if not matriz:
        return []
    atributos = matriz.get("atributos") or []
    linhas_data = matriz.get("linhas") or []
    if not atributos or not linhas_data:
        return []
    lines = section("Matriz De Atributos")
    lines.append("Leitura visual cruzada — sim/não/— por atributo. Mapa 2x2 estratégico fica em `posicionamento-competitivo-beachhead`.")
    lines.append("")
    header = "| Player | " + " | ".join(esc(a) for a in atributos) + " |"
    sep = "| --- | " + " | ".join("---" for _ in atributos) + " |"
    lines.append(header)
    lines.append(sep)
    for row in linhas_data:
        if not isinstance(row, dict):
            continue
        valores = row.get("valores") or []
        # garantir alinhamento mesmo que faltem células
        cells = [esc(v) for v in valores] + ["—"] * (len(atributos) - len(valores))
        lines.append(f"| {esc(row.get('player'))} | " + " | ".join(cells[: len(atributos)]) + " |")
    if matriz.get("nota"):
        lines += ["", f"_{matriz.get('nota')}_"]
    lines.append("")
    return lines


def render_bullets(title: str, items: list[Any]) -> list[str]:
    if not items:
        return []
    lines = section(title)
    for item in items:
        lines.append(f"- {item}")
    lines.append("")
    return lines


def render_conflitos(conflitos: list[dict[str, Any]]) -> list[str]:
    if not conflitos:
        return []
    lines = section("Conflitos Internos Da Marca")
    lines.append("Onde claim declarado colide com autocrítica do dono ou com percepção do mercado. Resolver antes da S2.")
    lines.append("")
    lines.append("| Conflito | Evidência | Resolução proposta |")
    lines.append("| --- | --- | --- |")
    for c in conflitos:
        if isinstance(c, dict):
            lines.append(f"| {esc(c.get('conflito'))} | {esc(c.get('evidencia'))} | {esc(c.get('resolucao_proposta'))} |")
    lines.append("")
    return lines


def render_ativos_pr(ativos: list[dict[str, Any]]) -> list[str]:
    if not ativos:
        return []
    lines = section("Ativos De PR Sub-aproveitados")
    lines.append("Cobertura espontânea, prêmios e depoimentos já existentes que não estão sendo aproveitados. Justifica budget orgânico/PR.")
    lines.append("")
    lines.append("| Ativo | Evidência | Uso recomendado |")
    lines.append("| --- | --- | --- |")
    for a in ativos:
        if isinstance(a, dict):
            lines.append(f"| {esc(a.get('ativo'))} | {esc(a.get('evidencia'))} | {esc(a.get('uso_recomendado'))} |")
    lines.append("")
    return lines


_PRIO_ORDER = {"p1": 0, "p2": 1, "p3": 2}
_PRIO_MEDAL = {"p1": "🥇", "p2": "🥈", "p3": "🥉"}


def _prio_key(o: dict[str, Any]) -> int:
    p = str(o.get("prioridade", "")).strip().lower()
    return _PRIO_ORDER.get(p, 99)


def render_oportunidades(ops: list[dict[str, Any]]) -> list[str]:
    if not ops:
        return []
    lines = section("Oportunidades (ranqueadas)")
    sorted_ops = sorted(ops, key=_prio_key)
    for o in sorted_ops:
        if not isinstance(o, dict):
            continue
        prio = str(o.get("prioridade", "")).strip().lower()
        medal = _PRIO_MEDAL.get(prio, "•")
        prio_label = f" ({prio.upper()})" if prio else ""
        nome = o.get("nome", "")
        impl = o.get("implicacao", "")
        ev = o.get("evidencia", "")
        lines.append(f"- {medal}{prio_label} **{nome}** — {impl} _(evidência: {ev})_")
    lines.append("")
    return lines


_QUANDO_ORDER = {"s1": 0, "s2": 1, "contínuo": 2, "continuo": 2}


def render_riscos(risks: list[dict[str, Any]]) -> list[str]:
    if not risks:
        return []
    lines = section("Riscos E Armadilhas (janela temporal)")
    sorted_risks = sorted(risks, key=lambda r: _QUANDO_ORDER.get(str(r.get("quando", "")).lower(), 99))
    lines.append("| Risco | Mitigação | Quando |")
    lines.append("| --- | --- | --- |")
    for r in sorted_risks:
        if isinstance(r, dict):
            lines.append(f"| {esc(r.get('nome'))} | {esc(r.get('mitigacao'))} | {esc(r.get('quando', '—'))} |")
    lines.append("")
    return lines


def render_implicacoes(impl: dict[str, Any]) -> list[str]:
    if not impl:
        return []
    lines = section("Implicações (por consumer skill)")
    headers = [
        ("DEOC / Comunicação", "deoc", "`dossie-estrategico-oferta-comunicacao`"),
        ("Plano De Mídia", "midia", "`plano-de-midia` + setup das skills de Meta/Google"),
        ("LP / Ponto De Conversão", "lp", "`lp-ponto-de-conversao`"),
        ("Criativos", "criativos", "`briefing-criativo-video-first`"),
        ("Próximos Testes", "proximos_testes", "skill irmã `benchmark-para-backlog-growth`"),
    ]
    for title, key, consumer in headers:
        body = impl.get(key)
        if not body:
            continue
        lines += section(title, level=3)
        lines.append(f"_Consumer: {consumer}_")
        lines.append("")
        lines.append(str(body))
        lines.append("")
    return lines


def render_fontes(fontes: list[dict[str, Any]]) -> list[str]:
    if not fontes:
        return []
    lines = section("Fontes")
    lines.append("Lista agrupada por categoria — qualquer afirmação no documento pode ser auditada por aqui.")
    lines.append("")

    categorias: dict[str, list[dict[str, Any]]] = {}
    for f in fontes:
        if not isinstance(f, dict):
            continue
        cat = str(f.get("categoria", "outros")).lower()
        categorias.setdefault(cat, []).append(f)

    rotulos = {
        "macro": "Macro de mercado",
        "concorrente": "Concorrentes",
        "voz_cliente": "Voz do cliente",
        "outros": "Outros",
    }
    ordem = ["macro", "concorrente", "voz_cliente", "outros"]
    for cat in ordem:
        items = categorias.get(cat)
        if not items:
            continue
        lines += section(rotulos.get(cat, cat.title()), level=3)
        for f in items:
            url = f.get("url", "")
            titulo = f.get("titulo", url or "(sem título)")
            data = f.get("data", "")
            data_str = f" — {data}" if data else ""
            if url:
                lines.append(f"- [{titulo}]({url}){data_str}")
            else:
                lines.append(f"- {titulo}{data_str}")
        lines.append("")
    # categorias fora da ordem padrão
    extras = [c for c in categorias.keys() if c not in ordem]
    for cat in extras:
        lines += section(cat.title(), level=3)
        for f in categorias[cat]:
            url = f.get("url", "")
            titulo = f.get("titulo", url or "(sem título)")
            data = f.get("data", "")
            data_str = f" — {data}" if data else ""
            if url:
                lines.append(f"- [{titulo}]({url}){data_str}")
            else:
                lines.append(f"- {titulo}{data_str}")
        lines.append("")
    return lines


def build_md(data: dict[str, Any]) -> str:
    versao = data.get("versao", "")
    dt = data.get("data", "")
    rev = data.get("proxima_revisao", "")

    lines: list[str] = ["# Benchmark Campo De Batalha GTM", ""]

    if versao or dt or rev:
        if versao:
            lines.append(f"**Versão:** {versao}  ")
        if dt:
            lines.append(f"**Data:** {dt}  ")
        if rev:
            lines.append(f"**Próxima revisão:** {rev}")
        lines.append("")

    lines += render_sumario_executivo(data.get("sumario_executivo") or [])

    lines += section("Pergunta De Negócio")
    lines.append(str(data.get("pergunta_negocio", "")))
    lines.append("")

    ctx = data.get("contexto") or {}
    if isinstance(ctx, dict):
        lines += render_contexto(ctx)

    lines += render_contexto_macro(data.get("contexto_macro") or {})
    lines += render_voz_cliente(data.get("voz_do_cliente") or {})
    lines += render_concorrentes(data.get("concorrentes") or [])
    lines += render_matriz_atributos(data.get("matriz_atributos") or {})
    lines += render_bullets("Padrões Dominantes", data.get("padroes") or [])
    lines += render_bullets("Ruído De Mercado", data.get("ruidos") or [])
    lines += render_conflitos(data.get("conflitos_internos_marca") or [])
    lines += render_ativos_pr(data.get("ativos_pr") or [])
    lines += render_oportunidades(data.get("oportunidades") or [])
    lines += render_riscos(data.get("riscos") or [])

    lines += section("Baseline Vs. Diferenciação")
    lines.append(f"- **Baseline:** {data.get('baseline', '')}")
    lines.append(f"- **Diferenciação:** {data.get('diferenciacao', '')}")
    lines.append("")

    impl = data.get("implicacoes") or {}
    if isinstance(impl, dict):
        lines += render_implicacoes(impl)

    lines += render_fontes(data.get("fontes") or [])

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build benchmark GTM markdown from JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path, required=True)
    args = parser.parse_args()

    data = load(args.input_json)
    md = build_md(data)
    args.md_path.parent.mkdir(parents=True, exist_ok=True)
    args.md_path.write_text(md, encoding="utf-8")


if __name__ == "__main__":
    main()

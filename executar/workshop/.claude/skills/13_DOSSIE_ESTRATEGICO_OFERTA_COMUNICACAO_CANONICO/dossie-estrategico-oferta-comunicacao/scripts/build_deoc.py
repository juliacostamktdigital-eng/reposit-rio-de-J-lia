#!/usr/bin/env python3
"""Constroi Markdown DEOC a partir de JSON e audita lacunas N2."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def block(text: str) -> str:
    s = (text or "").strip()
    return s if s else "_[preencher]_"


def bullets(items: list[Any]) -> str:
    if not items:
        return "- _[preencher]_"
    lines = []
    for it in items:
        lines.append(f"- {it}".strip())
    return "\n".join(lines)


def table_claims(
    rows: list[dict[str, str]],
    keys: tuple[str, ...],
    titles: tuple[str, ...] | None = None,
) -> str:
    heads = titles if titles else keys
    if not rows:
        return "| " + " | ".join(heads) + " |\n|" + "|".join(["---"] * len(heads)) + "|"
    header = "| " + " | ".join(heads) + " |"
    sep = "|" + "|".join(["---"] * len(heads)) + "|"
    body = []
    for r in rows:
        body.append("| " + " | ".join(block(r.get(k, "")) for k in keys) + " |")
    return "\n".join([header, sep, *body])


def cb(done: Any) -> str:
    return "[x]" if bool(done) else "[ ]"


def table_problemas(rows: list[dict[str, str]]) -> str:
    cols = ("Problema", "Custo atual", "Risco percebido", "Fricção na troca")
    if not rows:
        return "| " + " | ".join(cols) + " |\n|" + "|".join(["---"] * 4) + "|\n" + "| | | | |"
    header = "| # | " + " | ".join(cols) + " |"
    sep = "|---|" + "|".join(["---"] * 5) + "|"
    body = []
    for i, r in enumerate(rows, 1):
        cells = [str(i)] + [block(r.get(k, "")) for k in ("problema", "custo_atual", "risco_percebido", "friccao_troca")]
        body.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, sep, *body])


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    rs = d.get("resumo_estrategico") or {}
    dunf = d.get("esqueleto_dunford") or {}
    puv3 = d.get("puv_3_versoes") or {}
    pir = d.get("piramide_emocional") or []
    exe = d.get("output_executivo") or {}
    om = d.get("oferta_mecanismo") or {}
    icps = d.get("icp_personas") or []
    probs = d.get("problemas") or []
    alts = d.get("alternativas") or []
    pv = d.get("proposta_valor_expandida") or {}
    nar = d.get("narrativa") or {}
    cl = d.get("claims") or {}
    te = d.get("traducao_execucao") or {}
    pm = te.get("plano_midia") or {}
    bc = te.get("briefing_criativo") or {}
    lp = te.get("lp_site") or {}
    mc = te.get("materiais_comerciais") or {}
    tr = te.get("tracking") or {}
    log = d.get("changelog_n3") or []

    parts: list[str] = []
    parts.append("# Dossiê Estratégico de Oferta e Comunicação (DEOC)\n")
    parts.append(
        "| Campo | Valor |\n"
        "|-------|-------|\n"
        f"| Cliente / produto | {block(m.get('cliente_ou_produto', ''))} |\n"
        f"| Versão | {block(m.get('versao', ''))} |\n"
        f"| Data | {block(m.get('data', ''))} |\n"
        f"| Responsável | {block(m.get('responsavel', ''))} |\n"
        f"| Status | {block(m.get('status', ''))} |\n"
    )

    # ---- 0. Executivo (capa C-level) ----
    if any(v for v in (exe.values() if isinstance(exe, dict) else [])):
        parts.append("## 0. Executivo (capa C-level)\n")
        parts.append(f"**PUV — completa:** {block(exe.get('puv_completa'))}\n")
        parts.append(f"**PUV — headline 5s:** {block(exe.get('puv_headline_5s'))}\n")
        parts.append(f"**PUV — one-liner 2s:** {block(exe.get('puv_one_liner_2s'))}\n")
        parts.append(f"**POV:** {block(exe.get('pov'))}\n")
        parts.append("**Differentiated Value:**\n" + bullets(list(exe.get("differentiated_value_bullets") or [])) + "\n")
        parts.append(f"**Perfect World:** {block(exe.get('perfect_world_paragrafo'))}\n")
        parts.append(f"**Prova-âncora:** {block(exe.get('prova_ancora'))}\n")

    # ---- 0.1 Esqueleto Dunford ----
    if dunf:
        parts.append("## 0.1 Esqueleto Dunford de 5 elementos\n")
        parts.append(f"**POV / Insight nomeado:** {block(dunf.get('pov_insight_nomeado'))}\n")
        approaches = [x for x in (dunf.get("alternatives_approaches") or []) if isinstance(x, dict)]
        parts.append("**Alternatives (approaches, inclui status quo):**\n")
        if approaches:
            parts.append("| Approach | Descrição |\n|---|---|")
            for ap in approaches:
                parts.append(f"| {block(ap.get('approach'))} | {block(ap.get('descricao'))} |")
            parts.append("")
        else:
            parts.append("_[preencher pelo menos status quo / não fazer nada]_\n")
        parts.append(f"**Perfect World (Raskin):** {block(dunf.get('perfect_world'))}\n")
        parts.append("**Differentiated Value:**\n" + bullets(list(dunf.get("differentiated_value") or [])) + "\n")
        proofs = [x for x in (dunf.get("proof_por_differentiator") or []) if isinstance(x, dict)]
        parts.append("**Proof por differentiator (sem prova → claim pendente):**\n")
        if proofs:
            parts.append("| Differentiator | Prova | Status |\n|---|---|---|")
            for pr in proofs:
                parts.append(
                    f"| {block(pr.get('differentiator'))} | {block(pr.get('prova'))} | {block(pr.get('status', 'permitido'))} |"
                )
            parts.append("")
        else:
            parts.append("_[preencher cada differentiator com prova ou marcar pendente]_\n")

    # ---- 0.2 PUV em 3 versões ----
    if puv3:
        parts.append("## 0.2 PUV em 3 versões\n")
        parts.append("| Versão | Texto |\n|---|---|")
        parts.append(f"| Completa | {block(puv3.get('completa'))} |")
        parts.append(f"| Headline 5s | {block(puv3.get('headline_5s'))} |")
        parts.append(f"| One-liner 2s | {block(puv3.get('one_liner_2s'))} |\n")
        teste = puv3.get("teste_qualidade_dunford") or {}
        parts.append("**Teste de qualidade Dunford:**\n")
        parts.append(f"- {cb(teste.get('compreensivel_em_5s'))} Compreensível em <5s pra alguém do ICP\n")
        parts.append(f"- {cb(teste.get('menciona_icp'))} Menciona ICP\n")
        parts.append(f"- {cb(teste.get('promete_resultado_concreto'))} Promete resultado concreto\n")
        parts.append(f"- {cb(teste.get('memoravel'))} Memorável\n")

    # ---- 0.3 Pirâmide emocional ----
    if pir:
        parts.append("## 0.3 Pirâmide emocional (Feature → Vantagem → Funcional → Emocional → Prova)\n")
        parts.append("| Feature | Vantagem | Funcional | Emocional | Prova | Status |\n|---|---|---|---|---|---|")
        for row in pir:
            if not isinstance(row, dict):
                continue
            parts.append(
                f"| {block(row.get('feature'))} | {block(row.get('vantagem'))} | "
                f"{block(row.get('beneficio_funcional'))} | {block(row.get('beneficio_emocional'))} | "
                f"{block(row.get('prova'))} | {block(row.get('status', 'permitido'))} |"
            )
        parts.append("")

    parts.append("## 1. Resumo estratégico\n")
    parts.append(f"**Oferta e categoria:** {block(rs.get('oferta_e_categoria'))}\n")
    parts.append(f"**Público e anti-público:** {block(rs.get('publico_e_anti_publico'))}\n")
    parts.append(f"**Problema central:** {block(rs.get('problema_central'))}\n")
    parts.append(f"**Proposta de valor (uma frase):** {block(rs.get('proposta_valor_fracao'))}\n")
    parts.append(f"**Diferenciais defendíveis:** {block(rs.get('diferenciais_defensaveis'))}\n")
    parts.append(f"**CTA macro:** {block(rs.get('cta_macro'))}\n")
    parts.append(f"**Observações para execução:** {block(rs.get('observacoes_execucao'))}\n")

    parts.append("## 2. Oferta e mecanismo\n")
    parts.append(f"**Descrição:** {block(om.get('descricao_oferta'))}\n")
    parts.append(f"**Brainer:** {block(om.get('brainer'))}\n")
    parts.append("**Inclui:**\n" + bullets(list(om.get("inclui") or [])) + "\n")
    parts.append("**Exclui / limites:**\n" + bullets(list(om.get("exclui_limites") or [])) + "\n")
    parts.append(f"**Anti-ICP:** {block(om.get('anti_icp_quando_nao_recomendar'))}\n")
    parts.append(f"**Modelo de preço (lógica):** {block(om.get('modelo_preco_logica'))}\n")
    parts.append(f"**Prova mínima (claims fortes):** {block(om.get('prova_minima_claims_fortes'))}\n")

    parts.append("## 3. ICP e personas\n")
    for i, p in enumerate(icps, 1):
        parts.append(f"### Persona {i}: {block(p.get('nome_ou_rotulo', f'ICP {i}'))}\n")
        parts.append(f"- **Contexto de uso:** {block(p.get('contexto_uso'))}\n")
        parts.append("- **Jobs to be done:**\n" + bullets(list(p.get("jobs_to_be_done") or [])) + "\n")
        parts.append("- **Gatilhos de mudança:**\n" + bullets(list(p.get("gatilhos_mudanca") or [])) + "\n")
        parts.append("- **Objeções típicas:**\n" + bullets(list(p.get("objecoes_tipicas") or [])) + "\n")
        parts.append("- **Critérios de escolha:**\n" + bullets(list(p.get("criterios_escolha") or [])) + "\n")
    if not icps:
        parts.append("_[preencher pelo menos um ICP]_\n")

    parts.append("## 4. Problemas, custos e fricção\n")
    parts.append(table_problemas([dict(x) for x in probs if isinstance(x, dict)]) + "\n")

    parts.append("## 5. Alternativas competitivas\n")
    for alt in alts:
        if not isinstance(alt, dict):
            continue
        parts.append(f"### {block(alt.get('nome', 'Alternativa'))}\n")
        parts.append(f"- **Promessa típica:** {block(alt.get('promessa_tipica'))}\n")
        parts.append(f"- **Como vendem:** {block(alt.get('como_vendem'))}\n")
        parts.append(f"- **Fraquezas para o nosso ICP:** {block(alt.get('fraquezas_para_nosso_icp'))}\n")
        parts.append(f"- **Quando ainda ganha:** {block(alt.get('quando_ainda_ganha'))}\n")
    if not alts:
        parts.append("_[preencher alternativas incluindo status quo]_\n")

    parts.append("## 6. Proposta de valor (expandido)\n")
    parts.append(f"**Frase principal:** {block(pv.get('frase_principal'))}\n")
    parts.append(f"**Parágrafo de suporte:** {block(pv.get('paragrafo_suporte'))}\n")

    parts.append("## 7. Inimigo, tese e narrativa\n")
    parts.append(f"**Inimigo:** {block(nar.get('inimigo'))}\n")
    parts.append(f"**Crença atual:** {block(nar.get('crenca_atual'))}\n")
    parts.append(f"**Nova crença:** {block(nar.get('nova_crenca'))}\n")
    parts.append(f"**Hero / guide / plano:** {block(nar.get('hero_guide_plano'))}\n")
    parts.append("**Pontos de virada:**\n" + bullets(list(nar.get("pontos_virada") or [])) + "\n")

    perm = [dict(x) for x in (cl.get("permitidos") or []) if isinstance(x, dict)]
    prob = [dict(x) for x in (cl.get("proibidos") or []) if isinstance(x, dict)]
    pend = [dict(x) for x in (cl.get("pendentes") or []) if isinstance(x, dict)]

    parts.append("## 8. Claims\n")
    parts.append("### Permitidos\n")
    parts.append(
        table_claims(perm, ("claim", "ancora_prova"), ("Claim", "Âncora de prova")) + "\n"
    )
    parts.append("### Proibidos\n")
    parts.append(table_claims(prob, ("claim", "motivo"), ("Claim", "Motivo")) + "\n")
    parts.append("### Pendentes\n")
    parts.append(
        table_claims(
            pend,
            ("claim", "tipo_evidencia", "owner_sugerido"),
            ("Claim", "Tipo de evidência", "Owner sugerido"),
        )
        + "\n"
    )

    parts.append("## 9. Tradução para execução\n")
    parts.append("### Plano de mídia\n")
    parts.append(f"- **Segmentos:** {block(pm.get('segmentos'))}\n")
    parts.append(f"- **Mensagens:** {block(pm.get('mensagens'))}\n")
    parts.append(f"- **Formatos:** {block(pm.get('formatos'))}\n")
    parts.append(f"- **Provas:** {block(pm.get('provas'))}\n")
    parts.append("### Briefing criativo\n")
    parts.append(f"- **Tom:** {block(bc.get('tom'))}\n")
    parts.append(f"- **Tabus:** {block(bc.get('tabus'))}\n")
    parts.append(f"- **Hero / inimigo / CTA:** {block(bc.get('hero_inimigo_cta'))}\n")
    parts.append("### LP / site\n")
    parts.append(f"- **H1:** {block(lp.get('h1'))}\n")
    parts.append(f"- **Promessa secundária:** {block(lp.get('promessa_secundaria'))}\n")
    parts.append(f"- **Provas:** {block(lp.get('provas'))}\n")
    parts.append(f"- **FAQ / objeções:** {block(lp.get('faq_objecoes'))}\n")
    parts.append("### Materiais comerciais\n")
    parts.append(f"- **Pitch one-liner:** {block(mc.get('pitch_one_liner'))}\n")
    parts.append(f"- **Objeções e respostas:** {block(mc.get('objecoes_respostas'))}\n")
    parts.append(f"- **Pricing story:** {block(mc.get('pricing_story'))}\n")
    parts.append("### Tracking\n")
    parts.append(f"- **Eventos / conversões:** {block(tr.get('eventos_conversoes'))}\n")
    parts.append(f"- **Atribuição / North Star:** {block(tr.get('atribuicao_north_star'))}\n")

    parts.append("## Changelog (N3)\n")
    if log:
        parts.append("| Versão | Data | Mudança |\n|--------|------|--------|")
        for row in log:
            if not isinstance(row, dict):
                continue
            parts.append(
                f"| {block(row.get('versao'))} | {block(row.get('data'))} | {block(row.get('mudanca'))} |"
            )
        parts.append("")
    else:
        parts.append("| Versão | Data | Mudança |\n|--------|------|--------|\n| | | |\n")

    return "\n".join(parts)


def nonempty_str(v: Any) -> bool:
    return isinstance(v, str) and bool(v.strip())


def audit_n2(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    rs = d.get("resumo_estrategico") or {}
    keys_rs = (
        "oferta_e_categoria",
        "publico_e_anti_publico",
        "problema_central",
        "proposta_valor_fracao",
        "diferenciais_defensaveis",
        "cta_macro",
    )
    for k in keys_rs:
        if not nonempty_str(rs.get(k)):
            issues.append(f"resumo_estrategico.{k} vazio")

    om = d.get("oferta_mecanismo") or {}
    for k in ("descricao_oferta", "brainer", "anti_icp_quando_nao_recomendar", "prova_minima_claims_fortes"):
        if not nonempty_str(om.get(k)):
            issues.append(f"oferta_mecanismo.{k} vazio")

    inc = om.get("inclui") or []
    exc = om.get("exclui_limites") or []
    if not (isinstance(inc, list) and inc) and not (isinstance(exc, list) and exc):
        issues.append("oferta: preencher inclui ou exclui/limites (escopo)")

    icps = d.get("icp_personas") or []
    if not isinstance(icps, list) or not icps:
        issues.append("icp_personas: pelo menos uma entrada")

    probs = d.get("problemas") or []
    if not isinstance(probs, list) or not probs:
        issues.append("problemas: pelo menos uma linha")

    alts = d.get("alternativas") or []
    if not isinstance(alts, list) or not alts:
        issues.append("alternativas: pelo menos status quo")

    pv = d.get("proposta_valor_expandida") or {}
    if not nonempty_str(pv.get("frase_principal")):
        issues.append("proposta_valor_expandida.frase_principal vazio")
    if not nonempty_str(pv.get("paragrafo_suporte")):
        issues.append("proposta_valor_expandida.paragrafo_suporte vazio")

    nar = d.get("narrativa") or {}
    for k in ("inimigo", "crenca_atual", "nova_crenca", "hero_guide_plano"):
        if not nonempty_str(nar.get(k)):
            issues.append(f"narrativa.{k} vazio")
    pv_list = nar.get("pontos_virada") or []
    if not (isinstance(pv_list, list) and pv_list):
        issues.append("narrativa.pontos_virada: pelo menos um item")

    cl = d.get("claims") or {}
    perm = cl.get("permitidos") or []
    prob = cl.get("proibidos") or []
    if not (isinstance(perm, list) and perm and any(nonempty_str(x.get("claim")) for x in perm if isinstance(x, dict))):
        issues.append("claims.permitidos: pelo menos um claim com texto")
    if not (isinstance(prob, list) and prob and any(nonempty_str(x.get("claim")) for x in prob if isinstance(x, dict))):
        issues.append("claims.proibidos: pelo menos um claim com texto (ou declarar lista vazia explicita no doc)")

    te = d.get("traducao_execucao") or {}
    for section, keys in (
        ("plano_midia", ("segmentos", "mensagens", "formatos", "provas")),
        ("briefing_criativo", ("tom", "tabus", "hero_inimigo_cta")),
        ("lp_site", ("h1", "promessa_secundaria", "provas", "faq_objecoes")),
        ("materiais_comerciais", ("pitch_one_liner", "objecoes_respostas", "pricing_story")),
        ("tracking", ("eventos_conversoes", "atribuicao_north_star")),
    ):
        sub = te.get(section) or {}
        for kk in keys:
            parent = f"traducao_execucao.{section}"
            if not nonempty_str(sub.get(kk)):
                issues.append(f"{parent}.{kk} vazio")

    # ---- Warnings: novos conceitos (Dunford / PUV 3v / Pirâmide / Executivo) ----
    # Backwards-compat: se o bloco inteiro estiver ausente, é WARNING (não issue duro).
    dunf = d.get("esqueleto_dunford")
    if dunf is None:
        issues.append("WARNING: esqueleto_dunford ausente (POV/Alternatives/Perfect World/Diff Value/Proof)")
    elif isinstance(dunf, dict):
        if not nonempty_str(dunf.get("pov_insight_nomeado")):
            issues.append("WARNING: esqueleto_dunford.pov_insight_nomeado vazio")
        if not nonempty_str(dunf.get("perfect_world")):
            issues.append("WARNING: esqueleto_dunford.perfect_world vazio")
        approaches = dunf.get("alternatives_approaches") or []
        if not (isinstance(approaches, list) and approaches):
            issues.append("WARNING: esqueleto_dunford.alternatives_approaches: pelo menos status quo")
        diffs = dunf.get("differentiated_value") or []
        if not (isinstance(diffs, list) and diffs):
            issues.append("WARNING: esqueleto_dunford.differentiated_value vazio (3-5 bullets)")
        proofs = dunf.get("proof_por_differentiator") or []
        if not (isinstance(proofs, list) and proofs):
            issues.append("WARNING: esqueleto_dunford.proof_por_differentiator: cada diff precisa de prova ou pendente")
        else:
            for i, pr in enumerate(proofs):
                if not isinstance(pr, dict):
                    continue
                if nonempty_str(pr.get("differentiator")) and not nonempty_str(pr.get("prova")):
                    if (pr.get("status") or "").strip().lower() != "pendente":
                        issues.append(
                            f"WARNING: esqueleto_dunford.proof_por_differentiator[{i}] sem prova e status != pendente (vira claim pendente)"
                        )

    puv3 = d.get("puv_3_versoes")
    if puv3 is None:
        issues.append("WARNING: puv_3_versoes ausente (completa/headline_5s/one_liner_2s)")
    elif isinstance(puv3, dict):
        for k in ("completa", "headline_5s", "one_liner_2s"):
            if not nonempty_str(puv3.get(k)):
                issues.append(f"WARNING: puv_3_versoes.{k} vazio")
        teste = puv3.get("teste_qualidade_dunford") or {}
        if isinstance(teste, dict):
            failed = [k for k in ("compreensivel_em_5s", "menciona_icp", "promete_resultado_concreto", "memoravel") if not teste.get(k)]
            if failed:
                issues.append(
                    f"WARNING: puv_3_versoes.teste_qualidade_dunford falhou em: {', '.join(failed)}"
                )

    pir = d.get("piramide_emocional")
    if pir is None:
        issues.append("WARNING: piramide_emocional ausente (Feature -> Vantagem -> Funcional -> Emocional -> Prova)")
    elif isinstance(pir, list):
        if not pir:
            issues.append("WARNING: piramide_emocional vazia (pelo menos uma feature)")
        for i, row in enumerate(pir):
            if not isinstance(row, dict):
                continue
            if nonempty_str(row.get("beneficio_emocional")) and not nonempty_str(row.get("prova")):
                if (row.get("status") or "").strip().lower() != "pendente":
                    issues.append(
                        f"WARNING: piramide_emocional[{i}] benefício emocional sem prova e status != pendente"
                    )

    exe = d.get("output_executivo")
    if exe is None:
        issues.append("WARNING: output_executivo ausente (capa C-level 2-3p)")
    elif isinstance(exe, dict):
        for k in ("puv_completa", "puv_headline_5s", "puv_one_liner_2s", "pov", "perfect_world_paragrafo", "prova_ancora"):
            if not nonempty_str(exe.get(k)):
                issues.append(f"WARNING: output_executivo.{k} vazio")

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Build DEOC Markdown from JSON; optional N2 audit.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path, help="Write rendered Markdown to this path")
    parser.add_argument("--audit", action="store_true", help="Print N2 gap list to stdout")
    args = parser.parse_args()

    data = load(args.input_json)
    if args.md_path:
        args.md_path.write_text(render_md(data), encoding="utf-8")
    if args.audit:
        issues = audit_n2(data)
        if issues:
            print("Lacunas N2 (playbook 13):")
            for line in issues:
                print(f"  - {line}")
        else:
            print("Auditoria N2: nenhuma lacuna obrigatoria detectada neste schema.")
    if not args.md_path and not args.audit:
        print(render_md(data), end="")


if __name__ == "__main__":
    main()

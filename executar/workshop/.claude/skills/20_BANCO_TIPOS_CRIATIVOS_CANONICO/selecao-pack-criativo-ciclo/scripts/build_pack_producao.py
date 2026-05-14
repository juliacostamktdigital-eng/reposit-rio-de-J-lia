#!/usr/bin/env python3
"""Pack de produção criativa (playbook 20 passo 5) — Markdown, auditoria e resumo."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def block(t: Any) -> str:
    s = "" if t is None else str(t).strip()
    return s if s else "_[preencher]_"


def filled(v: Any) -> bool:
    if v is None:
        return False
    if isinstance(v, str):
        t = v.strip()
        if not t or t == "[Nome]" or t.lower() == "yyyy-mm-dd":
            return False
        return True
    if isinstance(v, (list, dict)):
        return len(v) > 0
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, float)):
        return v > 0 if isinstance(v, int) else bool(v)
    return bool(v)


def _selecao_started(row: dict[str, Any]) -> bool:
    if not isinstance(row, dict):
        return False
    q = row.get("quantidade_pecas")
    try:
        qn = int(q) if q is not None else 0
    except (TypeError, ValueError):
        qn = 0
    if qn > 0:
        return True
    keys = ("tipo_id", "nome_tipo_ref", "hipotese_teste", "criterio_leitura")
    return any(filled(row.get(k)) for k in keys)


def default_document() -> dict[str, Any]:
    return {
        "meta": {
            "projeto": "[Nome]",
            "pack_id": "PACK-YYYY-MM-DD",
            "data": "YYYY-MM-DD",
            "ciclo": "primeira_leva",
            "responsavel": "",
            "link_banco_tipos": "",
            "link_plano_midia": "",
            "link_deoc": "",
            "link_benchmark": "",
            "canais": [],
            "etapa_funil_primaria": "",
            "orcamento_volume_notas": "",
            "capacidade_producao_notas": "",
            "justificativa_sem_banco": "",
        },
        "plano_contexto": {
            "cliente_segmento": "",
            "campanha_hipotese_macro": "",
            "tipos_campanha_detalhe": "",
            "oferta_brainer": "",
            "icp_anti_icp": "",
            "persona": "",
        },
        "contexto": {
            "aprendizados_ciclo_anterior": "",
            "restricoes_marca_claims": "",
        },
        "selecao": [
            {
                "prioridade": 1,
                "tipo_id": "",
                "nome_tipo_ref": "",
                "formato": "",
                "temperatura": "",
                "funcao_funil": "",
                "quantidade_pecas": 0,
                "variacoes_planejadas": ["A", "B", "C"],
                "mensagem_angulo": "",
                "prova_usada": "",
                "cta": "",
                "destino": "",
                "hipotese_teste": "",
                "criterio_leitura": "",
                "canais_prioritarios": [],
                "notas_dependencias": "",
            }
        ],
        "ambiente_conversao": {
            "lp_notas": "",
            "formulario_whatsapp_agenda": "",
            "tracking_minimo": "",
        },
        "guardrails": {
            "nucleo_nao_pode_mudar": "",
            "pode_variar": "",
        },
        "checklist_conformidade": {
            "oferta_alinhada": "",
            "copy_sem_promessas_impossiveis": "",
            "cta_destino_coerente": "",
            "evidencia_decisao_registrada": "",
        },
        "totais": {"total_pecas_planejadas": 0, "ajuste_capacidade": ""},
        "riscos_gaps": "",
    }


def _destino_sugere_site(rows: list[Any]) -> bool:
    hints = ("lp", "landing", "site", "página", "pagina", "url", "http")
    for r in rows:
        if not isinstance(r, dict):
            continue
        d = str(r.get("destino", "")).lower()
        if any(h in d for h in hints):
            return True
    return False


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not filled(m.get("projeto")):
        issues.append("meta.projeto")
    if not filled(m.get("responsavel")):
        issues.append("meta.responsavel")
    if not filled(m.get("data")):
        issues.append("meta.data")
    if not filled(m.get("pack_id")):
        issues.append("meta.pack_id")

    if not filled(m.get("link_banco_tipos")):
        if not filled(m.get("justificativa_sem_banco")):
            issues.append(
                "meta.link_banco_tipos ou meta.justificativa_sem_banco (exceção documentada)"
            )
        else:
            issues.append(
                "(aviso) pack sem link ao banco — fechar catálogo conforme playbook 20"
            )

    rows = d.get("selecao") or []
    if not isinstance(rows, list):
        issues.append("selecao deve ser lista")
        return issues

    started = [r for r in rows if isinstance(r, dict) and _selecao_started(r)]
    if not started:
        issues.append("selecao: nenhuma linha iniciada (tipo_id, qtd ou hipótese)")

    for i, r in enumerate(rows, 1):
        if not isinstance(r, dict) or not _selecao_started(r):
            continue
        pr = f"selecao[{i}]"
        if not filled(r.get("tipo_id")):
            issues.append(f"{pr}.tipo_id")
        try:
            q = int(r.get("quantidade_pecas") or 0)
        except (TypeError, ValueError):
            q = 0
        if q < 1:
            issues.append(f"{pr}.quantidade_pecas (mínimo 1)")
        if not filled(r.get("hipotese_teste")):
            issues.append(f"{pr}.hipotese_teste")
        if not filled(r.get("criterio_leitura")):
            issues.append(f"{pr}.criterio_leitura")

    if not filled(m.get("canais")):
        issues.append("(aviso) meta.canais vazio — documentar canais do ciclo")

    soma = 0
    for r in rows:
        if isinstance(r, dict):
            try:
                soma += int(r.get("quantidade_pecas") or 0)
            except (TypeError, ValueError):
                pass
    tt = d.get("totais") or {}
    try:
        tot = int(tt.get("total_pecas_planejadas") or 0)
    except (TypeError, ValueError):
        tot = 0
    if started and tot > 0 and soma != tot:
        issues.append(
            f"(aviso) soma quantidade_pecas ({soma}) ≠ totais.total_pecas_planejadas ({tot})"
        )

    if started:
        pc = d.get("plano_contexto") or {}
        if not filled(pc.get("oferta_brainer")):
            issues.append("(aviso) plano_contexto.oferta_brainer vazio")
        gr = d.get("guardrails") or {}
        if not filled(gr.get("nucleo_nao_pode_mudar")) and not filled(
            gr.get("pode_variar")
        ):
            issues.append(
                "(aviso) guardrails vazio — definir núcleo fixo vs variável (template canônico)"
            )
        if _destino_sugere_site(rows):
            ac = d.get("ambiente_conversao") or {}
            if not filled(ac.get("lp_notas")):
                issues.append(
                    "(aviso) destino sugere site/LP — preencher ambiente_conversao.lp_notas"
                )
            if not filled(ac.get("tracking_minimo")):
                issues.append(
                    "(aviso) preencher ambiente_conversao.tracking_minimo para leitura íntegra"
                )
        ck = d.get("checklist_conformidade") or {}
        for key, label in (
            ("oferta_alinhada", "oferta_alinhada"),
            ("copy_sem_promessas_impossiveis", "copy_sem_promessas_impossiveis"),
            ("cta_destino_coerente", "cta_destino_coerente"),
            ("evidencia_decisao_registrada", "evidencia_decisao_registrada"),
        ):
            if not filled(ck.get(key)):
                issues.append(
                    f"(aviso) checklist_conformidade.{label} vazio (marcar ok ou N/A com nota)"
                )

    return issues


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    pc = d.get("plano_contexto") or {}
    ctx = d.get("contexto") or {}
    tt = d.get("totais") or {}
    ac = d.get("ambiente_conversao") or {}
    gr = d.get("guardrails") or {}
    ck = d.get("checklist_conformidade") or {}
    parts: list[str] = []
    parts.append("# Pack de produção criativa (playbook 20 + template canônico)\n\n")
    ch = m.get("canais") or []
    ch_s = ", ".join(str(x) for x in ch) if ch else "_[preencher]_"
    parts.append(
        f"- **Projeto:** {block(m.get('projeto'))}\n"
        f"- **Pack ID:** {block(m.get('pack_id'))}\n"
        f"- **Data:** {block(m.get('data'))}\n"
        f"- **Ciclo:** {block(m.get('ciclo'))}\n"
        f"- **Responsável:** {block(m.get('responsavel'))}\n"
        f"- **Banco tipos:** {block(m.get('link_banco_tipos'))}\n"
        f"- **Plano mídia:** {block(m.get('link_plano_midia'))}\n"
        f"- **DEOC:** {block(m.get('link_deoc'))}\n"
        f"- **Benchmark:** {block(m.get('link_benchmark'))}\n"
        f"- **Canais:** {ch_s}\n"
        f"- **Etapa funil:** {block(m.get('etapa_funil_primaria'))}\n"
        f"- **Orçamento/volume:** {block(m.get('orcamento_volume_notas'))}\n"
        f"- **Capacidade produção:** {block(m.get('capacidade_producao_notas'))}\n"
    )
    jb = m.get("justificativa_sem_banco") or ""
    if str(jb).strip():
        parts.append(f"- **Justificativa sem banco:** {jb.strip()}\n")
    parts.append(
        "\n## Plano — contexto\n\n"
        f"- **Cliente/segmento:** {block(pc.get('cliente_segmento'))}\n"
        f"- **Hipótese macro:** {block(pc.get('campanha_hipotese_macro'))}\n"
        f"- **Tipos campanha:** {block(pc.get('tipos_campanha_detalhe'))}\n"
        f"- **Oferta (brainer):** {block(pc.get('oferta_brainer'))}\n"
        f"- **ICP / anti-ICP:** {block(pc.get('icp_anti_icp'))}\n"
        f"- **Persona:** {block(pc.get('persona'))}\n"
    )
    parts.append(
        "\n## Ciclo / restrições\n\n"
        f"**Aprendizados:** {block(ctx.get('aprendizados_ciclo_anterior'))}\n\n"
        f"**Restrições/claims:** {block(ctx.get('restricoes_marca_claims'))}\n"
    )
    parts.append("\n## Seleção — criativos\n\n")
    parts.append(
        "| Prio | tipo_id | Nome | Fmt | Tmp | Funil | Qtd | Var | Ângulo | Prova | CTA | Dest | Hipótese | Leitura |\n"
        "|---|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|\n"
    )
    for r in d.get("selecao") or []:
        if not isinstance(r, dict):
            continue
        vp = r.get("variacoes_planejadas") or []
        vp_s = "/".join(str(x) for x in vp) if vp else "_[preencher]_"
        parts.append(
            f"| {block(r.get('prioridade'))} | {block(r.get('tipo_id'))} | "
            f"{block(r.get('nome_tipo_ref'))} | {block(r.get('formato'))} | "
            f"{block(r.get('temperatura'))} | {block(r.get('funcao_funil'))} | "
            f"{block(r.get('quantidade_pecas'))} | {vp_s} | "
            f"{block(r.get('mensagem_angulo'))} | {block(r.get('prova_usada'))} | "
            f"{block(r.get('cta'))} | {block(r.get('destino'))} | "
            f"{block(r.get('hipotese_teste'))} | {block(r.get('criterio_leitura'))} |\n"
        )
    parts.append(
        "\n## Ambiente de conversão\n\n"
        f"- **LP:** {block(ac.get('lp_notas'))}\n"
        f"- **Formulário / WhatsApp / agenda:** {block(ac.get('formulario_whatsapp_agenda'))}\n"
        f"- **Tracking mínimo:** {block(ac.get('tracking_minimo'))}\n"
    )
    parts.append(
        "\n## Guardrails\n\n"
        f"- **Núcleo (não mudar):** {block(gr.get('nucleo_nao_pode_mudar'))}\n"
        f"- **Pode variar:** {block(gr.get('pode_variar'))}\n"
    )
    parts.append(
        "\n## Checklist conformidade\n\n"
        f"- Oferta alinhada: {block(ck.get('oferta_alinhada'))}\n"
        f"- Copy sem promessas impossíveis: {block(ck.get('copy_sem_promessas_impossiveis'))}\n"
        f"- CTA ↔ destino: {block(ck.get('cta_destino_coerente'))}\n"
        f"- Evidência de decisão: {block(ck.get('evidencia_decisao_registrada'))}\n"
    )
    parts.append(
        "\n## Totais\n\n"
        f"- **Total peças (campo):** {block(tt.get('total_pecas_planejadas'))}\n"
        f"- **Ajuste capacidade:** {block(tt.get('ajuste_capacidade'))}\n\n"
        f"**Riscos/gaps:** {block(d.get('riscos_gaps'))}\n"
    )
    return "".join(parts)


def summary(d: dict[str, Any]) -> None:
    rows = d.get("selecao") if isinstance(d.get("selecao"), list) else []
    n = sum(1 for r in rows if isinstance(r, dict) and _selecao_started(r))
    soma = 0
    for r in rows:
        if isinstance(r, dict):
            try:
                soma += int(r.get("quantidade_pecas") or 0)
            except (TypeError, ValueError):
                pass
    print(f"Linhas de seleção iniciadas: {n}")
    print(f"Soma quantidade_pecas: {soma}")


def main() -> None:
    p = argparse.ArgumentParser(description="Pack produção criativa (playbook 20)")
    p.add_argument("input_json", nargs="?", type=Path)
    p.add_argument("--md", dest="md_path", type=Path)
    p.add_argument("--audit", action="store_true")
    p.add_argument("--summary", action="store_true")
    p.add_argument("--write-default", dest="out_json", type=Path)
    args = p.parse_args()

    if args.out_json:
        args.out_json.write_text(
            json.dumps(default_document(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"Escrito: {args.out_json}")
        return

    if not args.input_json:
        p.error("informe input_json ou --write-default")

    doc = load(args.input_json)
    if args.audit:
        xs = audit(doc)
        print("Lacunas (pack de produção):")
        for x in xs:
            print(f"  - {x}")
        return
    if args.summary:
        summary(doc)
        return
    if args.md_path:
        args.md_path.write_text(render_md(doc), encoding="utf-8")
        print(f"Escrito: {args.md_path}")
    else:
        print(render_md(doc), end="")


if __name__ == "__main__":
    main()

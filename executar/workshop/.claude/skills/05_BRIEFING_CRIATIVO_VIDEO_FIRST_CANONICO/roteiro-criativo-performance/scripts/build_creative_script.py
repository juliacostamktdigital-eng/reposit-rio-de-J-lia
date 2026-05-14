#!/usr/bin/env python3
"""Build performance creative scripts from structured JSON."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "creative_id",
    "brief_id",
    "cliente",
    "campanha",
    "formato",
    "duracao",
    "canal",
    "placement",
    "persona",
    "etapa",
    "hipotese",
    "variavel_testada",
    "hook",
    "dor",
    "mecanismo",
    "prova",
    "cta",
    "utm_content",
    "legenda",
    "direcao_visual",
    "qa_flags",
]

SCENE_FIELDS = [
    "creative_id",
    "tipo",
    "ordem",
    "tempo_ou_slide",
    "funcao",
    "texto_ou_fala",
    "texto_tela",
    "prova_exemplo",
    "visual",
    "cta_transicao",
    "atributo",
    "edicao",
]


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def qa_flags(item: dict[str, Any]) -> str:
    flags: list[str] = []
    required = ["creative_id", "brief_id", "formato", "persona", "hipotese", "hook", "prova", "cta", "utm_content"]
    for field in required:
        if not str(item.get(field, "")).strip():
            flags.append(f"faltando_{field}")
    if not item.get("cenas") and not item.get("slides"):
        flags.append("sem_cenas_ou_slides")
    if str(item.get("variavel_testada", "")).strip() == "":
        flags.append("variavel_nao_declarada")
    return "; ".join(flags) if flags else "ok"


def normalize_script(item: dict[str, Any]) -> dict[str, str]:
    row = {field: str(item.get(field, "")) for field in FIELDS if field != "qa_flags"}
    row["qa_flags"] = qa_flags(item)
    return row


def normalize_scenes(item: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    creative_id = str(item.get("creative_id", ""))
    scenes = item.get("cenas", [])
    if isinstance(scenes, list):
        for index, scene in enumerate(scenes, start=1):
            if not isinstance(scene, dict):
                continue
            rows.append({
                "creative_id": creative_id,
                "tipo": "video",
                "ordem": str(index),
                "tempo_ou_slide": str(scene.get("tempo", "")),
                "funcao": str(scene.get("funcao", "")),
                "texto_ou_fala": str(scene.get("fala", "")),
                "texto_tela": str(scene.get("texto_tela", "")),
                "prova_exemplo": "",
                "visual": str(scene.get("visual", "")),
                "cta_transicao": "",
                "atributo": "",
                "edicao": str(scene.get("edicao", "")),
            })
    slides = item.get("slides", [])
    if isinstance(slides, list):
        for index, slide in enumerate(slides, start=1):
            if not isinstance(slide, dict):
                continue
            rows.append({
                "creative_id": creative_id,
                "tipo": "carousel",
                "ordem": str(index),
                "tempo_ou_slide": str(slide.get("slide", "")),
                "funcao": str(slide.get("funcao", "")),
                "texto_ou_fala": str(slide.get("texto", "")),
                "texto_tela": str(slide.get("texto", "")),
                "prova_exemplo": str(slide.get("prova_exemplo", "")),
                "visual": str(slide.get("visual", "")),
                "cta_transicao": str(slide.get("cta_transicao", "")),
                "atributo": str(slide.get("atributo", "")),
                "edicao": "",
            })
    return rows


def build_rows(payload: dict[str, Any]) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, Any]]]:
    scripts = payload.get("roteiros", [])
    if not isinstance(scripts, list):
        raise ValueError("'roteiros' must be a list.")
    raw = [item for item in scripts if isinstance(item, dict)]
    script_rows = [normalize_script(item) for item in raw]
    scene_rows: list[dict[str, str]] = []
    for item in raw:
        scene_rows.extend(normalize_scenes(item))
    return script_rows, scene_rows, raw


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_video(item: dict[str, Any]) -> list[str]:
    scenes = item.get("cenas", [])
    if not isinstance(scenes, list) or not scenes:
        return []
    lines = [
        "| Tempo | Função | Fala | Texto em tela | Visual | Edição |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for scene in scenes:
        if isinstance(scene, dict):
            fields = ["tempo", "funcao", "fala", "texto_tela", "visual", "edicao"]
            lines.append("| " + " | ".join(escape_md(str(scene.get(field, ""))) for field in fields) + " |")
    return lines


def render_carousel(item: dict[str, Any]) -> list[str]:
    slides = item.get("slides", [])
    if not isinstance(slides, list) or not slides:
        return []
    lines = [
        "| Slide | Função | Texto | Prova/exemplo | Visual | CTA/transição | Atributo |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for slide in slides:
        if isinstance(slide, dict):
            fields = ["slide", "funcao", "texto", "prova_exemplo", "visual", "cta_transicao", "atributo"]
            lines.append("| " + " | ".join(escape_md(str(slide.get(field, ""))) for field in fields) + " |")
    return lines


def write_markdown(path: Path, script_rows: list[dict[str, str]], raw_items: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Roteiros Criativos Performance", ""]
    for row, item in zip(script_rows, raw_items):
        lines.extend([
            f"## {row['creative_id']} - {row['formato']}",
            "",
            f"- Brief ID: {row['brief_id']}",
            f"- Persona: {row['persona']}",
            f"- Etapa: {row['etapa']}",
            f"- Hipótese: {row['hipotese']}",
            f"- Variável testada: {row['variavel_testada']}",
            f"- Hook: {row['hook']}",
            f"- CTA: {row['cta']}",
            f"- UTM content: `{escape_md(row['utm_content'])}`",
            f"- QA flags: {row['qa_flags']}",
            "",
            "### Roteiro",
            "",
        ])
        lines.extend(render_video(item) or render_carousel(item))
        lines.extend([
            "",
            "### Legenda / Copy",
            "",
            row["legenda"],
            "",
            "### Direção Visual",
            "",
            row["direcao_visual"],
            "",
        ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build performance creative scripts from JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path, help="Main script matrix CSV.")
    parser.add_argument("--scenes-csv", dest="scenes_csv_path", type=Path, help="Optional scene/slide CSV.")
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    script_rows, scene_rows, raw_items = build_rows(payload)
    if not args.md_path and not args.csv_path and not args.scenes_csv_path:
        for row in script_rows:
            print(f"{row['creative_id']}: {row['formato']} [{row['qa_flags']}]")
        return
    if args.csv_path:
        write_csv(args.csv_path, FIELDS, script_rows)
    if args.scenes_csv_path:
        write_csv(args.scenes_csv_path, SCENE_FIELDS, scene_rows)
    if args.md_path:
        write_markdown(args.md_path, script_rows, raw_items)


if __name__ == "__main__":
    main()

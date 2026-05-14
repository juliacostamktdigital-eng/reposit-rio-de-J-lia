#!/usr/bin/env python3
"""Print context for iterating Marketing OS skills."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


WORKFLOW_RE = re.compile(r"workflow\.knowledge-os\.v(\d+)\.json$")


def find_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "assets" / "canonicos").is_dir() and (candidate / ".claude" / "skills").is_dir():
            return candidate
    raise SystemExit("Nao encontrei a raiz do workflow_marketing_os_v1.")


def latest_workflow(root: Path) -> Path:
    versions: list[tuple[int, Path]] = []
    for path in root.glob("workflow.knowledge-os.v*.json"):
        match = WORKFLOW_RE.match(path.name)
        if match:
            versions.append((int(match.group(1)), path))
    if not versions:
        raise SystemExit("Nao encontrei workflow.knowledge-os.vN.json.")
    return max(versions, key=lambda item: item[0])[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def skill_files(root: Path) -> list[Path]:
    return sorted((root / ".claude" / "skills").glob("*/*/SKILL.md"))


def parse_frontmatter_name(markdown: str) -> str | None:
    if not markdown.startswith("---"):
        return None
    end = markdown.find("\n---", 3)
    if end == -1:
        return None
    for line in markdown[3:end].splitlines():
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip()
    return None


def resolve_skill(root: Path, value: str) -> Path:
    candidate = Path(value)
    if candidate.exists():
        if candidate.is_dir():
            candidate = candidate / "SKILL.md"
        return candidate.resolve()

    matches: list[Path] = []
    for path in skill_files(root):
        skill_id = path.parent.name
        if value == skill_id:
            matches.append(path)
            continue
        name = parse_frontmatter_name(path.read_text(encoding="utf-8"))
        if value == name:
            matches.append(path)

    if not matches:
        raise SystemExit(f"Nao encontrei skill com id ou caminho: {value}")
    if len(matches) > 1:
        rels = "\n".join(str(path.relative_to(root)) for path in matches)
        raise SystemExit(f"Skill ambigua. Matches:\n{rels}")
    return matches[0]


def playbook_dir_for_skill(root: Path, skill_path: Path) -> str:
    rel = skill_path.relative_to(root / ".claude" / "skills")
    parts = rel.parts
    if len(parts) < 3:
        raise SystemExit(f"Caminho de skill inesperado: {skill_path}")
    return parts[0]


def summarize_skill(root: Path, skill_path: Path, workflow: dict[str, Any]) -> dict[str, Any]:
    playbook_dir = playbook_dir_for_skill(root, skill_path)
    canonical = root / "assets" / "canonicos" / f"{playbook_dir}.md"
    doc_path = f"./assets/canonicos/{playbook_dir}.md"
    same_playbook = [
        {
            "id": path.parent.name,
            "skillPath": f"./{path.relative_to(root).as_posix()}",
        }
        for path in skill_files(root)
        if playbook_dir_for_skill(root, path) == playbook_dir
    ]
    auxiliary = sorted(
        f"./{path.relative_to(root).as_posix()}"
        for path in skill_path.parent.rglob("*")
        if path.is_file() and path.name != "SKILL.md"
    )

    canonical_doc = None
    for item in workflow.get("canonicalDocuments", []):
        if isinstance(item, dict) and item.get("path") == doc_path:
            canonical_doc = item
            break

    mentions = []
    for item in collect_doc_mentions(workflow, doc_path):
        mentions.append(item)

    return {
        "skillId": skill_path.parent.name,
        "skillPath": f"./{skill_path.relative_to(root).as_posix()}",
        "playbookDir": playbook_dir,
        "canonicalPath": f"./{canonical.relative_to(root).as_posix()}" if canonical.exists() else None,
        "canonicalExists": canonical.exists(),
        "canonicalDocument": canonical_doc,
        "workflowMentions": mentions[:20],
        "samePlaybookSkills": same_playbook,
        "auxiliaryFiles": auxiliary,
    }


def collect_doc_mentions(payload: Any, doc_path: str) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []

    def walk(value: Any, trail: list[str]) -> None:
        if isinstance(value, dict):
            if value.get("docPath") == doc_path or value.get("path") == doc_path:
                out.append(
                    {
                        "where": ".".join(trail) or "$",
                        "id": str(value.get("id", "")),
                        "title": str(value.get("title", value.get("name", ""))),
                    }
                )
            for key, child in value.items():
                walk(child, [*trail, str(key)])
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, [*trail, str(index)])

    walk(payload, [])
    return out


def summarize_all(root: Path) -> dict[str, Any]:
    names: dict[str, list[str]] = {}
    by_playbook: dict[str, int] = {}
    for path in skill_files(root):
        markdown = path.read_text(encoding="utf-8")
        name = parse_frontmatter_name(markdown) or path.parent.name
        names.setdefault(name, []).append(f"./{path.relative_to(root).as_posix()}")
        playbook_dir = playbook_dir_for_skill(root, path)
        by_playbook[playbook_dir] = by_playbook.get(playbook_dir, 0) + 1

    duplicates = {name: paths for name, paths in names.items() if len(paths) > 1}
    return {
        "totalSkills": len(skill_files(root)),
        "skillsByPlaybook": dict(sorted(by_playbook.items())),
        "duplicateNames": duplicates,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", help="Raiz do workflow_marketing_os_v1.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--skill", help="Id, name, caminho do SKILL.md ou diretorio da skill.")
    group.add_argument("--playbook", help="Diretorio de playbook em .claude/skills.")
    group.add_argument("--all", action="store_true", help="Resumo de todas as skills.")
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else find_root(Path.cwd().resolve())
    workflow_path = latest_workflow(root)
    workflow = load_json(workflow_path)

    result: dict[str, Any] = {
        "root": str(root),
        "latestWorkflow": f"./{workflow_path.relative_to(root).as_posix()}",
        "workflowVersion": workflow.get("version"),
    }

    manifest_path = root / "workflow.manifest.json"
    if manifest_path.exists():
        manifest = load_json(manifest_path)
        result["manifestDefaultVersionId"] = manifest.get("defaultVersionId")

    if args.skill:
        result["skill"] = summarize_skill(root, resolve_skill(root, args.skill), workflow)
    elif args.playbook:
        paths = [path for path in skill_files(root) if playbook_dir_for_skill(root, path) == args.playbook]
        result["playbook"] = args.playbook
        result["skills"] = [summarize_skill(root, path, workflow) for path in paths]
    else:
        result["summary"] = summarize_all(root)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

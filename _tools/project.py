#!/usr/bin/env python3
"""Project Manager — Multi-project workspace management via symlinks.

Usage:
    python project.py create "Nome do Projeto" [--group "Squad Checkout"] [--description "..."]
    python project.py list
    python project.py switch <slug-or-name>
    python project.py status
    python project.py archive <slug-or-name>
    python project.py delete <slug-or-name>
    python project.py rename <slug-or-name> "Novo Nome"
    python project.py group "Squad Checkout"              # list projects in group
    python project.py cross-ref "Squad Checkout"          # cross-reference report
    python project.py cross-ref projeto1 projeto2         # cross-ref specific projects
    python project.py link projeto1 projeto2 [--note "..."]  # link related projects
    python project.py links [projeto]                     # show linked projects

Projects live in projects/<slug>/ with standard discovery structure.
Root-level dirs (0-documentation, 1-problem, 2-solution, 3-delivery)
are symlinks to the active project. This means all skills and agents
work without any path changes.
"""

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS_DIR = ROOT / "projects"
REGISTRY_FILE = PROJECTS_DIR / "registry.json"
WORKSPACE_DIRS = ["0-documentation", "1-problem", "2-solution", "3-delivery"]
DOMAINS_DIR = ROOT / "domains"
DOMAIN_CONTEXT_SYMLINKS = ["_domain-context", "_domain-knowledge"]

# Full directory structure for a new project
PROJECT_STRUCTURE = [
    "0-documentation/0a-projectdocs",
    "0-documentation/0b-Interviews",
    "1-problem/1a-interview-analysis",
    "1-problem/1b-painpoints/1b0-granular",
    "1-problem/1b-painpoints/1b1-painpoints-breakdown",
    "1-problem/1b-painpoints/1b2-jtbd",
    "1-problem/1c-asis-journey/1c2-asis-breakdown",
    "1-problem/1d-problem-output",
    "2-solution/2a-opportunities",
    "2-solution/2b-tobe-journey",
    "2-solution/2c-solution-concepts",
    "2-solution/2d-prioritization",
    "2-solution/2e-roadmap",
    "2-solution/2f-solution-output",
    "3-delivery/confluence",
    "3-delivery/jira",
]

INITIATIVE_STRUCTURES = {
    "investigation": ["notes"],
    "quick": PROJECT_STRUCTURE.copy(),
    "full": PROJECT_STRUCTURE.copy(),
}


def slugify(name):
    """Convert project name to filesystem-safe slug."""
    slug = name.lower().strip()
    slug = re.sub(r"[àáâãäå]", "a", slug)
    slug = re.sub(r"[èéêë]", "e", slug)
    slug = re.sub(r"[ìíîï]", "i", slug)
    slug = re.sub(r"[òóôõö]", "o", slug)
    slug = re.sub(r"[ùúûü]", "u", slug)
    slug = re.sub(r"[ç]", "c", slug)
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug


def load_registry():
    """Load or create project registry."""
    if REGISTRY_FILE.exists():
        with open(REGISTRY_FILE) as f:
            reg = json.load(f)
        # Auto-detect v1 and add missing v2 fields
        if "version" not in reg:
            reg["version"] = 2
        if "domains" not in reg:
            reg["domains"] = []
        return reg
    return {"version": 2, "active": None, "projects": [], "domains": []}


def save_registry(registry):
    """Save project registry."""
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(REGISTRY_FILE, "w") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)


def find_project(registry, query):
    """Find project by slug or name (partial match)."""
    query_lower = query.lower()
    # Exact slug match
    for p in registry["projects"]:
        if p["slug"] == query_lower or p["slug"] == slugify(query):
            return p
    # Partial name match
    for p in registry["projects"]:
        if query_lower in p["name"].lower():
            return p
    return None


def get_active_path(registry):
    """Resolve filesystem path for the active project/initiative."""
    active = registry.get("active")
    if active is None:
        return None, None  # (path, domain_slug)

    # v1: active is a string (legacy slug)
    if isinstance(active, str):
        return PROJECTS_DIR / active, None

    # v2: active is an object
    if active.get("type") == "project":
        return PROJECTS_DIR / active["slug"], None
    elif active.get("type") == "initiative":
        path = DOMAINS_DIR / active["domain"] / "initiatives" / active["slug"]
        return path, active["domain"]

    return None, None


def find_domain(registry, query):
    """Find domain by slug or name (partial match)."""
    query_lower = query.lower()
    for d in registry.get("domains", []):
        if d["slug"] == query_lower or d["slug"] == slugify(query):
            return d
        if query_lower in d["name"].lower():
            return d
    return None


def find_initiative(domain, query):
    """Find initiative by slug or name (partial match)."""
    query_lower = query.lower()
    for i in domain.get("initiatives", []):
        if i["slug"] == query_lower or i["slug"] == slugify(query):
            return i
        if query_lower in i["name"].lower():
            return i
    return None


def update_symlinks(target_path, domain_slug=None):
    """Update root symlinks to point to the given project/initiative path."""
    for dirname in WORKSPACE_DIRS:
        link_path = ROOT / dirname
        target = target_path / dirname

        # Remove existing (symlink, dir, or file)
        if link_path.is_symlink():
            link_path.unlink()
        elif link_path.is_dir():
            # Real directory exists — merge contents into project
            if target.exists():
                shutil.copytree(str(link_path), str(target), dirs_exist_ok=True)
            shutil.rmtree(str(link_path))

        # Create symlink (relative path for portability)
        if target.exists():
            rel_target = os.path.relpath(target, ROOT)
            link_path.symlink_to(rel_target)

    # Domain context symlinks
    for ctx_name in DOMAIN_CONTEXT_SYMLINKS:
        link_path = ROOT / ctx_name
        if link_path.is_symlink():
            link_path.unlink()

    if domain_slug:
        domain_dir = DOMAINS_DIR / domain_slug
        ctx_map = {
            "_domain-context": domain_dir / "_context",
            "_domain-knowledge": domain_dir / "_knowledge",
        }
        for link_name, target in ctx_map.items():
            if target.exists():
                link_path = ROOT / link_name
                rel_target = os.path.relpath(target, ROOT)
                link_path.symlink_to(rel_target)


def remove_symlinks():
    """Remove workspace symlinks from root."""
    for dirname in WORKSPACE_DIRS:
        link_path = ROOT / dirname
        if link_path.is_symlink():
            link_path.unlink()


def cmd_create(args):
    """Create a new project."""
    registry = load_registry()
    slug = slugify(args.name)

    # Check for duplicates
    if any(p["slug"] == slug for p in registry["projects"]):
        print(f"Erro: Projeto '{args.name}' já existe (slug: {slug})")
        sys.exit(1)

    # Create directory structure
    project_dir = PROJECTS_DIR / slug
    for subdir in PROJECT_STRUCTURE:
        (project_dir / subdir).mkdir(parents=True, exist_ok=True)

    # Create project metadata file
    today = datetime.now().strftime("%Y-%m-%d")
    meta = {
        "name": args.name,
        "slug": slug,
        "created": today,
        "status": "active",
        "description": args.description or "",
        "group": args.group or "",
        "links": [],
    }

    group_line = f"\n**Grupo:** {args.group}" if args.group else ""
    meta_content = f"""# {args.name}

**Slug:** {slug}
**Criado:** {today}
**Status:** ativo{group_line}
**Descrição:** {args.description or 'Sem descrição'}

## Notas

_(adicione notas sobre este projeto aqui)_
"""
    with open(project_dir / "project.md", "w") as f:
        f.write(meta_content)

    # Create broad-context.md template
    ctx_content = f"""# Contexto do Projeto — {args.name}

## Empresa / Produto

## Problema Central

## Público-alvo

## Objetivos da Discovery

## Fontes de Dados Disponíveis

## Restrições e Premissas
"""
    ctx_path = project_dir / "0-documentation" / "broad-context.md"
    if not ctx_path.exists():
        with open(ctx_path, "w") as f:
            f.write(ctx_content)

    # Add to registry
    registry["projects"].append(meta)
    registry["active"] = slug
    save_registry(registry)

    # Update symlinks
    update_symlinks(PROJECTS_DIR / slug)

    print(f"✓ Projeto '{args.name}' criado!")
    print(f"  Slug: {slug}")
    print(f"  Diretório: projects/{slug}/")
    print(f"  Status: ativo (projeto atual)")


def format_project_line(p, active):
    """Format a single project line for display."""
    marker = " ◀ atual" if p["slug"] == active else ""
    desc = f' — {p["description"]}' if p.get("description") else ""
    icon = "●" if p["slug"] == active else "○"
    if p.get("status") == "archived":
        icon = "◻"
    links = p.get("links", [])
    link_indicator = f" [{len(links)} links]" if links else ""
    return f'  {icon} {p["name"]}{desc} [{p["created"]}]{link_indicator}{marker}'


def cmd_list(args):
    """List all projects."""
    registry = load_registry()
    projects = registry["projects"]

    if not projects:
        print("Nenhum projeto encontrado. Use 'create' para começar!")
        return

    active = registry.get("active")

    # Separate active and archived
    active_projects = [p for p in projects if p.get("status") == "active"]
    archived_projects = [p for p in projects if p.get("status") == "archived"]

    # Group active projects by group
    grouped = {}
    ungrouped = []
    for p in active_projects:
        group = p.get("group", "")
        if group:
            grouped.setdefault(group, []).append(p)
        else:
            ungrouped.append(p)

    print("PROJETOS ATIVOS")
    print("-" * 55)

    # Show grouped first
    for group_name in sorted(grouped.keys()):
        print(f"\n  [{group_name}]")
        for p in grouped[group_name]:
            print(format_project_line(p, active))

    # Then ungrouped
    if ungrouped:
        if grouped:
            print(f"\n  [Sem grupo]")
        for p in ungrouped:
            print(format_project_line(p, active))

    if archived_projects:
        print(f"\nARQUIVADOS")
        print("-" * 55)
        for p in archived_projects:
            print(format_project_line(p, active))

    print(f"\nTotal: {len(active_projects)} ativos, {len(archived_projects)} arquivados")
    if grouped:
        print(f"Grupos: {', '.join(sorted(grouped.keys()))}")

    # Show domains + initiatives
    domains = registry.get("domains", [])
    if domains:
        print("\n--- Dominios ---")
        for d in domains:
            print(f"\n  {d['name']} ({d.get('owner', '')})")
            for i in d.get("initiatives", []):
                marker = "→" if (isinstance(active, dict) and active.get("slug") == i["slug"]) else " "
                print(f"    {marker} [{i.get('size','full'):13s}] {i['name']} ({i['slug']})")


def cmd_switch(args):
    """Switch active project."""
    registry = load_registry()

    if "/" in args.name:
        # domain/initiative format
        parts = args.name.split("/", 1)
        domain = find_domain(registry, parts[0])
        if domain:
            initiative = find_initiative(domain, parts[1])
            if initiative:
                initiative_dir = DOMAINS_DIR / domain["slug"] / "initiatives" / initiative["slug"]
                registry["active"] = {"type": "initiative", "domain": domain["slug"], "slug": initiative["slug"]}
                save_registry(registry)
                update_symlinks(initiative_dir, domain_slug=domain["slug"])
                print(f"Switched to: {initiative['name']} ({domain['name']})")
                return
        print(f"Iniciativa '{args.name}' nao encontrada")
        sys.exit(1)

    project = find_project(registry, args.name)

    if not project:
        print(f"Erro: Projeto '{args.name}' não encontrado.")
        print("Projetos disponíveis:")
        for p in registry["projects"]:
            print(f"  - {p['name']} ({p['slug']})")
        sys.exit(1)

    if project["slug"] == registry.get("active"):
        print(f"'{project['name']}' já é o projeto atual!")
        return

    registry["active"] = project["slug"]
    save_registry(registry)
    update_symlinks(PROJECTS_DIR / project["slug"])

    print(f"✓ Trocado para '{project['name']}'")
    print(f"  Diretório: projects/{project['slug']}/")


def cmd_status(args):
    """Show current project status."""
    registry = load_registry()
    active = registry.get("active")

    if isinstance(active, dict) and active.get("type") == "initiative":
        domain = find_domain(registry, active["domain"])
        initiative = find_initiative(domain, active["slug"])
        print(f"Projeto ativo: {initiative['name']}")
        print(f"Dominio: {domain['name']}")
        print(f"Tipo: {initiative.get('size', 'full')}")
        print(f"Path: domains/{active['domain']}/initiatives/{active['slug']}/")
        return

    if not active:
        print("Nenhum projeto ativo. Use 'create' para começar!")
        return

    project = find_project(registry, active)
    if not project:
        print(f"Erro: projeto ativo '{active}' não encontrado no registro.")
        return

    project_dir = PROJECTS_DIR / active

    print(f"PROJETO ATUAL: {project['name']}")
    print(f"  Slug: {project['slug']}")
    print(f"  Criado: {project['created']}")
    print(f"  Status: {project.get('status', 'active')}")
    if project.get("group"):
        print(f"  Grupo: {project['group']}")
    if project.get("description"):
        print(f"  Descrição: {project['description']}")
    if project.get("links"):
        linked_names = []
        for link in project["links"]:
            lp = find_project(registry, link["slug"])
            name = lp["name"] if lp else link["slug"]
            note = f' ({link["note"]})' if link.get("note") else ""
            linked_names.append(f"{name}{note}")
        print(f"  Relacionados: {', '.join(linked_names)}")
    print()

    # Check what phases have content
    phases = {
        "0-documentation": "Documentação",
        "1-problem": "Análise de Problemas",
        "2-solution": "Ideação de Soluções",
        "3-delivery": "Entregáveis",
    }

    print("PROGRESSO")
    print("-" * 40)
    for dirname, label in phases.items():
        phase_dir = project_dir / dirname
        if phase_dir.exists():
            files = list(phase_dir.rglob("*.md"))
            if files:
                print(f"  ✓ {label} ({len(files)} arquivos)")
            else:
                print(f"  ○ {label} (vazio)")
        else:
            print(f"  ✗ {label} (não existe)")


def cmd_archive(args):
    """Archive a project."""
    registry = load_registry()
    project = find_project(registry, args.name)

    if not project:
        print(f"Erro: Projeto '{args.name}' não encontrado.")
        sys.exit(1)

    project["status"] = "archived"

    # If archiving the active project, deactivate
    if project["slug"] == registry.get("active"):
        registry["active"] = None
        remove_symlinks()
        print(f"  (symlinks removidos — nenhum projeto ativo)")

    save_registry(registry)
    print(f"✓ Projeto '{project['name']}' arquivado.")


def cmd_delete(args):
    """Delete a project (requires --confirm)."""
    if not args.confirm:
        print("ATENÇÃO: Isso vai APAGAR todos os dados do projeto permanentemente!")
        print(f"Para confirmar, rode novamente com --confirm")
        sys.exit(1)

    registry = load_registry()
    project = find_project(registry, args.name)

    if not project:
        print(f"Erro: Projeto '{args.name}' não encontrado.")
        sys.exit(1)

    # Remove from active if needed
    if project["slug"] == registry.get("active"):
        registry["active"] = None
        remove_symlinks()

    # Remove directory
    project_dir = PROJECTS_DIR / project["slug"]
    if project_dir.exists():
        shutil.rmtree(project_dir)

    # Remove from registry
    registry["projects"] = [p for p in registry["projects"] if p["slug"] != project["slug"]]
    save_registry(registry)

    print(f"✓ Projeto '{project['name']}' deletado permanentemente.")


def cmd_rename(args):
    """Rename a project."""
    registry = load_registry()
    project = find_project(registry, args.name)

    if not project:
        print(f"Erro: Projeto '{args.name}' não encontrado.")
        sys.exit(1)

    old_name = project["name"]
    project["name"] = args.new_name
    save_registry(registry)

    # Update project.md
    meta_file = PROJECTS_DIR / project["slug"] / "project.md"
    if meta_file.exists():
        content = meta_file.read_text()
        content = content.replace(f"# {old_name}", f"# {args.new_name}", 1)
        meta_file.write_text(content)

    print(f"✓ Projeto renomeado: '{old_name}' → '{args.new_name}'")


def cmd_group(args):
    """List projects in a group."""
    registry = load_registry()
    active = registry.get("active")
    group_lower = args.name.lower()

    matches = [p for p in registry["projects"]
               if group_lower in p.get("group", "").lower()]

    if not matches:
        # Show available groups
        all_groups = set(p.get("group", "") for p in registry["projects"] if p.get("group"))
        if all_groups:
            print(f"Grupo '{args.name}' não encontrado. Grupos disponíveis:")
            for g in sorted(all_groups):
                count = sum(1 for p in registry["projects"] if p.get("group") == g)
                print(f"  - {g} ({count} projetos)")
        else:
            print("Nenhum grupo definido. Use --group ao criar projetos.")
        return

    group_name = matches[0].get("group", args.name)
    print(f"GRUPO: {group_name}")
    print("-" * 55)
    for p in matches:
        print(format_project_line(p, active))

    # Show phase progress comparison
    print(f"\nPROGRESSO COMPARADO")
    print("-" * 55)
    phases = {
        "0-documentation": "Docs",
        "1-problem": "Problema",
        "2-solution": "Solução",
        "3-delivery": "Entrega",
    }
    header = f'  {"Projeto":<25}'
    for label in phases.values():
        header += f" {label:>10}"
    print(header)

    for p in matches:
        pdir = PROJECTS_DIR / p["slug"]
        line = f'  {p["name"][:25]:<25}'
        for dirname in phases:
            d = pdir / dirname
            if d.exists():
                count = len(list(d.rglob("*.md")))
                line += f" {count:>10}" if count else f' {"—":>10}'
            else:
                line += f' {"—":>10}'
        print(line)


def get_key_outputs(project_slug):
    """Extract key outputs from a project for cross-referencing."""
    pdir = PROJECTS_DIR / project_slug
    outputs = {}

    key_files = {
        "pain-report": "1-problem/1d-problem-output/pain-report.md",
        "problem-report": "1-problem/1d-problem-output/problem-report.md",
        "painpoint-mapping": "1-problem/1b-painpoints/painpoint-mapping.md",
        "jtbd-mapping": "1-problem/1b-painpoints/1b2-jtbd/jtbd-mapping.md",
        "journey": "1-problem/1c-asis-journey/asis-journey.md",
        "opportunities": "2-solution/2a-opportunities/opportunities-identification.md",
        "solution-concepts": "2-solution/2c-solution-concepts/solution-concepts.md",
        "mvp-scope": "2-solution/2d-prioritization/mvp-scope.md",
        "product-brief": "2-solution/2f-solution-output/product-brief.md",
    }

    for key, relpath in key_files.items():
        fpath = pdir / relpath
        if fpath.exists():
            outputs[key] = fpath.read_text()

    # Also collect all granular pain points
    granular_dir = pdir / "1-problem/1b-painpoints/1b0-granular"
    if granular_dir.exists():
        granular_texts = []
        for f in sorted(granular_dir.glob("*.md")):
            if "review" not in f.name:
                granular_texts.append(f.read_text())
        if granular_texts:
            outputs["granular-painpoints"] = "\n\n---\n\n".join(granular_texts)

    return outputs


def cmd_crossref(args):
    """Generate cross-reference report between projects."""
    registry = load_registry()

    # Determine which projects to cross-reference
    if len(args.targets) == 1:
        # Could be a group name
        group_lower = args.targets[0].lower()
        targets = [p for p in registry["projects"]
                   if group_lower in p.get("group", "").lower()
                   and p.get("status") == "active"]
        if not targets:
            # Try as project name — need at least 2
            print("Cross-reference precisa de pelo menos 2 projetos.")
            print("Use: cross-ref 'Nome do Grupo' ou cross-ref projeto1 projeto2")
            sys.exit(1)
    else:
        targets = []
        for name in args.targets:
            p = find_project(registry, name)
            if not p:
                print(f"Erro: Projeto '{name}' não encontrado.")
                sys.exit(1)
            targets.append(p)

    if len(targets) < 2:
        print("Cross-reference precisa de pelo menos 2 projetos.")
        sys.exit(1)

    # Collect outputs from all projects
    all_outputs = {}
    for p in targets:
        all_outputs[p["slug"]] = {
            "name": p["name"],
            "outputs": get_key_outputs(p["slug"]),
        }

    # Generate cross-reference report
    today = datetime.now().strftime("%Y-%m-%d")
    group_name = targets[0].get("group", "Cross-reference")
    project_names = [p["name"] for p in targets]

    lines = [
        f"# Cross-Reference Report — {group_name}",
        f"**Data:** {today}",
        f"**Projetos:** {', '.join(project_names)}",
        "",
        "[Source: cross-reference automática entre projetos]",
        "",
        "## Conteúdo por Projeto",
        "",
    ]

    for slug, data in all_outputs.items():
        name = data["name"]
        outputs = data["outputs"]
        lines.append(f"### {name}")
        if not outputs:
            lines.append("_(sem outputs ainda)_")
        else:
            lines.append(f"Outputs disponíveis: {', '.join(outputs.keys())}")
        lines.append("")

    # Sections for each key output type that exists in multiple projects
    output_types = {
        "painpoint-mapping": "Pain Points",
        "jtbd-mapping": "Jobs to Be Done",
        "journey": "Jornada As-Is",
        "opportunities": "Oportunidades",
        "mvp-scope": "Escopo MVP",
        "product-brief": "Product Brief",
    }

    lines.append("## Outputs Lado a Lado")
    lines.append("")

    for key, label in output_types.items():
        projects_with = [(slug, d) for slug, d in all_outputs.items() if key in d["outputs"]]
        if len(projects_with) >= 2:
            lines.append(f"### {label}")
            lines.append("")
            for slug, data in projects_with:
                content = data["outputs"][key]
                # Extract first ~30 lines as summary
                content_lines = content.strip().split("\n")[:30]
                preview = "\n".join(content_lines)
                lines.append(f"#### {data['name']}")
                lines.append("```")
                lines.append(preview)
                if len(content.strip().split("\n")) > 30:
                    lines.append(f"... ({len(content.strip().split(chr(10)))} linhas total)")
                lines.append("```")
                lines.append("")

    lines.extend([
        "## Análise Cruzada",
        "",
        "_(Use este relatório como input para o Claude analisar padrões comuns,_",
        "_pain points compartilhados, oportunidades de sinergia e contradições._",
        "_Peça: 'analise o cross-ref e identifique padrões')_",
        "",
        "---",
        f"*Gerado automaticamente em {today}*",
    ])

    report = "\n".join(lines)

    # Save report
    output_dir = PROJECTS_DIR / "_cross-references"
    output_dir.mkdir(exist_ok=True)
    slugs = "-".join(p["slug"][:15] for p in targets[:3])
    output_file = output_dir / f"{today}-{slugs}.md"
    output_file.write_text(report)

    print(f"✓ Cross-reference gerado!")
    print(f"  Projetos: {', '.join(project_names)}")
    print(f"  Arquivo: {output_file.relative_to(ROOT)}")
    print(f"\n  Dica: peça ao Claude 'analise o cross-ref' para insights cruzados")


def cmd_link(args):
    """Link two related projects."""
    registry = load_registry()

    p1 = find_project(registry, args.project1)
    p2 = find_project(registry, args.project2)

    if not p1:
        print(f"Erro: Projeto '{args.project1}' não encontrado.")
        sys.exit(1)
    if not p2:
        print(f"Erro: Projeto '{args.project2}' não encontrado.")
        sys.exit(1)

    if p1["slug"] == p2["slug"]:
        print("Erro: Não pode linkar um projeto com ele mesmo.")
        sys.exit(1)

    note = args.note or ""

    # Add bidirectional link
    if "links" not in p1:
        p1["links"] = []
    if "links" not in p2:
        p2["links"] = []

    # Check if already linked
    if any(l["slug"] == p2["slug"] for l in p1["links"]):
        print(f"'{p1['name']}' e '{p2['name']}' já estão linkados.")
        return

    p1["links"].append({"slug": p2["slug"], "note": note})
    p2["links"].append({"slug": p1["slug"], "note": note})
    save_registry(registry)

    print(f"✓ Projetos linkados: '{p1['name']}' ↔ '{p2['name']}'")
    if note:
        print(f"  Nota: {note}")


def cmd_links(args):
    """Show linked projects."""
    registry = load_registry()

    if args.name:
        project = find_project(registry, args.name)
        if not project:
            print(f"Erro: Projeto '{args.name}' não encontrado.")
            sys.exit(1)
        projects_to_show = [project]
    else:
        # Show all projects with links
        projects_to_show = [p for p in registry["projects"] if p.get("links")]

    if not projects_to_show:
        print("Nenhum projeto com links encontrados.")
        return

    for p in projects_to_show:
        links = p.get("links", [])
        if not links:
            print(f"{p['name']}: sem links")
            continue
        print(f"{p['name']}:")
        for link in links:
            lp = find_project(registry, link["slug"])
            name = lp["name"] if lp else link["slug"]
            note = f' — {link["note"]}' if link.get("note") else ""
            print(f"  ↔ {name}{note}")


def cmd_domain_create(args):
    """Create a new domain."""
    registry = load_registry()
    slug = slugify(args.name)

    if find_domain(registry, slug):
        print(f"Erro: Dominio '{args.name}' ja existe")
        sys.exit(1)

    domain_dir = DOMAINS_DIR / slug
    (domain_dir / "_context").mkdir(parents=True, exist_ok=True)
    (domain_dir / "_knowledge").mkdir(parents=True, exist_ok=True)
    (domain_dir / "initiatives").mkdir(parents=True, exist_ok=True)

    # Create domain.md
    today = datetime.now().strftime("%Y-%m-%d")
    (domain_dir / "domain.md").write_text(f"# {args.name}\n**Owner:** {args.owner or 'N/A'}\n**Criado:** {today}\n**Descricao:** {args.description or ''}\n")

    # Create context templates
    (domain_dir / "_context" / "domain-context.md").write_text(f"# Domain Context — {args.name}\n\n## Sobre\n{args.description or 'Descreva o dominio aqui.'}\n\n## Stakeholders\n- \n\n## Metricas-chave\n- \n")
    (domain_dir / "_context" / "known-painpoints.md").write_text(f"# Known Pain Points — {args.name}\n\nPain points acumulados de todas as iniciativas neste dominio.\n\n(Atualizado automaticamente via `harvest`)\n")
    (domain_dir / "_context" / "metrics-baseline.md").write_text(f"# Metrics Baseline — {args.name}\n\nBaseline quantitativo do dominio.\n\n| Metrica | Valor Atual | Fonte | Data |\n|---------|-------------|-------|------|\n| | | | |\n")

    domain_entry = {
        "slug": slug,
        "name": args.name,
        "owner": args.owner or "",
        "created": today,
        "description": args.description or "",
        "initiatives": [],
    }
    registry["domains"].append(domain_entry)
    save_registry(registry)
    print(f"Dominio '{args.name}' criado em domains/{slug}/")


def cmd_domain_list(args):
    """List all domains."""
    registry = load_registry()
    domains = registry.get("domains", [])
    if not domains:
        print("Nenhum dominio criado. Use: python project.py domain create 'Nome'")
        return
    for d in domains:
        count = len(d.get("initiatives", []))
        print(f"  {d['name']} ({d['slug']}) — {count} iniciativas | Owner: {d.get('owner', 'N/A')}")


def cmd_domain_status(args):
    """Show domain details."""
    registry = load_registry()
    domain = find_domain(registry, args.query)
    if not domain:
        print(f"Dominio '{args.query}' nao encontrado")
        sys.exit(1)
    print(f"\n=== {domain['name']} ===")
    print(f"Owner: {domain.get('owner', 'N/A')}")
    print(f"Descricao: {domain.get('description', '')}")
    active = registry.get("active")
    active_slug = active.get("slug") if isinstance(active, dict) else None
    print(f"\nIniciativas ({len(domain.get('initiatives', []))}):")
    for i in domain.get("initiatives", []):
        marker = " ◀ atual" if i["slug"] == active_slug else ""
        print(f"  [{i.get('size', 'full'):13s}] {i['name']} ({i['slug']}) — {i.get('status', 'active')}{marker}")


def cmd_initiative_create(args):
    """Create an initiative within a domain."""
    registry = load_registry()
    domain = find_domain(registry, args.domain)
    if not domain:
        print(f"Dominio '{args.domain}' nao encontrado. Crie com: python project.py domain create 'Nome'")
        sys.exit(1)

    slug = slugify(args.name)
    size = args.size or "full"

    if find_initiative(domain, slug):
        print(f"Erro: Iniciativa '{args.name}' ja existe no dominio {domain['name']}")
        sys.exit(1)

    initiative_dir = DOMAINS_DIR / domain["slug"] / "initiatives" / slug
    structure = INITIATIVE_STRUCTURES.get(size, PROJECT_STRUCTURE)
    for subdir in structure:
        (initiative_dir / subdir).mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    size_labels = {"investigation": "Investigacao", "quick": "Quick Discovery", "full": "Full Discovery"}
    (initiative_dir / "initiative.md").write_text(
        f"# {args.name}\n**Dominio:** {domain['name']}\n**Tipo:** {size_labels.get(size, size)}\n"
        f"**Criado:** {today}\n**Descricao:** {args.description or ''}\n"
    )

    initiative_entry = {
        "slug": slug,
        "name": args.name,
        "created": today,
        "status": "active",
        "size": size,
        "description": args.description or "",
        "links": [],
    }
    domain["initiatives"].append(initiative_entry)
    save_registry(registry)

    # Activate it
    registry["active"] = {"type": "initiative", "domain": domain["slug"], "slug": slug}
    save_registry(registry)
    update_symlinks(initiative_dir, domain_slug=domain["slug"])
    print(f"Iniciativa '{args.name}' ({size}) criada em {domain['name']}")
    print(f"Context herdado de domains/{domain['slug']}/_context/")


def cmd_initiative_list(args):
    """List initiatives, optionally filtered by domain."""
    registry = load_registry()
    if args.domain:
        domain = find_domain(registry, args.domain)
        if not domain:
            print(f"Dominio '{args.domain}' nao encontrado")
            sys.exit(1)
        domains = [domain]
    else:
        domains = registry.get("domains", [])

    for d in domains:
        initiatives = d.get("initiatives", [])
        if not initiatives:
            continue
        print(f"\n  {d['name']}:")
        for i in initiatives:
            print(f"    [{i.get('size', 'full'):13s}] {i['name']} ({i['slug']}) — {i.get('status', 'active')}")


def cmd_harvest(args):
    """Extract learnings from completed initiative to domain knowledge."""
    registry = load_registry()
    active = registry.get("active")

    if not isinstance(active, dict) or active.get("type") != "initiative":
        print("Harvest so funciona com iniciativas em dominios. Projeto legacy nao suportado.")
        sys.exit(1)

    domain_slug = active["domain"]
    initiative_slug = active["slug"]
    domain = find_domain(registry, domain_slug)
    initiative = find_initiative(domain, initiative_slug)

    # Check if there's anything to harvest
    pain_report = ROOT / "1-problem" / "1d-problem-output" / "pain-report.md"
    problem_report = ROOT / "1-problem" / "1d-problem-output" / "problem-report.md"
    has_content = pain_report.exists() or problem_report.exists()

    if not has_content:
        print(f"Nenhum output encontrado pra harvest (pain-report.md ou problem-report.md).")
        print(f"Rode o pipeline primeiro ou use /pair pra gerar insights.")
        return

    knowledge_dir = DOMAINS_DIR / domain_slug / "_knowledge"
    knowledge_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")

    output_file = knowledge_dir / f"{today}-{initiative_slug}.md"

    content = f"# Learnings: {initiative['name']}\n**Data:** {today}\n**Tipo:** {initiative.get('size', 'full')}\n\n"

    if pain_report.exists():
        with open(pain_report) as f:
            report_text = f.read()
        content += "## Key Findings (from pain-report.md)\n\n"
        content += report_text[:500] + "\n...\n\n"

    content += "## Manual Notes\n\n(Adicione insights adicionais aqui)\n"

    output_file.write_text(content)
    print(f"Learnings salvos em {output_file.relative_to(ROOT)}")

    # Update known-painpoints in domain context
    known_pp = DOMAINS_DIR / domain_slug / "_context" / "known-painpoints.md"
    if known_pp.exists() and pain_report.exists():
        with open(known_pp, "a") as f:
            f.write(f"\n## De: {initiative['name']} ({today})\n\n")
            f.write(f"(Ver {output_file.relative_to(ROOT)} para detalhes)\n")
        print(f"Domain known-painpoints.md atualizado")


def main():
    parser = argparse.ArgumentParser(
        description="Product Discovery — Gerenciador de Projetos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", help="Comando")

    # create
    p_create = sub.add_parser("create", help="Criar novo projeto")
    p_create.add_argument("name", help="Nome do projeto")
    p_create.add_argument("--group", "-g", help="Grupo/squad (ex: 'Squad Checkout')")
    p_create.add_argument("--description", "-d", help="Descrição breve")

    # list
    sub.add_parser("list", help="Listar projetos")

    # switch
    p_switch = sub.add_parser("switch", help="Trocar projeto ativo")
    p_switch.add_argument("name", help="Nome ou slug do projeto")

    # status
    sub.add_parser("status", help="Status do projeto atual")

    # archive
    p_archive = sub.add_parser("archive", help="Arquivar projeto")
    p_archive.add_argument("name", help="Nome ou slug do projeto")

    # delete
    p_delete = sub.add_parser("delete", help="Deletar projeto")
    p_delete.add_argument("name", help="Nome ou slug do projeto")
    p_delete.add_argument("--confirm", action="store_true", help="Confirmar deleção")

    # rename
    p_rename = sub.add_parser("rename", help="Renomear projeto")
    p_rename.add_argument("name", help="Nome ou slug atual")
    p_rename.add_argument("new_name", help="Novo nome")

    # group
    p_group = sub.add_parser("group", help="Listar projetos de um grupo")
    p_group.add_argument("name", help="Nome do grupo")

    # cross-ref
    p_crossref = sub.add_parser("cross-ref", help="Cross-reference entre projetos")
    p_crossref.add_argument("targets", nargs="+", help="Nome do grupo ou nomes dos projetos")

    # link
    p_link = sub.add_parser("link", help="Linkar projetos relacionados")
    p_link.add_argument("project1", help="Primeiro projeto")
    p_link.add_argument("project2", help="Segundo projeto")
    p_link.add_argument("--note", "-n", help="Nota sobre a relação")

    # links
    p_links = sub.add_parser("links", help="Mostrar projetos linkados")
    p_links.add_argument("name", nargs="?", help="Nome do projeto (opcional)")

    # Domain commands
    p_domain = sub.add_parser("domain", help="Manage domains")
    domain_sub = p_domain.add_subparsers(dest="domain_action")

    p_dc = domain_sub.add_parser("create", help="Create domain")
    p_dc.add_argument("name")
    p_dc.add_argument("--owner", default="")
    p_dc.add_argument("--description", default="")

    p_dl = domain_sub.add_parser("list", help="List domains")
    p_ds = domain_sub.add_parser("status", help="Domain status")
    p_ds.add_argument("query")

    # Initiative commands
    p_init = sub.add_parser("initiative", help="Manage initiatives")
    init_sub = p_init.add_subparsers(dest="init_action")

    p_ic = init_sub.add_parser("create", help="Create initiative")
    p_ic.add_argument("name")
    p_ic.add_argument("--domain", required=True)
    p_ic.add_argument("--size", choices=["investigation", "quick", "full"], default="full")
    p_ic.add_argument("--description", default="")

    p_il = init_sub.add_parser("list", help="List initiatives")
    p_il.add_argument("--domain", default="")

    # Harvest
    p_harvest = sub.add_parser("harvest", help="Extract learnings to domain knowledge")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "create": cmd_create,
        "list": cmd_list,
        "switch": cmd_switch,
        "status": cmd_status,
        "archive": cmd_archive,
        "delete": cmd_delete,
        "rename": cmd_rename,
        "group": cmd_group,
        "cross-ref": cmd_crossref,
        "link": cmd_link,
        "links": cmd_links,
    }

    if args.command == "domain":
        if args.domain_action == "create": cmd_domain_create(args)
        elif args.domain_action == "list": cmd_domain_list(args)
        elif args.domain_action == "status": cmd_domain_status(args)
        else: p_domain.print_help()
    elif args.command == "initiative":
        if args.init_action == "create": cmd_initiative_create(args)
        elif args.init_action == "list": cmd_initiative_list(args)
        else: p_init.print_help()
    elif args.command == "harvest":
        cmd_harvest(args)
    else:
        commands[args.command](args)


if __name__ == "__main__":
    main()

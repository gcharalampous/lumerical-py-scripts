from __future__ import annotations
from pathlib import Path
from typing import Iterable, List, Dict, Optional
import sys
from sim_registry import get_sim


def _add_repo_root_to_syspath(start_file: str) -> Path:
    p = Path(start_file).resolve()
    for parent in [p.parent, *p.parents]:
        if (parent / "sim_registry.py").exists() and (parent / "project_layout.py").exists():
            parent_str = str(parent)
            if parent_str not in sys.path:
                sys.path.insert(0, parent_str)
            return parent
    raise RuntimeError("Repo root not found (sim_registry.py/project_layout.py missing).")


def setup(sim_key: str, start_file: str):
    """
    Ensures repo root is importable, loads SIM spec, creates output dirs,
    returns (spec, out, template_paths).
    """
    _add_repo_root_to_syspath(start_file)

    spec = get_sim(sim_key)

    # Support both dict specs and dataclass specs (SimSpec)
    domain = spec["domain"] if isinstance(spec, dict) else spec.domain
    module = spec["module"] if isinstance(spec, dict) else spec.module
    figure_groups = (
        spec.get("figure_groups", []) if isinstance(spec, dict) else getattr(spec, "figure_groups", [])
    )
    templates = spec.get("templates", []) if isinstance(spec, dict) else getattr(spec, "templates", [])
    create_lumerical_dir = (
        spec.get("create_lumerical_dir", False) if isinstance(spec, dict) 
        else getattr(spec, "create_lumerical_dir", False)
    )

    out = ensure_results_layout(domain, module, list(figure_groups), create_lumerical_dir)
    template_paths = [templates_dir(domain, module) / f for f in templates]
    return spec, out, template_paths



def repo_root() -> Path:
    """Return the repository root directory.

    Assumes this file (project_layout.py) lives in the repo root.
    """
    return Path(__file__).resolve().parent


def templates_dir(domain: str, module: str) -> Path:
    """Path to Lumerical template files for a given module."""
    return repo_root() / domain / module / "user_inputs" / "lumerical_files"


def results_module_dir(domain: str, module: str) -> Path:
    """Base results directory for a given module.

    Keeps your existing layout: <repo>/<DOMAIN>/Results/<module>/
    """
    return repo_root() / domain / "Results" / module


def ensure_dirs(dirs: Iterable[Path]) -> None:
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)


def ensure_results_layout(
    domain: str,
    module: str,
    figure_groups: Optional[List[str]] = None,
    create_lumerical_dir: bool = True,
) -> Dict[str, Path]:
    """Create (if needed) the standard results folders for a module."""
    out_root = results_module_dir(domain, module)
    figures_root = out_root / "Figures"
    lumerical_dir = out_root / "lumerical_files"

    figure_groups = figure_groups or []
    group_dirs = {g: figures_root / g for g in figure_groups}

    dirs = [figures_root, *group_dirs.values()]
    if create_lumerical_dir:
        dirs.append(lumerical_dir)

    ensure_dirs(dirs)

    return {
        "root": out_root,
        "figures": figures_root,
        "lumerical": lumerical_dir,
        "figure_groups": group_dirs,
    }

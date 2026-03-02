# Contributing

This is a solo research repository. This guide documents the project conventions,
development environment setup, and the steps for adding new simulation modules.

---

## Development Setup

### Requirements

- Python 3.8 or higher
- Lumerical Design Suite (required for running simulations)
- Conda (recommended) or virtualenv

### PYTHONPATH Configuration

Scripts are **not installed as a package**. Two paths must be on `PYTHONPATH`:

1. The repository root — so `project_layout.py` and `sim_registry.py` are importable
2. The Lumerical `api/python` directory — so `lumapi` is importable

**VSCode** — create or edit `.env` at the repo root:

```
PYTHONPATH=C:\Program Files\Lumerical\vXXX\api\python;D:\path\to\lumerical-py-scripts
```

**Spyder** — add both paths via `Tools → PYTHONPATH manager → Add Path`.

Replace `vXXX` with your installed Lumerical version (e.g. `v232`).

### Installing Dev Tools (no lumapi needed)

```bash
pip install ruff pre-commit
pre-commit install
```

---

## Adding a New Simulation Module

Follow these steps to stay consistent with the existing 27 modules.

### 1. Create the directory structure

```
<DOMAIN>/<module_name>/
├── README.md                       ← copy from README_TEMPLATE.md and fill in
├── user_inputs/
│   ├── user_simulation_parameters.py
│   ├── user_sweep_parameters.py
│   └── user_materials.py           ← DEVICE modules only
├── <analysis_subdir>/
│   └── <analysis_script>.py
└── <render_script>.py              ← optional
```

### 2. Register the module in sim_registry.py

Add a `SimSpec` entry to the `SIMS` dict:

```python
"fdtd.my_new_module": SimSpec(
    key="fdtd.my_new_module",
    domain="FDTD",
    module="my_new_module",
    templates=["my_template.fsp"],
    figure_groups=["Transmission", "Fields"],
    create_lumerical_dir=False,
),
```

Keys follow the pattern `{domain_lowercase}.{module_name}` (e.g. `"fdtd.adiabatic_dc"`).

### 3. Add the setup call to every analysis script

```python
from project_layout import setup

spec, out, templates = setup("fdtd.my_new_module", __file__)
template_fsp = templates[0]
figures_dir = out["figure_groups"]["Transmission"]
```

### 4. Fill out README.md using README_TEMPLATE.md

At minimum complete: **Purpose**, **What this module does**, **Quick Start**,
**Folder Structure**, and **Status** sections.

### 5. Add an entry to the solver-level README

Add a `###` subsection for the new module in `FDTD/README.md`, `MODE/README.md`,
or `DEVICE/README.md` as appropriate.

---

## Code Style

### Function Naming

| Context | Convention | Rationale |
|---------|-----------|-----------|
| Analysis functions (`get*`, extraction/processing) | `camelCase` | Mirrors Lumerical's own API (`getdata`, `getresult`, `setnamed`) |
| Render / infrastructure functions | `snake_case` | Standard Python (e.g. `add_fde_region`, `waveguide_draw`) |
| Constants and module-level parameters | `UPPER_CASE` | PEP 8 convention |

**Do not rename existing functions.** Renaming would silently break scripts that
import them and provides no functional benefit.

### Docstring Standard

Use **Google-style** docstrings throughout. The canonical example is
`FDTD/adiabatic_directional_coupler/transmission/getFrequencyResponse.py`.

**Rule by function type:**

| Function type | Required docstring |
|---|---|
| Module-level (every `.py` file) | Short paragraph: what it computes, what monitors/data it uses |
| Functions with multiple parameters | Full `Args:` + `Returns:` blocks |
| Single-argument analysis functions | `Args:` + `Returns:` blocks (recommended) |
| Render functions (e.g. `waveguide_draw`) | One-liner summary is sufficient |
| `user_inputs/user_*.py` | Module-level comment + inline parameter annotations |

**Module-level docstring example:**

```python
"""
Extract the cross-port and through-port transmission spectra from FDTD monitors.

Monitors expected: ``cross_transmission``, ``through_transmission``, ``source``.
"""
```

**Function-level docstring example:**

```python
def getCrossResponse(fdtd):
    """Extract transmission response from FDTD monitors.

    Args:
        fdtd: FDTD simulation object from lumapi.

    Returns:
        tuple: (T1, T2, f) where T1 is the through-port transmission (ndarray),
            T2 is the bar-port transmission (ndarray), and f is the frequency
            array (ndarray).
    """
```

**Render function example:**

```python
def add_fde_region(mode):
    """Add and configure the FDE region and mesh in the MODE simulation."""
```

### Imports in user_inputs Files

`user_inputs/user_*.py` files are intentionally flat parameter namespaces.
Wildcard imports (`from module.user_inputs.user_parameters import *`) are a
deliberate design choice — they expose all parameters to analysis scripts without
requiring explicit listing. These are excluded from linting rules; do not
convert them to explicit imports.

### Line Length

Target **100 characters**. The linter is configured with `line-length = 100`.
Existing files that exceed this are grandfathered in via `extend-ignore = ["E501"]`.
Apply the limit to all new code.

---

## Running the Linter

```bash
ruff check .            # report all lint issues
ruff check . --fix      # auto-fix safe issues
ruff format .           # auto-format code style
```

Or via pre-commit on staged files only:

```bash
pre-commit run ruff
```

To run all hooks across the entire repo (useful after initial install):

```bash
pre-commit run --all-files
```

---

## Limitations

- **No automated test suite.** All simulation scripts require a running Lumerical
  license to execute. The CI pipeline runs linting only — it does not execute
  any simulation code.
- **Results directories are not tracked.** The `.gitignore` excludes all `Results/`
  directories. Only scripts and user inputs are version-controlled.
- **lumapi is not in requirements.txt.** It is a proprietary system dependency
  installed with Lumerical Design Suite and must be configured via `PYTHONPATH`
  as described in the setup section above.

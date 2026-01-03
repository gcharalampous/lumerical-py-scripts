"""Central registry for simulation modules (repo-local).

This repo intentionally keeps a "not-installed" workflow because scripts
operate on template Lumerical files stored inside the repository.

The registry provides a single place to define:
- domain: "FDTD" | "MODE" | "DEVICE"
- module folder name
- template file(s)
- figure group folders

No filesystem side effects are allowed in this file.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Sequence


@dataclass(frozen=True)
class SimSpec:
    key: str
    domain: str          # "FDTD" | "MODE" | "DEVICE"
    module: str          # e.g. "adiabatic_directional_coupler"
    templates: Sequence[str]
    figure_groups: Sequence[str]
    create_lumerical_dir: bool = False  # Whether to create Results/lumerical_files/




# Add modules here.
# FDTD
SIMS: Dict[str, SimSpec] = {
    # FDTD: Adiabatic directional coupler
    "fdtd.adiabatic_dc": SimSpec(
        key="fdtd.adiabatic_dc",
        domain="FDTD",
        module="adiabatic_directional_coupler",
        templates=["sbend_adiabatic_directional_coupler.fsp"],
        figure_groups=["Sweep Transmission", "Frequency Response", "E-fields"],
    ),
    # FDTD: Adiabatic Y-branch
    "fdtd.adiabatic_y_branch": SimSpec(
        key="fdtd.adiabatic_y_branch",
        domain="FDTD",
        module="adiabatic_y_branch",
        templates=["adiabatic_y_branch.fsp"],
        figure_groups=["Sweep Transmission", "Frequency Response", "E-fields"],
    ),
    # FDTD: Coupled ring coupler
    "fdtd.coupled_ring_coupler": SimSpec(
        key="fdtd.coupled_ring_coupler",
        domain="FDTD",
        module="coupled_ring_coupler",
        templates=["circular_bend_coupler.fsp", "racetrack_coupler.fsp"],
        figure_groups=["Sweep Transmission", "Frequency Response", "E-fields"],
    ),
}


def get_sim(key: str) -> SimSpec:
    """Return the SimSpec for a given key with a friendly error message."""
    try:
        return SIMS[key]
    except KeyError as e:
        available = ", ".join(sorted(SIMS.keys()))
        raise KeyError(f"Unknown sim key: {key}. Available keys: {available}") from e
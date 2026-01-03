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
    # FDTD: Directional coupler
    "fdtd.directional_coupler": SimSpec(
        key="fdtd.directional_coupler",
        domain="FDTD",
        module="directional_coupler",
        templates=["sbend_directional_coupler.fsp"],
        figure_groups=["Sweep Transmission", "Frequency Response", "E-fields"],
    ),
    # FDTD: Disk resonator coupler
    "fdtd.disk_resonator_coupler": SimSpec(
        key="fdtd.disk_resonator_coupler",
        domain="FDTD",
        module="disk_resonator_coupler",
        templates=["straight_disk_coupling_section.fsp", "coocentric_disk_coupling_section.fsp"],
        figure_groups=["Fields", "Index Profile", "Gap Sweep", "Transmission"],
    ),
    # FDTD: Ring resonator coupler
    "fdtd.ring_resonator_coupler": SimSpec(
        key="fdtd.ring_resonator_coupler",
        domain="FDTD",
        module="ring_resonator_coupler",
        templates=["straight_ring_coupling_section.fsp", "coocentric_ring_coupling_section.fsp", "rectangular_ring_coupling_section.fsp"],
        figure_groups=["Fields", "Index Profile", "Gap Sweep", "Length Sweep", "Transmission"],
    ),
}


def get_sim(key: str) -> SimSpec:
    """Return the SimSpec for a given key with a friendly error message."""
    try:
        return SIMS[key]
    except KeyError as e:
        available = ", ".join(sorted(SIMS.keys()))
        raise KeyError(f"Unknown sim key: {key}. Available keys: {available}") from e
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
    # FDTD: Edge coupler
    "fdtd.edge_coupler": SimSpec(
        key="fdtd.edge_coupler",
        domain="FDTD",
        module="edge_coupler",
        templates=["edge_taper.fsp"],
        figure_groups=["Fields", "Index Profile", "Tip Sweep", "Length Sweep", "Transmission"],
    ),
    # FDTD: Ring resonator coupler
    "fdtd.ring_resonator_coupler": SimSpec(
        key="fdtd.ring_resonator_coupler",
        domain="FDTD",
        module="ring_resonator_coupler",
        templates=["straight_ring_coupling_section.fsp", "coocentric_ring_coupling_section.fsp", "rectangular_ring_coupling_section.fsp"],
        figure_groups=["Fields", "Index Profile", "Gap Sweep", "Length Sweep", "Transmission"],
    ),
    # FDTD: Vertical taper
    "fdtd.vertical_taper": SimSpec(
        key="fdtd.vertical_taper",
        domain="FDTD",
        module="vertical_taper",
        templates=["vertical_taper.fsp"],
        figure_groups=["Fields", "Gap Sweep", "Index Profile", "Transmission"],
    ),
    # FDTD: Waveguide crossing
    "fdtd.waveguide_crossing": SimSpec(
        key="fdtd.waveguide_crossing",
        domain="FDTD",
        module="waveguide_crossing",
        templates=["waveguide_crossing_multi_wg_taper.fsp"],
        figure_groups=["Fields", "Index Profile", "Length Sweep", "Transmission"],
    ),
    # FDTD: Grating coupler 2D
    "fdtd.grating_coupler_2D": SimSpec(
        key="fdtd.grating_coupler_2D",
        domain="FDTD",
        module="grating_coupler_2D",
        templates=["grating_coupler_2D.fsp", "grating_coupler_bilayer_2D.fsp"],
        figure_groups=["Index Profile", "Sweep Functions", "Transmission"],
    ),
    # FDTD: Grating coupler rectangular 3D
    "fdtd.grating_coupler_rectangular_3D": SimSpec(
        key="fdtd.grating_coupler_rectangular_3D",
        domain="FDTD",
        module="grating_coupler_rectangular_3D",
        templates=["grating_coupler_rectangular_3D.fsp", "grating_coupler_rectangular_bilayer_3D.fsp"],
        figure_groups=["Fields", "Index Profile", "Sweep Functions", "Transmission"],
    ),
    # FDTD: Sub-wavelength grating
    "fdtd.swg_grating": SimSpec(
        key="fdtd.swg_grating",
        domain="FDTD",
        module="swg_grating",
        templates=["sub_wavelength_grating_layer_1.fsp", "sub_wavelength_grating_layer_2.fsp"],
        figure_groups=["Fields", "Index Profile", "Frequency Response"],
    ),
    # FDTD: MMI couplers
    "fdtd.mmi_couplers": SimSpec(
        key="fdtd.mmi_couplers",
        domain="FDTD",
        module="mmi_couplers",
        templates=["MMI_1x2.fsp", "MMI_2x2.fsp"],
        figure_groups=["Fields", "Index Profile", "Length Sweep", "Transmission"],
    ),
    # FDTD: Waveguide straight
    "fdtd.waveguide_straight": SimSpec(
        key="fdtd.waveguide_straight",
        domain="FDTD",
        module="waveguide_straight",
        templates=["straight_wg.fsp"],
        figure_groups=["Fields", "Mode Profile"],
    ),
    # FDTD: Waveguide mode taper
    "fdtd.waveguide_mode_taper": SimSpec(
        key="fdtd.waveguide_mode_taper",
        domain="FDTD",
        module="waveguide_mode_taper",
        templates=["mode_taper.fsp"],
        figure_groups=["Fields", "Index Profile", "Sweep Transmission"],
    ),
    # FDTD: Waveguide bend
    "fdtd.waveguide_bend": SimSpec(
        key="fdtd.waveguide_bend",
        domain="FDTD",
        module="waveguide_bend",
        templates=["circular_bend.fsp", "euler_bend.fsp"],
        figure_groups=["Fields", "Index Profile", "Sweep Transmission"],
    ),

    # ------------------------------------------------------------------ MODE
    # MODE: AWG Star Coupler
    "mode.awg_star_coupler": SimSpec(
        key="mode.awg_star_coupler",
        domain="MODE",
        module="awg_star_coupler",
        templates=["awg_input_taper.lms"],
        figure_groups=["Index Profile", "Far Field Profile"],
    ),
    # MODE: Butt Coupling
    "mode.butt_coupling": SimSpec(
        key="mode.butt_coupling",
        domain="MODE",
        module="butt_coupling",
        templates=["waveguide_1.lms", "waveguide_2.lms"],
        figure_groups=["Mode Profile", "Sweep Misalignment", "Sweep Width"],
        create_lumerical_dir=True,
    ),
    # MODE: Directional Coupler
    "mode.directional_coupler": SimSpec(
        key="mode.directional_coupler",
        domain="MODE",
        module="directional_coupler",
        templates=["waveguide_coupler.lms"],
        figure_groups=["Mode Profile", "Gap Sweep", "Length Sweep", "Dissimilar Waveguides"],
        create_lumerical_dir=True,
    ),
    # MODE: Edge Coupler
    "mode.edge_coupler": SimSpec(
        key="mode.edge_coupler",
        domain="MODE",
        module="edge_coupler",
        templates=[],
        figure_groups=["MFD Sweep", "Height Sweep"],
        create_lumerical_dir=True,
    ),
    # MODE: Laser Tapered Waveguide
    "mode.laser_tapered_waveguide": SimSpec(
        key="mode.laser_tapered_waveguide",
        domain="MODE",
        module="laser_tapered_waveguide",
        templates=["laser_taper_waveguide.lms"],
        figure_groups=["Mode Profile", "Index Profile", "Width Sweep"],
        create_lumerical_dir=True,
    ),
    # MODE: Sub-Wavelength Grating
    "mode.swg_grating": SimSpec(
        key="mode.swg_grating",
        domain="MODE",
        module="swg_grating",
        templates=["sub_wavelength_grating_layer_1.lms"],
        figure_groups=["Index Profile", "Frequency Response", "E-fields"],
    ),
    # MODE: Vertical Taper
    "mode.vertical_taper": SimSpec(
        key="mode.vertical_taper",
        domain="MODE",
        module="vertical_taper",
        templates=["taper_waveguide_layer1.lms", "taper_waveguide_layer2.lms"],
        figure_groups=["Neff Sweep"],
        create_lumerical_dir=True,
    ),
    # MODE: Waveguide
    "mode.waveguide": SimSpec(
        key="mode.waveguide",
        domain="MODE",
        module="waveguide",
        templates=[],
        figure_groups=["Index Profile", "Mode Profile", "Neff Sweep", "Radius Sweep",
                       "PIN Offset", "NP Density", "PCM"],
        create_lumerical_dir=True,
    ),

}





def get_sim(key: str) -> SimSpec:
    """Return the SimSpec for a given key with a friendly error message."""
    try:
        return SIMS[key]
    except KeyError as e:
        available = ", ".join(sorted(SIMS.keys()))
        raise KeyError(f"Unknown sim key: {key}. Available keys: {available}") from e
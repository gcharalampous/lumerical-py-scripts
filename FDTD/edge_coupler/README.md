# Edge Coupler (3D FDTD)

**Purpose:**  
This simulation models a 3D edge coupler (spot-size converter) designed to efficiently couple light between a fiber/PLC mode and an on-chip waveguide. The taper structure gradually transitions the mode profile and effective index to minimize insertion loss at the chip facet.


## What this module does

This module performs electromagnetic simulations of an edge coupler taper structure using the 3D FDTD computational method.

The simulation extracts:
- **Transmission frequency response**: Quantifies power coupling efficiency and spectral characteristics across the operating bandwidth
- **Electric field (E-field) distribution**: Maps the spatially-resolved electromagnetic field intensity and polarization state throughout the simulation domain
- **Refractive index profile**: Characterizes the spatial variation of the material's refractive index to validate the taper geometry

This analysis is essential for optimizing mode conversion efficiency and minimizing modal mismatch losses in chip-to-fiber coupling interfaces.


## Quick start
1. Set materials and dimensions in `user_inputs/lumerical_files/edge_taper.fsp` (cladding, core, box).
2. Run the scripts to generate results:
    - `python fields/getFields.py`
    - `python index_profile/index_profile_2D.py`
    - `python tip_sweep/getTipSweep.py`
    - `python length_sweep/getLengthSweep.py`
    - `python transmission/getFrequencyResponse.py`

3. Results will be saved automatically under:
   ```
   FDTD/Results/edge_coupler/Figures/
   ├── Fields/
   ├── Index Profile/
   ├── Tip Sweep/
   ├── Length Sweep/
   └── Transmission/
   ```



## Lumerical Template file

- `edge_taper.fsp` : Lumerical file that defines edge coupler


## Outputs

Results are saved automatically and may include:
- Electric field distributions at multiple cross-sections (xy and xz views)
- Refractive index profile maps (xy and xz views)
- Frequency-dependent transmission spectra (linear and dB scales)
- Back reflection estimates
- Tip width sweep results (linear and dB scales)
- Taper length sweep results (linear and dB scales)

Typical output location:

```
FDTD/Results/edge_coupler/Figures/
```


## Folder structure

```
edge_coupler/
├── fields/
│   └── getFields.py
├── index_profile/
│   └── index_profile_2D.py
├── length_sweep/
│   └── getLengthSweep.py
├── override_edge_coupler_region.py
├── override_fdtd_region.py
├── README.md
├── tip_sweep/
│   └── getTipSweep.py
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
    ├── lumerical_files/
    │   └── edge_taper.fsp
    └── user_simulation_parameters.py
```


## Notes
- Requires Lumerical installed and accessible via lumapi
- Scripts use `project_layout.py` for path management
- Designed to be run from the repository root
- Override scripts (`override_edge_coupler_region.py` and `override_fdtd_region.py`) can be used to programmatically modify simulation parameters


## Related modules
- [MODE/butt_coupling](../../MODE/butt_coupling/)
- [MODE/edge_coupler](../../MODE/edge_coupler/)
- [FDTD/vertical_taper](../vertical_taper/)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

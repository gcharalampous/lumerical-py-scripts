# Grating Coupler 2D (2D FDTD)

**Purpose:**  
This simulation models a 2D grating coupler designed to efficiently interface between optical fiber (Gaussian beam) and on-chip waveguides. The periodic grating structure enables efficient out-of-plane coupling with wavelength selectivity.


## What this module does

This module performs electromagnetic simulations of a 2D grating coupler structure using the 2D FDTD computational method.

The simulation extracts:
- **Transmission frequency response**: Quantifies coupling efficiency between fiber and waveguide across the operating bandwidth
- **Refractive index profile**: Visualizes the grating geometry and material structure
- **Parametric sweeps**: Optimizes fiber angle, fiber position, and grating fill factor for maximum coupling efficiency

This analysis is essential for designing efficient fiber-to-chip coupling interfaces in photonic integrated circuits.


## Quick start
1. Set materials and dimensions in `user_inputs/lumerical_files/`:
   - `grating_coupler_2D.fsp` (default)
   - `grating_coupler_bilayer_2D.fsp`
2. Choose which template to load via `file_index` in `user_inputs/user_simulation_parameters.py` (0 or 1). Other parameters stay inside the .fsp files.
3. Run the scripts to generate results:
    - `python transmission/getFrequencyResponse.py`
    - `python index_profile/index_profile_2D.py`
    - `python sweep_functions/getFiberAngle.py`
    - `python sweep_functions/getFiberPosition.py`
    - `python sweep_functions/getFillFactorSweep.py`

3. Results will be saved automatically under:
   ```
   FDTD/Results/grating_coupler_2D/Figures/
   ├── Index Profile/
   ├── Sweep Functions/
   └── Transmission/
   ```


## Analytical Design

- `analytical/1D_grating_coupler_design.ipynb` : Jupyter notebook for analytical grating coupler design calculations


## Lumerical Template files

- `grating_coupler_2D.fsp` : Standard 2D grating coupler structure
- `grating_coupler_bilayer_2D.fsp` : Bilayer 2D grating coupler variant


## Outputs

Results are saved automatically and may include:
- Transmission spectra showing grating coupling efficiency (linear and dB scales)
- Refractive index profile plots (xy view)
- Back reflection estimates
- Fiber angle sweep results
- Fiber position sweep results
- Fill factor sweep results

Typical output location:

```
FDTD/Results/grating_coupler_2D/Figures/
```


## Folder structure

```
grating_coupler_2D/
├── analytical/
│   └── 1D_grating_coupler_design.ipynb
├── index_profile/
│   └── index_profile_2D.py
├── README.md
├── sweep_functions/
│   ├── getFiberAngle.py
│   ├── getFiberPosition.py
│   └── getFillFactorSweep.py
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
    ├── lumerical_files/
    │   ├── grating_coupler_2D.fsp
    │   └── grating_coupler_bilayer_2D.fsp
    └── user_simulation_parameters.py
```


## Notes
- Requires Lumerical installed and accessible via lumapi
- Scripts use `project_layout.py` for path management
- Designed to be run from the repository root
- The analytical design notebook provides theoretical guidance for grating coupler parameters
- Sweep scripts have commented-out `runsweep()` calls to avoid accidental long-running simulations


## Related modules
- [FDTD/grating_coupler_rectangular_3D](../grating_coupler_rectangular_3D/)
- [MODE/swg_grating](../../MODE/swg_grating/)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

# Grating Coupler Rectangular 3D (3D FDTD)

**Purpose:**  
Simulates a 3D rectangular grating coupler that interfaces between optical fiber (Gaussian beam) and on-chip waveguides. The periodic grating structure enables efficient out-of-plane coupling with wavelength selectivity.


## What this module does
Models the rectangular grating coupler in 3D FDTD and extracts:
- Transmission vs. wavelength (coupling efficiency)
- Refractive index profiles to visualize grating geometry
- Field profiles showing mode coupling and grating interaction
- Sweeps for beam angle, fiber position, and fill factor optimization


## Quick start
1. Go to `user_inputs/lumerical_files/` and set materials and dimensions in the grating coupler `grating_coupler_rectangular_3D.fsp` file.
2. (Optional) Adjust overrides in `user_simulation_parameters.py` following the inline notes, then uncomment override calls in the scripts if needed.
3. Run the scripts to generate results:
   - `transmission/getFrequencyResponse.py`
   - `index_profile/index_profile_2D.py`
   - `sweep_functions/getFiberAngle.py`
   - `sweep_functions/getFiberPosition.py`
   - `sweep_functions/getFillFactorSweep.py`
   - `analytical/1D_grating_coupler_design.ipynb` (Jupyter notebook for analytical design)
4. Results save to `FDTD/Results/grating_coupler_rectangular_3D/`.


## Rendering scripts

- `override_grating_coupler_region.py`: Override the grating coupler device
- `override_fdtd_region.py`: Override the fdtd simulation settings

These scripts are used for rendering and you are not required to directly run them


## Inputs

Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- grating period and fill factor
- grating depth and width
- material properties
- fiber angle and position
- wavelength or frequency settings
- sweep definitions


## Outputs

Results are saved automatically and may include:
- Transmission spectra showing grating coupling efficiency
- Refractive index profile plots
- Field plots showing fiber-to-chip coupling
- Sweep data for fiber angle, position, and fill factor optimization
- Analytical design calculations from Jupyter notebook


Typical output location:

```
FDTD/Results/grating_coupler_rectangular_3D/
```


## Folder structure

```
grating_coupler_rectangular_3D/
├── analytical/
│   └── 1D_grating_coupler_design.ipynb
├── index_profile/
│   └── index_profile_2D.py
├── sweep_functions/
│   ├── getFiberAngle.py
│   ├── getFiberPosition.py
│   └── getFillFactorSweep.py
├── override_fdtd_region.py
├── override_grating_coupler_region.py
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
   ├── lumerical_files/
   │   └── *.fsp
   └── user_simulation_parameters.py
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root
- The analytical design notebook provides theoretical guidance for grating coupler parameters


## Related modules

- [FDTD/grating_coupler_2D](../grating_coupler_2D/README.md)
- [MODE/swg_grating](../../MODE/swg_grating/README.md)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

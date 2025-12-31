# 2D Waveguide Simulations (MODE Solutions)

**Purpose:**  
This module serves as a general waveguide analysis toolbox used across multiple device families.

## What this module does
  This module provides a comprehensive suite of tools for analyzing 2D waveguide behavior in MODE Solutions:

  - Visualizes mode profiles across diverse waveguide configurations.
  - Analyzes effective index variations based on waveguide dimensions (width and height).
  - Models absorption losses attributed to metal layers and free carriers in waveguides.
  - Estimates the Q-factor and Free Spectral Range (FSR) for racetrack resonators.
  - Assesses losses in straight-to-bend waveguide transitions.
  - Determines confinement factors in Phase Change Materials (PCM).

  These capabilities enable detailed characterization of waveguide performance across multiple design parameters and operating conditions.


## Quick start

1. After downloading the repository, navigate through the `waveguide/user-inputs` directory.
2. Edit the `user_materials.py` to define the simulation materials for the cladding, core, box, and substrate layers. Follow the instructions written in the file.
3. Edit the `user_simulation_parameters.py` to define the simulation properties, region and structure dimensions. Follow the instructions written in the file. If you would like to do a sweep, modify the `user_sweep_parameters/py`.
4. Navigate under the `waveguide/mode_profile` or `waveguide/neff_sweep` directories to run the desired python file.


## Rendering scripts

- `fde_region.py` : Setting up the FDE simulation region
- `waveguide_render.py` : Setting up the waveguide geometry

These scripts are used for rendering and you are not required to directly run them

## Inputs

Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- material properties
- geometry and simulation parameters
- sweep definitions

## Outputs

Results are saved automatically and may include:
- mode profiles or field plots
- figures for quick inspection
- CSV data file for Lumerical Device

Typical output location:

```
MODE/Results/waveguide/
```


## Folder structure

````
MODE/waveguide/
├── fde_region.py
├── index_profile
│   └── get_index_mesh_2D.py
├── mode_profile
│   ├── mode_profile_1D.py
│   └── mode_profile_2D.py
├── neff_sweep
│   ├── neff_height_sweep_2D.py
│   ├── neff_height_sweep_variations_2D.py
│   ├── neff_width_sweep_2D.py
│   └── neff_width_sweep_variations_2D.py
├── np_density_sweep
│   └── voltage_sweep_2D.py
├── pcm
│   └── confinement_factor.py
├── pin_offset_sweep
│   └── loss_offset_sweep_2D.py
├── radius_sweep
│   ├── overlap_radius_sweep_2D.py
│   └── Q_factor_radius_sweep_2D.py
├── README.md
├── user_inputs
│   ├── user_materials.py
│   ├── user_simulation_parameters.py
│   └── user_sweep_parameters.py
└── waveguide_render.py

````


## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root


# Related modules

- [FDTD/waveguide](../../FDTD/waveguide_straight/)


## Status

- [ ] Verified
- [x] Actively used
- [ ] Legacy or reference

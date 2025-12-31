# 2D Electro-Optic (DEVICE)

**Purpose:**  
This module models a Pockels electro-optic modulator to study electric-field-induced refractive index changes and their effect on optical transmission. The simulation quantifies the electro-optic coefficient and modulation efficiency under applied voltage.


## What this module does

This module simulates a Pockels electro-optic modulator using Lumerical DEVICE electrostatics solvers.
- Calculates the electric field distribution in the modulator under applied voltage
- Computes the resulting refractive index changes via the electro-optic effect
  
The workflow integrates electrostatic analysis (2D field and index mapping) with optical mode solving to characterize device performance.

## Quick start
1. After downloading the repository, navigate through the `electro-optic/user_inputs/` directory.
2. Edit the `user_inputs/user_materials.py` and `user_inputs/user_simulation_parameters.py` to define the simulation materials for the cladding, core, box, and substrate layers. Follow the instructions written in the file.
3.  Run scripts in these directories to generate results:
    -  `electrostatics/`
    -  `mode_profile/`


## Rendering scripts
- `charge_region.py` : Renders the charge simulation region
- `waveguide_render.py` : Renders the PIN modulator structure

These scripts are used for rendering and you are not required to directly run them


## Inputs

Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- geometry parameters
- charge region properties


## Outputs
Results are saved automatically and may include:
- Electrostatic Fields
- Refractive index changes
- mode profiles or field plots


Typical output location:

```
DEVICE/Results/electro-optic/
```


## Folder structure

```
electro_optic/
├── charge_region.py
├── electrostatics
│   ├── get_Efield_static_2D.py
│   └── get_index_change_2D.py
├── feem_region.py
├── mode_profile
│   └── mode_index.py
├── user_inputs
│   ├── user_materials.py
│   └── user_simulation_parameters.py
└── waveguide_render.py

```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

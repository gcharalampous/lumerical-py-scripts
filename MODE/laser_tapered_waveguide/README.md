# 2D Laser Tapered Waveguide Simulations (MODE Solutions)

**Purpose:**
This module analyzes the optical confinement of a laser tapered waveguide as the width changes.

## What this module does
This module provides three core workflows for the tapered laser waveguide structure:

- Generates the index mesh for the Lumerical model.
- Plots the mode profile for the supported modes.
- Sweeps waveguide width and computes confinement to the waveguide and active region.

## Quick start
1. Open `laser_tapered_waveguide/user_inputs/lumerical_files/laser_taper_waveguide.lms`.
2. Edit `user_inputs/user_sweep_parameters.py` to define the mode count and sweep ranges.
3. Run the scripts in `index_profile/`, `mode_profile/`, or `width_sweep/` depending on the result you need.

## Lumerical template
- `laser_taper_waveguide.lms` : Lumerical template used by the MODE scripts

## Inputs
Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- Lumerical template files
- sweep definitions

## Outputs
Results are saved automatically and may include:
- index profile figures
- mode profile figures
- confinement-factor sweep plots

Typical output location:

```
MODE/Results/laser_tapered_waveguide/
```

## Folder structure

```
laser_tapered_waveguide/
├── OpticalConfinement.py
├── index_profile
│   └── get_index_mesh_2D.py
├── mode_profile
│   └── mode_profile_2D.py
├── user_inputs
│   ├── lumerical_files
│   │   └── laser_taper_waveguide.lms
│   └── user_sweep_parameters.py
└── width_sweep
    └── width_sweep_confinement.py
```

## Notes

- Requires Lumerical installed and accessible via lumapi
- Designed to be run from the repository root

## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

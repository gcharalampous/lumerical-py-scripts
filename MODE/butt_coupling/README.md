# 2D Butt-Coupling Simulations (MODE Solutions)

**Purpose:**  
This simulation helps analyze how light couples between two waveguides. It focuses on mode interactions and improving device performance in butt-coupling configurations for photonic devices.


## What this module does

This module simulates a butt-coupling device using the MODE simulation domain. It analyzes coupling efficiency between two waveguides by:

- Extracting mode profiles from both waveguides
- Calculating transmission characteristics from the overlap integral between modes
- Examining misalignment effects on coupling performance
- Optimizing device performance by varying waveguide width

The analysis focuses on mode interactions and identifying potential losses during the coupling process.



## Quick start
1. Navigate to `butt_coupling/user_inputs/` and edit `waveguide_1.lms` and `waveguide_2.lms` to define waveguide properties (materials and dimensions).
2. Edit `user_simulation_parameters.py` to set simulation properties (number of modes, mode order to overlap).
3. Edit `user_sweep_parameters.py` to define sweep parameters (width of `waveguide_2.lms` and misalignment axis).
4. Run `mode_profile/mode_profile_2D.py` to extract modes from each waveguide.
5. Run `overlap_mode/overlap_mode_integral_2D.py` to calculate the overlap integral between mode orders.
6. Run `overlap_profile_sweep/overlap_misalignment_integral_2D.py` or `overlap_profile_sweep/overlap_width_sweep_2D.py` to sweep over misalignment or width dimensions.



## Lumerical Templates and Rendering

- `waveguide_1.lms` : Lumerical template for waveguide-1
- `waveguide_2.lms` : Lumerical template for waveguide-2
- `fde_region.py` : Setting the FDE simulation region (this script is used for rendering only)



## Inputs

Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- geometry and material parameters
- simulation region settings
- sweep definitions
- Lumerical template files


## Outputs

Results are saved automatically and may include:
- Mode overlap integrals
- Coupling efficiency versus misalignment and geometry

Typical output location:

```
MODE/Results/butt_coupling
```


## Folder structure

```
    butt_coupling/
    ├── fde_region.py
    ├── mode_profile
    │   └── mode_profile_2D.py
    ├── overlap_mode
    │   └── overlap_mode_integral_2D.py
    ├── overlap_profile_sweep
    │   ├── overlap_misalignment_integral_2D.py
    │   └── overlap_width_sweep_2D.py
    ├── README.md
    └── user_inputs
        ├── lumerical_files
        │   ├── waveguide_1.lms
        │   └── waveguide_2.lms
        ├── user_simulation_parameters.py
        └── user_sweep_parameters.py
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in project_layout.py
- Designed to be run from the repository root


## Status

- [ ] Verified
- [x] Actively used
- [ ] Legacy or reference

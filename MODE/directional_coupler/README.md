# 2D Directional Coupler (MODE Solutions)

**Purpose:**  
This module is used to efficiently extract supermode indices required to compute coupling length without full 3D propagation simulations.


## What this module does
This module analyzes coupling behavior between parallel waveguides by computing supermode profiles and determining optimal gap spacing and coupling length for directional coupler design using MODE's efficient eigenmode solver.


## Simulation Setup
1. Configure the Lumerical template (`waveguide_coupler.lms`): set materials, geometry, and layers
2. Edit `user_simulation_parameters.py` and `user_sweep_parameters.py` with your simulation settings
3. Run the analysis scripts: `mode_profile_2D.py`, `coupling_length.py`, `coupling_gap.py`
4. The standard `coupling_sweep` analysis assumes phase-matched waveguides (identical dimensions and materials). For waveguides with different widths, use `dissimilar_waveguides/coupling_length.py` instead.


## Rendering scripts
- `waveguide_coupler.lms` : Lumerical file that defines the coupling waveguides
- `even_odd_mode_profile` : Gets the supermode profile

These scripts are used for rendering and you are not required to directly run them


## Inputs
Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- geometry parameters
- material properties
- simulation region settings
- sweep definitions


## Outputs
Results are saved automatically and may include:
- coupling as a function of the length and gap
- mode profiles or field plots

Typical output location:

```
MODE/Results/directional_coupler/
```


## Folder structure
```
directional_coupler/
├── coupling_sweep
│   ├── coupling_gap.py
│   └── coupling_length.py
├── dissimilar_waveguides
│   └── coupling_length.py
├── even_odd_mode_profile.py
├── mode_profile
│   └── mode_profile_2D.py
├── README.md
└── user_inputs
    ├── lumerical_files
    │   └── waveguide_coupler.lms
    ├── user_simulation_parameters.py
    └── user_sweep_parameters.py
```        


## Notes
- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root


## Related modules

- [FDTD/directional_coupler](../../FDTD/directional_coupler/)



## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

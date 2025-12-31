# 2D Edge-Coupler Simulations (MODE Solutions)

**Purpose:**  
This module focuses on fiber or free-space Gaussian beam coupling and does not model on-chip laser mode evolution.


## What this module does
This simulation evaluates the coupling efficiency between a Gaussian beam and waveguide modes by analyzing their overlap integral.
- Evaluates overlap between Gaussian beam and waveguide mode profiles.
- Examines coupling efficiency as a function of Gaussian beam Mode-Field Diameter (MFD).
- Analyzes the impact of waveguide thickness on overlap efficiency.


## Quick start
1. After downloading the repository, navigate through the `edge_coupler/user_inputs/` directory.
2. Edit the parameter file `gausian_beam_parameters.py` to define the Gaussian beam parameter properties (i.e. waist-radius, index, sample span, etc). 
3. Edit the `user_inputs/user_materials.py` and `user_inputs/user_simulation_parameters.py` to define the simulation materials for the cladding, core, box, and substrate layers. Follow the instructions written in the file.
4. Then define the in `user_inputs/user_sweep_parameters.py` the sweep parameters.
5. Run the `overlap_profile_sweep/overlap_profile_sweep_2D.py` Python file and get the overlap integral results.


## Rendering scripts
- `fde_region.py` : renders the FDE simulation region
- `gaussian_beam_render.py` : renders the Gaussian beam
- `waveguide_render.py` : renders the waveguide geometry

These scripts are used for rendering and you are not required to directly run them


## Inputs
Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- Gaussian beam parameters
- geometry and material parameters
- simulation region settings
- sweep definitions


## Outputs
Results are saved automatically and may include:
- Overlap Integral plots

Typical output location:

```
MODE/Results/edge_coupler/
```

## Folder structure
```
    edge_coupler
    ├── fde_region.py
    ├── gaussian_beam_render.py
    ├── overlap_profile_sweep
    │   └── overlap_width_sweep_2D.py
    ├── README.md
    ├── user_inputs
    │   ├── gaussian_beam_parameters.py
    │   ├── user_materials.py
    │   ├── user_simulation_parameters.py
    │   └── user_sweep_parameters.py
    └── waveguide_render.py

```


## Notes
- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root


## Related modules
- [FDTD/edge_coupler](../../FDTD/edge_coupler/)


## Status
- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

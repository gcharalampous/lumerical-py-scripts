# 2D Verttical Taper Simulations (MODE Solutions)

**Purpose:**  
Effective index evolution is used to assess adiabatic taper behavior and guide taper length selection. The following module provides capabilities for analyzing vertical taper structures in photonics.


## What this module does

Calculates the crossing length of a vertical taper, defined as the taper length where the effective indices of the bottom and upper layers are equal. This crossing point indicates where light couples from the bottom to the upper layer or vice versa.


- Computes the effective refractive index variation as a function of taper length for vertically tapered waveguide structures.
- Sweeps across taper geometries and plots the resulting effective index for each layer.
- Enables optimization of taper designs through detailed analysis.
- Provides visualization tools to analyze coupling efficiency between layers.


This module accurately determines the crossing length where effective indices of layers are equal, enables layer-to-layer coupling analysis through effective index calculations.


## Quick start

1. After downloading the repository, navigate through the `vertical_taper/user_inputs/lumerical_files` directory.
2. Edit the two lumerical files `taper_waveguide_layer1.lms` and `taper_waveguide_layer2.lms` to define the simulation materials for the cladding, core, and box layers along with their dimensions. 
3. Edit the `user_sweep_parameters.py` to define the simulation sweep parameters. Follow the comment-sections written in the file.
4. Run the files in the `vertical_taper/neff_sweep` directory and get the results.



## Lumerical Template file

- `taper_waveguide_layer1.lms` : Lumerical file that defines i.e. the bottom layer
- `taper_waveguide_layer2.lms` : Lumerical file that defines i.e. the upper layer



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
- figures for quick inspection

Typical output location:

```
MODE/Results/vertical_taper/
```


## Folder structure

```
vertical_taper/
├── neff_sweep
│   └── neff_width_sweep_2D.py
└── user_inputs
    ├── lumerical_files
    │   ├── taper_waveguide_layer1.lms
    │   └── taper_waveguide_layer2.lms
    └── user_sweep_parameters.py
```

## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root


## Related modules

- [FDTD/vertical_taper](../../FDTD/vertical_taper/)



## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

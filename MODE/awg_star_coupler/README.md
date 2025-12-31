# 2D AWG Star Coupler Simulations (MODE Solutions)

**Purpose:**  
This module simulates the aperture profile of a 2D star coupler using Lumerical MODE solutions. A star coupler is a key component in Arrayed Waveguide Grating (AWG) devices that distributes light from input waveguides to an array of output waveguides.



## What this module does

- Aperture Profile Analysis: Calculates and visualizes the electromagnetic field distribution at the aperture plane of the star coupler.


## Quick start

1. Navigate to `awg_star_coupler/user_inputs/lumerical_files`
2. Edit `awg_input_taper.lms` to set material properties and taper dimensions
3. Run `apperture_profile_2D.py` to compute and visualize the aperture field profile



## Lumerical Template file

- `awg_input_taper.lms` : Lumerical file that defines the awg input star coupler section.


## Inputs

Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- Lumerical template file `awg_input_taper.lms`


## Outputs

Results are saved automatically and may include:
- Simulations of the aperture profile of a 2D star coupler.

Typical output location:

```
MODE/Results/awg_star_coupler/
```


## Folder structure

```
awg_star_coupler/
├── mode_field_profile
│   ├── apperture_profile_2D.py
│   └── get_index_mesh_2D.py
├── README.md
└── user_inputs
    └── lumerical_files

```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root




## Status

- [X] Verified
- [ ] Actively used
- [ ] Legacy or reference

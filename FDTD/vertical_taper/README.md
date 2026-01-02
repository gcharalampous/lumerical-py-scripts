# Vertical Taper (3D FDTD)

**Purpose:**  
This simulation models a 3D vertical taper structure designed to efficiently couple light between waveguides of different gaps or cross-sectional dimensions. The vertical taper gradually transitions the mode profile and effective index between input and output waveguides.


## What this module does

This module performs electromagnetic simulations of a vertical taper waveguide structure using the 3D FDTD computational method. 

The simulation extracts:
- **Transmission frequency response**: Quantifies power coupling efficiency and spectral characteristics across the operating bandwidth
- **Electric field (E-field) distribution**: Maps the spatially-resolved electromagnetic field intensity and polarization state throughout the simulation domain
- **Refractive index profile**: Characterizes the spatial variation of the material's refractive index to validate the tapered waveguide geometry

This analysis is essential for optimizing mode conversion efficiency and minimizing modal mismatch losses in integrated photonic waveguide transitions.


## Quick start
1. Go to `vertical_taper/user_inputs/lumerical_files/`.
2. Set materials and dimensions in `vertical_taper.fsp` (cladding, core, box).
3. (Optional) Update overrides in `user_simulation_parameters.py` by following the inline notes, then uncomment override calls in the scripts.
4. Run the scripts to generate results:
    - `fields/`
    - `index_profile/`
    - `transmission/`



## Lumerical Template file

- `vertical_taper.fsp` : Lumerical file that defines vertical taper


## Inputs

Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- geometry parameters
- material properties
- wavelength or frequency settings
- sweep definitions


## Outputs

Results are saved automatically and may include:
- Frequency-dependent power transmission
- Spatial field distributions at input, output, and intermediate planes

Typical output location:

```
FDTD/Results/vertical_taper/
```


## Folder structure

```
vertical_taper/
├── fields
│   └── getFields.py
├── index_profile
│   └── index_profile_2D.py
├── override_fdtd_region.py
├── override_vertical_taper_region.py
├── README.md
├── transmission
│   └── getFrequencyResponse.py
└── user_inputs
    ├── lumerical_files
    └── user_simulation_parameters.py

```


## Notes
- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root


## Related modules
- [MODE/vertical_taper](../../MODE/vertical_taper/)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

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
1. Set materials and dimensions in `user_inputs/lumerical_files/vertical_taper.fsp` (cladding, core, box).
2. Run the scripts to generate results:
    - `python fields/getFields.py`
    - `python gap_sweep/getGapSweep.py`
    - `python index_profile/index_profile_2D.py`
    - `python transmission/getFrequencyResponse.py`

3. Results will be saved automatically under:
   ```
   FDTD/Results/vertical_taper/Figures/
   ├── Fields/
   ├── Gap Sweep/
   ├── Index Profile/
   └── Transmission/
   ```



## Lumerical Template file

- `vertical_taper.fsp` : Lumerical file that defines vertical taper


## Outputs

Results are saved automatically and may include:
- Electric field distributions at multiple cross-sections (xy-top, xy-bottom, xz)
- Refractive index profile maps (xy and xz views)
- Frequency-dependent transmission spectra (linear and dB scales)
- Back reflection estimates

Typical output location:

```
FDTD/Results/vertical_taper/Figures/
```


## Folder structure

```
vertical_taper/
├── fields/
│   └── getFields.py
├── gap_sweep/
│   └── getGapSweep.py
├── index_profile/
│   └── index_profile_2D.py
├── README.md
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
    └── lumerical_files/
        └── vertical_taper.fsp
```


## Notes
- Requires Lumerical installed and accessible via lumapi
- Scripts use `project_layout.py` for path management
- Designed to be run from the repository root


## Related modules
- [MODE/vertical_taper](../../MODE/vertical_taper/)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

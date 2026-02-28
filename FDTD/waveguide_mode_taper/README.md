# Waveguide Mode Taper (3D FDTD)

**Purpose:**  
This simulation models a 3D waveguide mode taper structure designed to efficiently transition light between waveguides of different widths. The taper gradually converts the mode profile to minimize insertion loss and back-reflection.


## What this module does

This module performs electromagnetic simulations of a waveguide mode taper structure using the 3D FDTD computational method.

The simulation extracts:
- **Electric field (E-field) distribution**: Maps the spatially-resolved electromagnetic field intensity through the taper (top-view and side-view)
- **Transmission vs. taper length**: Sweeps taper length to find the optimal adiabatic transition
- **Transmission vs. output width**: Sweeps the output waveguide width to characterize mode conversion efficiency


## Quick start
1. Set materials and dimensions in `user_inputs/lumerical_files/mode_taper.fsp`.
2. Run the scripts to generate results:
    - `python fields/getFields.py`
    - `python sweep_transmission/sweep_length_transmission.py`
    - `python sweep_transmission/sweep_width_transmission.py`

3. Results will be saved automatically under:
   ```
   FDTD/Results/waveguide_mode_taper/Figures/
   ├── Fields/
   └── Sweep Transmission/
   ```


## Lumerical Template file

- `mode_taper.fsp` : Lumerical file that defines the waveguide mode taper


## Outputs

Results are saved automatically and may include:
- Electric field distributions (xy top-view, xz side-view)
- Transmission vs. taper length sweep plots
- Transmission vs. output width sweep plots

Typical output location:

```
FDTD/Results/waveguide_mode_taper/Figures/
```


## Folder structure

```
waveguide_mode_taper/
├── fields/
│   └── getFields.py
├── README.md
├── sweep_transmission/
│   ├── sweep_length_transmission.py
│   └── sweep_width_transmission.py
└── user_inputs/
    └── lumerical_files/
        └── mode_taper.fsp
```


## Notes
- Requires Lumerical installed and accessible via lumapi
- Scripts use `project_layout.py` for path management
- Designed to be run from the repository root


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

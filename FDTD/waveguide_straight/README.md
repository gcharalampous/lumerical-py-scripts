# Straight Waveguide (3D FDTD)

**Purpose:**  
This simulation models a 3D straight waveguide to characterize its propagation mode profile and electric field distribution. It is useful for verifying waveguide confinement, mode shape, and propagation behaviour before integrating into more complex photonic circuits.


## What this module does

This module performs electromagnetic simulations of a straight waveguide structure using the 3D FDTD computational method.

The simulation extracts:
- **1D mode profiles**: Slices of the electric field along the y-direction and z-direction to characterize mode confinement
- **2D E-field distributions**: Top-view (xy), side-view (xz), and cross-section (yz) maps of the electromagnetic field intensity throughout the waveguide


## Quick start
1. Set materials and dimensions in `user_inputs/lumerical_files/straight_wg.fsp` (cladding, core, box, substrate).
2. Run the script to generate results:
    - `python propagation_mode/mode_profile.py`

3. Results will be saved automatically under:
   ```
   FDTD/Results/waveguide_straight/Figures/
   ├── Fields/
   └── Mode Profile/
   ```


## Lumerical Template file

- `straight_wg.fsp` : Lumerical file that defines the straight waveguide


## Outputs

Results are saved automatically and may include:
- 1D mode profile slices (linear-y and linear-z)
- Electric field distributions at multiple views (xy top-view, xz side-view, yz cross-section)

Typical output location:

```
FDTD/Results/waveguide_straight/Figures/
```


## Folder structure

```
waveguide_straight/
├── propagation_mode/
│   └── mode_profile.py
├── README.md
└── user_inputs/
    └── lumerical_files/
        └── straight_wg.fsp
```


## Notes
- Requires Lumerical installed and accessible via lumapi
- Scripts use `project_layout.py` for path management
- Designed to be run from the repository root


## Related modules
- [MODE/waveguide](../../MODE/waveguide/)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

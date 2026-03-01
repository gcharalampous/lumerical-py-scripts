# Waveguide Bend (3D FDTD)

**Purpose:**  
This simulation models bent waveguide sections and evaluates bend-induced loss for different bend radii.


## What this module does

This module performs electromagnetic simulations of waveguide bends using 3D FDTD.

The simulation extracts:
- **Propagation mode fields**: Top-view and output cross-section E-field profiles
- **Refractive index profiles**: Top-view and cross-section index maps
- **Transmission vs. bend radius**: Sweeps bend radius and evaluates total and fundamental mode transmission


## Quick start
1. Set materials and dimensions in either:
    - `user_inputs/lumerical_files/circular_bend.fsp`
    - `user_inputs/lumerical_files/euler_bend.fsp`
2. Set template selection in `user_inputs/user_simulation_parameters.py`.
3. Run the scripts:
    - `python fields/mode_profile.py`
    - `python index_profile/index_profile_2D.py`
    - `python sweep_transmission/sweep_radius_transmission.py`

4. Results will be saved automatically under:
    ```
    FDTD/Results/waveguide_bend/Figures/
    ├── Fields/
    ├── Index Profile/
    └── Sweep Transmission/
    ```


## Lumerical Template files

- `circular_bend.fsp` : Circular bend waveguide template
- `euler_bend.fsp` : Euler bend waveguide template


## Outputs

Results are saved automatically and may include:
- E-field distribution plots for propagation mode
- Refractive index profile plots (xy and xz)
- Transmission vs. bend radius (linear and dB)

Typical output location:

```
FDTD/Results/waveguide_bend/Figures/
```


## Folder structure

```
waveguide_bend/
├── fields/
│   └── mode_profile.py
├── index_profile/
│   └── index_profile_2D.py
├── README.md
├── sweep_transmission/
│   └── sweep_radius_transmission.py
└── user_inputs/
    ├── user_simulation_parameters.py
     └── lumerical_files/
          ├── circular_bend.fsp
          └── euler_bend.fsp
```


## Notes
- Requires Lumerical installed and accessible via lumapi
- Scripts use `project_layout.py` for path management
- Current scripts default to `circular_bend.fsp`; switch the template index in scripts if needed


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

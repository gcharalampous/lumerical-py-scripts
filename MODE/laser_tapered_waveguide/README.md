# 2D Laser Tapered Waveguide (MODE Solutions)

**Purpose:**  
Calculates optical confinement characteristics of a tapered laser waveguide as the width progressively narrows. Tracks how optical modes behave when vertically displaced and determines how tapering affects mode distribution and confinement efficiency. Enables optimization of laser waveguide geometry for improved optical performance.

## What this module does
This module calculates the optical confinement characteristics of a laser tapered waveguide structure. It analyzes how optical modes are distributed and confined when the waveguide geometry is modified through tapering.

- **Passive Waveguide**: A guiding layer that passively confines light
- **Active Waveguide**: A laser-active layer responsible for optical amplification

This modules calculates the optical confnment of a laser tapered waveguide. The template consinst of a waveguide layer that guides the light and the laser waveguide 


## Quick start
1. Navigate to `laser_tapered_waveguide/user_inputs/lumerical_files/`
2. Edit `laser_taper_waveguide.lms` to define simulation materials (cladding, core, box) and their dimensions
3. Edit `user_sweep_parameters.py` and follow the inline comments to configure sweep simulation parameters
4. Run scripts in these directories to generate results:
   - `laser_tapered_waveguide/width_sweep/`

## Lumerical template
- `laser_taper_waveguide.lms` : Lumerical file that defines the laser taper device


## Inputs
Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- geometry and simulation parameters
- wavelength or frequency settings
- sweep definitions


## Outputs
Results are saved automatically and may include:
- Optical mode profiles in tapered geometry
- Confinement factors as a function of waveguide width
- Modal shift and overlap with active region


Typical output location:

```
MODE/Results/laser_tapered_waveguide/
```


## Folder structure

```
laser_tapered_waveguide/
├── index_profile
│   └── get_index_mesh_2D.py
├── mode_profile
│   └── mode_profile_2D.py
├── OpticalConfinement.py
├── __pycache__
│   └── OpticalConfinement.cpython-39.pyc
├── user_inputs
│   ├── lumerical_files
│   ├── __pycache__
│   └── user_sweep_parameters.py
└── width_sweep
    └── width_sweep_confinement.py
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

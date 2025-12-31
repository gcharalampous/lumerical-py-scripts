# 2D Disk High-Speed Modulator (DEVICE)

**Purpose:**  
   This module models a high-speed PN junction optical modulator to study carrier-induced refractive index and absorption changes under electrical bias. The simulation quantifies the optoelectronic modulation efficiency and frequency response of the PN junction.


## What this module does
This module simulates a 2D PN high-speed optical modulator to analyze how electrical bias affects light propagation. It performs the following calculations:

- Charge distribution across the junction
- PN junction properties (e.g., width, capacitance)
- RC time constant over a voltage sweep (DC & AC)

By sweeping the bias voltage, the simulation characterizes key modulator performance metrics including modulation speed and response time.


## Quick start
1. After downloading the repository, navigate through the `disk_modulator/user_inputs/` directory.
2. Edit the `user_inputs/user_materials.py` and `user_inputs/user_simulation_parameters.py` to define the simulation materials for the cladding, core, box, and substrate layers. Follow the instructions written in the file.
3. Then define in `user_inputs/user_sweep_parameters.py` the sweep parameters.
4.  Run scripts in these directories to generate results:
    -  `ac_sweep/`
    -  `analyrical_calculations/`
    -  `charge_distribution/`
    -  `dc_sweep/`


## Rendering scripts
- `charge_region.py` : Renders the charge simulation region
- `waveguide_render.py` : Renders the PIN modulator structure

These scripts are used for rendering and you are not required to directly run them


## Inputs
Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- geometry parameters
- charge region properties
- sweep definitions


## Outputs
Results are saved automatically and may include:
- Capacitance (theoretical and simulated)
- Charge distribution across the junction
- AC & DC capacitance and resistance for forward and reverse bias

Typical output location:

```
DEVICE/Results/disk_modulator/
```


## Folder structure

```
disk_modulator/
├── ac_sweep
│   └── getAC_RC.py
├── analytical_calculations
│   └── capacitance_analytical.py
├── charge_distribution
│   ├── get_band_potential.py
│   ├── get_charge_1D.py
│   └── get_junction_width.py
├── charge_region.py
├── dc_sweep
│   ├── getDC_RC.py
│   └── voltage_sweep.py
├── user_inputs
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
- [MODE/waveguide](../../MODE/waveguide/)



## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

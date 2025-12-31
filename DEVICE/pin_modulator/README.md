# 2D DEVICE PIN Modulator

**Purpose:**  
This module models a PIN optical modulator to study carrier-induced refractive index and absorption changes under electrical bias. The simulation is used to quantify the optoelectronic properties of the PIN junction.


## What this module does
This module simulates a 2D PIN optical modulator to analyze how electrical bias affects light propagation. It performs the following calculations:

- Charge distribution across the junction
- PIN junction properties (e.g., width, capacitance)
- RC time constant over a voltage sweep

By sweeping the bias voltage, the simulation characterizes key modulator performance metrics including modulation speed and response time.


## Quick start
1. After downloading the repository, navigate through the `pin_modulator/user_inputs/` directory.
2. Edit the `user_inputs/user_materials.py` and `user_inputs/user_simulation_parameters.py` to define the simulation materials for the cladding, core, box, and substrate layers. Follow the instructions written in the file.
3. Then define the in `user_inputs/user_sweep_parameters.py` the sweep parameters.
4.  Run scripts in these directories to generate results:
    -  `analytical_calculations/`
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
- DC capacitance and resistance for forward and reverse bias


Typical output location:

```
MODE/Results/pin_modulator
```


## Folder structure

```
pin_modulator/
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
├── README.md
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

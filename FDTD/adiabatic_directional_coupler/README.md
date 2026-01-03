# Adiabatic Directional Coupler (3D FDTD)

**Purpose:**  
Simulates an adiabatic directional coupler that uses gradual tapering to achieve high coupling efficiency between two waveguides. The adiabatic transition minimizes losses and improves mode transfer compared to conventional directional couplers.


## What this module does
Models the adiabatic directional coupler in 3D FDTD and extracts:
- Transmission vs. wavelength for through and bar ports (coupling efficiency)
- Field profiles to visualize mode evolution
- Gap sweep to optimize coupling distance


## Quick start
1. Navigate to `user_inputs/lumerical_files/` and open `sbend_adiabatic_directional_coupler.fsp` in Lumerical to configure materials and dimensions.
2. Run any of the scripts to automatically run the simulation and extract results:
   - `fields/getFields.py` - Extract and visualize electric field profiles
   - `gap_sweep/getGapSweep.py` - Sweep gap distance and analyze coupling
   - `transmission/getFrequencyResponse.py` - Extract frequency response (through and coupled ports)
3. Results save automatically to `FDTD/Results/adiabatic_directional_coupler/`.


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
- Transmission spectra for through and bar ports
- Field plots showing mode coupling
- Gap sweep data for optimization


Typical output location:

```
FDTD/Results/adiabatic_directional_coupler/
```


## Folder structure

```
adiabatic_directional_coupler/
├── fields/
│   └── getFields.py
├── gap_sweep/
│   └── getGapSweep.py
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
    └── lumerical_files/
        └── sbend_adiabatic_directional_coupler.fsp
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- All scripts use the `project_layout` system for path management
- Each script is self-contained and can be run independently
- Simulation data is cached by Lumerical, so re-running scripts is fast


## Related modules

- [FDTD/directional_coupler](../directional_coupler/README.md)
- [FDTD/adiabatic_y_branch](../adiabatic_y_branch/README.md)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

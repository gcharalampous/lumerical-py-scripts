# Adiabatic Y-Branch (3D FDTD)

**Purpose:**  
Simulates an adiabatic Y-branch splitter that uses smooth tapering to achieve symmetric, low-loss power splitting between two output waveguides. The gradual divergence minimizes mode conversion losses and improves splitting efficiency.


## What this module does
Models the adiabatic Y-branch in 3D FDTD and extracts:
- Transmission vs. wavelength for both output ports (splitting efficiency)
- Field profiles to visualize mode splitting and evolution
- Gap and length sweeps to optimize device performance


## Quick start
1. Navigate to `user_inputs/lumerical_files/` and open `adiabatic_y_branch.fsp` in Lumerical to configure materials and dimensions.
2. Run any of the scripts to automatically run the simulation and extract results:
   - `fields/getFields.py` - Extract and visualize electric field profiles
   - `gap_sweep/getGapSweep.py` - Sweep gap distance and analyze splitting
   - `length_sweep/getLengthSweep.py` - Sweep taper length and analyze performance
   - `transmission/getFrequencyResponse.py` - Extract frequency response (both output ports)
3. Results save automatically to `FDTD/Results/adiabatic_y_branch/`.




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
- Transmission spectra for both output ports
- Field plots showing mode splitting
- Gap and length sweep data for optimization


Typical output location:

```
FDTD/Results/adiabatic_y_branch/
```


## Folder structure

```
adiabatic_y_branch/
├── fields/
│   └── getFields.py
├── gap_sweep/
│   └── getGapSweep.py
├── length_sweep/
│   └── getLengthSweep.py
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
    └── lumerical_files/
        └── adiabatic_y_branch.fsp
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- All scripts use the `project_layout` system for path management
- Each script is self-contained and can be run independently
- Simulation data is cached by Lumerical, so re-running scripts is fast


## Related modules

- [FDTD/adiabatic_directional_coupler](../adiabatic_directional_coupler/README.md)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

# Adiabatic Y-Branch (3D FDTD)

**Purpose:**  
Simulates an adiabatic Y-branch splitter that uses smooth tapering to achieve symmetric, low-loss power splitting between two output waveguides. The gradual divergence minimizes mode conversion losses and improves splitting efficiency.


## What this module does
Models the adiabatic Y-branch in 3D FDTD and extracts:
- Transmission vs. wavelength for both output ports (splitting efficiency)
- Field profiles to visualize mode splitting and evolution
- Gap and length sweeps to optimize device performance


## Quick start
1. Go to `user_inputs/lumerical_files/` and set materials and dimensions in `adiabatic_y_branch.fsp`.
2. (Optional) Adjust overrides in `user_simulation_parameters.py` following the inline notes.
3. Run the scripts to generate results:
   - `fields/getFields.py`
   - `gap_sweep/getGapSweep.py`
   - `length_sweep/getLengthSweep.py`
   - `transmission/getFrequencyResponse.py`
4. Results save to `FDTD/Results/adiabatic_y_branch/`.




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
   ├── lumerical_files/
   │   └── adiabatic_y_branch.fsp
   └── user_simulation_parameters.py
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root


## Related modules

- [FDTD/adiabatic_directional_coupler](../adiabatic_directional_coupler/README.md)


## Status

- [ ] Verified
- [ ] Actively used
- [ ] Legacy or reference

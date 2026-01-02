# Adiabatic Directional Coupler (3D FDTD)

**Purpose:**  
Simulates an adiabatic directional coupler that uses gradual tapering to achieve high coupling efficiency between two waveguides. The adiabatic transition minimizes losses and improves mode transfer compared to conventional directional couplers.


## What this module does
Models the adiabatic directional coupler in 3D FDTD and extracts:
- Transmission vs. wavelength for through and bar ports (coupling efficiency)
- Field profiles to visualize mode evolution
- Gap sweep to optimize coupling distance


## Quick start
1. Go to `user_inputs/lumerical_files/` and set materials and dimensions in `sbend_adiabatic_directional_coupler.fsp`.
2. (Optional) Adjust overrides in `user_simulation_parameters.py` following the inline notes.
3. Run the scripts to generate results:
   - `fields/getFields.py`
   - `gap_sweep/getGapSweep.py`
   - `transmission/getFrequencyResponse.py`
4. Results save to `FDTD/Results/adiabatic_directional_coupler/`.


## Lumerical Template

These scripts are used for rendering and you are not required to directly run them


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
   ├── lumerical_files/
   │   └── sbend_adiabatic_directional_coupler.fsp
   └── user_simulation_parameters.py
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root


## Related modules

- [FDTD/directional_coupler](../directional_coupler/README.md)
- [FDTD/adiabatic_y_branch](../adiabatic_y_branch/README.md)


## Status

- [ ] Verified
- [ ] Actively used
- [ ] Legacy or reference

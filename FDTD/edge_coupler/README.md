# Edge Coupler (3D FDTD)

**Purpose:**  
Simulates a 3D edge coupler (spot-size converter) that transitions from a fiber/PLC mode to an on-chip waveguide. The taper reshapes the mode size and effective index to reduce insertion loss at the chip facet.


## What this module does
Models the edge-coupler taper in 3D FDTD and extracts:
- Transmission vs. wavelength (coupling efficiency)
- Forward and backward field profiles (mode matching and reflections)
- Mode overlap at the input/output facets


## Quick start
1. Go to `user_inputs/lumerical_files/` and set materials and dimensions in `edge_taper.fsp`.
2. (Optional) Adjust overrides in `user_simulation_parameters.py` following the inline notes, then uncomment override calls in the scripts if needed.
3. Run the scripts to generate results:
   - `fields/getFields.py`
   - `index_profile/index_profile_2D.py`
   - `tip_sweep/getTipSweep.py`
   - `transmission/getFrequencyResponse.py`
4. Results save to `FDTD/Results/edge_coupler/`.


## Rendering scripts

- `override_edge_coupler_region.py`: Override the edge coupler device
- `override_fdtd_region.py`: Override the fdtd simulation settings
 spectrum


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
- Transmission or reflection spectra
- Mode profiles or field plots


Typical output location:

```
FDTD/Results/edge_coupler/
```


## Folder structure

```
edge_coupler/
├── fields/
│   └── getFields.py
├── index_profile/
│   └── index_profile_2D.py
├── override_edge_coupler_region.py
├── override_fdtd_region.py
├── tip_sweep/
│   └── getTipSweep.py
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
   ├── lumerical_files/
   │   └── edge_taper.fsp
   └── user_simulation_parameters.py
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root


## Related modules

- [MODE/butt_coupling](../../MODE/butt_coupling/README.md)
- [MODE/edge_coupler](../../MODE/edge_coupler/README.md)


## Status

- [ ] Verified
- [ ] Actively used
- [ ] Legacy or reference

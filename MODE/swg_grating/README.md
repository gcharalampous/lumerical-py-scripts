# varFDTD Subwavelength Grating (MODE Solutions)

**Purpose:**  
Simulate and analyze the transmission and reflection properties of a subwavelength grating (SWG) waveguide structure using MODE Solutions, extracting spectral response and mode characteristics across a wavelength range.


## What this module does
This module simulates a subwavelength grating (SWG) waveguide structure in MODE Solutions:
- Transmission and reflection spectra across a wavelength range
- Guided mode profiles and effective indices
- Grating-induced loss

These simulations capture effective-medium behavior and do not model out-of-plane radiation losses.


## Quick start
1. Navigate to `swg_grating/user_inputs/lumerical_files/`
2. Edit `sub_wavelength_grating_layer_1.lms` to define simulation materials (cladding, core, box) and their dimensions
3. Edit `user_simulation_parameters.py` and follow the inline comments to configure simulation parameters
4. Run scripts in these directories to generate results:
   - `swg_grating/fields/`
   - `swg_grating/index_profile/`
   - `swg_grating/transmission/`
5. Optionally, override the Lumerical template by modifying input sections and uncommenting override function calls in the scripts


## Rendering scripts
- `override_swg_region.py`: Overrides the Lumerical file with parameters defined in editable files
- `override_varfdtd_region.py`: Overrides the Lumerical file with parameters defined in editable files

These scripts are used for rendering and you are not required to directly run them.


## Inputs
Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- lumerical template: `sub_wavelength_grating_layer_1.lms`
- material and geometry properties 
- wavelength or frequency settings


## Outputs
Results are saved automatically and may include:
- transmission or reflection spectra
- mode profiles or field plots
- figures for quick inspection

Typical output location:

```
MODE/Results/swg_grating/
```


## Folder structure
```
swg_grating/
├── fields
│   └── getFields.py
├── index_profile
│   └── index_profile_2D.py
├── override_swg_region.py
├── override_varfdtd_region.py
├── transmission
│   └── getFrequencyResponse.py
└── user_inputs
    ├── lumerical_files
    └── user_simulation_parameters.py

```


## Notes
- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root


## Related modules
- [FDTD/swg_grating](../../FDTD/swg_grating/)


## Status
- [ ] Verified
- [ ] Actively used
- [x] Legacy or reference

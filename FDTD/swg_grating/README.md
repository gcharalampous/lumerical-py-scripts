# Sub-Wavelength Grating (3D FDTD)

**Purpose:**  
Simulates sub-wavelength grating (SWG) structures for broadband waveguide filtering and dispersion engineering. SWGs provide engineering of effective refractive index and dispersion properties through periodic subwavelength features.


## What this module does
Models the sub-wavelength grating in 3D FDTD and extracts:
- Transmission vs. wavelength (filtering and broadband response)
- Refractive index profiles to visualize grating structure
- Field profiles showing mode interaction with SWG
- Multiple layer configurations for dispersion engineering


## Quick start
1. Set materials and dimensions in `user_inputs/lumerical_files/`:
   - `sub_wavelength_grating_layer_1.fsp` (default)
   - `sub_wavelength_grating_layer_2.fsp`
2. Choose which template to load via `file_index` in `user_inputs/user_simulation_parameters.py` (0 or 1). Other parameters stay inside the .fsp files.
3. Run the scripts to generate results:
   - `python FDTD/swg_grating/fields/getFields.py`
   - `python FDTD/swg_grating/index_profile/index_profile_2D.py`
   - `python FDTD/swg_grating/transmission/getFrequencyResponse.py`

4. Results will be saved automatically under:
   ```
   FDTD/Results/swg_grating/Figures/
   ├── Fields/
   ├── Index Profile/
   └── Frequency Response/
   ```


## Inputs

Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- grating period and duty cycle
- grating height and width
- material properties
- layer configuration
- wavelength or frequency settings


## Outputs

Results are saved automatically and may include:
- Transmission spectra showing filtering response
- Refractive index profile plots
- Field plots showing mode interaction with SWG


Typical output location:

```
FDTD/Results/swg_grating/
```


## Folder structure

```
swg_grating/
├── fields/
│   └── getFields.py
├── index_profile/
│   └── index_profile_2D.py
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
    ├── lumerical_files/
    │   ├── sub_wavelength_grating_layer_1.fsp
    │   └── sub_wavelength_grating_layer_2.fsp
    └── user_simulation_parameters.py
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts use `project_layout.py` for path management
- Designed to be run from the repository root

## Related modules

- [FDTD/grating_coupler_2D](../grating_coupler_2D/README.md)
- [FDTD/grating_coupler_rectangular_3D](../grating_coupler_rectangular_3D/README.md)
- [MODE/swg_grating](../../MODE/swg_grating/README.md)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

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
1. Go to `user_inputs/lumerical_files/` and set materials and dimensions in the SWG `.fsp` file:
   - `sub_wavelength_grating_layer_1.fsp`
   - `sub_wavelength_grating_layer_2.fsp`
2. (Optional) Adjust overrides in `user_simulation_parameters.py` following the inline notes, then uncomment override calls in the scripts if needed.
3. Run the scripts to generate results:
   - `Fields/getFields.py`
   - `index_profile/index_profile_2D.py`
   - `transmission/getFrequencyResponse.py`
4. Results save to `FDTD/Results/swg_grating/`.


## Rendering scripts

- `override_swg_region.py`: Override the sub-wavelength grating device
- `override_fdtd_region.py`: Override the fdtd simulation settings

These scripts are used for rendering and you are not required to directly run them


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
├── Fields/
│   └── getFields.py
├── index_profile/
│   └── index_profile_2D.py
├── override_fdtd_region.py
├── override_swg_region.py
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
- Scripts assume paths defined in config.py
- Designed to be run from the repository root

## Related modules

- [FDTD/grating_coupler_2D](../grating_coupler_2D/README.md)
- [FDTD/grating_coupler_rectangular_3D](../grating_coupler_rectangular_3D/README.md)
- [MODE/swg_grating](../../MODE/swg_grating/README.md)


## Status

- [ ] Verified
- [ ] Actively used
- [ ] Legacy or reference

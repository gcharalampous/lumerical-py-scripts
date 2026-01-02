# Disk Resonator Coupler (3D FDTD)

**Purpose:**  
Simulates a disk resonator coupled to a waveguide using 3D FDTD to extract coupling coefficients, and field profiles. Multiple disk geometries (straight, concentric, rectangular) can be analyzed.


## What this module does
Models the disk resonator coupling in 3D FDTD and extracts:
- Transmission vs. wavelength (coupling efficiency and resonance response)
- Refractive index profiles to visualize device geometry
- Field profiles showing resonator mode confinement
- Gap sweep to optimize coupling gap


## Quick start
1. Go to `user_inputs/lumerical_files/` and select the disk geometry configuration in one of the `.fsp` files:
   - `straight_disk_coupling_section.fsp`
   - `concentric_disk_coupling_section.fsp`
   - `rectangular_disk_coupling_section.fsp`
2. (Optional) Adjust overrides in `user_simulation_parameters.py` following the inline notes, then uncomment override calls in the scripts if needed.
3. Run the scripts to generate results:
   - `fields/getFields.py`
   - `index_profile/index_profile_2D.py`
   - `gap_sweep/getGapSweep.py`
   - `transmission/getFrequencyResponse.py`
4. Results save to `FDTD/Results/disk_resonator_coupler/`.


## Rendering scripts

- `override_disk_coupler_region.py`: Override the disk resonator coupler device
- `override_fdtd_region.py`: Override the fdtd simulation settings

These scripts are used for rendering and you are not required to directly run them


## Inputs

Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- disk geometry parameters (radius, thickness)
- coupling gap
- material properties
- wavelength or frequency settings
- sweep definitions


## Outputs

Results are saved automatically and may include:
- Transmission spectra showing resonance
- Refractive index profile plots
- Field plots showing resonator mode confinement
- Gap sweep data for coupling optimization


Typical output location:

```
FDTD/Results/disk_resonator_coupler/
```


## Folder structure

```
disk_resonator_coupler/
├── fields/
│   └── getFields.py
├── gap_sweep/
│   └── getGapSweep.py
├── index_profile/
│   └── index_profile_2D.py
├── override_disk_coupler_region.py
├── override_fdtd_region.py
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
   ├── lumerical_files/
   │   ├── straight_disk_coupling_section.fsp
   │   ├── concentric_disk_coupling_section.fsp
   │   └── rectangular_disk_coupling_section.fsp
   └── user_simulation_parameters.py
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root
- Multiple disk geometries are supported; select the appropriate `.fsp` file for your configuration


## Related modules

- [FDTD/ring_resonator_coupler](../ring_resonator_coupler/README.md)
- [MODE/directional_coupler](../../MODE/directional_coupler/README.md)


## Status

- [ ] Verified
- [ ] Actively used
- [ ] Legacy or reference

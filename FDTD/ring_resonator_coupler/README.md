# Ring Resonator Coupler (3D FDTD)

**Purpose:**  
Simulates a ring resonator coupled to a waveguide using 3D FDTD to extract coupling efficiency, and field profiles. Multiple ring geometries (straight, concentric, rectangular) can be analyzed.


## What this module does
Models the ring resonator coupling in 3D FDTD and extracts:
- Transmission vs. wavelength (coupling efficiency and resonance response)
- Refractive index profiles to visualize device geometry
- Field profiles showing resonator mode confinement
- Gap and length sweeps to optimize coupling performance


## Quick start
1. Go to `user_inputs/lumerical_files/` and select the ring geometry configuration in one of the `.fsp` files:
   - `straight_ring_coupling_section.fsp`
   - `concentric_ring_coupling_section.fsp`
   - `rectangular_ring_coupling_section.fsp`
2. (Optional) Adjust overrides in `user_simulation_parameters.py` following the inline notes, then uncomment override calls in the scripts if needed.
3. Run the scripts to generate results:
   - `fields/getFields.py`
   - `index_profile/index_profile_2D.py`
   - `sweep/getGapSweep.py`
   - `sweep/getLengthSweep.py`
   - `transmission/getFrequencyResponse.py`
4. Results save to `FDTD/Results/ring_resonator_coupler/`.


## Rendering scripts

- `override_ring_coupler_region.py`: Override the ring resonator coupler device
- `override_fdtd_region.py`: Override the fdtd simulation settings

These scripts are used for rendering and you are not required to directly run them


## Inputs

Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- ring geometry parameters (radius, thickness)
- coupling gap distance
- material properties
- wavelength or frequency settings
- sweep definitions


## Outputs

Results are saved automatically and may include:
- Transmission spectra showing resonance
- Refractive index profile plots
- Field plots showing resonator mode confinement
- Gap and length sweep data for coupling optimization


Typical output location:

```
FDTD/Results/ring_resonator_coupler/
```


## Folder structure

```
ring_resonator_coupler/
├── fields/
│   └── getFields.py
├── index_profile/
│   └── index_profile_2D.py
├── sweep/
│   ├── getGapSweep.py
│   └── getLengthSweep.py
├── override_fdtd_region.py
├── override_ring_coupler_region.py
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
   ├── lumerical_files/
   │   ├── straight_ring_coupling_section.fsp
   │   ├── concentric_ring_coupling_section.fsp
   │   └── rectangular_ring_coupling_section.fsp
   └── user_simulation_parameters.py
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root
- Multiple ring geometries are supported; select the appropriate `.fsp` file for your configuration


## Related modules

- [FDTD/disk_resonator_coupler](../disk_resonator_coupler/README.md)
- [MODE/directional_coupler](../../MODE/directional_coupler/README.md)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

# MMI Couplers

**Purpose:**  
Simulates Multi-Mode Interferometer (MMI) couplers using 3D FDTD to extract power splitting characteristics, mode behavior, and field profiles for optimizing MMI coupler designs.


## What this module does
Models MMI coupler systems in 3D FDTD domain.
Mention:
- device type: MMI coupler (1x2 and 2x2 variants)
- simulation domain: FDTD
- what is being extracted: transmission spectra, power splitting efficiency, mode profiles, field distributions, and MMI length optimization


## Quick start

1. Open and select a Lumerical template file from:
   ```
   user_inputs/lumerical_files/
   ```
   Available templates:
   - `MMI_1x2.fsp` - 1x2 MMI coupler splitter
   - `MMI_2x2.fsp` - 2x2 MMI coupler

2. (Optional) Edit simulation parameters in:
   ```
   user_inputs/user_simulation_parameters.py
   ```

3. Run the analysis scripts:
   ```
   python fields/getFields.py
   python index_profile/index_profile_2D.py
   python length_sweep/getLengthSweep.py
   python transmission/getFrequencyResponse.py
   ```

4. Results will be saved automatically under:
   ```
   FDTD/Results/mmi_couplers/
   ```


## Simulation scripts

- fields/getFields.py : extract electromagnetic field profiles
- index_profile/index_profile_2D.py : generate refractive index profile visualization  
- length_sweep/getLengthSweep.py : perform MMI length parametric sweep
- transmission/getFrequencyResponse.py : extract transmission vs. wavelength spectrum

Run these scripts individually to perform different types of analysis on the MMI coupler


## Inputs

Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- MMI length and width parameters
- waveguide dimensions and spacing
- material properties (refractive index)
- wavelength or frequency settings
- sweep definitions for parametric analysis


## Outputs

Results are saved automatically and may include:
- transmission spectra showing power splitting ratios
- field plots showing mode interference patterns
- refractive index profile plots
- length sweep data for MMI optimization

Typical output location:

```
FDTD/Results/mmi_couplers/
```


## Folder structure

```
mmi_couplers/
├── README.md
├── fields/
│   └── getFields.py
├── index_profile/
│   └── index_profile_2D.py
├── length_sweep/
│   └── getLengthSweep.py
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
    ├── lumerical_files/
    │   ├── MMI_1x2.fsp
    │   └── MMI_2x2.fsp
    └── user_simulation_parameters.py
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Scripts assume paths defined in config.py
- Designed to be run from the repository root
- Multiple MMI geometries are supported; select the appropriate `.fsp` file for your configuration


## Related modules

- [FDTD/directional_coupler](../directional_coupler/README.md)
- [FDTD/coupled_ring_coupler](../coupled_ring_coupler/README.md)
- [MODE/directional_coupler](../../MODE/directional_coupler/README.md)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

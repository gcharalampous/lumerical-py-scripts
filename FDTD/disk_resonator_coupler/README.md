# Disk Resonator Coupler

**Purpose:**  
Simulates a disk resonator coupled to a waveguide using 3D FDTD to extract coupling coefficients, resonance characteristics, and field profiles for optimizing coupling efficiency.


## What this module does
Models a disk resonator coupling system in 3D FDTD domain.
Mention:
- device type: disk resonator coupled to waveguide
- simulation domain: FDTD
- what is being extracted: transmission spectra, coupling efficiency, resonance response, field profiles, and coupling gap optimization


## Quick start

1. Open and select a Lumerical template file from:
   ```
   user_inputs/lumerical_files/
   ```
   Available templates:
   - `straight_disk_coupling_section.fsp` - Disk resonator with straight waveguide coupling
   - `coocentric_disk_coupling_section.fsp` - Concentric disk resonator coupling

2. (Optional) Edit simulation parameters in:
   ```
   user_inputs/user_simulation_parameters.py
   ```

3. Run the analysis scripts:
   ```
   python fields/getFields.py
   python index_profile/index_profile_2D.py
   python gap_sweep/getGapSweep.py
   python transmission/getFrequencyResponse.py
   ```

4. Results will be saved automatically under:
   ```
   FDTD/Results/disk_resonator_coupler/
   ```


## Simulation scripts

- fields/getFields.py : extract electromagnetic field profiles
- index_profile/index_profile_2D.py : generate refractive index profile visualization  
- gap_sweep/getGapSweep.py : perform coupling gap parametric sweep
- transmission/getFrequencyResponse.py : extract transmission vs. wavelength spectrum

Run these scripts individually to perform different types of analysis on the disk resonator coupler


## Inputs

Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- disk geometry parameters (radius, thickness)
- coupling gap distance
- material properties
- wavelength or frequency settings
- sweep definitions


## Outputs

Results are saved automatically and may include:
- transmission spectra showing resonance peaks
- field plots showing resonator mode confinement
- refractive index profile plots
- gap sweep data for coupling optimization

Typical output location:

```
FDTD/Results/disk_resonator_coupler/
```


## Folder structure

```
disk_resonator_coupler/
├── README.md
├── fields/
│   └── getFields.py
├── gap_sweep/
│   └── getGapSweep.py
├── index_profile/
│   └── index_profile_2D.py
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
    ├── lumerical_files/
    │   ├── straight_disk_coupling_section.fsp
    │   └── coocentric_disk_coupling_section.fsp
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

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

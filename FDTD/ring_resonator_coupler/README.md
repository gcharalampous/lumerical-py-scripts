# Ring Resonator Coupler

**Purpose:**  
Simulates a ring resonator coupled to a waveguide using 3D FDTD to extract coupling coefficients, resonance characteristics, and field profiles for optimizing coupling efficiency.


## What this module does
Models a ring resonator coupling system in 3D FDTD domain.
Mention:
- device type: ring resonator coupled to waveguide
- simulation domain: FDTD
- what is being extracted: transmission spectra, coupling efficiency, resonance response, field profiles, gap and length sweep optimization


## Quick start

1. Open and select a Lumerical template file from:
   ```
   user_inputs/lumerical_files/
   ```
   Available templates:
   - `straight_ring_coupling_section.fsp` - Ring resonator with straight waveguide coupling
   - `coocentric_ring_coupling_section.fsp` - Concentric ring resonator coupling
   - `rectangular_ring_coupling_section.fsp` - Rectangular ring resonator coupling

2. (Optional) Edit simulation parameters in:
   ```
   user_inputs/user_simulation_parameters.py
   ```

3. Run the analysis scripts:
   ```
   python fields/getFields.py
   python index_profile/index_profile_2D.py
   python sweep/getGapSweep.py
   python sweep/getLengthSweep.py
   python transmission/getFrequencyResponse.py
   ```

4. Results will be saved automatically under:
   ```
   FDTD/Results/ring_resonator_coupler/
   ```


## Simulation scripts

- fields/getFields.py : extract electromagnetic field profiles
- index_profile/index_profile_2D.py : generate refractive index profile visualization
- sweep/getGapSweep.py : perform coupling gap parametric sweep
- sweep/getLengthSweep.py : perform coupling length parametric sweep
- transmission/getFrequencyResponse.py : extract transmission vs. wavelength spectrum

Run these scripts individually to perform different types of analysis on the ring resonator coupler


## Inputs

Editable files are located in:

```
user_inputs/
```

Typical inputs include:
- ring geometry parameters (radius, thickness)
- coupling gap distance
- coupling length
- material properties
- wavelength or frequency settings
- sweep definitions


## Outputs

Results are saved automatically and may include:
- transmission spectra showing resonance peaks
- field plots showing resonator mode confinement
- refractive index profile plots
- gap and length sweep data for coupling optimization

Typical output location:

```
FDTD/Results/ring_resonator_coupler/
```


## Folder structure

```
ring_resonator_coupler/
├── README.md
├── fields/
│   └── getFields.py
├── index_profile/
│   └── index_profile_2D.py
├── sweep/
│   ├── getGapSweep.py
│   └── getLengthSweep.py
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
    ├── lumerical_files/
    │   ├── straight_ring_coupling_section.fsp
    │   ├── coocentric_ring_coupling_section.fsp
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
- [FDTD/coupled_ring_coupler](../coupled_ring_coupler/README.md)
- [MODE/directional_coupler](../../MODE/directional_coupler/README.md)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

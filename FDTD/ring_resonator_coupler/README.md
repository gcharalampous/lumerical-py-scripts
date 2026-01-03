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

2. Set the template file index in:
   ```
   user_inputs/user_simulation_parameters.py
   ```
   Set `file_index` to select which template to use:
   - `file_index = 0` for straight ring coupling
   - `file_index = 1` for concentric ring coupling
   - `file_index = 2` for rectangular ring coupling (required for length sweep)

3. Run the analysis scripts:
   ```
   python fields/getFields.py
   python index_profile/index_profile_2D.py
   python gap_sweep/getGapSweep.py
   python length_sweep/getLengthSweep.py
   python transmission/getFrequencyResponse.py
   ```

4. Results will be saved automatically under:
   ```
   FDTD/Results/ring_resonator_coupler/Figures/
   ├── Gap Sweep/
   ├── Length Sweep/
   └── (other result folders)
   ```


## Simulation scripts

- fields/getFields.py : extract electromagnetic field profiles
- index_profile/index_profile_2D.py : generate refractive index profile visualization
- gap_sweep/getGapSweep.py : perform coupling gap parametric sweep
- length_sweep/getLengthSweep.py : perform coupling length parametric sweep
- transmission/getFrequencyResponse.py : extract transmission vs. wavelength spectrum

Run these scripts individually to perform different types of analysis on the ring resonator coupler


## Inputs

Editable files are located in:

```
user_inputs/user_simulation_parameters.py
```

Set `file_index` to select which Lumerical template file to load:
- `0` = straight_ring_coupling_section.fsp
- `1` = concentric_ring_coupling_section.fsp  
- `2` = rectangular_ring_coupling_section.fsp (required for length sweep)

All other simulation parameters (ring geometry, coupling gap, material properties, wavelength settings, sweep definitions) should be configured within the selected `.fsp` file.


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
├── gap_sweep/
│   └── getGapSweep.py
├── index_profile/
│   └── index_profile_2D.py
├── length_sweep/
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

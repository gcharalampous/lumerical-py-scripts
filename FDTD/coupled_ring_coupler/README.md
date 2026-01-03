# Coupled Ring Coupler (3D FDTD)

**Purpose:**  
Simulate bus-to-ring coupling using 3D FDTD templates (circular bend and racetrack) to study coupling efficiency, field overlap, and spectral response.


## What this module does
Provides ready-to-run Lumerical FDTD projects plus automation scripts for coupled ring couplers. You can:
- Inspect and modify coupling geometry (gap, bend radius, racetrack length)
- Run gap sweeps, frequency response, and field captures via Python helpers
- Visualize field confinement and coupling regions


## Quick start

1. Open a template project in Lumerical FDTD:
   ```
   user_inputs/lumerical_files/circular_bend_coupler.fsp
   user_inputs/lumerical_files/racetrack_coupler.fsp
   ```
2. Adjust geometry, mesh, sources, and monitors inside Lumerical.
3. For automated runs, use the helper scripts (run from repo root):
   ```
   python FDTD/coupled_ring_coupler/gap_sweep/getGapSweep.py
   python FDTD/coupled_ring_coupler/length_sweep/getLengthSweep.py
   python FDTD/coupled_ring_coupler/transmission/getFrequencyResponse.py
   python FDTD/coupled_ring_coupler/fields/getFields.py
   ```
4. Run the simulation and export or view transmission/field data in:
   ```
   FDTD/Results/coupled_ring_coupler/
   ```


## Rendering scripts

- gap_sweep/getGapSweep.py: runs `sweep_coupling_gap` and plots through/coupled vs. gap
- length_sweep/getLengthSweep.py: runs `sweep_coupling_length` and plots through/coupled vs. coupling length (requires `template_index=1`, racetrack only)
- transmission/getFrequencyResponse.py: runs a simulation and plots through vs. bar ports
- fields/getFields.py: runs a simulation and plots top-view E-field

All scripts use the template specified in `user_inputs/user_simulation_parameters.py`.


## Inputs

Editable files are located in:

```
user_inputs/lumerical_files/
```

Typical inputs include:
- Coupling gap and coupling length
- Ring bend radius and racetrack straight length
- Waveguide dimensions and material models
- Wavelength range, source settings, and monitor placement


## Outputs

Results are saved automatically by the scripts (figures) or manually from Lumerical and may include:
- Transmission spectra through the bus waveguide
- Field profile snapshots in the coupling region
- Effective index or overlap integrals for design comparison

Typical output location:

```
FDTD/Results/coupled_ring_coupler/
```


## Folder structure

```
coupled_ring_coupler/
├── README.md
├── gap_sweep/
│   └── getGapSweep.py
├── length_sweep/
│   └── getLengthSweep.py
├── transmission/
│   └── getFrequencyResponse.py
├── fields/
│   └── getFields.py
└── user_inputs/
    ├── user_simulation_parameters.py
    └── lumerical_files/
        ├── circular_bend_coupler.fsp
        └── racetrack_coupler.fsp
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Paths assume repository root execution when running scripts
- Verify mesh refinement and material models before relying on results
- Length sweep (`getLengthSweep.py`) requires `template_index=1` (racetrack_coupler) in user_simulation_parameters.py
- Gap sweep and other scripts work with both templates


## Related modules

- FDTD/ring_resonator_coupler
- FDTD/disk_resonator_coupler
- FDTD/directional_coupler


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

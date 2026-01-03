# Directional Coupler (3D FDTD)

**Purpose:**  
Simulate waveguide-to-waveguide coupling using 3D FDTD to study coupling efficiency, field overlap, and spectral response.


## What this module does
Provides ready-to-run Lumerical FDTD projects plus automation scripts for directional couplers. You can:
- Inspect and modify coupling geometry (gap, coupling length)
- Run length sweeps, frequency response, and field captures via Python helpers
- Visualize field confinement and coupling regions


## Quick start

1. Open the template project in Lumerical FDTD:
   ```
   user_inputs/lumerical_files/sbend_directional_coupler.fsp
   ```
2. Adjust geometry, mesh, sources, and monitors inside Lumerical.
3. For automated runs, use the helper scripts (run from repo root):
   ```
   python FDTD/directional_coupler/length_sweep/getLengthSweep.py
   python FDTD/directional_coupler/transmission/getFrequencyResponse.py
   python FDTD/directional_coupler/fields/getFields.py
   ```
4. Results will be saved automatically under:
   ```
   FDTD/Results/directional_coupler/
   ```


## Rendering scripts

- length_sweep/getLengthSweep.py: runs `sweep_coupling_length` and plots through/coupled vs. coupling length
- transmission/getFrequencyResponse.py: runs a simulation and plots separate through and coupled frequency responses (results only)
- fields/getFields.py: runs a simulation and plots top-view E-field (results only)

All scripts use the template specified in `user_inputs/user_simulation_parameters.py`.


## Inputs

Editable files are located in:

```
user_inputs/lumerical_files/
```

Typical inputs include:
- Coupling gap and coupling length
- Waveguide dimensions and material models
- Wavelength range, source settings, and monitor placement


## Outputs

Results are saved automatically by the scripts (figures) and may include:
- Transmission spectra through the bus waveguide
- Field profile snapshots in the coupling region
- Effective index or overlap integrals for design comparison

Typical output location:

```
FDTD/Results/directional_coupler/
```


## Folder structure

```
directional_coupler/
├── README.md
├── length_sweep/
│   └── getLengthSweep.py
├── transmission/
│   └── getFrequencyResponse.py
├── fields/
│   └── getFields.py
└── user_inputs/
    ├── user_simulation_parameters.py
    └── lumerical_files/
        └── sbend_directional_coupler.fsp
```


## Notes

- Requires Lumerical installed and accessible via lumapi
- Paths assume repository root execution when running scripts
- Verify mesh refinement and material models before relying on results


## Related modules

- [FDTD/coupled_ring_coupler](../coupled_ring_coupler/README.md)
- [FDTD/ring_resonator_coupler](../ring_resonator_coupler/README.md)
- [FDTD/disk_resonator_coupler](../disk_resonator_coupler/README.md)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

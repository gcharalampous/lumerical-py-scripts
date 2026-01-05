# Waveguide Crossing (3D FDTD)

**Purpose:**  
This simulation models a 3D waveguide crossing structure designed to minimize crosstalk and insertion loss when two waveguides intersect. The structure uses tapered sections to optimize mode confinement and reduce scattering losses at the crossing region.


## What this module does

This module performs electromagnetic simulations of a waveguide crossing structure using the 3D FDTD computational method.

The simulation extracts:
- **Transmission and crosstalk frequency response**: Quantifies power coupling efficiency in the through port and parasitic coupling to the cross port across the operating bandwidth
- **Electric field (E-field) distribution**: Maps the spatially-resolved electromagnetic field intensity showing light propagation through the crossing region
- **Refractive index profile**: Characterizes the spatial variation of the material's refractive index to validate the crossing geometry
- **Taper length optimization**: Sweeps taper length to find optimal balance between transmission, crosstalk, and device footprint

This analysis is essential for designing compact photonic integrated circuits with minimal crosstalk penalties.


## Quick start
1. Set materials and dimensions in `user_inputs/lumerical_files/waveguide_crossing_multi_wg_taper.fsp` (cladding, core, box, taper geometry).
2. Run the scripts to generate results:
    - `python fields/getFields.py`
    - `python index_profile/index_profile_2D.py`
    - `python length_sweep/getLengthSweep.py`
    - `python transmission/getFrequencyResponse.py`

3. Results will be saved automatically under:
   ```
   FDTD/Results/waveguide_crossing/Figures/
   ├── Fields/
   ├── Index Profile/
   ├── Length Sweep/
   └── Transmission/
   ```



## Lumerical Template file

- `waveguide_crossing_multi_wg_taper.fsp` : Lumerical file that defines the waveguide crossing structure


## Outputs

Results are saved automatically and may include:
- Electric field distributions (xy top view with logarithmic color scale)
- Refractive index profile maps (xy top view and yz cross-section)
- Frequency-dependent transmission and crosstalk spectra (linear and dB scales)
- Taper length sweep results showing transmission vs. crosstalk trade-off (linear and dB scales)

Typical output location:

```
FDTD/Results/waveguide_crossing/Figures/
```


## Folder structure

```
waveguide_crossing/
├── fields/
│   └── getFields.py
├── index_profile/
│   └── index_profile_2D.py
├── length_sweep/
│   └── getLengthSweep.py
├── README.md
├── transmission/
│   └── getFrequencyResponse.py
└── user_inputs/
    └── lumerical_files/
        └── waveguide_crossing_multi_wg_taper.fsp
```


## Notes
- Requires Lumerical installed and accessible via lumapi
- Scripts use `project_layout.py` for path management
- Designed to be run from the repository root
- Uses logarithmic color scale for field visualization to capture wide dynamic range
- Monitor names: `through_mode` for transmission, `crosstalk_mode` for parasitic coupling


## Related modules
- [FDTD/waveguide_straight](../waveguide_straight/)


## Status

- [x] Verified
- [ ] Actively used
- [ ] Legacy or reference

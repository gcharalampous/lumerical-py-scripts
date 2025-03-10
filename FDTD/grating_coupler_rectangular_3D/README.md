## 2D Grating Coupler Simulation (2D FDTD)

```
.
├── analytical
│   └── 1D_grating_coupler_design.ipynb
├── index_profile
│   └── index_profile_2D.py
├── override_fdtd_region.py
├── override_grating_coupler_region.py
├── sweep_functions
│   ├── getFiberAngle.py
│   ├── getFiberPosition.py
│   └── getFillFactorSweep.py
├── transmission
│   └── getFrequencyResponse.py
└── user_inputs
    ├── lumerical_files
    │   └── grating_coupler_2D.fsp
    └── user_simulation_parameters.py

```

### Quick Simulation Setup

1. After cloning the repository, navigate to `analytical/1D_grating_coupler_design.ipynb` to estimate roughly the grating period based on the slab effective indices from the waveguides, fiber angle of incidences, and refractive indices.
2. Navigate through the `user_inputs/lumerical_files` directory and edit the Lumerical file `grating_coupler_2D.fsp` to define the simulation materials for the cladding, core, and box layers along with their dimensions.
3. Edit the `user_inputs/user_simulation_parameters.py` to define the simulation properties, region, and structure dimensions. Follow the instructions written in the file.
4. Run the files in the `sweep_functions` directory to perform the desired parameter sweeps and obtain the results.
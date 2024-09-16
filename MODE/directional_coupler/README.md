## 2D Directional Coupler (MODE Solutions)

```
directional_coupler/
├── coupling_sweep
│   ├── coupling_gap.py
│   └── coupling_length.py
├── dissimilar_waveguides
│   └── coupling_length.py
├── even_odd_mode_profile.py
├── mode_profile
│   └── mode_profile_2D.py
├── README.md
└── user_inputs
    ├── lumerical_files
    │   └── waveguide_coupler.lms
    ├── user_simulation_parameters.py
    └── user_sweep_parameters.py
```                                                                                                        

### Quick Simulation Setup

1. After downloading the repository, navigate through the `directional-coupler/user_inputs/lumerical_files` directory.
2. Edit the lumerical file `waveguide_coupler.lms` to define the simulation parameters such as materials, cladding, core, and box layers along with their dimensions. 
3. Edit the `user_sweep_parameters.py` and `user_simulation_parameters.py`to define the sweep and simulation parameters, respectively. Follow the comment-sections written in the file.
4. Run the `mode_profile/mode_profile_2D.py`, `coupling_sweep/coupling_length.py` and `coupling_sweep/coupling_gap.py` Python files to get the results.

**Tip**: The analysis found in `coupling_sweep` is valid only when the two waveguides are phase-matched. This means both waveguides should have the same dimensions and materials. If the two waveguides have different widths, run `dissimilar_waveguides/coupling_length.py`.

## 2D Directional Coupler(MODE Solutions)

    ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐           
    │directional-coupler                                                                                                   │           
    └┬──────────────────────────────────────────────────┬─────────────────────────┬───────────────────────────────────────┬┘           
    ┌▽────────────────────────────────────────────────┐┌▽───────────────────────┐┌▽─────────────────────────────────────┐┌▽──────────┐ 
    │user_inputs                                      ││mode_profile            ││coupling_sweep                        ││get_mode.py│ 
    └┬────────────────┬──────────────────────────────┬┘└───────────────────────┬┘└─────────────────┬───────────────────┬┘└───────────┘ 
    ┌▽──────────────┐┌▽────────────────────────────┐┌▽───────────────────────┐┌▽─────────────────┐┌▽─────────────────┐┌▽──────────────┐
    │lumerical_files││user_simulation_parameters.py││user_sweep_parameters.py││mode_profile_2D.py││coupling_length.py││coupling_gap.py│
    └┬──────────────┘└─────────────────────────────┘└────────────────────────┘└──────────────────┘└──────────────────┘└───────────────┘
    ┌▽────────────────────┐                                                                                                            
    │waveguide_coupler.lms│                                                                                                            
    └─────────────────────┘                                                                                                            

### Quick Simulation Setup

1. After downloading the repository, navigate through the `directional-coupler/user_inputs/lumerical_files` directory.
2. Edit the lumerical file `waveguide_coupler.lms` to define the simulation parameters such as materials, cladding, core, and box layers along with their dimensions. 
3. Edit the `user_sweep_parameters.py` and `user_simulation_parameters.py`to define the sweep and simulation parameters, respectively. Follow the comment-sections written in the file.
4. Run the `mode_profile/mode_profile_2D.py`, `coupling_sweep/coupling_length.py` and `coupling_sweep/coupling_gap.py` Python files to get the results.

Tip: This analysis found in `coupling_sweep` is valid only when the two waveguides are phased matched. Meaning, both waveguides should have the same dimensions and materials.

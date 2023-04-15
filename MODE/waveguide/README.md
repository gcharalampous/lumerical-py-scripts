## 2D Waveguide Simulations (MODE Solutions)

    ┌─────────────────────────────────────────────────────────────────────────────────────────────┐                                                                                                 
    │waveguide                                                                                    │                                                                                                 
    └┬────────────────────┬──────────────┬────────────────────────┬──────────────────────────────┬┘                                                                                                 
    ┌▽──────────────────┐┌▽────────────┐┌▽──────────────────────┐┌▽────────────────────────────┐┌▽─────────────────────────────────────────────────────────────────┐                                
    │waveguide_render.py││fde_region.py││user_inputs            ││mode_profile                 ││neff_sweep                                                        │                                
    └───────────────────┘└─────────────┘└┬──┬──────────────────┬┘└────────────────────────────┬┘└─────────────────┬─────────────────┬─────────────────────────────┬┘                                
    ┌────────────────────────────────────▽┐┌▽────────────────┐┌▽────────────────────────────┐┌▽─────────────────┐┌▽───────────────┐┌▽───────────────────────────┐┌▽────────────────────────────────┐
    │user_sweep_parameters.py             ││user_materials.py││user_simulation_parameters.py││mode_profile_2D.py││neff_width_2D.py││neff_height_variations_2D.py││neff_width_sweep_variations_2D.py│
    └─────────────────────────────────────┘└─────────────────┘└─────────────────────────────┘└──────────────────┘└────────────────┘└────────────────────────────┘└─────────────────────────────────┘
    
    

### Quick Simulation Setup

1. After downloading the repository, navigate through the `waveguide/user-inputs` directory.
2. Edit the `user_materials.py` to define the simulation materials for the cladding, core, box, and substrate layers. Follow the instructions written in the file.
3. Edit the `user_simulation_parameters.py` to define the simulation properties, region and structure dimensions. Follow the instructions written in the file.
4. Navigate under the `waveguide/mode_profile` or `waveguide/neff_sweep` directories to run the desired python file.

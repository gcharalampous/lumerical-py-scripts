## 2D Waveguide Heater (MODE Solutions)

    ┌──────────────────────────────────────────────────┐           
    │waveguide-heater                                  │           
    └┬────────────────────┬──────────────┬────────────┬┘           
    ┌▽──────────────────┐┌▽────────────┐┌▽──────────┐┌▽───────────┐
    │waveguide_render.py││fde_region.py││user_inputs││mode_profile│
    └───────────────────┘└─────────────┘└┬──────────┘└┬───────────┘
    ┌────────────────────────────────────▽┐┌──────────▽───────┐    
    │user_materials.py                    ││mode_profile_2D.py│    
    └─────────────────────────────────────┘└──────────────────┘    
    
    

### Quick Simulation Setup

1. After downloading the repository, navigate through the `waveguide/user-inputs` directory.
2. Edit the `user_materials.py` to define the simulation materials for the cladding, core, box, metals and substrate layers. Follow the instructions written in the file.
3. Edit the `user_simulation_parameters.py` to define the simulation properties, region and structure dimensions. Follow the instructions written in the file.
4. Navigate under the `waveguide/mode_profile` to get the mode profile with the metal layer.
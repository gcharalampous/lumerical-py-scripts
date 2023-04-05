## 2D Waveguide Simulations (MODE Solutions)

    ┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐                                      
    │vertical-taper                                                                                           │                                      
    └┬────────────────────────────────────────────────────────────────────────────────────┬──────────────────┬┘                                      
    ┌▽──────────────────────────────────────────────────────────────────────────────────┐┌▽────────────────┐┌▽─────────────────┐                     
    │user-inputs                                                                        ││mode-profile     ││neff-sweep        │                     
    └┬───────────────────────────┬───────────────────────────┬─────────────────────────┬┘└────────────────┬┘└─────────────────┬┘                     
    ┌▽─────────────────────────┐┌▽─────────────────────────┐┌▽───────────────────────┐┌▽────────────────┐┌▽─────────────────┐┌▽─────────────────────┐
    │taper_waveguide_layer1.lms││taper_waveguide_layer2.lms││user_sweep_parameters.py││user_materials.py││mode_profile_2D.py││neff_width_sweep_2D.py│
    └──────────────────────────┘└──────────────────────────┘└────────────────────────┘└─────────────────┘└──────────────────┘└──────────────────────┘
    
    

### Quick Simulation Setup

1. After downloading the repository, navigate through the `vertical-taper/user-inputs` directory.
2. Edit the `user_materials.py` to define the simulation materials for the cladding, core, and box layers. Follow the instructions written in the file.
3. Edit the two files namely `taper_waveguide_layer1.lms` and `taper_waveguide_layer2.lms`. You can also define materials from these files too.
4. Edit the `user_sweep_parameters.py` to define the simulation sweep parameters. Follow the instructions written in the file.
5. Navigate under the `vertical-taper/mode_profile` or `vertical-taper/neff_sweep` directories to run the desired python file and get the results.

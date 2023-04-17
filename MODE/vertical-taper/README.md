## 2D Verttical Taper Simulations (MODE Solutions)

    ┌───────────────────────────────────┐                                            
    │vertical-taper                     │                                            
    └┬─────────────────────────────────┬┘                                            
    ┌▽───────────────────────────────┐┌▽───────────────────────┐                     
    │user_inputs                     ││neff_sweep              │                     
    └┬──────────────────────────────┬┘└───────────────────────┬┘                     
    ┌▽────────────────────────────┐┌▽───────────────────────┐┌▽─────────────────────┐
    │lumerical_files              ││user_sweep_parameters.py││neff_width_sweep_2D.py│
    └┬───────────────────────────┬┘└────────────────────────┘└──────────────────────┘
    ┌▽─────────────────────────┐┌▽─────────────────────────┐                         
    │taper_waveguide_layer1.lms││taper_waveguide_layer2.lms│                         
    └──────────────────────────┘└──────────────────────────┘

### Quick Simulation Setup

1. After downloading the repository, navigate through the `vertical-taper/user_inputs/lumerical_files` directory.
2. Edit the two lumerical files `taper_waveguide_layer1.lms` and `taper_waveguide_layer2.lms`to define the simulation materials for the cladding, core, and box layers along with their dimensions. 
3. Edit the `user_sweep_parameters.py` to define the simulation sweep parameters. Follow the comment-sections written in the file.
4. Run the `vertical-taper/neff_sweep` Python file and get the results.



Tip: At the taper-length where the two effective indices of the bottom and upper taper are equal, that's the point where the light couples from the bottom to the upper layer.

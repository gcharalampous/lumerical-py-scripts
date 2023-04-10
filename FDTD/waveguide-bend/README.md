## 2D Waveguide Simulations (MODE Solutions)

    ┌───────────────────────────────────────────────┐                                         
    │waveguide-bend                                 │                                         
    └┬───────────────────┬─────────────────────────┬┘                                         
    ┌▽─────────────────┐┌▽───────────────────────┐┌▽───────────────────────────┐              
    │user_inputs       ││sweep_transmission      ││propagation_mode            │              
    └┬────────────────┬┘└───────────────────────┬┘└───────────────────────────┬┘              
    ┌▽──────────────┐┌▽───────────────────────┐┌▽───────────────────────────┐┌▽──────────────┐
    │lumerical_files││user_sweep_parameters.py││sweep_radius_transmission.py││mode_profile.py│
    └┬──────────────┘└────────────────────────┘└────────────────────────────┘└───────────────┘
    ┌▽─────────────────┐                                                                      
    │waveguide_bend.lms│                                                                      
    └──────────────────┘                                                                      
    
    

### Quick Simulation Setup

1. After downloading the repository, navigate through the `waveguide-bend/user_inputs/lumerical_files` directory.
2. Edit the lumerical file template`waveguide_bend.lms` and define the simulation materials for the cladding, core, and box layers along with their dimensions. 
3. Edit the `user_sweep_parameters.py` to define the simulation sweep parameters. Follow the comment-sections written in the file.
4. Run the `sweep_transmission/swee_radius_transmission.py` Python file to get the results.
   1. You can also run the `propagation_mode/mode_profile.py` to see the E-fields at the bending section

Tip: Low-index contrast material platforms such as silica have larger bending radius than high-index contrast material platforms

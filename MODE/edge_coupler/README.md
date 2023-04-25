## 2D Edge-Coupler Simulations (MODE Solutions)

    ┌─────────┐┌───────────────────────────┐                      
    │waveguide││edge_coupler               │                      
    └─────────┘└┬──┬──────────────────────┬┘                      
    ┌───────────▽┐┌▽────────────────────┐┌▽──────────────────────┐
    │user_inputs ││overlap_profile_sweep││gaussian_beam_render.py│
    └┬───────────┘└───────────────┬─────┘└───────────────────────┘
    ┌▽──────────────────────────┐┌▽──────────────────────────┐    
    │gaussian_beam_parameters.py││overlap_profile_sweep_2D.py│    
    └───────────────────────────┘└───────────────────────────┘    

### Quick Simulation Setup

1. After downloading the repository, navigate through the `edge_coupler/user_inputs/` directory.
2. Edit the parameter file `gausian_beam_parameters.py` to define the Gaussian beam parameter properties (i.e. waist-radius, index, sample span, etc). 
3. Edit the `user_inputs/user_materials.py` and `user_inputs/user_simulation_parameters.py` to define the simulation materials for the cladding, core, box, and substrate layers. Follow the instructions written in the file.
4. Then define the in `user_inputs/user_sweep_parameters.py` the sweep parameters.
5. Run the `overlap_profile_sweep/overlap_profile_sweep_2D.py` Python file and get the overlap integral results.

Tip: The script works only with the two fundamental polarizations namely TE and TM. If the Gaussian beam angle is set to 0<sup>o</sup> the script will calculate the overlap integral for TE mode. Setting the angle to 90<sup>o</sup>, the script will calculate the overlap integral for TM.

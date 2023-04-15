## Edge-Coupler Simulations (MODE Solutions)

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

1. After downloading the repository, navigate through the `edge-coupler/user_inputs/` directory.
2. Edit the parameter file `gausian_beam_parameters.py` to define the Gaussian beam parameter properties (i.e. waist-radius, index, sample span, etc). 
3. Navigate to the [waveguide](../waveguide) repository to define the waveguide properties including the width sweep variations. 
4. Run the `overlap_profile_sweep/overlap_profile_sweep_2D.py` Python file and get the overlap integral results.

Tip: The script works only with the two fundamental polarization of TE and TM. If the Gaussian beam angle is 0deg the script will calculate the overlap integral for TE. Setting the angle to 90deg, the script will calculate the overlap integral for TM.

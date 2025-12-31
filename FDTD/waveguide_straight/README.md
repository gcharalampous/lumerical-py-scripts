## 3D Waveguide Simulations (FDTD)
                                                                                                     
                      +---------------------+                                                        
            +----------- waveguide-straight  ----+-------------------+---------------------+         
            |          +----------|----------+   |                   |                     |         
            |                     |              |                   |                     |         
            |                     |              |                   |                     |         
            v                     v        +-----v-----+   +---------v--------+   +--------v--------+
    waveguide_render.py   fdtd_region.py   |user-inputs|   |sweep-transmission|   |propagation-mode |
                                           +-----|-----+   +---------|--------+   +--------|--------+
                                                 |                   |                     |       
                      +-----------+--------------|                   v                     |       
                      |           |              |      sweep_width_transmission.py        |       
                      |           |              |                                         |       
                      |           |              v                                         v       
                      |           |  user_simulation_parameters.py                  mode_profile.py
                      |           v        
                      |   user_materials.py
                      v             
            user_sweep_parameters.py    

### Quick Simulation Setup

1. After downloading the repository, navigate through the `waveguide-straight/user-inputs` directory.
2. Edit the `user_materials.py` to define the simulation materials for the cladding, core, box, and substrate layers. Follow the instructions written in the file.
3. Edit the `user_simulation_parameters.py` to define the simulation properties, region and structure dimensions. Follow the instructions written in the file.
4. Edit the `user_sweep_parameters.py` to define the parameters to sweep, like the waveguide width.
5. Navigate under the `waveguide-straight/propagation-mode` and run ` mode_profile.py`file to calculate the transmission for fundamental TE or TM modes and watch the propagated E-field profiles.

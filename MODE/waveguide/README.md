## 2D Waveguide Simulations (MODE Solutions)

                        +-----------+                                                                                                                          
               +------- | waveguide |--------------------+--------------+
               |        +-----------+   |                |              |
               |              |         |                v              v
               |              |   +-----v-----+  +-------------+  +----------+
               |              |   |user-inputs|  |mode profile |  |neff-sweep|
               |              |   +-----------+  +-------------+  +----------+
               v              v         |               |              |      
    waveguide_render.py fde_region.py   |               v              |      
                                        |        mode_profile_2D.py    |      
                +--------------+--------|----+                         v      
                |              v             |            neff_width_sweep_2D.py
                |      user_materials.py     |                                 
                v                            v                                 
     user_sweep_parameters.py  user_simulation_parameters.py              

### Quick Simulation Setup

1. After downloading the repository, navigate through the `waveguide/user-inputs` directory.
2. Edit the `user_materials.py` to define the simulation materials for the cladding, core, box, and substrate layers. Follow the instructions written in the file.
3. Edit the `user_simulation_parameters.py` to define the simulation properties, region and structure dimensions. Follow the instructions written in the file.
4. Navigate under the `waveguide/mode_profile` or `waveguide/neff_sweep` directories to run the desired python file.

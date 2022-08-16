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
                               +--------|----+                         v        
                               v             |            neff_width_sweep_2D.py
                       user_materials.py     |                                
                                             v              
                               user_simulation_parameters.py



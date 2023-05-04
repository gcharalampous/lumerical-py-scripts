#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are required.

In this file, the user is rmust enter the parameters required to setup the
simulation file. The simulation parameters along with their dimensions are
presented below.

                                                                  
                                   simulation_span_x                                                                  
                                                                                                                      
     clad_max_y    <---------------------------------------------->                                                   
          ------ ^ +----------------------------------------------+                                                   
                   | Cladding         wg_width                    |                                                   
                   |+--------------------------------------------+| ^                                                 
                   ||                <---------->                || |                                                 
                   ||               +-----------+ ^              || |                                                 
                   ||               |           | | wg_thickness || |                                                 
                   ||               | waveguide | |              || |                                                 
     clad_min_y    ||               |           | v              || |                                                 
          ------ ^ +|--------------------------------------------|+ | simulation_span_y                               
  box_thickness  | ||                    Box                     || |                                                 
          ------ v +|--------------------------------------------|+ |                                                 
                 ^ ||                                            || |                                                 
                 | ||                               FDE region   || |                                                 
   sub_thickness | |+--------------------------------------------+| v                                                 
                 | |                                              |                                                   
                 | | Substrate                                    |                                                   
                 v +----------------------------------------------+                                                   
                                                                                                                      
  
 Be aware, the waveguide 'y min = 0' starts at zero and it is centered at the 
'x=0'.
                                                                                                                                 
                                                                                                             
               ^                                                                         
               |                                                                         
               |                                                                         
               |                    -                                                    
            wg_width                                                                     
        <--------------->                                                                
       +-------|--------+ ^                                                              
       |       |        | |                                                              
       |   waveguide    | | wg_thickness                                                 
       |       |        | |                                                              
   ------------|----------v--------------------->                                        
          (0,0)|                                                                         
               |                                                                         
               |                                                                         
               |                                                                         


In addition, there is a mesh layer with the exact dimensions as the waveguide, which
is not shown on the figures above. You can disable it by selecting 'mesh_enable = False'.


The user needs to define
1. The span of the simulation region, along with other FDE parameters from the template files
2. FDE simulation parameters, like the number of trial modes, the wavelength and
the number of mesh cells across the x and y axes.
3. A mesh with equal dimensions and coordinates as the waveguide. Set 'mesh_enable = True' 
for enabling the mesh. Overide mesh across x and y axes with 'dx' and 'dy', respectively.
4. Set the DPI of your screen for getting the right image resolution.

Warning: The FDE simulation parameters will overide the FDE simulation parameters you defined
in the two lumerical template files.
"""


# Length units are in meters!

# 1. FDE Parameters. 
num_modes = 20
wavelength = 4.0e-6
fde_mesh_cell_y = 200
fde_mesh_cell_z = 200

# 2. Mesh (waveguide)
mesh_enable = False
mesh_dx = 5e-9
mesh_dy = 5e-9


# 3. Overlap Intgral
# Pick the order of modes you want to overlap

# 3.1 Waveguide_1.lms
m_waveguide1=5

# 3.2 Waveguide_2.lms
m_waveguide2=10


# 4. Figures
my_dpi = 96

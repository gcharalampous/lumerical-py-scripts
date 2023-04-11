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
1. The span of the simulation region
2. The ''y min'' and ''y max'' of the cladding 
3. The waveguide width and thickness.
4. The thickness of the Box Layer sitting below the waveguide
5. The thickness of the Substrate Layer sitting below the box layer
6. FDE simulation parameters, like the number of trial modes, the wavelength and
the number of mesh cells across the x and y axes.
7. A mesh with equal dimensions and coordinates as the waveguide. Set 'mesh_enable = True' 
for enabling the mesh. Overide mesh across x and y axes with 'dx' and 'dy', respectively.
8. Set the DPI of your screen for getting the right image resolution.
"""


# Length units are in meters!


# 1. Simulation Paramters
simulation_span_x = 10e-6
simulation_span_y = 10e-6


# 2. Cladding Dimensions. Note, waveguide y min = 0.
clad_min_y = 0e-6
clad_max_y = 5e-6


# 3. Waveguide Dimensions
wg_width = 1.2e-6
wg_thickness = 0.22e-6

# 3.1 Bend Waveguide at the center of the simualation ?
bend_waveguide = False
bend_radius = 25e-6
bend_orientation = 0

# 4. Box Layer Thickness
box_thickness = 5.0e-6


# 5. Substrate Layer Thickness
sub_thickness = 5e-6


# 6. FDE Parameters. 
num_modes = 2
wavelength = 1.31e-6
fde_mesh_cell_x = 300
fde_mesh_cell_y = 300

# 7. Mesh (waveguide)
mesh_enable = True
mesh_dx = 5e-9
mesh_dy = 5e-9



# 8. Figures
my_dpi = 96

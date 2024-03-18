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
simulation_span_x = 8e-6
simulation_min_z = -3.0e-6
simulation_max_z = 3.5e-6


# 2. Cladding Dimensions. Note, waveguide y min = 0.
clad_min_y = 0e-6
clad_max_y = 1.0e-6


# 3. Waveguide Dimensions
wg_width = 0.5e-6
wg_thickness = 0.3e-6
wg_angle = 80  #deg

# 3.2 Set slab thickness > 0 to enable a slab waveguide
slab_thickness = 0.05e-6


# 3.3 Metal Layer
metal_left_width = 1e-6
metal_center_width = metal_left_width
metal_right_width = metal_left_width
metal_thicknes = 1.0e-6
metal_pitch = 2.0e-6


# 3.3.1 GSG Pads
GSG_pads_enable = True  # False = GS Pads


# 3.4 Voltage of Signal and Ground
v_signal = 1


# 4. Box Layer Thickness
box_thickness = abs(simulation_min_z)


# 5. Substrate Layer Thickness
sub_thickness = 10e-6


# 6. Charge Parameters. 
# 6.1 
min_edge_length = 4e-9
max_edge_length = 600e-9


# 3D Expansion
norm_length = 1e-6


# 7. Mesh (waveguide)
mesh_enable = True
max_edge_length_mesh_override = 500e-9


# 8. Figures
my_dpi = 96

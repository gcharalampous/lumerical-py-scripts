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
simulation_span_x = 5e-6
simulation_min_y = -2.0e-6
simulation_max_y = 2.0e-6


# 2. Cladding Dimensions. Note, waveguide y min = 0.
clad_min_y = 0e-6
clad_max_y = 5.0e-6


# 3. Waveguide Dimensions
wg_width = 0.48e-6
wg_thickness = 0.22e-6


# 3.1 Set slab thickness > 0 to enable a slab waveguide
slab_thickness = 0.110e-6


# 3.2 Bend Waveguide at the center of the simualation ?
bend_waveguide = False
bend_radius = 5e-6
bend_orientation = 0

disk_enable = False        # If False, ring resonator



# 3.3 Distance of the p++ boundary to the pn junction centre
doping_enable = False     # Set True to Enable doping profiles
offset_P = 1e-6
offset_N = 1e-6
doping_P_depth = 40e-9
doping_N_depth = 50e-9

# 3. 4. Metal Layer Stack (You can use a metal stuck using arrays)
metal_layer_enable = False
metal_xmin = [-0.5e-6, -0.5e-6]
metal_xmax = [ 0.5e-6, 0.5e-6]
metal_thickness = [10.0e-9, 200.0e-9]
metal_min_y = [1e-6, 1e-6 + metal_thickness[0]]
# clad_max_y = metal_min_y[0]


# 3.5 PCM material
pcm_layer_enable = False
pcm_thickness = 20e-9
pcm_width = 0.9*wg_width


# 4. Box Layer Thickness
box_thickness = 6.0e-6


# 5. Substrate Layer Thickness
sub_thickness = 10e-6


# 6. FDE Parameters. 
num_modes = 6
wavelength = 1.55e-6
fde_mesh_cell_x = 300
fde_mesh_cell_y = 300


# 6.1 FDE Boundaries
fde_xmax_boundary = 'Metal'
fde_ymax_boundary = 'Metal'
fde_ymin_boundary = 'Metal'


# 7. Mesh (waveguide)
mesh_enable = True
mesh_dx = 5e-9
mesh_dy = 5e-9


# 8. Figures
my_dpi = 96
colormesh_plot_log = True
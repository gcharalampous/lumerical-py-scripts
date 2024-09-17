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
simulation_min_y = -2.5e-6
simulation_max_y = 2.5e-6


# 2. Cladding Dimensions. Note, waveguide y min = 0.
clad_min_y = 0e-6
clad_max_y = simulation_max_y


# 3. Waveguide Dimensions
wg_width = 0.48e-6
wg_thickness = 0.22e-6


# 3.1 Set slab thickness > 0 to enable a slab waveguide
slab_thickness = 0.11e-6


# 3.2 Plateau Left and Right
plateau_width = 2.5e-6
plateau_thickness = wg_thickness


# 3.3 Metal Anode and Cathode
metal_anode_width = 1.2e-6
metal_cathode_width = metal_anode_width

# 3.4 Voltage of Anode and Cathode
v_cathode = 0
v_anode = 0

# 3.5 Distance of the p++ and n++ boundaries to the pn junction centre
offset_Ppp = 1.0e-6
offset_Nnn = 1.0e-6

doping_P_depth = 40e-9
doping_N_depth = 50e-9

# 3.6 Recombination models
## 3.6.1 Metal to semiconductor
semi_metal_enabled = True
e_velocity_semi_metal = 1e5            # m/s
h_velocity_semi_metal =  1e5           # m/s

## 3.6.2
semi_oxide_enabled = True
e_velocity_semi_oxide = 100e-2          # m/s
h_velocity_semi_oxide =  100e-2         # m/s


# 4. Box Layer Thickness
box_thickness = 2.5e-6


# 5. Substrate Layer Thickness
sub_thickness = 10e-6


# 6. Charge Parameters. 
# 6.1 Device mesh settings
min_edge_length = 4e-9
max_edge_length = 200e-9
max_refine_steps = 40000

# 3D Expansion (Don't change, unless you change the plot units)
norm_length = 1e-6

# 6.2 Solver Type ('newton' or 'gummel)
solver_type = 'gummel'

# 7. Mesh (waveguide)
mesh_enable = True
max_edge_length_mesh_override = 100e-9



# 8. Figures
my_dpi = 96

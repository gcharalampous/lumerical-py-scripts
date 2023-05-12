#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are required.

In this file, the user is must enter the parameters required to setup the
simulation file. The simulation parameters along with their dimensions are
presented below.

                                                                  
                                   simulation_span_y                                                                  
                                                                                                                      
     clad_max_z    <---------------------------------------------->                                                   
          ------ ^ +----------------------------------------------+                                                   
                   | Cladding         wg_width                    |                                                   
                   |+--------------------------------------------+| ^                                                 
                   ||                <---------->                || |                                                 
                   ||               +-----------+ ^              || |                                                 
                   ||               |           | | wg_thickness || |                                                 
                   ||               | waveguide | |              || |                                                 
     clad_min_z    ||               |           | v              || |                                                 
          ------ ^ +|--------------------------------------------|+ | simulation_span_z                               
  box_thickness  | ||                    Box                     || |                                                 
          ------ v +|--------------------------------------------|+ |                                                 
                 ^ ||                                            || |                                                 
                 | ||                              FDTD region   || |                                                 
   sub_thickness | |+--------------------------------------------+| v                                                 
                 | |                                              |                                                   
                 | | Substrate                                    |                                                   
                 v +----------------------------------------------+                                                   
                                                                                                                      
  
 Be aware, the waveguide 'z min = 0' starts at zero and it is centered at the 
'y=0'.
                                                                                                                                 
                                                                                                             
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
  (y=0,z min=0)|                                                                         
               |                                                                         
               |                                                                         
               |                                                                         



The user needs to define
1. The span of the simulation region
2. The ''z min'' and ''z max'' of the cladding 
3. The waveguide width and thickness.
4. The thickness of the Box Layer sitting below the waveguide
5. The thickness of the Substrate Layer sitting below the box layer
6. FDTD simulation parameters, like the mesh accuracy, the wavelength and
the polarization and dimensions of the source (TM/TE).
7. Set the polarizion of the fundamental mode (TM/TE).
8. Set the DPI of your screen for getting the right image resolution.
"""


# Length units are in meters!


# 1. Sub-wavelength Grating Parameters

# 1.1. Waveguide Dimensions
wg_width = 6e-6
wg_thickness = 2e-6

# 1.2. Grating Properties
mirror_periods = 500
pitch = 0.52e-6
duty_cycle = 0.5
etch_depth = 0.2e-6





# 2. FDTD Simulation Parameters

# 2.1 FDTD Span Region
simulation_span_y = 20e-6
simulation_span_z = 20e-6
simulation_time = 35e-12

# 2.2.1. Mesh Settings 
mesh_accuracy = 1

# 2.2.2. Override Mesh Settings
mesh_dx = pitch/10
mesh_dy = pitch/10
mesh_dz = pitch/10
enable_dx = 1
enable_dy = 1
enable_dz = 0


# 2.3 Source/Monitor Properties
wavelength_start = 3.5e-6
wavelength_stop = 4.5e-6
mode_fundamental = "TM"             # Select TE for fundamental TE or TM for fundamental TM
frequency_points = 512

# 2.4. Port extension
port_extension = 5e-6


# 3. Figures
my_dpi = 96


# -------------------------- End of Input Section -----------------------------


if(mode_fundamental == "TE"):
    mode_monitor = "Linear X"
else:
    mode_monitor = "Linear Y"  
    
    

if(mode_fundamental == "TE"):
    mode_source = "fundamental mode"
else:
    mode_source = "fundamental mode"  

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


# 1. Simulation Paramters
simulation_span_x = 20e-6
simulation_span_y = 40e-6
simulation_span_z = 35e-6
offset_x = 1e-6 

# 2. Cladding Dimensions. Note, waveguide y min = 0.
clad_min_z = 0e-6
clad_max_z = 10e-6


# 3. Waveguide Dimensions
wg_width = 14.0e-6
wg_thickness = 1.5218e-6
wg_length =simulation_span_x

# 4. Box Layer Thickness
box_thickness = 5e-6


# 5. Substrate Layer Thickness
sub_thickness = 5e-6


# 6. FDTD Parameters. 
mode_source = "TM"             # Select TE for fundamental TE or TM for fundamental TM
source_span_y = 5e-6
source_span_z = 5e-6

wavelength_start = 3.8e-6
wavelength_stop = wavelength_start # Only Single Frequency is supported at the moment

mesh_accuracy = 2

# 7. Monitor
mode_monitor = "TM"             # Select TE for fundamental TE or TM for fundamental TM


# 9. Figures
my_dpi = 96


# -------------------------- End of Input Section -----------------------------


if(mode_monitor == "TE"):
    mode_monitor = "fundamental TE mode"
else:
    mode_monitor = "fundamental TM mode"  
    
    

if(mode_source == "TE"):
    mode_source = "fundamental TE mode"
else:
    mode_source = "fundamental TM mode"  

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

----- 2D Cross-section
                                   
        ^ z-axis               
        |                      
        |                      
        |                      
        |                      
        |                      
      x o ------------- >  y-axis                           

                                       
                                   simulation_span_y                                                                  
                                                                                                                      
     clad_max_z    <---------------------------------------------->                                                   
          ------ ^ +----------------------------------------------+                                                   
                   | Cladding         wg_width                    |   ------ simulation_max_z                                               
                   |+--------------------------------------------+| ^                                                 
                   ||                <---------->                || |                  
                   ||               +-----------+ ^              || |                  
                   ||               |           | | wg_thickness || |                  
                   ||               | waveguide | |              || | simulation_span_z
     clad_min_z    ||               |           | v              || |                                                 
          ------ ^ +|--------------------------------------------|+ | 
  box_thickness  | ||                    Box                     || |                                                 
          ------ v +|--------------------------------------------|+ |                                                 
                 ^ ||                                            || |                                                 
                 | ||                              FDTD region   || |                                                 
   sub_thickness | |+--------------------------------------------+| v                                                 
                 | |                                              |   ------ simulation_min_z                                              
                 | | Substrate                                    |                                                   
                 v +----------------------------------------------+                                                   
                                                                                                                      
  
 Be aware, the waveguide 'z min = 0' starts at zero and it is centered at 'y=0'.
                                                                                                                                 
                                                                                                             
               ^                                                                         
               |                                                                         
               |                                                                         
               |                                                                        
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



----- 2D Top-down View


                                                                               
                ^ y-axis               
                |                      
                |                      
                |                      
                |                      
                |                      
              z o ------------- >  x-axis


                      taper_length        offset_x
                  <-------------------><---------------->                                                                                                                    
                  +-------------------------------------+                                                                                       
                  |                                     |                                                                                       
                  |             Cladding                |                                                                                         
               ^  |------                               | 
               |  |      ------                         |                              
               |  |            ------                   |
               |  |                   ------------------| ^
 wg_width_left |  |          taper    |     waveguide   | | wg_width_right
               |  |                   ------------------| v
               |  |             ------                  |
               |  |       ------                        |
               |  | ------                              |
               v  |                                     |
                  |-------------------------------------|                                                                                       
      
                  
                  <------------------------------------->
                            simulation_span_x


The user needs to define
1. The ''z min'' and ''z max'' of the cladding 
2. The waveguide width and thickness.
3. The thickness of the Box Layer sitting below the waveguide (z max = 0)
4. The thickness of the Substrate Layer sitting below the box layer
5. The span of the simulation region
6. FDTD simulation parameters, like the mesh accuracy, the wavelength and
the polarization and dimensions of the source (TM/TE).
7. Set the polarizion of the fundamental mode (TM/TE).
8. Set the DPI of your screen for getting the right image resolution.
"""


# Length units are in meters!


# 1. Cladding Dimensions. Note, waveguide sits on 'z min = 0'
clad_min_z = 0e-6               # No need to change
clad_max_z = 10e-6


# 2. Waveguide Dimensions
wg_width_left = 1.2e-6          # Taper start width
wg_width_right = 3.0e-6         # Taper end width
wg_thickness = 0.15e-6          # Taper and waveguide thickness
taper_length = 100e-6           # Taper Length
poly_res = 10                   # Polygon Resolution
m = 1                           # Taper order
offset_x = 5e-6                 # Extends the waveguide structure beyond simulation region


# 3. Box Layer Thickness
box_thickness = 10e-6


# 4. Substrate Layer Thickness
sub_thickness = 5e-6


# 5. Simulation Paramters
#simulation_span_x = taper_length + offset_x  ---- The values are defined later
simulation_span_x = taper_length + offset_x
simulation_span_y = 20e-6
simulation_max_z = clad_max_z - 1e-6
simulation_min_z = -box_thickness


# 6. FDTD Parameters. 
mode_source = "TE"              # Select TE for fundamental TE or TM for fundamental TM
wavelength_start = 1.31e-6      
wavelength_stop = wavelength_start# Only Single Frequency is supported at the moment
mesh_accuracy = 1
simulation_time = 5000e-15
source_span_y = simulation_span_y
source_span_z = abs(simulation_max_z - simulation_min_z)


# 7. Monitor
mode_monitor = "TE"             # Select TE for fundamental TE or TM for fundamental TM


# 9. Figure Screen Resolution
my_dpi = 96




# -------------------------- End of User Input Section -----------------------------


if(mode_monitor == "TE"):
    mode_monitor = "fundamental TE mode"
else:
    mode_monitor = "fundamental TM mode"  
    
    

if(mode_source == "TE"):
    mode_source = "fundamental TE mode"
else:
    mode_source = "fundamental TM mode"  

simulation_span_z = abs(simulation_max_z - simulation_min_z)


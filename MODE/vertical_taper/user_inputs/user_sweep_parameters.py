#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are required.

In this file, the user is rmust enter the parameters required to sweep. 

The waveguide parameters to sweep are 'wg_width' for each Taper.


               ^                                                                         
               |                                                                         
               |                                                                         
               |                    -                                                    
            wg_width                                                                     
        <--------------->                                                                
       +-------|--------+ ^                                                              
       |       |        | |                                                              
       |   waveguide    | | Thickness defined in Lumerical File                                                 
       |       |        | |                                                              
   ------------|----------v--------------------->                                        
          (0,0)|                                                                         
               |                                                                         
               |                                                                         
               |                                                                         

"""

# 1. Simulation Parameters
num_modes = 4

# 2. Taper length parameters
res = 30                            # Ressolution of polygon, thus, loop itterations
m=1                                 # Order of the taper
taper_length = 200e-6;              # Total length of the taper

# 3. Taper width parameters
# 3.1 Choose the waveguide width on left side 'width_wg_left' 
width_wg_left_1 = 1.2e-6;
width_wg_right_1 = 0.25e-6;
# 3.2 Choose the waveguide width on right side 'width_wg_right' 
width_wg_left_2 = 0.25e-6;
width_wg_right_2 = 1.2e-6;

# 4 Figure plot DPI
my_dpi = 96




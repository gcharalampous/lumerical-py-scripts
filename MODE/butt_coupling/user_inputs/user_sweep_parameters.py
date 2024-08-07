#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are required.

In this file, the user is must enter the parameters required to sweep. 

The waveguide parameters to sweep are 'wg_2_width', which is the width
of the waveguide_2.lms file only. 

The width from waveguide_1.lms is held constant. It can be changed from the
user_simulation_paramaters.py


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

"""



wg_2_width_start = 0.250e-6    # Choose the start width for waveguide-2 'wg_2_width_start' 
wg_2_width_stop = 10.0e-6      # Choose the stop width for waveguide-2 'wg_2_width_stop' 
wg_2_width_step = 0.50e-6     # Choose the step width for waveguide-2 'wg_2_width_step'  



# Misalign the two beams in y (horizontal) or z (vertical) directions
misalign_y_start = -5e-6
misalign_y_stop = 5e-6
misalign_y_step = 0.5e-6


misalign_z_start  = -5e-6
misalign_z_stop = 5e-6
misalign_z_step  = 0.25e-6


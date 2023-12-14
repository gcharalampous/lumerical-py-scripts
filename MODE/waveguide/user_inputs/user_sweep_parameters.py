#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are required.

In this file, the user is rmust enter the parameters required to sweep. 

The waveguide parameters to sweep are 'wg_thickness' and 'wg_width' .



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




wg_width_start = 0.10e-6            # Choose the start waveguide width 'wg_width_start' 
#you want to start sweeping
wg_width_stop = 1.10e-6             # Choose the stop waveguide width 'wg_width_stop' you 
#want to finish sweeping
wg_width_step = 0.10e-6             # Choose the step of each sweep 'wg_width_step'




wg_height_start = 0.05e-6           # Choose the start waveguide height 'wg_height_start' 
#you want to start sweeping
wg_height_stop = 0.55e-6            # Choose the stop waveguide height 'wg_height_stop' you 
#want to finish sweeping
wg_height_step = 0.05e-6            # Choose the step of each sweep 'wg_height_step'


track_mode = 'TE'                   # Select the fundamental mode to track 'track_mode = 'TE' or 'TM'
PropagationLoss_dB_cm = 2.5         # Propagation loss for the Q-factor radius sweep in dB/cm
wg_radius_start = 3.0e-6            # Choose the start waveguide radius 'wg_radius_start' you want to start sweeping
wg_radius_stop = 8.0e-6             # Choose the stop waveguide radius 'wg_radius_stop' you  want to finish sweeping
wg_radius_step = 0.50e-6            # Choose the step of each sweep 'radius'



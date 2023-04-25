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




wg_width_start = 0.050e-6     # Choose the start waveguide width 'wg_width_start' 
#you want to start sweeping
wg_width_stop = 3.0e-6      # Choose the stop waveguide width 'wg_width_stop' you 
#want to finish sweeping
wg_width_step = 0.10e-6     # Choose the step of each sweep 'wg_width_step'




wg_height_start = 0.05e-6     # Choose the start waveguide height 'wg_height_start' 
#you want to start sweeping
wg_height_stop = 0.50e-6      # Choose the stop waveguide height 'wg_height_stop' you 
#want to finish sweeping
wg_height_step = 0.025e-6     # Choose the step of each sweep 'wg_height_step'



waist_start = 1.0e-6     # Choose the start waist radius 'waist_start' 
#you want to start sweeping
waist_stop = 6.0e-6      # Choose the stop waist radius 'waist_stop' you 
#want to finish sweeping
waist_step = 0.5e-6     # Choose the step of waist step 'waist_step'

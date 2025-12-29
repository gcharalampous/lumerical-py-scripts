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

import numpy as np

num_modes = 10               # Choose the number of modes you want to track

# Set the name of the structure you want to track


# Waveguide

wg_width_start = 0.1e-6     # Choose the start waveguide width 'wg_width_start'
#you want to start sweeping
wg_width_stop = 1.0e-6      # Choose the stop waveguide width 'wg_width_stop' you
#want to finish sweeping
wg_width_step = 0.10e-6     # Choose the step of each sweep 'wg_step'


# Mesa
mesa_width_start = 0.250e-6     # Choose the start waveguide width 'wg_width_start'
#you want to start sweeping
mesa_width_stop = 4.250e-6      # Choose the stop waveguide width 'wg_width_stop' you
#want to finish sweeping
mesa_width_step = 0.25e-6     # Choose the step of each sweep 'wg_step'


wg_width_array = []
mesa_width_array = []

wg_width_array = np.arange(wg_width_start, wg_width_stop, wg_width_step) 
mesa_width_array = np.arange(mesa_width_start, mesa_width_stop, mesa_width_step) 
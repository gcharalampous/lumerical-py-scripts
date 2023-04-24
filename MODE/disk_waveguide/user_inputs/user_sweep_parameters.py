#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are required.

In this file, the user is rmust enter the parameters required to sweep. 

The waveguide parameters to sweep are 'wg_thickness' .



               ^                                                                         
               |                                                                         
               |                                                                         
               |                    -                                                    
        ------------->                                                                
       +-------|--------+ ^                                                              
               |        | |                                                              
           waveguide    | | wg_thickness                                                 
               |        | |                                                              
   ------------|----------v--------------------->                                        
          (0,0)|                                                                         
               |                                                                         
               |                                                                         
               |                                                                         

"""




wg_height_start = 0.01e-6     # Choose the start waveguide height 'wg_height_start' 
#you want to start sweeping
wg_height_stop = 0.50e-6      # Choose the stop waveguide height 'wg_height_stop' you 
#want to finish sweeping
wg_height_step = 0.025e-6     # Choose the step of each sweep 'wg_height_step'



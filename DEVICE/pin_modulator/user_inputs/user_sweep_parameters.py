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



# Voltage Sweep
v_anode_start = -0.75
v_anode_stop = 2.0
v_anode_step = 0.1
v_num_pts = int((v_anode_stop - v_anode_start)/v_anode_step)+1


offset_P_start = 0.0e-6                     # Choose the start clear width (offset) 'offset_P_start' 
offset_P_stop = 1.1e-6                     # Choose the stop clear width (offset) 'offset_P_stop'  
offset_P_step = 0.1e-6                     # Choose the step clear width (offset) 'offset_P_step'

offset_N_start = offset_P_start             # Choose the start clear width (offset) 'offset_N_start' 
offset_N_stop = offset_P_stop               # Choose the stop clear width (offset) 'offset_N_stop'  
offset_N_step = offset_P_step               # Choose the step clear width (offset) 'offset_N_step'
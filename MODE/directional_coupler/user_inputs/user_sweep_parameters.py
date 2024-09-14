#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are required.



            wg1_width    gap     wg2_width
        <---------------><--><--------------->
       +-------^--------+ ^ +-------^--------+ ^
       |       |        | | |       |        | |
       |  waveguide-1   | | |  waveguide-2   | | wg_thickness
       |       |        | | |       |        | |
   ------------v----------v---------V----------v--->                                        
                     (0,0)|



In addition, there is a mesh layer which overlaps both waveguide-1 and waveguide-2.
You can disable it from the .lms file in order to speed up the simulation results


"""

# 1. Define the coupling length array
coupling_length_start = 1e-6
coupling_length_stop = 80e-6
coupling_length_step = 0.5e-6

# 2. Define the coupling gap array
coupling_gap_start = 0.1e-6
coupling_gap_stop = 0.5e-6
coupling_gap_step = 0.05e-6
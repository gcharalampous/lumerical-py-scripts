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


num_modes = 4       # Typically (2x modes per polarization - symm/anti-symm)


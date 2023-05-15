#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The script overrides the FDTD region for the vertical taper simulation.


"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import lumapi
from FDTD.vertical_taper.user_inputs.user_simulation_parameters import *  
from config import FDTD_VERTICAL_DIRECTORY_READ



def override_vertical_taper(fdtd):
   
    fdtd.switchtolayout()

    
    configuration = (
    ("taper-bottom",            (("width_wg_left", wg_bottom_width_left),
                                 ("width_wg_right", wg_bottom_width_right),
                                 ("taper_thickness", wg_bottom_thickness),
                                 ("rib_thickness", wg_bottom_rib_thickness))),
    
    
    ("taper-top",               (("width_wg_left", wg_top_width_left),
                                 ("width_wg_right", wg_top_width_right),
                                 ("taper_thickness", wg_top_thickness),
                                 ("rib_thickness", wg_top_rib_thickness))),
    
    ("::model",                 (("taper_gap", taper_gap),
                                 ("taper_length", taper_length),
                                 ("port_extension", port_extension),
                                 ("FDTD_y_span", simulation_span_y),
                                 ("FDTD_z_span", simulation_span_z))),
    
    
    )


    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               fdtd.setnamed(obj, k, v)

    fdtd.save()

# ---------------------------------------------------------------------------


if(__name__=="__main__"):
    
    with lumapi.FDTD(FDTD_VERTICAL_DIRECTORY_READ) as fdtd:
        override_vertical_taper(fdtd=fdtd)



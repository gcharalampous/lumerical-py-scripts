#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The script sets the FDTD region for the sub-wavelength grating simulation.

There are in total

1. ...
"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import lumapi
from FDTD.swg_grating.user_inputs.user_simulation_parameters import *  
from config import FDTD_SWG_DIRECTORY_READ



def override_swg(fdtd):
   
    fdtd.switchtolayout()

    
    configuration = (
    ("grating-constructor",     (("wg_width", wg_width),
                                 ("wg_thickness", wg_thickness),
                                 ("mirror_periods", mirror_periods),
                                 ("pitch", pitch),
                                 ("duty_cycle", duty_cycle),
                                 ("etch_depth", etch_depth))),
    
    
    )

    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               fdtd.setnamed(obj, k, v)

    fdtd.save()

# ---------------------------------------------------------------------------


if(__name__=="__main__"):
    
    with lumapi.FDTD(FDTD_SWG_DIRECTORY_READ) as fdtd:
        override_swg(fdtd=fdtd)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The script sets the MODE region for the sub-wavelength grating simulation.

There are in total

1. ...
"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import lumapi
from MODE.swg_grating.user_inputs.user_simulation_parameters import *  
from project_layout import setup

spec, out, templates = setup("mode.swg_grating", __file__)



def override_swg(mode):
   
    mode.switchtolayout()

    
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
               mode.setnamed(obj, k, v)

    mode.save()

# ---------------------------------------------------------------------------


if(__name__=="__main__"):
    
    with lumapi.MODE(str(templates[0])) as mode:
        override_swg(mode=mode)



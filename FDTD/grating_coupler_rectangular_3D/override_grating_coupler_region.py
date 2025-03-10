#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The script overrides the FDTD region for the edge coupler taper simulation.


"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import lumapi
from FDTD.grating_coupler_2D.user_inputs.user_simulation_parameters import *  
from config import FDTD_GRATING_COUPLER_2D_DIRECTORY_READ



def override_grating_coupler(fdtd):
   
    fdtd.switchtolayout()

    
    configuration = (
         ("::model", (
            ("cladding_thickness", cladding_thickness),
            ("box_thickness", box_thickness),
        )),

        ("grating_coupler", (
            ("wg_thickness", wg_thickness),
            ("slab_thickness", slab_thickness),
            ("grating_period", period),
            ("fill_factor", fill_factor),
            ("gc_sections", gc_sections),
            ("port_extension", port_extension)
        )),

    )


    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               fdtd.setnamed(obj, k, v)

    fdtd.save()

# ---------------------------------------------------------------------------


if(__name__=="__main__"):
    
    with lumapi.FDTD(FDTD_GRATING_COUPLER_2D_DIRECTORY_READ) as fdtd:
        override_grating_coupler(fdtd=fdtd)



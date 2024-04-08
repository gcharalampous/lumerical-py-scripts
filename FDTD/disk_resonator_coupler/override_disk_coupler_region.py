#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The script overrides the FDTD region for the ring coupler simulation.


"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import lumapi
from FDTD.disk_resonator_coupler.user_inputs.user_simulation_parameters import *  
from config import FDTD_DISK_DIRECTORY_READ
from FDTD.disk_resonator_coupler.user_inputs.user_simulation_parameters import *




def override_disk_coupler(fdtd):
   
    fdtd.switchtolayout()

    
    configuration = (
    ("ring",  (("ring_radius", ring_radius),
                        ("wg_bus_width", wg_bus_width),
                        ("wg_thickness", wg_thickness),
                        ("slab_thickness", slab_thickness),
                        ("bus_angle", bus_angle),
                        ("gap", gap))),
    
    )


    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               fdtd.setnamed(obj, k, v)

    fdtd.save()

# ---------------------------------------------------------------------------


if(__name__=="__main__"):
    
    with lumapi.FDTD(FDTD_DISK_DIRECTORY_READ[file_index]) as fdtd:
        override_disk_coupler(fdtd=fdtd)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The script overrides the FDTD simulation region from the *.fsp files.


"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import lumapi
from FDTD.ring_resonator_coupler.user_inputs.user_simulation_parameters import *
from config import FDTD_RING_DIRECTORY_READ

def override_fdtd(fdtd):
   
    fdtd.switchtolayout()
    
    configuration = (
         
    ("source",  (("mode selection", mode_polarization),
                 ("wavelength start", wavelength_start),
                 ("wavelength stop", wavelength_stop))),
    
    ("C",       (("mode selection", mode_polarization),)),
    
    ("T",       (("mode selection", mode_polarization),)),
    
    ("mesh",    (("dx", mesh_dx),
                 ("dy", mesh_dy),
                 ("override x mesh", enable_dx),
                 ("override y mesh", enable_dy),
                 ("override z mesh", False))),    
    
    ("::model", (("monitor_theta", monitor_theta),
                 ("FDTD_z_span", simulation_span_z),
                 ("port_extension", port_extension))),
        
    ("FDTD",    (("simulation time", simulation_time),
                 ("mesh accuracy", mesh_accuracy))),
)


    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               fdtd.setnamed(obj, k, v)
               
    fdtd.setglobalmonitor("frequency points",frequency_points)

    fdtd.save()


# ---------------------------------------------------------------------------


if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_RING_DIRECTORY_READ[file_index]) as fdtd:
        override_fdtd(fdtd=fdtd)



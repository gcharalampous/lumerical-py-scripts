#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The script overrides the FDTD simulation region from the vertical_taper.fsp
file.


"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import lumapi
from FDTD.vertical_taper.user_inputs.user_simulation_parameters import *  
from config import FDTD_VERTICAL_DIRECTORY_READ

def override_fdtd(fdtd):
   
    fdtd.switchtolayout()
    
    configuration = (
    
        
    ("source",      (("mode selection", mode_source),
                     ("wavelength start", wavelength_start),
                     ("wavelength stop", wavelength_stop))),

    ("T_exp",       (("mode selection", mode_monitor),
                    )),
    
    ("mesh",        (("dx", mesh_dx),
                     ("dy", mesh_dy),
                     ("dz", mesh_dz),
                     ("override x mesh", enable_dx),
                     ("override y mesh", enable_dy),
                     ("override z mesh", enable_dz))),    
    
    ("::model",      (("taper_gap",taper_gap),
                      ("taper_length",taper_length),
                      ("FDTD_z_span", simulation_span_z),
                     ("FDTD_y_span", simulation_span_y),
                     ("port_extension", port_extension))),
        
    ("FDTD",        (("simulation time", simulation_time),
                     ("mesh accuracy",mesh_accuracy))),
    
    )

    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               fdtd.setnamed(obj, k, v)
               
    fdtd.setglobalmonitor("frequency points",frequency_points)

    fdtd.save()


# ---------------------------------------------------------------------------


if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_VERTICAL_DIRECTORY_READ) as fdtd:
        override_fdtd(fdtd=fdtd)



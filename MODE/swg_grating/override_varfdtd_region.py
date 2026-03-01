#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The script sets the varFDTD region for the sub-wavelength grating simulation.

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

def override_varfdtd(mode):
   
    mode.switchtolayout()
    
    configuration = (
    
        
    ("source",      (("mode selection", mode_source),
                     ("wavelength start", wavelength_start),
                     ("wavelength stop", wavelength_stop))),
    
    ("R_exp",       (("monitor type", mode_monitor),
                    )),

    ("T_exp",       (("monitor type", mode_monitor),
                    )),
    
    ("mesh",        (("dx", mesh_dx),
                     ("dy", mesh_dy),
                     ("dz", mesh_dz),
                     ("override x mesh", enable_dx),
                     ("override y mesh", enable_dy),
                     ("override z mesh", enable_dz))),    
    
    ("::model",      (("FDTD_z_span", simulation_span_z),
                     ("FDTD_y_span", simulation_span_y),
                     ("port_extension", port_extension))),
        
    ("varFDTD",        (("simulation time", simulation_time),
                     ("mesh accuracy",mesh_accuracy))),
    
    )

    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               mode.setnamed(obj, k, v)
               
    mode.setglobalmonitor("frequency points",frequency_points)

    mode.save()


# ---------------------------------------------------------------------------


if(__name__=="__main__"):
    with lumapi.MODE(str(templates[0])) as mode:
        override_varfdtd(mode=mode)



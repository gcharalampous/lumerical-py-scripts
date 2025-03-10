#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The script overrides the FDTD simulation region from the edge_taper.fsp
file.


"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import lumapi
from FDTD.grating_coupler_2D.user_inputs.user_simulation_parameters import *  
from config import FDTD_GRATING_COUPLER_2D_DIRECTORY_READ

def override_fdtd(fdtd):
   
    fdtd.switchtolayout()
    
    configuration = (
        ("::model", (
            ("FDTD_y_min", simulation_min_y),
            ("fiber_position_x", fiber_position_x),
            ("fiber_angle", fiber_angle)
        )),
        ("FDTD", (
            ("simulation time", simulation_time),
            ("mesh accuracy", mesh_accuracy)
        )),

        ("fiber", (
            ("polarization angle", mode_source),
            ("angle theta", fiber_angle),
            ("x", fiber_position_x),
            ("waist radius w0", waist_radius),
            ("distance from waist", distance_from_waist),
            ("override global source settings", 1),
            ("wavelength start", wavelength_start),
            ("wavelength stop", wavelength_stop)
        )),


        # ("mesh", (
        #     ("dx", mesh_dx),
        #     ("dy", mesh_dy),
        #     ("dz", mesh_dz),
        #     ("override x mesh", enable_dx),
        #     ("override y mesh", enable_dy),
        #     ("override z mesh", enable_dz)
        # )),

    )

    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               fdtd.setnamed(obj, k, v)
               
    fdtd.setglobalmonitor("frequency points",frequency_points)

    fdtd.save()


# ---------------------------------------------------------------------------


if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_GRATING_COUPLER_2D_DIRECTORY_READ) as fdtd:
        override_fdtd(fdtd=fdtd)



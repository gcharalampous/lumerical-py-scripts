#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script calculates confinement factor in PCM region

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
from config import *
from scipy import integrate

from MODE.waveguide.waveguide_render import *
from MODE.waveguide.fde_region import add_fde_region  


# ------------------------- No inputs are required ---------------------------

def integrate_power():
    if(pcm_layer_enable):
        pcm_x_min = mode.getnamed("pcm","x min")
        pcm_x_max = mode.getnamed("pcm","x max")
        pcm_y_min = mode.getnamed("pcm","y min")
        pcm_y_max = mode.getnamed("pcm","y max")

        for m in range(1,num_modes+1):
            Em = np.squeeze(mode.getelectric("FDE::data::mode"+str(m)))
            Im = np.abs(Em)**2

            # Integrate power over the specified region

            x=np.squeeze(mode.getdata("FDE::data::mode"+str(m),"x"))
            y=np.squeeze(mode.getdata("FDE::data::mode"+str(m),"y"))
            X, Y = np.meshgrid(x, y)

            filter = (X<pcm_x_max) & (X>pcm_x_min)
            filter = filter & (Y<pcm_y_max) & (Y>pcm_y_min)

            E1 = integrate.simpson(integrate.simpson(np.transpose(Im)*filter,x),y)

            E2 = integrate.simpson(integrate.simpson(np.transpose(Im),x),y)

            # Accumulate the power integration result
            print(str(np.round((E1/E2)*100,2)) + " %")
    else:
        print("Enable PCM material in user_inputs/user_simulation_parameters.py")


if(__name__=="__main__"):
    with lumapi.MODE() as mode:
        
        # Disable Rendering
        mode.redrawoff()

        # Draw the waveguide structure using a custom function
        waveguide_draw(mode)

        # Add a finite-difference eigenmode (FDE) region to the simulation environment
        add_fde_region(mode)

        # Run the simulation, create a mesh, and compute the modes, then save
        mode.run()
        mode.findmodes()
        mode.save(MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE + "\\waveguide_modes.lms")
        
        # Turn redraw back on and close LumAPI connection
        mode.redrawon()  

        # Get confinement factor
        integrate_power()

        

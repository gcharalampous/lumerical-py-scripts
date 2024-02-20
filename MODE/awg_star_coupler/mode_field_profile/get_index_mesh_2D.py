#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script calculates the apperture profile of the star coupler specified in 
'user_inputs/awg_input_taper.lms' and 'user_simulation_parameters.py'.

"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
import os 
from config import *

# Import user-defined parameters from another file
from MODE.directional_coupler.user_inputs.user_simulation_parameters import *


# ------------------------- No inputs are required ---------------------------
if(__name__=="__main__"):

    with lumapi.MODE(MODE_AWG_DIRECTORY_READ) as mode:

        mode.switchtolayout()
        mode.run()
        
        
        # Get the index profile
        index = np.squeeze(mode.getdata("effective_index","index_x"))
        x = np.squeeze(mode.getdata("effective_index","x"))
        y = np.squeeze(mode.getdata("effective_index","y"))


    px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    fig, ax = plt.subplots(figsize=(512*px, 256*px))

    c = ax.pcolormesh(x*1e6,y*1e6,np.real(np.transpose(index)),shading = 'gouraud',cmap = 'jet')
    fig.colorbar(c, ax = ax)

    ax.set_xlabel("x (\u00B5m)")
    ax.set_ylabel("y (\u00B5m)")
    ax.set_title("Star Coupler Index Mesh")

    file_name_plot = os.path.join(MODE_AWG_DIRECTORY_WRITE[0], "index_profile_xz.png")
    plt.savefig(file_name_plot)


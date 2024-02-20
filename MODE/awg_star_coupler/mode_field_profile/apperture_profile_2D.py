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
from config import *

# Import user-defined parameters from another file
from MODE.directional_coupler.user_inputs.user_simulation_parameters import *





with lumapi.MODE(MODE_AWG_DIRECTORY_READ) as mode:

    mode.switchtolayout()
    mode.run()
    mode.save()            
    
    
    # Get the far field
    Ep=mode.farfield2d("monitor_field")
    theta=mode.farfieldangle("monitor_field")
    
   
    # Normalize in dB scale
    Ep_dB = 10*np.log10(abs(Ep))
    Ep_dB_unity = 10*np.log10(abs(Ep))-np.max(Ep_dB)
    
    
    px = 1/plt.rcParams['figure.dpi']  # pixel in inches

    fig, ax = plt.subplots(figsize=(512*px, 256*px))
    ax.plot(theta,Ep_dB_unity,label = 'Ep')
    ax.set_xlabel("\u03B8 (deg)")
    ax.set_ylabel("Transmission (dB)")
    ax.grid()

    ax.axhline(y = -30,linestyle = '--', color = 'g')
    
    ax.axvline(x = -30,linestyle = '--', color = 'r')
    ax.axvline(x = 30,linestyle = '--', color = 'r')
    
file_name_plot_writing = os.path.join(MODE_AWG_DIRECTORY_WRITE[1], 
                                            "far_field_profile.png")
fig.tight_layout()

fig.savefig(file_name_plot_writing, dpi=my_dpi, format="png")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the transmission and reflection for the sub-wavelength
bragg grating structure defined in the sub_wavelength_grating.fsp file
from the T and R monitors

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
import scipy.constants as scpy
from project_layout import setup

from MODE.swg_grating.override_varfdtd_region import override_varfdtd
from MODE.swg_grating.override_swg_region import *

def getBraggResponse(mode):
    mode.run()
    T  = np.squeeze(mode.transmission("T"))
    R  = np.squeeze(mode.transmission("R"))
    f  = np.squeeze(mode.getdata("T","f"))

    return T, R, f



if(__name__=="__main__"):
    spec, out, templates = setup("mode.swg_grating", __file__)
    with lumapi.MODE(str(templates[0])) as mode:
        
# ------------ Comment for Avoiding Overriding the Simulation Region
        # override_varfdtd(mode=mode)
        # override_swg(mode=mode)
        
# --------------------------------Plot-T/R---------------------------------

        T, R, f = getBraggResponse(mode=mode)

# --------------------------------Plot-T/R---------------------------------

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot((scpy.c/f)*1e6,T,label = 'Transmission')
        ax.plot((scpy.c/f)*1e6,abs(R),label = 'Reflection')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude")
        plt.ylim([0,1])
        plt.tight_layout()
        file_name_plot = str(out["figure_groups"]["Frequency Response"] / "frequency_response.png")
        plt.savefig(file_name_plot)        
        
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot((scpy.c/f)*1e6,10*np.log10(T),label = 'Transmission')
        ax.plot((scpy.c/f)*1e6,10*np.log10(abs(R)),label = 'Reflection')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude (dB)")
        plt.tight_layout()
        file_name_plot = str(out["figure_groups"]["Frequency Response"] / "frequency_response_dB.png")
        plt.savefig(file_name_plot)      
        
        plt.show()
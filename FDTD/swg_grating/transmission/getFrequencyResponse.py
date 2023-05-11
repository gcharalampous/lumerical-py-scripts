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
import lumapi, os
import matplotlib.pyplot as plt
import scipy.constants as scpy
from config import *

from FDTD.swg_grating.override_fdtd_region import override_fdtd
from FDTD.swg_grating.override_swg_region import *

def getBraggResponse(fdtd):
    fdtd.run()
    T  = np.squeeze(fdtd.transmission("T"))
    R  = np.squeeze(fdtd.transmission("R"))
    f  = np.squeeze(fdtd.getdata("T","f"))

    return T, R, f



if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_SWG_DIRECTORY_READ) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region
        # override_swg(fdtd=fdtd)
        # override_fdtd(fdtd=fdtd)
        
# --------------------------------Plot-T/R---------------------------------

        T, R, f = getBraggResponse(fdtd=fdtd)

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
        file_name_plot = os.path.join(FDTD_SWG_DIRECTORY_WRITE[1], "frequency_response.png")
        plt.savefig(file_name_plot)        
        
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot((scpy.c/f)*1e6,10*np.log10(T),label = 'Transmission')
        ax.plot((scpy.c/f)*1e6,10*np.log10(abs(R)),label = 'Reflection')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude (dB)")
        ax.set_ylim([-20,0])
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_SWG_DIRECTORY_WRITE[1], "frequency_response_dB.png")
        plt.savefig(file_name_plot)      
        
        plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the transmission and crosstalk for the waveguide crossing
structure defined in the waveguide_crossing_multi_wg_taper.fsp file
from the 'through' and crosstalk monitor.

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
import scipy.constants as scpy
from config import *

# from FDTD.waveguide_cross.override_cross_region import *

def getCrossResponse(fdtd):
    fdtd.run()
    T  = np.squeeze(fdtd.getresult("through_mode","expansion for ").get("T_forward"))
    C  = np.squeeze(fdtd.getresult("crosstalk_mode","expansion for ").get("T_forward"))
    f  = np.squeeze(fdtd.getdata("through","f"))

    return T, C, f



if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_CROSS_DIRECTORY_READ) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region
        # override_cross(fdtd=fdtd)
        
# --------------------------------Plot-T/R---------------------------------

        T, C, f = getCrossResponse(fdtd=fdtd)

# --------------------------------Plot-T/R---------------------------------

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.semilogy((scpy.c/f)*1e6,T,label = 'Transmission')
        ax.semilogy((scpy.c/f)*1e6,C,label = 'Crosstalk')
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude")
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_CROSS_DIRECTORY_WRITE[1], "frequency_response.png")
        plt.savefig(file_name_plot)        
        
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot((scpy.c/f)*1e6,10*np.log10(T),label = 'Transmission')
        ax.plot((scpy.c/f)*1e6,10*np.log10(C),label = 'Crosstalk')
        ax.grid(which='major')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude (dB)")
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_CROSS_DIRECTORY_WRITE[1], "frequency_response_dB.png")
        plt.savefig(file_name_plot)      
        
        plt.show()
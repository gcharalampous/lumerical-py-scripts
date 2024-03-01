#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the transmission and coupling for the ring coupler
structure defined in the *.fsp files from the 'T' and 'C' monitors.

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
import scipy.constants as scpy
from config import *

from FDTD.ring_resonator_coupler.user_inputs.user_simulation_parameters import *

from FDTD.ring_resonator_coupler.override_fdtd_region import *
from FDTD.ring_resonator_coupler.override_ring_coupler_region import *


def getCouplingResponse(fdtd):
    fdtd.run()
    T  = np.squeeze(fdtd.getresult("T","expansion for ").get("T_forward"))
    C  = np.squeeze(fdtd.getresult("C","expansion for ").get("T_forward"))
    f  = np.squeeze(fdtd.getdata("through","f"))

    return T, C, f



if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_RING_DIRECTORY_READ[file_index]) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region defined in the file
        # override_fdtd(fdtd=fdtd)
        # override_ring_coupler(fdtd=fdtd)
        
# --------------------------------Plot-T/R---------------------------------

        T, C, f = getCouplingResponse(fdtd=fdtd)

# --------------------------------Plot-T/R---------------------------------

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.semilogy((scpy.c/f)*1e6,T,label = 'Through')
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude")
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_RING_DIRECTORY_WRITE[1], "frequency_response_T.png")
        plt.savefig(file_name_plot)        
        
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.semilogy((scpy.c/f)*1e6,C,label = 'Crosstalk')
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude")
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_RING_DIRECTORY_WRITE[1], "frequency_response_C.png")
        plt.savefig(file_name_plot)   
       



        
        plt.show()
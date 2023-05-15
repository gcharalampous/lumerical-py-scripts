#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the transmission for the fundamental TE or TM mode
of the vertical taper structure defined in the vertical_taper.fsp file
from the T_exp monitor. The back reflection from the source is also printed

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
import scipy.constants as scpy
from config import *

from FDTD.vertical_taper.override_fdtd_region import override_fdtd
from FDTD.vertical_taper.override_vertical_taper_region import *

def getBraggResponse(fdtd):
    fdtd.run()
    T_total  = np.squeeze(fdtd.getresult("T_exp","expansion for fundamental").get("T_total"))
    T_forward  = np.squeeze(fdtd.getresult("T_exp","expansion for fundamental").get("T_forward"))
    R  = np.squeeze(fdtd.transmission("R"))
    f  = np.squeeze(fdtd.getdata("T","f"))

    return T_total, T_forward, R, f



if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_VERTICAL_DIRECTORY_READ) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region
        # override_vertical_taper(fdtd=fdtd)
        # override_fdtd(fdtd=fdtd)
        
# -----------------------------Plot-T_forward/T_total------------------------------

        T_total, T_forward, R, f = getBraggResponse(fdtd=fdtd)
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches

# -----------------------------Plot-T_forward/T_total------------------------------

        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot((scpy.c/f)*1e6, T_total,'-o',label = 'Total')
        ax.plot((scpy.c/f)*1e6, T_forward,'-o',label = 'Fundamental')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude")
        plt.ylim([0,1])
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_VERTICAL_DIRECTORY_WRITE[1], "frequency_response.png")
        plt.savefig(file_name_plot)        
        
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot((scpy.c/f)*1e6,10*np.log10(T_total),'-o',label = 'Total')
        ax.plot((scpy.c/f)*1e6,10*np.log10(abs(T_forward)),'-o',label = 'Fundamental')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude (dB)")
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_VERTICAL_DIRECTORY_WRITE[1], "frequency_response_dB.png")
        plt.savefig(file_name_plot)      
        
        plt.show()
        
        print('Back Reflection: ' + str(round(10*np.log10(abs(R.mean())),2)) + ' dB')
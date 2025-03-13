#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the transmission for the waveguide adiabatic y-branch
structure defined in the MMI_1x2.fsp file
from the 'Ttop' and 'Tbot' monitor ports.

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
import scipy.constants as scpy
from config import *


def getCrossResponse(fdtd):
    T1  = np.squeeze(fdtd.getresult("through_1","T").get("T"))
    T2  = np.squeeze(fdtd.getresult("through_2","T").get("T"))
    f  = np.squeeze(fdtd.getdata("through_1","f"))

    return T1, T2, f



if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_MMI_DIRECTORY_READ[0]) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region
        # override_cross(fdtd=fdtd)
        # fdtd.run()

# --------------------------------Plot-T/R---------------------------------

        T1, T2, f = getCrossResponse(fdtd=fdtd)

# --------------------------------Plot-T/R---------------------------------

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot((scpy.c/f)*1e6,T1,label = 'Port 1')
        ax.plot((scpy.c/f)*1e6,abs(T2),label = 'Port 2',linestyle='--')
        ax.set_ylim(0,1)
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude")
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_MMI_DIRECTORY_WRITE[1], "1x2MMI_frequency_response.png")
        plt.savefig(file_name_plot)        
        
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot((scpy.c/f)*1e6,10*np.log10(T1),label = 'Port 1')
        ax.plot((scpy.c/f)*1e6,10*np.log10(abs(T2)),label = 'Port 2',linestyle='--')
        ax.grid(which='major')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude (dB)")
        
        min_val = 10 * np.log10(np.min([T1, abs(T2)]))
        max_val = 10 * np.log10(np.max([T1, abs(T2)]))
        ax.axhline(y=min_val, color='black', linestyle='--')
        ax.axhline(y=max_val, color='black', linestyle='--')
        
        # Calculate the deviation from 3dB        
        deviation_from_3dB_1 = abs(-3.01 - min_val)
        deviation_from_3dB_2 = abs(-3.01 - max_val)
        
        # Get the worst case deviation from 3dB
        deviation_from_3dB = (max(deviation_from_3dB_1, deviation_from_3dB_2))
        deviation_percentage = (10**(-deviation_from_3dB/10)-1) * 100
        
        
        print(f"Deviation: {deviation_from_3dB} dB")
        print(f"Deviation: {abs(deviation_percentage):.2f}%")
        
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_MMI_DIRECTORY_WRITE[1], "1x2MMI_frequency_response_dB.png")
        plt.savefig(file_name_plot)      
        
        plt.show()
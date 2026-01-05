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
import lumapi
import matplotlib.pyplot as plt
import scipy.constants as scpy
from pathlib import Path
from project_layout import setup

def getCrossResponse(fdtd):
    fdtd.run()
    T  = np.squeeze(fdtd.getresult("through_mode","expansion for ").get("T_forward"))
    C  = np.squeeze(fdtd.getresult("crosstalk_mode","expansion for ").get("T_forward"))
    f  = np.squeeze(fdtd.getdata("through","f"))

    return T, C, f



if(__name__=="__main__"):
    spec, out, templates = setup("fdtd.waveguide_crossing", __file__)
    template_fsp = templates[0]  # waveguide_crossing_multi_wg_taper.fsp
    figures_dir = out["figures"] / "Transmission"
    figures_dir.mkdir(parents=True, exist_ok=True)
    
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        
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
        plt.savefig(figures_dir / "frequency_response.png")        
        
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot((scpy.c/f)*1e6,10*np.log10(T),label = 'Transmission')
        ax.plot((scpy.c/f)*1e6,10*np.log10(C),label = 'Crosstalk')
        ax.grid(which='major')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude (dB)")
        plt.tight_layout()
        plt.savefig(figures_dir / "frequency_response_dB.png")
        
        plt.show()
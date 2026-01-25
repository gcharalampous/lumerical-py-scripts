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
from FDTD.swg_grating.user_inputs.user_simulation_parameters import file_index

def getBraggResponse(fdtd):
    
    T  = np.squeeze(fdtd.transmission("T"))
    R  = np.squeeze(fdtd.transmission("R"))
    f  = np.squeeze(fdtd.getdata("T","f"))

    return T, R, f



if(__name__=="__main__"):
        
    spec, out, templates = setup("fdtd.swg_grating", __file__)
    template_fsp = templates[file_index]
    figures_dir = out["figures"] / "Frequency Response"
    figures_dir.mkdir(parents=True, exist_ok=True)

    with lumapi.FDTD(str(template_fsp)) as fdtd:
    
        fdtd.run()    
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
        plt.savefig(figures_dir / "frequency_response.png")       
        
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot((scpy.c/f)*1e6,10*np.log10(T),label = 'Transmission')
        ax.plot((scpy.c/f)*1e6,10*np.log10(abs(R)),label = 'Reflection')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude (dB)")
        # ax.set_ylim([-20,0])
        plt.tight_layout()
        plt.savefig(figures_dir / "frequency_response_dB.png")     
        
        plt.show()
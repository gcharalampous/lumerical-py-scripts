#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the transmission for the fundamental TE or TM mode
of the vertical taper structure defined in the edge_taper.fsp file
from the T_exp monitor. The back reflection from the source is also printed

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

def getTaperResponse(fdtd):
    fdtd.run()
    T_total  = np.squeeze(fdtd.getresult("T_exp","expansion for fundamental").get("T_total"))
    T_forward  = np.squeeze(fdtd.getresult("T_exp","expansion for fundamental").get("T_forward"))
    R  = np.squeeze(fdtd.transmission("R"))
    f  = np.squeeze(fdtd.getdata("T","f"))

    return T_total, T_forward, R, f



if(__name__=="__main__"):
    spec, out, templates = setup("fdtd.edge_coupler", __file__)
    template_fsp = templates[0]  # edge_taper.fsp
    figures_dir = out["figures"] / "Transmission"
    figures_dir.mkdir(parents=True, exist_ok=True)
    
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        
        
# -----------------------------Plot-T_forward/T_total------------------------------

        T_total, T_forward, R, f = getTaperResponse(fdtd=fdtd)
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
        plt.savefig(figures_dir / "frequency_response.png")

        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot((scpy.c/f)*1e6,10*np.log10(T_total),'-o',label = 'Total')
        ax.plot((scpy.c/f)*1e6,10*np.log10(abs(T_forward)),'-o',label = 'Fundamental')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude (dB)")
        plt.tight_layout()
        plt.savefig(figures_dir / "frequency_response_dB.png")

        plt.show()
        
        print('Back Reflection: ' + str(round(10*np.log10(abs(R.mean())),2)) + ' dB')
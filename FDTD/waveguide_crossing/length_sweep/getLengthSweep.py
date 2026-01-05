#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the transmission and crosstalk for the waveguide crossing 
structure as a function of taper length from the mode expansion monitors.

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



def getCrossingResponse(fdtd):
    T = fdtd.getsweepresult("sweep_length", "through_mode0")
    C = fdtd.getsweepresult("sweep_length", "crosstalk_mode0")
    
    return T, C


if(__name__=="__main__"):
    spec, out, templates = setup("fdtd.waveguide_crossing", __file__)
    template_fsp = templates[0]  # waveguide_crossing_multi_wg_taper.fsp
    figures_dir = out["figures"] / "Length Sweep"
    figures_dir.mkdir(parents=True, exist_ok=True)
    
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        
# ------------ Comment for Avoiding Running Sweep 
        fdtd.runsweep("sweep_length")

# Get Transmission and Crosstalk
        T, C = getCrossingResponse(fdtd=fdtd)
        Lm = np.squeeze(T['Lm'])
        through = np.squeeze(T['T_forward'])
        crosstalk = np.squeeze(C['T_forward'])
        
        # Slice at center wavelength if multiple wavelength points
        if through.ndim > 1:
            c_wavelength = int(np.rint(through.shape[0]/2))
            through = through[c_wavelength, :]
            crosstalk = crosstalk[c_wavelength, :]

# --------------------------------Plot-T/C---------------------------------

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        
        # Linear scale
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot(Lm*1e6, through, '-o', label = 'Transmission')
        ax.plot(Lm*1e6, crosstalk, '-o', label = 'Crosstalk')
        ax.grid(which='major')
        ax.legend()
        ax.set_xlabel("multimode waveguide length (um)")
        ax.set_ylabel("Magnitude")
        plt.tight_layout()
        plt.savefig(figures_dir / "crossing_length_sweep.png")
        
        # dB scale
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot(Lm*1e6, 10*np.log10(abs(through)), '-o', label = 'Transmission')
        ax.plot(Lm*1e6, 10*np.log10(abs(crosstalk)), '-o', label = 'Crosstalk')
        ax.grid(which='major')
        ax.legend()
        ax.set_xlabel("multimode waveguide length (um)")
        ax.set_ylabel("Magnitude (dB)")
        plt.tight_layout()
        plt.savefig(figures_dir / "crossing_length_sweep_dB.png")
        
        plt.show()

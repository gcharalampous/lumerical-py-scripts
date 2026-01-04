#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the transmission for the edge coupler structure defined in 
the edge_taper.fsp file from the mode expansion monitor 'T_exp' as a function 
of taper length.

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



def getCouplingResponse(fdtd):
    T  = (fdtd.getsweepresult("sweep_length","mode0"))

    return T


if(__name__=="__main__"):
    spec, out, templates = setup("fdtd.edge_coupler", __file__)
    template_fsp = templates[0]  # edge_taper.fsp
    figures_dir = out["figures"] / "Length Sweep"
    figures_dir.mkdir(parents=True, exist_ok=True)
    
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        
# ------------ Comment for Avoiding Running Sweep 
        fdtd.runsweep("sweep_length")

# Get Coupling and Through
        T = getCouplingResponse(fdtd=fdtd)
        taper_length = np.squeeze(T['taper_length'])
        through = np.squeeze(T['T_forward'])
        gaussian_radius = fdtd.getnamed("source","waist radius w0")
        
        # Slice at center wavelength if multiple wavelength points
        if through.ndim > 1:
            c_wavelength = int(np.rint(through.shape[0]/2))
            through = through[c_wavelength, :]

# --------------------------------Plot-T/C---------------------------------

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot(taper_length*1e6, through, label = 'Fundamental Mode')
        ax.grid(which='major')
        ax.legend()
        ax.set_xlabel("taper length (um)")
        ax.set_ylabel("Magnitude")
        ax.set_title("Waist Radius: {:.2f} um".format(gaussian_radius*1e6))
        plt.tight_layout()
        plt.savefig(figures_dir / "Coupling_length_sweep.png")
        
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot(taper_length*1e6, 10*np.log10(abs(through)), label = 'Fundamental Mode')
        ax.grid(which='major')
        ax.legend()
        ax.set_xlabel("taper length (um)")
        ax.set_ylabel("Magnitude (dB)")
        ax.set_title("Waist Radius: {:.2f} um".format(gaussian_radius*1e6))
        plt.tight_layout()
        plt.savefig(figures_dir / "Coupling_length_sweep_dB.png")
        
        plt.show()
        

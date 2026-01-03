#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Extract and plot length sweep results for adiabatic Y-branch.

The script performs a length sweep on the adiabatic Y-branch splitter
structure and plots the transmission for both output ports
as a function of taper length.
"""

#----------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup

# Configuration
spec, out, templates = setup("fdtd.adiabatic_y_branch", __file__)
template_fsp = templates[0]
figures_dir = out["figure_groups"]["Sweep Transmission"]


def getCouplingResponse(fdtd):
    """Extract length sweep results from FDTD simulation.
    
    Args:
        fdtd: FDTD simulation object from lumapi.
    
    Returns:
        tuple: (through, bar, length, lambda0) where
            - through: Port 1 transmission
            - bar: Port 2 transmission
            - length: Taper length array
            - lambda0: Central wavelength used
    """
    T = fdtd.getsweepresult("sweep_taper_length", "T1")
    C = fdtd.getsweepresult("sweep_taper_length", "T2")
           
    length = np.squeeze(T['length'])
    through = np.squeeze(T['T'])
    bar = np.squeeze(C['T'])
    lambda_array = np.squeeze(T['lambda'])

    if lambda_array.size > 1:
        index_array = int(np.floor(lambda_array.size / 2))
        through = abs(through[index_array])
        bar = abs(bar[index_array])
        lambda0 = lambda_array[index_array]
        print(f"The central wavelength is: {lambda0*1e6:.3f} um")
    else:
        through = abs(through)
        bar = abs(bar)
        lambda0 = lambda_array if lambda_array.size == 1 else lambda_array[0]
        print(f"The central wavelength is: {lambda0*1e6:.3f} um")
    
    return through, bar, length, lambda0



if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.runsweep("sweep_taper_length")
        
        # Get port transmission data
        through, bar, length, lambda0 = getCouplingResponse(fdtd=fdtd)
        
        # ---- Plot 1: Linear scale ----
        px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(length * 1e6, through, label='Port 1 (Top)', marker='o')
        ax.plot(length * 1e6, bar, label='Port 2 (Bottom)', marker='s')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Length (µm)")
        ax.set_ylabel("Transmission (Linear)")
        ax.set_title(f"Wavelength = {lambda0*1e6:.3f} µm")
        plt.tight_layout()
        file_name_plot = figures_dir / "sweep_length_linear.png"
        plt.savefig(file_name_plot)
        
        # ---- Plot 2: Logarithmic scale (dB) ----
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(length * 1e6, 10 * np.log10(through), label='Port 1 (Top)', marker='o')
        ax.plot(length * 1e6, 10 * np.log10(bar), label='Port 2 (Bottom)', marker='s')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Length (µm)")
        ax.set_ylabel("Transmission (dB)")
        ax.set_title(f"Wavelength = {lambda0*1e6:.3f} µm")
        plt.tight_layout()
        file_name_plot = figures_dir / "sweep_length_dB.png"
        plt.savefig(file_name_plot)
        
        plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Extract and plot gap sweep results for adiabatic directional coupler.

The script performs a gap sweep on the adiabatic directional coupler
structure and plots the transmission for through and coupled ports
as a function of gap distance.
"""

#----------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup

# Configuration
spec, out, templates = setup("fdtd.adiabatic_dc", __file__)
template_fsp = templates[0]
figures_dir = out["figure_groups"]["Sweep Transmission"]


def getCouplingResponse(fdtd):
    """Extract gap sweep results from FDTD simulation.
    
    Args:
        fdtd: FDTD simulation object from lumapi.
    
    Returns:
        tuple: (T, C) where
            - T: Through port sweep results
            - C: Coupled port sweep results
    """
    T = fdtd.getsweepresult("sweep_coupling_gap", "Through")
    C = fdtd.getsweepresult("sweep_coupling_gap", "Bar")

    return T, C



if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:

        # Perform the gap sweep, comment to avoid re-running the sweep
        fdtd.runsweep("sweep_coupling_gap")
        
        # Get Through and Coupled port data
        T, C = getCouplingResponse(fdtd=fdtd)
        gap = np.squeeze(T['coupling_gap'])
        through = np.squeeze(T['T'])
        coupled = np.squeeze(C['T'])
        
        # ---- Plot 1: Through port transmission ----
        px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(gap * 1e6, through, label='Through', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Gap (µm)")
        ax.set_ylabel("Transmission (Linear)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        file_name_plot = figures_dir / "gap_sweep_through.png"
        plt.savefig(file_name_plot)
        
        # ---- Plot 2: Coupled port transmission ----
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(gap * 1e6, coupled, label='Coupled', marker='o', color='orange')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Gap (µm)")
        ax.set_ylabel("Transmission (Linear)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        file_name_plot = figures_dir / "gap_sweep_coupled.png"
        plt.savefig(file_name_plot)
        
        # ---- Plot 3: Through port transmission (dB) ----
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        through_dB = 10 * np.log10(through)
        ax.plot(gap * 1e6, through_dB, label='Through', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Gap (µm)")
        ax.set_ylabel("Transmission (dB)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        file_name_plot = figures_dir / "gap_sweep_through_dB.png"
        plt.savefig(file_name_plot)
        
        # ---- Plot 4: Coupled port transmission (dB) ----
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        coupled_dB = 10 * np.log10(coupled)
        ax.plot(gap * 1e6, coupled_dB, label='Coupled', marker='o', color='orange')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Gap (µm)")
        ax.set_ylabel("Transmission (dB)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        file_name_plot = figures_dir / "gap_sweep_coupled_dB.png"
        plt.savefig(file_name_plot)
        
        plt.show()
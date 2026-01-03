#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Extract and plot transmission response for adiabatic Y-branch.

The script plots the transmission for the adiabatic Y-branch splitter
structure defined in the adiabatic_y_branch.fsp file,
extracting data from the top and bottom output port monitors.
"""

#----------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
import scipy.constants as scpy
from project_layout import setup

# Configuration
spec, out, templates = setup("fdtd.adiabatic_y_branch", __file__)
template_fsp = templates[0]
figures_dir = out["figure_groups"]["Frequency Response"]

# Analysis parameters
TARGET_3DB = -3.01  # Target 3dB point for Y-branch splitting analysis


def getCrossResponse(fdtd):
    """Extract transmission response from FDTD monitors.
    
    Args:
        fdtd: FDTD simulation object from lumapi.
    
    Returns:
        tuple: (T1, T2, f) where
            - T1: Top port transmission
            - T2: Bottom port transmission
            - f: Frequency array
    """
    T1 = np.squeeze(fdtd.getresult("T_top", "T").get("T"))
    T2 = np.squeeze(fdtd.getresult("T_bot", "T").get("T"))
    f = np.squeeze(fdtd.getdata("T_top", "f"))

    return T1, T2, f



if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.run()
        
        # Extract transmission data
        T1, T2, f = getCrossResponse(fdtd=fdtd)
        wavelength = (scpy.c / f) * 1e6  # Convert to wavelength in micrometers
        
        # ---- Plot 1: Linear magnitude response ----
        px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(wavelength, T1, label='Port 1 (Top)')
        ax.plot(wavelength, abs(T2), label='Port 2 (Bottom)', linestyle='--')
        ax.set_ylim(0, 1)
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("Wavelength (µm)")
        ax.set_ylabel("Transmission (Linear)")
        plt.tight_layout()
        file_name_plot = figures_dir / "frequency_response.png"
        plt.savefig(file_name_plot)
        
        # ---- Plot 2: Logarithmic (dB) response ----
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        T1_dB = 10 * np.log10(T1)
        T2_dB = 10 * np.log10(abs(T2))
        
        ax.plot(wavelength, T1_dB, label='Port 1 (Top)')
        ax.plot(wavelength, T2_dB, label='Port 2 (Bottom)', linestyle='--')
        ax.grid(which='major')
        ax.legend()
        ax.set_xlabel("Wavelength (µm)")
        ax.set_ylabel("Transmission (dB)")
        
        # Calculate 3dB point deviations
        min_val = 10 * np.log10(np.min([T1, abs(T2)]))
        max_val = 10 * np.log10(np.max([T1, abs(T2)]))
        ax.axhline(y=min_val, color='black', linestyle='--', alpha=0.5)
        ax.axhline(y=max_val, color='black', linestyle='--', alpha=0.5)
        
        # Calculate deviation from target 3dB point
        deviation_from_3dB_min = abs(TARGET_3DB - min_val)
        deviation_from_3dB_max = abs(TARGET_3DB - max_val)
        deviation_from_3dB = max(deviation_from_3dB_min, deviation_from_3dB_max)
        deviation_percentage = (10 ** (-deviation_from_3dB / 10) - 1) * 100
        
        print(f"Min value: {min_val:.3f} dB")
        print(f"Max value: {max_val:.3f} dB")
        print(f"Deviation from 3dB: {deviation_from_3dB:.3f} dB")
        print(f"Deviation percentage: {abs(deviation_percentage):.2f}%")
        
        plt.tight_layout()
        file_name_plot = figures_dir / "frequency_response_dB.png"
        plt.savefig(file_name_plot)
        
        plt.show()
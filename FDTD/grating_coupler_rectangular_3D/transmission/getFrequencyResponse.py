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
from the T_exp monitor. The back reflection from the source is also printed.
"""

#----------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import os
import matplotlib.pyplot as plt
import scipy.constants as scpy
from config import *

from FDTD.grating_coupler_2D.override_fdtd_region import override_fdtd
from FDTD.grating_coupler_2D.override_grating_coupler_region import override_grating_coupler
from FDTD.grating_coupler_2D.user_inputs.user_simulation_parameters import mode_fundamental

def get_grating_coupler_response(fdtd):
        """
        Runs the FDTD simulation and retrieves the transmission and reflection data.

        Parameters:
        fdtd (lumapi.FDTD): The FDTD simulation object.

        Returns:
        tuple: Total transmission, reflection, and frequency data.
        """
        fdtd.run()
        T_total = abs(np.squeeze(fdtd.getresult("T", "T").get("T")))
        R = np.squeeze(fdtd.transmission("R"))
        f = np.squeeze(fdtd.getdata("T", "f"))

        return T_total, R, f

def plot_response(wavelength, T_total, mode_fundamental, output_dir):
        """
        Plots the transmission response.

        Parameters:
        wavelength (numpy.ndarray): Array of wavelengths.
        T_total (numpy.ndarray): Total transmission data.
        mode_fundamental (str): The fundamental mode.
        output_dir (str): Directory to save the plots.
        """
        px = 1 / plt.rcParams['figure.dpi']  # pixel in inches

        # Plot T_total
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(wavelength, T_total, '-o', label='Total')
        ax.legend()
        ax.set_xlabel("Wavelength (um)")
        ax.set_ylabel("Magnitude")
        ax.set_title('Mode: ' + mode_fundamental)
        plt.ylim([0, 1])
        plt.tight_layout()
        file_name_plot = os.path.join(output_dir, "frequency_response.png")
        plt.savefig(file_name_plot)        
        
        # Plot T_total in dB
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(wavelength, 10 * np.log10(T_total), '-o', label='Total')
        ax.legend()
        ax.set_xlabel("Wavelength (um)")
        ax.set_ylabel("Magnitude (dB)")
        ax.set_title('Mode: ' + mode_fundamental)
        plt.tight_layout()
        file_name_plot = os.path.join(output_dir, "frequency_response_dB.png")
        plt.savefig(file_name_plot)      
        
        plt.show()
        
if __name__ == "__main__":
        with lumapi.FDTD(FDTD_GRATING_COUPLER_2D_DIRECTORY_READ) as fdtd:
                # Override the simulation region
                # override_grating_coupler(fdtd=fdtd)
                # override_fdtd(fdtd=fdtd)

                # Get the grating coupler response
                T_total, R, f = get_grating_coupler_response(fdtd=fdtd)
                wavelength = (scpy.c / f) * 1e6

                # Plot the response
                plot_response(wavelength, T_total, mode_fundamental, FDTD_GRATING_COUPLER_2D_DIRECTORY_WRITE[1])

                # Print back reflection
                print('Back Reflection: ' + str(round(10 * np.log10(abs(R.mean())), 2)) + ' dB')
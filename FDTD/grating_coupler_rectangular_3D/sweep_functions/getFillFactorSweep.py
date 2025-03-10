#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the transmission for the grating coupler structure defined in 
the grating_coupler_2D.fsp file from the Transmission monitor 'T'.
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

from FDTD.grating_coupler_2D.user_inputs.user_simulation_parameters import *
from FDTD.grating_coupler_2D.override_fdtd_region import *
from FDTD.grating_coupler_2D.override_grating_coupler_region import *

def getCouplingResponse(fdtd):
        """
        Get the coupling response from the FDTD simulation.

        Parameters:
        fdtd (lumapi.FDTD): The FDTD simulation object.

        Returns:
        tuple: Transmission (T), wavelength, and fill factor arrays.
        """
        T = np.squeeze(fdtd.getsweepresult("sweep_fill_factor", "transmission").get('T'))
        wavelength = np.squeeze(fdtd.getsweepresult("sweep_fill_factor", "transmission").get('lambda'))
        fill_factor = np.squeeze(fdtd.getsweepresult("sweep_fill_factor", "transmission").get('fill_factor'))
        
        T = np.abs(T)

        return T, wavelength, fill_factor

def plot_coupling_response(T, wavelength, fill_factor, output_path):
        """
        Plot the coupling response.

        Parameters:
        T (numpy.ndarray): Transmission array.
        wavelength (numpy.ndarray): Wavelength array.
        fill_factor (numpy.ndarray): Fill factor array.
        output_path (str): Path to save the plot.
        """
        T_log = 10 * np.log10(T)

        px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))

        if wavelength.ndim == 0:
                ax.plot(fill_factor, T_log, label=wavelength * 1e9)
                ax.set_xlabel("Fill Factor")
                ax.legend(title="Wavelength (nm)")
        else:
                for i in range(len(fill_factor)):
                        ax.plot(wavelength * 1e9, T_log[:, i], label=f"{fill_factor[i]:.3f}")
                        ax.set_xlabel("Wavelength (nm)")
                        ax.legend(title="Fill Factor")

        ax.grid(which='major')
        ax.set_ylabel("Magnitude [dB]")
        ax.set_ylim(bottom=None, top=0)
        plt.tight_layout()
        plt.savefig(output_path)

if __name__ == "__main__":
        try:
                with lumapi.FDTD(FDTD_GRATING_COUPLER_2D_DIRECTORY_READ) as fdtd:
                        # Uncomment to override the simulation region defined in the file
                        # override_fdtd(fdtd=fdtd)
                        # override_grating_coupler(fdtd=fdtd)

                        # Uncomment to run the sweep
                        fdtd.runsweep('sweep_fill_factor')

                        # Get Coupling via the getFillFactorSweep function
                        T, wavelength, fill_factor = getCouplingResponse(fdtd=fdtd)

                        # Define the output path for the plot
                        file_name_plot = os.path.join(FDTD_GRATING_COUPLER_2D_DIRECTORY_WRITE[3], "grating_coupler_sweep_fill_factor.png")

                        # Plot the coupling response
                        plot_coupling_response(T, wavelength, fill_factor, file_name_plot)
        except Exception as e:
                print(f"An error occurred: {e}")
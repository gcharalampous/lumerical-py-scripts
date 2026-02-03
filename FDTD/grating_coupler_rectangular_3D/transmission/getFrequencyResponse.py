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
import matplotlib.pyplot as plt
import scipy.constants as scpy
from pathlib import Path
from project_layout import setup
from FDTD.grating_coupler_rectangular_3D.user_inputs.user_simulation_parameters import file_index



def get_grating_coupler_response(fdtd):
        """
        Runs the FDTD simulation and retrieves the transmission and reflection data.

        Parameters:
        fdtd (lumapi.FDTD): The FDTD simulation object.

        Returns:
        tuple: Total transmission, reflection, and frequency data.
        """
        T_total = abs(np.squeeze(fdtd.getresult("T", "T").get("T")))
        R = np.squeeze(fdtd.transmission("R"))
        f = np.squeeze(fdtd.getdata("T", "f"))

        return T_total, R, f

def plot_response(wavelength, T_total, output_dir):
        """Plot the transmission response and save figures."""
        px = 1 / plt.rcParams['figure.dpi']  # pixel in inches

        # Plot T_total
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(wavelength, T_total, '-o', label='Total')
        ax.legend()
        ax.set_xlabel("Wavelength (um)")
        ax.set_ylabel("Magnitude")
        plt.ylim([0, 1])
        plt.tight_layout()
        file_name_plot = str(output_dir / "frequency_response.png")
        plt.savefig(file_name_plot)
        plt.show()
        
        # Plot T_total in dB
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(wavelength, 10 * np.log10(T_total), '-o', label='Total')
        ax.legend()
        ax.set_xlabel("Wavelength (um)")
        ax.set_ylabel("Magnitude (dB)")
        plt.tight_layout()
        file_name_plot = str(output_dir / "frequency_response_dB.png")
        plt.savefig(file_name_plot)
        plt.show()
        
if __name__ == "__main__":
        spec, out, templates = setup("fdtd.grating_coupler_rectangular_3D", __file__)
        template_fsp = templates[file_index]
        figures_dir = out["figures"] / "Transmission"
        figures_dir.mkdir(parents=True, exist_ok=True)
        
        with lumapi.FDTD(str(template_fsp)) as fdtd:

                fdtd.run()


                # Get the grating coupler response
                T_total, R, f = get_grating_coupler_response(fdtd=fdtd)
                wavelength = (scpy.c / f) * 1e6

                # Plot the response
                plot_response(wavelength, T_total, figures_dir)

                # Print back reflection
                print('Back Reflection: ' + str(round(10 * np.log10(abs(R.mean())), 2)) + ' dB')
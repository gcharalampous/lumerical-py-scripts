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
import matplotlib.pyplot as plt
import scipy.constants as scpy
from pathlib import Path
from project_layout import setup
from FDTD.grating_coupler_rectangular_3D.user_inputs.user_simulation_parameters import file_index

def getCouplingResponse(fdtd):
        """
        Get the coupling response from the FDTD simulation.

        Parameters:
        fdtd (lumapi.FDTD): The FDTD simulation object.

        Returns:
        tuple: Transmission (T), wavelength, and fill factor arrays.
        """
        T = np.squeeze(fdtd.getsweepresult("sweep_taper_width", "transmission").get('T'))
        wavelength = np.squeeze(fdtd.getsweepresult("sweep_taper_width", "transmission").get('lambda'))
        width_grating = np.squeeze(fdtd.getsweepresult("sweep_taper_width", "transmission").get('width_grating'))
        
        T = np.abs(T)

        return T, wavelength, width_grating

def plot_coupling_response(T, wavelength, width_grating, output_path):
        """
        Plot the coupling response.

        Parameters:
        T (numpy.ndarray): Transmission array.
        wavelength (numpy.ndarray): Wavelength array.
        width_grating (numpy.ndarray): Grating width array.
        output_path (str): Path to save the plot.
        """
        T_log = 10 * np.log10(T)

        px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))

        if wavelength.ndim == 0:
                ax.plot(width_grating*1e6, T_log, label=wavelength * 1e9)
                ax.set_xlabel("Grating Width (um)")
                ax.legend(title="Wavelength (nm)")
        else:
                for i in range(len(width_grating)):
                        ax.plot(wavelength * 1e9, T_log[:, i], label=f"{width_grating[i]*1e6:.3f}")
                        ax.set_xlabel("Wavelength (nm)")
                        ax.legend(title="Grating Width (um)")

        ax.grid(which='major')
        ax.set_ylabel("Magnitude [dB]")
        ax.set_ylim(bottom=None, top=0)
        plt.tight_layout()
        plt.savefig(output_path)

def plot_max_transmission_at_wavelength(T, wavelength, width_grating, target_wavelength, output_path):
        """
        Plot the maximum transmission at a specific wavelength.

        Parameters:
        T (numpy.ndarray): Transmission array.
        wavelength (numpy.ndarray): Wavelength array.
        width_grating (numpy.ndarray): Grating width array.
        target_wavelength (float): Target wavelength in meters.
        output_path (str): Path to save the plot.
        """
        # Find the index closest to target wavelength
        if wavelength.ndim == 0:
                # Single wavelength case
                T_at_wavelength = T
        else:
                # Multiple wavelengths - find closest index
                wavelength_idx = np.argmin(np.abs(wavelength - target_wavelength))
                T_at_wavelength = T[wavelength_idx, :]
                actual_wavelength = wavelength[wavelength_idx]
        
        T_linear = np.abs(T_at_wavelength)
        T_dB = 10 * np.log10(T_linear)

        px = 1 / plt.rcParams['figure.dpi']
        
        # Linear plot
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(width_grating*1e6, T_linear, '-o')
        ax.grid(which='major')
        ax.set_xlabel("Grating Width (um)")
        ax.set_ylabel("Transmission")
        if wavelength.ndim == 0:
                ax.set_title(f"Wavelength: {wavelength*1e9:.1f} nm")
        else:
                ax.set_title(f"Wavelength: {actual_wavelength*1e9:.1f} nm")
        plt.tight_layout()
        plt.savefig(output_path.parent / f"{output_path.stem}_at_wavelength.png")
        
        # dB plot
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(width_grating*1e6, T_dB, '-o')
        ax.grid(which='major')
        ax.set_xlabel("Grating Width (um)")
        ax.set_ylabel("Transmission (dB)")
        if wavelength.ndim == 0:
                ax.set_title(f"Wavelength: {wavelength*1e9:.1f} nm")
        else:
                ax.set_title(f"Wavelength: {actual_wavelength*1e9:.1f} nm")
        plt.tight_layout()
        plt.savefig(output_path.parent / f"{output_path.stem}_at_wavelength_dB.png")
        plt.show()

if __name__ == "__main__":
        try:
                spec, out, templates = setup("fdtd.grating_coupler_rectangular_3D", __file__)
                template_fsp = templates[file_index]  # grating_coupler_rectangular_3D.fsp
                figures_dir = out["figures"] / "Sweep Functions"
                figures_dir.mkdir(parents=True, exist_ok=True)
                
                with lumapi.FDTD(str(template_fsp)) as fdtd:


                        # Uncomment to run the sweep
                        fdtd.runsweep('sweep_taper_width')

                        # Get Coupling via the getFillFactorSweep function
                        T, wavelength, width_grating = getCouplingResponse(fdtd=fdtd)

                        # Define the output path for the plot
                        file_name_plot = figures_dir / "grating_coupler_sweep_width_grating.png"

                        # Plot the coupling response
                        plot_coupling_response(T, wavelength, width_grating, file_name_plot)

                        # Define target wavelength for maximum transmission plot (example: 1550 nm)
                        target_wavelength = 1550e-9  # Convert to meters

                        # Plot maximum transmission at specific wavelength
                        plot_max_transmission_at_wavelength(T, wavelength, width_grating, target_wavelength, file_name_plot)
        except Exception as e:
                print(f"An error occurred: {e}")
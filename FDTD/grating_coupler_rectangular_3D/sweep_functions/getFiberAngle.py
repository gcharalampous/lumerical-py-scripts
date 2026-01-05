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


def getCouplingResponse(fdtd):
        """
        Get the coupling response from the FDTD simulation.

        Parameters:
        fdtd (lumapi.FDTD): The FDTD simulation object.

        Returns:
        tuple: Transmission (T), wavelength, and fill factor arrays.
        """
        T = np.squeeze(fdtd.getsweepresult("sweep_fiber_angle", "transmission").get('T'))
        wavelength = np.squeeze(fdtd.getsweepresult("sweep_fiber_angle", "transmission").get('lambda'))
        fiber_angle = np.squeeze(fdtd.getsweepresult("sweep_fiber_angle", "transmission").get('fiber_angle'))
        
        T = np.abs(T)

        return T, wavelength, fiber_angle

def plot_coupling_response(T, wavelength, fiber_angle, output_path):
        """
        Plot the coupling response.

        Parameters:
        T (numpy.ndarray): Transmission array.
        wavelength (numpy.ndarray): Wavelength array.
        fiber_angle (numpy.ndarray): Fiber Angle Array.
        output_path (str): Path to save the plot.
        """
        T_log = 10 * np.log10(T)

        px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))

        if wavelength.ndim == 0:
                ax.plot(fiber_angle, T, label=wavelength * 1e9)
                ax.set_xlabel("Fiber Angle (degrees)")
                ax.legend(title="Wavelength (nm)")
        else:
                for i in range(len(fiber_angle)):
                        ax.plot(wavelength * 1e9, T[:, i], label=f"{fiber_angle[i]:.3f}")
                        ax.set_xlabel("Wavelength (nm)")
                        ax.legend(title="Fiber Angle (degrees)")

        ax.grid(which='major')
        ax.set_ylabel("Magnitude")
        ax.set_ylim(bottom=None, top=1)
        plt.tight_layout()
        plt.savefig(str(output_path))
        plt.show()

def plot_max_transmission_at_wavelength(T, wavelength, fiber_angle, target_wavelength, output_path):
        """
        Plot the maximum transmission at a specific wavelength.

        Parameters:
        T (numpy.ndarray): Transmission array.
        wavelength (numpy.ndarray): Wavelength array.
        fiber_angle (numpy.ndarray): Fiber Angle Array.
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
        ax.plot(fiber_angle, T_linear, '-o')
        ax.grid(which='major')
        ax.set_xlabel("Fiber Angle (degrees)")
        ax.set_ylabel("Transmission")
        if wavelength.ndim == 0:
                ax.set_title(f"Wavelength: {wavelength*1e9:.1f} nm")
        else:
                ax.set_title(f"Wavelength: {actual_wavelength*1e9:.1f} nm")
        plt.tight_layout()
        plt.savefig(output_path.parent / f"{output_path.stem}_at_wavelength.png")
        
        # dB plot
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(fiber_angle, T_dB, '-o')
        ax.grid(which='major')
        ax.set_xlabel("Fiber Angle (degrees)")
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
                # Setup project layout
                spec, out, templates = setup("fdtd.grating_coupler_rectangular_3D", __file__)
                template_fsp = templates[0]
                figures_dir = out["figure_groups"].get("Sweep Functions", out["figures"])
                figures_dir.mkdir(parents=True, exist_ok=True)
                
                with lumapi.FDTD(str(template_fsp)) as fdtd:
                        # Uncomment to override the simulation region defined in the file
                        # override_fdtd(fdtd=fdtd)
                        # override_grating_coupler(fdtd=fdtd)

                        # Comment to skip the sweep
                        # fdtd.runsweep('sweep_fiber_angle')

                        # Get Coupling via the getFillFactorSweep function
                        T, wavelength, fiber_angle = getCouplingResponse(fdtd=fdtd)

                        # Define the output path for the plot
                        file_name_plot = figures_dir / "grating_coupler_sweep_fiber_angle.png"

                        # Plot the coupling response
                        plot_coupling_response(T, wavelength, fiber_angle, file_name_plot)

                        # Define target wavelength (example: 1550 nm)
                        target_wavelength = 1550e-9  # Convert to meters

                        # Plot maximum transmission at specific wavelength
                        plot_max_transmission_at_wavelength(T, wavelength, fiber_angle, target_wavelength, file_name_plot)
        except Exception as e:
                print(f"An error occurred: {e}")
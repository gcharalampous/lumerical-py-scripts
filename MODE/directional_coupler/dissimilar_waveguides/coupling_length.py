#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Calculates the coupling length for the transmission and bar ports
of the directional coupler.
"""

# Import required modules
import numpy as np
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup

spec, out, templates = setup("mode.directional_coupler", __file__)

# Import user-defined parameters
from MODE.directional_coupler.user_inputs.user_simulation_parameters import *
from MODE.directional_coupler.even_odd_mode_profile import super_mode_profile
from MODE.directional_coupler.mode_profile.mode_profile_2D import modeProfiles


def getSupermodes(mode):
    """Extract even and odd supermodes for TE and TM polarizations."""
    nTE = []
    nTM = []

    polariz_mode, sym_mode, neff, wavelength, num_modes = super_mode_profile(mode)

    # Locate the supermodes
    for i in range(len(polariz_mode) - 1):
        if polariz_mode[i] == 'TE' and polariz_mode[i+1] == 'TE':
            if (sym_mode[i] < 0 and sym_mode[i+1] >= 0) or (sym_mode[i] >= 0 and sym_mode[i+1] < 0):
                print('TE supermode found')
                mode.copydcard("mode" + str(i+1), "mode1_TE_super")
                mode.copydcard("mode" + str(i+2), "mode2_TE_super")
                nTE.append([neff[i], neff[i+1]])
            
        if polariz_mode[i] == 'TM' and polariz_mode[i+1] == 'TM':
            if (sym_mode[i] < 0 and sym_mode[i+1] >= 0) or (sym_mode[i] >= 0 and sym_mode[i+1] < 0):
                print('TM supermode found')
                nTM.append([neff[i], neff[i+1]])

    nTE_super = np.squeeze(nTE)
    nTM_super = np.squeeze(nTM)

    return nTE_super, nTM_super, wavelength


if __name__ == "__main__":
    spec, out, templates = setup("mode.directional_coupler", __file__)

    with lumapi.MODE(str(templates[0])) as mode:
        # Run simulation and find modes
        mode.switchtolayout()
        mode.mesh()
        mode.run()
        mode.findmodes()
                
        # Retrieve the effective indices of the supermodes
        nTE_super, nTM_super, wavelength = getSupermodes(mode)

        # Retrieve the effective indices of waveguide A (isolated)
        mode.switchtolayout()
        mode.setnamed("waveguide-constructor", "wg1_enable", 1)
        mode.setnamed("waveguide-constructor", "wg2_enable", 0)
        neff_wgA, _, polariz_mode, _ = modeProfiles(mode)
        gap = str(mode.getnamed("waveguide-constructor", "gap") * 1e9)

        # Find the TE mode and copy it
        for index, polar in enumerate(polariz_mode):
            if polar == 'TE':
                neff_wgA_TE = neff_wgA[index]
                mode.copydcard("mode" + str(index+1), "mode_wgA_TE")
                break

        # Perform power overlap integral
        coeff_mode1 = mode.overlap("mode_wgA_TE", "global_mode1_TE_super")[1]
        coeff_mode2 = mode.overlap("mode_wgA_TE", "global_mode2_TE_super")[1]

        # Normalize to amplitude coefficients
        norm = np.sqrt(np.abs(coeff_mode1) + np.abs(coeff_mode2))
        coeff_mode1_normalize = np.sqrt(np.abs(coeff_mode1)) / norm
        coeff_mode2_normalize = np.sqrt(np.abs(coeff_mode2)) / norm

        # Calculate the propagation constants of the supermodes
        beta_super_TE_mode1 = nTE_super[0] * (2 * np.pi / wavelength) * 1e-6
        beta_super_TE_mode2 = nTE_super[1] * (2 * np.pi / wavelength) * 1e-6

        # Create the beat length array
        L = np.arange(0, 3, 0.001)
        coupling_beat_length = L * (2 * np.pi) / np.abs(beta_super_TE_mode1 - beta_super_TE_mode2)

        # Calculate power in each waveguide
        c1_sq = np.abs(coeff_mode1_normalize)**2
        c2_sq = np.abs(coeff_mode2_normalize)**2
        delta_beta = beta_super_TE_mode2 - beta_super_TE_mode1
        
        Power_WGA = c1_sq**2 + c2_sq**2 + 2 * c1_sq * c2_sq * np.cos(delta_beta * coupling_beat_length)
        Power_WGB = 1 - Power_WGA

        # Plot coupling length
        px = 1 / plt.rcParams['figure.dpi']
        plt.figure(num_modes + 1, figsize=(512 * px, 256 * px))
        plt.plot(coupling_beat_length, 10 * np.log10(Power_WGA), 
                 coupling_beat_length, 10 * np.log10(Power_WGB))
        plt.title(f'TE Mode, gap = {gap} nm')
        plt.xlabel('Coupling length (μm)')
        plt.ylabel('Crosstalk (dB)')
        plt.legend(['WG-A', 'WG-B'])
        plt.tight_layout()

        # Save the plot
        file_name_plot = str(out["figure_groups"]["Dissimilar Waveguides"] / "length_TE_dissimilar_waveguides.png")
        plt.savefig(file_name_plot)
        plt.show()


        # Save the simulation
        mode.save(str(out["lumerical"] / "dissimilar_waveguide_modes.lms"))
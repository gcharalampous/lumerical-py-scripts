#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The script calculates the coupling length for the transmission and bar ports
of the directional coupler.


"""

#----------------------------------------------------------------------------
# Imports from user files
# --
# Import required modules
import numpy as np
import lumapi
from config import *
import matplotlib.pyplot as plt

# Import user-defined parameters
from MODE.directional_coupler.user_inputs.user_simulation_parameters import *
from MODE.directional_coupler.even_odd_mode_profile import super_mode_profile
from MODE.directional_coupler.user_inputs.user_simulation_parameters import my_dpi
from MODE.directional_coupler.mode_profile.mode_profile_2D import modeProfiles



# ---------------------------- Get Odd/Even Modes ---------------------------


def getSupermodes(mode):

    # Initialize empty lists
    nTE = []
    nTM = []

    # Retrieve the supermodes
    polariz_mode, sym_mode, neff, wavelength, num_modes = super_mode_profile(mode)


    # Locate the Super-mode
    for i in range(0,len(polariz_mode)-1):
        if (polariz_mode[i] == 'TE' and polariz_mode[i+1] == 'TE'):
            if(sym_mode[i] < 0 and sym_mode[i+1] >= 0 or 
            sym_mode[i] >= 0 and sym_mode[i+1] < 0):
                print('Great, TE supermode-found')
                mode.copydcard("mode"+str(i+1), "mode1_TE_super")
                mode.copydcard("mode"+str(i+2), "mode2_TE_super")
                nTE.append([neff[i],neff[i+1]])
            
        if (polariz_mode[i] == 'TM' and polariz_mode[i+1] == 'TM'):
            if(sym_mode[i] < 0 and sym_mode[i+1] >= 0 or 
            sym_mode[i] >= 0 and sym_mode[i+1] < 0):
                print('Great, TM supermode-found')
                nTM.append([neff[i],neff[i+1]])

    # Convert lists to numpy arrays and squeeze to remove redundant dimensions (supermodes)
    nTE_super = np.squeeze(nTE)
    nTM_super = np.squeeze(nTM)


    return nTE_super, nTM_super, wavelength




if(__name__=="__main__"):



    with lumapi.MODE(MODE_DC_DIRECTORY_READ) as mode:

    # Run the simulation, create a mesh, and compute the modes, then save
    

        # Initialize empty lists to store mode properties
        nTE_super = []      # TE even/odd effective index
        nTM_super = []      # TM even/odd effective index
        neff_wgA = []       # effective index of waveguide A
        neff_wgB = []       # effective index of waveguide B
        polariz_mode = []   # polarization mode

        # Switch to layout mode
        mode.switchtolayout()
        
        # Generate the mesh for the simulation
        mode.mesh()
        
        # Run the simulation
        mode.run()
        
        # Find the modes in the simulation
        mode.findmodes()
                
        # Retrieve the effective indices of the supermodes
        nTE_super, nTM_super, wavelength = getSupermodes(mode)



        # Retrieve the effective indices of the dissimilar waveguide modes isolated
        # Switch to layout mode
        mode.switchtolayout()
        mode.setnamed("waveguide-constructor", "wg1_enable", 1)
        mode.setnamed("waveguide-constructor", "wg2_enable", 0)
        neff_wgA, _, polariz_mode, _ = modeProfiles(mode)
        gap = str(mode.getnamed("waveguide-constructor","gap")*1e9)

        # Iterate through polariz_mode list
        for index, polar in enumerate(polariz_mode):
            if polar == 'TE':
                neff_wgA_TE = neff_wgA[index]
                mode.copydcard("mode"+str(index+1), "mode_wgA_TE")
                break  # Break the loop when the first 'TE' is found
        
        # # Switch to layout mode
        # mode.switchtolayout()
        # mode.setnamed("waveguide-constructor", "wg1_enable", 0)
        # mode.setnamed("waveguide-constructor", "wg2_enable", 1)
        # neff_wgB, _, polariz_mode, _ = modeProfiles(mode)

        # # Iterate through polariz_mode list
        # for index, polar in enumerate(polariz_mode):
        #     if polar == 'TE':
        #         neff_wgB_TE = neff_wgB[index]
        #         mode.copydcard("mode"+str(index+1), "mode_wgB_TE")
        #         break  # Break the loop when the first 'TE' is found

        # Perform Power Overlap Integral
        coeff_mode1 = mode.overlap("mode_wgA_TE", "global_mode1_TE_super")[1]
        coeff_mode2 = mode.overlap("mode_wgA_TE", "global_mode2_TE_super")[1]


        # Normalize to Amplitude coefficients
        coeff_mode1_normalize = np.sqrt(np.abs(coeff_mode1)) / (np.sqrt(np.abs(coeff_mode1) + np.abs(coeff_mode2)))
        coeff_mode2_normalize = np.sqrt(np.abs(coeff_mode2)) / (np.sqrt(np.abs(coeff_mode1) + np.abs(coeff_mode2)))


        # Calculate the propagation constants of the supermodes
        beta_super_TE_mode1 = nTE_super[0]*(2*np.pi/wavelength)*1e-6
        beta_super_TE_mode2 = nTE_super[1]*(2*np.pi/wavelength)*1e-6

        # Create the beat length for the supermodes
        L = np.arange(0, 10, 0.001)
        coupling_beat_length = L*(2*np.pi)/(np.abs(beta_super_TE_mode1 - beta_super_TE_mode2))


        Power_WGA = (np.abs(coeff_mode1_normalize)**4 + np.abs(coeff_mode2_normalize)**4) + 2 * np.abs(coeff_mode1_normalize)**2 * np.abs(coeff_mode2_normalize)**2 * np.cos((beta_super_TE_mode2 - beta_super_TE_mode1) * coupling_beat_length)

        Power_WGB = 1 - Power_WGA

        # Calculate the coupling coefficients for TE mode
        px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
        plt.figure(num_modes+1, figsize=(512 * px, 256 * px))
        plt.plot(coupling_beat_length, 10*np.log10(Power_WGA), coupling_beat_length, 10*np.log10(Power_WGB))

        plt.title('TE Mode, gap = ' + gap + " nm" )
        plt.xlabel('coupling length (um)')
        plt.ylabel('Crosstalk (dB)')
        plt.legend(['WG-A', 'WG-B'])

        plt.ylim([-80, 10])

        # Save the simulation
        mode.save(MODE_DC_DIRECTORY_WRITE_FILE + "\\dissimilar_waveguide_modes.lms")







# # Calculate the coupling coefficients for TE mode
# C = ((np.abs(np.real(nTE[0] - nTE[1]))) / wavelength) * np.pi
# t_te = np.power(np.cos(C * length_array), 2)   # Through
# k_te = np.power(np.sin(C * length_array), 2)   # Cross

# # Set the figure size
# px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
# plt.figure(num_modes+1, figsize=(512 * px, 256 * px))
   
# # Plot the coupling coefficients for TE mode
# plt.plot(length_array * 1e6, t_te, length_array * 1e6, k_te)
# plt.title('TE Mode')
# plt.xlabel('coupling length (um)')
# plt.legend(['Through', 'Cross'])
# plt.tight_layout()
# file_name_plot_writing = os.path.join(directory_to_write[1], 
#                                                     "TE_coupling_coef_.png")
# plt.savefig(file_name_plot_writing, dpi=my_dpi, format="png")

# # Calculate the coupling coefficients for TM mode
# C = ((np.abs(np.real(nTM[0] - nTM[1]))) / wavelength) * np.pi
# t_tm = np.power(np.cos(C * length_array), 2)   # Through
# k_tm = np.power(np.sin(C * length_array), 2)   # Cross

# # Set the figure size
# px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
# plt.figure(num_modes+2, figsize=(512 * px, 256 * px))

# # Plot the coupling coefficients for TM mode
# plt.plot(length_array * 1e6, t_tm, length_array * 1e6, k_tm)
# plt.title("TM Mode")
# plt.xlabel('coupling length (um)')
# plt.legend(['Through', 'Cross'])
# plt.tight_layout()
# file_name_plot_writing = os.path.join(directory_to_write[1], 
#                                                     "TM_coupling_coef_.png")
# plt.savefig(file_name_plot_writing, dpi=my_dpi, format="png")
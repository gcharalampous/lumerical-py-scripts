#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The script calculates the through and bar as a function of the coupling gap
of the directional coupler.


"""

#----------------------------------------------------------------------------
# Imports from user files
# --
# Import required modules
import numpy as np
import lumapi
import matplotlib.pyplot as plt
import pandas as pd
import os, sys 

# Add the parent directory to the system path
sys.path.append("..")

# Import user-defined parameters
from user_inputs.user_sweep_parameters import *
from get_mode import mode_profile

# Get the path of the current directory and the filename of the Lumerical file

cur_path = os.path.dirname(__file__)
print(cur_path)

filename = "waveguide_coupler.lms"
# Set the name of the waveguide constructor
waveguide_constructor = 'waveguide-constructor'

# Get the path of the Lumerical file
file_path = os.path.relpath('..\\user_inputs\\lumerical_files\\'+filename, cur_path)
print(file_path)

directory = "sweep"

# Create target Directory if it doesn't exist
if not os.path.exists(directory):
    os.mkdir(directory)
    print("Directory ", directory, " created ")
else:
    print("Directory ", directory, " already exists")

# Initialize empty lists
nTE = [0]*2
nTM = [0]*2

# Create an array of coupling lengths to sweep over
gap_array = np.arange(coupling_gap_start, coupling_gap_stop, coupling_gap_step)
Lx_te = [0]*len(gap_array)
Lx_tm = [0]*len(gap_array)
C_te = [0]*len(gap_array)
C_tm = [0]*len(gap_array)


polariz_mode, sym_mode, neff, wavelength, num_modes, mode = mode_profile(file_path)

for g in range(0,len(gap_array)):
    
    filename = "wavegude_coupler" + str(g) + ".lms"
    
    file_path = os.path.relpath('sweep\\'+filename, cur_path)

    mode.switchtolayout()
    mode.save(cur_path+'\\sweep\\' + filename)    
    mode.setnamed(waveguide_constructor,"gap",gap_array[g])
    mode.save(cur_path+'\\sweep\\' + filename)    
    mode.close()
    polariz_mode, sym_mode, neff, wavelength, num_modes, mode = mode_profile(file_path)

    # Locate the Super-mode
    for i in range(0,len(polariz_mode)-1):
        if (polariz_mode[i] == 'TE' and polariz_mode[i+1] == 'TE'):
            if(sym_mode[i] < 0 and sym_mode[i+1] >= 0 or 
               sym_mode[i] >= 0 and sym_mode[i+1] < 0):
                print('Great, TE supermode-found')
                nTE[0] = neff[i]
                nTE[1] = neff[i+1]
            
        if (polariz_mode[i] == 'TM' and polariz_mode[i+1] == 'TM'):
            if(sym_mode[i] < 0 and sym_mode[i+1] >= 0 or 
               sym_mode[i] >= 0 and sym_mode[i+1] < 0):
                print('Great, TM supermode-found')
                nTM[0] = neff[i]
                nTM[1] = neff[i+1]
    
    # Convert lists to numpy arrays and squeeze to remove redundant dimensions
    nTE = np.squeeze(nTE)
    nTM = np.squeeze(nTM)
    
    # Calculate the Lpi and Coupling coefficient C for TE mode
    Lx_te[g] = wavelength/((np.abs(np.real(nTE[0] - nTE[1])))*2)
    C_te[g] = ((np.abs(np.real(nTE[0] - nTE[1]))) / wavelength) * np.pi

    
   

       
    # plt.xlabel('coupling length (um)')
    # plt.legend(['Through', 'Cross'])
    
    # Calculate the Lpi for TM mode
    Lx_tm[g] = wavelength/((np.abs(np.real(nTM[0] - nTM[1])))*2)
    C_tm[g] = ((np.abs(np.real(nTM[0] - nTM[1]))) / wavelength) * np.pi
    
    # Set the figure size
    # px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
    # plt.figure(num_modes+2, figsize=(512 * px, 256 * px))
    
    # # Plot the coupling coefficients for TM mode
    # plt.plot(gap_array * 1e6, t_tm, gap_array * 1e6, k_tm)
    # plt.title("TM Mode")

    # plt.legend(['Through', 'Cross'])
    
    
   
    
   
# Set the figure size
px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
plt.figure(1, figsize=(512 * px, 256 * px))


# Plot the Lpi coefficients for TE and TM mode
Lx_tm = np.squeeze(Lx_tm)
Lx_te = np.squeeze(Lx_te)
plt.semilogy(gap_array * 1e6, Lx_te * 1e6,gap_array * 1e6, Lx_tm * 1e6)
plt.xlabel('coupling gap (um)')
plt.ylabel('$L_\pi$ (um)')
plt.legend(['TE','TM'])



# Plot the Coupling Coefficient of TE and TM mode
C_te = np.squeeze(C_te)
C_tm = np.squeeze(C_tm)
plt.figure(2, figsize=(512 * px, 256 * px))
plt.semilogy(gap_array * 1e6, C_te * 1e-6,gap_array * 1e6, C_tm * 1e-6)
plt.xlabel('coupling gap (um)')
plt.ylabel('Coupling Coefficient (/um)')
plt.legend(['TE','TM'])




mode.close()
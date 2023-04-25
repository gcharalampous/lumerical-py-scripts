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

# Initialize empty lists
nTE = []
nTM = []

# Create an array of coupling lengths to sweep over
length_array = np.arange(coupling_length_start, coupling_length_stop, coupling_length_step)



polariz_mode, sym_mode, neff, wavelength, num_modes, mode = mode_profile(file_path)


# Locate the Super-mode
for i in range(0,len(polariz_mode)-1):
    if (polariz_mode[i] == 'TE' and polariz_mode[i+1] == 'TE'):
        if(sym_mode[i] < 0 and sym_mode[i+1] >= 0 or 
           sym_mode[i] >= 0 and sym_mode[i+1] < 0):
            print('Great, TE supermode-found')
            nTE.append([neff[i],neff[i+1]])
        
    if (polariz_mode[i] == 'TM' and polariz_mode[i+1] == 'TM'):
        if(sym_mode[i] < 0 and sym_mode[i+1] >= 0 or 
           sym_mode[i] >= 0 and sym_mode[i+1] < 0):
            print('Great, TM supermode-found')
            nTM.append([neff[i],neff[i+1]])

# Convert lists to numpy arrays and squeeze to remove redundant dimensions
nTE = np.squeeze(nTE)
nTM = np.squeeze(nTM)

# Calculate the coupling coefficients for TE mode
C = ((np.abs(np.real(nTE[0] - nTE[1]))) / wavelength) * np.pi
t_te = np.power(np.cos(C * length_array), 2)   # Through
k_te = np.power(np.sin(C * length_array), 2)   # Cross

# Set the figure size
px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
plt.figure(num_modes+1, figsize=(512 * px, 256 * px))
   
# Plot the coupling coefficients for TE mode
plt.plot(length_array * 1e6, t_te, length_array * 1e6, k_te)
plt.title('TE Mode')
plt.xlabel('coupling length (um)')
plt.legend(['Through', 'Cross'])

# Calculate the coupling coefficients for TM mode
C = ((np.abs(np.real(nTM[0] - nTM[1]))) / wavelength) * np.pi
t_tm = np.power(np.cos(C * length_array), 2)   # Through
k_tm = np.power(np.sin(C * length_array), 2)   # Cross

# Set the figure size
px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
plt.figure(num_modes+2, figsize=(512 * px, 256 * px))

# Plot the coupling coefficients for TM mode
plt.plot(length_array * 1e6, t_tm, length_array * 1e6, k_tm)
plt.title("TM Mode")
plt.xlabel('coupling length (um)')
plt.legend(['Through', 'Cross'])

mode.close()
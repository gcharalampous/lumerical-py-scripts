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

# Import user-defined parameters
from MODE.directional_coupler.user_inputs.user_sweep_parameters import *
from MODE.directional_coupler.even_odd_mode_profile import mode_profile
from MODE.directional_coupler.user_inputs.user_simulation_parameters import my_dpi


# ------------------------- Directories for Results ---------------------------

# specify the directory path
path_to_write = ["MODE\\Results\\directional_coupler\\lumerical_files\\coupling_length",
"MODE\\Results\\directional_coupler\\Figures\\coupling_length"]
directory_to_write = ['']*len(path_to_write)


# get the current file path
current_path = os.path.abspath(__file__)

# get the directory of the current file
current_dir = os.path.dirname(current_path)

# find the project root directory by traversing up the directory 
# tree until a specific file is found
while not os.path.isfile(os.path.join(current_dir, ".gitignore")):
    # move up to the parent directory
    current_dir = os.path.dirname(current_dir)

for i in range(0,len(path_to_write)):
    directory_to_write[i] = os.path.join(current_dir, path_to_write[i])

    # create the directory if it doesn't exist already
    if not os.path.exists(directory_to_write[i]):
        os.makedirs(directory_to_write[i])
        print("Directory:" + directory_to_write[i] + "\n created successfully!")
    else:
        print("Directory:" + directory_to_write[i] + "\n already exists!")



# ---------------------------------------------------------------------------


# ------------------------- Directories for Reading ---------------------------

# Define path to read files from
path_to_read = "MODE\\directional_coupler\\user_inputs\\lumerical_files"

# Define the list of waveguide files to be loaded into Lumerical MODE
file_waveguide = ["waveguide_coupler.lms"]

# Get the current path and directory of this Python script
current_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_path)

# Move up the directory hierarchy until we find the .gitignore file,
# which is assumed to be in the root directory of the project
while not os.path.isfile(os.path.join(current_dir, ".gitignore")):
    current_dir = os.path.dirname(current_dir)

# Define the directory to read the files from, based on the project root directory
dir_to_read = os.path.join(current_dir, path_to_read)

# Initialize a list to store the names of the waveguide modes in Lumerical MODE
file_name_mode = [str]*len(file_waveguide)
# Get the current path and directory of this Python script
current_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_path)

# Move up the directory hierarchy until we find the .gitignore file,
# which is assumed to be in the root directory of the project
while not os.path.isfile(os.path.join(current_dir, ".gitignore")):
    current_dir = os.path.dirname(current_dir)

# Define the directory to read the files from, based on the project root directory
dir_to_read = os.path.join(current_dir, path_to_read)

# Initialize a list to store the names of the waveguide modes in Lumerical MODE
file_name_mode = [str]*len(file_waveguide)

# ---------------------------------------------------------------------------


# ---------------------------- Get Odd/Even Modes ---------------------------
file_name_mode[0] = os.path.join(dir_to_read, file_waveguide[0])

# Set the name of the waveguide constructor
waveguide_constructor = 'waveguide-constructor'





# Initialize empty lists
nTE = []
nTM = []

# Create an array of coupling lengths to sweep over
length_array = np.arange(coupling_length_start, coupling_length_stop, coupling_length_step)



polariz_mode, sym_mode, neff, wavelength, num_modes, mode = mode_profile(file_name_mode[0])


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
plt.tight_layout()
file_name_plot_writing = os.path.join(directory_to_write[1], 
                                                    "TE_coupling_coef_.png")
plt.savefig(file_name_plot_writing, dpi=my_dpi, format="png")

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
plt.tight_layout()
file_name_plot_writing = os.path.join(directory_to_write[1], 
                                                    "TM_coupling_coef_.png")
plt.savefig(file_name_plot_writing, dpi=my_dpi, format="png")
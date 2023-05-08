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

# Import user-defined parameters
from MODE.directional_coupler.user_inputs.user_sweep_parameters import *
from MODE.directional_coupler.even_odd_mode_profile import mode_profile
from MODE.directional_coupler.user_inputs.user_simulation_parameters import my_dpi


# ------------------------- Directories for Results ---------------------------

# specify the directory path
path_to_write = ["MODE\\Results\\directional_coupler\\lumerical_files\\coupling_gap",
"MODE\\Results\\directional_coupler\\Figures\\coupling_gap"]
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

# --------------------------- Generate Sweep Files --------------------------
gap_array = np.arange(coupling_gap_start, coupling_gap_stop, coupling_gap_step)
file_name_mode_writing = ['str']*len(gap_array)

file_name_mode[0] = os.path.join(dir_to_read, file_waveguide[0])


# Set the name of the waveguide constructor
waveguide_constructor = 'waveguide-constructor'


for g in range(0,len(gap_array)):
    with lumapi.MODE() as mode:
        mode.load(file_name_mode[0])
        mode.setnamed(waveguide_constructor,"gap",gap_array[g])
        file_name_mode_writing[g] = os.path.join(directory_to_write[0], 
                                                    "waveguide_mode_sweep" + str(g) + ".lms")
        mode.save(file_name_mode_writing[g])  
        
# ---------------------------------------------------------------------------
        
# -------------------------------- Simulations ------------------------------

# Initialize empty lists
nTE = [0]*2
nTM = [0]*2

# Create an array of coupling lengths to sweep over
Lx_te = [0]*len(gap_array)
Lx_tm = [0]*len(gap_array)
C_te = [0]*len(gap_array)
C_tm = [0]*len(gap_array)
file_name_mode_load = ['str']*len(gap_array)


for g in range(0,len(gap_array)):
    
    


    polariz_mode, sym_mode, neff, wavelength, num_modes, mode = mode_profile(file_name_mode_writing[g])
    # mode.save(file_name_mode_writing[g])
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
plt.tight_layout()
file_name_plot_writing = os.path.join(directory_to_write[1], 
                                                    "Lpi_coupling_coef_.png")
plt.savefig(file_name_plot_writing, dpi=my_dpi, format="png")


# Plot the Coupling Coefficient of TE and TM mode
C_te = np.squeeze(C_te)
C_tm = np.squeeze(C_tm)
plt.figure(2, figsize=(512 * px, 256 * px))
plt.semilogy(gap_array * 1e6, C_te * 1e-6,gap_array * 1e6, C_tm * 1e-6)
plt.xlabel('coupling gap (um)')
plt.ylabel('Coupling Coefficient (/um)')
plt.legend(['TE','TM'])
plt.tight_layout()
file_name_plot_writing = os.path.join(directory_to_write[1], 
                                                    "TMTE_coupling_coef_.png")
plt.savefig(file_name_plot_writing, dpi=my_dpi, format="png")




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script calculates the apperture profile of the star coupler specified in 
'user_inputs/awg_input_taper.lms' and 'user_simulation_parameters.py'.

"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
import os 


# Import user-defined parameters from another file
from MODE.directional_coupler.user_inputs.user_simulation_parameters import *


# ------------------------- Directories for Results ---------------------------

# specify the directory path
path_to_write = ["MODE\\Results\\awg_star_coupler\\lumerical_files\\mode_profile",
"MODE\\Results\\awg_star_coupler\\Figures\\mode_profile"]
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
path_to_read = "MODE\\awg_star_coupler\\user_inputs\\lumerical_files"

# Define the list of waveguide files to be loaded into Lumerical MODE
file_waveguide = ["awg_input_taper.lms"]

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


with lumapi.MODE() as mode:
    mode.switchtolayout()
    mode.load(file_name_mode[0])
    mode.run()
    file_name_mode_writing = os.path.join(directory_to_write[0], 
                                                    "awg_star_coupler.lms")
    mode.save(file_name_mode_writing)            
    
    
    # Get the index profile
    
    index = np.squeeze(mode.getdata("effective_index","index_x"))
    x = np.squeeze(mode.getdata("effective_index","x"))
    y = np.squeeze(mode.getdata("effective_index","y"))


px = 1/plt.rcParams['figure.dpi']  # pixel in inches
fig, ax = plt.subplots(figsize=(512*px, 256*px))

c = ax.pcolormesh(x*1e6,y*1e6,np.real(np.transpose(index)),shading = 'gouraud',cmap = 'jet')
fig.colorbar(c, ax = ax)

ax.set_xlabel("x (\u00B5m)")
ax.set_ylabel("y (\u00B5m)")
ax.set_title("Star Coupler Index Mesh")


file_name_plot_writing = os.path.join(directory_to_write[1], 
                                            "index_mesh.png")


fig.savefig(file_name_plot_writing, dpi=my_dpi, format="png")
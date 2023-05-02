#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts calculates the overlap integral for the mode order you defined in
the user_simulation_parameters.py.

# 4.1 Waveguide_1.lms
m_waveguide1=2

# 4.2 Waveguide_2.lms
m_waveguide2=1


"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------
# Import necessary modules
import lumapi
from MODE.butt_coupling.user_inputs.user_simulation_parameters import *
from MODE.butt_coupling.user_inputs.user_sweep_parameters import *
import numpy as np
import os 
import matplotlib.pyplot as plt


# ------------------------- Directories for Results ---------------------------

# specify the directory path
path_to_write = ["MODE\\Results\\butt_coupling\\Figures\\sweep_misalignment"]
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
path_to_read = "MODE\\Results\\butt_coupling\\lumerical_files\\d_cards"

# Define the list of waveguide files to be loaded into Lumerical MODE
file_waveguide = ['waveguide_1.ldf', 'waveguide_2.ldf']

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




# ------------------------- Start Sweeping Misalign---------------------------

# Initialize the misalignment arrays
misalign_y_array = np.arange(misalign_y_start,misalign_y_stop,misalign_y_step)
misalign_z_array = np.arange(misalign_z_start,misalign_z_stop,misalign_z_step)


w, h = 2, len(misalign_y_array)
overlap_y = [[0 for x in range(w)] for y in range(h)] 
w, h = 2, len(misalign_z_array)
overlap_z = [[0 for x in range(w)] for y in range(h)] 

# Initialize LumAPI and turn off redraw for faster simulations
with lumapi.MODE() as mode:
    
    # Switch to layout mode
    mode.switchtolayout()
    
    # Load each waveguide file into Lumerical MODE
    for i in range(0,len(file_waveguide)):
        file_name_mode[i] = os.path.join(dir_to_read, file_waveguide[i])
        mode.loaddata(file_name_mode[i])

    
    
    for i in range(len(misalign_y_array)):
        overlap_y[i] = mode.overlap("waveguide_1_mode" + str(m_waveguide1), 
                            "waveguide_2_mode" + str(m_waveguide2)
                            ,0,misalign_y_array[i],0)

    for i in range(len(misalign_z_array)):
        overlap_z[i] = mode.overlap("waveguide_1_mode" + str(m_waveguide1), 
                            "waveguide_2_mode" + str(m_waveguide2)
                            ,0,0,misalign_z_array[i])


# ---------------------------------------------------------------------------


# ----------------------- Prepare the data for plots --------------------------
overlap_y_coupling = [0]*len(overlap_y)
overlap_y_power = [0]*len(overlap_y)

overlap_z_coupling = [0]*len(overlap_z)
overlap_z_power = [0]*len(overlap_z)


for i in range(0,len(overlap_y)):
    overlap_y_coupling[i] = overlap_y[i][0]
    overlap_y_power[i] = overlap_y[i][1]
            
for i in range(0,len(overlap_z)):
    overlap_z_coupling[i] = overlap_z[i][0]
    overlap_z_power[i] = overlap_z[i][1]
                    
# ---------------------------------------------------------------------------


# ---------------------------  Plot the Results  ----------------------------
# Plot overlap integral versus waveguide y-axis missalignement for given mode
plt.figure(figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)

plt.plot(misalign_y_array*1e6,overlap_y_coupling,'-o', label = 'Mode Coupling')
plt.plot(misalign_y_array*1e6,overlap_y_power,'-o', label = 'Power Coupling')
plt.legend()
plt.xlabel("Horizontal y-axis (um)")
plt.ylabel("Mode Overlap")
plt.ylim([0,1])
plt.title("Horizontal Misalignment") 
plt.legend()

# Save the figure files as .png     
file_name_plot = os.path.join(directory_to_write[0], "overlap_misalignment_horizontal" + ".png")
plt.tight_layout()
plt.savefig(file_name_plot, dpi=my_dpi, format="png")


# Plot overlap integral versus waveguide z-axis missalignement for given mode
plt.figure(figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)

plt.plot(misalign_z_array*1e6,overlap_z_coupling,'-o', label = 'Mode Coupling')
plt.plot(misalign_z_array*1e6,overlap_z_power,'-o', label = 'Power Coupling')
plt.legend()
plt.xlabel("Vertical z-axis (um)")
plt.ylabel("Mode Overlap")
plt.ylim([0,1])
plt.title("Vertical Misalignment") 
plt.legend()


# Save the figure files as .png     
file_name_plot = os.path.join(directory_to_write[0], "overlap_misalignment_vertical" + ".png")
plt.tight_layout()
plt.savefig(file_name_plot, dpi=my_dpi, format="png")




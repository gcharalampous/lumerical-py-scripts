#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts sweeps the width of the waveguide and calculates the effective
index for the number of modes you defined.
"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

# Import necessary libraries and modules
import numpy as np
import lumapi
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Import user-defined input parameters
from MODE.waveguide.user_inputs.user_sweep_parameters import *    
from MODE.waveguide.waveguide_render import *
from MODE.waveguide.fde_region import add_fde_region  


# ------------------------- Directories for Results ---------------------------

# specify the directory path
path_to_write = ["MODE\\Results\\waveguide\\Figures\\sweep_height",
"MODE\\Results\\waveguide\\lumerical_files\\sweep_height"]
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



# Create a MODE object
mode = lumapi.MODE()

# Turn off redraw to speed up simulation
mode.redrawoff()

# Define the waveguide and FDE region
waveguide_draw(mode)
add_fde_region(mode)

# Create an array to store waveguide height values for each simulation
wg_height_array = np.arange(wg_height_start, wg_height_stop, wg_height_step) 

# Create empty arrays to store simulation results
h, w = len(wg_height_array), num_modes
neff = [[0 for y in range(w)] for x in range(h)] 
polariz_frac = [[0 for y in range(w)] for x in range(h)] 
polariz_mode = [[0 for y in range(w)] for x in range(h)] 

# Loop over each waveguide height value and simulate the waveguide for each height
for wd in range(0,len(wg_height_array)):
    mode.switchtolayout()    
    mode.setnamed("waveguide","y max",wg_height_array[wd])
    mode.setnamed("mesh","y max",wg_height_array[wd])
    mode.run()
    mode.mesh()
    mode.findmodes()

    # Save the file
    file_name_mode = os.path.join(directory_to_write[1], "waveguide_mode_height_sweep_" + str(wd) + ".lms")
    mode.save(file_name_mode)

    # Store the neff and TE polarization fraction values for each mode
    for m in range(1,num_modes+1):
        neff[wd][m-1] = (mode.getdata("FDE::data::mode"+str(m),"neff"))
        polariz_frac[wd][m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
        
#        if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
#        	polariz_mode[wd][m-1] = ("TE")
#        else:
#            polariz_mode[wd][m-1] = ("TM")    
    
# Squeeze the neff and TE polarization fraction arrays
neff_array = np.squeeze(neff)
polariz_frac_array = np.squeeze(polariz_frac)

# Create a plot of neff vs. waveguide height for each mode
plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
for m in range(1,num_modes+1):
    plt.plot(wg_height_array*1e6,np.real(neff_array[:,m-1]),'-o', label = 'M-'+str(m))

plt.legend()
plt.xlabel("height (um)")
plt.ylabel("neff")
plt.title("width "+ str(wg_width*1e6) + " um") 

# Turn on redraw feature to update simulation layout
mode.redrawon()

# Save the figure files as .png
file_name_plot = os.path.join(directory_to_write[0], "neff_height_sweep" + ".png")
plt.tight_layout()
plt.savefig(file_name_plot, dpi=my_dpi, format="png")

# Close the session
mode.close()
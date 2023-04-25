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
# Import necessary modules
import numpy as np
import os
import lumapi
import matplotlib.pyplot as plt

# Import user-defined input parameters
from MODE.waveguide.user_inputs.user_sweep_parameters import *    
from MODE.waveguide.waveguide_render import *
from MODE.waveguide.fde_region import add_fde_region  


# ------------------------- Directories for Results ---------------------------

# specify the directory path
path_to_write = ["MODE\\Results\\waveguide\\Figures\\sweep_width",
"MODE\\Results\\waveguide\\lumerical_files\\sweep_width"]
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


# Create a MODE instance and turn off redraw feature
mode = lumapi.MODE()
mode.redrawoff()

# Draw the waveguide structure and add a finite-difference eigenmode (FDE) region
waveguide_draw(mode)
add_fde_region(mode)

# Create an empty list for waveguide widths and use numpy to generate a list based on user-defined parameters
wg_width_array = []
wg_width_array = np.arange(wg_width_start, wg_width_stop, wg_width_step) 

# Initialize empty 2D lists to store effective index and polarization fraction for each mode and width
h, w = len(wg_width_array), num_modes
neff = [[0 for y in range(w)] for x in range(h)] 
polariz_frac = [[0 for y in range(w)] for x in range(h)] 
polariz_mode = [[0 for y in range(w)] for x in range(h)] 

# Nested for loop to iterate over each waveguide width and mode
for wd in range(0,len(wg_width_array)):
    mode.switchtolayout()    
    mode.setnamed("waveguide","x span",wg_width_array[wd])
    mode.setnamed("mesh","x span",wg_width_array[wd])
    mode.run()
    mode.mesh()
    mode.findmodes()
    
    # Save the file
    file_name_mode = os.path.join(directory_to_write[1], "waveguide_mode_width_sweep_" + str(wd) + ".lms")
    mode.save(file_name_mode)

    for m in range(1,num_modes+1):
        # Get effective index and polarization fraction for each mode and store in corresponding 2D list
        neff[wd][m-1] = (mode.getdata("FDE::data::mode"+str(m),"neff"))
        polariz_frac[wd][m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
        
#        if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
#        	polariz_mode[wd][m-1] = ("TE")
#        else:
#            polariz_mode[wd][m-1] = ("TM")    
    
neff_array = np.squeeze(neff)
polariz_frac_array = np.squeeze(polariz_frac)

# Plot effective index versus waveguide width for each mode
plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
for m in range(1,num_modes+1):
    plt.plot(wg_width_array*1e6,np.real(neff_array[:,m-1]),'-o', label = 'M-'+str(m))
plt.legend()
plt.xlabel("width (um)")
plt.ylabel("neff")
plt.title("thickness "+ str(wg_thickness*1e6) + " um") 

# Turn on redraw feature to update simulation layout
mode.redrawon()

# Save the figure files as .png
file_name_plot = os.path.join(directory_to_write[0], "neff_width_sweep" + ".png")
plt.tight_layout()
plt.savefig(file_name_plot, dpi=my_dpi, format="png")

# Close the session
mode.close()
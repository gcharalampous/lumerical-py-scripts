#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script calculates the mode profile for the number of modes (num_modes) 
specified in 'user_simulation_parameters.py'.

The scripts calculates the effective index of each mode and plots the profile,
it also quantifies if the mode is TE or TM based on the polarization fraction.

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


from MODE.disk_waveguide.waveguide_render import *
from MODE.disk_waveguide.fde_region import add_fde_region  


# ------------------------- No inputs are required ---------------------------

# ------------------------- Directories for Results ---------------------------

# specify the directory path
path_to_write = ["MODE\\Results\\disk_waveguide\\Figures\\mode_profile",
"MODE\\Results\\disk_waveguide\\lumerical_files\\mode_profile"]
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

# Initialize LumAPI and turn off redraw for faster simulations
mode = lumapi.MODE()
mode.redrawoff()

# Draw the waveguide structure using a custom function
waveguide_draw(mode)

# Add a finite-difference eigenmode (FDE) region to the simulation environment
add_fde_region(mode)

# Run the simulation, create a mesh, and compute the modes
mode.run()
mode.mesh()
mode.findmodes()

# Initialize empty lists to store mode properties
neff = []           # effective index
polariz_frac = []   # polarization fraction
polariz_mode = []   # polarization mode (TE or TM)

# Loop over each mode and extract its properties
for m in range(1,num_modes+1):
    # Extract effective index and polarization fraction
    neff.append(mode.getdata("FDE::data::mode"+str(m),"neff"))
    polariz_frac.append(mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
    
    # Determine if mode is TE-like or TM-like based on polarization fraction
    if ( polariz_frac[m-1] > 0.5 ):
        polariz_mode.append("TE")
    else:
        polariz_mode.append("TM")

    # Extract electric and magnetic fields and plot the electric field
    plt.figure(m-1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
    x  = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"x")); 
    y= np.squeeze(mode.getdata("FDE::data::mode"+str(m),"y"));
    E1 = np.squeeze(mode.getelectric("FDE::data::mode"+str(m)))
    H1 = np.squeeze(mode.getmagnetic("FDE::data::mode"+str(m)))



    plt.pcolormesh(x*1e6,y*1e6,np.transpose(E1),shading = 'gouraud',cmap = 'jet')
    plt.colorbar()
    plt.xlabel("x (\u00B5m)")
    plt.ylabel("y (\u00B5m)")
    plt.title("Mode-"+str(m) + "(E-field): " + polariz_mode[m-1] + ", neff=" + str(np.round(neff[m-1],4)))


    #add the disk waveguide
    plt.gca().add_patch(Rectangle((0, 0),
                        x.min()*1e6,wg_thickness*1e6,
                        ec='white',
                        fc='none',
                        lw=0.5))


    # Save the figure files as .png
    file_name_plot = os.path.join(directory_to_write[0], "mode_profile_" + str(m) + ".png")
    plt.tight_layout()
    plt.savefig(file_name_plot, dpi=my_dpi, format="png")


# Turn redraw back on
mode.redrawon()  

# Save the file
file_name_mode = os.path.join(directory_to_write[1], "disk_mode_profile" + ".lms")
mode.save(file_name_mode)

# Close the mode solutions session
mode.close()    
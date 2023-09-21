#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script calculates the index mesh for the given waveguide specified in 
'user_simulation_parameters.py'.


"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os 


from MODE.waveguide.waveguide_render import *
from MODE.waveguide.fde_region import add_fde_region  


# -------------------_----- No inputs are required ---------------------------
# ------------------------- Directories for Results ---------------------------

# specify the directory path
path_to_write = ["MODE\\Results\\waveguide\\Figures\\mode_profile",
"MODE\\Results\\waveguide\\lumerical_files\\mode_profile"]
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











# Extract electric and magnetic fields and plot the electric field
plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)



x  = np.squeeze(mode.getdata("FDE::data::material","x")); 
y  = np.squeeze(mode.getdata("FDE::data::material","y")); 
index_x = np.squeeze(mode.getdata("FDE::data::material","index_x"));
index_y = np.squeeze(mode.getdata("FDE::data::material","index_y"));


plt.pcolormesh(x*1e6,y*1e6,np.real(np.transpose(index_x)),shading = 'gouraud',cmap = 'jet')
plt.colorbar()

plt.xlabel("x (\u00B5m)")
plt.ylabel("y (\u00B5m)")
plt.title("Waveguide Index Mesh")



# Save the figure files as .png
file_name_plot = os.path.join(directory_to_write[0], "waveguide_index_mesh" + ".png")
plt.tight_layout()
plt.savefig(file_name_plot, dpi=my_dpi, format="png")

# # Turn redraw back on and close LumAPI connection
mode.redrawon()  

# # Save the file
file_name_mode = os.path.join(directory_to_write[1], "waveguide_index_mesh" + ".lms")
mode.save(file_name_mode)

# Close the MODE session
mode.close()    

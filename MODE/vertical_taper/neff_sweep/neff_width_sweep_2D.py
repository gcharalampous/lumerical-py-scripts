#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts sweeps the width of the waveguide and calculates the effective
index for the TE Mode.

if you prefer calculating the effective index of the TM mode, modify the
lines between 86 and 100.
"""

#----------------------------------------------------------------------------
# Imports from user files
# --

import numpy as np
import lumapi
import matplotlib.pyplot as plt
import pandas as pd
import os 



from MODE.vertical_taper.user_inputs.user_sweep_parameters import *    


# ------------------------- Directories for Results ---------------------------

# specify the directory path
path_to_write = ["MODE\\Results\\vertical_taper\\lumerical_files\\sweep_width",
"MODE\\Results\\vertical_taper\\Figures\\sweep_taper_length"]
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
path_to_read = "MODE\\vertical_taper\\user_inputs\\lumerical_files"

# Define the list of waveguide files to be loaded into Lumerical MODE
file_waveguide = ["taper_waveguide_layer1.lms", "taper_waveguide_layer2.lms"]

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



# ---------------------------- Start Sweeping --------------------------------
taper_length_array = np.linspace(0,taper_length,res)



w, h = 2, len(taper_length_array)
neff = [[0 for x in range(w)] for y in range(h)] 
neff_wg1 = [0]*len(taper_length_array)
neff_wg2 = [0]*len(taper_length_array)



for i in range(0,len(file_waveguide)):
    
    if(i == 0):
        width_wg_left = width_wg_left_1 
        width_wg_right = width_wg_right_1
    else:
        width_wg_left = width_wg_left_2 
        width_wg_right = width_wg_right_2
    
    
    alpha = (width_wg_left - width_wg_right)/taper_length**m;
    wg_width_array = alpha * (taper_length - taper_length_array)**m + width_wg_right;
    
    
    waveguide_constructor = 'waveguide-constructor'
    
    file_name_mode[i] = os.path.join(dir_to_read, file_waveguide[i])
    
    
    with lumapi.MODE() as mode:
        mode.load(file_name_mode[i])
        mode.switchtolayout()
        mode.redrawoff()

        
        
        structure_waveguide = waveguide_constructor + "::waveguide_core"
        
        
        
        polariz_frac = [0]*num_modes
        
        
        
        mode.setnamed("FDE","number of trial modes",num_modes)
        
        
        for wd in range(0,len(wg_width_array)):
            print("Loop: " + str(wd))
            mode.switchtolayout()    
            mode.setnamed(waveguide_constructor,"width",wg_width_array[wd])
            mode.setnamed("mesh_waveguide","x span",wg_width_array[wd])
            mode.save()
            mode.mesh()
            mode.run()
            mode.findmodes()
            file_name_mode_writing = os.path.join(directory_to_write[0], 
                                                    "waveguide_"+str(i+1)+"_width_sweep_" +str(wd) + ".lms")
            mode.save(file_name_mode_writing)            
            for m in range(1,num_modes+1):
                polariz_frac[m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
                
                if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
        
                    # Do something when you find the TE Mode
                    print("TE Mode " + str(m) + "\n")
                    neff[wd][i] = (mode.getdata("FDE::data::mode"+str(m),"neff"))
                    break;
        
                else:
                    # Do something when you find the TM Mode
                    print("TM Mode " + str(m) + "\n")
                    continue;
        
# ---------------------------------------------------------------------------

# ---------------------------- Plot/Save Results - ---------------------------


# Get the data from the neff lists and prepare for the plot
for n in range(0,len(neff)):
    neff_wg1[n] = np.real(neff[n][0])
    neff_wg2[n] = np.real(neff[n][1])

neff_wg1=np.squeeze(neff_wg1)
neff_wg2=np.squeeze(neff_wg2)
    
plt.figure(figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)

plt.plot(taper_length_array*1e6, neff_wg1,label = 'taper-1')
plt.plot(taper_length_array*1e6, neff_wg2,label = 'taper-2')


plt.xlabel('Taper Length (um)')
plt.ylabel('neff')
plt.legend()

# Save the figure files as .png     
file_name_plot = os.path.join(directory_to_write[1], "neff_sweep_width" + ".png")
plt.tight_layout()
plt.savefig(file_name_plot, dpi=my_dpi, format="png")




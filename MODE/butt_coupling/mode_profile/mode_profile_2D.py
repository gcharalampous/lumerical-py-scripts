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

The mode profiles are save to a d-cards which are loaded later from 
overlap_mode.overlap_mode_integral_2D.py

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from MODE.butt_coupling.fde_region import *



# -------------------_----- No inputs are required ---------------------------
# ------------------------- Directories for Results ---------------------------

# specify the directory path
path_to_write = ["MODE\\Results\\butt_coupling\\Figures\\mode_profile",
"MODE\\Results\\butt_coupling\\lumerical_files\\mode_profile",
"MODE\\Results\\butt_coupling\\lumerical_files\\d_cards"]
directory_to_write = ['']*len(path_to_write)

path_to_read = "MODE\\butt_coupling\\user_inputs\\lumerical_files"

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



# Search for the two template files 
filename = ["waveguide_1.lms", "waveguide_2.lms"]
directory_to_read = [str]*len(filename)
file_directory = [str]*len(filename)
polariz_mode_waveguide = []#[[0 for j in range(num_modes)] for i in range(len(filename))]

for i in range(0,len(filename)):
    directory_to_read[i] = os.path.join(current_dir, path_to_read)
    file_directory[i] = os.path.join(directory_to_read[i], filename[i])



for i in range(0,len(filename)):
    with lumapi.MODE(file_directory[i]) as mode:
        mode.switchtolayout()

        # Reload the simulation region from user_inputs.user_simualtion_parameters
        add_fde_region(mode)

        # Set and Get the data
        mode.setnamed("FDE","number of trial modes",num_modes)
        wg_width = mode.getnamed("waveguide-constructor::waveguide_core","y span")
        wg_thickness = mode.getnamed("waveguide-constructor::waveguide_core","z max")
        slab_thickness = mode.getnamed("waveguide-constructor::rib","z max")
        simulation_span_y = mode.getnamed("::model","FDE_span_y")
        
        
        mode.mesh()
        mode.findmodes()
       
        
        # Save the file
        file_name_mode = os.path.join(directory_to_write[1], "waveguide_mode_profile_" +str(i+1) + ".lms")
        mode.save(file_name_mode)
        mode.save()
        
        # Initialize empty lists to store mode properties
        neff = []           # effective index
        polariz_frac = []   # polarization fraction
        # polarization mode (TE or TM)
        polariz_mode = ['str']*num_modes
    

        for m in range(1,num_modes+1):
            
            # Copy d-card mode to the global deck
            mode.copydcard("mode" + str(m),"waveguide_" + str(i+1) + "_mode" + str(m))
            
            # Extract effective index and polarization fraction
            neff.append(mode.getdata("FDE::data::mode"+str(m),"neff"))
            polariz_frac.append(mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
            
            # Determine if mode is TE-like or TM-like based on polarization fraction
            if ( polariz_frac[m-1] > 0.5 ):
                polariz_mode[m-1] = "TE"
            else:
                polariz_mode[m-1] = "TM"
     
     
            # Extract electric and magnetic fields and plot the electric field
            plt.figure(figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
            y  = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"y"))
            z = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"z"))
            E1 = np.squeeze(mode.getelectric("FDE::data::mode"+str(m)))
            H1 = np.squeeze(mode.getmagnetic("FDE::data::mode"+str(m)))
            plt.pcolormesh(y*1e6,z*1e6,np.transpose(E1),shading = 'gouraud',cmap = 'jet')


            plt.xlabel("y (\u00B5m)")
            plt.ylabel("z (\u00B5m)")
            plt.title("Mode-"+str(m) + "(E-field): " + polariz_mode[m-1] + ", neff=" + str(np.round(neff[m-1],4)))
            print('Waveguide_' + str(i+1) + '.lms, Mode: ' + str(m))
            
            
            #add the waveguide
            plt.gca().add_patch(Rectangle((-0.5*wg_width*1e6, 0),
                                wg_width*1e6,wg_thickness*1e6,
                                ec='white',
                                fc='none',
                                lw=0.5))
            
            if(slab_thickness > 0):
                #add the slab
                plt.gca().add_patch(Rectangle((-0.5*simulation_span_y*1e6, 0),
                                    simulation_span_y*1e6,slab_thickness*1e6,
                                    ec='white',
                                    fc='none',
                                    lw=0.5))

            # Save the figure files as .png
            file_name_plot = os.path.join(directory_to_write[0], "waveguide_" +str(i+1) + "_mode_profile_" +  str(m) + ".png")
            plt.tight_layout()
            plt.savefig(file_name_plot, dpi=my_dpi, format="png")
            plt.show()
            x = ["a","a"]
        polariz_mode_waveguide.append(polariz_mode)
        print(polariz_mode_waveguide)
        file_name_ldf = os.path.join(directory_to_write[2], "waveguide_" +str(i+1) + ".ldf")
        mode.savedcard(file_name_ldf)

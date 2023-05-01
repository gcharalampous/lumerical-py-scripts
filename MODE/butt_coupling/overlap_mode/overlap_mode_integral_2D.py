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
import os 


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

# Initialize LumAPI and turn off redraw for faster simulations
with lumapi.MODE() as mode:
    
    # Switch to layout mode
    mode.switchtolayout()
    
    # Load each waveguide file into Lumerical MODE
    for i in range(0,len(file_waveguide)):
        file_name_mode[i] = os.path.join(dir_to_read, file_waveguide[i])
        mode.loaddata(file_name_mode[i])

    # Compute the overlap integral between the two waveguides
    print("Overlap Integral [Mode,Power]\n")
    print(mode.overlap("waveguide_1_mode" + str(m_waveguide1), 
                       "waveguide_2_mode" + str(m_waveguide2)))

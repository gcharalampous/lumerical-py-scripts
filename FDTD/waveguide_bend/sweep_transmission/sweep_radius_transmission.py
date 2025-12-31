#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts sweeps the radius of the waveguide and calculates the transmission
of the fundamental mode.
"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

"""
No user-inputs are required.

The scripts sweeps the width of the waveguide and calculates the effective
index for the TE Mode.

"""

#----------------------------------------------------------------------------
# Imports from user files
# --

# Import necessary libraries
import numpy as np
import lumapi
import matplotlib.pyplot as plt
import os 
import sys 

# Add path to custom module directory
sys.path.append("..")

# Import user inputs
from user_inputs.user_sweep_parameters import bend_radius_start, bend_radius_stop,bend_radius_step   

# Get the current working directory and the filename
cur_path = os.path.dirname(__file__)
filename = "waveguide_bend.lms"

# Define the waveguide constructor
waveguide_constructor = 'waveguide-constructor'

# Define the file path
file_path = os.path.relpath('..\\user_inputs\\lumerical_files\\'+filename, cur_path)

# Connect to the Lumerical FDTD software
fdtd = lumapi.FDTD(file_path)

# Turn off redrawing of the FDTD layout
fdtd.redrawoff()

# Create an array of bend radii to sweep through
bend_radius_array = np.arange(bend_radius_start,bend_radius_stop,bend_radius_step)

# Initialize arrays to store the transmission coefficients
trans_f=[]
trans_t=[]

# Loop through each bend radius value
for rad in range(0,len(bend_radius_array)):
    print("Loop: " + str(rad))
    
    # Switch to the layout mode
    fdtd.switchtolayout()
    
    # Set the bend radius to the current value
    fdtd.setnamed(waveguide_constructor,"bend_radius",bend_radius_array[rad])
    
    # Save the changes
    fdtd.save()
    
    # Run the simulation
    fdtd.run()
    
    # Store the transmission coefficients
    trans_f.append(fdtd.getresult("monitor_exp","expansion for T").get("T_forward"))
    trans_t.append(fdtd.getresult("monitor_exp","expansion for T").get("T_total"))

# Convert the transmission arrays to numpy arrays
trans_f_array = np.squeeze(trans_f)   
trans_t_array = np.squeeze(trans_t)

# Plot the transmission coefficients versus the bend radius
plt.plot(bend_radius_array*1e6,trans_t_array,bend_radius_array*1e6,trans_f_array)
plt.ylabel('Transmission')
plt.xlabel('Radius [um]')
plt.legend(['Total','Fundamental'])

# Turn on redrawing of the FDTD layout
fdtd.redrawon()

# Close the connection to the Lumerical FDTD software
fdtd.close()

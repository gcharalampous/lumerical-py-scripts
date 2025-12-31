#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script calculates the mode profile for the mode specified in the
'user_simulation_parameters.py'.

The scripts calculates a slice of the E-field along the y-direction and x-
direction. Additionally, the 2D E-field distributions for the top-view,
side-view and cross-section of the waveguide.

"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import sys,os 

# Add the parent directory of the current file to the system path
sys.path.append("..")

# Import user-defined parameters from another file
from user_inputs.user_sweep_parameters import *

# Get the path of the current directory and the filename of the Lumerical file
cur_path = os.path.dirname(__file__)
filename = "waveguide_bend.lms"
   
# Set the name of the waveguide constructor
waveguide_constructor = 'waveguide-constructor'

# Get the path of the Lumerical file
file_path = os.path.relpath('..\\user_inputs\\lumerical_files\\'+filename, cur_path)

# Open a Lumerical FDTD session
fdtd = lumapi.FDTD(file_path)


# Plot the top-down view of the E-field distribution
plt.figure(1)

# Get the x, y, z, Ex, Ey, and Ez components of the E-field distribution
# from the simulation
x  = np.squeeze(fdtd.getdata("topdown","x"))
y = np.squeeze(fdtd.getdata("topdown","y"))
z = np.squeeze(fdtd.getdata("topdown","z"))
Ex = np.squeeze(fdtd.getdata("topdown","Ex"))
Ey = np.squeeze(fdtd.getdata("topdown","Ey"))
Ez = np.squeeze(fdtd.getdata("topdown","Ez"))

# Calculate the magnitude of the E-field vector and convert to dB
E = np.sqrt(pow(abs(Ex),2) + pow(abs(Ey),2) + pow(abs(Ez),2))
E_log = 20*np.log10(np.transpose(E))

# Create a color map and plot the E-field distribution
cf = plt.pcolormesh(x*1e6,y*1e6,E_log,
               shading = 'gouraud',cmap = 'jet', vmin = -50, vmax = 0)
plt.colorbar(cf)

plt.xlabel("x (um)")
plt.ylabel("y (um)")
plt.title("Top-view (xy)")

# Plot the cross section of the E-field distribution at the output
plt.figure(2)

# Get the x, y, z, Ex, Ey, and Ez components of the E-field distribution
# from the simulation
x  = np.squeeze(fdtd.getdata("transmission","x"))
y = np.squeeze(fdtd.getdata("transmission","y"))
z = np.squeeze(fdtd.getdata("transmission","z"))
Ex = np.squeeze(fdtd.getdata("transmission","Ex"))
Ey = np.squeeze(fdtd.getdata("transmission","Ey"))
Ez = np.squeeze(fdtd.getdata("transmission","Ez"))

# Calculate the magnitude of the E-field vector
E = np.sqrt(pow(abs(Ex),2) + pow(abs(Ey),2) + pow(abs(Ez),2))

# Create a color map and plot the E-field distribution
plt.pcolormesh(x*1e6,z*1e6,np.transpose(E),shading = 'gouraud',cmap = 'jet')
plt.xlabel("x (um)")
plt.ylabel("z (um)")
plt.title("Cross-section (xz)")

# Close the Lumerical FDTD session
fdtd.close()



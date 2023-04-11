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
# Imports from user files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
import sys, os 

# Add the parent directory of the current file to the system path
sys.path.append("..")

# Import user-defined parameters from another file
from user_inputs.user_simulation_parameters import *


# -------------------_----- No inputs are required ---------------------------

# Get the path of the current directory and the filename of the Lumerical file
cur_path = os.path.dirname(__file__)
filename = "waveguide_coupler.lms"
   
# Set the name of the waveguide constructor
waveguide_constructor = 'waveguide-constructor'

# Get the path of the Lumerical file
file_path = os.path.relpath('..\\user_inputs\\lumerical_files\\'+filename, cur_path)

# Open a Lumerical MODE session
mode = lumapi.MODE(file_path)



mode.run()
mode.mesh()
mode.findmodes()


neff = []
polariz_frac = []
polariz_mode = []



for m in range(1,num_modes+1):
    neff.append(mode.getdata("FDE::data::mode"+str(m),"neff"))
    polariz_frac.append(mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
    
    if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
       	polariz_mode.append("TE")
        E1 = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Ex"))
        H1 = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Hx"))
    else:
        polariz_mode.append("TM")
        E1 = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Ey"))
        H1 = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Hy"))


    x  = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"x")); 
    y= np.squeeze(mode.getdata("FDE::data::mode"+str(m),"y"));



    px = 1/plt.rcParams['figure.dpi']  # pixel in inches
    fig, ax = plt.subplots(figsize=(512*px, 256*px))
        
    im = ax.pcolormesh(x*1e6,y*1e6,np.transpose(np.real(E1)),shading = 'gouraud',cmap = 'jet')
    cbar = fig.colorbar(im)



    ax.set_xlabel("x (\u00B5m)")
    ax.set_ylabel("y (\u00B5m)")
    ax.set_title("Mode-"+str(m) + "(E-field): " + polariz_mode[m-1] + ", neff=" + str(neff[m-1]))
    
mode.close()    

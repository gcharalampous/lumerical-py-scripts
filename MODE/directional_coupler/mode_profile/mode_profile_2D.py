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
from config import *

from MODE.directional_coupler.user_inputs.user_simulation_parameters import *


# ------------------------- No inputs are required ---------------------------


def modeProfiles(mode):

    mode.findmodes()

    Ef = mode.getresult("FDE::data::mode"+str(1),"E")
    wavelength = np.squeeze(Ef['lambda'])

    neff = []
    polariz_frac = []
    polariz_mode = []
    sym_mode = [0]*(num_modes)



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
            
        sym_mode[m-1] = np.real(E1.min())
        x  = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"x")); 
        y= np.squeeze(mode.getdata("FDE::data::mode"+str(m),"y"));


        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
            
        im = ax.pcolormesh(x*1e6,y*1e6,np.transpose(np.real(E1)),shading = 'gouraud',cmap = 'jet')
        cbar = fig.colorbar(im)


        ax.set_xlabel("x (\u00B5m)")
        ax.set_ylabel("y (\u00B5m)")
        ax.set_title("Mode-"+str(m) + "(E-field): " + polariz_mode[m-1] + ", neff=" + str(neff[m-1]))
        
        file_name_plot = os.path.join(MODE_DC_DIRECTORY_WRITE[0], "mode_profile_"+str(m)+".png")
        plt.savefig(file_name_plot)

    return neff, polariz_frac, polariz_mode, sym_mode







if(__name__=="__main__"):

    with lumapi.MODE(MODE_DC_DIRECTORY_READ) as mode:

    # Run the simulation, create a mesh, and compute the modes, then save
    

        # Mode Profiles
        # Initialize empty lists to store mode properties
        neff = []           # effective index
        polariz_frac = []   # polarization fraction
        polariz_mode = []   # polarization mode (TE or TM)
        sym_mode = []       # symmetry of the mode

        # Switch to layout mode
        mode.switchtolayout()
        
        # Generate the mesh for the simulation
        mode.mesh()
        
        # Run the simulation
        mode.run()
        
        # Find the modes in the simulation
        # mode.findmodes()
        
        
        # Retrieve mode profiles and assign to respective variables
        neff, polariz_frac, polariz_mode, sym_mode = modeProfiles(mode)

    
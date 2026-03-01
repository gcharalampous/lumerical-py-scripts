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
from project_layout import setup

# Import user-defined parameters from another file
from MODE.directional_coupler.user_inputs.user_simulation_parameters import *


# -------------------_----- No inputs are required ---------------------------

def super_mode_profile(mode):





        # Get the wavelength from the simulation region
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
        
        
        
        

        return polariz_mode, sym_mode, neff, wavelength, num_modes










if(__name__=="__main__"):
    spec, out, templates = setup("mode.directional_coupler", __file__)

    with lumapi.MODE(str(templates[0])) as mode:

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
        polariz_mode, sym_mode, neff, wavelength, num_modes = super_mode_profile(mode)


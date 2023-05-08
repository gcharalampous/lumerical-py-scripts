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


# Import user-defined parameters from another file
from MODE.directional_coupler.user_inputs.user_simulation_parameters import *


# -------------------_----- No inputs are required ---------------------------

def mode_profile(file_path):

    # Open a Lumerical MODE session

    with lumapi.MODE() as mode:
        mode.load(file_path)     
        mode.switchtolayout()
        xmin  = mode.getnamed("waveguide-constructor::wg1","x min")
        xmax = mode.getnamed("waveguide-constructor::wg2","x max")
        mode.setnamed("mesh","x min",xmin)
        mode.setnamed("mesh","x max",xmax)
        print("Repositioning mesh..")
        print("xmin: " +str(xmin)+"\n"+"xmax: " + str(xmax))
        mode.run()
        mode.mesh()
        mode.findmodes()
        
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
        
        
        
        

    return polariz_mode, sym_mode, neff, wavelength, num_modes, mode


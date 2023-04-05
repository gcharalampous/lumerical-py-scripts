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
import sys 

sys.path.append("..")


from user_inputs.user_sweep_parameters import *    
from vertical_taper_plot import plot_tapers

cur_path = os.path.dirname(__file__)
filename = ["taper_waveguide_layer1.lms", "taper_waveguide_layer2.lms"]


for taper_lay in range(0,2):
    
    if(taper_lay == 0):
        width_wg_left = width_wg_left_1 
        width_wg_right = width_wg_right_1
    else:
        width_wg_left = width_wg_left_2 
        width_wg_right = width_wg_right_2
    
    
    taper_length_array = np.linspace(0,taper_length,res);
    alpha = (width_wg_left - width_wg_right)/taper_length**m;
    wg_width_array = alpha * (taper_length - taper_length_array)**m + width_wg_right;
    
    
    
    waveguide_constructor = 'waveguide-constructor'
    file_path = os.path.relpath('..\\user_inputs\\lumerical_files\\'+filename[taper_lay], cur_path)
    
    
    
    mode = lumapi.MODE(file_path)
    mode.redrawoff()
    
    
    
    structure_waveguide = waveguide_constructor + "::waveguide_core"
    neff = [0]*len(taper_length_array)
    
    # h, w = len(wg_width_array), num_modes
    # polariz_frac = [[0 for y in range(w)] for x in range(h)] 
    
    polariz_frac = [0]*num_modes
    
    
    
    mode.switchtolayout()    
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
        for m in range(1,num_modes+1):
            polariz_frac[m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
            
            if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
    
                # Do something when you find the TE Mode
                print("TE Mode " + str(m) + "\n")
                neff[wd] = (mode.getdata("FDE::data::mode"+str(m),"neff"))
                break;
    
            else:
                # Do something when you find the TM Mode
                print("TM Mode " + str(m) + "\n")
                continue;
    
    neff_real = [0]*len(neff)
    for i in range(len(neff)):
        neff_real[i] = np.real(neff[i])
        
        
    neff_real = np.squeeze(neff_real)
    
    plt.plot(taper_length_array*1e6, neff_real)
    plt.xlabel('Taper Length (um)')
    plt.ylabel('neff')
    
    dict = {'Length': taper_length_array, 'neff': neff_real}
    
    df = pd.DataFrame(dict)
    path = "data"
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
    
       # Create a new directory because it does not exist
       os.makedirs(path)
       print("The new directory is created!")
    
    df.to_csv('data\\' + filename[taper_lay][:len(filename[taper_lay])-4] + '.csv')
    mode.close()
plt.legend(['Bottom Taper','Top Taper'])
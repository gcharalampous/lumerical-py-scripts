#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts sweeps the width of the waveguide and calculates the overlap
integral for the given mode-number.
"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------
# Import necessary modules
import numpy as np
import lumapi
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import sys, os 

sys.path.append("..")
from user_inputs.gaussian_beam_parameters import *  
from gaussian_beam_render import add_gaussian_beam  


# Get current working directory
cdir = os.getcwd()
print("Current directory:", cdir)

# Change directory to a new path
os.chdir(cdir + "..\\..\\..\\waveguide")

# Get current working directory after changing
print("New current directory:", os.getcwd())


# Append parent directory to system path to import user-defined scripts
sys.path.append("..")
from waveguide_render import waveguide_draw  
from user_inputs.user_simulation_parameters import *  
from user_inputs.user_materials import *
from user_inputs.user_sweep_parameters import *    
from fde_region import add_fde_region  

# Create a MODE instance and turn off redraw feature
mode = lumapi.MODE()
mode.redrawoff()

# Draw the waveguide structure and add a finite-difference eigenmode (FDE) region
waveguide_draw(mode)
add_fde_region(mode)

# Add the Gaussian Mode on the Global Deck
add_gaussian_beam(mode)

# Create an empty list for waveguide widths and use numpy to generate a list based on user-defined parameters
wg_width_array = []
wg_width_array = np.arange(wg_width_start, wg_width_stop, wg_width_step) 

# Initialize empty 2D lists to store effective index and polarization fraction for each mode and width


polariz_frac = [0]*len(wg_width_array)
overlap_TE = [0]*len(wg_width_array)
overlap_TM = [0]*len(wg_width_array)


# Nested for loop to iterate over each waveguide width and mode - Fundamental TE
if(polarization_angle == 0):

    for wd in range(0,len(wg_width_array)):
        mode.switchtolayout()    
        mode.setnamed("waveguide","x span",wg_width_array[wd])
        mode.setnamed("mesh","x span",wg_width_array[wd])
        mode.run()
        mode.mesh()
        mode.findmodes()
        
        for m in range(1,num_modes+1):
                    polariz_frac[m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
                    
                    if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
            
                        # Do something when you find the TE Mode
                        print("TE Mode " + str(m) + "\n")
                        mode.copydcard("mode"+str(m),"mode"+str(m));
                        overlap_TE[wd] = mode.overlap("global_" + "mode"+str(m),"gaussian1");
                        mode.cleardcard("global_" +"mode"+str(m))
                        break;
            
                    else:
                        # Do something when you find the TM Mode
                        print("TM Mode " + str(m) + "\n")
                        continue;
                        
                        
                        
    
    
    
    overlap_TE_coupling = [0]*len(overlap_TE)
    overlap_TE_power = [0]*len(overlap_TE)
    
    
    
    for i in range(0,len(overlap_TE)):
        overlap_TE_coupling[i] = overlap_TE[i][0]
        overlap_TE_power[i] = overlap_TE[i][1]
        
    
    
    
    
    # Plot mode overlap integral versus waveguide width for given mode
    plt.figure(1,figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
    
    plt.plot(wg_width_array*1e6,overlap_TE_coupling,'-o', label = 'Mode Coupling')
    plt.plot(wg_width_array*1e6,overlap_TE_power,'-o', label = 'Power Coupling')
    plt.legend()
    plt.xlabel("width (um)")
    plt.ylabel("TE Mode Overlap (%)")
    plt.title("waist radius "+ str(waist_radius*1e6) + " um") 
    
    plt.legend()
    plt.xlabel("width (um)")
    plt.ylabel("TE overlap (%)")





    
# Uncomment for TM

if(polarization_angle == 90):
    
    overlap_TM_coupling = [0]*len(overlap_TM)
    overlap_TM_power = [0]*len(overlap_TM)

    
    
    
    
    # Nested for loop to iterate over each waveguide width and mode - Fundamental TM
    for wd in range(0,len(wg_width_array)):
        mode.switchtolayout()    
        mode.setnamed("waveguide","x span",wg_width_array[wd])
        mode.setnamed("mesh","x span",wg_width_array[wd])
        mode.run()
        mode.mesh()
        mode.findmodes()
        
        for m in range(1,num_modes+1):
                    polariz_frac[m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
                    
                    if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
            
                        # Do something when you find the TE Mode
                        print("TE Mode " + str(m) + "\n")
                        continue;
            
                    else:
                        # Do something when you find the TM Mode
                        print("TM Mode " + str(m) + "\n")
                        mode.copydcard("mode"+str(m),"mode"+str(m));
                        overlap_TM[wd] = mode.overlap("global_" + "mode"+str(m),"gaussian1");
                        mode.cleardcard("global_" +"mode"+str(m))
                        break;
    
        
    for i in range(0,len(overlap_TM)):
        overlap_TM_coupling[i] = overlap_TM[i][0]
        overlap_TM_power[i] = overlap_TM[i][1]
        
    
    # Plot mode overlap integral versus waveguide width for given mode
    plt.figure(2,figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
    
    plt.plot(wg_width_array*1e6,overlap_TM_coupling,'-o', label = 'Mode Coupling')
    plt.plot(wg_width_array*1e6,overlap_TM_power,'-o', label = 'Power Coupling')
    
    plt.legend()
    plt.xlabel("width (um)")
    plt.ylabel("TM Mode Overlap (%)")
    plt.title("waist radius "+ str(waist_radius*1e6) + " um") 


# Turn on redraw feature to update simulation layout
mode.redrawon()
mode.close()
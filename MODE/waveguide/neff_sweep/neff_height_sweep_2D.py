#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts sweeps the width of the waveguide and calculates the effective
index for the number of modes you defined.
"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

# Import necessary libraries and modules
import numpy as np
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup


# Import user-defined input parameters
from MODE.waveguide.user_inputs.user_sweep_parameters import *    
from MODE.waveguide.waveguide_render import *
from MODE.waveguide.fde_region import add_fde_region  

spec, out, templates = setup("mode.waveguide", __file__)

# ------------------------- No inputs are required ---------------------------



def heightSweep(mode):
    
    # Create an array to store waveguide height values for each simulation
    wg_height_array = np.arange(wg_height_start, wg_height_stop, wg_height_step) 

    # Create empty arrays to store simulation results
    h, w = len(wg_height_array), num_modes
    neff = [[0 for y in range(w)] for x in range(h)] 
    polariz_frac = [[0 for y in range(w)] for x in range(h)] 
    polariz_mode = [[0 for y in range(w)] for x in range(h)] 

    # Loop over each waveguide height value and simulate the waveguide for each height
    for wd in range(0,len(wg_height_array)):
        mode.switchtolayout()    
        mode.setnamed("waveguide","y max",wg_height_array[wd])
        mode.setnamed("mesh","y max",wg_height_array[wd])
        mode.run()
        mode.mesh()
        mode.findmodes()
        # Turn on redraw feature to update simulation layout
        mode.redrawon()
        mode.save(str(out["lumerical"] / ("waveguide_mode_height_sweep_"+str(wd) + ".lms")))

        
        for m in range(1,num_modes+1):
            # Get effective index and polarization fraction for each mode and store in corresponding 2D list
            neff[wd][m-1] = (mode.getdata("FDE::data::mode"+str(m),"neff"))
            polariz_frac[wd][m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
            
    #        if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
    #        	polariz_mode[wd][m-1] = ("TE")
    #        else:
    #            polariz_mode[wd][m-1] = ("TM")    
        
    # Squeeze the neff and TE polarization fraction arrays
    neff_array = np.squeeze(neff)
    polariz_frac_array = np.squeeze(polariz_frac)

    # Create a plot of neff vs. waveguide height for each mode
    plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
    for m in range(1,num_modes+1):
        plt.plot(wg_height_array*1e6,np.real(neff_array[:,m-1]),'-o', label = 'M-'+str(m))

    plt.legend()
    plt.grid(True, which='both')
    plt.xlabel("height (um)")
    plt.ylabel("neff")
    plt.title("width "+ str(wg_width*1e6) + " um") 
    

    # Turn on redraw feature to update simulation layout
    mode.redrawon()

    # Save the figure files as .png
    file_name_plot = str(out["figure_groups"]["Neff Sweep"] / "neff_height_sweep.png")
    plt.savefig(file_name_plot, dpi=my_dpi, format="png")

    return neff_array, wg_height_array, polariz_frac_array, polariz_mode




if(__name__=="__main__"):
    with lumapi.MODE() as mode:
        
        # Disable Rendering
        mode.redrawoff()

        # Draw the waveguide structure using a custom function
        waveguide_draw(mode)

        # Add a finite-difference eigenmode (FDE) region to the simulation environment
        add_fde_region(mode)

        # Plots effective index with widths
        wg_height_array = np.arange(wg_height_start, wg_height_stop, wg_height_step) 
        h, w = len(wg_height_array), num_modes
        neff = [[0 for y in range(w)] for x in range(h)] 
        polariz_frac = [[0 for y in range(w)] for x in range(h)] 
        wg_height_array = np.arange(wg_height_start, wg_height_stop, wg_height_step) 
        neff_array, wg_height_array, polariz_frac_array, polariz_frac_mode = heightSweep(mode=mode)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts sweeps the P-I-N clear width of the waveguide, and calculates
the propagation loss due to dopants

    ______________________________________      
   |              _______                |
   |             |       |               |
   |             |  Rib  |               |
   |_____________|_______|_______________|
   |_P++_|_________slab_____________|N++_|

         < ------------------------->
                clear Width

    

"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------
# Import necessary modules
import numpy as np
import lumapi
import matplotlib.pyplot as plt
from config import *

# Import user-defined input parameters
from MODE.waveguide.user_inputs.user_sweep_parameters import *    
from MODE.waveguide.waveguide_render import *
from MODE.waveguide.fde_region import add_fde_region  



wg_offset_N_array = np.arange(offset_P_start, offset_P_stop, offset_P_step) 
wg_offset_P_array = np.arange(offset_N_start, offset_N_stop, offset_N_step) 
clear_width = wg_offset_N_array + wg_offset_P_array


N = len(clear_width)
c = 299792458 

# Initialize empty 2D lists to store effective index and polarization fraction for each mode and width
h, w = len(wg_offset_P_array), num_modes
neff = [[0 for y in range(w)] for x in range(h)] 
polariz_frac = [[0 for y in range(w)] for x in range(h)] 
prop_loss = [[0 for y in range(w)] for x in range(h)] 

def dopingSweep(mode):
    # Create an empty list for waveguide widths and use numpy to generate a list based on user-defined parameters
    loss_TE=[]
    ng_TE = []
    ng_TM = []
    loss_TM=[]

    # Nested for loop to iterate over each waveguide width and mode
    for r in range(0,N):
        print('clear width: ',clear_width[r])


        mode.switchtolayout()
        mode.setnamed("slab_N++", "enabled", True)   
        mode.setnamed("slab_P++", "enabled", True)   
          
        mode.setnamed("slab_N++", "x min", wg_offset_N_array[r])   
        mode.setnamed("slab_P++", "x max", -wg_offset_P_array[r])   

        # Run the simulation, create a mesh, and compute the modes, then save
        mode.run()
        mode.findmodes()
        mode.redrawon()  
        mode.save(MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE + "\\waveguide_mode_doping_sweep_"+str(r) + ".lms")

        
        for m in range(1,num_modes+1):
            # Get effective index and polarization fraction for each mode and store in corresponding 2D list
            neff[r][m-1] = (mode.getdata("FDE::data::mode"+str(m),"neff"))
            polariz_frac[r][m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
            prop_loss[r][m-1] = (mode.getdata("FDE::data::mode"+str(m),"loss"))
            
            if ( polariz_frac[r][m-1] > 0.5 ):   # identify the TE-like or TM-like modes
                if(track_mode == 'TE'):
                    loss_TE.append(prop_loss[r][m-1])
                    ng_TE = (mode.getdata("FDE::data::mode"+str(m),"ng"))
                    mode.save(MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE + "\\waveguide_mode_radius_sweep_"+str(r) + ".lms")
                    break
            else:
                if(track_mode == 'TM'):
                    loss_TM.append(prop_loss[r][m-1])
                    ng_TM = (mode.getdata("FDE::data::mode"+str(m),"ng"))
                    mode.save(MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE + "\\waveguide_mode_radius_sweep_"+str(r) + ".lms")
                    break
    


    return loss_TE, loss_TM, ng_TE, ng_TM







if(__name__=="__main__"):
    with lumapi.MODE() as mode:
        
        # Disable Rendering
        mode.redrawoff()

        # Draw the waveguide structure using a custom function
        waveguide_draw(mode)

        # Add a finite-difference eigenmode (FDE) region to the simulation environment
        add_fde_region(mode)


        loss_TE, loss_TM, ng_TE, ng_TM = dopingSweep(mode=mode)
                    
        
        # Plots the loss as a function of the bend radius
        plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        plt.xlabel("clear width  (\u00B5m)")
        plt.ylabel('Excess Loss (dB/cm)')
        plt.grid(which='both')

        if(track_mode == 'TE'):    
            

            propagation_loss_TE_dB = np.squeeze(np.abs(loss_TE))          
            plt.semilogy(clear_width*1e6,propagation_loss_TE_dB*1e-2,'o-')
            plt.tight_layout()
            file_name_plot = os.path.join(MODE_WAVEGUIDE_DIRECTORY_WRITE[3], "pin_doping_offset.png")
            plt.savefig(file_name_plot)
        else:
            propagation_loss_TM_dB = np.squeeze(np.abs(loss_TM))          
            plt.semilogy(clear_width*1e6,propagation_loss_TM_dB*1e-2,'o-')
            plt.tight_layout()
            file_name_plot = os.path.join(MODE_WAVEGUIDE_DIRECTORY_WRITE[3], "pin_doping_offset.png")
            plt.savefig(file_name_plot)
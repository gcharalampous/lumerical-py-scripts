#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts sweeps the radius of the waveguide, tracks the TE or TM fundamental
modes and calculates the radiation loss, and mode missmatch
"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------
# Import necessary modules
import numpy as np
import os
import lumapi
import matplotlib.pyplot as plt
from config import *

# Import user-defined input parameters
from MODE.waveguide.user_inputs.user_sweep_parameters import *    
from MODE.waveguide.waveguide_render import *
from MODE.waveguide.fde_region import add_fde_region  



# ------------------------- You may change the FDE Boundaries below ---------------------------

wg_radius_array = np.arange(wg_radius_start, wg_radius_stop, wg_radius_step) 
# Append 0 radius at the beginning of the list
wg_radius_array = np.concatenate(([0.0], wg_radius_array))
R = wg_radius_array
N = len(wg_radius_array)
c = 299792458 

# Initialize empty 2D lists to store effective index and polarization fraction for each mode and width
h, w = len(wg_radius_array), num_modes
neff = [[0 for y in range(w)] for x in range(h)] 
polariz_frac = [[0 for y in range(w)] for x in range(h)] 
prop_loss = [[0 for y in range(w)] for x in range(h)] 

def radiusSweep(mode):
    # Create an empty list for waveguide widths and use numpy to generate a list based on user-defined parameters
    loss_TE=[]
    ng_TE = []
    ng_TM = []
    overlap_TE=[]
    overlap_TM=[]
    loss_TM=[]

    # Nested for loop to iterate over each waveguide width and mode
    for r in range(0,len(wg_radius_array)):
        mode.switchtolayout()  
        
        if(r>0):
            mode.setanalysis("bent waveguide", 1)
            mode.setanalysis("bend radius",wg_radius_array[r])
        else:
            mode.setanalysis("bent waveguide", 0)
        
        # Set the Boundaries to PML
        mode.setnamed("FDE","x max bc","PML")
        mode.setnamed("FDE","y min bc","PML")
        mode.setnamed("FDE","y max bc","PML")

    
        # Run the simulation, create a mesh, and compute the modes, then save
        mode.run()
        mode.findmodes()
        mode.redrawon()  
        mode.save(MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE + "\\waveguide_mode_radius_sweep_"+str(r) + ".lms")

        
        for m in range(1,num_modes+1):
            # Get effective index and polarization fraction for each mode and store in corresponding 2D list
            neff[r][m-1] = (mode.getdata("FDE::data::mode"+str(m),"neff"))
            polariz_frac[r][m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
            prop_loss[r][m-1] = (mode.getdata("FDE::data::mode"+str(m),"loss"))
            
            if ( polariz_frac[r][m-1] > 0.5 ):   # identify the TE-like or TM-like modes
                if(track_mode == 'TE'):
                    loss_TE.append(prop_loss[r][m-1])
                    ng_TE = (mode.getdata("FDE::data::mode"+str(m),"ng"))
                    mode.copydcard("mode"+str(m),"mode_TE"+"_radius_"+str(r));
                    mode.save(MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE + "\\waveguide_mode_radius_sweep_"+str(r) + ".lms")
                    overlap_TE.append(mode.overlap("mode_TE_radius_0","mode_TE"+"_radius_"+str(r)))
                    print(overlap_TE)
                    break
            else:
                if(track_mode == 'TM'):
                    loss_TM.append(prop_loss[r][m-1])
                    ng_TM = (mode.getdata("FDE::data::mode"+str(m),"ng"))
                    mode.copydcard("mode"+str(m),"mode_TM"+"_radius_"+str(r));
                    mode.save(MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE + "\\waveguide_mode_radius_sweep_"+str(r) + ".lms")
                    overlap_TM.append(mode.overlap("mode_TM_radius_0","mode_TM"+"_radius_"+str(r)))
                    print(overlap_TM)
                    break
    

    neff_array = np.squeeze(neff)
    polariz_frac_array = np.squeeze(polariz_frac)

    return loss_TE, loss_TM, overlap_TE, overlap_TM, ng_TE, ng_TM







if(__name__=="__main__"):
    with lumapi.MODE() as mode:
        
        # Disable Rendering
        mode.redrawoff()

        # Draw the waveguide structure using a custom function
        waveguide_draw(mode)

        # Add a finite-difference eigenmode (FDE) region to the simulation environment
        add_fde_region(mode)


        loss_TE, loss_TM, overlap_TE, overlap_TM, ng_TE, ng_TM = radiusSweep(mode=mode)
        
        # Mode Missmatch Loss
        overlap_TE_array_dB = [0]*(N)
        overlap_TM_array_dB = [0]*(N)
        
        # Propagation loss
        PropagationLoss_dB_m=PropagationLoss_dB_cm*100     # dB/cm *100 --- dB/m
        PropagationLoss_dB=PropagationLoss_dB_m*2*np.pi*R/4       # quarter turn
        
        
        
        # Plots the loss as a function of the bend radius
        plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        plt.xlabel('bend radius (um)')
        plt.ylabel('Loss/90deg (dB)')
        plt.grid(True, which='both')

        if(track_mode == 'TE'):    
            
            # Radiation Loss [dB] per quarter

            radiation_loss_TE_dB = (np.squeeze(np.abs(loss_TE)) - 
                                np.abs(loss_TE[0]))*0.5*np.pi*wg_radius_array.reshape(1,N)
            radiation_loss_TE_dB = radiation_loss_TE_dB.reshape(N)
            
            for i in range(0,len(wg_radius_array)):
                # Per Quarter Loss Missmatch
                overlap_TE_array_dB[i] = -10*np.log10(overlap_TE[i][1][0])
                
                # Total Loss
            total_loss_TE_dB = np.dot(1,overlap_TE_array_dB) + np.dot(1,radiation_loss_TE_dB) + np.dot(1,PropagationLoss_dB)
                
            plt.semilogy(wg_radius_array[1:N]*1e6,overlap_TE_array_dB[1:N],'-',label='Mode-missmatch')
            plt.semilogy(wg_radius_array[1:N]*1e6,radiation_loss_TE_dB[1:N],'-',label='Radiation Loss')
            plt.semilogy(wg_radius_array[1:N]*1e6,PropagationLoss_dB[1:N],'-',label= str(PropagationLoss_dB_cm) +' dB/cm')
            plt.semilogy(wg_radius_array[1:N]*1e6,total_loss_TE_dB[1:N],'--',label = 'Total Loss')
            plt.legend()
        else:
            
            # Radiation Loss [dB] per quarter

            radiation_loss_TM_dB = np.abs((np.squeeze(loss_TM) - 
                                loss_TM[0])*0.5*np.pi*wg_radius_array.reshape(1,N))
            radiation_loss_TM_dB = radiation_loss_TM_dB.reshape(N)
            
            for i in range(0,len(wg_radius_array)):
                # Per Quarter Loss Missmatch
                overlap_TM_array_dB[i] = -10*np.log10(overlap_TM[i][1][0])
                
                # Total Loss
            total_loss_TM_dB = np.dot(1,overlap_TM_array_dB) + np.dot(1,radiation_loss_TM_dB) + np.dot(1,PropagationLoss_dB)
                
            plt.semilogy(wg_radius_array[1:N]*1e6,overlap_TM_array_dB[1:N],'-o',label='Mode-missmatch')
            plt.semilogy(wg_radius_array[1:N]*1e6,radiation_loss_TM_dB[1:N],'-o',label='Radiation Loss')
            plt.semilogy(wg_radius_array[1:N]*1e6,PropagationLoss_dB[1:N],'-o',label='Propagation Loss')
            plt.semilogy(wg_radius_array[1:N]*1e6,total_loss_TM_dB[1:N],'--', label = 'Total Loss')
            plt.legend()
        plt.tight_layout()

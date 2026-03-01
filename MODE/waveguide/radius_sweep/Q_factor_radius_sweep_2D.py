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
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup
from MODE.waveguide.radius_sweep.overlap_radius_sweep_2D import *

spec, out, templates = setup("mode.waveguide", __file__)

# Bending Radius of the Ring
R = wg_radius_array
# Circumferance of the Ring
L = 2*np.pi*R

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
        fig, ax1 = plt.subplots(figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        ax1.grid(which='both')
        ax2 = ax1.twinx()
        ax1.set_xlabel('bend radius (um)')
        ax1.set_ylabel('intrinsic Q-factor')
        ax2.set_ylabel('FSR (THz)')
       
        # ax1.grid(True, which='both')

        if(track_mode == 'TE'):    
            
            # Radiation Loss [dB] per quarter

            radiation_loss_TE_dB = (np.squeeze(np.abs(loss_TE)) - 
                                np.abs(loss_TE[0]))*0.5*np.pi*wg_radius_array.reshape(1,N)
            radiation_loss_TE_dB = radiation_loss_TE_dB.reshape(N)
            
            for i in range(0,len(wg_radius_array)):
                # Per Quarter Loss Missmatch
                overlap_TE_array_dB[i] = -10*np.log10(overlap_TE[i][1][0])
                
                # Total Loss
            total_loss_TE_dB = np.dot(4,overlap_TE_array_dB) + np.dot(4,radiation_loss_TE_dB) + np.dot(4,PropagationLoss_dB)

            total_loss_TE = np.power(10,-total_loss_TE_dB/10)
            alpha = -(1/L[1:len(R)])*np.log(total_loss_TE[1:len(R)])
            Qi = ((2*np.pi*np.real(ng_TE))/(wavelength*alpha)).transpose()
            fsr_TE = (c/np.real(ng_TE)/L).transpose()
            
           
            ax1.semilogy(R[1:N]*1e6,Qi)
            ax2.semilogy(R[1:N]*1e6,fsr_TE[1:N]*1e-12,'r')


        else:
            
            # Radiation Loss [dB] per quarter

            radiation_loss_TM_dB = np.abs((np.squeeze(loss_TM) - 
                                loss_TM[0])*0.5*np.pi*wg_radius_array.reshape(1,N))
            radiation_loss_TM_dB = radiation_loss_TM_dB.reshape(N)
            
            for i in range(0,len(wg_radius_array)):
                # Per Quarter Loss Missmatch
                overlap_TM_array_dB[i] = -10*np.log10(overlap_TM[i][1][0])
                
                # Total Loss
            total_loss_TM_dB = np.dot(4,overlap_TM_array_dB) + np.dot(4,radiation_loss_TM_dB) + np.dot(4,PropagationLoss_dB)

            total_loss_TM = np.power(10,-total_loss_TM_dB/10)
            alpha = -(1/L[1:len(R)])*np.log(total_loss_TM[1:len(R)])
            Qi = ((2*np.pi*np.real(ng_TM))/(wavelength*alpha)).transpose()
            fsr_TM = (c/np.real(ng_TM)/L).transpose()
            
           
            ax1.semilogy(R[1:N]*1e6,Qi)
            ax2.semilogy(R[1:N]*1e6,fsr_TM[1:N]*1e-12,'r')
            
            
        plt.tight_layout()
        file_name_plot = str(out["figure_groups"]["Radius Sweep"] / "Qfactor_radius.png")
        plt.savefig(file_name_plot)
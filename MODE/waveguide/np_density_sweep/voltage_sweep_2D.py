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
"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------
# Import necessary modules
import numpy as np
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup
import pandas as pd

# Import user-defined input parameters
from MODE.waveguide.user_inputs.user_sweep_parameters import *    
from MODE.waveguide.waveguide_render import *
from MODE.waveguide.fde_region import add_fde_region  
from DEVICE.pin_modulator.user_inputs.user_sweep_parameters import v_num_pts

spec, out, templates = setup("mode.waveguide", __file__)


# ------------------------- You may change the FDE Boundaries below ---------------------------
N = v_num_pts
filename = "D:\\Georgios\\Python-Scripts\\lumerical-py-scripts\\DEVICE\\Results\\pin_modulator\\lumerical_files\\charge_sweep.mat"

c = 299792458 



# Initialize empty 2D lists to store effective index and polarization fraction for each mode and width
h, w = N, num_modes
neff = [[0 for y in range(w)] for x in range(h)] 
polariz_frac = [[0 for y in range(w)] for x in range(h)] 
prop_loss = [[0 for y in range(w)] for x in range(h)] 
V = [0]*N

def voltageSweep(mode):
    # Create an empty list for waveguide widths and use numpy to generate a list based on user-defined parameters
    loss_TE=[]
    loss_TM=[]
    neff_TE=[]
    neff_TM=[]
    # Nested for loop to iterate over each waveguide width and mode
    for r in range(0,N):
        print('V_index: ',r)


        mode.switchtolayout()  
        mode.setnamed("np density", "V_anode_index",r+1)
        Va = mode.getnamed("np density", "V_anode")
        Vc = mode.getnamed("np density", "V_cathode")
        V[r] = Va - Vc

        # Run the simulation, create a mesh, and compute the modes, then save
        mode.run()
        mode.findmodes()
        mode.redrawon()  
        mode.save(str(out["lumerical"] / ("waveguide_mode_voltage_sweep_"+str(r) + ".lms")))

        
        for m in range(1,num_modes+1):
            # Get effective index and polarization fraction for each mode and store in corresponding 2D list
            neff[r][m-1] = (mode.getdata("FDE::data::mode"+str(m),"neff"))
            polariz_frac[r][m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
            prop_loss[r][m-1] = (mode.getdata("FDE::data::mode"+str(m),"loss"))
            
            if ( polariz_frac[r][m-1] > 0.5 ):   # identify the TE-like or TM-like modes
                if(track_mode == 'TE'):
                    loss_TE.append(prop_loss[r][m-1])
                    neff_TE.append(neff[r][m-1])
                    mode.save(str(out["lumerical"] / ("waveguide_mode_radius_sweep_"+str(r) + ".lms")))
                    break
            else:
                if(track_mode == 'TM'):
                    loss_TM.append(prop_loss[r][m-1])
                    neff_TM.append(neff[r][m-1])
                    mode.save(str(out["lumerical"] / ("waveguide_mode_radius_sweep_"+str(r) + ".lms")))
                    break
    

    neff_array = (neff)
    polariz_frac_array = np.squeeze(polariz_frac)

    return loss_TE, loss_TM, neff_TE, neff_TM, V


def set_np_density_region(mode, filename):

    mode.addgridattribute("np density")
    mode.importdataset(filename)
    mode.setnamed("waveguide","material","silicon_np")
    mode.setnamed("slab","material","silicon_np")


if(__name__=="__main__"):
    with lumapi.MODE() as mode:
        
        # Disable Rendering
        mode.redrawoff()

        # Draw the waveguide structure using a custom function
        waveguide_draw(mode)
        set_np_density_region(mode,filename)
        # Add a finite-difference eigenmode (FDE) region to the simulation environment
        add_fde_region(mode)


        loss_TE, loss_TM, neff_TE, neff_TM, V = voltageSweep(mode=mode)


        abs_diff = np.abs(np.array(V) - 0)                
        index_closest = np.argmin(abs_diff)
        V_o = V[index_closest]
        indices = np.where(np.array(V) == V_o)[0]

        # Plots the loss as a function of the bend radius
        fig, ax1 = plt.subplots(figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        ax1.grid(which='both')
        ax2 = ax1.twinx()
        ax1.set_xlabel('$V_{anode} - V_{cathode}$')
        ax1.set_ylabel('$\Delta n_{eff}$')
        ax2.set_ylabel('Loss (dB/cm)')
        ax1.grid(True,which='both')
    




        if(track_mode == 'TE'):    
            ax2.plot(V, np.squeeze(loss_TE)*1e-2,'-o', color = 'r')

            Dneff_TE_V = (np.squeeze(np.real(neff_TE) - np.real(neff_TE[int(indices)])))
            ax1.plot(V, Dneff_TE_V, '-o')            

        else:
            ax2.semilogy(V, np.squeeze(loss_TM)*1e-2,'-o')



        plt.tight_layout()
        file_name_plot = str(out["figure_groups"]["Neff Sweep"] / "neff_Voltage_sweep.png")
        plt.savefig(file_name_plot, dpi=my_dpi, format="png")
        
        
        
        # Plots the loss as a function of the bend radius
        fig, ax1 = plt.subplots(figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        ax1.grid(which='both')
        ax1.set_xlabel('$V_{anode} - V_{cathode}$')
        ax1.set_ylabel('$-\Delta \phi$ (rad/mm)')
        
        
        
        if(track_mode == 'TE'):    
            dphi = 2e-3*Dneff_TE_V/wavelength
            ax1.semilogy(V, -dphi, '-o')            
            ax1.axhline(y=1, linestyle = '--', color = 'black')
            
            neff_TE = np.squeeze(neff_TE)
            loss_TE = np.squeeze(loss_TE)
        data = {'loss_TE': loss_TE,
                'neff_TE': (neff_TE),
                'V_anode': (V)
                }
        df = pd.DataFrame(data)
        


        file_name_plot = str(out["lumerical"] / "neff_Voltage_sweep_TE.csv")

        df.to_csv(file_name_plot, index=False)
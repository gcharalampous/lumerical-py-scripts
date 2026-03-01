#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The script calculates the through and bar as a function of the coupling gap
of the directional coupler.


"""

#----------------------------------------------------------------------------
# Imports from user files
# --
# Import required modules
import numpy as np
import lumapi
import matplotlib.pyplot as plt
import pandas as pd
from project_layout import setup

spec, out, templates = setup("mode.directional_coupler", __file__)

# Import user-defined parameters
from MODE.directional_coupler.user_inputs.user_sweep_parameters import *
from MODE.directional_coupler.even_odd_mode_profile import super_mode_profile
from MODE.directional_coupler.user_inputs.user_simulation_parameters import my_dpi




# --------------------------- Generate the gap array --------------------------
gap_array = np.arange(coupling_gap_start, coupling_gap_stop, coupling_gap_step)


# Initialize empty lists
nTE = [0]*2
nTM = [0]*2

# Create an array of coupling gaps to sweep over
Lx_te = [0]*len(gap_array)
Lx_tm = [0]*len(gap_array)
C_te = [0]*len(gap_array)
C_tm = [0]*len(gap_array)
file_name_mode_load = ['str']*len(gap_array)

# Set the name of the waveguide constructor as in file.
waveguide_constructor = 'waveguide-constructor'


for g in range(0,len(gap_array)):
    with lumapi.MODE(str(templates[0])) as mode:
        mode.setnamed(waveguide_constructor,"gap",gap_array[g])
        mode.save(str(out["lumerical"] / ("coupling_gap_sweep_" + str(g) + ".lms")))


# ---------------------------------------------------------------------------        
# -------------------------------- Simulations ------------------------------
      
        xmin  = mode.getnamed("waveguide-constructor::wg1","x min")
        xmax = mode.getnamed("waveguide-constructor::wg2","x max")
        mode.switchtolayout()
        mode.setnamed("mesh","x min",xmin)
        mode.setnamed("mesh","x max",xmax)
        print("Repositioning mesh..")
        print("xmin: " +str(xmin)+"\n"+"xmax: " + str(xmax))
        mode.save(str(out["lumerical"] / ("coupling_gap_sweep_" + str(g) + ".lms")))

        # Create the mesh
        mode.mesh()

        # Run the simulation
        mode.run()

        # Find the modes
        mode.findmodes()

        polariz_mode, sym_mode, neff, wavelength, num_modes = super_mode_profile(mode)

        # save the file
        mode.save(str(out["lumerical"] / ("coupling_gap_sweep_" + str(g) + ".lms")))
        mode.close()        


        # Locate the Super-mode
        for i in range(0,len(polariz_mode)-1):
            if (polariz_mode[i] == 'TE' and polariz_mode[i+1] == 'TE'):
                if(sym_mode[i] < 0 and sym_mode[i+1] >= 0 or 
                sym_mode[i] >= 0 and sym_mode[i+1] < 0):
                    print('Great, TE supermode-found')
                    nTE[0] = np.real(neff[i])
                    nTE[1] = np.real(neff[i+1])
                
            if (polariz_mode[i] == 'TM' and polariz_mode[i+1] == 'TM'):
                if(sym_mode[i] < 0 and sym_mode[i+1] >= 0 or 
                sym_mode[i] >= 0 and sym_mode[i+1] < 0):
                    print('Great, TM supermode-found')
                    nTM[0] = np.real(neff[i])
                    nTM[1] = np.real(neff[i+1])
        
        # Convert lists to numpy arrays and squeeze to remove redundant dimensions
        nTE = np.squeeze(nTE)
        nTM = np.squeeze(nTM)
        
        # Calculate the Lpi and Coupling coefficient C for TE mode
        Lx_te[g] = wavelength/((np.abs(np.real(nTE[0] - nTE[1])))*2)
        C_te[g] = ((np.abs(np.real(nTE[0] - nTE[1]))) / wavelength) * np.pi
        
        # Calculate the Lpi and Coupling coefficient C for TM mode
        Lx_tm[g] = wavelength/((np.abs(np.real(nTM[0] - nTM[1])))*2)
        C_tm[g] = ((np.abs(np.real(nTM[0] - nTM[1]))) / wavelength) * np.pi



# Squeeze the Lpi the -30dB Coupling length and Coupling coefficient C for TM mode           
Lx_tm = np.squeeze(Lx_tm)
Lx_te = np.squeeze(Lx_te)
C_te = np.squeeze(C_te)
C_tm = np.squeeze(C_tm)

# Set the figure size
px = 1 / plt.rcParams['figure.dpi']  # pixel in inches


#Lpi dB plot
plt.figure(1, figsize=(512 * px, 256 * px))
plt.semilogy(gap_array * 1e6, Lx_te * 1e6,gap_array * 1e6, Lx_tm * 1e6)
plt.grid(True,which='both')
plt.xlabel('coupling gap (um)')
plt.ylabel('$L_{\pi}$ (um)')
plt.legend(['TE','TM'])
plt.tight_layout()
# Save the plot
file_name_plot = str(out["figure_groups"]["Gap Sweep"] / "Lpi_coupling_gap_sweep_.png")
plt.savefig(file_name_plot)


#-30 dB plot
plt.figure(2, figsize=(512 * px, 256 * px))
plt.semilogy(gap_array * 1e6, 0.001*Lx_te * 1e6,gap_array * 1e6, 0.001*Lx_tm * 1e6)
plt.grid(True,which='both')
plt.xlabel('coupling gap (um)')
plt.ylabel('$L_{-30dB}$ (um)')
plt.legend(['TE','TM'])
plt.tight_layout()
# Save the plot
file_name_plot = str(out["figure_groups"]["Gap Sweep"] / "30dB_coupling_gap_sweep_.png")
plt.savefig(file_name_plot)


# Plot the Coupling Coefficient of TE and TM mode
plt.figure(3, figsize=(512 * px, 256 * px))
plt.semilogy(gap_array * 1e6, C_te * 1e-6,gap_array * 1e6, C_tm * 1e-6)
plt.grid('both')
plt.xlabel('coupling gap (um)')
plt.ylabel('Coupling Coefficient (/um)')
plt.legend(['TE','TM'])
plt.tight_layout()
# Save the plot
file_name_plot = str(out["figure_groups"]["Gap Sweep"] / "TMTE_coupling_coef_.png")
plt.savefig(file_name_plot)



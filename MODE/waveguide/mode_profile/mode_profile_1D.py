#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script calculates the 1D mode profile for the number of modes (num_modes) 
specified in 'user_simulation_parameters.py'.

The scripts calculates the effective index of each mode and plots the profile,
it also quantifies if the mode is TE or TM based on the polarization fraction.

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import shapely.geometry as sg
import shapely.ops as so
import matplotlib.pyplot as plt
from project_layout import setup


from MODE.waveguide.waveguide_render import *
from MODE.waveguide.fde_region import add_fde_region  

spec, out, templates = setup("mode.waveguide", __file__)

# ------------------------- No inputs are required ---------------------------







def modeProfiles1D():

    # Initialize empty lists to store mode properties
    neff = []           # effective index
    ng = []             # group index
    polariz_frac = []   # polarization fraction
    polariz_mode = []   # polarization mode (TE or TM)
    Ex = []             # Electric field component Ex
    Ey = []             # Electric field component Ey
    y = None            # Initialize y to ensure it is always bound
    E = None            # Initialize E to ensure it is always bound


    # Loop over each mode and extract its properties
    for m in range(1,num_modes+1):
        # Extract effective index and polarization fraction
        neff.append(mode.getdata("FDE::data::mode"+str(m),"neff"))
        ng.append(mode.getdata("FDE::data::mode"+str(m),"ng"))
        polariz_frac.append(mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
        
        # Determine if mode is TE-like or TM-like based on polarization fraction
        if ( polariz_frac[m-1] > 0.5 ):
            polariz_mode.append("TE")
            Ex.append(np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Ex")))            
        else:
            polariz_mode.append("TM")
            Ey.append(np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Ey")))

        # Extract y for each mode
        y = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"y"))


    return neff, ng, polariz_frac, polariz_mode,y, E, Ex, Ey




if(__name__=="__main__"):
    with lumapi.MODE() as mode:
        
        # Disable Rendering
        mode.redrawoff()

        # Draw the waveguide structure using a custom function
        waveguide_draw(mode)

        # Add a finite-difference eigenmode (FDE) region to the simulation environment
        add_fde_region(mode)
        
        # add 1D mode solver (horizontal waveguide cross-section)
        mode.setnamed("FDE","solver type","1D Y:Z prop")

        # Run the simulation, create a mesh, and compute the modes, then save
        mode.run()
        mode.findmodes()
        mode.save(str(out["lumerical"] / "waveguide_modes.lms"))
        
        # Turn redraw back on and close LumAPI connection
        mode.redrawon()  

        # Mode Profiles
        # Initialize empty lists to store mode properties
        neff = []           # effective index
        ng = []             # group index
        polariz_frac = []   # polarization fraction
        polariz_mode = []   # polarization mode (TE or TM)
        

        neff, ng, polariz_frac, polariz_mode, y, E, Ex, Ey = modeProfiles1D()
        
        
        
        # Extract electric field and plot
        x_=y_=0
        for m in range(1,num_modes+1):
            plt.figure(m-1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
            plt.title("Mode-"+str(m) + "(E-field): " + polariz_mode[m-1] + ", neff=" + str(np.round(neff[m-1],4)))
            plt.axhline(1/(np.exp(1)), color='red', lw=1.5, ls='--')
            plt.xlabel("y (\u00B5m)")
            plt.tight_layout()
            if ( polariz_mode[m-1] == "TE" ):
                plt.plot(y*1e6,np.transpose(Ex[x_]))
                plt.ylabel("|Ex|")
                # Find the 1/exp(1) point on the mode profile
                mfd_field=np.abs(np.transpose(max(Ex[x_]))/np.exp(1))
                mfd_index=np.argmin(np.abs(mfd_field - (Ex[x_])))
                print("Mode-"+str(m) + "(Ex): " + polariz_mode[m-1] + ", neff=" + str(np.round(neff[m-1],4)) + ", MFD: " + str(np.round((y[mfd_index]*2)*1e6,4)) + " um")
                x_ = x_ + 1
            else:                
                plt.plot(y*1e6,np.transpose(Ey[y_]))
                plt.ylabel("|Ey|")
                # Find the 1/exp(1) point on the mode profile
                mfd_field=np.abs(np.transpose(max(Ey[y_]))/np.exp(1))
                mfd_index=np.argmin(np.abs(mfd_field - (Ey[y_])))
                print("Mode-"+str(m) + "(Ey): " + polariz_mode[m-1] + ", neff=" + str(np.round(neff[m-1],4)) + ", MFD: " + str(np.round((y[mfd_index]*2)*1e6,4)) + " um")
                y_ = y_ + 1
            file_name_plot = str(out["figure_groups"]["Mode Profile"] / ("mode_profile_1D_"+str(m)+".png"))
            plt.savefig(file_name_plot)
            plt.grid()
            plt.show()

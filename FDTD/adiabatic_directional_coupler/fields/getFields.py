#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the E-fields profile for the device structure
defined in the sbend_adiabatic_directional_coupler.fsp file

"""


#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from config import *

# from FDTD.waveguide_cross.override_cross_region import *


def getFields(fdtd):
    
   
    field_xy = fdtd.getelectric("xy_topview")

    x = fdtd.getdata("xy_topview","x").squeeze()
    y = fdtd.getdata("xy_topview","y").squeeze()
    
    return x,y,field_xy






if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_ADIAB_DC_DIRECTORY_READ) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region
        # override_cross(fdtd=fdtd)
        # fdtd.run()
        
        x,y,E_xy = getFields(fdtd=fdtd)
        c_wavelength = np.rint(len(E_xy[0,0,0,:])/2)
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        
# --------------------------------Top-View---------------------------------
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6, y*1e6, (np.transpose(E_xy[:, :, 0, int(c_wavelength)])),
                     shading='gouraud', cmap='jet', norm=LogNorm(vmin=1e-4, vmax=1))
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Top-view(xy)')
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_ADIAB_DC_DIRECTORY_WRITE[2], "E_profile_xy.png")
        plt.savefig(file_name_plot)
        

        
        plt.show()
        
        
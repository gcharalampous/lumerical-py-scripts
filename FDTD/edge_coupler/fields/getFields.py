#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the E-fields profile for the device structure
defined in the edge_taper.fsp file

"""


#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
import scipy.constants as scpy
from config import *

from FDTD.edge_coupler.override_fdtd_region import override_fdtd
from FDTD.edge_coupler.override_edge_coupler_region import *


def getFields(fdtd):
    
    fdtd.run()
    
    field_xy = fdtd.getelectric("field_xy")
    field_xy = fdtd.getelectric("field_xy")

    field_xz = fdtd.getelectric("field_xz")

    x = fdtd.getdata("field_xy","x").squeeze()
    y = fdtd.getdata("field_xy","y").squeeze()
    z = fdtd.getdata("field_xz","z").squeeze()
    
    return x, y, z, field_xy, field_xz






if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_EDGE_DIRECTORY_READ) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region
        # override_taper(fdtd=fdtd)
        # override_fdtd(fdtd=fdtd)
        
        x,y,z,E_xy, E_xz = getFields(fdtd=fdtd)
        c_wavelength = np.rint(len(E_xy[0,0,0,:])/2)
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        
# --------------------------------Top-View---------------------------------
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6,y*1e6,np.transpose(E_xy[:,:,0,int(c_wavelength)]),
                             shading = 'gouraud',cmap = 'jet')
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Top-view(xy)')
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_EDGE_DIRECTORY_WRITE[2], "E_profile_xy.png")
        plt.savefig(file_name_plot)
        
# --------------------------------Side-View---------------------------------
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6,z*1e6,np.transpose(E_xz[:,0,:,int(c_wavelength)]),
                             shading = 'gouraud',cmap = 'jet')
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("z (um)")
        plt.title('Side-view(xz)')
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_EDGE_DIRECTORY_WRITE[2], "E_profile_xz.png")
        plt.savefig(file_name_plot)
        
        plt.show()
        
        
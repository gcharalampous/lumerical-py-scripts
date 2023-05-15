#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the E-fields profile for the device structure
defined in the vertical_taper.fsp file

"""


#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
import scipy.constants as scpy
from config import *

from FDTD.vertical_taper.override_fdtd_region import override_fdtd
from FDTD.vertical_taper.override_vertical_taper_region import *


def getFields(fdtd):
    
    fdtd.run()
    
    field_xy_top = fdtd.getelectric("field_xy_top")
    field_xy_bottom = fdtd.getelectric("field_xy_bottom")

    field_xz = fdtd.getelectric("field_xz")

    x = fdtd.getdata("field_xy_top","x").squeeze()
    y = fdtd.getdata("field_xy_top","y").squeeze()
    z = fdtd.getdata("field_xz","z").squeeze()
    
    return x, y, z, field_xy_top, field_xy_bottom, field_xz






if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_VERTICAL_DIRECTORY_READ) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region
        # override_vertical_taper(fdtd=fdtd)
        # override_fdtd(fdtd=fdtd)
        
        x,y,z,E_xy_top,E_xy_bottom, E_xz = getFields(fdtd=fdtd)
        c_wavelength = np.rint(len(E_xy_top[0,0,0,:])/2)
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        
# --------------------------------Top-View---------------------------------
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6,y*1e6,np.transpose(E_xy_top[:,:,0,int(c_wavelength)]),
                             shading = 'gouraud',cmap = 'jet')
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Top-view(xy) - Top taper')
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_VERTICAL_DIRECTORY_WRITE[2], "E_profile_xy_top.png")
        plt.savefig(file_name_plot)

        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6,y*1e6,np.transpose(E_xy_bottom[:,:,0,int(c_wavelength)]),
                             shading = 'gouraud',cmap = 'jet')
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Top-view(xy) - Bottom taper')
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_VERTICAL_DIRECTORY_WRITE[2], "E_profile_xy_bottom.png")
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
        file_name_plot = os.path.join(FDTD_VERTICAL_DIRECTORY_WRITE[2], "E_profile_xz.png")
        plt.savefig(file_name_plot)
        
        plt.show()
        
        
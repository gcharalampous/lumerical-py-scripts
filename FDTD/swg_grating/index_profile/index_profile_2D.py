#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the refractive index profile for the device structure
defined in the sub_wavelength_grating.fsp file

"""


#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
from config import *

from FDTD.swg_grating.override_fdtd_region import *
from FDTD.swg_grating.override_swg_region import *

# -------------------_----- No inputs are required ---------------------------


def getIndex(fdtd):

    # Get the data from the Index monitors
    index_xy = fdtd.getresult("index_xy","index")
    index_xz = fdtd.getresult("index_xz","index")
    return index_xy, index_xz


if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_SWG_DIRECTORY_READ) as fdtd:
        
        # ------------Comment for Avoiding Overriding the Simulation Region
        # override_swg(fdtd=fdtd)
        # override_fdtd(fdtd=fdtd)
        
        index_xy, index_xz = getIndex(fdtd=fdtd)




# --------------------------------Top-View---------------------------------
        x = index_xy["x"].squeeze()
        y = index_xy["y"].squeeze()
        index_x = np.real(index_xy["index_x"].squeeze())

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6, y*1e6,np.transpose(index_x))
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Top-view(xy)')
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_SWG_DIRECTORY_WRITE[0], "index_profile_xy.png")
        plt.savefig(file_name_plot)
        plt.show()

        
        
# --------------------------------Side-View---------------------------------
        xx = index_xz["x"].squeeze()
        z = index_xz["z"].squeeze()
        index_z = np.real(index_xz["index_z"].squeeze())

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6, z*1e6,np.transpose(index_z))
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("z (um)")
        plt.title('Side-view(xz)')
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_SWG_DIRECTORY_WRITE[0], "index_profile_xz.png")
        plt.savefig(file_name_plot)
        plt.show()
        
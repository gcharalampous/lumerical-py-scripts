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

from MODE.swg_grating.override_varfdtd_region import *
from MODE.swg_grating.override_swg_region import *

# -------------------_----- No inputs are required ---------------------------


def getIndex(mode):

    # Get the data from the Index monitors
    index_xy = mode.getresult("index_xy","index")
    index_xz = mode.getresult("index_xz","index")
    return index_xy, index_xz


if(__name__=="__main__"):
    with lumapi.MODE(MODE_SWG_DIRECTORY_READ) as mode:
        
        # ------------Comment for Avoiding Overriding the Simulation Region
        # override_varfdtd(mode=mode)
        # override_swg(mode=mode)
        
        index_xy, index_xz = getIndex(mode=mode)




# --------------------------------Side-View---------------------------------
        x = index_xy["x"].squeeze()
        y = index_xy["y"].squeeze()
        index_x = np.real(index_xy["index_x"].squeeze())

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6, y*1e6,np.transpose(index_x))
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Side-view(xy)')
        plt.tight_layout()
        file_name_plot = os.path.join(MODE_SWG_DIRECTORY_WRITE[0], "index_profile_xy.png")
        plt.savefig(file_name_plot)
        plt.show()

        
        
# --------------------------------Top-View---------------------------------
        xx = index_xz["x"].squeeze()
        z = index_xz["z"].squeeze()
        index_z = np.real(index_xz["index_z"].squeeze())

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6, z*1e6,np.transpose(index_z))
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("z (um)")
        plt.title('Top-view(xz)')
        plt.tight_layout()
        file_name_plot = os.path.join(MODE_SWG_DIRECTORY_WRITE[0], "index_profile_xz.png")
        plt.savefig(file_name_plot)
        plt.show()
        
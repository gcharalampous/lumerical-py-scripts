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
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup
from FDTD.swg_grating.user_inputs.user_simulation_parameters import file_index

# -------------------_----- No inputs are required ---------------------------


def getIndex(fdtd):

    # Get the data from the Index monitors
    index_xy = fdtd.getresult("index_xy","index")
    index_xz = fdtd.getresult("index_xz","index")
    return index_xy, index_xz


if(__name__=="__main__"):
    spec, out, templates = setup("fdtd.swg_grating", __file__)
    template_fsp = templates[file_index]
    figures_dir = out["figures"] / "Index Profile"
    figures_dir.mkdir(parents=True, exist_ok=True)

    with lumapi.FDTD(str(template_fsp)) as fdtd:

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
        plt.savefig(figures_dir / "index_profile_xy.png")
        plt.show()

        
        
# --------------------------------Side-View---------------------------------
        xx = index_xz["x"].squeeze()
        z = index_xz["z"].squeeze()
        index_z = np.real(index_xz["index_z"].squeeze())

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(xx*1e6, z*1e6,np.transpose(index_z))
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("z (um)")
        plt.title('Side-view(xz)')
        plt.tight_layout()
        plt.savefig(figures_dir / "index_profile_xz.png")
        plt.show()
        
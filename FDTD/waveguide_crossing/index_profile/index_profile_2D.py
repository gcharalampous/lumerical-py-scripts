#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the refractive index profile for the device structure
defined in the waveguide_crossing_multi_wg_taper.fsp file

"""


#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
from pathlib import Path
from project_layout import setup

# -------------------_----- No inputs are required ---------------------------


def getIndex(fdtd):

    # Get the data from the Index monitors
    index_xy = fdtd.getresult("index_xy","index")
    index_xz = fdtd.getresult("index_yz","index")
    return index_xy, index_xz


if(__name__=="__main__"):
    spec, out, templates = setup("fdtd.waveguide_crossing", __file__)
    template_fsp = templates[0]  # waveguide_crossing_multi_wg_taper.fsp
    figures_dir = out["figures"] / "Index Profile"
    figures_dir.mkdir(parents=True, exist_ok=True)
    
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        
        index_xy, index_yz = getIndex(fdtd=fdtd)




# --------------------------------Top-View---------------------------------
        x = index_xy["x"].squeeze()
        y = index_xy["y"].squeeze()
        index_x = np.real(index_xy["index_x"].squeeze())

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.axis('equal')
        cmap = ax.pcolormesh(x*1e6, y*1e6,np.transpose(index_x))
        fig.colorbar(cmap)
        ax.set_xlabel("x (um)")
        ax.set_ylabel("y (um)")
        ax.set_title('Top-view(xy)')
        fig.tight_layout()
        plt.savefig(figures_dir / "index_profile_xy.png")
        plt.show()

        
        
# --------------------------------Cross-View---------------------------------
        y = index_yz["y"].squeeze()
        zz = index_yz["z"].squeeze()
        index_z = np.real(index_yz["index_z"].squeeze())

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(y*1e6, zz*1e6,np.transpose(index_z))
        fig.colorbar(cmap)
        plt.xlabel("y (um)")
        plt.ylabel("z (um)")
        plt.title('Cross-view(yz)')
        plt.tight_layout()
        plt.savefig(figures_dir / "index_profile_yz.png")
        plt.show()
        
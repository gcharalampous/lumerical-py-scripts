#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the refractive index profile for the device structure
defined in the vertical_taper.fsp file

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
    index_xy_top = fdtd.getresult("index_xy_top","index")
    index_xy_bottom = fdtd.getresult("index_xy_bottom","index")
    index_xz = fdtd.getresult("index_xz","index")
    return index_xy_top, index_xy_bottom, index_xz


if(__name__=="__main__"):
    spec, out, templates = setup("fdtd.vertical_taper", __file__)
    template_fsp = templates[0]  # vertical_taper.fsp
    figures_dir = out["figures"] / "Index Profile"
    figures_dir.mkdir(parents=True, exist_ok=True)
    
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        
        
        index_xy_top, index_xy_bottom, index_xz = getIndex(fdtd=fdtd)

        x = index_xy_top["x"].squeeze()
        y = index_xy_top["y"].squeeze()
        z = index_xz["z"].squeeze()
        
        index_xy_top_X = np.real(index_xy_top["index_x"].squeeze())
        index_xy_bottom_X = np.real(index_xy_bottom["index_x"].squeeze())
        index_xz_Z = np.real(index_xz["index_z"].squeeze())

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches

# --------------------------------Top-View---------------------------------
       
        # Taper-Top
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6, y*1e6,np.transpose(index_xy_top_X))
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Top-view(xy) - Top taper')
        plt.tight_layout()
        plt.savefig(figures_dir / "top_taper_index_profile_xy.png")
        plt.show()


        # Taper-Bottom
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6, y*1e6,np.transpose(index_xy_bottom_X))
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Top-view(xy) - Bottom taper')
        plt.tight_layout()
        plt.savefig(figures_dir / "bottom_taper_index_profile_xy.png")
        plt.show()
        
        
# --------------------------------Side-View---------------------------------
        xx = index_xz["x"].squeeze()
        z = index_xz["z"].squeeze()
        index_z = np.real(index_xz["index_z"].squeeze())

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6, z*1e6,np.transpose(index_xz_Z))
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("z (um)")
        plt.title('Side-view(xz)')
        plt.tight_layout()
        plt.savefig(figures_dir / "index_profile_xz.png")
        plt.show()
        
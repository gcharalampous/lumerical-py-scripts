#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the refractive index profile for the device structure
defined in the edge_taper.fsp file

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

def get_index(fdtd):
    """Get the data from the Index monitors."""
    try:
        index_xy = fdtd.getresult("index_xy", "index")
        index_xz = fdtd.getresult("index_xz", "index")
        return index_xy, index_xz
    except Exception as e:
        print(f"Error getting index data: {e}")
        return None, None

def plot_index_profile(x, y, index_x, output_path, title, ylabel):
    """Plot the refractive index profile."""
    px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
    fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
    cmap = ax.pcolormesh(x * 1e6, y * 1e6, np.transpose(index_x))
    fig.colorbar(cmap)
    plt.xlabel("x (um)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()

if __name__ == "__main__":
    spec, out, templates = setup("fdtd.grating_coupler_rectangular_3D", __file__)
    template_fsp = templates[0]  # grating_coupler_rectangular_3D.fsp
    figures_dir = out["figures"] / "Index Profile"
    figures_dir.mkdir(parents=True, exist_ok=True)
    
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        # Comment for Avoiding Overriding the Simulation Region
        
        index_xy, index_xz = get_index(fdtd=fdtd)
        
        # --------------------------------Top-View (xy)---------------------------------
        if index_xy is not None:
            x = index_xy["x"].squeeze()
            y = index_xy["y"].squeeze()
            index_x = np.real(index_xy["index_x"].squeeze())

            output_file_path = figures_dir / "index_profile_xy.png"
            plot_index_profile(x, y, index_x, output_file_path, 'Top-view (xy)', 'y (um)')
        else:
            print("Failed to retrieve xy index data.")
        
        # --------------------------------Side-View (xz)---------------------------------
        if index_xz is not None:
            x = index_xz["x"].squeeze()
            z = index_xz["z"].squeeze()
            index_z = np.real(index_xz["index_z"].squeeze())

            output_file_path = figures_dir / "index_profile_xz.png"
            plot_index_profile(x, z, index_z, output_file_path, 'Side-view (xz)', 'z (um)')
        else:
            print("Failed to retrieve xz index data.")
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
import os
import matplotlib.pyplot as plt
from config import *

from FDTD.grating_coupler_2D.override_fdtd_region import *
from FDTD.grating_coupler_2D.override_grating_coupler_region import *

# -------------------_----- No inputs are required ---------------------------

def get_index(fdtd):
    """Get the data from the Index monitors."""
    try:
        index_data = fdtd.getresult("index_xy", "index")
        return index_data
    except Exception as e:
        print(f"Error getting index data: {e}")
        return None

def plot_index_profile(x, y, index_x, output_path):
    """Plot the refractive index profile."""
    px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
    fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
    cmap = ax.pcolormesh(x * 1e6, y * 1e6, np.transpose(index_x))
    fig.colorbar(cmap)
    plt.xlabel("x (um)")
    plt.ylabel("y (um)")
    plt.title('Side-view(xz)')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()

if __name__ == "__main__":
    with lumapi.FDTD(FDTD_GRATING_COUPLER_2D_DIRECTORY_READ) as fdtd:
        # Comment for Avoiding Overriding the Simulation Region
        override_grating_coupler(fdtd=fdtd)
        override_fdtd(fdtd=fdtd)
        
        index_data = get_index(fdtd=fdtd)
        if index_data is not None:
            x = index_data["x"].squeeze()
            y = index_data["y"].squeeze()
            index_x = np.real(index_data["index_x"].squeeze())
            index_y = np.real(index_data["index_y"].squeeze())

            output_file_path = os.path.join(FDTD_GRATING_COUPLER_2D_DIRECTORY_WRITE[0], "taper_index_profile_xy.png")
            plot_index_profile(x, y, index_x, output_file_path)
        else:
            print("Failed to retrieve index data.")
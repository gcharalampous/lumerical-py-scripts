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
from project_layout import setup

spec, out, templates = setup("fdtd.adiabatic_dc", __file__)
template_fsp = templates[0]
e_fields_dir = out["figure_groups"]["E-fields"]




def getFields(fdtd):
    """Extract electric field data from FDTD simulation.
    
    Args:
        fdtd: FDTD simulation object from lumapi.
    
    Returns:
        tuple: (x, y, field_xy) - spatial coordinates and electric field data.
    """
    field_xy = fdtd.getelectric("xy_topview")
    x = fdtd.getdata("xy_topview", "x").squeeze()
    y = fdtd.getdata("xy_topview", "y").squeeze()
    
    return x, y, field_xy






if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.run()
        
        x, y, E_xy = getFields(fdtd=fdtd)
        # Extract central wavelength index for visualization
        c_wavelength = E_xy.shape[-1] // 2
        
        # ---- Top-View (xy plane) ----
        # Figure size: 512x256 pixels
        px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        cmap = ax.pcolormesh(
            x * 1e6, y * 1e6, 
            np.transpose(E_xy[:, :, 0, int(c_wavelength)]),
            shading='gouraud', cmap='jet', 
            norm=LogNorm(vmin=1e-4, vmax=1)
        )
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Top-view (xy)')
        plt.tight_layout()
        file_name_plot = e_fields_dir / "E_profile_xy.png"
        plt.savefig(file_name_plot)
        plt.show()
        
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Extract and plot E-field profiles for the MMI coupler.

The script plots the E-fields profile for the device structure
defined in the MMI templates.

"""


#----------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from project_layout import setup
import sys
from pathlib import Path

# Import user configuration
user_inputs_dir = Path(__file__).resolve().parent.parent / "user_inputs"
sys.path.insert(0, str(user_inputs_dir))
from user_simulation_parameters import file_index

spec, out, templates = setup("fdtd.mmi_couplers", __file__)
template_fsp = templates[file_index]
figures_dir = out["figure_groups"].get("Fields", out["figures"])


def getFields(fdtd):
    
   
    field_xy = fdtd.getelectric("xy_topview")

    x = fdtd.getdata("xy_topview","x").squeeze()
    y = fdtd.getdata("xy_topview","y").squeeze()
    
    return x, y, field_xy


if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region
        fdtd.run()
        
        x, y, E_xy = getFields(fdtd=fdtd)
        c_wavelength = np.rint(len(E_xy[0,0,0,:])/2)
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        
# --------------------------------Top-View---------------------------------
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6, y*1e6, (np.transpose(E_xy[:, :, 0, int(c_wavelength)])),
                     shading='gouraud', cmap='jet', norm=LogNorm(vmin=1e-3, vmax=1))
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Top-view(xy)')
        plt.tight_layout()
        file_name_plot = figures_dir / "E_profile_xy_MMI.png"
        plt.savefig(file_name_plot)
        

        
        plt.show()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the E-fields profile for the device structure
defined in the sub_wavelength_grating.fsp file

"""


#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
import scipy.constants as scpy
from project_layout import setup

from MODE.swg_grating.override_varfdtd_region import override_varfdtd
from MODE.swg_grating.override_swg_region import *


def getFields(mode):
    
    mode.run()
    
    field_xy = mode.getelectric("field_xy")
    field_xz = mode.getelectric("field_xz")

    x = mode.getdata("field_xy","x").squeeze()
    y = mode.getdata("field_xy","y").squeeze()
    z = mode.getdata("field_xz","z")
    
    return x,y,z,field_xy, field_xz






if(__name__=="__main__"):
    spec, out, templates = setup("mode.swg_grating", __file__)
    with lumapi.MODE(str(templates[0])) as mode:
        
# ------------ Comment for Avoiding Overriding the Simulation Region
        # override_swg(mode=mode)
        # override_varfdtd(mode=mode)
        
        x,y,z,E_xy,E_xz = getFields(mode=mode)
        c_wavelength = np.rint(len(E_xy[0,0,0,:])/2)
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        
# --------------------------------Side-View---------------------------------
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6,y*1e6,np.transpose(E_xy[:,:,0,int(c_wavelength)]),
                             shading = 'gouraud',cmap = 'jet')
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Side-view(xy)')
        plt.tight_layout()
        file_name_plot = str(out["figure_groups"]["E-fields"] / "E_profile_xy.png")
        plt.savefig(file_name_plot)
        
# --------------------------------Top-View---------------------------------
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.plot(x*1e6,np.transpose(E_xz[:,0,0,int(c_wavelength)]))
        
        plt.xlabel("x (um)")
        plt.ylabel("Normalized E-field")
        plt.title('Top-view (2D)')
        plt.tight_layout()
        file_name_plot = str(out["figure_groups"]["E-fields"] / "E_profile_xz.png")
        plt.savefig(file_name_plot)
        
        plt.show()
        
        
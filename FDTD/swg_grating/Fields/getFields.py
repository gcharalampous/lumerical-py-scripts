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
from project_layout import setup
from FDTD.swg_grating.user_inputs.user_simulation_parameters import file_index


def getFields(fdtd):
    
    
    field_xy = fdtd.getelectric("field_xy")
    field_xz = fdtd.getelectric("field_xz")

    x = fdtd.getdata("field_xy","x").squeeze()
    y = fdtd.getdata("field_xy","y").squeeze()
    z = fdtd.getdata("field_xz","z").squeeze()
    
    return x,y,z,field_xy, field_xz






if(__name__=="__main__"):
    spec, out, templates = setup("fdtd.swg_grating", __file__)
    template_fsp = templates[file_index]
    figures_dir = out["figures"] / "Fields"
    figures_dir.mkdir(parents=True, exist_ok=True)

    with lumapi.FDTD(str(template_fsp)) as fdtd:

        fdtd.run()
        x,y,z,E_xy,E_xz = getFields(fdtd=fdtd)
        c_wavelength = np.rint(len(E_xy[0,0,0,:])/2)
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        
# --------------------------------Top-View---------------------------------
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6,y*1e6,np.transpose(E_xy[:,:,0,int(c_wavelength)]),
                             shading = 'gouraud',cmap = 'jet')
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Top-view(xy)')
        plt.tight_layout()
        plt.savefig(figures_dir / "E_profile_xy.png")
        
# --------------------------------Side-View---------------------------------
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6,z*1e6,np.transpose(E_xz[:,0,:,int(c_wavelength)]),
                             shading = 'gouraud',cmap = 'jet')
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("z (um)")
        plt.title('Side-view(xz)')
        plt.tight_layout()
        plt.savefig(figures_dir / "E_profile_xz.png")
        
        plt.show()
        
        
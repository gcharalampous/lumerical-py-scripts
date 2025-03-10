#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the E-fields profile for the device structure
defined in the edge_taper.fsp file

"""


#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
from config import *

# from FDTD.edge_coupler.override_fdtd_region import override_fdtd
# from FDTD.edge_coupler.override_edge_coupler_region import *



def getFieldSide(fdtd):
        
    field_xz = fdtd.getelectric("side_monitor")

    x = fdtd.getdata("side_monitor","x").squeeze()
    z = fdtd.getdata("side_monitor","z").squeeze()
    
    return x, z, field_xz

monitors = ["mesa","side_1", "side_1_1", "side_1_1_1", "side_1_1_1_1","waveguide"]

def getFieldCross(fdtd,monitors):
        field_yz = []
        z = []
        y = []
        for monitor in monitors:
                field = fdtd.getelectric(monitor)
                z.append(fdtd.getdata(monitor,"z").squeeze())
                y.append(fdtd.getdata(monitor,"y").squeeze())
                field_yz.append(field)
        
        return z, y, field_yz




if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_LASER_TAPERED_DIRECTORY_READ) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region
        # override_taper(fdtd=fdtd)
        # override_fdtd(fdtd=fdtd)
        # fdtd.r

        # Get the taper length
        mesa = fdtd.getdata("mesa","x")
        waveguide = fdtd.getdata("waveguide","x")
        taper_mesa_1 = fdtd.getnamed("mesa-constructor","taper_length_1_mesa")
        taper_mesa_2 = fdtd.getnamed("mesa-constructor","taper_length_2_mesa")
        taper_n_1 = fdtd.getnamed("mesa-constructor","taper_length_1_n")
        taper_n_2 = fdtd.getnamed("mesa-constructor","taper_length_2_n")


        x,z,E_xz = getFieldSide(fdtd=fdtd)
        zz, y, E_xy = getFieldCross(fdtd=fdtd,monitors=monitors)

        c_wavelength = np.rint(len(E_xz[0,0,0,:])/2)
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        
# --------------------------------Cross-Section---------------------------------


        for i, monitor in enumerate(monitors):
            fig, ax = plt.subplots(figsize=(512*px, 256*px))
            cmap = ax.pcolormesh(y[i]*1e6, zz[i]*1e6, np.transpose(E_xy[i][0,:,:,int(c_wavelength)]),
                                 shading='gouraud', cmap='jet')
            fig.colorbar(cmap)
            plt.xlabel("y (um)")
        #     plt.xlim(-3,3)
            plt.ylabel("z (um)")
            plt.title(f'Crosssection(yz) - Monitor {monitor}')
            plt.tight_layout()
            file_name_plot = os.path.join(FDTD_LASER_TAPERED_DIRECTORY_WRITE[2], f"E_profile_yz_{monitor}.png")
            plt.savefig(file_name_plot)
        




# --------------------------------Side-View---------------------------------
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6,z*1e6,np.transpose(E_xz[:,0,:,int(c_wavelength)]),
                             shading = 'gouraud',cmap = 'jet')
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("z (um)")
        plt.title('Side-view (xz)')
        plt.tight_layout()
        
        ax.axvline(x=mesa*1e6, color='w', linestyle='--')
        ax.axvline(x=taper_mesa_1*1e6, color='w', linestyle='--')
        ax.axvline(x=(taper_mesa_1+taper_mesa_2)*1e6, color='w', linestyle='--')
        ax.axvline(x=taper_n_1*1e6, color='w', linestyle='--')
        ax.axvline(x=(taper_n_1+taper_n_2)*1e6, color='w', linestyle='--')
        ax.axvline(x=(waveguide)*1e6, color='w', linestyle='--')
        
        
        file_name_plot = os.path.join(FDTD_LASER_TAPERED_DIRECTORY_WRITE[2], f"E_profile_xz_{monitor}.png")
        plt.savefig(file_name_plot)
        
        
        
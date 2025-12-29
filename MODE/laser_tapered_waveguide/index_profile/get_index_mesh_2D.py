#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script calculates the index mesh for the given waveguide specified in 
'user_simulation_parameters.py'.


"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
from config import *
import shapely.geometry as sg
import shapely.ops as so



# ------------------------- No inputs are required ---------------------------


def getIndex(mode):

    # Get the data from the FDE Region
    x  = np.squeeze(mode.getdata("FDE::data::material","x")); 
    y  = np.squeeze(mode.getdata("FDE::data::material","y")); 
    index_x = np.squeeze(mode.getdata("FDE::data::material","index_x"));
    index_y = np.squeeze(mode.getdata("FDE::data::material","index_y"));

    return x,y, index_x, index_y




if(__name__=="__main__"):
    with lumapi.MODE(MODE_LASER_TAPERED_DIRECTORY_READ) as mode:
        
        
        # Run the simulation, create a mesh, and compute the modes, then save
        mode.mesh()
        mode.save(MODE_LASER_TAPERED_DIRECTORY_WRITE_FILE + "\\laser_waveguide_modes.lms")

        # Turn redraw back on and close LumAPI connection
        mode.redrawon()  

 
        x, y, index_x, index_y = getIndex(mode=mode)



        # Real Index Mesh
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        plt.subplots(figsize=(512*px, 256*px))

        plt.pcolormesh(x*1e6,y*1e6,np.real(np.transpose(index_x)),shading = 'gouraud',cmap = 'jet')
        plt.colorbar()

        plt.xlabel("x (\u00B5m)")
        plt.ylabel("y (\u00B5m)")
        plt.title("Waveguide Real Index Mesh")
        plt.axis('scaled')
        plt.tight_layout()

        # Save the file
        file_name_plot = os.path.join(MODE_LASER_TAPERED_DIRECTORY_WRITE[0], "index_real_profile_2D.png")
        plt.savefig(file_name_plot)



        # Imaginary Index Mesh
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        plt.subplots(figsize=(512*px, 256*px))
        plt.pcolormesh(x*1e6,y*1e6,np.imag(np.transpose(index_x)),shading = 'gouraud',cmap = 'jet')
        plt.colorbar()

        plt.xlabel("x (\u00B5m)")
        plt.ylabel("y (\u00B5m)")
        plt.title("Waveguide Imag Index Mesh")
        plt.axis('scaled')
        plt.tight_layout()


        # Save the file
        file_name_plot = os.path.join(MODE_LASER_TAPERED_DIRECTORY_WRITE[0], "index_imag_profile_2D.png")
        plt.savefig(file_name_plot)

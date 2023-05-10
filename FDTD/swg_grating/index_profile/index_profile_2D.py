#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the refractive index profile for the device structure
defined in the sub_wavelength_grating.fsp file

"""


#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt


# -------------------_----- No inputs are required ---------------------------


def getIndex(fdtd):
# ------------------------- Directories for Results ---------------------------

    # specify the directory path
    path_to_write = ["FDTD\\Results\\swg_grating\\Figures\\index_profile"]
    directory_to_write = ['']*len(path_to_write)

    path_to_read = "FDTD\\swg_grating\\user_inputs\\lumerical_files"

    # get the current file path
    current_path = os.path.abspath(__file__)

    # get the directory of the current file
    current_dir = os.path.dirname(current_path)


    # find the project root directory by traversing up the directory 
    # tree until a specific file is found
    while not os.path.isfile(os.path.join(current_dir, ".gitignore")):
        # move up to the parent directory
        current_dir = os.path.dirname(current_dir)

    for i in range(0,len(path_to_write)):
        directory_to_write[i] = os.path.join(current_dir, path_to_write[i])

        # create the directory if it doesn't exist already
        if not os.path.exists(directory_to_write[i]):
            os.makedirs(directory_to_write[i])
            print("Directory:" + directory_to_write[i] + "\n created successfully!")
        else:
            print("Directory:" + directory_to_write[i] + "\n already exists!")



    # Search for the two template files 
    filename = ["sub_wavelength_grating.fsp"]
    directory_to_read = [str]*len(filename)
    file_directory = [str]*len(filename)
    polariz_mode_waveguide = []#[[0 for j in range(num_modes)] for i in range(len(filename))]

    for i in range(0,len(filename)):
        directory_to_read[i] = os.path.join(current_dir, path_to_read)
        file_directory[i] = os.path.join(directory_to_read[i], filename[i])

# ---------------------------------------------------------------------------
    fdtd.switchtolayout()
    fdtd.load(file_directory[0])
    index_xy = fdtd.getresult("index_xy","index")
    index_xz = fdtd.getresult("index_xz","index")
    return index_xy, index_xz, directory_to_write


if(__name__=="__main__"):
    with lumapi.FDTD() as fdtd:
        index_xy, index_xz, directory_to_write = getIndex(fdtd=fdtd)




# --------------------------------Top-View---------------------------------
        x = index_xy["x"].squeeze()
        y = index_xy["y"].squeeze()
        index_x = np.real(index_xy["index_x"].squeeze())

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6, y*1e6,np.transpose(index_x))
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Top-view(xy)')
        plt.tight_layout()
        file_name_plot = os.path.join(directory_to_write[0], "index_profile_xy.png")
        plt.savefig(file_name_plot)
        plt.show()

        
        
# --------------------------------Side-View---------------------------------
        xx = index_xz["x"].squeeze()
        z = index_xz["z"].squeeze()
        index_z = np.real(index_xz["index_z"].squeeze())

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6, z*1e6,np.transpose(index_z))
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("z (um)")
        plt.title('Side-view(xz)')
        plt.tight_layout()
        file_name_plot = os.path.join(directory_to_write[0], "index_profile_xz.png")
        plt.savefig(file_name_plot)
        plt.show()
        
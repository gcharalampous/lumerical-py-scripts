#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the transmission and reflection for the sub-wavelength
bragg grating structure defined in the sub_wavelength_grating.fsp file
from the T and R monitors

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
import scipy.constants as scpy

def getBraggResponse(fdtd):
     # specify the directory path
    path_to_write = ["FDTD\\Results\\swg_grating\\Figures\\frequency_response"]
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
    
    fdtd.load(file_directory[0])
    fdtd.run()
    T  = np.squeeze(fdtd.transmission("T"))
    R  = np.squeeze(fdtd.transmission("R"))
    f  = np.squeeze(fdtd.getdata("T","f"))

    return T, R, f, directory_to_write

if(__name__=="__main__"):
    with lumapi.FDTD() as fdtd:
        T, R, f, directory_to_write = getBraggResponse(fdtd=fdtd)


# --------------------------------Plot-T/R---------------------------------

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot((scpy.c/f)*1e6,T,label = 'Transmission')
        ax.plot((scpy.c/f)*1e6,abs(R),label = 'Reflection')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude")
        plt.ylim([0,1])
        plt.tight_layout()
        file_name_plot = os.path.join(directory_to_write[0], "frequency_response.png")
        plt.savefig(file_name_plot)        
        
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot((scpy.c/f)*1e6,10*np.log10(T),label = 'Transmission')
        ax.plot((scpy.c/f)*1e6,10*np.log10(abs(R)),label = 'Reflection')
        ax.legend()
        ax.set_xlabel("wavelength (um)")
        ax.set_ylabel("Magnitude (dB)")
        plt.tight_layout()
        file_name_plot = os.path.join(directory_to_write[0], "frequency_response_dB.png")
        plt.savefig(file_name_plot)      
        
        plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the transmission and crosstalk for the waveguide crossing
structure defined in the waveguide_crossing_multi_wg_taper.fsp file
from the 'through' and crosstalk monitor.

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
from config import *


def getCouplingResponse(fdtd):
    T  = (fdtd.getsweepresult("sweep_taper_length","T1"))
    C  = (fdtd.getsweepresult("sweep_taper_length","T2"))


    return T, C



if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_ADIAB_Y_BR_DIRECTORY_READ) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region defined in the file
        # override_fdtd(fdtd=fdtd)

# ------------ Comment for Avoiding Running Sweep 
        # fdtd.runsweep()


# Get Coupling and Through
        T, C = getCouplingResponse(fdtd=fdtd)
        length = np.squeeze(T['length'])
        through = np.squeeze(T['T'])
        bar = np.squeeze(C['T'])


# --------------------------------Plot-T/C---------------------------------

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.semilogy(length*1e6, through, label = 'Through')
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("length (um)")
        ax.set_ylabel("Magnitude")
        ax.set_title(fdtd.getnamed("source","mode selection"))
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_ADIAB_Y_BR_DIRECTORY_WRITE[1], "frequency_response_T.png")
        plt.savefig(file_name_plot)        
        
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.semilogy(length*1e6, bar,label = 'Coupling')
        ax.grid(which='both')
        ax.legend()
        ax.set_title(fdtd.getnamed("source","mode selection"))
        ax.set_xlabel("length (um)")
        ax.set_ylabel("Magnitude")
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_ADIAB_Y_BR_DIRECTORY_WRITE[1], "frequency_response_C.png")
        plt.savefig(file_name_plot)   
       



        
        plt.show()
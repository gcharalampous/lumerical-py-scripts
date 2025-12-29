#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the Through and Cross for the ring resonator coupler
as a function of gap for the structures defined in the 
["straight_ring_coupling_section.fsp",
"coocentric_ring_coupling_section.fsp",
"rectangular_ring_coupling_section"]

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
import scipy.constants as scpy
from config import *

from FDTD.ring_resonator_coupler.user_inputs.user_simulation_parameters import *

from FDTD.ring_resonator_coupler.override_fdtd_region import *
from FDTD.ring_resonator_coupler.override_ring_coupler_region import *

def getCouplingResponse(fdtd):
    T  = (fdtd.getsweepresult("sweep_straight_coupler","Through"))
    C  = (fdtd.getsweepresult("sweep_straight_coupler","Bar"))


    return T, C



if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_RING_DIRECTORY_READ[file_index]) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region defined in the file
        # override_fdtd(fdtd=fdtd)
        # override_ring_coupler(fdtd=fdtd)

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
        ax.plot(length*1e6, through, label = 'Through')
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("length (μm)")
        ax.set_ylabel("Magnitude")
        ax.set_title(fdtd.getnamed("source","mode selection"))
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_RING_DIRECTORY_WRITE[1], "frequency_response_T.png")
        plt.savefig(file_name_plot)        
        
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot(length*1e6, bar,label = 'Coupling')
        ax.grid(which='both')
        ax.legend()
        ax.set_title(fdtd.getnamed("source","mode selection"))
        ax.set_xlabel("length (μm)")
        ax.set_ylabel("Magnitude")
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_RING_DIRECTORY_WRITE[1], "frequency_response_C.png")
        plt.savefig(file_name_plot)   
       
        
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot(length*1e6, through, label='Through')
        ax.plot(length*1e6, bar, label='Coupling')
        ax.grid(which='both')
        ax.legend()
        ax.set_title(fdtd.getnamed("source","mode selection"))
        ax.set_xlabel("length (μm)")
        ax.set_ylabel("Magnitude")
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_RING_DIRECTORY_WRITE[1], "frequency_response_TC.png")
        plt.savefig(file_name_plot)   
       





        
        plt.show()
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
import scipy.constants as scpy
from config import *

from FDTD.ring_resonator_coupler.user_inputs.user_simulation_parameters import *

from FDTD.ring_resonator_coupler.override_fdtd_region import *
from FDTD.ring_resonator_coupler.override_ring_coupler_region import *

def getCouplingResponse(fdtd):
    fdtd.run()
    T  = (fdtd.getsweepresult("sweep_gap","T"))
    C  = (fdtd.getsweepresult("sweep_gap","C"))


    return T, C



if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_RING_DIRECTORY_READ[file_index]) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region defined in the file
        override_fdtd(fdtd=fdtd)
        override_ring_coupler(fdtd=fdtd)

# ------------ Comment for Avoiding Running Sweep 
        fdtd.runsweep()


# Get Coupling and Through
        T, C = getCouplingResponse(fdtd=fdtd)
        gap = np.squeeze(T['gap'])
        through = np.squeeze(T['T'])
        bar = np.squeeze(C['T'])


# --------------------------------Plot-T/C---------------------------------

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.semilogy(gap*1e9, through, label = 'Through')
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("gap (nm)")
        ax.set_ylabel("Magnitude")
        ax.set_title(fdtd.getnamed("source","mode selection"))
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_RING_DIRECTORY_WRITE[1], "frequency_response_T.png")
        plt.savefig(file_name_plot)        
        
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.semilogy(gap*1e9, bar,label = 'Coupling')
        ax.grid(which='both')
        ax.legend()
        ax.set_title(fdtd.getnamed("source","mode selection"))
        ax.set_xlabel("gap (nm)")
        ax.set_ylabel("Magnitude")
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_RING_DIRECTORY_WRITE[1], "frequency_response_C.png")
        plt.savefig(file_name_plot)   
       



        
        plt.show()
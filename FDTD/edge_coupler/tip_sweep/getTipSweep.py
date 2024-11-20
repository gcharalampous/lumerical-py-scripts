#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the transmission for the edge coupler structure defined in 
the edge_taper.fsp file from the mode expansion monitor 'T_exp'.

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
import scipy.constants as scpy
from config import *

from FDTD.edge_coupler.user_inputs.user_simulation_parameters import *

from FDTD.edge_coupler.override_fdtd_region import *
from FDTD.edge_coupler.override_edge_coupler_region import *

def getCouplingResponse(fdtd):
    T  = (fdtd.getsweepresult("sweep_tip","mode0"))



    return T


if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_EDGE_DIRECTORY_READ) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region defined in the file
        # override_fdtd(fdtd=fdtd)
        # override_taper(fdtd=fdtd)

# ------------ Comment for Avoiding Running Sweep 
        fdtd.runsweep()

# Get Coupling and Through
        T = getCouplingResponse(fdtd=fdtd)
        width_wg_left = np.squeeze(T['width_wg_left'])
        through = np.squeeze(T['T_forward'])
        gaussian_radius = fdtd.getnamed("source","waist radius w0")

# --------------------------------Plot-T/C---------------------------------

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot(width_wg_left*1e9, through, label = 'Fundamental Mode')
        ax.grid(which='major')
        ax.legend()
        ax.set_xlabel("waveguide tip (nm)")
        ax.set_ylabel("Magnitude")
        ax.set_title("Waist Radius: {:.2f} um".format(gaussian_radius*1e6))
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_EDGE_DIRECTORY_WRITE[3], "Coupling_tip_sweep.png")
        plt.savefig(file_name_plot)        
        
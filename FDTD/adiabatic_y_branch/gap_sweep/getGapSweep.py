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
        T = fdtd.getsweepresult("sweep_taper_gap", "T1")
        C = fdtd.getsweepresult("sweep_taper_gap", "T2")
               
        gap = np.squeeze(T['gap'])
        through = np.squeeze(T['T'])
        bar = np.squeeze(C['T'])
        lambda_array = np.squeeze(T['lambda'])

        if through.shape[0] > 1:
                index_array = int(np.floor(through.shape[0] / 2))
                through = abs(through[index_array])
                bar = abs(bar[index_array])
                lambda0 = lambda_array[index_array]
                print("The central wavelength is: {:.3f}".format(lambda0*1e6))
        else:
                lambda0 = lambda_array[0]
                print("The central wavelength is: {:.3f}".format(lambda0*1e6))

        
        
        
        
        return through, bar, gap, lambda0



if(__name__=="__main__"):
    with lumapi.FDTD(FDTD_ADIAB_Y_BR_DIRECTORY_READ) as fdtd:
        
# ------------ Comment for Avoiding Overriding the Simulation Region defined in the file
        # override_fdtd(fdtd=fdtd)

# ------------ Comment for Avoiding Running Sweep 
        # fdtd.runsweep()


# Get Coupling and Through
        through, bar, gap, lambda0 = getCouplingResponse(fdtd=fdtd)
        


# --------------------------------Plot-T/C---------------------------------

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot(gap*1e9, through, label = 'Through')
        ax.plot(gap*1e9, bar, label = 'Bar')
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("gap (nm)")
        ax.set_ylabel("Magnitude")
        ax.set_title("wavelength [μm] = {:.3f}".format(lambda0*1e6))
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_ADIAB_Y_BR_DIRECTORY_WRITE[0], "gap_sweep_linear.png")
        plt.savefig(file_name_plot)        
        
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        ax.plot(gap*1e9, 10 * np.log10(through), label = 'Through')
        ax.plot(gap*1e9, 10 * np.log10(bar), label = 'Bar')
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("gap (nm)")
        ax.set_ylabel("Magnitude")
        ax.set_title("wavelength [μm] = {:.3f}".format(lambda0*1e6))
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_ADIAB_Y_BR_DIRECTORY_WRITE[0], "gap_sweep_log.png")
        plt.savefig(file_name_plot)        
        

        
        plt.show()
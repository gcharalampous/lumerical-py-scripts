#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts calculates the effective index variations of the width based on 
the number of modes you defined. 

You need to run the neef_width_sweep_2D.pyto calculate the effective index 
vs width.
"""


#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# Import user-defined input parameters
from MODE.waveguide.user_inputs.user_sweep_parameters import *    
from MODE.waveguide.waveguide_render import *

# Runs the module to calculate the neff vs height
from MODE.waveguide.neff_sweep.neff_width_sweep_2D import *




# Plots the effective index width variations as a function of width
if(__name__=="__main__"):
    with lumapi.MODE() as mode:
        
        # Disable Rendering
        mode.redrawoff()

        # Draw the waveguide structure using a custom function
        waveguide_draw(mode)

        # Add a finite-difference eigenmode (FDE) region to the simulation environment
        add_fde_region(mode)


        neff_array, wg_width_array, polariz_frac, polariz_mode = widthSweep(mode=mode)
        

        # Plots effective index with widths
        plt.figure(2, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)

        for m in range(1,num_modes+1):

            # Calculates the derivative    
            dneffdwidth = np.gradient(neff_array[:,m-1], wg_width_array)
            plt.semilogy(wg_width_array*1e6,np.real(dneffdwidth)*1e-9,'-o', label = 'M-'+str(m))

        plt.legend()
        plt.ylim([1e-6,1e-2])
        plt.xlabel("waveguide width (um)")
        plt.ylabel('$d(n_{eff})/d(w)\quad (nm^{-1})$')
        plt.title("thickness "+ str(wg_thickness*1e6) + " um") 

        # Save the figure files as .png

        file_name_plot = os.path.join(MODE_WAVEGUIDE_DIRECTORY_WRITE[2], "neff_width_sweep_variations.png")
        plt.grid(True, which='both')
        plt.tight_layout()
        plt.savefig(file_name_plot, dpi=my_dpi, format="png")
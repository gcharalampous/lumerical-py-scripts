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

# Import user-defined input parameters
from MODE.waveguide.user_inputs.user_sweep_parameters import *    
from MODE.waveguide.waveguide_render import *

# Runs the module to calculate the neff vs height
from neff_height_sweep_2D import *


# Plots the effective index width variations as a function of heigt

plt.figure(2,figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)

for m in range(1,num_modes+1):

    # Calculates the derivative    
    dneffdwidth = np.gradient(neff_array[:,m-1], wg_height_array)
    plt.semilogy(wg_height_array*1e6,np.real(dneffdwidth)*1e-9,'-o', label = 'M-'+str(m))

plt.legend()
plt.ylim([1e-5,1e-2])
plt.xlabel("height (um)")
plt.ylabel('$\partial(n_{eff})/\partial(h)\quad (nm^{-1})$')
plt.title("width "+ str(wg_width*1e6) + " um") 
plt.grid(True, which='both')

# Save the figure files as .png
file_name_plot = os.path.join(directory_to_write[0], "neff_height_sweep_variations" + ".png")
plt.tight_layout()
plt.savefig(file_name_plot, dpi=my_dpi, format="png")
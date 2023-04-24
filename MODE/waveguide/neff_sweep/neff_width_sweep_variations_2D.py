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
from neff_width_sweep_2D import *




# Plots the effective index width variations as a function of width



plt.figure(m-1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)

for m in range(1,num_modes+1):

    # Calculates the derivative    
    dneffdwidth = np.gradient(neff_array[:,m-1], wg_width_array)
    plt.semilogy(wg_width_array*1e6,np.real(dneffdwidth)*1e-9,'-o', label = 'M-'+str(m))

plt.legend()
plt.xlabel("width (um)")
plt.ylabel('$d(n_{eff})/d(w)\quad (nm^{-1})$')
plt.title("thickness "+ str(wg_thickness*1e6) + " um") 

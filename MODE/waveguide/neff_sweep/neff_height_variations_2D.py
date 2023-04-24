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
import sys 

sys.path.append("..")

from waveguide_render import waveguide_draw  
from user_inputs.user_simulation_parameters import *  
from user_inputs.user_materials import *
from user_inputs.user_sweep_parameters import *    
from fde_region import add_fde_region  
from neff_height_sweep_2D import *





plt.figure(m-1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)

for m in range(1,num_modes+1):
    
    dneffdwidth = np.gradient(neff_array[:,m-1], wg_height_array)
    

    plt.semilogy(wg_height_array*1e6,dneffdwidth*1e-9,'-o', label = 'M-'+str(m))

plt.legend()
plt.xlabel("height (um)")
plt.ylabel('$\partial(n_{eff})/\partial(h)\quad (nm^{-1})$')
plt.title("width "+ str(wg_width*1e6) + " um") 
plt.show()    

mode.close()
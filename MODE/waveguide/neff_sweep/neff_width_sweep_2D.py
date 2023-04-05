#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts sweeps the width of the waveguide and calculates the effective
index for the number of modes you defined.
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


mode = lumapi.MODE()

mode.redrawoff()


waveguide_draw(mode)
add_fde_region(mode)


wg_width_array = []
wg_width_array = np.arange(wg_width_start, wg_width_stop, wg_width_step) 




h, w = len(wg_width_array), num_modes
neff = [[0 for y in range(w)] for x in range(h)] 

h, w = len(wg_width_array), num_modes
polariz_frac = [[0 for y in range(w)] for x in range(h)] 

h, w = len(wg_width_array), num_modes
polariz_mode = [[0 for y in range(w)] for x in range(h)] 





for wd in range(0,len(wg_width_array)):
    mode.switchtolayout()    
    mode.setnamed("waveguide","x span",wg_width_array[wd])
    mode.setnamed("mesh","x span",wg_width_array[wd])
    mode.run()
    mode.mesh()
    mode.findmodes()
    
    for m in range(1,num_modes+1):
        neff[wd][m-1] = (mode.getdata("FDE::data::mode"+str(m),"neff"))
        polariz_frac[wd][m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
        
#        if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
#        	polariz_mode[wd][m-1] = ("TE")
#        else:
#            polariz_mode[wd][m-1] = ("TM")    
    
neff_array = np.squeeze(neff)
polariz_frac_array = np.squeeze(polariz_frac)

plt.figure(m-1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
for m in range(1,num_modes+1):
    plt.plot(wg_width_array*1e6,neff_array[:,m-1],'-o', label = 'M-'+str(m))

plt.legend(loc = "upper left")
plt.xlabel("width (um)")
plt.ylabel("neff")
plt.title("thickness "+ str(wg_thickness*1e6) + " um") 
plt.axhline(y=sub_index, linewidth=1, label= 'Si-index')   
plt.show()    

mode.redrawon()

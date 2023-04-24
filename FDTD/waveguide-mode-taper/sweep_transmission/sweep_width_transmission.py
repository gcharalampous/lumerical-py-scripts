#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts sweeps the width of the waveguide and calculates the transmission
of the fundamental mode.
"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------


import numpy as np
import lumapi
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import sys 
import time
sys.path.append("..")

from waveguide_taper_render import waveguide_taper_draw  
from user_inputs.user_simulation_parameters import *  
from user_inputs.user_materials import *
from user_inputs.user_sweep_parameters import *    
from fdtd_region import add_fdtd_region


fdtd = lumapi.FDTD()


wav = ((wavelength_start + wavelength_stop)/2)*1e6
fdtd.save(str(round(wav,2)) + "nm_straight_waveguide_width_sweep" + "_thick_" + str(round(wg_thickness*1e6,2)))


waveguide_taper_draw(fdtd)
add_fdtd_region(fdtd)

fdtd.redrawoff()

wg_width_array = []
wg_width_array = np.arange(wg_width_start, wg_width_stop, wg_width_step) 


trans_f=[]
trans_t=[]

# Sweeps through the waveguide widths, and calculates the transmission

for wd in range(0,len(wg_width_array)):
    fdtd.switchtolayout()    
    fdtd.redrawoff()
    
    wg_width_left = wg_width_array[wd]
    fdtd.setnamed("waveguide_left","y span",wg_width_left)
      
    alpha = (wg_width_left - wg_width_right)/pow(taper_length,m);
    xspan = np.linspace(0, taper_length, poly_res);
    yspan = alpha * pow((taper_length - xspan),m) + wg_width_right;

    V = np.zeros((2*poly_res,2))

    for x in range(0,len(xspan)):
        V[x][0] = xspan[x]
        V[x][1] = -yspan[x]/2
        
    xspan_r = np.flip(xspan, axis=0)
    yspan_r = np.flip(yspan, axis=0)
    
    for x in range(len(xspan),2*len(xspan)):
        V[x][0] = xspan_r[x-len(xspan)]
        V[x][1] = yspan_r[x-len(xspan)]/2

    fdtd.setnamed("taper","vertices",V)

    #time.sleep(5)
    fdtd.run()
    trans_f.append(fdtd.getresult("monitor_exp","expansion for input").get("T_forward"))
    trans_t.append(fdtd.getresult("monitor_exp","expansion for input").get("T_total"))
    
    

trans_f_array = np.squeeze(trans_f)   
trans_t_array = np.squeeze(trans_t)

plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
plt.plot(wg_width_array*1e6,trans_f_array,'-o',wg_width_array*1e6,trans_t_array,'-o')

plt.xlabel("width (um)")
plt.ylabel("T")
plt.title("thickness "+ str(wg_thickness*1e6) + " um") 
plt.show()    

fdtd.redrawon()





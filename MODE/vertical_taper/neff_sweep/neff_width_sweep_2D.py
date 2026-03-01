#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts sweeps the width of the waveguide and calculates the effective
index for the TE Mode.

if you prefer calculating the effective index of the TM mode, modify the
lines between 86 and 100.
"""

#----------------------------------------------------------------------------
# Imports from user files
# --

import numpy as np
import lumapi
import matplotlib.pyplot as plt

from MODE.vertical_taper.user_inputs.user_sweep_parameters import num_modes, res, m, taper_length, width_wg_left_1, width_wg_right_1, width_wg_left_2, width_wg_right_2, my_dpi
from project_layout import setup

spec, out, templates = setup("mode.vertical_taper", __file__)
lumerical_dir = out["lumerical"] / "sweep_width"
lumerical_dir.mkdir(parents=True, exist_ok=True)
figures_dir = out["figure_groups"]["Neff Sweep"]
figures_dir.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------



# ---------------------------- Start Sweeping --------------------------------
taper_length_array = np.linspace(0,taper_length,res)



w, h = 2, len(taper_length_array)
neff = [[0 for x in range(w)] for y in range(h)] 
neff_wg1 = [0]*len(taper_length_array)
neff_wg2 = [0]*len(taper_length_array)



for i in range(0,len(templates)):
    
    if(i == 0):
        width_wg_left = width_wg_left_1 
        width_wg_right = width_wg_right_1
    else:
        width_wg_left = width_wg_left_2 
        width_wg_right = width_wg_right_2
    
    
    alpha = (width_wg_left - width_wg_right)/taper_length**m;
    wg_width_array = alpha * (taper_length - taper_length_array)**m + width_wg_right;
    
    
    waveguide_constructor = 'waveguide-constructor'
    
    file_name_mode = str(templates[i])
    
    
    with lumapi.MODE() as mode:
        mode.load(file_name_mode)
        mode.switchtolayout()
        mode.redrawoff()

        
        
        structure_waveguide = waveguide_constructor + "::waveguide_core"
        
        
        
        polariz_frac = [0]*num_modes
        
        
        
        mode.setnamed("FDE","number of trial modes",num_modes)
        
        
        for wd in range(0,len(wg_width_array)):
            print("Loop: " + str(wd))
            mode.switchtolayout()    
            mode.setnamed(waveguide_constructor,"width",wg_width_array[wd])
            mode.setnamed("mesh_waveguide","x span",wg_width_array[wd])
            mode.mesh()
            mode.run()
            mode.findmodes()
            file_name_mode_writing = str(lumerical_dir / f"waveguide_{i+1}_width_sweep_{wd}.lms")
            mode.save(file_name_mode_writing)            
            for m in range(1,num_modes+1):
                polariz_frac[m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
                
                if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
        
                    # Do something when you find the TE Mode
                    print("TE Mode " + str(m) + "\n")
                    neff[wd][i] = (mode.getdata("FDE::data::mode"+str(m),"neff"))
                    break;
        
                else:
                    # Do something when you find the TM Mode
                    print("TM Mode " + str(m) + "\n")
                    continue;
        
# ---------------------------------------------------------------------------

# ---------------------------- Plot/Save Results - ---------------------------


# Get the data from the neff lists and prepare for the plot
for n in range(0,len(neff)):
    neff_wg1[n] = np.real(neff[n][0])
    neff_wg2[n] = np.real(neff[n][1])

neff_wg1=np.squeeze(neff_wg1)
neff_wg2=np.squeeze(neff_wg2)
    
plt.figure(figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)

plt.plot(taper_length_array*1e6, neff_wg1,label = 'taper-1')
plt.plot(taper_length_array*1e6, neff_wg2,label = 'taper-2')


plt.xlabel('Taper Length (um)')
plt.ylabel('neff')
plt.legend()

# Save the figure files as .png     
file_name_plot = str(figures_dir / "neff_sweep_width.png")
plt.tight_layout()
plt.savefig(file_name_plot, dpi=my_dpi, format="png")




# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 23:23:56 2022

@author: Georgios
"""
import numpy as np
import lumapi
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import sys 

sys.path.append("..")

from waveguide_render import waveguide_draw  
from user_inputs.user_simulation_parameters import *  
from user_inputs.user_materials import *  
from fde_region import add_fde_region  




mode = lumapi.MODE()
mode.redrawoff()

waveguide_draw(mode)
add_fde_region(mode)

mode.run()
mode.mesh()
mode.findmodes()


neff = []
polariz_frac = []
polariz_mode = []
for m in range(1,num_modes+1):
    neff.append(mode.getdata("FDE::data::mode"+str(m),"neff"))
    polariz_frac.append(mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
    
    if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
    	polariz_mode.append("TE")
    else:
        polariz_mode.append("TM")

    plt.figure(m-1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
    x  = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"x")); 
    y= np.squeeze(mode.getdata("FDE::data::mode"+str(m),"y"));
    
    E1 = np.squeeze(mode.getelectric("FDE::data::mode"+str(m)))
    H1 = np.squeeze(mode.getmagnetic("FDE::data::mode"+str(m)))
    
    rect = Rectangle((-(wg_width/2)*1e6, -(wg_thickness/2)*1e6),(wg_width)*1e6, wg_thickness*1e6, color='black', fill = False)
    plt.gca().add_patch(rect)
    plt.pcolormesh(x*1e6,y*1e6,np.transpose(E1),shading = 'gouraud',cmap = 'plasma')
    plt.xlabel("x (\u00B5m)")
    plt.ylabel("y (\u00B5m)")
    plt.title("Mode-"+str(m) + "(E-field): " + polariz_mode[m-1] + ", neff=" + str(neff[m-1]))
    
mode.redrawon()  
    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script calculates the mode profile for the mode specified in the
'user_simulation_parameters.py'.

The scripts calculates a slice of the E-field along the y-direction and x-
direction. Additionally, the 2D E-field distributions for the top-view,
side-view and cross-section of the waveguide.

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

from matplotlib.patches import Polygon
from waveguide_taper_render import waveguide_taper_draw  
from user_inputs.user_simulation_parameters import *  
from user_inputs.user_materials import *
from user_inputs.user_sweep_parameters import *    
from fdtd_region import add_fdtd_region

fdtd = lumapi.FDTD()
fdtd.redrawoff()

V = waveguide_taper_draw(fdtd)
add_fdtd_region(fdtd)



wav = ((wavelength_start + wavelength_stop)/2)*1e6
fdtd.save(str(round(wav,2)) + "taper_" + str(round(wg_width_left*1e6,2)) 
          + "_to_" + str(round(wg_width_right*1e6,2)) + "_length_" 
          + str(round(taper_length*1e6,2)) + "um")

fdtd.run()
fdtd.redrawon()




# Plot (Linear - Y)
y = np.squeeze(fdtd.getdata("linear_y","y"))
Ex = np.squeeze(fdtd.getdata("linear_y","Ex"))
Ey = np.squeeze(fdtd.getdata("linear_y","Ey"))
Ez = np.squeeze(fdtd.getdata("linear_y","Ez"))
E = np.sqrt(pow(abs(Ex),2) + pow(abs(Ey),2) + pow(abs(Ez),2))
plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
plt.plot(y*1e6,E)
plt.xlabel("y (\u00B5m)")
plt.ylabel("E$_y$")
plt.title("Mode profile, w_o"  )



# Plot (Linear - Z)
z = np.squeeze(fdtd.getdata("linear_z","z"))
Ex = np.squeeze(fdtd.getdata("linear_z","Ex"))
Ey = np.squeeze(fdtd.getdata("linear_z","Ey"))
Ez = np.squeeze(fdtd.getdata("linear_z","Ez"))
E = np.sqrt(pow(abs(Ex),2) + pow(abs(Ey),2) + pow(abs(Ez),2))
plt.figure(2, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
plt.plot(z*1e6,E)
plt.xlabel("z (\u00B5m)")
plt.ylabel("E$_z$")
plt.title("Mode profile, w_o"  )



# Plot (Top-view - xy)
x  = np.squeeze(fdtd.getdata("2D_xy","x"))
y = np.squeeze(fdtd.getdata("2D_xy","y"))
z = np.squeeze(fdtd.getdata("2D_xy","z"))
Ex = np.squeeze(fdtd.getdata("2D_xy","Ex"))
Ey = np.squeeze(fdtd.getdata("2D_xy","Ey"))
Ez = np.squeeze(fdtd.getdata("2D_xy","Ez"))
E = np.sqrt(pow(abs(Ex),2) + pow(abs(Ey),2) + pow(abs(Ez),2))

plt.figure(3, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
polygon_v = Polygon(V*1e6, color='black', fill = False)
plt.gca().add_patch(polygon_v)
rect = Rectangle((-offset_x/2*1e6, (-wg_width_left/2)*1e6),(offset_x/2)*1e6, (wg_width_left)*1e6, color='black', fill = False)
plt.gca().add_patch(rect)
rect = Rectangle((taper_length*1e6, (-wg_width_right/2)*1e6),(offset_x)*1e6, (wg_width_right)*1e6, color='black', fill = False)
plt.gca().add_patch(rect)

plt.pcolormesh(x*1e6,y*1e6,np.transpose(E),shading = 'gouraud',cmap = 'jet')
plt.xlabel("x (\u00B5m)")
plt.ylabel("y (\u00B5m)")
plt.title("Top-view (xy)")



# Plot (Side-view - xz)
x  = np.squeeze(fdtd.getdata("2D_xz","x"))
y = np.squeeze(fdtd.getdata("2D_xz","y"))
z = np.squeeze(fdtd.getdata("2D_xz","z"))
Ex = np.squeeze(fdtd.getdata("2D_xz","Ex"))
Ey = np.squeeze(fdtd.getdata("2D_xz","Ey"))
Ez = np.squeeze(fdtd.getdata("2D_xz","Ez"))
Ez = np.squeeze(fdtd.getdata("2D_xz","Ez"))
E = np.sqrt(pow(abs(Ex),2) + pow(abs(Ey),2) + pow(abs(Ez),2))

plt.figure(4, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
rect = Rectangle((-offset_x*1e6, 0),(simulation_span_x + offset_x)*1e6, wg_thickness*1e6, color='black', fill = False)
plt.gca().add_patch(rect)
plt.pcolormesh(x*1e6,z*1e6,np.transpose(E),shading = 'gouraud',cmap = 'jet')
plt.xlabel("x (\u00B5m)")
plt.ylabel("z (\u00B5m)")
plt.title("Side-view (xz)")



# Plot (Cross section - yz)
x  = np.squeeze(fdtd.getdata("transmission","x"))
y = np.squeeze(fdtd.getdata("transmission","y"))
z = np.squeeze(fdtd.getdata("transmission","z"))
Ex = np.squeeze(fdtd.getdata("transmission","Ex"))
Ey = np.squeeze(fdtd.getdata("transmission","Ey"))
Ez = np.squeeze(fdtd.getdata("transmission","Ez"))
Ez = np.squeeze(fdtd.getdata("transmission","Ez"))
E = np.sqrt(pow(abs(Ex),2) + pow(abs(Ey),2) + pow(abs(Ez),2))

plt.figure(5, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
rect = Rectangle((-(wg_width_left/2)*1e6, 0),(wg_width_left)*1e6, wg_thickness*1e6, color='black', fill = False)
plt.gca().add_patch(rect)
plt.pcolormesh(y*1e6,z*1e6,np.transpose(E),shading = 'gouraud',cmap = 'jet')
plt.xlabel("y (\u00B5m)")
plt.ylabel("z (\u00B5m)")
plt.title("Cross-section (yz)")


# Print Transmission
print("--- Transmission Results ---" + "\n")
trans_f = (fdtd.getresult("monitor_exp","expansion for input").get("T_forward"))
trans_t = (fdtd.getresult("monitor_exp","expansion for input").get("T_total"))
print("Total Trans: " + str(round(trans_t[0][0],3)))
print("Forward Trans: " + str(round(trans_f[0][0],3)))
    
fdtd.close()

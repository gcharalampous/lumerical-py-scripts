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
import lumapi, os
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle
from config import *
from FDTD.waveguide_mode_taper.waveguide_taper_render import waveguide_taper_draw
from FDTD.waveguide_mode_taper.user_inputs.user_simulation_parameters import *  
from FDTD.waveguide_mode_taper.user_inputs.user_materials import *
from FDTD.waveguide_mode_taper.user_inputs.user_sweep_parameters import *    
from FDTD.waveguide_mode_taper.fdtd_region import add_fdtd_region





def getLinearFields(fdtd):
    
    fdtd.run()
    
    # Monitor (Linear - Y)
    y = np.squeeze(fdtd.getdata("linear_y","y"))
    Ex_ylinear = np.squeeze(fdtd.getdata("linear_y","Ex"))
    Ey_ylinear = np.squeeze(fdtd.getdata("linear_y","Ey"))
    Ez_ylinear = np.squeeze(fdtd.getdata("linear_y","Ez"))
    E2_ylinear = np.sqrt(pow(abs(Ex_ylinear),2) + pow(abs(Ey_ylinear),2) 
                         + pow(abs(Ez_ylinear),2))
        
        
    # Plot (Linear - Z)
    z = np.squeeze(fdtd.getdata("linear_z","z"))
    Ex_zlinear = np.squeeze(fdtd.getdata("linear_z","Ex"))
    Ey_zlinear = np.squeeze(fdtd.getdata("linear_z","Ey"))
    Ez_zlinear = np.squeeze(fdtd.getdata("linear_z","Ez"))
    E2_zlinear = np.sqrt(pow(abs(Ex_zlinear),2) + pow(abs(Ey_zlinear),2) 
                         + pow(abs(Ez_zlinear),2))
        
    return y, E2_ylinear, z, E2_zlinear


def get2DFields(fdtd):

    # Plot (Top-view - xy)
    x  = np.squeeze(fdtd.getdata("2D_xy","x"))
    y = np.squeeze(fdtd.getdata("2D_xy","y"))
    z = np.squeeze(fdtd.getdata("2D_xz","z"))
    Ex = np.squeeze(fdtd.getdata("2D_xy","Ex"))
    Ey = np.squeeze(fdtd.getdata("2D_xy","Ey"))
    Ez = np.squeeze(fdtd.getdata("2D_xy","Ez"))
    E2_topdown = np.sqrt(pow(abs(Ex),2) + pow(abs(Ey),2) + pow(abs(Ez),2))
    
    
    # Plot (Side-view - xz)
    Ex = np.squeeze(fdtd.getdata("2D_xz","Ex"))
    Ey = np.squeeze(fdtd.getdata("2D_xz","Ey"))
    Ez = np.squeeze(fdtd.getdata("2D_xz","Ez"))
    E2_sideview = np.sqrt(pow(abs(Ex),2) + pow(abs(Ey),2) + pow(abs(Ez),2))
    
    # Plot (Cross section - yz)
    Ex = np.squeeze(fdtd.getdata("transmission","Ex"))
    Ey = np.squeeze(fdtd.getdata("transmission","Ey"))
    Ez = np.squeeze(fdtd.getdata("transmission","Ez"))
    E2_crossection = np.sqrt(pow(abs(Ex),2) + pow(abs(Ey),2) + pow(abs(Ez),2))

    # Print Transmission
    print("--- Transmission Results ---" + "\n")
    trans_f = (fdtd.getresult("monitor_exp","expansion for input").get("T_forward"))
    trans_t = (fdtd.getresult("monitor_exp","expansion for input").get("T_total"))
    print("Total Trans: " + str(round(trans_t[0][0],3)))
    print("Forward Trans: " + str(round(trans_f[0][0],3)))



    return x, y, z, E2_topdown, E2_sideview, E2_crossection



    
if(__name__=="__main__"):
    
    with lumapi.FDTD() as fdtd:
        


        V = waveguide_taper_draw(fdtd,taper_length,wg_width_right)
        add_fdtd_region(fdtd,taper_length)
        
        
        fdtd.save(os.path.join(FDTD_WGTAPER_DIRECTORY_WRITE_FILE, 
                               FDTD_WGTAPER_FILENAME))
        
        fdtd.run()
        
        
        y, E2_ylinear, z, E2_zlinear = getLinearFields(fdtd=fdtd)
        
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches       
        fig, (ax1, ax2) = plt.subplots(2,1)
        

        ax1.plot(y*1e6,E2_ylinear)
        ax1.set_xlabel("y (\u00B5m)")
        ax1.set_ylabel("E$_y$")
        
        ax2.plot(z*1e6,E2_zlinear)
        ax2.set_xlabel("z (\u00B5m)")
        ax2.set_ylabel("E$_z$")
       
        
        fig.tight_layout()

        file_name_plot = os.path.join(FDTD_WGTAPER_DIRECTORY_WRITE[2], "E_profile_linear.png")
        plt.savefig(file_name_plot)




        x, y, z, E2_topdown, E2_sideview, E2_crossection = get2DFields(fdtd=fdtd)

        

# --------------------------------Top-View---------------------------------
        fig, ax = plt.subplots(figsize=(512*px, 256*px))

        cmap = ax.pcolormesh(x*1e6,y*1e6,np.transpose(E2_topdown),shading = 'gouraud',cmap = 'jet')

        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title('Top-view(xy)')
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_WGTAPER_DIRECTORY_WRITE[2], "E_profile_xy.png")
        plt.savefig(file_name_plot)
        
        
        
# --------------------------------Side-View---------------------------------
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(x*1e6,z*1e6,np.transpose(E2_sideview),shading = 'gouraud',cmap = 'jet')        
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("z (um)")
        plt.title('Side-view (xz)')
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_WGTAPER_DIRECTORY_WRITE[2], "E_profile_xz.png")
        plt.savefig(file_name_plot)
        
    
# --------------------------------Cross-View---------------------------------

        fig, ax = plt.subplots(figsize=(512*px, 256*px))
        cmap = ax.pcolormesh(y*1e6,z*1e6,np.transpose(E2_crossection),shading = 'gouraud',cmap = 'jet')        
        fig.colorbar(cmap)
        plt.xlabel("y (um)")
        plt.ylabel("z (um)")
        plt.title('Cross-Section (yz)')
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_WGTAPER_DIRECTORY_WRITE[2], "E_profile_yz.png")
        plt.savefig(file_name_plot)
    
    



    


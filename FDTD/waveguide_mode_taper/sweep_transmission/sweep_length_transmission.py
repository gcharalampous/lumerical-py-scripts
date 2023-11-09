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
from config import *
import matplotlib.pyplot as plt

from FDTD.waveguide_mode_taper.waveguide_taper_render import waveguide_taper_draw  
from FDTD.waveguide_mode_taper.user_inputs.user_simulation_parameters import *  
from FDTD.waveguide_mode_taper.user_inputs.user_materials import *
from FDTD.waveguide_mode_taper.user_inputs.user_sweep_parameters import *    
from FDTD.waveguide_mode_taper.fdtd_region import add_fdtd_region



def sweepWidth(fdtd, wg_taper_length_array, tl):
    
    fdtd.switchtolayout()    
    fdtd.selectall()
    fdtd.delete()
    fdtd.redrawoff()
    taper_length = wg_taper_length_array[tl]
    waveguide_taper_draw(fdtd,taper_length, wg_width_right)
    add_fdtd_region(fdtd,taper_length)    
    
      
    # alpha = (wg_width_left - wg_width_right)/pow(taper_length,m)
    # xspan = np.linspace(0, taper_length, poly_res)
    # yspan = alpha * pow((taper_length - xspan),m) + wg_width_right

    # V = np.zeros((2*poly_res,2))

    # for x in range(0,len(xspan)):
    #     V[x][0] = xspan[x]
    
    #     V[x][1] = -yspan[x]/2
        
    # xspan_r = np.flip(xspan, axis=0)
    # yspan_r = np.flip(yspan, axis=0)
    
    # for x in range(len(xspan),2*len(xspan)):
    #     V[x][0] = xspan_r[x-len(xspan)]
    #     V[x][1] = yspan_r[x-len(xspan)]/2

    # fdtd.setnamed("taper","vertices",V)

    # #time.sleep(5)
    
    
    fdtd.run()
    trans_f = (fdtd.getresult("monitor_exp","expansion for input").get("T_forward"))
    trans_t = (fdtd.getresult("monitor_exp","expansion for input").get("T_total"))    
    return trans_f, trans_t




    
if(__name__=="__main__"):

    trans_f_=[]
    trans_t_=[]

    
    with lumapi.FDTD() as fdtd:

        fdtd.save(os.path.join(FDTD_WGTAPER_DIRECTORY_WRITE_FILE, 
                               FDTD_WGTAPER_FILENAME))
   

        wg_taper_length_array = []
        wg_taper_length_array = np.arange(wg_taper_start, wg_taper_stop, wg_taper_step) 





        for tl in range(0,len(wg_taper_length_array)):

            # Sweeps through the waveguide widths, and calculates the transmission
            trans_f, trans_t = sweepWidth(fdtd, wg_taper_length_array, tl)
            trans_f_.append(trans_f)
            trans_t_.append(trans_t)
            

            trans_f_array = np.squeeze(trans_f_)   
            trans_t_array = np.squeeze(trans_t_)

        plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        plt.plot(wg_taper_length_array*1e6,trans_f_array,'-o',label = mode_source)
        plt.legend()           

        plt.xlabel("Taper Length (um)")
        plt.ylabel("T")
        plt.title("thickness "+ str(wg_thickness*1e6) + " um") 
        plt.show()    
        file_name_plot = os.path.join(FDTD_WGTAPER_DIRECTORY_WRITE[0], "sweep_length.png")
        plt.savefig(file_name_plot)
        
        fdtd.redrawon()





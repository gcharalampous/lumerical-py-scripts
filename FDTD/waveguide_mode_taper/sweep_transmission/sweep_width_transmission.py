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



def sweepWidth(fdtd, wg_width_array, wd):
    
    fdtd.switchtolayout()    
    fdtd.redrawoff()
    
    wg_width_right = wg_width_array[wd]
    
    
    fdtd.switchtolayout()    
    fdtd.selectall()
    fdtd.delete()
    fdtd.redrawoff()
    waveguide_taper_draw(fdtd,taper_length, wg_width_right)
    add_fdtd_region(fdtd,taper_length)    
    
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
   
  
        wg_width_array = []
        wg_width_array = np.arange(wg_width_start, wg_width_stop, wg_width_step) 





        for wd in range(0,len(wg_width_array)):

            # Sweeps through the waveguide widths, and calculates the transmission
            trans_f, trans_t = sweepWidth(fdtd, wg_width_array, wd)
            trans_f_.append(trans_f)
            trans_t_.append(trans_t)
            

            trans_f_array = np.squeeze(trans_f_)   
            trans_t_array = np.squeeze(trans_t_)

        plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)        
        plt.plot(wg_width_array*1e6,trans_t_array,label = 'Total Transmission')
        
        plt.plot(wg_width_array*1e6,trans_f_array,'-o',label = mode_source)

        plt.legend()           
        plt.xlabel("width (um)")
        plt.ylabel("T")
        plt.title("thickness "+ str(wg_thickness*1e6) + " um") 
        plt.tight_layout()
        file_name_plot = os.path.join(FDTD_WGTAPER_DIRECTORY_WRITE[0], "sweep_width.png")
        plt.savefig(file_name_plot)
        plt.show()    

        fdtd.redrawon()





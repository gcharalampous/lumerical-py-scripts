#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts sweeps the radius of the waveguide and calculates the transmission
of the fundamental mode.
"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

"""
No user-inputs are required.

The scripts sweeps the width of the waveguide and calculates the effective
index for the TE Mode.

"""

#----------------------------------------------------------------------------
# Imports from user files
# --

import numpy as np
import lumapi
import matplotlib.pyplot as plt
import pandas as pd
import os 
import sys 

sys.path.append("..")


from user_inputs.user_sweep_parameters import *    

cur_path = os.path.dirname(__file__)
filename = "waveguide_bend.lms"



    
waveguide_constructor = 'waveguide-constructor'

file_path = os.path.relpath('..\\user_inputs\\lumerical_files\\'+filename, cur_path)
    
    

fdtd = lumapi.FDTD(file_path)
fdtd.redrawoff()


bend_radius_array = np.arange(bend_radius_start,bend_radius_stop,bend_radius_step)
trans_f=[]
trans_t=[]



for rad in range(0,len(bend_radius_array)):
    print("Loop: " + str(rad))
    fdtd.switchtolayout()    
    fdtd.setnamed(waveguide_constructor,"bend_radius",bend_radius_array[rad])
    fdtd.save()
    fdtd.run()
    trans_f.append(fdtd.getresult("monitor_exp","expansion for T").get("T_forward"))
    trans_t.append(fdtd.getresult("monitor_exp","expansion for T").get("T_total"))

    

trans_f_array = np.squeeze(trans_f)   
trans_t_array = np.squeeze(trans_t)


plt.plot(bend_radius_array*1e6,trans_t_array,bend_radius_array*1e6,trans_f_array)
plt.ylabel('Transmission')
plt.xlabel('Radius')
plt.legend(['Total','Fundamental'])
fdtd.redrawon()
fdtd.close()


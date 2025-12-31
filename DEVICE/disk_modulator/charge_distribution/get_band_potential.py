#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------

import lumapi
import matplotlib.pyplot as plt
import heapq

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

from DEVICE.pin_modulator.user_inputs.user_simulation_parameters import *  
from DEVICE.pin_modulator.user_inputs.user_materials import *  
from DEVICE.pin_modulator.waveguide_render import waveguide_draw
from DEVICE.pin_modulator.charge_region import add_charge_region
from config import *



def find_closest_value(array, target):
    
    closest_value = min(array, key=lambda x: abs(x - target))
    return closest_value


def getDCVbi(device):

    Ei = device.getdata("CHARGE", "bandstructure","Ei")
    Vbi= np.max(Ei) - np.min(Ei)
    return Vbi



def getJunctionWidth(device):
    
    band = device.getresult("CHARGE::band_monitor", "bandstructure")
    
    Ec = np.squeeze((band["Ec"]))
    Ec_gradient = np.gradient(Ec) # Find max and minimum of Ec
    x = np.squeeze((band["x"]))
    
    mid = int(len(x)/2)
    
    min_values = min(Ec_gradient[:(mid)])
    index = np.where(Ec_gradient == min_values)
    W_max99 = x[index]
       
    min_values = min(Ec_gradient[(mid):])
    index = np.where(Ec_gradient == min_values)
    W_min99 = x[index]   
    
    
       
    

    junction_width = abs(W_max99 - W_min99)
    
    return junction_width, W_max99, W_min99, Ec, x



if(__name__=="__main__"):
    with lumapi.DEVICE(hide=True) as device:
        

        # Draw the waveguide structure using a custom function
        device.redrawoff()
        waveguide_draw(device)
        
        # Draw the Simulation Region
        add_charge_region(device)
        
        # Save and Run
        device.save(PIN_MODULATOR_DIRECTORY_WRITE_FILE + "\\pin_waveguide_simulation.ldev")
        
        device.run()
        
        Vbi = getDCVbi(device)        
        print("Built in Voltage is " + str(Vbi)+ " eV")
        
        junction_width, W_max99, W_min99, Ec, x = getJunctionWidth(device)
        print("Junction Width is " + str(junction_width)+ " V")
        
        plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        plt.plot(x*1e6,Ec)
        plt.axvline(x = W_max99*1e6, color = 'r',  linestyle = '--') 
        plt.axvline(x = W_min99*1e6,  color = 'r', linestyle = '--') 
        
        plt.xlabel("x (\u00B5m)")
        plt.ylabel("$E_c$ (eV)")
        plt.grid()
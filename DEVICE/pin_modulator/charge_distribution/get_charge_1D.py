#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------

"""
No user-inputs are required.

"""


import lumapi
import matplotlib.pyplot as plt



#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

from DEVICE.pin_modulator.user_inputs.user_simulation_parameters import *  
from DEVICE.pin_modulator.user_inputs.user_materials import *  
from DEVICE.pin_modulator.waveguide_render import waveguide_draw
from DEVICE.pin_modulator.charge_region import add_charge_region
from config import *



def get_charge_1D (device):


        

        charge_result = device.getresult("CHARGE::charge_monitor","charge")
        x = np.squeeze(charge_result['x'])
        n = np.squeeze(charge_result['n'])
        p = np.squeeze(charge_result['p'])
        # n = device.getdata("CHARGE::charge_monitor","charge","n")
        # p = device.getdata("CHARGE::charge_monitor","charge","p")
        
        return x, n, p
        
        
        
if(__name__=="__main__"):
    with lumapi.DEVICE(hide=True) as device:
        
        # Draw the waveguide structure using a custom function
        device.redrawoff()
        waveguide_draw(device)
        
        # Draw the Simulation Region
        add_charge_region(device)
        
        
        # Save and Run
        device.setnamed("CHARGE::charge_monitor","monitor type", 2)
        device.save(PIN_MODULATOR_DIRECTORY_WRITE_FILE + "\\pin_waveguide_simulation.ldev")        
        device.run()
        
        # Get the charge
        x, n, p = get_charge_1D(device)
        
        
        
        plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        plt.semilogy(x*1e6, n, label = 'ND')
        plt.semilogy(x*1e6, p, label = 'NA')
        plt.minorticks_on
        plt.legend()

        plt.xlabel("x (\u00B5m)")
        plt.ylabel("Charge (cm$^{-3}$)")
        plt.grid(True, 'both')

        plt.savefig(PIN_MODULATOR_DIRECTORY_WRITE[0] + "\\charge_distrigution.png")


        
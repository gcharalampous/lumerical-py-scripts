#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------

import lumapi
import matplotlib.pyplot as plt



#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

from DEVICE.pin_modulator.analytical_calculations.capacitance_analytical import capDCanalytical
from DEVICE.pin_modulator.user_inputs.user_simulation_parameters import *  
from DEVICE.pin_modulator.user_inputs.user_materials import *  
from DEVICE.pin_modulator.user_inputs.user_sweep_parameters import *
from DEVICE.pin_modulator.waveguide_render import waveguide_draw
from DEVICE.pin_modulator.charge_region import add_charge_region
from config import *


def voltage_sweep(device, v_anode_start,v_anode_stop,v_num_pts):

    configuration = (

    ("CHARGE::boundary conditions::anode",
             (("bc mode", "steady state"),
              ('sweep type', 'range'),
              ('range start', v_anode_start),
              ('range stop', v_anode_stop),
              ('range num points', v_num_pts),
              ("surface type", "solid"),
              ("solid", "metal_anode"))),
              
    
    ("CHARGE::boundary conditions::cathode",
             (("bc mode", "steady state"),
              ('sweep type', 'single'),
              ('voltage', 0),
              ("surface type", "solid"),
              ("solid", "metal_cathode"))),
    
    
    ("CHARGE",
             (("norm length", norm_length),
              ('solver type', 'newton'))),
    
    
    ("CHARGE::charge_monitor",
             (("monitor type", 7),
              ("integrate total charge", 1),
              ("save data", True),
              ("filename","charge_sweep.mat"))),
    
    
    )
    
    

    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               device.setnamed(obj, k, v)
               
               
if(__name__=="__main__"):
    with lumapi.DEVICE(hide=True) as device:
    
        
        # Draw the waveguide structure using a custom function
        device.redrawoff()
        waveguide_draw(device)
        
        # Draw the Simulation Region
        add_charge_region(device)
        
        
        
        # Load voltage sweep range from user_sweep_parameters
        voltage_sweep(device, v_anode_start, v_anode_stop, v_num_pts)
        
        # Save and Run
        device.save(PIN_MODULATOR_DIRECTORY_WRITE_FILE + "\\pin_waveguide_simulation.ldev")
        
        device.run()
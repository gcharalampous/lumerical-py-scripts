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
from DEVICE.pin_modulator.dc_sweep.voltage_sweep import voltage_sweep
from DEVICE.pin_modulator.user_inputs.user_simulation_parameters import *  
from DEVICE.pin_modulator.user_inputs.user_materials import *  
from DEVICE.pin_modulator.user_inputs.user_sweep_parameters import *
from DEVICE.pin_modulator.waveguide_render import waveguide_draw
from DEVICE.pin_modulator.charge_region import add_charge_region
from config import *



epsilon0 = 8.854187817620e-12               # [F/m]
epsilon_s = 11.8                            # Si Relative Dielectric constant
q = 1.60217646e-19                          # Electronic charge [Coulumbs]



def getDCResistance(device):
    
    cathode_result = device.getresult("CHARGE","cathode")
    V_c = cathode_result["V_cathode"]
    i_c = cathode_result["I"]
    
    anode_result = device.getresult("CHARGE","anode")
    V_a = anode_result["V_anode"]
    i_a = anode_result["I"]


    R = abs((V_a) - (V_c))/(abs(i_a))
    
    return R, V_a, i_a


def getDCCapacitance(device):

        # Charge Desity

        Q = device.getresult("CHARGE::charge_monitor","total_charge");

        V_a = np.squeeze(Q["V_anode"])
        Qn = np.squeeze(Q["n"])
        Qp = np.squeeze(Q["p"])
        
        dQn = np.gradient(Qn)*q
        dQp = np.gradient(Qp)*q
        
        dV = V_a[1] - V_a[0]

        Cn = dQn/dV     # F/m
        Cp = dQp/dV     # F/m





        return Cn, Cp, V_a,


def getDCVbi(device):
    
    Ei = device.getdata("CHARGE", "bandstructure","Ei")
    Vbi= np.max(Ei) - np.min(Ei)
    
    return Vbi


if(__name__=="__main__"):
    with lumapi.DEVICE() as device:
    
        
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
        
        R, V_a, i_a = getDCResistance(device)
        Cn, Cp, V_a  = getDCCapacitance(device)
        
        
        
        
        # Theoretical Calcualtion
        Cj = capDCanalytical()
        


              
                
        plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        plt.grid(visible=True, which='both')   
        plt.semilogy(V_a,R*1e-3,'-')
        plt.xlabel("Voltage (V)")
        plt.ylabel("Resistance ($k\\Omega \\cdot \\mu m$)")
        plt.tight_layout()
        file_name_plot = os.path.join(PIN_MODULATOR_DIRECTORY_WRITE[1], "Resistance_DC.png")
        plt.savefig(file_name_plot)
        
                
        
        plt.figure(2, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        C_static = 0.5*(Cn+Cp)  # F/m

        
        plt.semilogy(V_a,C_static*1e15*1e-6,'-', label='Cstatic')
        

        plt.hlines(Cj*1e15*1e-6, xmin=min(V_a), xmax = 0, color='r', linestyle='--', 
                    label='Theoretical')
               
        
        plt.legend()
        plt.xlabel("Voltage (V)")
        plt.ylabel("Capacitance ($fF~/~\\mu m$)")
        plt.grid(which='both')   
        plt.tight_layout()

        file_name_plot = os.path.join(PIN_MODULATOR_DIRECTORY_WRITE[1], "Capacitance_DC.png")
        plt.savefig(file_name_plot)


        Lrt = 25e-6
        C_static_array = np.squeeze(C_static)
        R_array = np.squeeze(R)
        tau = (R_array*norm_length/Lrt) * (C_static_array*Lrt)  
        f_3dB = 1/(2*np.pi*tau)

        plt.figure(3, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        plt.semilogy(V_a,f_3dB*1e-6)
        plt.grid(True, which='major')   
        plt.xlabel("$Voltage (V)$")
        plt.ylabel("3-dB Bandwidth (MHz)")
        
        plt.figure(4, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        plt.plot(V_a,i_a*(Lrt/norm_length)*1e3,'-', label='Cn')
        plt.grid(True, which='both')   
        plt.xlabel("Voltage (V)")
        plt.ylabel("Current (mA)")
        
        
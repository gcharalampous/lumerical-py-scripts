# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 09:53:18 2023

@author: Lab
"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------


import numpy as np
from DEVICE.pin_modulator.user_inputs.user_materials import Nnn, Ppp  
from DEVICE.pin_modulator.user_inputs.user_sweep_parameters import *
from DEVICE.pin_modulator.user_inputs.user_simulation_parameters import wg_thickness  
from DEVICE.pin_modulator.user_inputs.user_simulation_parameters import *  





def capDCanalytical():

    # CONSTANTS
    epsilon0 = 8.854187817620e-12               # [F/m]
    epsilon_s = 11.8                            # Si Relative Dielectric constant
    q = 1.60217646e-19                          # Electronic charge [Coulumbs]
    kB = 1.3806503e-23                          # Boltzmann Constant in J/K
    h = 4.135e-15                               # Plank’s constant [eV-s]
    m_0 = 9.11e-31                              # Electron Mass [kg]
    m_n = 1.08*m_0                              # Density-of-states effective 
                                                        # mass for electrons
    m_p = 1.15*m_0                              # Density-of-states effective 
                                                        # mass for holes
    Eg=1.1242                                   # Si Band-gap [eV]
    pi = np.pi
    # --------------------------------------------------------------------------

    ND = Nnn;
    NA = Ppp

    
    # T = T+273.15                            # Temperature [K]
    # VT = kB*T/q                             # Thermal Voltage
    
    # Nc = ( 2*(2*pi*m_n*(kB/q)*T/h**2)**     # Effective Density of states Conduction Band
    #     (3/2)/(q)**(3/2) )
    
    # Nv = ( 2*(2*pi*m_p*(kB/q)*T/h**2)**     # Effective Density of states Valence Band
    #     (3/2)/(q)**(3/2) )
    
    
    # ni = ( np.sqrt(Nc*Nv)*
    #     np.exp(-Eg/(2*(kB/q)*T)) )          # intrinsict charge carriers in m^-3
    
    # Vbi = VT*np.log(NA*ND/ni**2)            # Built-in or Diffusion Potential
    
    
    # Cj = np.sqrt(q*epsilon0*epsilon_s/2/(1/ND+1/NA)/(Vbi-V))*h_rib
    
    
    d = offset_Ppp + offset_Nnn
    
    Cj = ((epsilon0*epsilon_s)*metal_anode_width)/d
    
    return Cj


if(__name__=="__main__"):


    T = 25
    V = np.linspace(v_anode_start, v_anode_stop, v_num_pts) 
    V = V[V<=0]
    h_rib = wg_thickness


    Cj = capDCanalytical()
    
    
    print('Capacitance (pF)',Cj*1e12 )


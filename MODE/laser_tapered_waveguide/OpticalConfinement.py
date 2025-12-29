# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 09:41:30 2023

@author: Georgios
"""

import lumapi
import numpy as np
from scipy import integrate


def optical_confinement(mode,structure,mode_order):

    m=mode_order
    
    y = []
    z = []
    Ey = []
    Ez = []
    
    x_max = mode.getnamed(structure,"x max")
    x_min = mode.getnamed(structure,"x min")
    y_max = mode.getnamed(structure,"y max")
    y_min = mode.getnamed(structure,"y min")
    z_max = mode.getnamed(structure,"z max")
    z_min = mode.getnamed(structure,"z min")
    
    
    
    x=np.squeeze(mode.getdata("FDE::data::mode"+str(m),"x"))
    y=np.squeeze(mode.getdata("FDE::data::mode"+str(m),"y"))
    
    
    # y_max = max(y)
    # y_min=min(y)
    
    
    # z_max=max(z)
    # z_min=min(z)
    
    neff=(mode.getdata("FDE::data::mode"+str(m),"neff"))
    
    Ex=np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Ex"))
    Ey=np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Ey"))
    Ez=np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Ez"))
    E = np.transpose(np.sqrt(Ex**2 + Ey**2 + Ez**2))
    
    
    Hx=np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Hx"))
    Hy=np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Hy"))
    Hz=np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Hz"))
    H = np.transpose(np.sqrt(Hx**2 + Hy**2 + Hz**2))
    
    
    Px = (Ey*Hz - Ez*Hy)
    Py = Ez*Hx - Ex*Hz
    Pz = Ex*Hy - Ey*Hx
    
    P = np.real(np.transpose(np.sqrt(Px**2 + Py**2 + Pz**2)))
    
    
    
    
    
    X, Y = np.meshgrid(x, y)
    
    
    
    filter = (X<x_max) & (X>x_min)
    filter = filter & (Y<y_max) & (Y>y_min);
    
    
    
    
    
    
    # Poynting Vector
    P1 = integrate.simpson(integrate.simpson(P*filter, x, axis=0), y, axis=0)
    P2 = integrate.simpson(integrate.simpson(P, x, axis=0), y, axis=0)
    
    
    power = (P1/P2)
    print("Core y-span: " + str(y_max - y_min))
    print("Core z-span: " + str(z_max - z_min))
    print("Confinement Factor: " + str(power) + "\n")    
    return power
    
    

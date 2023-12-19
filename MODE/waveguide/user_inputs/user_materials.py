#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------

import numpy as np
from MODE.waveguide.user_inputs.user_simulation_parameters import wavelength

"""
User-inputs are required.

Input the appropriate material for each structure as appears below 


                    +--------------------------------+                          
                    |           Claddding            |                          
                    |                                |                        
                    |         +-----------+          |                          
                    |         |           |          |                          
                    |         | waveguide |          |                          
                    |         |           |          |                          
                    +--------------------------------+                          
                    |               Box              |                          
                    +--------------------------------+                          
                    |                                |                          
                    |           Substrate            |                          
                    |                                |                          
                    +--------------------------------+                          

                                                                               
Select between material model or material index. By selecting the variable  
'is_clad_index = True' the material model will be ingonred and instead the 
cladding_index = 1 cladding index 1 will be set.


Please make sure that you type the material model exactly as it is in the material 
database.

"""

# Cladding
is_clad_index = True                            # If true ignore clad_material
clad_material = "SiO2 (Glass) - Palik"
clad_index = 1.5362


# Waveguide Core
is_wg_index = True
wg_material = "Si (Silicon) - Palik"
wg_index = 3.4777


# Waveguide Slab
is_slab_index = True                              # If true ignore wg_material
slab_material = "Si (Silicon) - Palik"
slab_index = 3.4777


# Box
is_box_index = True
box_material = "SiO2 (Glass) - Palik"
box_index = 1.5362


# Substrate
is_sub_index = False                            # If true ignore sub_material
sub_material = "Si (Silicon) - Palik"
sub_index = 3.4777



## ------ Doping
N=5e19                                          # N++ 
P=1e20                                          # P++

# -------------------------- End of Input Section -----------------------------


if(is_wg_index):
    wg_material = "<Object defined dielectric>"
else:
    wg_material = wg_material
    
if(is_slab_index):
    slab_material = "<Object defined dielectric>"
else:
    slab_material = slab_material
    
if(is_clad_index):
    clad_material = "<Object defined dielectric>"
else:
    clad_material = clad_material
   
if(is_box_index):
    box_material = "<Object defined dielectric>"
else:
    box_material = box_material
   
if(is_sub_index):
    sub_material = "<Object defined dielectric>"
else:
    sub_material = sub_material

# Calculates the attenulation coefficients [Silicon only]
alphaN_m = 3.52e-6*wavelength**2*N*100
alphaP_m = 2.4e-6*wavelength**2*P*100
# Calculates the extnction coefficients
k_P = wavelength * alphaP_m /4/np.pi;
k_N = wavelength * alphaN_m /4/np.pi;
